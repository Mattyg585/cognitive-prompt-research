---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A5
tier: pipeline
run: 2
stage: 01-debug-investigator
---

# Investigation Report

## Validated Behavior
- **Issue**: `order-service` is intermittently failing (approx. 15% error rate) with `500 Internal Server Error`.
- **Reproduction**: Issue is observed in Production environment. Failures occur when placing orders. Retry attempts sometimes succeed.
- **Errors**:
  - `context deadline exceeded` in `order-service` (duration_ms=5003).
  - Downstream call to `inventory-service` (`/v2/reserve`) failed with `context deadline exceeded` (timeout_ms=5000).

## Context Gathered
- **Affected Files**:
  - `order-service/handler.go`: Line 142 in `CreateOrder` (initiates the order process).
  - `order-service/internal/inventory/client.go`: Line 89 in `Reserve` (calls `inventory-service`).
- **Recent Changes**:
  - **3 days ago**: `order-service` configuration change increasing request timeout from 3s to 5s.
  - **3 weeks ago**: `inventory-sync-lambda` deployed by the warehouse team.
- **Environment**:
  - **Services**: `order-service` (Go, EKS), `inventory-service` (Go, EKS).
  - **Database**: PostgreSQL (RDS, db.r6g.xlarge) shared by `inventory-service` and `inventory-sync-lambda`.
  - **Infrastructure**: AWS (us-east-1).

## Observations
- **Correlation with Load**: `inventory-service` response times are severely elevated (P99 = 4800ms) compared to normal (200ms), closely matching the `order-service` 5s timeout.
- **Database Contention**: The shared RDS instance is under heavy load (CPU 92%, 185 active connections vs. normal 40).
- **Scheduled Job Anomaly**: The `inventory-sync-lambda` started at 00:15 UTC and is still running (duration > 2.5 hours), whereas it normally completes in 10 minutes. This coincides with the start of the issue (around 00:30 UTC).
- **Timeout Configuration**: The recent timeout increase in `order-service` (to 5s) explains why some requests are succeeding despite the high latency, but the P99 of `inventory-service` is dangerously close to this limit.
