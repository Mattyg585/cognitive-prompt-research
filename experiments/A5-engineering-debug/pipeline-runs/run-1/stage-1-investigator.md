## Investigation: Intermittent Order Processing Failures — `order-service` 500s Due to Downstream Timeout Against `inventory-service`

### Reproduction
- **Expected**: Orders placed via `order-service` are processed successfully. The service calls `inventory-service /v2/reserve` to reserve inventory, receives a response within normal latency (p50 ~40ms, p99 ~200ms), and completes the order.
- **Actual**: Approximately 15% of orders fail with `500 Internal Server Error`. The underlying error is `context deadline exceeded` — the call from `order-service` to `inventory-service /v2/reserve` exceeds the 5000ms timeout. Failures are intermittent: the same user retrying can succeed on a subsequent attempt.
- **Conditions**: Intermittent, not deterministic. Correlates with `inventory-service` tail latency — p99 has ballooned to 4800ms (24x normal). At a 5s timeout, requests landing in the upper tail fail. The ~15% failure rate is consistent with a latency distribution where a significant fraction of requests exceed 5s. The intermittent nature follows directly: each request draws from the same degraded latency distribution, so identical requests sometimes complete (landing in the body of the distribution) and sometimes don't (landing in the tail).

### Isolation
- **Affected component(s)**: The failure path is `order-service` -> `inventory-service` -> PostgreSQL (RDS). The bottleneck is at the RDS layer. `inventory-service` itself is not computationally overloaded — it's waiting on the database. `order-service` is functioning correctly; it's a victim of downstream latency.

- **Timeline**:
  - **00:15 UTC**: `inventory-sync-lambda` begins execution (CloudWatch). This is the nightly scheduled sync job from the warehouse system.
  - **~00:30 UTC**: Order failures begin. This is approximately 15 minutes after the Lambda started — consistent with the Lambda accumulating database load that crosses a tipping point.
  - **02:47 UTC**: Error rate crosses alert threshold, on-call engineer paged.
  - **02:47 UTC (ongoing)**: Lambda is still running. It normally completes in ~10 minutes. It has now been running for over 2.5 hours.

- **What changed**:
  - **Root timeline event**: `inventory-sync-lambda` started at 00:15 and has not completed. It normally finishes in ~10 minutes. Something about tonight's run is causing it to run 15x+ longer than usual — either a larger dataset from the warehouse system, a query plan regression, or a runaway loop.
  - **3 days ago**: `order-service` request timeout was increased from 3s to 5s. This change is not causal but is load-relevant: by allowing requests to wait longer before timing out, it increases the duration that `order-service` holds connections to `inventory-service`, and that `inventory-service` holds connections/queries against the database. Under contention, longer timeouts can paradoxically make things worse by keeping resources occupied longer — the longer timeout is masking some failures (some requests that would have failed at 3s now succeed at 4.5s) but also increasing connection pressure on the already-saturated database.
  - **3 weeks ago**: `inventory-sync-lambda` was deployed by the warehouse team. It has been running nightly for ~3 weeks without apparent incident, meaning tonight's failure is not from the Lambda's existence but from a change in its workload or execution characteristics tonight specifically.

- **Resource state**:
  - **RDS CPU**: 92% (normal baseline: 25%). This is severe — the database is compute-saturated.
  - **RDS active connections**: 185 (normal baseline: 40). This is 4.6x normal. The connection increase comes from two sources: the Lambda holding connections for its long-running sync, and `inventory-service` connections that are now held longer because queries take longer (the convoy effect — slow queries hold connections, new requests queue or open new connections, further saturating the database).
  - **RDS read IOPS**: Normal. This is a significant data point. The database is CPU-bound, not I/O-bound. This points toward compute-expensive queries (full table scans, complex joins, lock contention, row-level locking with heavy scanning) rather than simple read volume.
  - **`inventory-service` latency**: p50 = 180ms (4.5x normal), p99 = 4800ms (24x normal). Both are elevated but the tail is disproportionately affected, which is characteristic of resource contention — most requests complete with moderate delay, but under contention, some requests get stuck behind expensive operations and wait much longer.
  - **Restarting `inventory-service` pods had no effect**: This confirms the problem is not in `inventory-service` itself (no memory leak, no stuck goroutines, no local state issue). The problem is downstream in the shared database.

### Hypotheses

#### Hypothesis 1: Runaway `inventory-sync-lambda` Is Saturating the Shared RDS Instance
**Statement**: The `inventory-sync-lambda` is executing an abnormally long sync operation tonight, consuming excessive CPU and connections on the shared RDS instance. This resource contention degrades `inventory-service` query performance, causing tail latencies to exceed `order-service`'s 5s timeout.

