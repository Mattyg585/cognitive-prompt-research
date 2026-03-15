---
model: GPT-5.3-Codex (gpt-5.3-codex)
date: 2026-03-15
experiment: A6
tier: pipeline
artifact: design-notes
---

# A6 Pipeline Design Notes

## Why this is a five-stage pipeline

The A6 postmortem task mixes at least five thinking modes in one template: timeline reconstruction, causal inquiry, response evaluation, intervention design, and synthesis. Combining these in one context tends to produce compliance-style output (complete sections, shallow insight).

Five stages are the minimum split that avoids known interferences:

- Timeline is factual/structural.
- Causal analysis is exploratory/deep.
- Response evaluation is convergent/judgmental.
- Action-item generation is creative but constrained.
- Final synthesis is reframing/composition.

## Why sequential execution

Each stage depends on transformed artifacts from the previous stage(s), not raw source context. Sequential flow enforces cognitive isolation and makes contamination auditable.

## Expected quality shift

- Baseline: standard incident report.
- Optimised: better single-pass causal reasoning.
- Pipeline: strongest chance of organizational-learning outcomes, especially around:
  - structural detection blind spots,
  - confidence-without-coverage patterns,
  - relationship between control design and human decision environment.

## Trade-offs

- Higher orchestration overhead
- More files to manage
- Better traceability and mode integrity

## Anti-patterns this design avoids

1. **5-Whys lock-in**: no fixed numeric causal chain.
2. **Evaluation leakage into investigation**: evaluation delayed until after causal map.
3. **Actionability bias in root-cause discovery**: interventions generated only after causes are stabilized.
4. **Premature narrative closure**: synthesis is final stage only.
