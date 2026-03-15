# A2 Tier 3 Pipeline — Design Notes (GPT-5.2)

## Pipeline overview
This pipeline produces **high-quality creative marketing assets** by separating: (1) brief structuring, (2) divergent angle generation, (3) convergent selection + message spine compression, (4) templated channel drafting, and (5) final optimization.

It is designed to reduce a known failure mode in A2: **templates + SEO + best-practice evaluation acting as a pre-filter on creative generation**, producing competent but generic copy.

## Why a pipeline (not a single prompt)
The original skill mixes **Generation + Structuring + Evaluation** with heavy templates and numeric anchors. That combination tends to:
- suppress divergent exploration (angles, voice, emotional framing)
- create “slot-filling” behavior
- cause midpoint gravity (fixed counts) and cross-channel leakage

This pipeline preserves creative exploration by giving it a **clean context** before any templating/checklists appear.

## Agent map (cognitive roles)

### 01 — `01-brief-normalizer`
- **Type(s):** Structuring / light reframing
- **Job:** turn a messy brief into a compact, structured `CREATIVE_BRIEF`.
- **Why separate:** prevents early copywriting from running ahead of constraints; keeps later stages from inheriting ambiguity.

### 02 — `02-angle-ideator`
- **Type(s):** Divergent generation
- **Job:** generate distinct campaign angles/hooks with voice options.
- **Why separate:** avoids evaluation + template/SEO constraints suppressing novelty.

### 03 — `03-concept-decider`
- **Type(s):** Evaluation + synthesis (convergent)
- **Job:** choose the best angle and compress it into a `MESSAGE_SPINE` that carries coherence.
- **Why separate:** evaluation is useful *after* ideation, but contaminating if present during it.

### 04 — `04-asset-drafter`
- **Type(s):** Constrained generation + structuring
- **Job:** draft channel-ready assets using templates as scaffolding.
- **Why separate:** lets templates/checklists do what they’re good at (production) without shaping ideation.

### 05 — `05-copy-optimizer`
- **Type(s):** Evaluation + light regeneration
- **Job:** polish, tighten, enforce channel fit, and remove genericness while preserving the chosen voice.
- **Why separate:** editing/QA language can flatten voice if mixed too early; it belongs after drafts exist.

## Execution order rationale
- **Compress ambiguity first (01)** so later stages reason from the same constraints.
- **Diverge next (02)** while the context is still “open.”
- **Converge and compress (03)** into a message spine (the coherence carrier).
- **Produce assets (04)** from the spine, not from ideation prose (prevents ideation tone from leaking).
- **Optimize last (05)** so evaluation improves drafts instead of suppressing creative moves.

## Coherence-preserving separation
Creative work needs continuity. The `MESSAGE_SPINE` is the continuity object:
- compact enough to fit in context
- specific enough to preserve voice, promise, proof points, and CTA
- structured to prevent channel leakage and generic rewriting

## What to watch for during testing
- If outputs feel safe/generic: ensure 02 does not see template/SEO rules.
- If assets diverge in voice across channels: expand `voice_and_style` and `vocabulary_to_use/avoid` in 03.
- If SEO feels awkward: in 05, prioritize natural phrasing over keyword placement rules.
