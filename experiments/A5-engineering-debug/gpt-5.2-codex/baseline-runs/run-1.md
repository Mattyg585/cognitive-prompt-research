---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A5
tier: baseline
run: 1
---

## Debug Report: Order failures due to inventory reservation timeouts

### Reproduction
- **Expected**: Orders successfully reserve inventory and complete within 5s.
- **Actual**: ~15% of orders fail with 500; `context deadline exceeded` while calling `inventory-service /v2/reserve`.
- **Steps**:
  1. Place orders while inventory-service p99 latency is elevated (~4.8s).
  2. Observe order-service logs at `handler.go:142/156` showing timeouts on the inventory-service call.
  3. Correlate timing with RDS CPU/connections spikes and the long-running `inventory-sync-lambda`.

### Root Cause
Inventory-service is timing out due to database saturation. The `inventory-sync-lambda` has been running abnormally long since 00:15 UTC and shares the same RDS instance. RDS CPU (92%) and active connections (185 vs 40 normal) indicate overload, which inflates inventory-service latency (p99 ~4800ms). The order-service timeout is 5000ms, so requests intermittently exceed the deadline and fail.

### Fix
- **Immediate**: Pause/disable or throttle `inventory-sync-lambda`; if needed, scale the RDS instance or increase IOPS to bring latency down.
- **Remediate**: Optimize lambda queries (batching, indexes), enforce DB timeouts and rate limits, and/or move the sync job to a separate DB/replica. Add backoff/circuit breaker handling for inventory-service timeouts.

### Prevention
- Add alerts on RDS CPU/connections and inventory-service p99 latency tied to scheduled jobs.
- Enforce per-service DB connection limits and lambda max runtime/concurrency.
- Add a regression test/runbook for disabling the sync job when order error rates spike.