**Supporting evidence**:
- The Lambda started at 00:15. Failures started at ~00:30. The temporal correlation is tight — 15 minutes is consistent with a ramp-up period as the Lambda's workload saturates database resources.
- The Lambda is still running after 2.5+ hours vs. its normal 10-minute completion time. Something is fundamentally different about tonight's execution.
- RDS CPU is at 92% (normal 25%). Active connections are at 185 (normal 40). Both indicate a major new consumer of database resources.
- The Lambda connects to the same RDS instance as `inventory-service` — confirmed shared resource.
- Read IOPS are normal despite CPU being at 92%, suggesting the Lambda is running CPU-intensive queries (complex aggregations, large sorts, or heavy row-level lock contention) rather than just high-volume reads.
- Restarting `inventory-service` pods had no effect — consistent with the problem being in the shared database, not in `inventory-service`.

**Contradicting evidence**: None identified. All available evidence is consistent with this hypothesis.

**Unresolved**:
- What is different about tonight's Lambda execution? Possibilities: larger dataset from warehouse (more SKUs, a bulk import, a full re-sync vs. incremental), a query plan regression due to stale statistics, or a schema/data change in the warehouse source. The Lambda's CloudWatch logs would reveal what it's doing and why it's slow.
- What specific queries is the Lambda running? RDS Performance Insights or `pg_stat_activity` would show the active queries, their duration, and whether they're holding locks.
- Is the Lambda stuck (deadlocked, waiting on a lock) or actively working (burning CPU on legitimate but slow work)? This distinction matters for understanding whether it will eventually complete or run indefinitely.
- How many connections is the Lambda itself holding? This would quantify its direct contribution to the connection count increase.

#### Hypothesis 2: Database Lock Contention Between Lambda and `inventory-service`
**Statement**: The `inventory-sync-lambda` is writing to inventory tables while `inventory-service /v2/reserve` also writes to those same tables (reserving inventory). PostgreSQL row-level or table-level locks from the Lambda's sync operations are blocking `inventory-service`'s reservation queries, causing them to wait rather than execute.

