---
model: GPT-5.3-Codex (gpt-5.3-codex)
date: 2026-03-15
experiment: A5
tier: optimised
run: 1
---

## Debug Report: Intermittent Order Processing Failures from Shared DB Saturation

### Reproduction
- **Expected**: Order creation should succeed consistently; inventory reservation should return quickly from `inventory-service /v2/reserve`.
- **Actual**: ~15% of orders fail with `500` after `context deadline exceeded` around 5000ms in `order-service` when calling `inventory-service`.
- **Steps/Conditions**:
  1. Place orders during incident window (~00:30 UTC onward).
  2. Observe intermittent 5s timeout failures (`handler.go:142`, `timeout_ms=5000`).
  3. Retry and sometimes succeed, indicating a latency-tail contention pattern, not deterministic payload failure.

### Diagnosis
**Hypothesis A: `order-service` code regression**
- Against: no deploys in 48h; stack trace shows timeout waiting on downstream call, not local panic/logic failure.
- Result: unlikely primary cause.

**Hypothesis B: network/DNS path issue**
- Against: connectivity and DNS already verified; behavior is slow response, not connection failure.
- Result: low likelihood.

**Hypothesis C: `inventory-service` app instability**
- Against: pod restarts did not improve symptoms; metrics point to external dependency pressure.
- Result: not root cause.

**Hypothesis D: shared RDS saturation triggered by long-running `inventory-sync-lambda`**
- For: timeline alignment (Lambda 00:15 -> failures ~00:30), Lambda still running far past normal 10m, RDS CPU 92%, connections 185, inventory-service p99 4800ms.
- Also consistent with intermittent failure rate: some requests hit normal-ish latency, tail requests exceed 5s timeout.
- Result: strongest explanation.

Narrowing logic: the combined timeline + resource metrics + ineffective pod restart makes shared DB contention the most coherent diagnosis.

### Root Cause
`inventory-sync-lambda` is running abnormally long and consuming substantial shared RDS capacity, causing `inventory-service` latency spikes and `order-service` timeout failures.

- **Proximate trigger**: anomalously long nightly Lambda execution.
- **Systemic root cause**: no resource isolation between batch sync and latency-sensitive reservation path on the same DB.
- **Contributing factor**: 5s timeout can increase in-flight wait pressure under degradation.

### Fix
**Immediate**
1. Stop/disable current Lambda run to relieve DB pressure.
2. Validate recovery (RDS CPU/connections and inventory latency).

**Targeted controls**
1. Constrain Lambda DB role connections and add execution timeout.
2. Break sync into bounded transactions/batches.
3. Add dependency circuit breaker for `order-service -> inventory-service`.

**Structural**
1. Separate batch sync load from transactional path (read replica and controlled primary writes, or dedicated DB capacity).
2. Institute cross-team change review for shared production DB consumers.

### Prevention
- Alert on Lambda runtime anomaly and failed completion window.
- Alert on RDS saturation thresholds with ownership routing.
- Add incident runbook for this failure mode.
- Add staged load test covering concurrent reserve + sync behavior.
- Enforce DB access guardrails (connection caps, timeout defaults) for batch workloads.

