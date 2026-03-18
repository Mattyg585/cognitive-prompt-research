# Cross-Experiment Findings

Updated as experiments complete. Patterns, boundary conditions, and surprises.

---

## Results Overview

### Claude (Opus 4.6) — Original Tests

| # | Domain | Baseline | Optimised | Pipeline | External Validation |
|---|--------|----------|-----------|----------|-------------------|
| A1 | Legal contract review | 3rd | 2nd | **1st** | Claude Web + Gemini: unanimous |
| A2 | Marketing content | 3rd | **1st/2nd** | **1st/2nd** | Split — creative boundary condition |
| A3 | HR performance review | 3rd | 2nd | **1st** | Second internal eval confirmed |
| A4 | Design research synthesis | 3rd | 2nd | **1st** | Claude Web + Gemini: unanimous |
| A5 | Engineering debug | 3rd | 2nd | **1st** | Second internal eval confirmed |
| A6 | SecOps incident response | 3rd | 2nd | **1st** | Second internal eval confirmed |

### Cross-Model Testing (Copilot CLI)

| # | Domain | GPT-5.3-Codex | GPT-5.2 | GPT-5.2-Codex | Gemini 3 Pro |
|---|--------|--------------|---------|---------------|-------------|
| A1 | Legal | **Pipeline** | Optimised | Baseline/Opt tie | **Baseline** |
| A2 | Marketing | **Pipeline** | **Pipeline** | **FAIL** (1.3) | **Pipeline** |
| A3 | HR | **Pipeline** | **Pipeline** | **FAIL** (2.2) | Baseline/Opt tie |
| A4 | Design research | **Pipeline** (5.0) | Optimised | **Pipeline** | **Pipeline** (4.8) |
| A5 | Debug | **Pipeline** | Optimised | Pipeline (slight) | Baseline |
| A6 | SecOps | **Pipeline** (5.0) | Three-way tie | **FAIL** (1.0) | Optimised |

**Key**: Bold = clear winner. **FAIL** = pipeline scored below 2.5/5, producing wrong artifact type or incomplete output.

### Summary Across All Models

| Model | Pipeline Wins | Pipeline Fails | Optimised Safest? |
|---|---|---|---|
| Claude Opus 4.6 | 5/6 (tied 1) | 0 | Yes but pipeline better |
| GPT-5.3-Codex | 6/6 | 0 | Pipeline consistently best |
| GPT-5.2 | 2/6 | 0 | **Yes — optimised was the safe bet** |
| GPT-5.2-Codex | 2/6 | **3 catastrophic** | **Yes — pipeline actively dangerous** |
| Gemini 3 Pro | 2/6 | 2 serious | **Yes — pipeline unreliable** |

---

## Confirmed Patterns

### 1. Tier 2 (optimised) is the universally safe improvement

Across all models and all experiments, prompt-level optimisation (removing anchors, replacing seeds with lenses, adding scope boundaries) rarely made things worse. This is the one consistently positive finding across the entire study.

### 2. Pipeline is an amplifier, not a guarantee

On models that handle it well (Claude Opus, GPT-5.3-Codex), the pipeline produces qualitative leaps — compound risk analysis, counterparty modelling, organisational learning reframes. On models that don't, it produces output worse than the baseline — wrong artifact types, introduced bias, missing critical findings.

The pipeline doesn't add quality. It creates the *conditions* for quality. Whether the model fills those conditions depends on the model.

### 3. Pipeline failures cascade — as predicted

The trust chain theory predicted that a break at one stage would cascade through the pipeline. The cross-model testing confirmed this exactly:
- A6/GPT-5.2-Codex: Stage 1 produced an intake checklist instead of investigation → every subsequent stage worked with the wrong input → final output was unusable
- A2/GPT-5.2-Codex: A pipeline stage output clarification questions instead of content → downstream stages had nothing to work with
- A1/Gemini: Pipeline consistently missed the DPA gap across all 3 runs → the gap propagated through evaluation and strategy stages

The theory said "each layer's cognitive quality cascades in both directions." The failures demonstrated the negative direction of that cascade. This is arguably stronger evidence for the trust chain than the positive results — predicting how something fails is harder to fake than claiming something works.

### 4. The creative boundary condition holds across models

A2 (marketing content) showed the most nuanced results across every model tested. Even on models where pipeline generally won, the creative writing gap between optimised and pipeline was consistently smaller than in analytical domains. The register-level improvement (voice, naturalness) that matters for creative work is captured by Tier 2 fixes.

