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
## Fix Proposal: Order Processing Failures from Shared-Database Saturation by Uncontrolled Batch Job

### Immediate Mitigation

The system is actively degraded. The `inventory-sync-lambda` has been running for 2.5+ hours against a shared production database, saturating it at 92% CPU and causing 15% order failures. Two actions to stop the bleeding:

**1. Kill the runaway Lambda execution.**

Invoke the Lambda's stop/cancel mechanism (or terminate it via the AWS console / CLI). The Lambda is not completing its work productively — it's been running 15x longer than normal. Stopping it will release its database connections and CPU-intensive queries, allowing `inventory-service` latency to recover. Before killing it, capture its current state from CloudWatch logs and `pg_stat_activity` for post-incident analysis.

If the Lambda is mid-transaction, killing it will cause PostgreSQL to roll back the transaction. On a heavily loaded RDS instance at 92% CPU, rollback of a large transaction can itself be expensive — monitor RDS CPU and connection counts after the kill to confirm recovery. If the Lambda is running many small transactions, rollback cost will be negligible.

**2. Revert the timeout increase on `order-service` from 5s back to 3s.**

This is counterintuitive — won't a shorter timeout cause *more* failures? Under normal conditions, yes. Under database contention, no. The 5s timeout is actively making the contention worse: every request that hangs for 4.5s before succeeding holds a database connection for 4.5s instead of failing at 3s and releasing it. The longer timeout increases the steady-state connection count against the database, deepening the resource pressure. Reverting to 3s will cause some marginal requests to fail that would have scraped through at 5s, but it will reduce the connection load on the database, improving latency for all other requests. This is the correct tradeoff during contention.

This revert should happen *after* killing the Lambda. If the Lambda kill restores database performance to normal (p99 back under 200ms), the timeout revert becomes less urgent — but it should still happen because the 5s timeout creates latent risk for the next contention event.

**3. Order reconciliation.**

Failed orders during the incident window (00:30 - present) need reconciliation. If the payment service processes charges before inventory reservation, some customers may have been charged without receiving order confirmations. If the system allows retries, some customers may have placed duplicate orders. The reconciliation should cross-reference payment records against confirmed orders for the incident window and resolve discrepancies. This is a business operations task, not an engineering fix, but it needs to be initiated now.

### Structural Fix

**What to change**: Isolate the batch workload from the production read/write path at the database layer.

**At what level**: Architecture and Process. This is not a code bug or a configuration knob — it's a missing architectural boundary. Two workloads with fundamentally different resource profiles (low-latency transactional queries vs. long-running bulk sync operations) share a database with no isolation. The fix needs to separate them.

**The fix has three parts:**

**Part 1 — Database resource isolation for the Lambda.**

Create a read replica for the `inventory-sync-lambda` to use for its read-heavy sync operations. The Lambda's job is to sync inventory counts from the warehouse system, which is primarily reading current state and computing deltas. The reads should go to a replica. The writes (applying the sync results) should go to the primary, but through a controlled path:

- The Lambda should use a dedicated database user/role with connection limits enforced at the PostgreSQL level (`ALTER ROLE sync_lambda CONNECTION LIMIT 5`). This prevents the Lambda from consuming unbounded connections regardless of what happens in its execution.
- The Lambda's write operations should be batched into small, bounded transactions — not one giant transaction that holds locks for hours. Each batch should commit independently. If the Lambda is currently running as a single transaction, this is the most important change.
- The Lambda should use `statement_timeout` on its database role (e.g., `ALTER ROLE sync_lambda SET statement_timeout = '30s'`) so that any individual query that runs longer than 30 seconds is killed rather than allowed to saturate the database indefinitely.

**Part 2 — Circuit breaker between `order-service` and `inventory-service`.**

The current architecture has no mechanism for `order-service` to detect that `inventory-service` is degraded and respond differently. It sends every request and waits for timeout. Under sustained degradation, this means every order attempt consumes resources (connections, threads, timeout duration) before failing.