**Supporting evidence**:
- The Lambda syncs inventory counts — it writes to inventory data. The `/v2/reserve` endpoint reserves inventory — it also writes to inventory data. These operations plausibly contend on the same rows or tables.
- CPU at 92% with normal read IOPS is consistent with lock contention: the database spends CPU on lock management and query planning/reprocessing rather than on I/O.
- The disproportionate p99 blowup (24x vs. p50's 4.5x) is characteristic of lock contention: most queries acquire locks quickly, but some unlucky requests hit a locked row and wait for the Lambda's transaction to release it.
- The intermittent failure pattern is consistent with lock contention: requests that hit non-contended rows succeed quickly; requests that hit rows the Lambda is currently modifying wait and may timeout.

**Contradicting evidence**: None identified. This hypothesis is compatible with Hypothesis 1 and may be the specific mechanism within it.

**Unresolved**:
- What isolation level is the Lambda using? Long-running transactions at SERIALIZABLE or REPEATABLE READ would hold locks for the entire transaction duration, which could be hours given the Lambda's abnormal runtime.
- Is the Lambda executing as a single large transaction or many small ones? A single large transaction holding locks on thousands of inventory rows for 2.5 hours would cause severe contention. Many small transactions would cause intermittent contention but release locks frequently.
- `pg_stat_activity` and `pg_locks` would confirm whether `inventory-service` queries are in a `waiting` state and what they're waiting on.

#### Hypothesis 3: Connection Pool Exhaustion on RDS
**Statement**: The combination of the Lambda's connections and degraded query times for `inventory-service` has pushed the RDS instance toward its connection limit, causing connection acquisition failures or queuing that manifests as timeouts.

**Supporting evidence**:
- Active connections are at 185 vs. normal 40 — a 4.6x increase.
- `db.r6g.xlarge` has 4 vCPUs and 32 GB memory. The default `max_connections` for RDS PostgreSQL on this instance class is typically around 400-800 depending on configuration. At 185, we may not be at the hard limit, but connection overhead contributes to CPU load.
- The 3-day-old timeout increase from 3s to 5s means `inventory-service` connections are held ~67% longer on average during degraded performance, compounding the connection pressure.

**Contradicting evidence**:
- 185 connections is elevated but likely below the RDS max_connections limit for this instance class, suggesting we haven't hit a hard connection ceiling.
- The error is `context deadline exceeded` (timeout), not a connection refused or connection pool exhaustion error. This suggests the problem is query execution time, not connection acquisition.

**Unresolved**:
- What is the configured `max_connections` on this RDS instance?
- What connection pool settings does `inventory-service` use? If it has a pool max of, say, 20 per pod (x4 pods = 80), and the Lambda holds 50+, the combined count is explained. But if `inventory-service` connections are timing out and being replaced, the pool churn adds overhead.

### Root Cause Analysis

**Root cause**: The shared PostgreSQL RDS instance is being saturated by the `inventory-sync-lambda`, which is running anomalously long tonight (2.5+ hours vs. normal 10 minutes). The Lambda and `inventory-service` share the same database, and there is no resource isolation between them — no separate connection pools, no query prioritisation, no resource governor. The database is a shared commons with no protection against one consumer degrading all others. The system has been running this way for 3 weeks since the Lambda was introduced, but tonight's Lambda execution is abnormal (likely due to a larger dataset, a full re-sync, or a query plan regression), and the shared-resource architecture has no capacity to absorb the spike.

**Proximate trigger**: Whatever caused tonight's `inventory-sync-lambda` execution to diverge from its normal 10-minute runtime — likely a change in the volume or shape of data from the warehouse system. This needs to be confirmed from the Lambda's logs and the warehouse system's state.

**Contributing factors**:
- The timeout increase from 3s to 5s (3 days ago) is making the situation worse than it would otherwise be. Under contention, longer timeouts keep database connections occupied longer, increasing connection counts and adding to CPU pressure. At the original 3s timeout, more `order-service` requests would fail faster, but the database would face less connection load from `inventory-service`. This is the classic tradeoff: the longer timeout increases individual request success probability but increases system-wide resource pressure.
- No connection limit or resource isolation for the Lambda on the shared database. The Lambda was introduced by a separate team and likely has no connection pooling or concurrency controls appropriate for a shared production database.
- No monitoring or alerting on the Lambda's runtime duration. It has been stuck for 2.5 hours without any alert — the alert that fired was on `order-service` error rate, not on the actual source of the problem.

**Confidence**: High confidence that the Lambda's abnormal execution is the cause of the RDS saturation, and that RDS saturation is the cause of `inventory-service` latency degradation, and that `inventory-service` latency degradation is the cause of `order-service` timeouts. The causal chain is well-supported by the timeline, the resource metrics, and the shared-resource architecture. The specific mechanism within the database (CPU-bound query execution vs. lock contention vs. both) is not confirmed and would require `pg_stat_activity` / `pg_locks` / Performance Insights data.

**Blast radius**:
- Any other service that queries this RDS instance is experiencing the same degradation. The investigation should determine whether other services connect to this database.
- If the Lambda is performing writes in a long-running transaction, there is a risk of transaction ID wraparound pressure or bloat in the affected tables, which would cause ongoing performance degradation even after the Lambda completes.
- If the Lambda is stuck (not just slow), it may not self-resolve. Manual intervention to stop the Lambda may be necessary to restore database performance.
- Orders that failed with 500s during this incident may need reconciliation — customers may have been charged (if payment is processed before inventory reservation) without receiving order confirmations, or may have retried and created duplicate orders.
- The 3-week window since the Lambda was introduced represents 3 weeks of nightly runs that succeeded. If tonight's failure is data-volume-driven, it will recur whenever the warehouse dataset crosses the threshold that makes the Lambda's queries expensive. This is a latent instability, not a one-time event.

### Information Gaps

The following data would strengthen or revise this analysis:

1. **`inventory-sync-lambda` CloudWatch logs**: What queries is it running? What data volume is it processing tonight vs. previous nights? Is it making progress or stuck?
2. **RDS `pg_stat_activity`**: What queries are currently running, how long have they been running, and are any in a `waiting` state?
3. **RDS `pg_locks`**: Are there blocking locks? What's holding them?
4. **RDS Performance Insights**: Top SQL by CPU, top SQL by waits, active sessions breakdown.
5. **Lambda connection count**: How many connections is the Lambda holding to the database?
6. **RDS `max_connections` setting**: How close to the hard limit is the current 185?
7. **Other consumers of this RDS instance**: What else connects to this database besides `inventory-service` and the Lambda?
8. **Warehouse system state**: Did the data volume or shape change tonight? Was there a bulk import, a full catalog refresh, or a schema change?
9. **Previous Lambda execution logs**: Runtime and resource consumption on previous nights for comparison.
10. **`inventory-service` connection pool configuration**: Max pool size, timeout settings, queue depth.
