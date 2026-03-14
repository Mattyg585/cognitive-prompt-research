# Blind Evaluation: A5 Engineering Debug

## Task

Debug an intermittent order processing failure in production, following a structured debugging process. The test material presents a scenario where ~15% of orders are failing with 500 errors due to `context deadline exceeded` when `order-service` calls `inventory-service`, which is backed by a PostgreSQL RDS instance being saturated by a long-running Lambda.

## Outputs Evaluated

- **Output A**: A single debug report with Reproduction, Root Cause, Fix, and Prevention sections.
- **Output B**: A single debug report with Reproduction, Diagnosis (hypothesis-elimination), Root Cause, Fix, and Prevention sections.
- **Output C**: A two-stage output — Stage 1 is an investigation report (Reproduction, Isolation, Hypotheses, Root Cause Analysis, Information Gaps); Stage 2 is a fix proposal (Immediate Mitigation, Structural Fix, Implementation Considerations, Verification, Prevention).

---

## Dimension 1: Depth (1-5)

### Output A: 4

Output A correctly identifies the full causal chain: Lambda saturates shared RDS, which degrades inventory-service latency, which causes order-service timeouts. It explains why the intermittent nature follows from the latency distribution, why pod restarts didn't help, and why the timeout increase from 3 days ago is relevant (masking severity). It also notes that read IOPS being normal suggests CPU-bound queries rather than I/O-bound work. This is solid, competent analysis that goes beyond the obvious. However, the treatment of the timeout increase is one-directional — it notes it masks the problem but does not explore the paradox that longer timeouts also *worsen* contention by holding connections longer.

### Output B: 4

Output B presents a structured hypothesis-elimination approach that demonstrates the diagnostic reasoning explicitly. It walks through five hypotheses, eliminating four and converging on the Lambda. The analysis matches Output A's depth on the causal chain but adds a useful observation: it frames the root cause as a "resource isolation failure" — a batch workload and a latency-sensitive production workload sharing a database without any protective mechanism. It also catches the timeout paradox that Output A misses — the 5s timeout consumes the request budget leaving no room for retries. The `pg_stat_activity` tagging suggestion in Prevention is a concrete operational insight. However, the hypothesis-elimination structure, while clear, is somewhat predictable — each hypothesis is eliminated with evidence that was already apparent in the bug report.

### Output C: 5

