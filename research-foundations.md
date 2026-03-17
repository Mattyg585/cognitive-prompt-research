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

## Data Stance: How Information Carries Cognitive Posture Through Pipelines

The trust chain describes how cognitive quality cascades between agents. But there's a related phenomenon that operates at the data level rather than the agent level: **the information passed between agents carries a cognitive stance that shapes what the receiving agent can discover**.

This emerged from two observations:
1. The CA pipeline's architecture — where the investigation agent receives both raw per-policy extractions (descriptive data) AND story groupings (classified data) — works because the investigator can follow threads the classifier didn't anticipate. If only the classified data were passed, the classifier's cognitive choices would become the ceiling for every downstream agent.
2. The A2 marketing content experiment — where the 4-stage pipeline produced technically superior output but the voice was fragmented because each agent received structured plans *about* the material rather than the material itself in its raw, engagement-inviting form.

### What data stance is

Every piece of data passed between pipeline stages has a cognitive stance — not just content, but a posture that shapes how the next agent relates to it:

| Data stance | What it looks like | What it enables downstream | What it constrains |
|------------|-------------------|--------------------------|-------------------|
| **Descriptive** | Raw extractions, observations, "what's there" | Widest downstream space — any agent can discover patterns | Nothing constraining; may overwhelm with volume |
| **Classified** | Organised by category, grouped by type, labelled | Pattern recognition within categories, cross-category comparison | Constrains to the classifier's lens — patterns that don't fit categories get dropped |
| **Evaluated** | Scored, judged, filtered, ranked | Efficient downstream processing — evaluation work already done | Most constraining — downstream agents inherit the evaluation and can only work within its boundaries |
| **Exploratory** | Threads followed, patterns noticed, tentative connections | Carries investigative momentum, may inspire further exploration | Biases receiver toward continued exploration; may carry premature commitments |
| **Generative** | Draft prose, creative artifacts, voice samples | Carries voice, tone, authorial presence | Carries the generative posture — may suppress analytical processing |

### The key insight: agent mode + data stance = processing quality

Getting either one right isn't enough:
- An investigative agent with clean prompting but **pre-evaluated data** will produce investigation-shaped evaluation (it only investigates what the evaluator already surfaced)
- A generation agent with creative prompting but **template-structured input** will produce creative-sounding template completion
- A synthesis agent with proper scope boundaries but **exploratory data** will be pulled into continued exploration rather than committing to a narrative

The pair must be aligned. The agent's cognitive mode determines *how* it processes. The data's cognitive stance determines *what space it has to process in*.

### How this shows up in the CA pipeline

The CA pipeline implicitly manages data stance at every boundary:

1. **L1 per-policy extraction** produces **descriptive data** (what each policy configures — observations, not findings)
2. **Story grouping** produces **classified data** (policies organised by intent — "these three policies form a guest access story")
3. **Framework assessment** produces **evaluated data** (maturity mapping against the NIST/Zero Trust framework)
4. **Investigation** receives descriptive + classified data, producing **exploratory data** (threads followed, patterns noticed, emergent connections)
5. **Synthesis** receives compressed exploratory data, producing **committed narrative** (the landscape model)

Crucially, the investigation agent (step 4) receives BOTH the raw per-policy extractions (descriptive) AND the story groupings (classified). This means it can follow threads the classifier didn't anticipate — it's not limited to the classification's lens. If only the classified data were passed, the investigation would be bounded by the classifier's categories. The raw data preserves access to lower-stance information alongside higher-stance summaries.

The traceability built into the system — where every claim traces back through the chain to source JSON — is a data stance mechanism. It means later agents can "pull on a thread" all the way back to descriptive data when the higher-stance summaries don't contain what they need.

### Connection to RAG and data processing

This theory extends naturally to how AI systems process, retrieve, and summarise data more broadly:

