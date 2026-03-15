---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A1
artifact: blind-evaluation
---

# Blind Evaluation — A1 (Baseline vs Optimised vs Pipeline)

Evaluator basis: `evaluation/evaluator-prompt.md` + `evaluation/rubric.md`  
Domain-specific dimension added: **Risk Identification Accuracy** (Legal)

## Blind setup

- **Set A**: three runs from one tier
- **Set B**: three runs from another tier
- **Set C**: three final-stage pipeline outputs (Stage 04)

Scoring was performed on set labels (A/B/C) before mapping labels to tier names.

## Set-level observations before unblinding

- **Set A**: Solid and usable, but highly pattern-repetitive across runs.
- **Set B**: Better focus and compound-risk articulation; moderate variation.
- **Set C**: Strongest strategic reasoning and explicit sequencing/trade logic; best preservation of cross-clause interactions.

## Scores (blind)

### Natural Variation (multi-run dimension)

| Dimension | Set A | Set B | Set C | Reasoning |
|---|---:|---:|---:|---|
| Natural Variation | 2 | 3 | 4 | A uses near-fixed finding patterns. B varies emphasis/count moderately. C varies framing and strategic depth by run focus. |

### Median-run scoring (Depth, Specificity, Completeness, Audience Awareness, Risk Identification Accuracy)

| Dimension | Set A | Set B | Set C |
|---|---:|---:|---:|
| Depth | 3 | 4 | 4 |
| Specificity | 3 | 4 | 4 |
| Completeness | 3 | 4 | 4 |
| Audience Awareness | 3 | 4 | 5 |
| Risk Identification Accuracy | 3 | 4 | 5 |

### Blind reasoning by dimension

- **Depth**: Set A finds core issues but remains checklist-like. Set B captures compound interactions. Set C best translates those interactions into negotiation logic.
- **Specificity**: Set A is specific enough for basic use. Set B/C are more clause-interaction aware and less generic.
- **Completeness**: Set A covers major areas but leaves some interaction-level detail shallow. Set B/C include stronger linkage across data rights, survival, and transfer dynamics.
- **Audience Awareness**: Set C most clearly writes for a buyer negotiating under time pressure.
- **Risk Identification Accuracy**: Set C most reliably identifies genuinely risky, interacting clauses (especially 1.6 + 5.6 + 12.6 and operational continuity links).

## Unblinding

- **Set A = Baseline** (`gpt-5.3-codex/baseline-runs`)
- **Set B = Optimised** (`gpt-5.3-codex/optimised-runs`)
- **Set C = Pipeline final stage** (`gpt-5.3-codex/pipeline-runs/run-N/04-strategic-advisor-output.md`)

## Comparison table with deltas (vs Baseline)

| Dimension | Baseline | Optimised | Pipeline | Δ Opt-BL | Δ Pipe-BL |
|---|---:|---:|---:|---:|---:|
| Depth | 3 | 4 | 4 | +1 | +1 |
| Specificity | 3 | 4 | 4 | +1 | +1 |
| Natural Variation | 2 | 3 | 4 | +1 | +2 |
| Completeness | 3 | 4 | 4 | +1 | +1 |
| Audience Awareness | 3 | 4 | 5 | +1 | +2 |
| Risk Identification Accuracy | 3 | 4 | 5 | +1 | +2 |

## Overall assessment

**Overall preference**: Pipeline > Optimised > Baseline  
**Trust for real work**: Pipeline tier, with Optimised as lower-overhead fallback.

**What the better versions do**:
- Optimised tier improves focus, removes some anchor behavior, and better surfaces interaction risks.
- Pipeline tier most clearly separates cognitive tasks and yields stronger strategic advice with higher legal risk-identification fidelity.

**Magnitude**: **Moderate-to-large**. The difference is meaningful in practice, especially for high-impact clauses and negotiation sequencing quality.

## Diagnostic notes beyond rubric

- Baseline remains competent but tends toward templated structure and repeated emphasis.
- Optimised materially improves issue framing without major complexity cost.
- Pipeline provides the clearest practical negotiation artifact when cross-clause interactions matter.
