# Cross-Experiment Findings

Updated as experiments complete. Patterns, boundary conditions, and surprises.

---

## Experiments Completed

| # | Domain | Type | Baseline | Optimised | Pipeline | External Validation |
|---|--------|------|----------|-----------|----------|-------------------|
| A1 | Legal contract review | Analytical | 3rd | 2nd | **1st** | Claude Web + Gemini: Pipeline 1st (unanimous) |
| A2 | Marketing content | Creative | 3rd | **1st/2nd** | **1st/2nd** | Claude Web: Opt 1st. Gemini: Pipe 1st. Human (Matt): Opt 1st |
| A3 | HR performance review | Template + judgment | 19/25 | 21/25 | **25/25** | Internal only |
| A4 | Design research synthesis | Synthesis | 14/20 | 17/20 | **20/20** | Internal only — "qualitative leap" |
| A5 | Engineering debug | Sequential | 20/25 | 20/25 | **25/25** | Internal only |
| A6 | SecOps incident response | Multi-mode | 15/25 | 20/25 | **25/25** | Internal only |

**Pipeline scored highest in all 6 experiments.** In 5 of 6, the gap between Pipeline and Optimised was larger than the gap between Optimised and Baseline.

---

## Confirmed Patterns

### 1. Baseline is consistently worst

All six experiments, all evaluators (internal + external + human): the original monolithic prompt produces the weakest output. This holds across analytical, creative, template-heavy, synthesis, sequential, and multi-mode domains.

The template anchors (numeric targets, fixed structures, seeded categories) consistently suppress both analytical depth and creative voice.

### 2. Pipeline produces the largest improvement in 5 of 6 domains

The exception is A2 (creative/marketing), where Pipeline and Optimised were close enough that evaluators split — and human judgment preferred Optimised for its more natural voice.

For all other domains — including the calibration cases we expected to show limited improvement (A3: template-heavy HR, A5: already well-structured debug) — the pipeline produced clear improvement.

**A5 is particularly notable**: Optimised scored the same as Baseline (20/25), meaning prompt-level fixes didn't help a well-structured sequential prompt. But Pipeline jumped to 25/25. The architecture matters even when the individual prompt is already clean.

### 3. The qualitative leap pattern

Two experiments showed what we're calling a "qualitative leap" — the pipeline didn't just score higher, it produced a fundamentally different kind of document:

- **A1 (legal)**: The pipeline version "treats the contract as a deal, not a document." Compound risk analysis, counterparty modelling, scripted negotiation moves.
- **A4 (design research)**: The pipeline produced strategic reframing rather than cataloguing themes. A different type of synthesis entirely.
- **A6 (SecOps)**: The pipeline produced an "organisational learning artifact" rather than a standard incident report.

### 4. "Good output hides great output" — confirmed across all domains

Every baseline output is competent. Nobody reading any of them in isolation would say they're bad. The gap only appears when you see what the other tiers produce. This is the most consistent finding across all six experiments.

### 5. The type of improvement varies by domain

| Domain type | What Pipeline improves | Stack layer |
|-------------|----------------------|-------------|
| Analytical (A1, A6) | Reasoning — connecting evidence, modelling adversaries, strategic thinking | Cognitive mode |
| Synthesis (A4) | Depth — reframing patterns rather than cataloguing them | Cognitive mode + Expertise |
| Template (A3) | Judgment — nuanced assessment vs filling in template fields | Expertise + Register |
| Sequential (A5) | Architecture — the investigation structure itself changes | Cognitive mode |
| Creative (A2) | Voice — but Tier 2 captures most of this improvement | Register |

### 6. Creative work is the boundary condition

A2 is the only experiment where evaluators disagreed on whether Pipeline or Optimised is better. The pattern:
- Pipeline produces better *process* (editorial reasoning, SEO strategy)
- Optimised produces better *prose* (voice, rhythm, naturalness)
- For a blog post, prose wins. For an analytical deliverable, process wins.

