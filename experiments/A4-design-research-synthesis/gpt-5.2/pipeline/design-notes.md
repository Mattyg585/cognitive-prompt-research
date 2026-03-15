# A4 Tier 3 Pipeline — Design Notes (GPT-5.2)

## Goal
Produce research synthesis that goes beyond cataloguing into **reframing sensemaking**: emergent models, tensions, and narratives that help teams decide what’s true, what matters, and why.

## Why a pipeline (mode separation)
This design implements the architect’s main interventions by separating incompatible postures into clean contexts:

- **Evidence extraction (Stage 01)** is investigation + light structuring.
- **Reframing / frame generation (Stage 02)** is divergent sensemaking.
- **Model commitment (Stage 03)** is convergent synthesis.
- **Prioritisation (Stage 04)** is evaluation.
- **Stakeholder packaging (Stage 05)** is reframing-for-audience and is intentionally last.

This avoids:
- executive framing contaminating discovery (exec summary moved to the end)
- solution-shaped synthesis (prioritisation isolated from theme discovery)
- forced completion (numeric slots become optional/conditional)

## Key design choices

### 1) Compression checkpoints before divergent work
Stage 01 outputs a structured **Evidence Ledger** (atomic items + tags). This strips narrative tone and prevents premature thematic prose from becoming context residue.

### 2) Lenses over templates
Stage 02 uses lenses (tensions, constraints, workarounds, identity/risk, trust/credibility, time/coordination) to invite emergence without seeding specific findings.

### 3) Conditional specificity
Across stages:
- prevalence counts are used **only when** the input supports participant totals/IDs
- quotes are verbatim **only when** present; otherwise marked as paraphrase with no fake attribution

### 4) Natural variation as a health signal
No stage asks for “exactly N themes/recommendations.” Each stage is instructed to produce as many as the evidence warrants, and to explicitly call out “not established” when the data doesn’t support segmentation.

### 5) Output packaging is downstream
The final stage can produce a stakeholder-ready artifact similar to the original skill’s structure, but only after the model and opportunities exist. The executive summary is written last to prevent narrative lock-in.

## Execution notes
- Default execution is sequential.
- If the raw corpus is too large, run Stage 01 per chunk (per interview / per doc), then concatenate ledgers and proceed.
- If Stage 03 identifies evidence gaps, loop back to Stage 01 (human-in-the-loop) to add missing context rather than forcing specificity.
