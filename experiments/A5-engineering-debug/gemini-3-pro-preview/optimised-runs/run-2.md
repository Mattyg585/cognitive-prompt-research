---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A5
tier: optimised
run: 2
---

# Debug Session: Order Service Intermittent Failures

## Session State 1: Analysis & Reproduction

### 1. Analysis
We have a reliable signal: 15% of orders are failing with `500 Internal Server Error`. The logs explicitly show `context deadline exceeded` in `order-service` after 5003ms, specifically during a call to `inventory-service` (`POST /v2/reserve`).

The `inventory-service` itself is experiencing severe latency degradation (p99 = 4800ms vs normal 200ms). This confirms the issue is downstream of the order service.

### 2. Current Phase
**ISOLATE**

### 3. Action Plan
We need to determine *why* the inventory service is slow. The provided metrics give us the smoking gun:
- `inventory-service` and `inventory-sync-lambda` share the same RDS instance.
- RDS CPU is at 92% (critically high).
- Active connections are at 185 (4.5x normal).
- `inventory-sync-lambda` has been running for >2.5 hours (normally 10 mins).

**Hypothesis:** The stuck `inventory-sync-lambda` is exhausting DB resources (likely connection pool starvation or CPU contention), causing `inventory-service` queries to queue up and time out.

---

## Session State 2: Diagnosis & Verification

### 1. Analysis
The correlation is clear. The lambda started at 00:15 UTC. The problems started around 00:30 UTC. The lambda is still running.

The `order-service` timeout increase (3s -> 5s) 3 days ago actually *helped* mask this slightly, or we would see even more failures. The hard timeout is now being hit at 5s.

The root cause isn't the code in `order-service` or `inventory-service`, but resource contention in the shared persistence layer caused by an auxiliary process.

### 2. Current Phase
**FIX**

### 3. Action Plan
1.  **Immediate Mitigation:** Terminate the running `inventory-sync-lambda` instance to free up RDS resources.
2.  **Verify Recovery:** Watch RDS CPU and connection count drop, and `order-service` error rate return to 0.
3.  **Permanent Fix:** Prevent the lambda from hoarding connections or running indefinitely.

---

## Debug Resolution

### Summary
Intermittent order failures (500s) caused by database resource exhaustion from a stuck background job.

### Root Cause
A scheduled `inventory-sync-lambda` job, which shares the primary RDS instance with the `inventory-service`, entered a stuck state (running >2.5 hours vs 10m expected). This caused:
1.  RDS Connection count to spike to 185 (vs 40 normal).
2.  RDS CPU to hit 92%.
3.  `inventory-service` queries to stall waiting for resources.
4.  `order-service` requests to time out after the configured 5s deadline.

### Fix
1.  **Immediate:** Manually stop the stuck `inventory-sync-lambda` execution.
2.  **Code Change:** Configure a strict execution timeout on the Lambda function (e.g., 15 minutes) to prevent indefinite resource holding.
3.  **Config Change:** Limit the maximum database connections allowed for the Lambda function user (e.g., `ALTER ROLE inventory_lambda_user CONNECTION LIMIT 10;`) to ensure it cannot starve the main service.

### Prevention
1.  **Alerting:** Add an alert for "Lambda duration > 20 minutes".
2.  **Architecture:** Move analytics/sync jobs to a Read Replica to isolate production traffic from background processing load.
