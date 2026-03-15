# Pipeline Handoff Specification

## Pipeline overview

Transform a product brief into published-quality marketing content through four cognitively separated stages: explore the brief, design the content strategy, write the piece, then polish for SEO and channel compliance.

## Agent sequence

```
Brief Explorer → Content Architect → Writer → Editor
  (diverge)       (converge)         (diverge)  (converge)
```

All stages are sequential — each depends on the previous stage's output.

## Stage 1: Brief Explorer

**Agent prompt**: `brief-explorer.md`
**Cognitive mode**: Investigation (divergent)
**Receives**: The product brief (`test-material/product-launch-brief.md`)
**Produces**: A structured strategic brief with sections for product insight, audience understanding, surprising elements, emotional territory, potential angles, voice notes, and raw material
**Why separate**: Investigation needs open exploration without the pressure to commit to a structure or start writing. If the explorer is also deciding on structure, it only explores angles it can already structure.

## Stage 2: Content Architect

**Agent prompt**: `content-architect.md`
**Cognitive mode**: Synthesis (convergent)
**Receives**: The strategic brief from Stage 1 + the original product brief
**Produces**: A content plan with angle, structure, voice direction, key beats, headline direction, and CTA direction
**Why separate**: Committing to a narrative structure is convergent — it narrows. This should happen after exploration is complete, not during it. And it should happen before writing, so the writer receives clear direction rather than having to explore AND write simultaneously.

## Stage 3: Writer

**Agent prompt**: `writer.md`
**Cognitive mode**: Generation (divergent)
**Receives**: The content plan from Stage 2 + the original product brief (for source data/quotes/stats)
**Produces**: The complete content piece — headline, body, meta description
**Why separate**: This is the critical separation. The writer's context contains NO evaluation criteria — no SEO checklist, no character limits, no readability rules, no formatting guidelines. This is where the original prompt's primary interference lived: generation + evaluation in the same context. The writer focuses entirely on voice, flow, and the reader's experience.

## Stage 4: Editor

**Agent prompt**: `editor.md`
**Cognitive mode**: Evaluation (convergent)
**Receives**: The draft from Stage 3 + the SEO requirements from the original product brief (primary keyword, secondary keywords, CTA)
**Produces**: The final polished piece + editorial notes documenting changes
**Why separate**: Evaluation criteria belong here — after the creative work is done. The editor can refine for SEO and channel compliance without suppressing the generative voice. The editor explicitly preserves voice while integrating requirements.

## Handoff details

### Handoff 1: Explorer → Architect

**What crosses**: The structured strategic brief (product insight, audience understanding, surprising elements, emotional territory, potential angles, voice notes, raw material)
**Format**: Structured sections with compressed observations — not exploratory prose
**What gets dropped**: The explorer's reasoning process, tentative threads that didn't lead anywhere, "this is interesting because..." explanations
**Compression**: Built into the explorer's output format — it produces structured observations, not narrative exploration

### Handoff 2: Architect → Writer

**What crosses**: The content plan (angle, structure, voice direction, key beats, headline direction, CTA direction) + the original product brief
**Format**: Structured plan with clear decisions
**What gets dropped**: The architect's deliberation about which angle to choose, the strategic brief from Stage 1 (the architect has already distilled what matters into the plan)
**Why the original brief also crosses**: The writer needs access to specific data points, quotes, and facts that the architect may not have included in the plan. The brief is source material, not a cognitive contaminant — it doesn't carry evaluation criteria or structural templates.

### Handoff 3: Writer → Editor

**What crosses**: The complete draft + the SEO/channel requirements extracted from the original product brief (primary keyword, secondary keywords, CTA, target content type)
**Format**: The draft as written content; the requirements as a short structured list
**What gets dropped**: The content plan from Stage 2 (the writer has already executed on it — the editor doesn't need to know the strategy, only to polish the result), the strategic brief from Stage 1
**Why requirements are passed separately**: The editor needs to know what keywords to integrate and what channel conventions to check. These come from the original brief, not from any upstream agent's output. This prevents evaluation criteria from contaminating any generative stage.

## Execution method

**Sequential** — each stage requires the previous stage's complete output before starting.

For running multiple experiment runs: the 3 runs can be parallelized (each is an independent pipeline execution), but within each run, the 4 stages must be sequential.

## Execution instructions

For each run (N = 1, 2, 3):

1. **Stage 1**: Spawn a subagent with `brief-explorer.md` as the prompt. Input: the product brief. Save output to `pipeline-runs/run-N/brief-explorer.md`.

2. **Stage 2**: Spawn a NEW subagent with `content-architect.md` as the prompt. Input: the strategic brief from Stage 1 + the original product brief. Save output to `pipeline-runs/run-N/content-architect.md`.

3. **Stage 3**: Spawn a NEW subagent with `writer.md` as the prompt. Input: the content plan from Stage 2 + the original product brief. Save output to `pipeline-runs/run-N/writer.md`.

4. **Stage 4**: Spawn a NEW subagent with `editor.md` as the prompt. Input: the draft from Stage 3 + SEO requirements (primary keyword: "async collaboration platform", secondary keywords: "distributed teams", "timezone collaboration", "async-first", CTA: "Start free trial"). Save output to `pipeline-runs/run-N/editor.md`.

**Each stage MUST be a separate subagent** — running stages in the same context creates the exact monolithic contamination the pipeline is designed to avoid.

## Context window notes

No volume concerns — each agent receives a manageable amount of input (one brief + one structured handoff). No compression checkpoints needed beyond what's built into each agent's output format. No external storage warranted for this scale.
