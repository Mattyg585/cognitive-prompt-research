---
title: "Testing the Theory — Nine Experiments, One Failed Prediction, and a Sharper Thesis"
date: 2026-03-18
draft: false
description: "I tested the cognitive mode separation theory against Anthropic's production prompts, a professional reasoning benchmark, and five additional models. Pipeline won where investigation was required. It lost where recognition was sufficient. The failed prediction was the most useful result."
summary: "The convergent/divergent framework from my AI pipeline project was a theory built on one domain. I tested it against Anthropic's knowledge-work-plugins across six domains, then against a professional reasoning benchmark. Pipeline won in five of the original six, then lost on the benchmark — and the failure sharpened the thesis into something more honest: pipelines earn their cost only when the correct output can't be produced without seeing the specific input data."
tags: ["AI", "Context Engineering", "Prompting", "Cognitive Modes", "LLM"]
series: "AI Reasoning Engine"
seriesOrder: 5
---

The previous posts in this series documented what I found building one system in one domain. A [reasoning engine for Conditional Access policies](/blog/what-i-learned-building-ai-tools-that-actually-think/) that emerged over [seven months of wrong turns](/blog/why-good-prompting-wasnt-enough/), a [convergent/divergent framework](/blog/context-carries-cognitive-mode/) that explained why the architecture worked, and the [evidence behind those claims](/blog/the-evidence-for-thinking-in-modes-evidence/).

All of it came from one project, one domain, one practitioner. The honest version of where I left it: I had a framework that worked for me, with evidence I trusted but couldn't rule out as self-confirming. The recursive problem — a system built on mode separation, investigating itself, finding that mode separation matters — was real. I said so at the time.

So I tested it on someone else's prompts.

---

## Anthropic's Production Prompts

Anthropic publishes a set of [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) — production-quality prompt templates for Claude, covering legal contract review, marketing content, HR performance reviews, design research synthesis, engineering debugging, and security operations incident response. Six domains. Six different types of knowledge work. None of them mine.

I ran each one through three tiers of intervention:

**Tier 1 — Baseline.** The original prompt, unchanged. Run it, capture the output, score it.

**Tier 2 — Optimised.** Same prompt structure, better cognitive hygiene. Remove numeric anchors ("find 3-5 issues" becomes "surface what you find"). Replace content prescription with analytical lenses. Add scope boundaries between thinking modes. Reorder sections so exploration precedes judgment. Fix the prompt without changing the architecture.

**Tier 3 — Pipeline.** Split the prompt into multiple agents, each doing one type of thinking in a clean context, with structured handoffs that strip cognitive residue between stages. Change the architecture.

The bet was the same as the V3/V4 experiment from the [third post](/blog/context-carries-cognitive-mode/): if Tier 2 improves things incrementally and Tier 3 produces a qualitative leap, then the monolithic prompt is the ceiling, not the floor.

---

## A Better Framing

Before the results — I need to correct something from the earlier posts.

I used "convergent" and "divergent" as labels for two types of thinking. Those labels were useful. They got me from "something's off" to "here's what to fix." But they carried an implication I didn't intend: that the AI is doing convergent or divergent thinking. That's a claim about cognition, and I don't think it's the right claim.

Here's what I think is actually happening.

LLMs are language models. Language is the only medium they process. And language carries the cognitive mode of the person who produced it. When a human writes in exploratory mode, the text has different statistical properties than when they write in evaluative mode — different sentence structures, hedging patterns, transition words, levels of commitment. An LLM trained on billions of words has learned these distributions. When you put evaluative language in the context, you activate distributional patterns associated with evaluation. The model doesn't need to "be cognitive" for this to work. It just needs to have learned that evaluative language predicts more evaluative language.

I'm not claiming LLMs have cognition. The claim is simpler:

1. Different types of human thinking produce different patterns of language
2. LLMs learned those patterns from training data
3. The patterns in the context window influence what the model generates next
4. Mixing incompatible patterns creates distributional interference that degrades output

When you put a quality-checking section in the same context as a synthesis task, you're not creating "cognitive interference" in the model's mind. You're creating **distributional interference** — the statistical patterns of evaluative language pull the generation away from the patterns associated with exploratory synthesis. The model does what it always does: predicts what comes next given what came before. And what came before is now carrying evaluative framing.

This reframe matters because it sidesteps the mechanistic objection. "LLMs don't have working memory or task-set inertia or cognitive modes." Fine. They don't need to. They need to have learned the language that those mechanisms produce — which they have, because that's what the training data is.

