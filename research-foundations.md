# Research Foundations

What we think is true, why we think it, and what we're testing. This document captures the theoretical framework behind the experiments — written as working hypotheses, not established conclusions.

---

## The Core Insight: Language Carries Cognitive Mode

LLMs are language models. Language is the only medium they process. And language carries the cognitive mode of the person who produced it.

When a human writes in exploratory mode, the text has different statistical properties than when they write in evaluative mode. Different sentence structures, different transition words, different hedging patterns, different levels of commitment. An LLM trained on billions of words has learned these distributions. When you put evaluative language in the context, you activate distributional patterns associated with evaluation. The model doesn't need to "be cognitive" for this to work. It just needs to have learned that evaluative language predicts more evaluative language.

**We are not claiming LLMs have cognition.** We are claiming that:

1. Different types of human thinking produce different patterns of language
2. LLMs learned those patterns from training data
3. The patterns in the context window influence what the model generates next
4. Therefore, mixing incompatible language patterns (from incompatible cognitive modes) creates distributional interference that degrades output

This reframe matters because it sidesteps the mechanistic objection ("LLMs don't have working memory / task-set inertia / cognitive modes"). We don't need them to. We need them to have learned the language that those mechanisms produce — which they have, because that's what the training data is.

---

## The Cognitive Stack

Language patterns don't appear from nowhere. They're shaped by layers of human cognition, each one influencing the layers below it. When we design prompts, we can intervene at any layer — and higher-layer interventions cascade further.

```
Epistemic stance    →  How the writer relates to knowledge ("I'm discovering" vs "I know")
    ↓
Intent / goals      →  What the writer is trying to achieve ("understand" vs "judge")
    ↓
Expertise / posture →  Who the writer is in relation to the work ("consultant" vs "auditor")
    ↓
Cognitive mode      →  What type of thinking is active (investigating vs evaluating)
    ↓
Register            →  How the writer writes (hedging, commitment, vocabulary choices)
    ↓
Language patterns   →  Statistical regularities the LLM learned
    ↓
Tokens              →  What the LLM actually processes
```

Each layer shapes the one below it. Changing a single word at the epistemic layer ("observation" vs "finding") cascades through mode, register, and language patterns to produce fundamentally different output. This was discovered empirically in the Conditional Access pipeline project — the word "observation" produced exploratory output, "finding" produced judgmental output, from the same model on the same data.

### Practical implications

- **Token/pattern level** (removing numeric anchors, word choice): Easy, predictable, limited scope
- **Register level** (seeds vs lenses, instruction style): Moderate effort, shapes whole sections
- **Cognitive mode level** (mode separation, context isolation): Architectural, high impact (the V3/V4 result)
- **Expertise/posture level** (CTA, role framing): Largest unlock in the original project — "four principles on a page"
- **Epistemic/intent level** ("observation" vs "finding", "not a verdict"): Subtle but pervasive

The higher up the stack you intervene, the more cascading effect. This is why Cognitive Task Analysis was such a big unlock — it operated at the expertise layer, which reshaped everything below it.

---

## The Trust Chain

In a multi-agent pipeline, each layer builds on the cognitive quality of the layer below it. This maps directly to the cognitive stack — and the cascade works in both directions.

**Upward**: If a lower layer uses evaluative language ("finding", "critical", severity ratings), that register propagates upward. Investigation pre-filters because the input already carries evaluative mode. Synthesis compresses prematurely because the investigation output already carries commitment.

**Downward**: If the synthesis layer is contaminated (V3 — QA mixed with synthesis), the handover sets a different tone for everything that follows. The consultant enters the triage session in a different posture. Their recorded entries carry that posture into the report.

The pipeline in the original project demonstrates this:
- L1 extracts (convergent, "observations" not "findings")
- Story grouping classifies (convergent, seeds appropriate for classification)
- L3 framework assessment (convergent, runs *before* investigation to pre-load context)
- Story investigator (divergent, clean context, follows threads)
- Landscape QA gate (convergent, separate from synthesis)
- Landscape synthesis (divergent, clean context — the V4 version)
- Triage (interactive, human-driven mode transitions)
- Strategic reframing (different audience, different register)
- Report compilation (generation, not analysis)

Each agent does one type of thinking. The database between stages strips cognitive mode — a structured record doesn't carry the exploratory tone of the investigation that produced it. The schema IS the cognitive boundary.

---

## The Three-Tier Experiment Model

When testing whether cognitive mode principles improve a prompt, we test three levels of intervention:

### Tier 1: Original
The prompt as-is. Run it, capture output, score it. This is the baseline.

### Tier 2: Optimised
Same prompt structure, better cognitive hygiene:
- Remove numeric anchors ("find 3-5 issues" → "surface what you find")
- Replace seeds with lenses (specific issue lists → open analytical questions)
- Add scope boundaries ("you are investigating, not assessing")
- Soften fixed category lists
- Reorder sections so exploration precedes judgment