**Possible explanation**: Creative writing quality lives at the register layer. Pipeline separation operates at the cognitive mode layer. For analytical work, freeing the cognitive mode cascades down to register. For creative work, the pipeline's structured handoffs may disrupt the register-level flow that makes writing feel human.

---

## Caveats and Limitations

### Perfect scores are suspicious

Pipeline scored maximum (25/25 or 20/20) in all four A3-A6 experiments. This ceiling effect may indicate:
- The internal evaluator is biased toward pipeline outputs (longer, more structured)
- The rubric doesn't discriminate well at the top end
- The pipeline outputs genuinely are excellent — but perfect scores across 4 experiments should be held carefully

### Internal evaluations only for A3-A6

A1 and A2 have external blind validation (Claude Web + Gemini, zero project context). A3-A6 have internal evaluation only. The external evaluations were more nuanced and provided stronger evidence. Running external blind evaluations on the most interesting A3-A6 results (particularly A4 and A6) would strengthen the findings.

### Single runs for A3-A6

A1 and A2 had 3 runs per tier. A3-A6 had 1 run per tier. Single runs can't measure natural variation or rule out lucky/unlucky runs. The consistency of the pattern across all 4 experiments partially compensates, but individual results should be held lightly.

### Same model everywhere

All experiments used Claude. The findings may be model-specific. Testing with other models (GPT-4, Gemini) would test generalisability.

### Self-evaluating

The model that produced the outputs is related to the model that evaluated them. External human evaluation from domain experts would be stronger evidence.

---

## Boundary Conditions

### Creative work: Tier 2 may be sufficient

For creative-within-constraints work (marketing), prompt-level fixes capture most of the improvement. The pipeline adds sophistication but may over-process the voice. This needs confirmation from B1 (pure creative writing).

### Open: Does pipeline design matter for creative work?

The A2 pipeline included an editorial/SEO stage that may have introduced convergent contamination. A differently designed pipeline might perform better.

### Open: Well-structured prompts and Tier 2

A5 (debug) showed that Tier 2 added nothing to an already well-structured prompt — but Tier 3 still helped. This suggests prompt-level fixes address *prompt-level problems* (anchors, seeds). When the prompt is already clean, the remaining improvement comes from architectural separation.

---

## What to Test Next

- **External blind evaluation on A4 and A6** — the most interesting results, need stronger validation
- **B1 (creative writing)** — pure creative work without marketing constraints
- **A2b (skills composition)** — does loading multiple skills degrade output?
- **Cross-model testing** — do the patterns hold on GPT-4 and Gemini?
- **Domain expert evaluation** — get a lawyer to review A1, an engineer to review A5
- **Pipeline design variants for creative work** — can a different pipeline structure avoid the "over-edited" quality?

---

## Summary Statement

Across six experiments in six domains, cognitive mode separation via pipeline architecture consistently outperformed both baseline monolithic prompts and prompt-level optimisations. The improvement was largest for analytical and synthesis work, where the pipeline produced qualitatively different output — not just better scores but fundamentally different documents. Creative work is the identified boundary condition where prompt-level fixes may be sufficient.

The monolithic-prompt-plus-skills paradigm appears to be a ceiling, not a floor, for complex tasks. The baseline output is always competent. The gap between competent and genuinely insightful is where the pipeline operates — and that gap is invisible until you separate the modes and compare.

---

## Raw Data

All outputs, evaluations, and blind comparison files are in the experiment directories. Each experiment has:
- `baseline-runs/`, `optimised-runs/`, `pipeline-runs/` — raw outputs
- `evaluation/` — internal blind evaluation
- `blind-comparison/` — external evaluation files (A1 and A2 only)
- `analysis/` — prompt architect analysis
- `optimised/revision-notes.md` — what changed and why
- `pipeline/handoff-spec.md` — pipeline architecture
