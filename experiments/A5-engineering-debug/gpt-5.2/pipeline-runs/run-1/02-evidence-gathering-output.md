---
model: GPT-5.2
date: 2026-03-15
experiment: A5
tier: pipeline
run: 1
stage: 02-evidence-gathering
---

### Evidence Packet

#### 1) Evidence collected (facts + citations)
- **E1:** `order-service` intermittently fails to process orders with `error="context deadline exceeded"` on the downstream call to `inventory-service` `/v2/reserve`; observed request duration ~5003ms with `timeout_ms=5000` and `retry_count=0`. (source: `...\run-1\01-hypothesis-generation-output.md:12-38`)
- **E2:** Incident context: production (AWS us-east-1). Symptoms began ~00:30 UTC; alert triggered 02:47 UTC. No deployments/infrastructure changes in last 48h. (source: `...\run-1\01-hypothesis-generation-output.md:39-41`)
- **E3:** A scheduled/batch component `inventory-sync-lambda` started ~00:15 UTC and is still running (normally ~10 min). (source: `...\run-1\01-hypothesis-generation-output.md:40-41,47-48`)
- **E4:** The shared RDS PostgreSQL instance (used by `inventory-service` and the Lambda) shows elevated resource usage: CPU ~92% (normal ~25%) and active connections 185 (normal 40). (source: `...\run-1\01-hypothesis-generation-output.md:40-41`)
- **E5:** `inventory-service` latency is elevated: p50 ~180ms and p99 ~4800ms. (source: `...\run-1\01-hypothesis-generation-output.md:40-41`)

#### 2) Hypothesis status update
- **H1:** Supported
  - **Why (cite evidence IDs):** Temporal correlation of long-running `inventory-sync-lambda` with onset (E2, E3) plus shared DB saturation indicators (E4) and tail latency close to client deadline (E5, E1).
  - **What’s still missing (if any):** DB load attribution (by user/app), top waits/top SQL, and confirmation the Lambda is the dominant driver during the incident window.

- **H2:** Unknown
  - **Why (cite evidence IDs):** No direct evidence of lock waits or blocking chains yet; only general DB stress signals are present (E4).
  - **What’s still missing (if any):** `pg_stat_activity`/`pg_locks` snapshot showing lock waits + blocker/blocked mapping during a spike.

- **H3:** Unknown
  - **Why (cite evidence IDs):** Connection count is elevated (E4), but connection attribution (Lambda vs `inventory-service`) and pool saturation metrics are not available.
  - **What’s still missing (if any):** Connections by application/user + `inventory-service` pool stats (in-use/wait), plus evidence of leak/idle-in-transaction.

- **H4:** Unknown
  - **Why (cite evidence IDs):** No pod-level metrics/logs or latency breakdown to separate app CPU/GC from DB time.
  - **What’s still missing (if any):** `inventory-service` pod CPU/mem/throttling + request latency breakdown (app vs DB) for `/v2/reserve`.

- **H5:** Unknown
  - **Why (cite evidence IDs):** No traffic/request-rate or request-attribute skew data is present.
  - **What’s still missing (if any):** `/v2/reserve` RPS before/after 00:30 + any tagged slow samples (SKU/warehouse/user) to test for hot-key/backlog patterns.

- **H6:** Supported
  - **Why (cite evidence IDs):** The observed failure mode is a 5s client deadline being exceeded (E1) while `inventory-service` p99 is near that threshold (E5), consistent with tail-latency tipping requests over the deadline.
  - **What’s still missing (if any):** Correlated client/server timing showing server completion after client cancellation; `inventory-service` access logs/traces for failing request IDs.

#### 3) Leading candidate(s) (inferences; conditional)
Evidence is **insufficient to narrow to a single cause**.

- Conditional leading set (based on current signals only): DB-driven tail latency involving the shared PostgreSQL instance (E4) plausibly linked to the overlapping long-running Lambda execution (E3), with client timeout sensitivity amplifying user-visible failures (E1, E5).

**Minimum next evidence to collect (to discriminate H1 vs H2 vs H3, and validate H6):**
1) RDS Performance Insights/top waits + DB load attribution by user/application for 00:15–now.
2) `pg_stat_activity` + lock/blocking snapshot taken during a latency spike.
3) `inventory-sync-lambda` CloudWatch metrics/log excerpt showing sustained runtime/concurrency (same window).
4) (If available) one correlated failing request ID across order-service + inventory-service with timings.

#### 4) Decision gate
- **Ready for 03-fix-plan?** No
- **If No:** what exact evidence is required before planning a fix?
  - Performance Insights (or equivalent DB attribution) for the incident window.
  - A live DB session/lock snapshot during a spike.
  - Lambda runtime/concurrency evidence for the same window.

#### 5) Evidence requests for the user (if needed)
Please provide the **smallest** artifacts below (any 1–3 are acceptable; priority order listed):

1) **RDS Performance Insights** for 00:15–now:
   - Screenshot/export showing **DB load**, **top waits**, and **top SQL**, ideally broken down by **DB user/application**.

2) **Read-only Postgres snapshots** captured during a spike (copy/paste output is fine):
   - Active/waiting sessions:
     ```sql
     SELECT now() AS ts,
            pid, usename, application_name, client_addr,
            state, wait_event_type, wait_event,
            now() - xact_start AS xact_age,
            now() - query_start AS query_age,
            left(query, 200) AS query_prefix
     FROM pg_stat_activity
     WHERE pid <> pg_backend_pid()
     ORDER BY (wait_event_type IS NOT NULL) DESC, query_start ASC;
     ```
   - Blocking chains (requires pg 9.6+; includes blockers/blocked):
     ```sql
     SELECT a.pid AS blocked_pid,
            pg_blocking_pids(a.pid) AS blocking_pids,
            a.usename, a.application_name,
            a.wait_event_type, a.wait_event,
            now() - a.query_start AS blocked_query_age,
            left(a.query, 200) AS blocked_query_prefix
     FROM pg_stat_activity a
     WHERE cardinality(pg_blocking_pids(a.pid)) > 0;
     ```

3) **Lambda evidence** (`inventory-sync-lambda`) for 00:15–now:
   - CloudWatch metrics: duration, concurrent executions, invocations, errors/throttles.
   - A short log excerpt showing whether it’s progressing vs looping/retrying.

4) (Optional but high value) **One correlated failing request**:
   - `order_id`/request ID from order-service + the matching inventory-service log line(s) with duration and outcome.