This tests: can you improve output by fixing interference *within* a single prompt?

### Tier 3: Pipeline Reconstruction
Split the prompt into multiple agents, each doing one type of thinking in a clean context, with deliberate handoffs that strip cognitive residue between stages.

This tests: is the single-prompt architecture itself the ceiling? Does splitting into a pipeline produce a *qualitative shift* (like V3 → V4)?

**If Tier 2 improves things incrementally and Tier 3 produces a qualitative leap, the headline finding is: the monolithic prompt is the ceiling, not the floor.**

---

## The Thesis: Is the Monolithic Paradigm Fundamentally Flawed?

The industry trend is toward bigger, more comprehensive single prompts. Skills, plugins, progressive loading — these are mechanisms to make prompts effectively longer without hitting token limits. The assumption is: more context = better output.

Our hypothesis: that assumption may be backwards for complex tasks.

- More context means more cognitive mode mixing
- More instructions means more interference between incompatible types of thinking
- Skills loaded on demand don't just add capabilities — they contaminate the context with whatever cognitive posture they carry
- The contamination is invisible because the output still looks fine ("good output hides great output")

The alternative: smaller, cognitively scoped agents in a pipeline. Each does one type of thinking in a clean context. Structured handoffs strip cognitive residue between stages.

This doesn't mean every prompt needs to be a pipeline. Simple tasks with one or two compatible types of thinking work fine as single prompts. The hypothesis applies specifically to complex tasks that require incompatible types of thinking — investigation AND evaluation, exploration AND generation, synthesis AND quality checking.

### The skills contamination corollary

Skills that get progressively loaded into an agent's context are a contamination vector. A base agent with an investigative posture loads a skill with evaluative framing — now investigation and evaluation share the context. The contamination is non-deterministic (depends on which skills load in which session), making it hard to debug. An agent that "day-drinks" (hallucinating, going off-rails) on some runs but not others may be experiencing session-dependent mode contamination from skill loading.

---

## What Field Is This?

This work sits at an intersection, not within a single discipline:

| Field | What it contributes |
|-------|-------------------|
| **Cognitive psychology** | Interference mechanisms (task switching, proactive interference, cognitive load) |
| **Cognitive linguistics** | How thinking shapes language and language shapes thinking (Lakoff, Sapir-Whorf) |
| **Discourse analysis / pragmatics** | How context shapes language choices, how language carries stance |
| **Register theory** (Halliday) | How situational context determines linguistic choices — literally the study of how context carries mode |
| **Rhetoric** | Audience awareness, framing effects, how delivery shapes reception |
| **Creativity research** | Convergent/divergent thinking, flow states, when tension helps vs hurts |
| **Narratology** | Story structures, narrative framing (Harari's insight about stories building society) |

The common thread isn't "cognitive science." It's something more like: **how thinking gets expressed through language, and how language shapes thinking**. For LLMs, the specific insight is: language is the only thing they have, so the cognitive patterns encoded in language are the cognitive patterns they reproduce.

The cognitive science explains *why humans write differently in different modes*. The linguistic patterns are *what the LLM actually learned*. Both layers matter — the cognitive science predicts which combinations will interfere, and the linguistic analysis tells us what the interference looks like in text.

---

## What We Don't Know

- Whether the convergent/divergent labels are the right granularity, or whether finer distinctions matter
- Whether creative work has a fundamentally different relationship with mode tension (the boundary test)
- Whether the improvements we've seen in one domain (security policy analysis) generalise across domains
- Whether "more detail" alone (without mode separation) explains the same improvements
- Whether the cognitive stack model has predictive power beyond what simpler "focus your prompt" advice provides
- What the right intervention level is for different types of tasks (some may need only Tier 2, others need Tier 3)
- Whether the effects are model-dependent or hold across different LLMs

These are what the experiments are designed to answer.

---

## Evidence So Far

All evidence comes from one practitioner's project (the Conditional Access policy analysis pipeline). The strongest results:

- **V3 → V4 experiment**: Removing a QA section from a synthesis prompt (making it smaller) produced 12 findings instead of 8, four entirely new themes, zero losses, and a register shift from "competent audit" to "consultant who understands the room." The combined agent had 70% of its context window unused — this was not a capacity problem.

- **Seeds → lenses**: Removing numeric anchors and replacing specific issue lists with open analytical questions produced output that varied naturally with input complexity for the first time (2 findings for simple inputs, 7 for complex) and independently arrived at numbers matching expert review.

- **Agent split in knowledge-capture pipeline**: A combined evidence-gathering + investigation agent self-diagnosed that "ration = converge." Splitting into a convergent evidence-preparation step and a divergent investigation step produced deeper cross-thread connections that were impossible in the combined configuration.

- **"Observation" vs "finding"**: A single word change at the epistemic layer fundamentally changed the model's output register from catastrophising to exploratory.

These experiments need independent replication on third-party prompts across different domains. That's what this repo is for.