But it also matters for a practical reason that I think is underappreciated: **cognitive science isn't for the model. It's for the person writing the prompt.**

When you write a prompt with evaluative framing — severity ratings, classification criteria, compliance checklists — you're not triggering cognition in the AI. You're shaping the distributional patterns the model will follow. Knowing how human cognitive modes map to language patterns is practically useful because it tells you what you're *actually doing* when you choose one word over another. "Observation" and "finding" are both English words. They activate different distributional patterns. One opens exploration, the other triggers judgment. Cognitive science tells you *why* — and linguistics tells you *how it shows up in the text the model processes*.

This means that cognitive science, linguistics, rhetoric, creativity research — fields the AI industry has largely ignored when thinking about prompt design — actually matter. Not because AI thinks like a human, but because the training data is human language, and those fields are the ones that understand how thinking gets encoded in language.

The output still looks fine. Competent, thorough, professional. Good output hides great output. The gap only appears when you separate the modes and compare.

---

## What the A-Series Experiments Showed

| Experiment | Domain | Baseline | Optimised | Pipeline | External Validation |
|---|---|---|---|---|---|
| A1 | Legal contract review | 3rd | 2nd | **1st** | Claude + Gemini: unanimous |
| A2 | Marketing content | 3rd | **1st/2nd** | **1st/2nd** | Split — creative boundary condition |
| A3 | HR performance review | 3rd | 2nd | **1st** | Internal |
| A4 | Design research synthesis | 3rd | 2nd | **1st** | Internal |
| A5 | Engineering debug | 3rd | 2nd | **1st** | Internal |
| A6 | SecOps incident response | 3rd | 2nd | **1st** | Internal |

Pipeline scored highest in all six experiments. In five of six, the gap between Pipeline and Optimised was larger than the gap between Optimised and Baseline.

That last part matters. Tier 2 — fixing the prompt — consistently improved things. But Tier 3 — separating the architecture — produced a different magnitude of improvement. The prompt-level fixes address prompt-level problems: anchors, seeds, prescriptive language. When you've fixed all of those and the output is still leaving something on the table, the remaining improvement comes from the architecture itself. The single context is the ceiling.

A5 — engineering debugging — made this especially clear. The original prompt was already well-structured. Tier 2 added nothing. Same score as baseline. But the pipeline jumped to maximum. A clean prompt in a contaminated architecture is still a contaminated prompt.

### What the improvements actually look like

These aren't marginal score differences. The pipeline produces qualitatively different documents.

**Legal (A1)**: The baseline review lists clause deviations. The pipeline version identifies compound interactions between clauses — your data goes into ML training under Section 1.6, survives termination under Section 5.6, and there's no export mechanism under Section 5.5. Three separate provisions that interact as a single structural risk. The pipeline scripts the negotiation move-by-move and predicts what the counterparty's responses will reveal about their organisation.

Two independent models with zero project context both ranked the pipeline first. Claude Web called it: *"treats the contract as a deal, not a document."* The baseline earned: *"competent, thorough piece of work... earns third not because it's wrong, but because it doesn't do what the other two do on top of being thorough."*

That second quote is the finding in miniature. The baseline is fine. Nobody reading it would complain. You don't see what's missing until you see what a separated architecture produces alongside it.

**Design Research (A4)**: The baseline catalogues interview themes — here's what participants said about X, grouped together. The pipeline surfaces compound insights no single interview contains. *"Workarounds are specifications written in behaviour."* *"Partial adoption produces negative value, not partial value."* The evaluator's summary: *"would actually change how I make decisions"* versus *"template faithfully executed."*

**SecOps (A6)**: The baseline produces a standard postmortem with a mechanical 5 Whys analysis. The pipeline reframes: *"confidence accumulates across checkpoints without coverage expanding"* and *"multiple overlapping checks can produce less safety than one well-scoped check."* Organisational learning versus compliance document.

### A1 v3: The gap is architectural

I re-ran the legal contract review with v3 of the agents — three pipeline stages instead of four, third iteration of the Tier 2 prompt. Three rounds of prompt improvement. Blind evaluation. Tier 2 scored 23/30. Pipeline scored 28/30.

