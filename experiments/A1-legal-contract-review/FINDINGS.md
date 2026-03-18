# A1 — Legal Contract Review: Experiment Findings

**Date**: 2026-03-17
**Contract**: Common Paper Cloud Service Agreement v2.1
**Perspective**: Customer/buyer, $150K/year SaaS, 2-week deadline
**Models tested**: Claude Opus 4.6, Gemini 3 Pro Preview, GPT-5.2, GPT-5.2-Codex, GPT-5.3-Codex

---

## The Core Finding

**On Claude (primary model): the monolithic prompt is the ceiling, not the floor.**

- Tier 1 → Tier 2 (prompt optimisation): +0.4 average across dimensions. Real but marginal.
- Tier 2 → Tier 3 (pipeline reconstruction): +1.2 average across dimensions. Qualitative leap.

The pipeline doesn't just produce better scores. It produces a *different kind of output*. The investigation discovers things the monolithic versions structurally cannot see. The strategy reasons about the deal rather than restating findings. Each stage does one cognitive job cleanly.

**This pattern is model-dependent.** It replicates strongly on GPT-5.3-Codex, partially on GPT-5.2, and fails on Gemini 3 Pro Preview and GPT-5.2-Codex. More on this below.

---

## What the Pipeline Finds That the Monolith Doesn't

The most important evidence isn't the scores — it's the *consistent gaps* in what monolithic versions miss across all runs:

| Finding | Tier 1 | Tier 2 | Tier 3 |
|---------|--------|--------|--------|
| Security testing prohibition is absolute (no pen-test carveout) | Miss | Miss | Find |
| Payment continues during suspension with no credit | Miss | Miss | Find |
| "Aggregated" is undefined, threshold unspecified | Miss | Miss | Find |
| De-identification standard is doubly qualified (effort + industry) | Miss | Miss | Find |
| Cover Page deferral is a *systematic* risk-shifting pattern | Partial | Partial | Find |
| Suspension = functional termination without procedural safeguards | Miss | Miss | Find |
| Data rights chain (1.4→1.5→1.6→5.5→5.6→11.1) as compound system | Partial | Partial | Find |
| Accountability vacuum (no standards + no audit + no notification) | Miss | Miss | Find |

These aren't edge cases. The security testing prohibition, payment during suspension, and undefined aggregation threshold are findings a careful human reviewer would catch. The monolithic versions miss them *consistently* — across five runs each — because evaluation criteria pre-filter what the investigator notices. When investigation and evaluation share a context, the model only finds things it can already classify.

This is the mode interference claim in action: the evaluation framework acts as a lens on the investigation, and the investigation only sees what the evaluation can categorise. The pipeline's contract reader — with no evaluation criteria in its context — surfaces findings the monolithic versions cannot.

---

## The Variance Story

When we revised the Tier 2 and Tier 3 prompts with updated cognitive theory (sharper stance scaffolding, cleaner mode boundaries), the results were revealing:

### Tier 2: Better prompts reduce variance, not raise the ceiling

| Metric | Old Runs (1-3) | New Runs (4-5) |
|--------|---------------|----------------|
| Score range | 3.4–4.0 | 3.4–4.1 |
| Working Theory present | 2 of 3 | 1 of 2 |
| Core findings | Same across all | Same across all |
| Missed findings | Same across all | Same across all |

The best new run (Run 5, 4.1) is marginally better than the best old run (Run 1, 4.0). But the structural ceiling is identical. All five runs find the same things and miss the same things. The template determines what's discoverable. Better prompts produce more consistent execution within that ceiling — the Working Theory is sharper when it appears, the BATNA reasoning is more developed, the counterparty modelling is more specific — but the *investigative range* doesn't expand.

This is exactly what the theory predicts. Tier 2 improvements are *within-mode* optimisations. You can make the investigation-evaluation fusion work better, but you can't make it see what it structurally can't see.

### Tier 3: Pipeline quality is more consistent than monolithic quality

| Metric | Old Runs (1-3) | New Runs (4-5) |
|--------|---------------|----------------|
| Usable starting point | All 3 | Both |
| Cross-stage building | Strong | Strong |
| Run-to-run variance | Higher (Run 2 weaker) | Lower (both strong) |
| Unique strengths | Run 1 polish, Run 3 comprehensiveness | Run 5 SLA redline, thematic structure |

The old pipeline runs had more variance — Run 1 was polished, Run 3 was comprehensive but too long, Run 2 had a priority numbering error and weaker comparator stage with checklist language creeping in. The revised pipeline runs are more even. Both are above the "genuinely useful" threshold. The stage separation is cleaner, and the handoffs carry more analytical weight.