**Current RAG treats processing as cognitively neutral.** Chunking, embedding, retrieval, and generation happen in sequence, but nobody asks what cognitive stance each step imposes on the data. A summarisation step that asks the model to both describe (what's there) and compress (what matters) produces evaluated data — the summary carries the evaluator's judgments about importance. Every downstream step inherits those judgments.

**Evidence that this matters:**
- A 2025 study found LLMs overgeneralise in 26-73% of summaries, even when prompted for accuracy. This is mode contamination in data processing — the compression operation activates evaluative patterns that reshape descriptive content. Newer models were worse, not better. ([Royal Society Open Science, 2025](https://royalsocietypublishing.org/doi/10.1098/rsos.241776))
- Two-stage retrieval (retrieve broadly, then rerank for relevance) consistently outperforms single-stage retrieval. This is implicitly separating "find things" (descriptive stance) from "judge things" (evaluative stance). ([Pinecone rerankers guide](https://www.pinecone.io/learn/series/rag/rerankers/))
- Microsoft's GraphRAG separates entity extraction → community detection → per-community answers → final synthesis, producing "substantial improvements in comprehensiveness and diversity." Each stage operates in a different stance. ([Microsoft Research, 2024](https://arxiv.org/abs/2404.16130))
- The "lost in the middle" problem — where LLMs lose accuracy on information in the middle of long contexts — may be partly a data stance issue. As context grows, the model is simultaneously retrieving, evaluating, and preparing to generate. These stances interfere with each other, with the evaluative stance dominating and suppressing retrieval of information that doesn't match the emerging evaluation. ([Liu et al., 2024](https://arxiv.org/abs/2307.03172))

**What a cognitively informed data pipeline would look like:**

Instead of: chunk → embed → retrieve → generate (stances mixed within each step)

Separate by stance:
1. **Structural chunking** (descriptive) — break text into coherent units, no relevance assessment
2. **Descriptive indexing** (descriptive) — what is each chunk about? Entity extraction, topic labelling. No evaluation of importance
3. **Query decomposition** (investigative) — what are we looking for? Clean context, no source material yet
4. **Broad retrieval** (descriptive/mechanical) — cast wide net, no relevance filtering
5. **Relevance assessment** (evaluative) — now and only now, judge what matters. Clear criteria
6. **Synthesis** (integrative) — connect across retained chunks. Clean context
7. **Generation** (generative) — produce output from synthesis

The handoff between each stage strips cognitive stance — structured chunk metadata (not prose summaries) between chunking and indexing, ranked lists (not explanatory text) between retrieval and relevance, filtered chunks with structured annotations (not evaluative prose) between relevance and synthesis.

### What this predicts

If data stance matters:
- **Higher recall in retrieval** when investigation mode doesn't pre-filter (retrieval in descriptive stance, not evaluative)
- **More faithful summaries** when descriptive mode is maintained (describe what's here, don't assess what matters)
- **Better synthesis** when integrative mode operates on clean inputs (not pre-evaluated fragments)
- **The gap should be largest on complex, ambiguous datasets** where stance contamination has the most room to operate

### Open experiment: mode-controlled summarisation

The cleanest test of whether data stance affects downstream processing: give the same model the same data, but explicitly control the summarisation mode:
- **Descriptive-only**: "Report what is in this text. Do not assess importance or relevance."
- **Evaluative-only**: "What in this text is most important? Rank by significance."
- **Mixed** (typical): "Summarise this text."

Then use each summary as input to a downstream analytical task. If the descriptive summary produces different (and potentially richer) downstream analysis than the evaluative summary, data stance is a real variable — not just a reframing of "garbage in, garbage out" but a specific, predictable, controllable property of pipeline design.

This experiment doesn't require building a full RAG system. It can be run with any substantial text and any downstream analytical task. It tests the core mechanism: does the cognitive stance of data processing affect what downstream agents can discover?

### Relationship to the trust chain

Data stance is the trust chain operating at the information level rather than the agent level. The trust chain says: each agent's cognitive quality cascades to agents above and below it. Data stance says: each processing step's cognitive stance cascades to every step that receives its output. They're the same mechanism viewed from two angles — one looking at the agents, one looking at the data flowing between them.

The practical implication: when designing a pipeline, you need to think about both the agent's mode (how it processes) AND the data's stance (what it receives). A well-designed pipeline aligns these at every boundary.

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
- Whether creative work has a fundamentally different relationship with mode tension (the boundary test — A2 is testing this)
- Whether voice-continuity tasks require fundamentally different pipeline architectures than analytical tasks (A2 v2 testing 2-stage vs 4-stage)
- Whether the improvements we've seen in one domain (security policy analysis) generalise across domains
- Whether "more detail" alone (without mode separation) explains the same improvements
- Whether the cognitive stack model has predictive power beyond what simpler "focus your prompt" advice provides
- What the right intervention level is for different types of tasks (some may need only Tier 2, others need Tier 3)
- Whether the effects are model-dependent or hold across different LLMs
- Whether data stance is a real, controllable variable in pipeline design or just a reframing of existing data quality concerns
- Whether mode-controlled summarisation (descriptive-only vs evaluative-only vs mixed) produces measurably different downstream analysis
- Whether the "lost in the middle" problem is partly a data stance phenomenon (mode interference during long-context processing) rather than purely architectural

These are what the experiments are designed to answer.

---

## Evidence So Far

All evidence comes from one practitioner's project (the Conditional Access policy analysis pipeline). The strongest results:

- **V3 → V4 experiment**: Removing a QA section from a synthesis prompt (making it smaller) produced 12 findings instead of 8, four entirely new themes, zero losses, and a register shift from "competent audit" to "consultant who understands the room." The combined agent had 70% of its context window unused — this was not a capacity problem.

- **Seeds → lenses**: Removing numeric anchors and replacing specific issue lists with open analytical questions produced output that varied naturally with input complexity for the first time (2 findings for simple inputs, 7 for complex) and independently arrived at numbers matching expert review.

- **Agent split in knowledge-capture pipeline**: A combined evidence-gathering + investigation agent self-diagnosed that "ration = converge." Splitting into a convergent evidence-preparation step and a divergent investigation step produced deeper cross-thread connections that were impossible in the combined configuration.

- **"Observation" vs "finding"**: A single word change at the epistemic layer fundamentally changed the model's output register from catastrophising to exploratory.

These experiments need independent replication on third-party prompts across different domains. That's what this repo is for.
