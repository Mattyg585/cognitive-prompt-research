---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A5
tier: pipeline
run: 3
stage: 01-debug-investigator
---

# Investigation Report

## Validated Behavior
- **Issue**: `order-service` fails intermittently (approx. 15% of requests) with `500 Internal Server Error`.
- **Reproduction**: The issue is actively occurring in production (AWS us-east-1).
- **Errors**:
  - `order-service` logs: `failed to process order`, `error="context deadline exceeded"`.
  - `order-service` logs: `downstream call failed`, `service="inventory-service"`, `error="context deadline exceeded"`.

## Context Gathered
- **Affected Files**:
  - `order-service/handler.go` (line 142): The `CreateOrder` handler where the error is logged.
  - `order-service/internal/inventory/client.go` (line 89): The `Reserve` method calling `inventory-service`.
- **Recent Changes**:
  - **3 days ago**: `order-service` request timeout increased from 3s to 5s.
  - **3 weeks ago**: `inventory-sync-lambda` deployed; runs nightly.
- **Environment**:
  - **Service**: `order-service` (Go) calling `inventory-service` (Go) which uses PostgreSQL (RDS).
  - **Database**: RDS `db.r6g.xlarge`.
  - **Metrics**: 
    - RDS CPU at 92% (normal 25%).
    - Active connections at 185 (normal 40).
    - `inventory-service` p99 latency is 4800ms (normal 200ms).

## Observations
- The `inventory-sync-lambda` started at 00:15 UTC and is still running (duration > 2 hours), whereas it usually completes in 10 minutes. This overlaps with the start of the error rate spike at 00:30 UTC.
- The Lambda connects to the same RDS instance as `inventory-service`.
- The high CPU and connection count on RDS suggest resource contention or a deadlock, likely caused by the long-running Lambda.
- The `order-service` timeout of 5000ms is being hit (`duration_ms=5003`, `timeout_ms=5000`), confirming that `inventory-service` is too slow to respond within the deadline.
- The 15% failure rate implies that some requests are succeeding, possibly because they hit the database when it's slightly less contended or use a cached connection, while others queue up and time out.