The revised prompts didn't raise the peak (Run 1 old was already excellent). They raised the floor. That's what better stance scaffolding does — it reduces the chance that a stage slips into the wrong cognitive mode.

---

## Cross-Model Results

The pipeline hypothesis doesn't replicate uniformly across models. This is itself a finding.

| Model | Tier 1 Avg | Tier 2 Avg | Tier 3 Avg | Pattern |
|-------|-----------|-----------|-----------|---------|
| **Claude Opus 4.6** | 2.9 | 3.3 | 4.5 | Pipeline >> Optimised > Baseline |
| **GPT-5.3-Codex** | 3.0 | 4.0 | 4.3 | Pipeline > Optimised > Baseline |
| **GPT-5.2** | 3.3 | 3.7 | 3.7 | Optimised ≈ Pipeline > Baseline |
| **GPT-5.2-Codex** | 3.7 | 3.7 | 3.0 | Baseline ≈ Optimised > Pipeline |
| **Gemini 3 Pro** | 4.0 | — | 2.5 | Baseline >> Pipeline |

### What this tells us

**The pipeline works best on models that are most susceptible to mode interference.** Claude shows the largest Tier 2→3 gap (+1.2), which suggests it is the most affected by having investigation and evaluation in the same context. GPT-5.3-Codex shows a similar pattern. These models appear to be more sensitive to the distributional signals in their context — which means they benefit more from having those signals cleaned up.

**Models with stronger instruction-following may resist the pipeline.** Gemini 3 Pro's baseline was already strong (4.0) and the pipeline *degraded* performance — the pipeline's contract reader missed the DPA gap in all three runs, a critical compliance oversight the baseline caught. GPT-5.2-Codex showed a similar pattern where the baseline performed well and the pipeline underperformed. Hypothesis: these models may have stronger internal templates for contract review that the pipeline disrupts without providing compensating structural benefit.

**The pipeline is not universally superior.** It's a tool that addresses a specific failure mode (mode interference). Models that already handle mode mixing well — or that have strong enough task-specific training to override distributional interference — may not benefit, and may be harmed by the fragmentation.

This is an important qualification. The claim is not "pipelines always win." The claim is "mode interference is real, it degrades output in predictable ways, and pipelines fix it — but only when the interference is the binding constraint."

---

## The Qualitative Picture

Four independent qualitative assessments (adopting the perspective of a senior legal consultant) converge on the same story:

**Tier 2 (both versions)**: A senior lawyer would find any of these a solid working document. The analysis understands *why* clauses matter (not just that they deviate), models the counterparty, provides specific executable redlines with fallbacks. The best runs (1 and 5) reach genuine commercial sophistication — the BATNA reasoning, the concession strategy, the internal decision requirements. A lawyer receiving this output would need to calibrate and verify, but not redo the analysis.

The ceiling is visible. The output does not find what it is not looking for. Because investigation and evaluation share the same context, the analysis tends to confirm expected findings rather than surprise with unexpected ones.

**Tier 3 (both versions)**: Each stage does one cognitive job, and the result is visibly different. The contract reader reads the contract as a *system* — identifying architectural risks, compound clause interactions, and structural absences that the monolithic versions consistently miss. The playbook comparator classifies without drafting. The redline writer drafts without strategising. The strategic advisor strategises without re-reading the contract.

The stages build genuinely across handoffs. Information first surfaced in Stage 1 appears as classified deviations in Stage 2, generates specific redline language in Stage 3, and becomes sequenced negotiation advice in Stage 4 — with the reasoning carried through at each stage rather than re-derived. The strategic advisor produces output that is qualitatively different from any tier's strategy section: it treats the counterparty as a specific entity with inferred motivations, identifies internal decisions the reader must resolve before negotiating, and provides a negotiation arc with internal logic rather than a prioritised list.

A senior lawyer receiving any pipeline run would have a usable starting point — not a finished work product, but a document that captures the right issues, frames the commercial risks correctly, proposes substantially reasonable redline language, and provides negotiation guidance grounded in the actual deal dynamics.

---

## Theoretical Implications

### What we expected vs what we found

