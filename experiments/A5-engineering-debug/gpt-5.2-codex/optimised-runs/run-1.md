---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A5
tier: optimised
run: 1
---

## Debug Report: Order failures due to inventory-service timeouts

### Investigation
- **Expected**: Order placement should consistently reserve inventory and complete within the request timeout.
- **Actual**: ~15% of orders fail with 500s after ~5s, with `context deadline exceeded` in `order-service` while calling `inventory-service`.
- **Reproduction**: Intermittent under current production load; failures occur when `inventory-service` response times approach the 5s timeout.
- **Scope/Impact**: Production only; customer-impacting intermittent order failures (~15%).
- **Evidence**:
  - `order-service` logs show downstream `inventory-service /v2/reserve` timing out at 5000ms with no retries.
  - `inventory-service` latency elevated (p50 180ms, p99 4800ms).
  - RDS CPU 92% (baseline ~25%) and active connections 185 (baseline ~40).
  - `inventory-sync-lambda` started 00:15 UTC and is still running; normally completes in ~10 minutes; uses same RDS instance.
  - No recent deploys to `order-service` or `inventory-service`.

### Observations & Anomalies
- Failure window started ~00:30 UTC, shortly after the long-running `inventory-sync-lambda` began.
- Elevated DB CPU and connections align with increased `inventory-service` tail latency.
- Restarting `inventory-service` pods did not change behavior, suggesting upstream/shared dependency issue.

### Root Cause (only if confident)
The `inventory-sync-lambda` is likely overloading the shared RDS instance (high CPU + connection count), causing `inventory-service` DB calls to slow down and breach the 5s request timeout, resulting in intermittent order failures.

### Fix (only when root cause is supported)
**Immediate mitigation**
- Pause/disable `inventory-sync-lambda` or reduce its concurrency to relieve RDS pressure.
- Reduce `inventory-sync-lambda` DB connection usage (pool limits) if pausing isn’t possible.

**Permanent fix**
- Optimize the lambda’s DB queries (add missing indexes, batch writes, avoid long-running transactions).
- Enforce strict DB connection limits for the lambda (separate pool/user with caps).
- Consider isolating workloads (separate RDS instance or read replica for sync jobs).

**Verification**
- Confirm RDS CPU and active connections return to baseline.
- Confirm `inventory-service` p99 latency drops to normal (~200ms) and order 500s fall below alert thresholds.
- Run a controlled load test or replay affected order flow to validate.

### Prevention (optional)
- Add alerts on long-running lambda duration and abnormal DB connection spikes.
- Schedule sync jobs with guardrails (max duration, circuit breaker on DB load).
- Add retry with jitter in `order-service` for transient 5xx from `inventory-service`.

### Open Questions / Next Steps (if needed)
- What queries or transaction patterns is `inventory-sync-lambda` running tonight vs. typical runs?
- Any recent data volume anomalies from the warehouse system?
- Can we capture slow query logs around 00:15–03:00 UTC to confirm hotspots?
