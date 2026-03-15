# Pipeline Handoff Spec — A2 (GPT-5.3-Codex)

## Sequence

`01-brief-explorer -> 02-narrative-architect -> 03-draft-writer -> 04-voice-seo-editor`

Execution model: sequential within each run. Runs may execute in parallel.

## Boundary discipline

- Each stage runs in a clean context.
- Each stage receives only declared inputs.
- No stage may read future-stage files.
- Stage 03 must not receive Stage 04 evaluation criteria language except minimal keyword/CTA constraints passed at Stage 04.

## Handoff details

### H1: 01 -> 02
**Crosses:** product insight, audience model, proof, angle options, voice signals, raw material.

**Format:** structured headings only.

**Dropped:** exploratory reasoning traces and dead-end threads.

### H2: 02 -> 03
**Crosses:** chosen angle, reader journey, structure plan, voice brief, must-land proof, headline/CTA intent.

**Format:** compact execution blueprint.

**Dropped:** optional alternatives and strategic deliberation.

### H3: 03 -> 04
**Crosses:** complete draft content + minimal SEO requirement list (primary, secondary, CTA).

**Format:** prose draft + short requirement block.

**Dropped:** writer's internal drafting rationale.

## File mapping

Pipeline prompts:
- `pipeline/01-brief-explorer.md`
- `pipeline/02-narrative-architect.md`
- `pipeline/03-draft-writer.md`
- `pipeline/04-voice-seo-editor.md`

Run outputs:
- `pipeline-runs/run-N/01-brief-explorer.md`
- `pipeline-runs/run-N/02-narrative-architect.md`
- `pipeline-runs/run-N/03-draft-writer.md`
- `pipeline-runs/run-N/04-voice-seo-editor.md`

## Metadata requirement for stage outputs

All stage output files must begin with:

---
model: GPT-5.3-Codex (gpt-5.3-codex)
date: 2026-03-15
experiment: A2
tier: pipeline
run: N
stage: [stage filename without extension]
---