---
model: GPT-5.3-Codex (gpt-5.3-codex)
date: 2026-03-15
experiment: A6
tier: pipeline
artifact: handoff-spec
---

# A6 Pipeline Handoff Specification

## Pipeline objective

Generate a blameless postmortem that functions as an organizational-learning artifact by separating incompatible cognitive modes.

## Stage sequence (strict)

1. `stage-1-timeline-reconstructor`
2. `stage-2-causal-analyst`
3. `stage-3-response-evaluator`
4. `stage-4-action-item-generator`
5. `stage-5-postmortem-synthesiser`

## Boundary rules

- Each stage runs in a fresh session context.
- Each stage may read only declared inputs for that stage.
- Handoffs pass structured findings only; exploratory process notes are dropped.
- Downstream stages must not re-open upstream investigative work unless explicitly asked.

## Handoff contracts

### H1: Stage 1 → Stage 2

**Crosses**
- Structured event timeline
- Information-state annotations (“what was known”)
- Evidence gaps

**Drops**
- Stage 1 hypotheses, causal speculation, evaluative commentary

### H2: Stage 2 → Stage 3

**Crosses**
- Causal map (root causes + contributing factors)
- Evidence references to timeline
- Human-factors context and unresolved uncertainties

**Drops**
- Stage 2 exploratory dead ends and drafting alternatives

### H3: Stage 3 → Stage 4

**Crosses**
- Response strengths and failures
- Detection/containment/communication assessment with evidence refs

**Drops**
- Stage 3 evaluative deliberation process

### H4: Stage 2 + Stage 3 → Stage 4

**Crosses**
- Root-cause findings (from Stage 2)
- Response-gap findings (from Stage 3)

**Drops**
- Any prescriptive text from prior stages

### H5: Stages 1–4 → Stage 5

**Crosses**
- Final structured outputs from stages 1 through 4

**Drops**
- None (final synthesis stage is integration point)

## Validation checks

1. Stage 2 does not cite original incident file directly.
2. Stage 3 does not invent causal findings absent Stage 2 payload.
3. Stage 4 action items map to explicit Stage 2/3 findings.
4. Stage 5 final narrative cites uncertainty and distinguishes incident report facts vs organizational learning insights.
