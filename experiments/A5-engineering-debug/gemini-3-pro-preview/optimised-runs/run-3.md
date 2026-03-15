---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A5
tier: optimised
run: 3
---

# Session State

### 1. Analysis
The incident involves 15% of orders failing with `500 Internal Server Error` due to timeouts (`context deadline exceeded`). The issue is isolated to the `inventory-service`, which shows elevated latency (p99 = 4800ms) and is backed by a shared RDS instance. The RDS instance is under high load (92% CPU, 185 active connections).

A strong correlation exists with the `inventory-sync-lambda`, which started 15 minutes before the incident (00:15 UTC) and is currently "stuck" or running unusually long. This Lambda connects to the same RDS instance. The evidence strongly suggests the Lambda is starving the `inventory-service` of database resources.

### 2. Current Phase
**Diagnose**

### 3. Action Plan
*   **Hypothesis:** The stuck `inventory-sync-lambda` is causing database resource exhaustion (CPU and connection saturation), leading to timeouts in the `inventory-service`.
*   **Verification:** Terminate the `inventory-sync-lambda` execution immediately.
*   **Expected Result:** RDS CPU and connection counts should drop; `inventory-service` latency should return to normal; order errors should stop.

---

# Debug Resolution

*   **Summary:** The critical incident was caused by the `inventory-sync-lambda` job exhausting resources on the shared production RDS instance, causing `inventory-service` queries to time out.
*   **Root Cause:** The `inventory-sync-lambda` (a nightly batch job) failed to complete and remained active, consuming 92% CPU and holding 185 database connections (vs normal 40). This resource contention blocked the OLTP `inventory-service`, causing it to miss the 5s deadline for `order-service` requests.
*   **Fix:**
    *   **Immediate:** Manually terminated the stuck `inventory-sync-lambda` process.
    *   **Code:** Fix the connection leak/inefficiency in the Lambda code. Ensure it closes connections properly.
    *   **Configuration:** Set a hard timeout on the Lambda function (e.g., 15 mins) to prevent indefinite runs.
*   **Prevention:**
    *   **Architecture:** Move the reporting/sync workload (Lambda) to a Read Replica to isolate it from the critical path (OLTP).
    *   **Monitoring:** Create a "Lambda Duration" alert.
    *   **Resiliency:** Implement connection pooling limits for the Lambda to prevent it from saturating the DB.