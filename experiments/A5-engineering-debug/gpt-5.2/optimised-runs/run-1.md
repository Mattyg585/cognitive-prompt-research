---
model: GPT-5.2
date: 2026-03-15
experiment: A5
tier: optimised
run: 1
---

## Debug Report: Intermittent order failures due to inventory reserve timeouts

### Reproduction (ground truth)
- **Expected:** `order-service` successfully creates an order and reserves inventory.
- **Actual:** ~15% of orders fail with `500 Internal Server Error` after ~5s; logs show `context deadline exceeded` on the downstream call to `inventory-service /v2/reserve`.
- **Steps / conditions to reproduce:** Place an order that triggers an inventory reservation during the incident window; some requests exceed the 5s timeout.
  - For a deterministic reproducer: run a steady stream of `/v2/reserve` requests while `inventory-sync-lambda` is running, and observe tail latency / timeouts.
- **Affected env(s):** Production (AWS us-east-1), `order-service` (Go on EKS) calling `inventory-service`.

### Observed Facts
- `order-service` logs show:
  - `downstream call failed` to `inventory-service` `/v2/reserve`
  - `error="context deadline exceeded"`
  - `timeout_ms=5000` and `duration_ms≈5003`
  - `retry_count=0`
- `inventory-service` latency is elevated: p50 180ms (normal 40ms), p99 4800ms (normal 200ms).
- `inventory-service` uses PostgreSQL on RDS (`db.r6g.xlarge`).
- RDS metrics during the incident: CPU ~92% (normal 25%), active connections 185 (normal 40), read IOPS normal.
- A scheduled `inventory-sync-lambda` started at ~00:15 UTC and is **still running**; it connects to the same RDS instance as `inventory-service`.
- No deploys to `order-service` or `inventory-service` in the last 48 hours.
- 3 days ago, `order-service` timeout increased from 3s → 5s.

### Inferences (clearly labeled)
- The `order-service` 500s are *secondary*: they’re caused by the inventory reservation call exceeding its 5s context deadline.
- The most likely bottleneck is PostgreSQL on the shared RDS instance (high CPU + high connections + a long-running batch job), which would directly drive elevated `inventory-service` tail latency.

### Evidence
Key correlations pointing to the shared-DB contention hypothesis:
- Symptom matches the configured timeout: `duration_ms≈timeout_ms≈5000`.
- `inventory-service` p99 (~4.8s) sits right below the 5s deadline, explaining “intermittent” failures.
- RDS CPU and connections are abnormally high at the same time the long-running `inventory-sync-lambda` is running.

### Root Cause (mechanism)
**Likely mechanism:** `inventory-sync-lambda` is running much longer than usual and is saturating/contending on the shared PostgreSQL RDS instance (CPU + connection pressure and/or lock contention), which slows `inventory-service` DB queries. That pushes `/v2/reserve` latency into the 5s range, causing context deadlines in both `inventory-service` and the upstream `order-service`, resulting in intermittent 500s.

**Why this explains the symptoms:**
- Elevated DB CPU/connections + elevated service p99 + timeouts exactly at 5s are a coherent chain.
- No deploys needed: workload/traffic patterns and the stuck batch job are sufficient.

**What would change my mind:**
- RDS Performance Insights shows no SQL from the Lambda and no DB wait events/CPU contention during failures.
- `inventory-service` traces/pprof show time spent elsewhere (e.g., external API, locks in app code) rather than waiting on DB.
- The Lambda is verified to be idle / not issuing queries (e.g., stuck before DB work), while DB load is driven by another actor.

### Discriminating checks (confirm/refute quickly)
1. **RDS Performance Insights (fastest confirmation):**
   - Top SQL by load during 00:15–now
   - Wait events (CPU vs lock vs IO vs LWLock)
   - “DB load by user” to see Lambda vs service users