### 5. "Good output hides great output" confirmed everywhere

Every baseline output across every model was competent. Nobody reading any of them in isolation would say they're bad. The gap only appears in comparison.

---

## Pipeline Failure Modes

Three distinct failure patterns emerged from cross-model testing:

### Wrong artifact type
The pipeline stage understood the *format* of the handoff but not the *purpose*. Produced an intake checklist instead of a postmortem (A6/Codex), a planning checklist instead of a diagnosis (A5/GPT-5.2). The handoff spec carried the data but not the task intent.

### Stage didn't execute
A pipeline stage stalled or misunderstood its role entirely. Produced clarification questions instead of content (A2/Codex). The model saw the handoff input and treated it as an incomplete brief rather than material to work with.

### Pipeline introduced errors the monolithic version avoided
The pipeline stripped context that the monolithic version had — including guardrails. A1/Gemini and A3/Gemini both introduced gender bias (masculine pronouns for gender-neutral name "Jordan Chen") that baseline and optimised versions handled perfectly. A1/Gemini consistently missed a critical compliance finding (DPA gap) that the baseline caught.

### Root cause: context comprehension at handoff boundaries

The handoff strips cognitive mode (that's the point). But it also strips higher-stack context — intent, epistemic stance, task purpose. Models that can reconstruct those from the structured input and the agent prompt succeed. Models that need them to be explicit in the context fail.

This suggests a potential fix: richer handoff specs that carry **intent** forward without carrying **mode**. Not just "here's the structured output from Stage 1" but "here's what Stage 1 found, and the overall task is X." Pass the intent layer while still stripping the cognitive mode layer.

---

## What This Means Practically

### If you're building with a strong model (Claude Opus, GPT-5.3+)
Pipeline reconstruction is worth it for complex analytical tasks. The qualitative improvements are real and independently validated.

### If you're building across models or with older models
Stick with Tier 2 (prompt-level optimisation). It's the universally safe improvement. Remove anchors, replace seeds with lenses, add scope boundaries. These fixes help everywhere without risk of catastrophic failure.

### If you want to try pipelines on an untested model
Test the handoff first. Run one pipeline stage and check: did the model understand what artifact to produce? Did it maintain task intent from the handoff spec? If not, enrich the handoff spec with explicit intent context before running the full pipeline.

---

## Honest Limitations

### Process fragility
The pipeline design was created by Claude, for Claude, automated while the researcher cooked a BBQ. It was not tuned for other models. The cross-model failures may reflect pipeline design fragility rather than fundamental limits of the approach. The handoff specs likely need model-specific tuning — which is itself an interesting finding about the portability of cognitive architecture.

### Platform differences
Claude Code (subagents with automatic context isolation) and Copilot CLI (manual session management) are different execution environments. Some failures may reflect Copilot CLI's context handling rather than the model's capability.

### Researcher time constraints
This is a side project, not a funded research programme. The pipeline stages weren't manually reviewed or tuned for each model. A more careful implementation might produce different results. The goal was to test the theory quickly and honestly, not to optimise for every platform.

### Single researcher
All experiment design, execution, and evaluation orchestrated by one person. Independent replication remains the strongest possible validation.

---

## The Nuanced Thesis

The original thesis: "Is the monolithic prompt the ceiling, not the floor?"

The refined thesis after cross-model testing: **For complex analytical tasks on models with strong context comprehension, the monolithic prompt is the ceiling. For other models, prompt-level optimisation (Tier 2) captures most of the improvement safely. Pipeline architecture amplifies model capability in both directions — it makes capable models much better and less capable models much worse.**

The theory (cognitive mode separation improves output) appears sound. The implementation (multi-stage pipelines with structured handoffs) is fragile and model-dependent. The universally safe intervention is Tier 2 prompt optimisation.

---

## v3 Agent Iteration Results (March 2026)

After three iterations of the prompt-architect and prompt-writer agents, we re-ran A1 and A2 to test whether the improved agents produced better prompts and whether the findings held.

### A1 (Legal Contract Review) — v3

| Tier | Score (6-dim) | Key Observation |
|------|--------------|-----------------|
| Baseline | 17/30 | Standard clause-by-clause review. Competent, template-shaped |
| Optimised (v3) | 23/30 | Stronger investigation, working theory, strategy posture shift |
| Pipeline (v3, 3-stage) | 28/30 | Found 8 things Tier 2 missed: suspension compound risk, data rights cascade, post-termination ML persistence |

The v3 pipeline reduced from 4 stages to 3 (folding Redline Writer into Playbook Evaluator) without quality loss. The investigation-evaluation separation — the critical boundary — was preserved. The pipeline's qualitative advantage persisted across all three agent versions: Tier 2 got incrementally better each time, but never closed the gap on compound risk discovery.

### A2 (Marketing Content) — v3

| Tier | Score (6-dim) | Key Observation |
|------|--------------|-----------------|
| Baseline | 16/30 | "How to Fix X Without Y" — formula headline, product tour structure |
| Optimised (v3) | 23/30 | Has a thesis ("your tools are synchronous"), confident voice |
| Pipeline (v3, 2-stage) | 28/30 | Has genuine voice — reads like someone who lived the problem |

The v3 Tier 2 **reversed the v2 regression**. The v2 Tier 2 had over-engineered the creative prompt with criterion gates and declared phases, creating anticipatory interference worse than no optimisation at all. v3 went lighter — "Read the brief as a writer, not as someone filling a template" — and it worked.

The pipeline headline ("You Already Know What Happened Last Night. You Just Don't Know It Yet.") was the best headline across all versions and tiers. The compliance editor's notes on the closing lines — "any editorial intervention there would be vandalism" — capture the voice gap between tiers.

### Agent Iteration Findings

Three versions of the agents revealed different improvement dynamics for different task types:

**Analytical tasks (A1) respond to progressive refinement.** v1→v2→v3, each measurably better. More precise mode separation, cleaner lenses, stronger strategy posture shift. The agents can keep improving these prompts incrementally.

**Creative tasks (A2) have an over-engineering trap.** v2 regressed because the writer added analytically-sound structures (criterion gates, declared phases) that created new interference in creative work. v3 fixed this by going lighter. The lesson: for creative tasks, the ceiling is reached by doing less, not more.

**The anti-pattern vocabulary prevents regression.** Adding "criterion gates create anticipatory interference" and "declared vs actual architecture" to the agents' reference material is what prevented v3 from repeating v2's mistakes. The agents learn from documented failures.

---

## The Decision Heuristic

The sharpest predictor of which tier earns its cost:

> **Can the correct output be produced without examining the specific input data?**
>
> **Yes** → Recognition-primed. Tier 2 is sufficient. The model is deploying schemas from training.
> **No** → Investigation-required. Tier 3 earns its cost. The answer lives in the data.
> **Partially** → Fuzzy middle. Tier 2 gets you 80%. Tier 3 gets you voice/depth. Cost-benefit depends on use case.

This maps to established cognitive science frameworks:
- **Premature closure** (Croskerry, 2003): The pipeline is a forced differential before diagnosis
- **Recognition-Primed Decision** (Klein): RPD is efficient for familiar patterns, harmful for novel situations
- **Expertise reversal effect** (Kalyuga, 2007): Scaffolding that helps on novel tasks degrades performance on familiar ones
- **Knowledge-telling vs knowledge-transformation** (Bereiter & Scardamalia): Monolithic prompts allow knowledge-telling; pipelines force knowledge-transformation

### RAG Implication

The same dynamic applies to Retrieval-Augmented Generation. Standard RAG stuffs retrieved chunks into context and generates — investigation and evaluation in the same pass. The model does RPD on the chunks, finding what it already knows how to classify.

For RAG over documents the model hasn't seen before (legal discovery, medical records, financial filings, codebase Q&A), this predicts premature closure: competent-looking answers that miss what's genuinely novel in the retrieved data.

A1 contract review is functionally a RAG task — the contract is the "retrieved document." The pipeline's findings that Tier 2 missed are exactly what this theory predicts. Testable with the same three-tier design applied to a RAG system.

---

## Raw Data

All outputs, evaluations, and pipeline artifacts are in the experiment directories:

**Claude (Opus 4.6)**: `experiments/A{1-6}/` (root level — baseline-runs, optimised-runs, pipeline-runs, evaluation, blind-comparison)

**v3 iterations**: `experiments/A{1,2}/baseline-runs-v3/`, `optimised-runs-v3/`, `pipeline-v3-runs/`, `evaluation/blind-evaluation-v3.md`

**Cross-model**: `experiments/A{1-6}/{model-name}/` where model-name is:
- `gpt-5.1-codex-max`
- `gpt-5.2`
- `gpt-5.2-codex`
- `gpt-5.3-codex`
- `gemini-3-pro-preview`
