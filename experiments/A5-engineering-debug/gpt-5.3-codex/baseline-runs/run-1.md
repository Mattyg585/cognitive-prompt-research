---
model: GPT-5.3-Codex (gpt-5.3-codex)
date: 2026-03-15
experiment: A5
tier: baseline
run: 1
---

## Debug Report: Intermittent Order Failures from Downstream Timeout

### Reproduction
- **Expected**: `order-service` should consistently create orders and reserve inventory through `inventory-service /v2/reserve` with normal latency (roughly p50 40ms / p99 200ms).
- **Actual**: About 15% of requests fail with `500 Internal Server Error` due to `context deadline exceeded` at ~5000ms while waiting on `inventory-service`.
- **Steps**:
  1. Submit orders in production during the incident window.
  2. Observe that a subset of requests take ~5s then fail.
  3. Retry same user/order pattern; some retries succeed, confirming intermittent timeout behavior.

### Root Cause
The most likely root cause is shared-database contention caused by `inventory-sync-lambda` running abnormally long against the same PostgreSQL RDS instance used by `inventory-service`.

Evidence chain:

1. Lambda started 00:15 UTC and remained running far beyond normal 10 minutes.
2. Order failures started around 00:30 UTC, shortly after Lambda runtime began accumulating load.
3. RDS CPU rose to 92% (normal 25%) and active connections to 185 (normal 40).
4. `inventory-service` latency degraded badly (p99 ~4800ms), pushing `order-service` calls past 5s timeout.
5. Restarting `inventory-service` pods had no effect, consistent with downstream database saturation rather than pod-local failure.

So the immediate trigger is long-running Lambda workload; systemic issue is lack of isolation between batch sync traffic and latency-sensitive reservation traffic.

### Fix
1. **Immediate mitigation**
   - Stop current `inventory-sync-lambda` execution (or set reserved concurrency to `0`) to release database pressure.
   - Confirm recovery via RDS CPU, active connections, and `inventory-service` p99 latency.

2. **Short-term hardening**
   - Add strict runtime timeout and alerting for `inventory-sync-lambda` duration anomalies.
   - Enforce DB connection limits for Lambda DB role so batch jobs cannot consume a large share of capacity.
   - Add backoff retries from `order-service` to `inventory-service` with jitter and bounded attempts.

3. **Structural fix**
   - Isolate sync workload from transactional path: move heavy sync reads to a read replica and constrain write batches/transaction sizes.
   - Add circuit-breaker behavior on `order-service` inventory dependency to fail fast under sustained downstream degradation.

### Prevention
- Alert on abnormal Lambda duration (> expected window).
- Alert on RDS CPU and connection thresholds well before saturation.
- Add runbook linking symptom (`context deadline exceeded`) to shared-RDS contention checks.
- Require cross-team review for any new production job that shares critical DB infrastructure.
- Add integration/load test simulating concurrent reserve traffic and sync-job pressure.