| Prediction | Result | Notes |
|-----------|--------|-------|
| Tier 2 improves incrementally over Tier 1 | Confirmed (+0.4 avg) | Better framing, compound risk awareness, variable depth |
| Tier 3 produces qualitative leap over Tier 2 | Confirmed on Claude (+1.2 avg) | Investigation discovers things monolith structurally cannot see |
| Investigation + evaluation is the toxic pair | Confirmed | The mode interference is visible in the consistent gaps |
| Revised prompts raise the ceiling | **Not confirmed** | They raise the floor instead — reduce variance, same ceiling |
| Pipeline benefits are model-universal | **Not confirmed** | Model-dependent; some models resist or degrade |

### The key insight: the ceiling vs floor distinction

The most surprising finding is the variance story. We expected revised prompts (with better stance scaffolding) to expand what the output could discover. Instead, they produced more consistent execution of the same discoveries. The investigative range didn't change — the reliability of hitting that range improved.

This suggests that mode interference isn't a *magnitude* problem (how good is the analysis?) but a *category* problem (what kinds of analysis are possible?). You can make a monolithic prompt produce excellent analysis within its category. You cannot make it produce analysis in a category that requires clean mode separation. The ceiling isn't about quality — it's about kind.

### The model-dependence question

The cross-model results raise a question we didn't anticipate: **is mode interference a property of the model or the task?**

If it were purely a task property, all models should show the same pattern. They don't. If it were purely a model property, there would be no task-level prediction possible. But there is — the specific investigation gaps (security testing, payment during suspension, undefined aggregation) appear consistently within the Claude monolithic runs, suggesting the interference pattern is reproducible for a given model-task pair.

Working hypothesis: mode interference is real in all models (they all learned the language patterns of different cognitive modes) but the *binding constraint* varies. Some models' instruction-following or task-specific training is strong enough to partially compensate. The pipeline helps most when mode interference is the binding constraint on output quality.

---

## What This Means for the Research

### The framework works

The cognitive stack theory predicted:
1. That mixing investigation and evaluation would produce a specific failure mode (pre-filtering, only finding classifiable things)
2. That prompt optimisation would improve but not eliminate this
3. That pipeline separation would produce qualitatively different output

All three predictions held on the primary model. The framework correctly identified *where* the degradation would occur and *what kind* of improvement pipeline separation would produce.

### The framework needs refinement

The cross-model variance was not predicted. The theory needs to account for:
- Why some models resist mode interference better than others
- Whether pipeline benefits scale with model capability (do frontier models benefit more or less?)
- Whether the pipeline's benefits are task-specific (does investigation + evaluation interference vary by domain?)
- Whether there are prompt-level interventions that can approximate pipeline-level mode separation without the multi-agent overhead

### Testable predictions for remaining experiments

Based on A1, we can predict:

1. **Tasks with stronger investigation/evaluation separation should show larger pipeline gains.** If A2 (research synthesis) or A3 (code review) involve heavy investigation, expect the Claude pipeline gap to be similar or larger.

2. **Tasks that are primarily convergent (evaluation-dominant) should show smaller pipeline gains.** If the task is mostly classification and recommendation without deep investigation, the monolithic version may be closer to the pipeline.

3. **The variance reduction effect should replicate.** Better stance scaffolding should consistently reduce run-to-run variance in pipeline outputs, even if it doesn't raise the ceiling.

4. **Models that underperformed on A1 pipeline should be checked for task-specific interference.** Gemini's DPA miss might be a fluke or might indicate that model's pipeline handling needs different stage design.

---

## Files Referenced

### Evaluation data
- `evaluation/baseline-vs-optimised.md` — Three-tier blind evaluation (Claude)
- `evaluation/blind-evaluation.md` — Tier 1 vs Tier 2 blind comparison (Claude)
- `evaluation/tier2-revision-comparison.md` — Five-run Tier 2 scorecard (old + new)
- `evaluation/tier2-old-qualitative.md` — Senior-lawyer assessment, Tier 2 runs 1-3
- `evaluation/tier2-new-qualitative.md` — Senior-lawyer assessment, Tier 2 runs 4-5
- `evaluation/tier3-old-qualitative.md` — Senior-lawyer assessment, Tier 3 runs 1-3
- `evaluation/tier3-new-qualitative.md` — Senior-lawyer assessment, Tier 3 runs 4-5

### Cross-model evaluations
- `gemini-3-pro-preview/evaluation/blind-evaluation-gemini-3-pro-preview-2026-03-15.md`
- `gpt-5.2/evaluation/blind-evaluation-GPT-5.2-2026-03-15.md`
- `gpt-5.2-codex/evaluation/blind-evaluation-gpt-5.2-codex-2026-03-15.md`
- `gpt-5.3-codex/evaluation/blind-evaluation-gpt-5.3-codex-2026-03-15.md`
