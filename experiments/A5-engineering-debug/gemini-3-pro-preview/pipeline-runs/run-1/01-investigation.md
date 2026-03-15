---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A5
tier: pipeline
run: 1
stage: 01-debug-investigator
---

# Investigation Report

## Validated Behavior
- **Issue**: `order-service` is intermittently failing with `500 Internal Server Error` (approx. 15% failure rate).
- **Reproduction**: Not reproducible locally as source code is unavailable. Occurring in Production environment.
- **Errors**:
  - Log 1: `order-service/handler.go:142 failed to process order error="context deadline exceeded"`
  - Log 2: `order-service/handler.go:156 downstream call failed service="inventory-service" error="context deadline exceeded"`
  - Stack trace points to `order-service/internal/inventory/client.go:89` in `(*Client).Reserve`.

## Context Gathered
- **Affected Files**:
  - `order-service/internal/inventory/client.go`: Contains the `Reserve` method which calls `inventory-service`. Fails with timeout.
  - `order-service/internal/handler/handler.go`: The HTTP handler for order creation. Catches the error and logs it.
- **Recent Changes**:
  - `order-service` config change (3 days ago): Increased request timeout from 3s to 5s.
  - `inventory-sync-lambda` deployment (3 weeks ago): New scheduled job added by warehouse team.
- **Environment**:
  - Service: `order-service` (Go, EKS), `inventory-service` (Go).
  - Database: PostgreSQL (RDS db.r6g.xlarge).
  - Job: `inventory-sync-lambda` (AWS Lambda).

## Observations
- The `order-service` timeout is configured to 5000ms, and failures occur at ~5003ms, confirming a hard timeout.
- `inventory-service` p99 latency is 4800ms, dangerously close to the 5000ms timeout.
- The high latency in `inventory-service` correlates with high CPU (92%) and connection count (185) on the shared RDS instance.
- The `inventory-sync-lambda` has been running unusually long (since 00:15 UTC) and coincides with the resource contention on RDS.
- The `order-service` timeout increase (3s -> 5s) explains why some requests succeed while others fail at the 5s deadline.