What the pipeline found that Tier 2 did not: a five-clause data rights cascade across Sections 1.4, 1.5, 1.6, 5.6, and 11.1. A compound risk where 29-day suspension combines with non-refundable fees and no SLA remedy. A non-renewal notice date that defaults against the customer. Indemnification exclusions that hollow out the protection they appear to offer. Post-termination ML model persistence. The evaluator's language: "a lawyer who had read Candidate Y and then read Candidate X would be aware of what Candidate X missed, not the reverse."

I also ran Tier 2 five times to test consistency. All five runs identified the same core issues, missed the same non-obvious issues, and scored 3/5 on Natural Variation. The template inherited from the prompt determines what gets found. The structural ceiling isn't about prompt quality — three iterations of improvement didn't lift it. It's about what a single context window can do when investigation and evaluation share the same space.

### Validation

For A1, A2, and A4, I ran blind evaluations with Claude (web interface, fresh session, no project context) and Google Gemini. The evaluators received randomised IDs — they didn't know which output came from which tier. They couldn't know, because the IDs were randomly generated strings like WLQZF0 and 8SNX69.

They invented their own vocabulary for what they saw. Claude Web described the legal pipeline output as understanding "the deal is between two organisations with competing interests, not between a reviewer and a document." Gemini used different language but arrived at the same ranking. Nobody told them what to look for. The rankings converged independently.

---

## The B2 Experiment: Where the Prediction Failed

PRBench is a benchmark for professional reasoning — tasks authored by domain experts with detailed scoring criteria. I picked a hard task: 26 criteria covering HSR antitrust law, scored by Sonnet 4.6 against expert-authored rubrics. This was the kind of complex knowledge work where I expected the pipeline to shine.

The prediction: Baseline < Tier 2 < Pipeline.

The result: Baseline 0.759. Pipeline 0.849. Tier 2 0.950.

Tier 2 won. Not by a little — by ten percentage points over the pipeline. A single system prompt with the right epistemic stance, scope boundaries, and uncertainty elevation scored 25 of 26 criteria. The pipeline scored 22. The pipeline was better than baseline, but it wasn't better than a well-written monolithic prompt.

The category-level predictions were worse. I expected the pipeline to improve Handling Uncertainty and Practical Utility. It didn't — both matched baseline. I expected Instruction Following to be unchanged. It was the pipeline's strongest category and the only tier to score 1.000 on it. The theory's predictive power on this task was poor.

### Why the pipeline lost

The pipeline lost for a specific reason, and the reason is more useful than a clean win would have been.

HSR antitrust law is knowledge the model already has. The correct analysis — procedural requirements, valuation mechanics, regulatory strategy — lives in training data. The model doesn't need to investigate the input to figure out what matters. It recognises the pattern and generates the right response. That's recognition-primed decision making (Klein), and for tasks where recognition is appropriate, it works.

The pipeline imposed investigation scaffolding on a task that didn't need investigation. Worse, the handoff schemas between stages stripped procedural detail that mattered. Criteria 17-19 (procedural valuation mechanics) scored 0.000 on the pipeline — same as baseline. A specific question about recent SEC commentary (criterion 26) got lost in the handoff compression. The structured boundary between stages, which is the pipeline's whole mechanism, threw away domain content the model already knew how to use.

---

## The Litmus Test

The B2 failure, set against the A-series results, sharpened the thesis into something I can actually use:

**Could the correct output be produced without seeing the specific input data?**

If yes — recognition-primed. The model matches patterns from training to generate the right analysis. Tier 2 is sufficient. Clean up the prompt, set the right epistemic stance, and get out of the way.

If no — investigation-required. The answer lives in the data, not in the model's prior knowledge. The pipeline earns its cost by forcing the model to actually look before it judges.

PRBench is recognition-primed. The correct HSR analysis could be produced by someone who knows HSR law and reads the task description. The contract in A1 is investigation-required. The compound risk where your data enters ML training under Section 1.6, survives termination under Section 5.6, and has no export mechanism under Section 5.5 — that lives in the specific contract. No amount of legal knowledge generates it without reading the document.

This is the A1/B2 contrast. Same framework, opposite predictions, both confirmed. The litmus test explains why: A1 is investigation-required, B2 is recognition-primed.

---

## A2: Voice Is the Dimension That Matters

The marketing content experiment got a full three-tier evaluation — nine outputs, three per tier, blind-scored. Baseline 17/30. Tier 2 24/30. Pipeline 29/30.

The surprise was where the gap lived. Voice and Engagement showed the largest spread of any dimension across all experiments: baseline 2, Tier 2 4, pipeline 5. The evaluator described the pipeline output as sounding like "someone who has lived this experience, not someone who understands it intellectually." The baseline-to-Tier 2 jump was immediately visible. The Tier 2-to-pipeline jump was subtler — visible to a sophisticated reader, easy to miss otherwise.

