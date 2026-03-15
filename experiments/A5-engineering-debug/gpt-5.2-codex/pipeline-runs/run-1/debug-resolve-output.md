---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A5
tier: pipeline
run: 1
stage: debug-resolve
---

# Resolution Report

## Root Cause (or Hypotheses)
- **Root cause (most likely)**: Inventory-service latency spikes causing order-service timeouts, driven by RDS contention from the long‑running `inventory-sync-lambda` sharing the same database.
  - **Evidence**:
    - inventory-service p99 latency ~4800ms vs normal ~200ms; order-service timeout is 5s and errors align with 5000ms duration.
    - RDS CPU 92% and active connections 185 (normal 40) while IOPS normal, suggesting CPU/connection contention rather than storage.
    - `inventory-sync-lambda` has been running since 00:15 UTC (normally ~10 min) and shares the same RDS instance.
- **Alternative hypotheses** (lower confidence):
  - Inventory-service connection pool exhaustion or lock waits causing long query latency (fits elevated connections/CPU but needs DB evidence).
  - Data volume spike in warehouse sync input causing `inventory-sync-lambda` to run long and stress DB (needs job metrics).

## Fix Plan
- **Change**:
  - Immediate mitigation: pause or throttle `inventory-sync-lambda` concurrency; reduce its DB load (batching, rate limits) or reschedule off-peak.
  - Short-term: move `inventory-sync-lambda` to a separate DB instance or read replica where possible; increase RDS capacity if needed.
  - Guardrail: set query timeouts / statement time limits for sync job; cap connection pool sizes to prevent exhaustion.
- **Rationale**:
  - Evidence points to DB contention during the long-running sync job; reducing or isolating its load should bring p99 latency below the 5s timeout and stop order failures.
- **Verification**:
  - Confirm drop in RDS CPU/active connections and inventory-service p99 latency returning to baseline.
  - Observe order-service errors for `/v2/reserve` returning to near-zero; verify in traces that downstream calls complete under timeout.
  - If timeout is increased temporarily, confirm no increased backlog/latency SLO breach.

## Prevention
- Monitor and alert on `inventory-sync-lambda` duration, concurrency, and DB query time; alert on sustained RDS CPU/connection spikes.
- Add SLO-based alerts for inventory-service p99 latency and order-service timeout rate.
- Add load tests that run inventory sync concurrently with order traffic to catch contention regressions.
- Separate OLTP (order/inventory) from batch sync workloads or enforce strict resource quotas.

## Risks / Side Effects
- Throttling/pausing sync may delay inventory accuracy; quantify acceptable staleness.
- Scaling RDS or moving workloads increases cost and operational complexity.
- Increasing timeouts can hide performance issues and raise end-to-end latency.

## If more info is needed
- RDS slow query logs, lock waits, and active query list during 00:15–present.
- `inventory-sync-lambda` logs/metrics (row counts, throughput, errors) and connection pool settings.
- Inventory-service pod metrics (CPU/mem/concurrency), connection pool configuration, and tracing spans for `/v2/reserve`.
- Any data volume anomalies in warehouse sync input.
