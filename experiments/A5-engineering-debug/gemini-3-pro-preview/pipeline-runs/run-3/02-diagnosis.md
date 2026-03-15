---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A5
tier: pipeline
run: 3
stage: 02-debug-diagnostician
---

# Diagnosis Report

## Root Cause Analysis
The root cause is severe resource contention on the shared RDS instance used by both `inventory-service` and the `inventory-sync-lambda`. The `inventory-sync-lambda` job, which started at 00:15 UTC, has been running for over 2 hours (normal duration: 10 minutes) and is consuming excessive database resources (92% CPU, 185 active connections). This contention causes `inventory-service` queries to slow down dramatically (p99 latency 4800ms), leading to `order-service` requests timing out (`context deadline exceeded`) after the configured 5-second limit.

## Supporting Evidence
- **Correlation**: The error spike started at 00:30 UTC, shortly after the `inventory-sync-lambda` began execution at 00:15 UTC.
- **Resource Saturation**: RDS CPU is at 92% (vs 25% normal) and active connections are at 185 (vs 40 normal), indicating a bottleneck at the database layer.
- **Latency Impact**: `inventory-service` p99 latency spiked to 4800ms, dangerously close to the 5000ms timeout configured in `order-service`.
- **Timeout Confirmation**: `order-service` logs show `context deadline exceeded` errors, confirming the upstream service is unresponsive within the allowed time.
- **Abnormal Job Duration**: The `inventory-sync-lambda` is running 12x longer than usual, suggesting a stuck process, infinite loop, or inefficient query handling a large dataset.

## Proposed Solution
- **Target Files**:
  - `inventory-sync-lambda` (External/Infrastructure)
  - `order-service/config` (Configuration - implied)
- **Specific Changes**:
  - **Immediate Mitigation**: Terminate the current execution of `inventory-sync-lambda` to restore database performance for OLTP traffic.
  - **Code Fix (Lambda)**: Optimize the synchronization logic in `inventory-sync-lambda` to use batched updates or a read replica to avoid locking the primary database. Investigate if a specific dataset caused the stall.
  - **Configuration (Order Service)**: Verify `order-service` timeout settings. While increased to 5s recently, this is a symptom management change. Ideally, revert to 3s once the root cause is fixed to fail fast, or implement a circuit breaker to prevent cascading failures during downstream outages.
- **Verification Plan**:
  1. Terminate the Lambda and verify RDS CPU drops to <30% and connections drop to <50.
  2. Verify `order-service` error rate drops to <1% immediately after database recovery.
  3. Run a controlled test of `inventory-sync-lambda` with a smaller batch size or on a replica to verify the fix.
- **Constraints**:
  - The `inventory-sync-lambda` must complete its nightly run within the maintenance window.
  - Changes to the Lambda must not degrade `order-service` availability (OLTP priority > Batch priority).
