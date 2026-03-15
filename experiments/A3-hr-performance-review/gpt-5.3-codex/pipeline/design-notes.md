---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A3
artifact: design-notes
tier: pipeline
---

# A3 Pipeline Design Notes

## Why only two stages

The manager-review interference is localized: **investigation** is contaminated when **evaluation/template commitments** are already in context.  
A two-stage split removes that interference with minimal orchestration overhead.

## Stage responsibilities

- **Stage 1 — Performance Investigator**
  - Divergent analysis of evidence
  - Surfaces patterns and contradictions
  - No evaluative decisions

- **Stage 2 — Review Writer**
  - Convergent synthesis into manager-review structure
  - Assigns rating from evidence
  - Produces development plan and compensation recommendation

## Fairness intent

This pipeline is designed to improve HR fairness behavior by:

1. Forcing evidence-first synthesis.
2. Separating observed behavior from personality labeling.
3. Reducing anchoring from pre-specified compensation/promotion signals.
4. Encouraging explicit treatment of contradictions rather than selective narrative smoothing.

