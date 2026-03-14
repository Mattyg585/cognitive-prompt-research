# Cross-Experiment Findings

Updated as experiments complete. Patterns, boundary conditions, and surprises.

---

## Experiments Completed

| # | Domain | Type | Baseline | Optimised | Pipeline | External Validation |
|---|--------|------|----------|-----------|----------|-------------------|
| A1 | Legal contract review | Analytical | 3rd (both) | 2nd (both) | **1st (both)** | Claude Web + Gemini unanimous |
| A2 | Marketing content | Creative | 3rd (both) | **1st/2nd (split)** | **1st/2nd (split)** | Claude Web: Opt 1st. Gemini: Pipe 1st |

---

## Emerging Patterns

### 1. Baseline is consistently worst

Both experiments, both external evaluators, unanimous: the original monolithic prompt with template anchors and mode mixing produces the weakest output. This holds across analytical (legal) and creative (marketing) domains.

Specific markers of baseline weakness:
- **A1**: "Thorough junior associate memo" / "automated checklist" (Claude). "Standard reviewer" (Gemini).
- **A2**: "Most identifiably AI-generated" / "keyword string, not a hook" (Claude). "Too formulaic and brochure-like" (Gemini).

The template anchors (numeric targets, fixed structures, seeded categories) consistently suppress both analytical depth and creative voice.

### 2. The intervention level that matters depends on the domain

**Analytical work (A1)**: Pipeline wins unanimously. The qualitative leap from Tier 2 to Tier 3 is large — compound risk analysis, counterparty modelling, scripted negotiation moves. The monolithic architecture is clearly the ceiling.

**Creative work (A2)**: Evaluators split between Pipeline and Optimised. The gap between Tier 2 and Tier 3 is small enough that preference varies. Prompt-level fixes (removing anchors, replacing seeds with lenses) capture most of the improvement.

**Possible explanation**: Creative work benefits from a unified voice. The pipeline's separate stages may introduce a slightly "edited" quality — the editorial/SEO pass (convergent) damping the creative voice (divergent). Claude Web specifically noted the pipeline version "reads slightly more 'edited' than 'written'."

### 3. The type of improvement differs by domain

**A1 (analytical)**: Pipeline improves *reasoning* — connecting clauses into compound risks, modelling the counterparty's strategic position, scripting negotiation moves. These are cognitive capabilities that require space to develop.

**A2 (creative)**: Both Tier 2 and Tier 3 improve *voice* — the output sounds like a human, uses natural language, integrates product details into narrative rather than listing them. The improvement is about register, not reasoning.

### 4. "Good output hides great output" confirmed in both domains

Both experiments show the same pattern: nobody reading the baseline in isolation would say it's bad. It's thorough, complete, covers the bases. The gap only appears when you see what the other tiers produce.

- A1: "O08FZY gives you everything; the other two give you what you need."
- A2: Both evaluators called the baseline "competent" but "forgettable."

---

## Boundary Conditions Identified

### Creative work may not need Tier 3

For creative-within-constraints work (marketing), Tier 2 prompt-level fixes may be sufficient. The pipeline adds sophistication but may over-process the voice. This is a tentative finding from one experiment — needs confirmation from B1 (pure creative writing) and more creative domain experiments.

### Open question: Does the pipeline design matter?

The A2 pipeline included an editorial/SEO stage that may have introduced convergent contamination back into the final output. A pipeline designed differently — with the editorial pass as input context rather than a final polish — might perform better for creative work. The issue may not be "pipelines don't help creative work" but "this pipeline design doesn't help creative work."

---

## What to Test Next

- **A3-A6**: Do the remaining analytical experiments confirm A1's pattern?
- **B1**: Pure creative writing — does mode separation help or hurt when there are no constraints?
- **A2b**: Skills composition — does loading multiple marketing skills degrade the output?
- **Pipeline design variants for creative work**: Can a differently structured pipeline avoid the "over-edited" quality?

---

## Raw Data

All outputs, evaluations, and blind comparison files are in the experiment directories. Each experiment has:
- `baseline-runs/`, `optimised-runs/`, `pipeline-runs/` — raw outputs
- `evaluation/` — internal blind evaluation
- `blind-comparison/` — external evaluation files with randomised IDs
- `analysis/` — prompt architect analysis
- `optimised/revision-notes.md` — what changed and why
- `pipeline/handoff-spec.md` — pipeline architecture
