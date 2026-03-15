---
model: GPT-5.2
date: 2026-03-15
experiment: A3
artifact: design-notes
tier: pipeline
---

# A3 Tier 3 Pipeline Design Notes — `/performance-review`

## What this pipeline is optimizing for

The original skill is a *template generator*, but the architect analysis shows predictable failure modes even in template-like tasks:

- **Premature convergence**: the presence of rating/comp fields pulls the session into an HR-decision posture before evidence is gathered.
- **Anchoring**: fixed slot counts ("3 goals", "top 3–5 accomplishments", "2–3 sentences") produce uniform, mid-point outputs regardless of input richness.
- **Calibration gravity**: company target percentages act as strong numeric anchors.
- **Connector hallucination risk**: conditional “pull data from HRIS/project tracker” language can cause implied retrieval.

Tier 3 addresses these by separating modes into clean contexts and making the **handoff format** the boundary.

## Agent map (mode-separated)

1. **Review Router** (orchestration)
   - Routes to a mode path and states what the pipeline will produce.
   - Keeps itself content-light to avoid orchestrator bloat.

2. **Context Intake** (investigation + structuring)
   - Elicits (or assembles) facts and raw notes.
   - Explicitly separates *facts* (role, period, goals) from *judgments* (rating).

3. **Evidence Dossier** (investigation → compression)
   - Converts raw notes into behavior-based evidence items.
   - Surfaces gaps and contradictions without resolving them into a rating.

4. **Template Drafter** (structuring + constrained generation)
   - Produces a clean Markdown artifact for the requested mode.
   - Removes numeric anchors by making sections repeatable and optional.
   - Leaves evaluative fields blank pending Stage 5.

5. **Evaluation & Calibration** (evaluation + synthesis)
   - Applies rubrics and constraints *explicitly*.
   - Treats calibration targets as constraints to confirm, not defaults to aim for.

6. **Final Editor** (assembly / reframing)
   - Merges draft + decisions and polishes tone.
   - Must not introduce new judgments.

## Why this is more stages than the prior A3 (manager-only) pipeline

A two-stage split (investigate → write) is the minimum fix for manager reviews. This Tier 3 pipeline is deliberately broader because it must cover all modes and explicitly isolate:

- **Evidence shaping** (Stage 3) from **template drafting** (Stage 4)
- **Template drafting** (Stage 4) from **ratings/calibration** (Stage 5)

Even if outputs remain “template-like,” these separations reduce anchoring and prevent evaluation language from infecting evidence gathering.

## Key design choices (linked to findings)

### 1) Evaluation is always downstream of evidence
Ratings/comp/distribution live in Stage 5 only. Earlier stages are forbidden from making those calls.

### 2) Replace fixed-count slots with elastic containers
Stage 4 uses:
- “Add accomplishments as needed”
- “Add goals as needed”
- Optional sections that can be omitted when not relevant

This directly targets the “numbers become targets” effect.

### 3) Connector boundary is explicit
Every data point can be optionally tagged with a source:
- user-provided
- tool-provided (only when actual tool output is present)

This prevents implied retrieval.

### 4) Calibration targets are treated as constraints, not defaults
Stage 4 may show targets only as “if applicable” references. Stage 5 is responsible for reasoning about them.

## What to watch for when testing

- **Natural variation**: Does output length and number of items vary with input richness?
- **Evidence quality**: Are claims grounded in observable behaviors and impacts?
- **No premature rating**: Does any pre-Stage-5 content imply a rating or comp action?
- **No connector hallucination**: Any “pulled from HRIS” claims must be backed by explicit tool outputs.
