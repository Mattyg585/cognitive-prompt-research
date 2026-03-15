# Cognitive Prompt Research

**What if the monolithic prompt is the ceiling, not the floor?**

This repo tests a theory: that mixing incompatible types of thinking in the same AI context window degrades output — and that splitting prompts into cognitively scoped pipelines produces measurably better results.

I tested this against [Anthropic's knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) across six domains: legal, marketing, HR, design research, engineering, and security operations. The pipeline produced qualitatively different output in 5 of 6 domains. The exception — creative writing — turned out to be the most interesting finding.

---

## The Core Bet

LLMs are language models. Language is the only medium they process. And **language carries the cognitive mode of the person who produced it**.

When a human writes in exploratory mode, the text has different statistical properties than when they write in evaluative mode — different sentence structures, hedging patterns, transition words, levels of commitment. An LLM trained on billions of words has learned these distributions.

**I am not claiming LLMs have cognition.** The claim is that:

1. Different types of human thinking produce different patterns of language
2. LLMs learned those patterns from training data
3. The patterns in the context window influence what the model generates next
4. Mixing incompatible patterns (from incompatible cognitive modes) creates distributional interference that degrades output

When you put a quality-checking section (evaluative, criteria-referencing language) in the same context as a synthesis task (exploratory, thread-following language), you're not creating "cognitive interference" in the model's mind. You're creating **distributional interference** — the statistical patterns of evaluative language pull the generation away from the patterns associated with exploratory synthesis. The model does what it always does: predicts what comes next given what came before. And what came before is now carrying evaluative framing.

The output still looks fine. It's competent, thorough, professional. **Good output hides great output.** The gap only appears when you separate the modes and compare.

### Why this matters

The entire industry trend is toward bigger, more comprehensive single prompts. Skills, plugins, progressive loading — these are mechanisms to make prompts effectively longer without hitting token limits. The assumption is: more context = better output.

The hypothesis: **for complex tasks, that assumption may be backwards.**

More context means more cognitive mode mixing. More instructions means more distributional interference between incompatible types of thinking. Skills loaded on demand don't just add capabilities — they contaminate the context with whatever language patterns they carry. And the contamination is invisible because the output is still... fine.

---

## The Experiment

I took production prompts from Anthropic's knowledge-work-plugins and tested three tiers of intervention:

1. **Baseline** — the original prompt, unchanged
2. **Optimised** — same structure, better cognitive hygiene (remove numeric anchors, replace content prescription with analytical lenses, add scope boundaries between thinking modes)
3. **Pipeline** — split into multiple agents, each doing one type of thinking in a clean context, with structured handoffs that strip cognitive residue between stages

### Results

| Experiment | Domain | Baseline | Optimised | Pipeline | External Validation |
|---|---|---|---|---|---|
| A1 | Legal contract review | 3rd | 2nd | **1st** | Claude + Gemini: unanimous |
| A2 | Marketing content | 3rd | **1st/2nd** | **1st/2nd** | Split — creative boundary condition |
| A3 | HR performance review | 3rd | 2nd | **1st** | Internal |
| A4 | Design research synthesis | 3rd | 2nd | **1st** | Claude + Gemini: unanimous |
| A5 | Engineering debug | 3rd | 2nd | **1st** | Internal |
| A6 | SecOps incident response | 3rd | 2nd | **1st** | Internal |

**Pipeline won in 5 of 6 experiments.** The exception was creative writing (A2), where evaluators split between Pipeline and Optimised — a genuine boundary condition where prompt-level fixes may capture most of the improvement.

### What the improvements look like

These aren't marginal score differences. The pipeline produces **qualitatively different documents**:

**Legal (A1)**: The baseline review lists clause deviations. The pipeline version identifies compound interactions between clauses (ML training + survival + no data export = a single structural risk), scripts the negotiation move-by-move, and predicts what the counterparty's responses will reveal about their organisation. Two independent models with zero project context both called it: *"treats the contract as a deal, not a document."*

**Design Research (A4)**: The baseline catalogues interview themes. The pipeline version surfaces compound insights no single interview contains — *"workarounds are specifications written in behaviour"* and *"partial adoption produces negative value, not partial value."* Both evaluators: *"would actually change how I make decisions"* vs *"template faithfully executed."*

**SecOps (A6)**: The baseline produces a standard postmortem with a mechanical 5 Whys analysis. The pipeline version reframes: *"confidence accumulates across checkpoints without coverage expanding"* and *"multiple overlapping checks can produce less safety than one well-scoped check."* Organisational learning vs compliance document.

### Validation approach

For A1, A2, and A4, I ran blind evaluations with Claude (web, no project context) and Google Gemini. The evaluators received randomised IDs — they didn't know which output came from which tier. They invented their own vocabulary for what they saw. The rankings converged independently.

---

## The Boundary Condition

Creative writing (A2) is where the pattern changes. Claude Web ranked the optimised version first; Gemini ranked the pipeline first; the human author preferred the optimised version. The pipeline produces better *process* (editorial reasoning, SEO strategy) but the optimised version produces better *prose* (voice, rhythm, naturalness).

For a blog post, prose wins. For a legal brief, process wins.

This maps to where the improvement lives in the **cognitive stack**:

```
Epistemic stance  →  Intent  →  Expertise  →  Cognitive mode  →  Register  →  Language patterns  →  Tokens
```

Pipeline separation operates at the cognitive mode layer. Creative writing quality lives at the register layer. For analytical work, freeing the cognitive mode cascades down and improves everything. For creative work, the pipeline's structured handoffs may disrupt the register-level flow. The right intervention for creative work may be Tier 2 (fix the register) rather than Tier 3 (separate the modes).

---

## What's Here

```
├── research-foundations.md     # Full theoretical framework
├── experiment-design.md        # Protocol and methodology
├── findings.md                 # Cross-experiment patterns and caveats
├── toolkit/                    # Analysis and writing agents
├── evaluation/                 # Rubric and blind evaluator prompt
├── experiments/A1-A6/          # Full experiment data (prompts, outputs, evaluations)
└── reference/                  # Original project context (blogs, V3/V4 comparison)
```

### Evaluate your own prompts

**[QUICK-START.md](QUICK-START.md)** — point the architect at your prompt and see what it finds. Three steps: analyse, fix, compare.

```
Use the prompt-architect agent to analyse [your prompt file]
```

It identifies mode interference patterns and recommends both prompt-level fixes and pipeline reconstruction. Works with single prompts, agents with skills, and multi-agent pipelines.

### Replicate the experiments

See [USAGE.md](USAGE.md) for agent invocation details and [RUN-ALL.md](RUN-ALL.md) for the full experiment protocol across all six domains.

---

## Caveats

This is early-stage research from one practitioner. Hold it lightly.

- **Six experiments, one model.** All outputs generated by Claude. Cross-model testing (GPT-5, Gemini) is planned.
- **LLM-as-judge bias.** The evaluators may prefer longer, more structured output. The external blind evaluations partially control for this, but domain expert evaluation would be stronger.
- **Single runs for A3-A6.** A1 and A2 had 3 runs per tier. A3-A6 had 1. The consistency of the pattern partially compensates, but individual results should be held carefully.
- **Pipeline cost.** A pipeline uses 4-12x more tokens than a single prompt. For a legal brief where the pipeline catches compound clause interactions your lawyer missed, the trade-off isn't close. For a quick internal summary, a single prompt is fine. The right answer depends on what the output is worth.
- **The A2 creative boundary.** One experiment doesn't define a boundary condition. More creative domain testing is needed.

What would strengthen this: independent replication, domain expert evaluation, cross-model testing, and more creative domain experiments.

---

## Background

This research grew out of a side project — seven months of building an AI pipeline for Microsoft Conditional Access policy analysis. The full story is in the blog series:

1. [I Built an AI Tool That Does My Job Better Than Me](https://thegrahams.au/blog/what-i-learned-building-ai-tools-that-actually-think/) — The project and what it produced
2. [Why Good Prompting Wasn't Enough](https://thegrahams.au/blog/why-good-prompting-wasnt-enough/) — Seven months of wrong turns and the architecture that fell out
3. [Context Carries Cognitive Mode](https://thegrahams.au/blog/context-carries-cognitive-mode/) — The evidence for mode separation
4. [Evidence & Methods](https://thegrahams.au/blog/the-evidence-for-thinking-in-modes-evidence/) — Full experiment designs and claims tables

The key experiment from the original project: removing a quality-checking section from a synthesis prompt — making it *smaller* — produced deeper output with zero losses. Same model, same data, 70% of the context window unused. Not a capacity problem. A contamination problem.

---

## License

[MIT](LICENSE) — do whatever you want with this.

---

*Built by [Matt Graham](https://www.linkedin.com/in/matthewgrahamau/), a cloud consultant with no formal AI research background who got curious about why his prompts were producing good output instead of great output. Research conducted with Claude Code (Opus 4.6). External validation by Claude Web and Google Gemini.*