Earlier blind evaluations had flagged creative writing as a boundary condition where the pipeline might not help. The full evaluation suggests the boundary is more nuanced than that. The pipeline helps with creative work — but through voice quality and audience modelling, not through the analytical depth that drives improvement in A1 and A6. The dimension that matters shifts with the domain.

---

## Why Domains Respond Differently

The distributional interference mechanism from the framing section above is correct but incomplete. It describes what happens — incompatible language patterns pulling generation in conflicting directions — but it doesn't explain why the interference helps some tasks and hurts others.

Three concepts fill the gap.

**Premature closure** (Croskerry, 2003) is the single most common diagnostic error in medicine — accepting a diagnosis before investigation is complete. The investigation-evaluation toxic pair that the pipeline separates is premature closure. The model sees the contract, recognises familiar patterns, and starts generating analysis before it has finished looking. Medicine's intervention is the same as the pipeline's: force a differential before committing. Stage 1 of the pipeline is a forced differential.

**Recognition-primed decision making** (Klein) is the complement. Under monolithic prompting, the model recognises a pattern and activates the first plausible response. For tasks where the pattern is correct — PRBench, where the model knows HSR law — RPD is efficient. For tasks where the pattern is incomplete — A1, where the compound risks live in the specific contract — RPD forces novel data through familiar templates. The pipeline adds value precisely when RPD is the wrong strategy.

**The expertise reversal effect** (Kalyuga, 2007) explains the cost. Scaffolding that helps novices degrades expert performance. The pipeline is scaffolding. When the model is already expert at the task, the scaffolding is overhead. When the task requires investigation the model can't shortcut, the scaffolding is what prevents premature closure. The B2 pipeline failure is literally the expertise reversal effect — the model was already expert at HSR law, and the pipeline's investigative scaffolding hurt rather than helped.

These aren't decorative theory. They're why the litmus test works. "Could the correct output be produced without seeing the data?" is asking: will recognition-primed decision making give you the right answer, or will it give you premature closure?

The cognitive stack from the earlier posts still holds as a map of where interventions land:

```
Epistemic stance  →  Intent  →  Expertise  →  Cognitive mode  →  Register  →  Language patterns  →  Tokens
```

Each layer shapes the one below it. Pipeline separation operates at the cognitive mode layer. The type of improvement varies by domain:

| Domain type | What Pipeline improves | Stack layer |
|-------------|----------------------|-------------|
| Analytical (A1, A6) | Reasoning — connecting evidence, modelling adversaries | Cognitive mode |
| Synthesis (A4) | Depth — reframing patterns rather than cataloguing | Cognitive mode + Expertise |
| Template (A3) | Judgment — nuanced assessment vs filling fields | Expertise + Register |
| Sequential (A5) | Architecture — the investigation structure itself | Cognitive mode |
| Creative (A2) | Voice — pipeline helps, but through a different dimension | Register |
| Knowledge-based (B2) | Nothing — scaffolding becomes overhead | N/A — expertise reversal |

The higher in the stack the improvement lives, the more pipeline separation helps. Analytical work benefits most because the improvement is at the cognitive mode layer — exactly where the pipeline intervenes. Creative work benefits through voice quality at the register layer. And knowledge-based reasoning doesn't benefit at all — the model already has what it needs, and the pipeline's handoff boundaries strip content that matters.

---

## Cross-Model Testing

Everything above was generated by Claude. That's a problem. If the findings are model-specific, the theory is less interesting. So I re-ran all six A-series experiments across four additional models via GitHub Copilot CLI: GPT-5.2, GPT-5.2-Codex, GPT-5.3-Codex, and Gemini 3 Pro Preview.

The results are more interesting than a clean replication.

| Model | Pipeline Wins | Pipeline Fails | Safe Improvement |
|---|---|---|---|
| Claude Opus 4.6 | 5/6 | 0 | Pipeline consistently best |
| GPT-5.3-Codex | 6/6 | 0 | Pipeline consistently best |
| GPT-5.2 | 2/6 | 0 | Optimised was the safe bet |
| GPT-5.2-Codex | 2/6 | **3 catastrophic** | Pipeline actively dangerous |
| Gemini 3 Pro | 2/6 | 2 serious | Pipeline unreliable |