Add a circuit breaker on `order-service`'s call to `inventory-service /v2/reserve`:
- **Closed** (normal): requests flow through.
- **Open** (tripped): after N failures within a window, stop sending requests and fail immediately with a meaningful error ("inventory service temporarily unavailable, please retry shortly") instead of waiting 5s per request to timeout.
- **Half-open**: periodically allow a probe request through to detect recovery.

This doesn't prevent the underlying problem, but it prevents `order-service` from compounding the damage by piling requests onto a degraded downstream, and it gives customers an immediate failure instead of a 5s hang followed by a failure.

**Part 3 — Timeout strategy.**

The 3s-to-5s timeout change was made without analysis of its system-wide effects. The timeout on `order-service`'s call to `inventory-service` should be set based on the *normal* latency distribution with headroom, not increased reactively when requests start timing out. The correct response to requests timing out at 3s is to investigate why latency increased, not to increase the timeout.

Set the timeout to a value that accommodates the normal p99 (200ms) with reasonable headroom — 1s to 1.5s is appropriate. A request that takes more than 1.5s to reserve inventory is already anomalous and indicates a systemic problem that a longer timeout will not solve. Combined with the circuit breaker, this means degradation is detected and surfaced quickly rather than masked.

**Rationale**: The root cause is not a bug — it's a missing architectural boundary. The Lambda and `inventory-service` are operated by different teams with different operational concerns, yet they share a critical resource (the database) with no isolation. The Lambda team had no visibility into the production impact of their batch job, and the `order-service` team had no mechanism to protect against downstream degradation. The fix creates the boundaries that should have existed before the Lambda was introduced: resource limits at the database layer, workload isolation via a replica, and a circuit breaker to contain blast radius.

### Implementation Considerations

**Side effects**:
- Read replica introduces replication lag. The Lambda reading from a replica will see slightly stale data. For an inventory sync job that runs nightly, this is acceptable — the warehouse data it's syncing is already hours old.
- Connection limits on the Lambda's database role will cause the Lambda to fail if it tries to open more than the allowed connections. The Lambda code must handle this gracefully — retry with backoff, or use a connection pool that respects the limit.
- The circuit breaker will cause `order-service` to fail orders *faster* during degradation. This is the intended behaviour, but it changes the failure mode from "slow failure after timeout" to "fast failure with circuit open." Downstream systems and the customer-facing error handling must be aware of this new failure mode.
- Reducing the timeout from 5s to 1-1.5s will cause requests that currently succeed between 1.5s and 5s to fail. Under normal operation (p99 = 200ms), virtually no requests fall in this range. Under degradation, many do — but those requests succeeding at 4s is itself a symptom of the problem, not a feature to preserve.

**Edge cases**:
- If the Lambda legitimately needs to process a very large dataset (e.g., annual full inventory reconciliation), the connection limit and statement timeout may cause it to fail. The Lambda should be designed to handle this gracefully — chunked processing, progress tracking, resumability. Very large syncs should be scheduled during a maintenance window with advance coordination, not run as an unattended nightly job.
- If the read replica falls significantly behind (minutes of lag), the Lambda's sync calculations based on stale data could produce incorrect deltas. The Lambda should check replication lag before proceeding and abort or alert if lag exceeds a threshold.

**Regression risks**:
- The most likely regression is the Lambda failing on its next run due to the new connection limits or statement timeouts. This is a controlled failure — it's better for the Lambda to fail visibly than to succeed silently while degrading production. The Lambda team needs to be informed and prepared to adapt.
- Reducing `order-service` timeout could cause regressions if there are legitimate slow paths in `inventory-service` that currently depend on the 5s timeout. Review `inventory-service` latency data under normal conditions to confirm that 1-1.5s accommodates the normal distribution.

**Dependencies**:
- **Warehouse/Lambda team**: They own `inventory-sync-lambda` and need to implement connection pooling, transaction batching, and the read-replica migration. This is the most significant coordination requirement.
- **Platform/DBA team**: Creating the read replica, configuring the sync role with connection limits and statement timeouts, and potentially reviewing RDS instance sizing.
- **Order-service team**: Implementing the circuit breaker and reverting/adjusting the timeout.
- **Business operations**: Order reconciliation for the incident window.

