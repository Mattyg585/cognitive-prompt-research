---
model: GPT-5.3-Codex (gpt-5.3-codex)
date: 2026-03-15
experiment: A5
tier: pipeline
run: 1
stage: stage-1-investigator
---

## Investigation: Intermittent `order-service` 500s on Inventory Reservation

### Reproduction
- **Expected**: `order-service` should reserve inventory via `inventory-service /v2/reserve` within normal latency and complete orders successfully.
- **Actual**: ~15% of orders fail with `500` and `context deadline exceeded` after ~5003ms.
- **Conditions**: Intermittent failure pattern. Same user can retry and sometimes succeed. Incident began around 00:30 UTC.

### Isolation
- **Affected component(s)**: Call path `order-service -> inventory-service -> PostgreSQL (RDS)`.
- **Timeline**:
  - 00:15 UTC: `inventory-sync-lambda` starts.
  - ~00:30 UTC: order failures begin.
  - 02:47 UTC: alert fires.
  - At report time: Lambda still running despite expected 10-minute completion.
- **What changed**:
  - No service deploys in last 48h for order/inventory services.
  - 3 days ago: `order-service` timeout increased from 3s to 5s.
  - 3 weeks ago: `inventory-sync-lambda` introduced.
- **Resource state**:
  - RDS CPU 92% (normal ~25%).
  - Active connections 185 (normal ~40).
  - Read IOPS normal.
  - `inventory-service` p50 180ms (normal 40ms), p99 4800ms (normal 200ms).

### Hypotheses

#### Hypothesis 1: `order-service` regression
**Statement**: A local order-service bug introduced timeout behavior.
**Supporting evidence**: Timeout occurs in order-service logs.
**Contradicting evidence**: No recent deploy; stack trace indicates downstream wait; timeout tied to inventory call.
**Unresolved**: None significant. Current evidence weak for this hypothesis.

#### Hypothesis 2: `inventory-service` internal app issue
**Statement**: Inventory pods have local instability or bug.
**Supporting evidence**: Elevated inventory latency.
**Contradicting evidence**: Restarting pods had no improvement; no recent deploy.
**Unresolved**: Could still have data-dependent slow query paths, but evidence points downstream.

#### Hypothesis 3: Shared RDS saturation from runaway `inventory-sync-lambda`
**Statement**: Long-running Lambda consumes DB compute/connection capacity, increasing inventory tail latency past order timeout.
**Supporting evidence**:
- Strong temporal alignment (Lambda starts before failures).
- Lambda runtime grossly exceeds normal behavior.
- RDS CPU/connections sharply elevated.
- Inventory p99 near timeout boundary.
- Intermittency matches tail-latency contention pattern.
**Contradicting evidence**: None material from provided data.
**Unresolved**:
- Exact mechanism split: CPU-heavy query plans vs lock contention vs both.
- Why Lambda run diverged tonight (data volume, query plan regression, retry loop, deadlock/wait pattern).

### Root Cause Analysis
**Root cause**: Shared RDS resource contention driven by abnormally long `inventory-sync-lambda` execution on the same DB instance used by `inventory-service`.

**Proximate trigger**: Tonight’s Lambda run exceeded normal duration by an order of magnitude and remained active for hours.

**Contributing factors**:
- Lack of resource isolation/guardrails between batch and transactional workloads.
- Elevated timeout (5s) can increase in-flight waits under degradation.
- Absence of early alerting on Lambda runtime anomaly.

**Confidence**: High for causal chain (Lambda -> RDS saturation -> inventory tail latency -> order timeout). Moderate for exact internal DB mechanism without lock/SQL profiling data.

**Blast radius**:
- Any service sharing this RDS may be degraded.
- Incident can recur on future nightly sync runs without structural isolation.
- Potential business-impact follow-ups (failed/retried orders requiring reconciliation).

### Information Gaps
- Lambda logs/progress state and query pattern for this run.
- `pg_stat_activity` / lock metrics for active blockers/waiters.
- Top SQL by CPU/wait from Performance Insights.
- Per-consumer DB connection attribution.

