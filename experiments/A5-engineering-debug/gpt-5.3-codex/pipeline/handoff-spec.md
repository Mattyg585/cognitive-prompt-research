# Handoff Specification: A5 Engineering Debug Pipeline

## Stage Sequence

1. `stage-1-investigator.md`
2. `stage-2-fix-designer.md`

Sequential only. Stage 2 depends on Stage 1 output.

## Boundary Contract

### What crosses from Stage 1 -> Stage 2

- Reproduction summary
- Isolation findings (components, timeline, changes, resource metrics)
- Hypotheses with evidence for/against
- Root cause analysis (including confidence and blast radius)
- Explicit information gaps/assumptions

### What is dropped

- Exploratory narrative and abandoned thought process details
- Open-ended investigative framing language
- Any undeveloped speculation not tied to evidence

## Input Constraints

- Stage 1 reads the original test material only.
- Stage 2 reads Stage 1 output only.
- Stage 2 must not read the original bug report or other context sources.

## Expected Artifact Paths (run-1)

- `pipeline-runs/run-1/stage-1-investigator.md`
- `pipeline-runs/run-1/stage-2-fix-designer.md`

