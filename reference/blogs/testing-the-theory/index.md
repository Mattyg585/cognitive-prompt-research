---
title: "Testing the Theory — Six Experiments Against Production Prompts"
date: 2026-03-15
draft: false
description: "I took the cognitive mode separation theory from my Conditional Access project and tested it against Anthropic's production prompts across six domains. Pipeline won in five. The exception was the most interesting finding."
summary: "The convergent/divergent framework from my AI pipeline project was a theory built on one domain. I tested it against Anthropic's knowledge-work-plugins across legal, marketing, HR, design research, engineering, and security operations. The results were more consistent than I expected — and the one domain where the pattern broke taught me more than the five where it held."
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

## What the Experiments Showed

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

### Validation

For A1, A2, and A4, I ran blind evaluations with Claude (web interface, fresh session, no project context) and Google Gemini. The evaluators received randomised IDs — they didn't know which output came from which tier. They couldn't know, because the IDs were randomly generated strings like WLQZF0 and 8SNX69.

They invented their own vocabulary for what they saw. Claude Web described the legal pipeline output as understanding "the deal is between two organisations with competing interests, not between a reviewer and a document." Gemini used different language but arrived at the same ranking. Nobody told them what to look for. The rankings converged independently.

---

## The Creative Writing Boundary

A2 — marketing content — is where the pattern breaks, and it's the most interesting result in the whole project.

Claude Web ranked the optimised version first. Gemini ranked the pipeline first. I preferred the optimised version. The evaluators split.

The pattern: the pipeline produces better *process* — editorial reasoning, SEO strategy, content architecture. The optimised version produces better *prose* — voice, rhythm, naturalness. For a blog post, prose wins. For a legal brief, process wins.

This maps to something I've started thinking of as the cognitive stack:

```
Epistemic stance  →  Intent  →  Expertise  →  Cognitive mode  →  Register  →  Language patterns  →  Tokens
```

Each layer shapes the one below it. Pipeline separation operates at the cognitive mode layer. Creative writing quality lives at the register layer — the specific word choices, sentence rhythms, and hedging patterns that make writing feel human. For analytical work, freeing the cognitive mode cascades down and improves everything below it, including register. For creative work, the pipeline's structured handoffs may actually disrupt the register-level flow.

The right intervention for creative work might be Tier 2 — fix the register — rather than Tier 3 — separate the modes. One experiment doesn't prove a boundary condition. But it points at one, and the cognitive stack gives a reason why the boundary would be where it is.

---

## Why Different Domains Respond Differently

The type of improvement varies by domain, and the variation maps to the cognitive stack:

| Domain type | What Pipeline improves | Stack layer |
|-------------|----------------------|-------------|
| Analytical (A1, A6) | Reasoning — connecting evidence, modelling adversaries | Cognitive mode |
| Synthesis (A4) | Depth — reframing patterns rather than cataloguing | Cognitive mode + Expertise |
| Template (A3) | Judgment — nuanced assessment vs filling fields | Expertise + Register |
| Sequential (A5) | Architecture — the investigation structure itself | Cognitive mode |
| Creative (A2) | Voice — but Tier 2 captures most of this | Register |

The higher in the stack the improvement lives, the more pipeline separation helps. Analytical work benefits most because the improvement is at the cognitive mode layer — exactly where the pipeline intervenes. Creative work benefits least because the improvement is at the register layer — below where the pipeline operates, and potentially disrupted by the structured handoffs.

This isn't a post-hoc rationalisation. The cognitive stack came from the theoretical framework, and the predictions map to what the experiments actually showed. But I want to be careful about that word "predictions" — I wrote the framework before running the experiments, but I was also the person scoring them. The internal evaluations are mine. The external blind evaluations are the stronger evidence.

---

## What I Trust and What I Don't

I trust:

- **The direction.** Baseline was worst in all six experiments. Pipeline was best in five, and tied for best in the sixth. That's consistent enough across diverse domains that I believe the pattern is real.
- **The external validations.** A1 and A4 had blind evaluation by models with zero project context, using randomised IDs. Those rankings converged independently. That's the strongest evidence here.
- **The A2 boundary.** The creative writing split wasn't a failure — it was information. It tells you where the framework's explanatory power changes.

I'm uncertain about:

- **The perfect scores.** Pipeline scored maximum marks in four of six experiments (A3-A6). That's suspicious. It might mean the rubric doesn't discriminate well at the top end, or that I'm biased toward the outputs I expect to win. The external evaluations for A1 and A4 partially control for this, but the internal ones should be held carefully.
- **Single runs.** A1 and A2 had three runs per tier. A3-A6 had one. Single runs can't measure natural variation. The consistency of the pattern across all six partially compensates, but individual results should be held lightly.
- **Same model everywhere.** All outputs generated by Claude. The findings might be model-specific. I haven't tested with GPT-5 or Gemini yet.
- **LLM-as-judge bias.** The evaluator models may prefer longer, more structured output — which the pipeline tends to produce. Domain expert evaluation would be stronger.
- **Pipeline cost.** A pipeline uses 4-12x more tokens than a single prompt. For a legal brief where the pipeline catches compound clause interactions your lawyer missed, the trade-off isn't close. For a quick internal summary, a single prompt is fine. The right answer depends on what the output is worth.

