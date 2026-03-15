# A4 Tier 3 Pipeline — Handoff Spec

Purpose: enable **reframing sensemaking** (emergent models, tensions, narrative frames) before any prioritisation or stakeholder packaging.

This pipeline is sequential by default. If the raw research is too large, Stage 01 can be run in batches and the ledgers concatenated before continuing.

## Sequence (filenames are the canonical order)

1) `01-evidence-ledger.md` (or `01-evidence-ledger.agent.md`)
2) `02-frame-generator.md` (or `02-frame-generator.agent.md`)
3) `03-synthesis-modeler.md` (or `03-synthesis-modeler.agent.md`)
4) `04-opportunity-prioritiser.md` (or `04-opportunity-prioritiser.agent.md`)
5) `05-stakeholder-reframer.md` (or `05-stakeholder-reframer.agent.md`)

## Artifacts passed between stages (handoff contracts)

### Stage 01 → Stage 02: Evidence Ledger (compression checkpoint)
**Pass:**
- `Evidence Ledger` table of atomic evidence items (quotes/observations), each with:
  - stable `E#` id
  - source reference (participant/session/doc)
  - verbatim quote if available (otherwise explicitly marked paraphrase)
  - minimal context
  - lightweight open-codes/tags (not themes)
- `Known metadata` (participant count, methods, date range) only if supported by input
- `Unknowns / missing metadata` list

**Drop:**
- theme naming
- conclusions, recommendations, impact/effort
- executive summaries

### Stage 02 → Stage 03: Candidate Frames (divergent reframing)
**Pass:**
- `Frame Set` with multiple candidate frames, each including:
  - frame name (working title)
  - what it makes salient (lens)
  - core tensions / tradeoffs
  - predicted user strategies / workarounds
  - evidence pointers (E# references)
  - what decisions this frame would inform
- `Contradictions / outliers` list (with E#)

**Drop:**
- prioritisation
- solution proposals

### Stage 03 → Stage 04: Core Synthesis Model (convergent commitment)
**Pass:**
- `Chosen frame(s)` and rationale
- `Themes` (variable count) with:
  - definition
  - boundaries (what’s in/out)
  - evidence pointers (E#)
  - notes on ambiguity/contradiction
- `Segments / contexts` only if evidenced (otherwise “not established”)
- `Insights` stated as falsifiable/operational claims + evidence pointers
- `Open questions` (research gaps)

**Drop:**
- stakeholder packaging and “sell” language

### Stage 04 → Stage 05: Opportunity Map (evaluation isolated)
**Pass:**
- `Opportunities` mapped from insights (Insight → Opportunity), each with:
  - intended user outcome
  - rationale and evidence pointers (E#)
  - expected impact (qualitative unless measured)
  - effort/complexity (qualitative)
  - risks / dependencies
- `Non-actionable-but-important` insights list

**Drop:**
- executive narrative (written last)

### Stage 05 → Final: Reframed Deliverables (audience-facing)
**Pass (final output):**
- stakeholder-ready synthesis document (method → findings → implications → opportunities)
- executive summary produced **last**
- audience-specific reframes (Exec / Design / Eng)
- explicit boundaries on evidence and unknowns

## Quality gates (quick checks)
- No invented participant IDs, quotes, or prevalence counts.
- Natural variation: number of themes/opportunities adapts to input complexity.
- Reframing occurs **before** prioritisation: frames/insights include non-actionable tensions.
- Executive summary is last and reflects the synthesis, not vice versa.
