# Blind Evaluation: A4 Design Research Synthesis (GPT-5.3-Codex)

**Date:** 2026-03-15  
**Experiment:** A4  
**Task:** Synthesize `test-material/user-interviews.md` into themes, insights, and recommendations.

**Evaluator setup (blind):**
- Output A: one candidate synthesis
- Output B: one candidate synthesis
- Output C: one candidate synthesis

Rubric used: `evaluation/evaluator-prompt.md` + `evaluation/rubric.md`.

> A4-specific note from RUN-ALL: check whether outputs **catalogue themes** vs **reframe strategically**.

---

## Step 1 — Initial impressions (blind)

- **Output A** is comprehensive and clearly structured, with strong template compliance and practical readability.
- **Output B** is less template-driven and provides stronger causal linking between findings.
- **Output C** is the most strategic: findings are translated into system dynamics, business implications, and decision trade-offs.

---

## Step 2 — Dimension scoring (absolute rubric)

### Depth
- **A: 3/5** — Competent pattern coverage, mostly descriptive cataloguing.
- **B: 4/5** — Clear causal synthesis and stronger interpretation.
- **C: 5/5** — Reframes the problem (incentive design, threshold collapse, role-architecture mismatch).

### Specificity
- **A: 4/5** — Grounded in concrete participant evidence and quotes.
- **B: 4/5** — Equally grounded, with stronger explanation of mechanism.
- **C: 5/5** — Evidence-grounded plus explicit product/business consequence mapping.

### Completeness
- **A: 4/5** — Covers major themes and recommendations.
- **B: 5/5** — Better weighting and stronger throughline across sections.
- **C: 5/5** — Full coverage plus tensions/trade-offs and confidence-calibrated actions.

### Audience Awareness
- **A: 3/5** — Suitable report style, but limited strategic framing for decision-makers.
- **B: 4/5** — Better aligned to product-team decision context.
- **C: 5/5** — Explicitly writes for product + business audiences and anticipates internal trade-offs.

### Natural Variation
- Not scored (single run per tier in this execution).

---

## Step 3 — Summary table

| Dimension | Output A | Output B | Output C |
|---|---:|---:|---:|
| Depth | 3 | 4 | 5 |
| Specificity | 4 | 4 | 5 |
| Completeness | 4 | 5 | 5 |
| Audience Awareness | 3 | 4 | 5 |
| **Total (out of 20)** | **14** | **17** | **20** |

**Overall preference:** C > B > A  
**Magnitude:** Large (practically meaningful)

---

## Step 4 — Catalogue vs reframe diagnostic (A4 requirement)

- **Output A (catalogue-heavy):** primarily lists themes and actions in a familiar synthesis template.
- **Output B (mixed):** still thematic, but begins to connect patterns into a coherent causal model.
- **Output C (reframe-dominant):** reframes from “usability/theme list” to “system incentive architecture + threshold dynamics + strategic positioning.”

This is the exact behavior RUN-ALL predicts for A4: pipeline-style separation best supports reframing instead of catalogue output.

---

## Step 5 — Unblinding

- **Output A = baseline** (`baseline-runs/run-1.md`)
- **Output B = optimised** (`optimised-runs/run-1.md`)
- **Output C = pipeline final** (`pipeline-runs/run-1/stage-3-strategic-translator.md`)

## Final verdict

The optimised single prompt improves quality over baseline, but the pipeline output is the only one that consistently converts interview themes into a strategic problem model. For A4, the strongest gain is not extra content volume; it is the shift from cataloguing to strategic reframing.
