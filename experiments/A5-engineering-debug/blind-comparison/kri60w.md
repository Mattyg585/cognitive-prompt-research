## Debug Report: Intermittent Order Processing Failures Due to Database Contention from Runaway Lambda

### Reproduction
- **Expected**: All orders placed through `order-service` should be processed successfully, with `inventory-service` responding within normal latency bounds (p50 ~40ms, p99 ~200ms).
- **Actual**: Approximately 15% of orders are failing with `500 Internal Server Error`. The `order-service` handler at `handler.go:142` reports `context deadline exceeded` after 5003ms when calling the `inventory-service` `/v2/reserve` endpoint. Failures are intermittent — retries sometimes succeed.
- **Steps**:
  1. Place an order through the normal order flow in production (us-east-1).
  2. The `order-service` calls `inventory-service` at `/v2/reserve` to reserve inventory.
  3. Approximately 15% of the time, the `inventory-service` response takes longer than the 5000ms timeout configured on the `order-service` client, resulting in a `context deadline exceeded` error.
  4. The order fails with a 500 status code.
  5. Retrying the same order may succeed if the `inventory-service` happens to respond within the timeout window.

**Scope**: Started around 00:30 UTC on 2026-03-14, detected at 02:47 UTC when the error rate crossed the alert threshold. All users placing orders are affected — this is not user-specific or region-specific. The issue correlates with the `inventory-sync-lambda` starting its nightly run at 00:15 UTC.

### Root Cause

The root cause is database resource contention on the shared PostgreSQL RDS instance (`db.r6g.xlarge`) caused by the `inventory-sync-lambda` function.

Here's the chain of events:

1. **00:15 UTC** — The `inventory-sync-lambda` (a scheduled nightly job added 3 weeks ago by the warehouse team) begins its run. It connects to the same RDS PostgreSQL instance used by `inventory-service`.

2. **The Lambda is running abnormally long.** It normally completes in ~10 minutes, but tonight it appears stuck or is processing a much larger dataset than usual. This suggests either the warehouse data volume has grown, the Lambda encountered a data condition causing it to process more rows than expected, or it's caught in a retry loop.

3. **The long-running Lambda is saturating the database.** The RDS metrics tell the story:
   - CPU at **92%** (normal: 25%) — the Lambda's queries are consuming the vast majority of CPU.
   - Active connections at **185** (normal: 40) — the Lambda is either holding many connections open or creating new ones rapidly. This is consuming the connection pool.
   - Read IOPS are normal — this suggests the load is CPU-bound (likely complex queries, aggregations, or row-level locking), not I/O-bound.

4. **`inventory-service` queries are starved.** With the database CPU pegged at 92% and connections bloated to 185, the `inventory-service`'s queries to the `/v2/reserve` endpoint — which need to check and update inventory counts — are forced to wait. Response times have ballooned: p50 from 40ms to 180ms, p99 from 200ms to 4800ms.

5. **`order-service` times out.** The `order-service` has a 5-second timeout on calls to `inventory-service` (increased from 3s three days ago). When `inventory-service` responses land in the tail of the latency distribution (approaching or exceeding 5000ms), the Go context deadline is exceeded. The stack trace confirms this: the `inventory.(*Client).Reserve` call blocks in a `select` statement waiting for a response that never arrives in time.

6. **The intermittent nature** is explained by the bimodal response time distribution. Most `inventory-service` requests still complete (p50 = 180ms), but the tail latency (p99 = 4800ms) is close to the timeout boundary. The ~15% failure rate reflects the portion of requests that fall into this high-latency tail.

**Why restarting `inventory-service` pods didn't help**: The bottleneck is not in `inventory-service` itself — it's in the database. Restarting pods just re-establishes connections to the same overloaded RDS instance.

**Why the timeout increase from 3 days ago is relevant**: The timeout was raised from 3s to 5s, which actually masks the problem slightly. At the original 3s timeout, the failure rate would likely be much higher than 15% tonight. This config change may also explain why the problem wasn't noticed during previous Lambda runs — if previous runs completed in 10 minutes, the elevated latency window was short, and the 3s timeout may have caused a small number of failures that didn't cross the alert threshold.

### Fix

**Immediate (stop the bleeding):**

1. **Kill or pause the `inventory-sync-lambda` execution.** This is the most important immediate action. Either:
   - Stop the currently running Lambda invocation via the AWS Console or CLI.
   - If the Lambda can't be stopped cleanly, adjust its concurrency to 0 to prevent it from continuing: `aws lambda put-function-concurrency --function-name inventory-sync-lambda --reserved-concurrent-executions 0`

2. **Monitor RDS recovery.** Once the Lambda is stopped, watch for:
   - CPU dropping back toward 25%
   - Active connections dropping back toward 40
   - `inventory-service` p99 latency returning to ~200ms
   - `order-service` error rate dropping to 0%

**Short-term (prevent recurrence):**

3. **Isolate the Lambda's database access.** Options (from most to least preferred):
   - **Create a read replica** for the Lambda to use. The inventory sync job likely only needs to read from or write to specific tables — it should not compete with production traffic on the primary.
   - **Add connection pooling** (e.g., RDS Proxy) in front of the RDS instance to manage connection limits and prevent one consumer from monopolizing connections.
   - **Rate-limit the Lambda's database queries** — add throttling or batch-size limits so it processes rows at a sustainable pace.

4. **Add a timeout and circuit breaker to the Lambda itself:**
   - Set a maximum execution time (e.g., 20 minutes) so it can't run indefinitely.
   - Add monitoring/alerting on Lambda execution duration.
   - If the Lambda exceeds its expected runtime, it should abort gracefully and alert the warehouse team.

5. **Add connection limits for the Lambda's database user/role:**
   - In PostgreSQL: `ALTER ROLE inventory_sync_lambda CONNECTION LIMIT 10;` (or appropriate number) to prevent it from consuming excessive connections.

**Longer-term (architectural):**

6. **`inventory-service` should have its own connection pool limits and circuit breaking.** If the database is slow, `inventory-service` should fail fast rather than letting requests queue up to the timeout boundary.

7. **`order-service` should implement retries with backoff** on the `/v2/reserve` call (currently `retry_count=0` in the logs, meaning no retries). A single retry with jitter could recover many of the transient failures.

8. **Consider separating the database** — if the inventory sync workload continues to grow, it may warrant its own database or a separate schema with resource isolation.

### Prevention
- **Add an alert on RDS active connections exceeding a threshold** (e.g., > 80) to catch runaway consumers before they impact production services.
- **Add an alert on RDS CPU exceeding 70%** with a notification to both the on-call engineer and the warehouse team.
- **Add an alert on `inventory-sync-lambda` execution duration** exceeding 15 minutes (1.5x normal).
- **Add an integration test** that verifies `inventory-service` response times remain within SLA bounds when the database is under concurrent load. This could be a periodic synthetic check or a load test that simulates the Lambda's query pattern.
- **Add a runbook entry** for this failure mode: "If `inventory-service` latency spikes and RDS CPU is elevated, check for long-running batch jobs on the shared database."
- **Enforce connection limits per service** at the database level so no single consumer can monopolize the connection pool.
- **Require a shared-resource review** for any new service or Lambda that connects to production databases — the warehouse team's Lambda was deployed without the `inventory-service` team being aware of the shared dependency.
