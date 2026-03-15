# Blind Evaluation: A5 Engineering Debug (GPT-5.3-Codex, 2026-03-15)

## Evaluation Setup

Prompt basis: `evaluation/evaluator-prompt.md` + `evaluation/rubric.md`  
Domain-specific dimension: **Correctness**

Compared sets (blind labels):

- **Set A**: one run
- **Set B**: one run
- **Set C**: one run

Natural Variation is not scored (single-run per tier by protocol).

---

## Dimension Scoring (blind)

### 1) Depth
- **Set A: 4** — Solid causal chain and practical fixes, but mostly linear reasoning.
- **Set B: 5** — Explicit hypothesis elimination and stronger trigger-vs-systemic distinction.
- **Set C: 5** — Deepest treatment; separates confidence levels and unresolved mechanism details.

### 2) Specificity
- **Set A: 4** — Uses concrete metrics/timeline and actionable controls.
- **Set B: 4** — Also concrete, with clearer narrowing logic than Set A.
- **Set C: 5** — Most explicit on boundary conditions, dependencies, and verification checkpoints.

### 3) Completeness
- **Set A: 4** — Covers reproduction, root cause, fix, prevention competently.
- **Set B: 4** — Adds diagnosis transparency and better systemic framing.
- **Set C: 5** — Most complete end-to-end package, including blast-radius-aware mitigation and verification structure.

### 4) Audience Awareness
- **Set A: 4** — Good on-call/engineering readability.
- **Set B: 4** — Better for review audiences due to explicit reasoning trail.
- **Set C: 4** — Strong for staff-level incident response; slightly denser than needed for quick triage.

### 5) Correctness (domain-specific)
- **Set A: 4** — Correct primary diagnosis and broadly sound intervention direction.
- **Set B: 5** — Correct diagnosis with stronger mechanistic reasoning and level-matched fixes.
- **Set C: 5** — Correct and most robustly reasoned, with strongest guardrail/verification alignment to failure mode.

---

## Summary Table

| Dimension | Set A | Set B | Set C |
|---|---:|---:|---:|
| Depth | 4 | 5 | 5 |
| Specificity | 4 | 4 | 5 |
| Completeness | 4 | 4 | 5 |
| Audience awareness | 4 | 4 | 4 |
| Correctness | 4 | 5 | 5 |
| **Total** | **20** | **22** | **24** |

**Overall preference (blind): Set C > Set B > Set A**  
**Magnitude:** Moderate (B over A), Moderate-to-large (C over A), Moderate (C over B).

Key differences:
- Set B and C show better diagnosis transparency than A.
- Set C best preserves systems-level thinking through to implementation and verification.
- Set A is competent but more template-linear and less explicit about uncertainty boundaries.

---

## Unblinding

- **Set A = Baseline** (`baseline-runs/run-1.md`)
- **Set B = Optimised** (`optimised-runs/run-1.md`)
- **Set C = Pipeline final stage** (`pipeline-runs/run-1/stage-2-fix-designer.md`, informed by stage-1 investigator output)

## Verdict

For A5 on **Correctness**, ranking is:

1. **Pipeline**
2. **Optimised**
3. **Baseline**

Difference is meaningful in practice due to stronger causal rigor, fix-level matching, and verification specificity.

