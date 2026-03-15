---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A3
artifact: handoff-spec
tier: pipeline
---

# A3 Pipeline Handoff Spec (Manager Review Mode)

## Stage sequence

1. `stage-1-investigator.md`
2. `stage-2-review-writer.md`

## Strict stage boundaries

### Stage 1 input (allowed)
- Employee details
- “What went well”
- “What needs work”
- Goals from prior cycle

### Stage 1 input (forbidden)
- Promotion consideration
- Compensation guidance
- Any review template/rating rubric

### Stage 1 output contract
- Structured findings only:
  - key patterns
  - tensions/contradictions
  - goal evidence
  - notable absences
- No rating, no compensation recommendation, no template-filling prose

### Stage 2 input (allowed)
- Stage 1 structured findings
- Employee details
- Goals from prior cycle

### Stage 2 input (forbidden)
- Raw “what went well / needs work” bullets
- Promotion/compensation section from test scenario
- Stage 1 hidden reasoning trail

## Why this split

The toxic interference is investigation under evaluative pressure. Stage 1 isolates investigation. Stage 2 performs convergent synthesis/evaluation from clean findings.

