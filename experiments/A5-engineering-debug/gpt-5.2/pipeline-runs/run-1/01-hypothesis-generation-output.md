---
model: GPT-5.2
date: 2026-03-15
experiment: A5
tier: pipeline
run: 1
stage: 01-hypothesis-generation
---

### Hypothesis Packet

#### 1) Problem statement (facts only)
- **Expected:** `order-service` should successfully create orders; downstream `inventory-service` reservation should complete within configured timeouts.
- **Actual:** ~15% of orders in the last ~2 hours fail intermittently with `500 Internal Server Error`; retrying sometimes succeeds.
- **Error text / stack trace (verbatim):**
  - 
    ```
    2026-03-14T02:47:12Z ERROR order-service/handler.go:142 failed to process order
        error="context deadline exceeded"
        order_id="ord_8f3k2m"
        user_id="usr_29dk3"
        duration_ms=5003

    2026-03-14T02:47:12Z ERROR order-service/handler.go:156 downstream call failed
        service="inventory-service"
        endpoint="/v2/reserve"
        error="context deadline exceeded"
        timeout_ms=5000
        retry_count=0
    ```
  - 
    ```
    goroutine 847 [select]:
    order-service/internal/inventory.(*Client).Reserve(0xc000234000, {0x1a2b3c4, 0xc000567890}, {0xc000345678, 0x3})
        /app/internal/inventory/client.go:89 +0x1a4
    order-service/internal/handler.(*OrderHandler).CreateOrder(0xc000123000, {0x1a2b3c4, 0xc000567890}, 0xc000789abc)
        /app/internal/handler/handler.go:142 +0x2b8
    ```
- **Where observed:** Production (AWS us-east-1). `order-service` calling `inventory-service` `/v2/reserve`.
- **When it started / what changed:** Symptoms started ~00:30 UTC; alert triggered 02:47. No deployments/infrastructure changes in last 48h. CloudWatch shows `inventory-sync-lambda` started ~00:15 UTC and is still running (normally ~10 min). RDS (same DB as `inventory-service` and Lambda) shows CPU 92% (normal 25%), active connections 185 (normal 40). `inventory-service` latency elevated (p50 180ms, p99 4800ms).

#### 2) Constraints & context (unknown is OK)
- **Runtime / platform:** `order-service` is Go on EKS. `inventory-service` is downstream (language/runtime unspecified) and uses PostgreSQL on RDS (db.r6g.xlarge).
- **Deploy/runtime differences:** Production incident; no recent deployments for `order-service` or `inventory-service`. Unknown whether staging reproduces.
- **Recent changes:**
  - 3 days ago: `order-service` request timeout increased 3s → 5s.
  - 3 weeks ago: `inventory-sync-lambda` deployed; nightly scheduled job; abnormal runtime tonight.
  - Data/traffic changes: unknown.
- **Blast radius:** Customer-impacting; intermittent failures (~15%) for order creation (likely subset of requests that hit tail latency >5s).

#### 3) Hypotheses (as many as needed)

- **ID:** H1
- **Claim (one sentence):** The long-running `inventory-sync-lambda` is saturating PostgreSQL (CPU + connections), causing `inventory-service` `/v2/reserve` to slow down until `order-service` hits its 5s deadline.
- **Why plausible given current facts:** Strong correlation in time (Lambda starts 00:15; errors start ~00:30); RDS CPU and connections are far above normal; `inventory-service` p99 ~4800ms is near the 5000ms timeout; intermittent success matches tail-latency/queueing effects.
- **What would strongly confirm it:** Performance Insights/top waits show DB time dominated by lambda queries; `pg_stat_activity` shows many active connections from Lambda and/or long-running transactions; `inventory-service` DB query latency increases during lambda runtime; connection count attributable to Lambda spikes.
- **What would strongly falsify it:** DB wait/CPU is not driven by lambda (no notable lambda DB activity), or `inventory-service` latency is high even when Lambda is not executing / on an isolated DB replica; DB metrics normal while errors persist.
- **Fast discriminating checks:**
  - RDS Performance Insights: top SQL, top wait events, DB load by user/application.
  - `pg_stat_activity` snapshot: active sessions by `application_name`/user; oldest `xact_start`.
  - `pg_locks` + `pg_stat_activity`: blocking/blocked chains.
  - CloudWatch logs for Lambda: duration, concurrency, errors, retry loops; confirm it’s actively running vs “stuck”.