What would genuinely strengthen this: independent replication, domain expert evaluation, cross-model testing, and more creative domain experiments.

---

## What This Means

The industry trend is toward bigger, more comprehensive single prompts. Skills, plugins, progressive loading — mechanisms to make prompts effectively longer without hitting token limits. The assumption: more context equals better output.

These experiments suggest that assumption may be backwards for complex tasks. More context means more cognitive mode mixing. More instructions means more distributional interference between incompatible types of thinking. Skills loaded on demand don't just add capabilities — they contaminate the context with whatever language patterns they carry. And the contamination is invisible because the output is still fine.

I don't think every prompt needs to be a pipeline. Simple tasks with one or two compatible types of thinking work fine as single prompts. The claim applies specifically to complex tasks that require incompatible types of thinking — investigation AND evaluation, exploration AND generation, synthesis AND quality checking.

For those tasks, the monolithic prompt appears to be a ceiling, not a floor. The baseline output is always competent. The gap between competent and genuinely insightful is where the pipeline operates — and that gap is invisible until you separate the modes and compare.

---

## A Note on Skills, Plugins, and Where This Leads

I want to be clear: I'm not arguing that skills are bad. Skills that add domain knowledge or tool access without carrying a strong cognitive posture are fine. Skills that share a compatible thinking mode with the base agent are fine. The issue is specifically when skills carry *incompatible* cognitive postures into the same context — an investigation agent loading an evaluation skill, for example. That's where the distributional interference kicks in.

What I think is more interesting is the direction the tooling is already heading. GitHub Copilot now has custom agents with handoff mechanisms — one agent finishes, a transition button appears, and structured output carries to the next agent's fresh context. That's almost exactly the pipeline architecture this research advocates for. Claude Code has subagents that spawn with isolated contexts. The infrastructure for cognitively scoped pipelines exists today.

The practical implication: a plugin doesn't have to be a single prompt. It can be a wrapper around a pipeline. The user invokes the plugin the same way. What changes is what happens inside it — sequential agents with clean handoffs instead of one big context window accumulating interference. Same UX, different cognitive architecture underneath. The legal contract review plugin could internally run a Contract Reader → Playbook Comparator → Redline Writer → Strategic Advisor pipeline, with the user seeing only the final output. No change to the interface. Significant change to the quality.

The argument isn't skills versus no skills. It's: for complex multi-mode tasks, the evidence says scoped agents with deliberate handoffs produce qualitatively better output than monolithic contexts. The tooling already supports this. The principled argument for *why* it works is what this research provides.

---

## What's Next

The full research — all six experiments, all outputs, all evaluations, the theoretical framework, and the toolkit — is [on GitHub](https://github.com/Mattyg585/cognitive-prompt-research). MIT licence. Do whatever you want with it.

The toolkit includes a prompt analysis agent that you can point at any prompt. It identifies mode interference patterns and recommends both prompt-level fixes and pipeline reconstruction. It works in Claude Code and GitHub Copilot. The agents encode the theory — you don't need to understand cognitive linguistics to use them. Point the architect at your prompt, read what it says, decide if the fixes are worth it.

What I'm planning: cross-model testing with GPT-5 and Gemini (if the distributional interference framing is right, it should hold across models, because all of them learned from the same human language patterns), a pure creative writing experiment to test the boundary condition properly, and skills composition testing to measure whether loading multiple skills into one context degrades each skill's output.

But the thing that would actually matter most: **domain expert review**. I'm not a lawyer. I'm not a UX researcher. I'm not a security operations engineer. The experiment outputs are in the repo. If you work in one of these domains and you have twenty minutes, read the three versions (baseline, optimised, pipeline) for the experiment in your field and tell me whether the pipeline version is genuinely better or whether I'm measuring something that doesn't matter in practice. That's the evidence I can't generate from inside.

This started as a side project about Conditional Access policies. It turned into something I didn't expect — a question about whether the way we build AI prompts is leaving quality on the table in a way that's invisible from inside. Six experiments later, I think the answer is yes for analytical work, probably not for creative work, and worth investigating further either way.

The output was always good enough to stop at. Until you see what it looks like when the modes aren't fighting each other.

---

*[Matt Graham](https://www.linkedin.com/in/matthewgrahamau/) is a cloud consultant specialising in the Microsoft ecosystem, based on the Sunshine Coast, Australia. The research described in this post used prompts from Anthropic's knowledge-work-plugins as baselines, with all experiments conducted using Claude Code (Opus 4.6). External validation by Claude Web and Google Gemini. Full data and methodology at [github.com/Mattyg585/cognitive-prompt-research](https://github.com/Mattyg585/cognitive-prompt-research).*