2. **Postgres live inspection (if you can run SQL):**
   - Long-running queries + blockers:
     ```sql
     SELECT now()-xact_start AS xact_age, pid, usename, state, wait_event_type, wait_event, query
     FROM pg_stat_activity
     WHERE datname = current_database()
     ORDER BY xact_age DESC
     LIMIT 50;

     SELECT blocked.pid AS blocked_pid, blocked.query AS blocked_query,
            blocker.pid AS blocker_pid, blocker.query AS blocker_query
     FROM pg_locks blocked_locks
     JOIN pg_stat_activity blocked ON blocked.pid = blocked_locks.pid
     JOIN pg_locks blocker_locks ON blocker_locks.locktype = blocked_locks.locktype
       AND blocker_locks.DATABASE IS NOT DISTINCT FROM blocked_locks.DATABASE
       AND blocker_locks.relation IS NOT DISTINCT FROM blocked_locks.relation
       AND blocker_locks.page IS NOT DISTINCT FROM blocked_locks.page
       AND blocker_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple
       AND blocker_locks.virtualxid IS NOT DISTINCT FROM blocked_locks.virtualxid
       AND blocker_locks.transactionid IS NOT DISTINCT FROM blocked_locks.transactionid
       AND blocker_locks.classid IS NOT DISTINCT FROM blocked_locks.classid
       AND blocker_locks.objid IS NOT DISTINCT FROM blocked_locks.objid
       AND blocker_locks.objsubid IS NOT DISTINCT FROM blocked_locks.objsubid
       AND blocker_locks.pid != blocked_locks.pid
     JOIN pg_stat_activity blocker ON blocker.pid = blocker_locks.pid
     WHERE NOT blocked_locks.granted;
     ```
3. **Lambda logs/metrics:** confirm what it’s doing (batch size, parallelism, retries, error loops) and why it’s running >10 minutes.
4. **Inventory-service traces:** confirm high latency is dominated by DB query time and identify the specific queries.

### Fast Triage / Mitigations (safe + reversible)
- **Stop the bleeding:** pause/disable the `inventory-sync-lambda` schedule and stop the currently running execution (if the job is non-critical vs customer orders).
- **Reduce DB pressure immediately (if needed):**
  - Temporarily scale up the RDS instance class (CPU-bound symptom) to restore headroom.
  - Temporarily reduce Lambda concurrency / batch size and ensure it sleeps between batches.
- **Avoid making it worse:** don’t add aggressive retries in `order-service` right now; retries can amplify DB load during saturation.

### Fix Plan (grounded + staged)
1. **Fix the Lambda to be “good citizen” on the shared DB**
   - Bound concurrency (limit parallel workers).
   - Batch updates/inserts and **commit frequently** (avoid long transactions).
   - Set `statement_timeout` and `lock_timeout` to prevent pathological stalls.
   - Ensure connections are reused/pooled appropriately and closed (avoid connection leaks).
   - Add a hard execution timeout and fail fast with alerting if exceeded.
2. **Protect `inventory-service` from batch workloads**
   - Separate DB users/roles and apply connection limits per role (keep capacity reserved for the service).
   - Use a connection pooler/proxy (e.g., RDS Proxy/pgbouncer) with sane max pool sizes.
   - Identify and index the hot paths for `/v2/reserve` and the sync job (based on PI “Top SQL”).
3. **Resilience / degradation strategy**
   - Prefer explicit 503/circuit-breaker behavior from `inventory-service` when the DB is overloaded (better than timing out at 5s).
   - If business allows: queue reservations or mark orders “pending reservation” rather than hard-failing.
4. **Validation**
   - Re-run the nightly sync in a controlled environment while load-testing `/v2/reserve`; confirm p99 stays within budget.

### Prevention
- Alerts:
  - Lambda duration > expected (e.g., >15m) and concurrent executions >1.
  - RDS CPU/DB load + connection count spikes, and lock-wait time.
  - `inventory-service` p99 approaching the `order-service` deadline.
- Runbook:
  - “Disable sync job” and “identify top SQL + blockers” steps with exact links/commands.
- Ownership:
  - Align warehouse team and inventory team on shared-DB SLOs and change management for batch jobs.