- **Evidence needed (minimum):** 1) Performance Insights screenshot/export for 00:15–now; 2) `pg_stat_activity` + lock snapshot; 3) Lambda invocation metrics/log excerpt showing sustained runtime/concurrency.

- **ID:** H2
- **Claim (one sentence):** `inventory-sync-lambda` (or a related batch job) is holding long transactions/locks (e.g., on inventory tables), intermittently blocking `/v2/reserve` queries until they time out.
- **Why plausible given current facts:** Elevated p99 + intermittent timeouts can come from lock contention; a “stuck” sync job commonly involves long transactions; high CPU + high connections can co-occur with lock waits if many sessions queue.
- **What would strongly confirm it:** Clear lock waits in DB (blocked queries waiting on locks held by the Lambda session); `pg_stat_activity.wait_event_type = 'Lock'` spikes; `pg_blocking_pids()` shows Lambda sessions blocking `inventory-service` sessions.
- **What would strongly falsify it:** No lock waits during the incident window; queries are slow due to CPU/IO rather than waiting on locks; `inventory-service` queries are not blocked.
- **Fast discriminating checks:**
  - Query lock state: `SELECT * FROM pg_stat_activity WHERE wait_event_type IS NOT NULL;` and `pg_locks` join to identify blockers.
  - Identify long-running transactions: `xact_start` age; autovacuum/maintenance activity.
  - Check whether `inventory-service` reserve path uses `SELECT ... FOR UPDATE` or similar locking semantics (if code/logs available).
- **Evidence needed (minimum):** Blocking tree evidence (blocked pid → blocking pid) during a spike; sample of blocked query text for reserve path.

- **ID:** H3
- **Claim (one sentence):** PostgreSQL connection pool exhaustion / connection leak in `inventory-service` (potentially triggered by increased latency) is increasing queueing and tail latency, pushing some calls past the 5s client deadline.
- **Why plausible given current facts:** Active connections are 185 vs normal 40; if `inventory-service` opens too many connections under stress or fails to reuse/close, it can amplify latency; intermittent success fits variable pool pressure.
- **What would strongly confirm it:** `inventory-service` connection count grows with traffic; many idle-in-transaction sessions or rapidly created sessions; app metrics show pool saturation; DB shows many connections from `inventory-service` user with short lifetimes.
- **What would strongly falsify it:** Connection attribution shows most new connections are from the Lambda; `inventory-service` maintains stable pool size and is not saturated; latency is independent of pool settings.
- **Fast discriminating checks:**
  - Break down RDS connections by DB user/application.
  - `inventory-service` metrics/logs: pool stats (open/in-use/wait), time waiting for a connection.
  - Look for `idle in transaction` sessions from `inventory-service`.
- **Evidence needed (minimum):** Connection attribution + pool stats during incident.

- **ID:** H4
- **Claim (one sentence):** `inventory-service` itself is resource constrained or degraded (CPU throttling, GC pauses, pod-level contention), causing slow `/v2/reserve` responses independent of DB.
- **Why plausible given current facts:** Pod restarts didn’t help, but that doesn’t rule out cluster-level issues; elevated p50 (180ms vs 40ms) suggests broad slowdown, not only rare DB stalls.
- **What would strongly confirm it:** `kubectl top pods` shows sustained high CPU/memory, throttling, restarts, or high request queue times; application profiles show increased handler time not attributable to DB; node-level saturation.
- **What would strongly falsify it:** `inventory-service` pods healthy with low CPU/mem; handler time correlates tightly with DB wait time; p50 increases match DB latency increases.
- **Fast discriminating checks:**
  - `kubectl top pods -n <ns>` and `kubectl describe pod` for throttling/OOM.
  - `kubectl logs` for timeouts, thread/goroutine dumps, circuit breaker events.
  - Service-level dashboards: request duration breakdown (app vs DB vs downstream).
- **Evidence needed (minimum):** Pod resource metrics + a latency breakdown (if available) for `/v2/reserve`.

