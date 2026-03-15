---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A5
tier: pipeline
run: 2
stage: 02-debug-diagnostician
---

# Diagnosis Report

## Root Cause Analysis
The outage is caused by **resource contention on the shared PostgreSQL instance**, triggered by the `inventory-sync-lambda` process.

The `inventory-sync-lambda` job, which started at 00:15 UTC, has been running for over 2.5 hours (normally 10 minutes). This long-running process is saturating the database CPU (92%) and occupying connection slots (185 active vs 40 normal). This contention has severely degraded the performance of the `inventory-service`, pushing its P99 response time to 4800ms.

The `order-service` has a configured timeout of 5000ms. Because the dependency's latency (4800ms) is effectively equal to the timeout, natural variance causes approximately 15% of requests to exceed the 5000ms limit, resulting in `context deadline exceeded` errors. The recent timeout increase (3s -> 5s) merely masked the issue temporarily.

## Supporting Evidence
- **Temporal Correlation**: The issue onset (00:30 UTC) correlates with the `inventory-sync-lambda` failing to complete its usual 10-minute window (started 00:15 UTC).
- **Resource Evidence**: Shared RDS CPU is at 92% and connections are 4.5x normal, confirming the database is the bottleneck.
- **Latency Logic**: The `inventory-service` P99 (4.8s) is dangerously close to the `order-service` timeout (5.0s), explaining the intermittent failures.
- **Architecture**: Both the batch job (Lambda) and the OLTP service (`inventory-service`) share the same database resources, creating a clear "noisy neighbor" failure mode.

## Proposed Solution
- **Target Files**:
  - `inventory-sync-lambda/main.go` (Assumed path for Lambda logic)
  - `order-service/internal/inventory/client.go`
- **Specific Changes**:
  - **`inventory-sync-lambda/main.go`**:
    - **Fix**: Configure the Lambda to connect to a **Read Replica** instead of the primary database instance. This will isolate the heavy read operations from the transactional write traffic.
    - **Optimization**: Implement **keyset pagination** (or cursor-based batching) for the sync query to avoid long-running transactions and table locks.
  - **`order-service/internal/inventory/client.go`**:
    - **Resilience**: Implement a **Circuit Breaker** around the `Reserve` method call. This will detect high latency/error rates and fail fast, preserving `order-service` resources.
- **Verification Plan**:
  1. **Immediate**: Terminate the currently running `inventory-sync-lambda` process to restore system health.
  2. **Test**: Deploy the Read Replica configuration to the Lambda in Staging. Run a full sync and monitor Primary DB CPU (should remain low) and execution time.
  3. **Test**: Verify `order-service` stability during the sync window.
- **Constraints**:
  - Check replication lag on the Read Replica to ensure the sync job isn't processing stale data beyond acceptable limits.
