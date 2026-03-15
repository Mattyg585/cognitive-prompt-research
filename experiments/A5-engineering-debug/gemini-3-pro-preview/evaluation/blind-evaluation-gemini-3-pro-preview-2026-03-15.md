# Blind Evaluation: Engineering Debug (A5)

**Experiment:** A5 (Engineering Debug)
**Model:** gemini-3-pro-preview
**Date:** 2026-03-15

## 1. Depth

**Output A (Baseline):** 4/5
The output correctly identifies the root cause (resource contention from `inventory-sync-lambda`) and explains the cascading failure mechanism (RDS CPU spike -> Inventory Service timeout -> Order Service 500s). It goes beyond surface level by linking the specific metrics (185 connections) to the failure mode.

**Output B (Optimised):** 4/5
The output provides a similarly deep analysis. It adds value by structuring the investigation into phases (Triage, Isolation, Root Cause) and using specific "Lenses" (Skeptic, Boundary) to justify the conclusions. It clearly separates observations from hypotheses.

## 2. Specificity

**Output A (Baseline):** 5/5
Extremely specific. It quotes exact timestamps (00:15 UTC), error messages (`context deadline exceeded`), latency figures (4800ms), and resource metrics (92% CPU, 185 connections). It references the specific services and lambdas involved.

**Output B (Optimised):** 5/5
Equally specific. It uses the same evidence base to build its case. It explicitly correlates the start time of the lambda with the onset of errors.

## 3. Natural Variation

**Output A (Baseline):** N/A
Only one run was provided, so variation cannot be assessed.

**Output B (Optimised):** 4/5
Across three runs, the model demonstrates healthy variation in structure while maintaining consistency in findings. Run 1 uses "Lenses" (Skeptic, Boundary), Run 2 uses a "Session State" format, and Run 3 uses a standard "Analysis/Action Plan" structure. The core diagnosis is identical, but the presentation adapts, suggesting the model is reasoning through the problem rather than reciting a template.

## 4. Completeness

**Output A (Baseline):** 4/5
The report is complete in that it covers the problem, root cause, immediate fix, and long-term prevention. It misses some of the investigative steps that led to the conclusion, jumping straight to the answer.

**Output B (Optimised):** 5/5
The optimised version feels more complete as a "debug record". It details the *process* of elimination (e.g., "The error is a timeout... This confirms the failure is due to latency, not an immediate crash"). This "show your work" aspect makes it a more complete artifact of engineering work.

## 5. Audience Awareness

**Output A (Baseline):** 5/5
The tone is perfect for a post-mortem or incident report: objective, concise, and focused on resolution. It is easy for a manager or engineer to read and understand the situation quickly.

**Output B (Optimised):** 4/5
The tone is more "in the weeds". Phrases like "I am applying the Skeptic Lens" are a bit meta and less natural for a standard engineering report, though they are helpful for a debugging log. It feels slightly more "prompt-influenced" than the natural professional tone of Baseline.

## 6. Domain Dimensions: Correctness (Diagnosis and Fix)

**Output A (Baseline):** 5/5
**Diagnosis:** 100% correct. Identifies the specific background job starving the database.
**Fix:** Correct immediate action (kill process) and valid long-term architectural fixes (read replica).

**Output B (Optimised):** 5/5
**Diagnosis:** 100% correct. Same findings.
**Fix:** Correct immediate action and long-term fixes.

## Summary

| Dimension | Output A (Baseline) | Output B (Optimised) | Delta |
|-----------|---------------------|----------------------|-------|
| Depth | 4 | 4 | 0 |
| Specificity | 5 | 5 | 0 |
| Natural Variation | N/A | 4 | N/A |
| Completeness | 4 | 5 | +1 |
| Audience Awareness | 5 | 4 | -1 |
| Correctness | 5 | 5 | 0 |

**Overall preference**: No meaningful difference

**Key differences**:
The **Optimised** version (Output B) explicitly structures the *reasoning process* (Triage -> Isolation -> Root Cause), showing how the conclusion was reached. The **Baseline** (Output A) presents the *conclusion* directly as a report.

**Magnitude**: Negligible
Both outputs are excellent. The Baseline is arguably better as a final artifact (Post-Mortem), while the Optimised version is better as a process log (Debug Session). The difference in utility is minimal; both solve the problem perfectly.

## Diagnostic Observations & Pipeline Note

**The "Pipeline" Tier (Runs 1-3):**
While the Baseline and Optimised tiers produced text reports, the **Pipeline** runs (provided for context) demonstrated a massive leap in capability.
- **Run 2** of the Pipeline tier not only diagnosed the issue but **wrote the code** to fix it:
    - Implemented a Circuit Breaker in `order-service` (Go).
    - Patched the `inventory-sync-lambda` to use a Read Replica and keyset pagination (Go).
    - Verified the fix with chaos testing.

Comparing the text-based prompts (Baseline/Optimised) to the Pipeline output highlights that the constraint on "Correctness" for the text prompts was "Correct description of a fix," whereas the Pipeline achieved "Correct implementation of a fix."

**Surprise in Optimised Run 1:**
The use of explicit "Lenses" (Skeptic, Boundary, Temporal) in Optimised Run 1 was interesting. It gave the output a very structured, almost detective-like feel. This is likely a result of the "Cognitive Prompting" techniques, but for a simple debug task, it felt slightly over-engineered compared to the straightforward Baseline.