- **ID:** H5
- **Claim (one sentence):** A traffic/data pattern change increased load on `/v2/reserve` (more orders, hot SKU contention, or warehouse sync backlog), pushing `inventory-service` into a high-latency regime and cascading into timeouts.
- **Why plausible given current facts:** No deployments; onset could be driven by scheduled jobs, traffic spikes, or data anomalies; intermittent success aligns with load shedding and tail latency.
- **What would strongly confirm it:** Order volume/traffic increased around 00:30; specific SKUs/users correlate with slow requests; reserve queries show skew (hot rows) and contention; warehouse sync backlog correlates.
- **What would strongly falsify it:** Traffic volume stable; latency spikes without traffic changes; failures evenly distributed and unrelated to request characteristics.
- **Fast discriminating checks:**
  - Compare request rate and latency for `/v2/reserve` before/after 00:30.
  - Sample slow logs/traces tagged with SKU/warehouse; look for heavy hitters.
  - DB query plan/regressions for reserve query under hot keys.
- **Evidence needed (minimum):** Traffic graph + tagged slow-request samples.

- **ID:** H6
- **Claim (one sentence):** The `order-service` client timeout (5s) is now the dominant failure mode because `inventory-service` p99 is hovering near 5s, and there is no retry/circuit behavior (`retry_count=0`), turning tail latency into user-visible 500s.
- **Why plausible given current facts:** Log shows timeout_ms=5000 and duration_ms=5003; p99 ~4800ms means a modest additional delay tips over; intermittent success matches distribution near the threshold.
- **What would strongly confirm it:** Traces show `inventory-service` responses arriving just after 5s; server-side logs show completion after client cancellation; error rate is sensitive to the exact timeout value.
- **What would strongly falsify it:** `inventory-service` is returning 5xx quickly (not near 5s) or order-service is failing earlier than 5s; retries already exist but are misreported.
- **Fast discriminating checks:**
  - Distributed tracing or correlated logs: client cancel vs server completion time.
  - `inventory-service` access logs for `/v2/reserve`: did it complete and how long?
  - Confirm whether order-service returns 500 on context deadline exceeded vs mapping to 504/timeout (behavioral, not fix).
- **Evidence needed (minimum):** One or two correlated request IDs showing timings across services.

#### 4) Prioritised next actions (evidence-first)
- Pull **RDS Performance Insights** for 00:00–now: identify top SQL and whether DB load is attributable to Lambda vs `inventory-service` (discriminates H1/H3).
- Take a **DB snapshot** (`pg_stat_activity`, `pg_locks`, blocking chains, long transactions) during a latency spike (discriminates H1 vs H2 vs H3).
- Pull **CloudWatch Lambda metrics/logs** for `inventory-sync-lambda` (duration, concurrency, retries, errors) and correlate with DB CPU/connections (supports/falsifies H1/H2).
- Check **`inventory-service` pod health and resource metrics** + request latency breakdown if available (discriminates H4).
- Get **one correlated trace/log bundle** for a failing order (order-service request → inventory-service handler → DB call timing) to distinguish “slow server” vs “client timeout threshold” (H6).

#### 5) Clarifying questions for the user
- Can you share **RDS Performance Insights** (top waits + top SQL) for the incident window, or confirm whether you have it enabled?
- Do you have a way to run **read-only DB queries** (psql) to capture `pg_stat_activity`/locks during the incident?
- Is there **distributed tracing** between `order-service` and `inventory-service` (and to DB) to correlate a single failing request ID end-to-end?
- What are the **`inventory-service` timeouts** (DB query timeout, HTTP handler timeout) and does it log when the client cancels?
- Any **traffic anomaly** around 00:30 UTC (orders/min, reserve calls/min), or is volume stable?

#### 6) Stop rule
- Move to **02-evidence-gathering** once we have: (a) Performance Insights or equivalent DB load attribution, (b) a `pg_stat_activity`/locks snapshot during a spike, and (c) Lambda runtime/concurrency evidence for the same window.
- If any of (a)-(c) cannot be obtained, stop and request the smallest substitute: e.g., a screenshot of DB metrics with connection count + CPU over time, and a Lambda log excerpt showing sustained execution and any retries/errors.
