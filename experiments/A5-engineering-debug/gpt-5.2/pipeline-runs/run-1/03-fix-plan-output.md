---
model: GPT-5.2
date: 2026-03-15
experiment: A5
tier: pipeline
run: 1
stage: 03-fix-plan
---

### Fix Plan Packet

#### 1) Selected root cause (conditional)
- **Claim:** Evidence is currently **insufficient to select a single root cause**. Conditional leading candidate is **DB-driven tail latency** in `inventory-service` (shared RDS PostgreSQL) plausibly linked to the overlapping long-running `inventory-sync-lambda`, causing `/v2/reserve` p99 to approach the `order-service` 5s client deadline and intermittently exceed it.
- **Confidence:** Low
- **Evidence:** E1, E3, E4, E5, E2
- **Remaining uncertainty (if any):** Whether the DB stress is primarily (a) Lambda-driven load (H1), (b) lock contention/blocking (H2), (c) connection/pool saturation or leak (H3), or (d) `inventory-service` node/pod resource issues vs DB time (H4). Attribution and a live snapshot during spikes are missing.

#### 2) Fix strategy
- **Primary approach:** **Blocked pending required evidence.** Collect the minimum discriminating evidence before choosing a fix:
  1) RDS Performance Insights (or equivalent) for ~00:15–now showing DB load, top waits, top SQL, and breakdown by DB user/application (E4; Decision Gate).
  2) A `pg_stat_activity` + lock/blocking snapshot captured during a latency spike to confirm/deny lock-driven blocking (Decision Gate).
  3) `inventory-sync-lambda` CloudWatch runtime/concurrency evidence for the same window to confirm it is the dominant contributor (E3; Decision Gate).
  4) If available, one correlated failing request ID across `order-service` and `inventory-service` with timings to validate client-cancel vs server-complete behavior (E1, E5).
- **Why this addresses the root cause:** Selecting a remediation without attribution risks treating symptoms (e.g., timeouts) while leaving the dominant DB constraint unchanged; the evidence above directly discriminates H1 vs H2 vs H3 and validates the deadline sensitivity (E1, E4, E5).
- **Alternatives considered (brief):** Immediate timeout/retry changes in `order-service` (symptom relief) were not selected as a primary strategy because the root cause is not yet confirmed and may amplify load on an already stressed DB/service.
- **Risks / side effects:** Delay in mitigation while collecting evidence; however, acting without attribution risks worsening DB load or masking the true driver.

#### 3) Change plan (implementation steps)
- Step-by-step actions.
  1) Pull RDS Performance Insights for 00:15–now; capture: DB load, top waits, top SQL, and attribution by user/application.
  2) During an active spike, capture `pg_stat_activity` and blocking-chain output to detect lock waits and identify blockers/blocked.
  3) Pull `inventory-sync-lambda` metrics/logs for duration, concurrency, invocations, errors/throttles in the same time window.
  4) Identify one failing `order-service` request (or order_id) and correlate to `inventory-service` access/log/trace to confirm server-side timing relative to the 5s client deadline.
  5) Decide the fix branch based on the evidence outcome:
     - If DB load/top SQL is dominated by the Lambda: plan to reduce Lambda concurrency, add pacing/backoff, fix inefficient queries, and/or reschedule/partition workload.
     - If top waits show lock contention: plan to eliminate long transactions, add/adjust indexes, rewrite queries to avoid hot-row locks, and/or adjust isolation/locking patterns.
     - If connection pressure dominates: plan to tune pools/limits, fix leaks/idle-in-transaction, and add circuit-breaking to prevent thundering herds.
     - If app resource limits dominate: plan to scale `inventory-service` pods and reduce per-request work (while confirming DB time).
  6) Only after selecting the evidence-backed branch, draft a minimal code/config change set.
- If code changes are involved, include:
  - **Files/areas likely touched:**
    - `order-service`: client timeout/retry/circuit-breaker for `inventory-service` `/v2/reserve`.
    - `inventory-service`: DB query path for `/v2/reserve`, connection pooling, transaction boundaries.
    - `inventory-sync-lambda`: concurrency/scheduling, batch sizing, retry/backoff, query efficiency.
    - RDS/Postgres: indexes, parameter tuning (only if evidence points there).
  - **Change sketch:** (conditional; choose one branch after evidence)
    - Lambda-dominant: reduce concurrency; add bounded batch loop + sleep/jitter; ensure idempotent progress markers; optimize top SQL.
    - Locking: shorten transactions; avoid `SELECT ... FOR UPDATE` hot paths; add missing indexes; move heavy writes out of request path.
    - Connections: enforce max pool; fail-fast when pool exhausted; eliminate leak/idle-in-txn; add bulkheads.

#### 4) Test & verification plan (pre-merge)
- **Repro test:** Reproduce the failure mode by generating sustained reserve traffic while the suspected driver is active (e.g., Lambda run) and confirm whether `inventory-service` p99 approaches the 5s deadline and triggers `context deadline exceeded` in `order-service` (E1, E5).
- **Regression tests:**
  - Ensure `/v2/reserve` correctness under concurrency (no double-reserve, no negative inventory), especially if changing locking/transactions.
  - Ensure Lambda progress/idempotency if changing batching or retries.
- **Commands to run:** N/A (repo/code not provided in evidence). Run the existing unit/integration/load tests for the affected services, plus any DB migration checks if indexes/schema change.
- **Expected outputs / pass criteria:**
  - `order-service` reserve failures attributable to timeouts drop to baseline.
  - `inventory-service` p99 drops materially below 5s (target: comfortably under deadline with headroom).
  - RDS CPU/connection counts return toward normal ranges, and top waits/top SQL no longer show the incident driver.

#### 5) Rollout / rollback plan (if relevant)
- **Safe rollout steps:**
  - Prefer a canary (small % traffic) for `inventory-service`/`order-service` changes; for Lambda changes, start with reduced concurrency/batch size and monitor.
  - Apply DB index changes off-peak where possible; use concurrent index builds if supported and safe.
- **Observability signals to watch:**
  - `order-service`: rate of `context deadline exceeded` on `inventory-service` calls; overall order success rate.
  - `inventory-service`: `/v2/reserve` latency distribution (p50/p95/p99), DB time vs app time, error rates.
  - RDS: CPU, active connections, DB load, top waits, top SQL.
  - Lambda: duration, concurrency, error/throttle rate, progress indicators.
- **Rollback triggers:**
  - Increased reserve/order failure rate, rising p99 latency, new DB lock waits, sustained rise in CPU/connections, or correctness anomalies (inventory inconsistencies).

#### 6) Handoff gate
- State what to provide to `04-verification` (commands, expected outcomes, artifacts).
  - Performance Insights export/screenshot for 00:15–now (DB load, top waits, top SQL, attribution by user/application).
  - `pg_stat_activity` and blocking-chain outputs captured during a spike.
  - `inventory-sync-lambda` metrics/log excerpt for the same window.
  - One correlated failing request (order-service ↔ inventory-service) with timings.
  - Once a fix branch is selected: the exact change list (diff/config), the test commands run, and the observed before/after metrics (p99, error rate, DB load).