GPT-5.3-Codex mirrored Claude exactly — pipeline won across the board. GPT-5.2-Codex was a disaster. Three pipeline runs scored below 2/5 — one produced an intake checklist instead of a postmortem, another output only clarification questions instead of content, a third was skeletal with placeholders. Gemini 3 Pro was mixed: the pipeline introduced gender bias in two experiments (masculine pronouns for the gender-neutral name "Jordan Chen") that the baseline handled perfectly, and consistently missed a critical compliance finding (DPA gap) that the monolithic version caught.

### Pipeline is an amplifier

The pipeline doesn't add quality. It creates the *conditions* for quality. Whether the model fills those conditions depends on the model.

On models with strong context comprehension — models that can infer task intent from structured input without being told explicitly — the pipeline produces qualitative leaps. On models that need more explicit context to understand what they're supposed to produce, the pipeline fails at the handoff boundaries. The handoff strips cognitive mode (that's the point) but it also strips higher-stack context: intent, task purpose, the larger picture. Models that can reconstruct those from the structured input succeed. Models that can't produce the wrong artifact entirely.

### The trust chain works in both directions

The trust chain theory — from the original CA pipeline project — predicted that each layer's cognitive quality cascades to the layers above and below it. The positive direction was demonstrated in the Claude experiments. The cross-model testing demonstrated the **negative direction**: when a pipeline stage fails, the failure cascades. A Stage 1 that produces an intake checklist instead of investigation output means every subsequent stage works with the wrong input. The pipeline amplifies in both directions.

Predicting how something fails is harder to fake than claiming it works. The cascade failures are arguably stronger evidence for the trust chain than the positive results.

### The safe bet

Tier 2 — prompt-level optimisation — improved output across every model tested. Removing anchors, replacing seeds with lenses, adding scope boundaries. These fixes helped everywhere without risk of catastrophic failure. If you're not sure your model can handle a pipeline, optimise the prompt. That's not a consolation prize — Tier 2 consistently produced meaningful improvement.

---

## A RAG Implication

There's a retrieval-augmented generation implication I haven't tested yet but think matters. Standard RAG stuffs retrieved documents into context and generates — the same dynamic as A1 baseline. The model sees the retrieved chunks through the lens of what it already knows how to say. The findings that A1's pipeline surfaced and Tier 2 missed are what you'd predict happens in production RAG over novel documents.

Most production RAG systems may be leaving their most valuable findings on the table. Nobody knows, because the output looks competent. That's probably the most impactful experiment to run next.

---

## What I Trust and What I Don't

I trust:

- **The direction.** Baseline was worst across all models and all experiments. Optimised was better everywhere. The pattern is real.
- **The external validations.** A1 and A4 had blind evaluation by models with zero project context. Rankings converged independently. That's the strongest evidence.
- **The litmus test direction.** Investigation-required tasks consistently benefit from pipeline separation. Recognition-primed tasks don't. The A1/B2 contrast makes this sharp.
- **The cascade failures.** They match the theory's predictions about how trust chains break.

I'm uncertain about:

- **The litmus test boundary.** The test is new. Creative work (A2) sits in a space where the pipeline helps through voice rather than analytical depth. Consulting engagements, code review of unfamiliar codebases, organisational assessments — these involve data-dependent reasoning but may not need full pipeline separation. The theory says investigation-required. I haven't tested it.
- **The minimal viable pipeline.** A1 v3 works with three stages instead of four. A2 works with two. The critical boundary appears to be investigation/evaluation separation — everything else is optimisation. But I haven't tested a two-stage pipeline on analytical tasks to see if that holds.
- **Whether the pipeline failures are theory failures or implementation failures.** The pipeline was designed by Claude, for Claude. It was not tuned for other models. The handoff specs might need model-specific tuning. That's an interesting finding in itself — cognitive pipeline architecture may not be portable across models without adaptation.
- **Platform differences.** Claude Code (automatic context isolation via subagents) and Copilot CLI (manual session management) are different execution environments. Some failures may reflect the platform, not the model.
- **The perfect scores on Claude.** Pipeline scored maximum marks in four of six experiments. That's still suspicious. The cross-model data partially addresses this — seeing the same pipeline produce both 5/5 and 1/5 depending on the model makes the high scores feel more real.
- **Pipeline cost.** A pipeline uses 4-12x more tokens. For a legal brief, worth it. For a quick summary, not.
- **Whether stronger models make pipelines unnecessary.** The decomposition literature (arXiv:2506.06843) finds pipeline advantages diminish as models improve. The expertise reversal effect suggests that if the model becomes expert enough at investigating novel data within a single context, the scaffolding becomes overhead. But that's theory, not data.
- **My time.** This is a side project, not funded research. I haven't manually reviewed every pipeline stage across every model. There are likely process flaws I haven't caught. That's an invitation, not an excuse.

