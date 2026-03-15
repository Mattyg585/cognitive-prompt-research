---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A5
tier: optimised
run: 1
---

I will conduct a structured debugging session to diagnose the intermittent `500 Internal Server Error` in the `order-service`.

### Phase 1: Triage & Observation

I am applying the **Skeptic Lens** to the error message: `context deadline exceeded` with `duration_ms=5003`.
*   **Observation:** The error is a timeout. The `order-service` gave up waiting for `inventory-service` after 5 seconds.
*   **Context:** The timeout config was recently increased to 5s, and the error shows it hitting exactly that limit. This confirms the failure is due to latency, not an immediate crash or logic bug.
*   **Scope:** 15% of orders are failing. This suggests resource contention or a bottleneck rather than a total outage.

### Phase 2: Isolation & Diagnosis

I am applying the **Boundary Lens** to isolate the fault domain.
*   The `order-service` is merely the reporter. The stack trace shows the blockage is in `inventory.(*Client).Reserve`, waiting for the downstream `inventory-service`.
*   **Investigation:** Why is `inventory-service` slow?
    *   Metrics show `inventory-service` p99 latency is 4800ms.
    *   RDS (Database) CPU is at 92% (Critical).
    *   RDS Active connections are 185 (4.6x normal).

I am applying the **Temporal Lens** to find the trigger.
*   **What changed?** The `inventory-sync-lambda` started at 00:15 UTC.
*   **Correlation:** The Lambda is *still running* (unusual, usually takes 10 mins). The errors started at 00:30 UTC, shortly after the Lambda began.

### Phase 3: Root Cause Confirmation

**Hypothesis:** The stuck `inventory-sync-lambda` is exhausting database resources (CPU and connections), causing the user-facing `inventory-service` to starve and time out.

**Mechanism:**
1.  The `inventory-sync-lambda` (batch job) started and failed to complete.
2.  It has consumed a large number of DB connections (185 vs 40) and high CPU (92%).
3.  When `inventory-service` (OLTP) tries to query the DB for a user order, it enters a queue for resources.
4.  The query takes >5 seconds to execute due to contention.
5.  `order-service` times out waiting for the response.

### Phase 4: Resolution

We need to relieve the pressure on the database immediately.

**Immediate Action:**
*   Kill the stuck `inventory-sync-lambda` process. This should drop DB connections and CPU usage, restoring `inventory-service` performance.

**Prevention:**
*   The Lambda needs a timeout.
*   Batch jobs should probably use a separate connection pool or a read replica to avoid impacting the write master used by OLTP services.

***

## Debug Report: Inventory Sync Lambda Starving Order Service

### Context
- **Impact**: 15% of customer orders failing with `500 Internal Server Error`.
- **Trigger**: `inventory-sync-lambda` scheduled job started at 00:15 UTC and hung.

### Root Cause Analysis
The `inventory-sync-lambda` is stuck in a loop or processing an abnormal batch, holding 140+ extra database connections and consuming 92% CPU on the shared RDS instance. This resource starvation causes `inventory-service` queries to slow down drastically (p99 ~4.8s), leading `order-service` to hit its 5-second timeout and fail the request.

### The Fix
**Immediate:**
1.  Terminate the running `inventory-sync-lambda` function execution via AWS Console or CLI.
2.  Verify RDS metrics (CPU and connections) return to normal levels.

**Code/Config Changes:**
1.  **Add Timeout:** Configure the Lambda with a hard execution timeout (e.g., 15 minutes) to prevent indefinite hanging.
2.  **Throttling:** Limit the Lambda's maximum database connections or concurrency to reserve capacity for the OLTP `inventory-service`.
3.  **Isolation:** Point the Lambda to a Read Replica if it only needs read access, or investigate why it locked up (logs review required).

### Verification
- Monitor `order-service` error rate (should drop to 0%).
- Check `inventory-service` p99 latency (should return to ~200ms).
- Confirm RDS CPU drops below 30%.
