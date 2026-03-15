---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A5
tier: pipeline
run: 1
stage: 02-debug-diagnostician
---

# Diagnosis Report

## Root Cause Analysis
The root cause is **resource contention on the shared PostgreSQL RDS instance**, specifically high CPU usage (92%) and connection exhaustion (185 connections). This is triggered by the `inventory-sync-lambda` batch job running concurrently with peak traffic.

This contention degrades the performance of the `inventory-service`, pushing its p99 latency to ~4800ms. The `order-service`, which depends on `inventory-service`, has a hard timeout of 5000ms. The proximity of the latency to the timeout threshold (combined with network overhead and variance) causes approximately 15% of requests to exceed the deadline, resulting in `500 Internal Server Error` responses with `context deadline exceeded`.

The recent configuration change (increasing timeout from 3s to 5s) merely masked the symptom for some requests but did not address the underlying resource bottleneck.

## Supporting Evidence
- **Timing Correlation**: Failures occur at ~5003ms, matching the 5000ms timeout plus overhead.
- **Resource Correlation**: High RDS CPU and connection counts coincide with the extended runtime of `inventory-sync-lambda`.
- **Latency Data**: `inventory-service` p99 (4800ms) is dangerously close to the `order-service` timeout (5000ms).
- **Log Evidence**: "context deadline exceeded" errors in `order-service` explicitly point to the timeout mechanism aborting the call to `inventory-service`.

## Proposed Solution

### 1. Immediate Operational Fix (Root Cause)
- **Action**: Stop or reschedule the `inventory-sync-lambda` to run during off-peak hours.
- **Long-term**: Refactor the Lambda to use a read-replica or optimize its batch processing to reduce DB load.

### 2. Code Resilience Fix (Mitigation)
- **Target Files**: `order-service/internal/inventory/client.go`
- **Specific Changes**:
  - Implement a **Circuit Breaker** pattern (e.g., using `gobreaker`) around the `Reserve` method.
  - **Logic**:
    - Configure the breaker to open if the error rate exceeds a threshold (e.g., 20%) or if consecutive failures occur.
    - When the circuit is open, fail immediately (Fail Fast) with a fallback error or cached response (if applicable), rather than waiting for the 5s timeout.
    - This prevents `order-service` thread/connection pool exhaustion and prevents it from hammering the already struggling `inventory-service`.
- **Verification Plan**:
  - **Unit Test**: Mock the `inventory-service` client to simulate slow responses and verify the circuit breaker opens after the configured threshold.
  - **Integration Test**: Simulate high latency in the downstream service and verify `order-service` returns 503 (or fallback) immediately instead of 500 after 5s.
- **Constraints**:
  - Circuit Breaker state must be maintained in memory.
  - Ensure failure threshold is tuned to avoid flapping during minor blips.
