---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A5
tier: baseline
run: 1
---

## Debug Report: Intermittent 500 Errors in Order Service

### Reproduction
- **Expected**: `order-service` should process orders successfully, typically within milliseconds.
- **Actual**: Approximately 15% of orders are failing with `500 Internal Server Error` due to `context deadline exceeded`. The `inventory-service` is timing out after 5000ms.
- **Steps**: 
  1. Trigger the `inventory-sync-lambda` (currently stuck running since 00:15 UTC).
  2. Attempt to place orders via `order-service`.
  3. Observe increased latency and timeouts when the database is under load.

### Root Cause
**Resource contention on the shared RDS instance caused by a long-running background job.**

1.  **Trigger**: The `inventory-sync-lambda` scheduled job started at 00:15 UTC and has been running abnormally long (stuck).
2.  **Resource Exhaustion**: This Lambda is consuming database resources on the shared RDS instance. 
    - RDS CPU is at 92% (vs. normal 25%).
    - Active connections are at 185 (vs. normal 40).
3.  **Cascading Failure**: 
    - The `inventory-service`, which shares this RDS instance, is experiencing slow query execution due to the contention.
    - `inventory-service` response times have spiked (p99 = 4800ms).
    - `order-service` calls to `inventory-service` are timing out because they exceed the 5000ms deadline.

### Fix
**Immediate Mitigation:**
1.  **Terminate the stuck `inventory-sync-lambda` process.** This should immediately free up database connections and CPU, allowing `inventory-service` to recover.

**Code/Configuration Fixes:**
1.  **Optimize the Lambda**: Review `inventory-sync-lambda` code for inefficient queries, missing indices, or failure to release database connections.
2.  **Connection Pooling**: Ensure the Lambda limits its maximum number of database connections to prevent starving the main service.
3.  **Timeout Configuration**: Review the `inventory-sync-lambda` timeout settings to ensure it fails gracefully rather than hanging indefinitely.

### Prevention
- **Database Isolation**: Move the `inventory-sync-lambda` read operations to a **Read Replica** to avoid impacting the primary writer instance used by `inventory-service`.
- **Alerting**: Add alerts for:
    - Lambda execution duration exceeding a threshold (e.g., > 15 mins).
    - RDS high CPU and connection count.
- **Circuit Breakers**: Implement a circuit breaker pattern in `order-service` to fail fast when `inventory-service` is degraded, rather than waiting for the full 5s timeout.
