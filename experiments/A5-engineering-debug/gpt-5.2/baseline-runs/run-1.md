---
model: GPT-5.2
date: 2026-03-15
experiment: A5
tier: baseline
run: 1
---

## Debug Report: Intermittent order failures due to inventory reservation timeouts

### Reproduction
- **Expected**: `order-service` creates the order and successfully reserves inventory via `inventory-service /v2/reserve`, returning 2xx within the request timeout.
- **Actual**: ~15% of requests return `500 Internal Server Error` after ~5s. Logs show `context deadline exceeded` on the downstream call to `inventory-service` with `timeout_ms=5000`, and `duration_ms≈5003`.
- **Steps**:
  1. Place an order in prod (or run the same request payload against prod with a test user) during the incident window.
  2. Observe `order-service` logs around `handler.go:142` / `handler.go:156` for `context deadline exceeded`.
  3. In parallel, call `inventory-service /v2/reserve` directly (bypassing `order-service`) with a 5s client timeout; note elevated tail latency / intermittent timeouts.
  4. Correlate timestamps with RDS metrics (CPU, active connections) and the running `inventory-sync-lambda` invocation(s).

### Root Cause
The failure mode is a classic downstream timeout cascade:
- `order-service` is not failing in its own logic; it is timing out waiting for `inventory-service`.
- `inventory-service` tail latency is dramatically elevated (p99 ~4800ms), aligning closely with the 5s timeout. That produces intermittent successes and failures depending on queueing/DB response time.
- RDS (shared by `inventory-service` and `inventory-sync-lambda`) shows abnormal load: **CPU ~92%** and **active connections ~185 vs normal ~40**, while read IOPS are normal. That pattern strongly suggests DB-side contention/CPU saturation and/or connection pressure rather than a storage throughput bottleneck.
- A scheduled job, `inventory-sync-lambda`, started at **00:15 UTC** and is **still running**, whereas it typically completes in ~10 minutes. This is the only noted behavioral change coincident with the incident start (~00:30 UTC).

Most likely root cause: **`inventory-sync-lambda` is running much longer than usual and is overloading the shared PostgreSQL instance** (e.g., unbounded batch update, inefficient query plan/full table scans, missing index, high concurrency, or a stuck loop causing repeated heavy writes). The overload increases query latency and/or exhausts DB connections, pushing `inventory-service` requests into long waits and causing `context deadline exceeded` in callers.

### Fix
**Immediate mitigation (stop the bleeding):**
1. **Disable/stop `inventory-sync-lambda`** (disable the schedule / reduce reserved concurrency to 0) to relieve DB pressure.
2. On RDS, use Performance Insights / `pg_stat_activity` to identify and **terminate the worst offending long-running queries/sessions** attributable to the Lambda if needed.
3. **Stabilize `inventory-service`** by ensuring its DB pool has sane limits (cap max open conns) so it cannot amplify connection storms under load.

**Corrective fix (make it not recur):**
- In `inventory-sync-lambda`:
  - Add **a hard time limit and context timeouts** for external calls and DB operations; fail fast rather than running indefinitely.
  - Ensure the job is **single-flight** (no overlaps): acquire a distributed lock (e.g., PostgreSQL advisory lock, DynamoDB lock, or Step Functions with a single execution) so a delayed run cannot overlap the next schedule.
  - Reduce DB impact: **process in small batches**, use set-based operations carefully, and avoid long transactions.
  - Identify and fix the slow query:
    - Inspect top SQL by total time; add **missing indexes** / rewrite queries to avoid sequential scans.
    - If doing wide-table updates, update only changed rows and avoid row-by-row loops.
  - Use **RDS Proxy** (or equivalent) if connection churn is part of the problem.
- In `inventory-service` / `order-service`:
  - Consider **hedged requests or bounded retries with exponential backoff** for `/v2/reserve` *only if* the operation is idempotent (or can be made idempotent with an idempotency key) to avoid double-reserving.
  - Add **circuit breaking / load shedding** so `order-service` fails quickly (and predictably) when `inventory-service` is unhealthy, rather than burning 5s and tying up resources.

### Prevention
- **Alerts**:
  - Alert when `inventory-sync-lambda` runtime exceeds expected (e.g., >15 minutes) or when concurrent executions >1.
  - Alert on RDS **CPU**, **active connections**, and **query latency** thresholds that correlate with `inventory-service` p99.
  - Alert on `inventory-service` p99 and timeout/error-rate specifically for `/v2/reserve`.
- **Guards**:
  - Enforce single-flight execution for the sync job.
  - Add statement/transaction timeouts for the Lambda’s DB role (e.g., `statement_timeout`).
- **Tests**:
  - Load/perf test `inventory-service /v2/reserve` under simulated DB contention.
  - Integration test the sync job against a realistic dataset to catch query-plan regressions (e.g., missing indexes) before rollout.