---

## A Note on Skills, Plugins, and Where This Leads

I want to be clear: I'm not arguing that skills are bad. Skills that add domain knowledge or tool access without carrying a strong cognitive posture are fine. Skills that share a compatible thinking mode with the base agent are fine. The issue is specifically when skills carry *incompatible* cognitive postures into the same context — an investigation agent loading an evaluation skill, for example. That's where the distributional interference kicks in.

What I think is more interesting is the direction the tooling is already heading. GitHub Copilot now has custom agents with handoff mechanisms — one agent finishes, a transition button appears, and structured output carries to the next agent's fresh context. That's almost exactly the pipeline architecture this research advocates for. Claude Code has subagents that spawn with isolated contexts. The infrastructure for cognitively scoped pipelines exists today.

The practical implication: a plugin doesn't have to be a single prompt. It can be a wrapper around a pipeline. The user invokes the plugin the same way. What changes is what happens inside it — sequential agents with clean handoffs instead of one big context window accumulating interference. Same UX, different cognitive architecture underneath. The legal contract review plugin could internally run a Contract Reader, then a Playbook Comparator, then a Redline Writer, then a Strategic Advisor pipeline, with the user seeing only the final output. No change to the interface. Significant change to the quality.

The argument isn't skills versus no skills. It's: for investigation-required tasks, the evidence says scoped agents with deliberate handoffs produce qualitatively better output than monolithic contexts. For recognition-primed tasks, the evidence says clean up your prompt and save the tokens. The tooling already supports both. The litmus test tells you which.

---

## Where This Leaves Things

The thesis is narrower and more honest than where I started. Not "pipelines beat monolithic prompts on complex tasks." Instead: pipelines beat monolithic prompts specifically when the task requires investigation of novel data — when the correct output can't be produced from training knowledge alone. For everything else, clean up your prompt and save the tokens.

The cognitive science connections aren't window dressing. They're why the litmus test predicts correctly. Premature closure, recognition-primed decision making, expertise reversal — these are mechanisms with decades of research behind them, and they map directly to the experimental results. The framework went from "this seems to work" to "here's why it works and when it doesn't."

The thing I got wrong — the B2 prediction — turned out to be the most useful result. A theory that always wins is a theory you can't learn from. The failure narrowed the claim, sharpened the test, and connected the work to cognitive science that explains both the successes and the failures.

The full research — all experiments, outputs, evaluations, the theoretical framework, and the toolkit — is [on GitHub](https://github.com/Mattyg585/cognitive-prompt-research). MIT licence. Do whatever you want with it.

The toolkit includes a prompt analysis agent that you can point at any prompt. It identifies mode interference patterns and recommends both prompt-level fixes and pipeline reconstruction. It works in Claude Code and GitHub Copilot. The agents encode the theory — you don't need to understand cognitive linguistics to use them. Point the architect at your prompt, read what it says, decide if the fixes are worth it.

If you work in a domain where investigation of novel data is the core task — legal, medical, security analysis, anything where the answer lives in the specific case rather than the general knowledge — I'd like to know whether this maps to your experience. And if you're building RAG systems, I'd especially like to hear whether the premature closure framing matches what you're seeing in production.

This started as a side project about Conditional Access policies. It turned into something I didn't expect — a question about whether the way we build AI prompts is leaving quality on the table in a way that's invisible from inside. Nine experiments later, I think the answer is yes for investigation-required work, probably not for knowledge-based reasoning, and worth investigating further either way.

The output was always good enough to stop at. Until you see what it looks like when the modes aren't fighting each other.

---

*[Matt Graham](https://www.linkedin.com/in/matthewgrahamau/) is a cloud consultant specialising in the Microsoft ecosystem, based on the Sunshine Coast, Australia. The research described in this post used prompts from Anthropic's knowledge-work-plugins as baselines, with experiments conducted using Claude Code (Opus 4.6) and cross-model testing via GitHub Copilot CLI. External validation by Claude Web and Google Gemini. Full data and methodology at [github.com/Mattyg585/cognitive-prompt-research](https://github.com/Mattyg585/cognitive-prompt-research).*