### Verification

**How to verify the fix works**:
- After killing the Lambda: RDS CPU should drop from 92% toward the 25% baseline within minutes. Active connections should drop from 185 toward 40. `inventory-service` p99 latency should return to the ~200ms range. `order-service` error rate should drop to zero. If these metrics don't recover after killing the Lambda, the root cause analysis may be incomplete — check for lingering transactions, vacuum pressure, or bloated tables from the Lambda's partial writes.
- After implementing resource isolation: Run the Lambda during business hours (intentionally, in a controlled test) with the connection limits and statement timeouts in place. Verify that `inventory-service` latency is unaffected during the Lambda's execution. Verify that the Lambda completes successfully within its normal runtime using the read replica for reads.
- After implementing the circuit breaker: Simulate `inventory-service` degradation (inject latency in a staging environment) and verify that the circuit breaker trips, that `order-service` returns fast failures, and that the circuit breaker recovers when `inventory-service` latency returns to normal.

**How to verify nothing else broke**:
- Monitor the Lambda's next nightly run end-to-end. Confirm it completes successfully with the new connection limits and read-replica configuration. Compare its output (inventory sync results) against previous successful runs.
- Monitor `order-service` error rates and latency after the timeout reduction to confirm no regression under normal conditions.
- Check whether any other services or jobs connect to this RDS instance and verify they are unaffected by the new role-level connection limits (which apply only to the Lambda's role).

### Prevention

**1. Connection-limit enforcement for all batch/async consumers of production databases.**
- *What it prevents*: Any batch job saturating a shared production database with unbounded connections — the exact failure mode seen tonight.
- *Where*: Enforced at the PostgreSQL role level for every non-application consumer of production databases. Codified in the infrastructure-as-code (Terraform, CloudFormation) that provisions database access for new consumers.
- *Relationship to root cause*: The Lambda was introduced 3 weeks ago with unrestricted database access. If connection limits had been a standard requirement for any new database consumer, this failure class would not exist.

**2. Runtime anomaly alerting on scheduled jobs.**
- *What it catches*: A scheduled job running significantly longer than its historical baseline — exactly what happened tonight with the Lambda running 15x longer than normal without any alert.
- *Where*: CloudWatch alarm on Lambda duration, configured relative to the job's historical p95 runtime. For a job that normally runs 10 minutes, alert at 20 minutes.
- *Relationship to root cause*: The Lambda ran for 2.5+ hours before anyone was paged, and the page was triggered by the *symptom* (`order-service` errors), not the *cause* (Lambda runtime anomaly). An alert on Lambda duration would have surfaced the cause directly, potentially before customer impact.

**3. Shared-resource review in the change management process for new database consumers.**
- *What it prevents*: A team introducing a new workload against a shared production database without understanding or mitigating its impact on existing consumers.
- *Where*: The change management or architecture review process. When a team proposes a new consumer of a production database, the review should assess: What is the query profile? What is the expected connection count? What is the worst-case runtime? Is resource isolation needed? This is not a heavyweight process — it's a checklist.
- *Relationship to root cause*: The Lambda was introduced by the warehouse team without (apparently) any coordination with the team that operates `inventory-service` or the database. A review would have identified the shared-resource risk and required isolation controls before deployment.

**4. Database resource monitoring with consumer-level attribution.**
- *What it catches*: Any single consumer disproportionately consuming database resources, before it degrades other consumers.
- *Where*: RDS Performance Insights or equivalent, with alerting segmented by database user/role. This requires each consumer to use a distinct database role (which the structural fix establishes for the Lambda).
- *Relationship to root cause*: Tonight, the RDS metrics showed aggregate saturation (92% CPU, 185 connections) but did not attribute the load to the Lambda vs. `inventory-service`. With per-role monitoring, the Lambda's resource consumption would have been visible and alertable independently.