Output C's investigation stage goes significantly deeper than either A or B. It produces three distinct hypotheses that are not treated as mutually exclusive — Hypothesis 1 (Lambda saturating RDS) is the primary, but Hypothesis 2 (lock contention as a *specific mechanism within* Hypothesis 1) and Hypothesis 3 (connection pool exhaustion as a compounding factor) add analytical layers that the other outputs don't reach. The lock contention hypothesis is genuinely insightful: it observes that the Lambda writing to inventory tables while `/v2/reserve` also writes to inventory tables creates row-level contention, and that the disproportionate p99 blowup (24x vs. p50's 4.5x) is characteristic of lock contention specifically. This is not just restating what's in the bug report — it's applying database internals knowledge to reason about the failure mechanism.

The investigation also surfaces the convoy effect (slow queries hold connections longer, which creates more connections, which further loads the database), the risk of transaction ID wraparound pressure if the Lambda is holding a long transaction, the possibility that the Lambda is stuck vs. slow (which affects whether it self-resolves), and the order reconciliation concern (customers charged without order confirmations, or duplicate orders from retries). The "blast radius" analysis is something neither A nor B attempts.

Stage 2 (fix design) adds depth with the counterintuitive but correct observation that reverting the timeout from 5s to 3s *reduces* total system load during contention — and explains *why* with the connection-holding mechanism. It proposes a 1-1.5s timeout based on the actual normal p99 distribution rather than reactive increases, which shows a deeper understanding of timeout strategy. The implementation considerations section examines side effects, edge cases, regression risks, and dependencies with a thoroughness that neither A nor B approaches.

---

## Dimension 2: Specificity (1-5)

### Output A: 4

Output A references specific evidence from the bug report: the exact metrics (p50 180ms, p99 4800ms, CPU 92%, connections 185), the timeline (00:15 Lambda start, 00:30 failures begin, 02:47 alert), the stack trace location (`inventory.(*Client).Reserve` blocking in `select`), and the specific endpoint (`/v2/reserve`). Fix recommendations include specific commands (`aws lambda put-function-concurrency`), specific PostgreSQL syntax (`ALTER ROLE ... CONNECTION LIMIT 10`), and specific alert thresholds. Every major claim is grounded in evidence from the input. However, some recommendations are somewhat generic — "add a circuit breaker" and "implement retries with backoff" are standard advice that isn't deeply tailored to this specific system's constraints.

### Output B: 4

Output B is similarly well-grounded in the specific evidence. The hypothesis-elimination structure forces specificity — each hypothesis is tested against specific data points. The observation about `retry_count=0` meaning the timeout consumes the full request budget is a specific, evidence-grounded insight. The `pg_stat_activity` tagging suggestion (distinct application names for batch vs. production connections) is practical and specific. Fix recommendations are slightly less detailed than Output A (no specific commands or SQL), but the structural fix section is well-reasoned for this specific scenario.

### Output C: 5

Output C is the most specific of the three. The investigation stage maps every observation to specific evidence and explicitly labels what is confirmed vs. unresolved. The connection count analysis (185 active, db.r6g.xlarge typically has 400-800 max_connections, so not at hard limit but contributing to CPU overhead) demonstrates instance-class-specific knowledge. The lock contention hypothesis reasons specifically about the interaction between inventory sync *writes* and reservation *writes* on the same rows — this is not generic advice but a specific prediction about what `pg_stat_activity` and `pg_locks` would show.

The fix design stage is deeply specific: `ALTER ROLE sync_lambda CONNECTION LIMIT 5`, `ALTER ROLE sync_lambda SET statement_timeout = '30s'`, timeout should be 1-1.5s based on the actual normal p99 of 200ms. The implementation considerations are tailored to this exact scenario: read replica introduces replication lag which is acceptable because the warehouse data is already hours old; if the Lambda legitimately needs a large annual reconciliation, the connection limit may cause it to fail and it needs chunked processing; the circuit breaker changes the failure mode from "slow failure" to "fast failure" and downstream error handling must be updated. The information gaps section lists 10 specific pieces of data that would refine the analysis, each tied to a specific diagnostic purpose. Nothing in Output C reads as templated.

---

## Dimension 3: Completeness (1-5)

### Output A: 4

Output A covers the essential ground well: reproduction, root cause chain, immediate/short-term/long-term fixes, and prevention. It addresses why pod restarts didn't help, why the timeout increase matters, and includes architectural recommendations (read replica, connection pooling, database separation). The prevention section covers monitoring, runbooks, and process (shared-resource review). One gap: it does not address order reconciliation — customers who were charged without order confirmation or who placed duplicate orders during the incident. It also does not discuss what data would be needed to confirm the diagnosis (Lambda logs, `pg_stat_activity`, etc.).

### Output B: 4

Output B covers similar ground to A, with the addition of the structured diagnosis section. The fix section is organized into Immediate/Short-term/Structural tiers with clear rationale. Prevention includes the canary/integration test idea and the `pg_stat_activity` tagging suggestion, both practical additions. Like Output A, it does not address order reconciliation or blast radius to other services. It does mention the cross-team review process. The "why the timeout increase is relevant" analysis is more nuanced than A's, noting that `retry_count=0` indicates no retries are possible within the timeout budget.

### Output C: 5

Output C is the most complete. The investigation stage covers everything A and B cover, plus: three distinct hypotheses with explicit supporting/contradicting evidence for each, the convoy effect, transaction ID wraparound risk, blast radius analysis (other services on the same RDS, order reconciliation needs), and a structured information gaps section listing 10 specific items. The fix design stage adds: the counterintuitive timeout revert recommendation with explanation, order reconciliation as an explicit action item, implementation considerations covering side effects/edge cases/regression risks/dependencies, a detailed verification plan for each component of the fix, and four prevention measures each explicitly linked to the root cause. The completeness is achieved without padding — each section contributes distinct analytical value.

---

## Dimension 4: Audience Awareness (1-5)

### Output A: 4

Output A reads as a competent incident report written for a senior engineer or engineering manager. The structure (Reproduction, Root Cause, Fix, Prevention) is standard incident-response format. The writing is clear and direct. The fix section is organized by urgency tier, which is appropriate for the audience — the on-call engineer needs to know what to do *now* vs. what to do *later*. The tone is appropriately confident without being overconfident. The AWS CLI command for stopping the Lambda is a practical touch for an on-call engineer.

### Output B: 4

Output B's hypothesis-elimination structure serves a dual audience: it helps the on-call engineer understand *why* certain remediation steps (pod restarts, network checks) didn't work, and it documents the reasoning for the post-incident review. The framing of the root cause as a "resource isolation failure" elevates the analysis beyond the specific incident to the architectural concern — appropriate for a team lead or architect who will need to approve the structural fix. The tone is slightly more analytical than Output A, which suits a post-incident write-up. The `pg_stat_activity` tagging suggestion shows awareness that the audience will face future incidents and need operational tools.

### Output C: 5

Output C demonstrates the strongest audience awareness. The two-stage structure maps naturally to two different audiences and two different moments in the incident lifecycle:

Stage 1 (investigation) is written for a senior engineer or incident commander who needs to understand the problem *before* committing to a fix. It presents hypotheses with explicit confidence levels, acknowledges what's unknown, and doesn't leap to solutions. The "blast radius" and "information gaps" sections anticipate the questions an incident commander would ask. The explicit distinction between "root cause" and "proximate trigger" serves the post-incident review process.

Stage 2 (fix design) is written for the engineer who will implement the fix and the tech lead who will review it. It separates immediate mitigation from structural fixes and explains *why* each action is correct — including counterintuitive ones (reverting the timeout increase). The implementation considerations section anticipates objections and risks that a reviewer would raise. The verification section provides specific acceptance criteria. The prevention section links each measure to the root cause, which is what a process-improvement review would need. The dependencies section identifies the cross-team coordination required, which is critical for execution.

---

## Dimension 5 (Domain-Specific): Correctness (1-5)

### Output A: 4

Output A correctly identifies the root cause: the `inventory-sync-lambda` saturating the shared RDS instance. The causal chain (Lambda -> RDS saturation -> inventory-service latency -> order-service timeout) is accurate. The explanation of why read IOPS being normal suggests CPU-bound rather than I/O-bound work is correct. The explanation of why the 15% failure rate reflects the tail of the latency distribution is correct. The fix recommendations are sound: killing the Lambda, read replica, connection limits, circuit breakers.

Minor correctness issue: the suggestion to "add connection pooling (e.g., RDS Proxy)" is presented as an alternative to a read replica, but these solve different problems — RDS Proxy manages connection multiplexing while a read replica offloads read workload. They are complementary, not substitutes. The suggestion to "rate-limit the Lambda's database queries" is vague and less practical than connection limits or statement timeouts.

### Output B: 4

Output B's diagnosis is correct throughout. The hypothesis-elimination approach adds rigour — each eliminated hypothesis is correctly dismissed with specific evidence. The root cause identification is accurate. The framing as "resource isolation failure" is architecturally correct. The observation about the timeout consuming the retry budget (retry_count=0) is a correct and relevant insight. The fix recommendations are sound.

Minor correctness issue: the suggestion to "schedule [the Lambda] during a genuine low-traffic window and implement connection pooling with priority queuing so production queries are always served first" is directionally correct but "priority queuing" at the database level is not straightforward in PostgreSQL — there is no native query priority mechanism. This would need to be approximated via connection limits and resource management.

### Output C: 5

Output C is the most technically precise. The investigation stage demonstrates strong correctness:
- The lock contention hypothesis correctly identifies that the Lambda writing to inventory tables and `/v2/reserve` also writing creates row-level contention, and correctly predicts that `pg_stat_activity` and `pg_locks` would confirm this.
- The convoy effect observation is technically accurate: slow queries hold connections longer, increasing active connection count, adding CPU overhead from connection management, deepening contention.
- The transaction ID wraparound risk from long-running transactions is a real PostgreSQL concern that the other outputs don't mention.
- The distinction between the Lambda being stuck (deadlocked) vs. slow (burning CPU on legitimate work) is operationally important and correctly framed.
- The observation that 185 connections on a db.r6g.xlarge (typically 400-800 max_connections) is elevated but likely below the hard limit is technically accurate for that instance class.

The fix design stage adds:
- The timeout revert recommendation is counterintuitive but technically correct — under contention, shorter timeouts reduce steady-state connection hold time and therefore total system load.
- The recommendation to set the timeout at 1-1.5s based on the normal p99 of 200ms reflects correct timeout engineering (allow headroom above normal p99 but not orders of magnitude above it).
- `ALTER ROLE sync_lambda SET statement_timeout = '30s'` is a real PostgreSQL mechanism that would prevent individual runaway queries.
- The warning that killing a Lambda mid-transaction will cause PostgreSQL rollback, which can itself be expensive on a loaded instance at 92% CPU, is technically accurate and operationally important.
- The read replica replication lag concern and the observation that it's acceptable because warehouse data is already hours old shows correct reasoning about consistency requirements.

No significant technical errors identified in Output C.

---

## Summary

| Dimension | Output A | Output B | Output C | A vs B | A vs C | B vs C |
|-----------|----------|----------|----------|--------|--------|--------|
| Depth | 4 | 4 | 5 | Tie | C +1 | C +1 |
| Specificity | 4 | 4 | 5 | Tie | C +1 | C +1 |
| Completeness | 4 | 4 | 5 | Tie | C +1 | C +1 |
| Audience Awareness | 4 | 4 | 5 | Tie | C +1 | C +1 |
| Correctness | 4 | 4 | 5 | Tie | C +1 | C +1 |
| **Total** | **20** | **20** | **25** | **Tie** | **C +5** | **C +5** |

**Overall preference**: C > A = B

**Key differences**:

Output A and Output B are very close in quality. Both correctly identify the root cause, trace the causal chain, and propose reasonable fixes. Output B's hypothesis-elimination structure is more rigorous in showing its work, while Output A is more concise and action-oriented. These are stylistic differences rather than quality differences — a reasonable reader could prefer either.

Output C is in a different tier. The separation between investigation and fix design allows each stage to do its work without compromise. The investigation stage generates hypotheses, weighs evidence, identifies what's unknown, and assesses blast radius — all without prematurely jumping to solutions. The fix design stage then proposes solutions with full awareness of side effects, edge cases, regression risks, and verification criteria.

Specific things Output C does that A and B do not:
- The lock contention hypothesis as a specific mechanism within the broader saturation diagnosis, with a technically correct prediction about how it would manifest in `pg_stat_activity` and `pg_locks`.
- The convoy effect observation explaining the self-reinforcing nature of the connection count increase.
- The transaction ID wraparound risk from potential long-running Lambda transactions.
- The counterintuitive but correct recommendation to revert the timeout from 5s to 3s *and the explanation of why this helps under contention*.
- The order reconciliation concern as an explicit action item.
- The blast radius analysis identifying risks to other services on the same RDS instance.
- The 10-item information gaps list, each tied to a diagnostic purpose.
- The implementation considerations section covering side effects, edge cases, regression risks, and cross-team dependencies.
- The verification plan with specific acceptance criteria for each component of the fix.

**Magnitude**: Moderate to Large.

The difference between A/B and C is meaningful in practice. Outputs A and B would give a competent on-call engineer what they need to resolve the immediate incident. Output C would give the same engineer a better understanding of the failure, a more complete set of immediate actions (including order reconciliation and the timeout revert), and a structural fix proposal that has already anticipated reviewer objections and cross-team coordination needs. In a real incident, Output C would lead to a faster, more confident response and a more complete post-incident process.

The difference between A and B is negligible. They are comparable in quality and reach the same conclusions through slightly different structures.

---

## Diagnostic Observations

1. **All three outputs correctly identify the root cause.** This is a well-constrained debugging scenario where the evidence strongly points to one conclusion. The differentiation is not in *what* they conclude but in *how thoroughly they reason about it* and *how completely they address its consequences*.

2. **Output C's two-stage structure creates space for genuine investigation.** In Outputs A and B, the diagnosis and fix are interleaved in the same document, which subtly compresses the investigation — the writer knows they need to get to the fix, so the diagnosis becomes a path to the fix rather than an exploration of the problem. Output C's Stage 1 investigates without knowing (or needing to know) what the fix will be. This produces the lock contention hypothesis, the convoy effect observation, and the blast radius analysis — none of which serve the fix directly, but all of which improve the *understanding* of the failure.

3. **The timeout revert is a litmus test.** Output C is the only one that recommends reverting the timeout increase from 5s to 3s *and explains why shorter timeouts reduce system load under contention*. Outputs A and B both note that the timeout increase masks the problem, but neither takes the analytical step of recommending the revert. This is a case where the "obvious" answer (longer timeout = more requests succeed) is wrong under contention, and Output C demonstrates the deeper systems thinking needed to see it.

4. **Output C's information gaps section is diagnostic work, not filler.** Each of the 10 items identifies a specific piece of data that would either confirm the diagnosis or reveal a different failure mechanism. This reflects genuine epistemic humility — the analysis is confident but explicitly acknowledges its limits and tells the reader exactly what to check. Outputs A and B present their diagnoses with less qualification.

5. **Neither A nor B addresses order reconciliation.** This is a significant omission for a customer-impacting incident. Failed orders during a 2+ hour window where some customers may have been charged without receiving confirmations is a business-critical concern. Output C identifies this explicitly and frames it as "not an engineering fix, but it needs to be initiated now" — which demonstrates awareness of the full incident response scope.
