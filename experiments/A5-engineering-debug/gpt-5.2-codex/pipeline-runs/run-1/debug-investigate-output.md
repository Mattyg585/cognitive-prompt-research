---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A5
tier: pipeline
run: 1
stage: debug-investigate
---

# Investigation Handoff

## Issue Snapshot
- **Expected**: Orders succeed with normal latency.
- **Actual**: ~15% of orders fail with 500 due to `context deadline exceeded` in order-service when calling inventory-service `/v2/reserve` (timeout 5s).
- **Environment/Version**: Production (AWS us-east-1); `order-service` (Go on EKS); `inventory-service` (uses PostgreSQL RDS db.r6g.xlarge); order-service timeout 5s (config change 3 days ago).
- **Impact (if stated)**: Customer-impacting; intermittent failures over last 2 hours (started ~00:30 UTC, alerted 02:47 UTC).

## Reproduction
- **Steps**: Place an order in production; request triggers order-service calling inventory-service `/v2/reserve`.
- **Preconditions**: Elevated inventory-service latency; order-service request timeout 5s.
- **Frequency**: ~15% failure rate in last 2 hours; intermittent (retries sometimes succeed).

## Evidence
- **Errors/Logs**: [verbatim excerpts + source]
  - order-service logs (2026-03-14T02:47:12Z):
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
  - Stack trace:
    ```
    goroutine 847 [select]:
    order-service/internal/inventory.(*Client).Reserve(0xc000234000, {0x1a2b3c4, 0xc000567890}, {0xc000345678, 0x3})
        /app/internal/inventory/client.go:89 +0x1a4
    order-service/internal/handler.(*OrderHandler).CreateOrder(0xc000123000, {0x1a2b3c4, 0xc000567890}, 0xc000789abc)
        /app/internal/handler/handler.go:142 +0x2b8
    ```
- **Metrics/Traces**:
  - inventory-service latency: p50 180ms (normal 40ms), p99 4800ms (normal 200ms)
  - RDS CPU 92% (normal 25%), active connections 185 (normal 40), read IOPS normal
  - Lambda `inventory-sync-lambda` running since 00:15 UTC (normally ~10 min)

## Observations & Anomalies
- Inventory-service p99 near the 5s timeout, aligning with `context deadline exceeded`.
- RDS CPU and connections elevated while IOPS normal (possible contention or long-running queries).
- `inventory-sync-lambda` is running much longer than usual and shares the same RDS instance.
- No deployments in last 48 hours for order-service or inventory-service; failures are intermittent.

## Recent Changes (facts only)
- 3 days ago: order-service config change increased request timeout from 3s to 5s.
- 3 weeks ago: `inventory-sync-lambda` deployed (nightly job, usually ~10 min).
- No code deployments to order-service or inventory-service; no infrastructure changes.

## Open Questions / Missing Data
- Inventory-service pod CPU/memory, request concurrency, and error rates during incident.
- RDS slow query logs/lock waits/active queries during 00:15–present.
- `inventory-sync-lambda` current state, logs, throughput, error rates, and DB query profile.
- Connection pool settings for inventory-service and lambda; any connection exhaustion?
- Any recent data volume changes in warehouse sync input.
- Whether other services on the same RDS instance are seeing latency.
- Trace spans between order-service and inventory-service; any retries upstream/downstream.
