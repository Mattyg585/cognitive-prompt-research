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

### Results — Claude (Opus 4.6)

| Experiment | Domain | Baseline | Optimised | Pipeline | External Validation |
|---|---|---|---|---|---|
| A1 | Legal contract review | 3rd | 2nd | **1st** | Claude + Gemini: unanimous |
| A2 | Marketing content | 3rd | **1st/2nd** | **1st/2nd** | Split — creative boundary condition |
| A3 | HR performance review | 3rd | 2nd | **1st** | Internal |
| A4 | Design research synthesis | 3rd | 2nd | **1st** | Claude + Gemini: unanimous |
| A5 | Engineering debug | 3rd | 2nd | **1st** | Internal |
| A6 | SecOps incident response | 3rd | 2nd | **1st** | Internal |

Pipeline won 5 of 6 on Claude, with the creative writing boundary condition (A2) as the exception.

### Cross-model testing — the picture gets more interesting

The same experiments were re-run across four additional models via GitHub Copilot CLI:

| Model | Pipeline Wins | Pipeline Fails | Key Finding |
|---|---|---|---|
| GPT-5.3-Codex | **6/6** | 0 | Mirrors Claude — pipeline consistently best |
| GPT-5.2 | 2/6 | 0 | Optimised was the safe bet |
| GPT-5.2-Codex | 2/6 | **3 catastrophic** | Pipeline produced wrong artifact types |
| Gemini 3 Pro | 2/6 | 2 serious | Pipeline introduced bias and missed critical findings |

**Pipeline is an amplifier, not a guarantee.** On models that handle it well, the qualitative leaps are real. On models that don't, it produces output *worse than the baseline* — wrong artifact types, introduced gender bias, missing critical compliance findings. The pipeline doesn't add quality. It creates the conditions for quality. Whether the model fills those conditions depends on the model.

**Tier 2 (prompt-level optimisation) is the universally safe improvement.** It helped across every model tested without risk of catastrophic failure.

The pipeline failures are themselves evidence for the theory: the trust chain predicted that a break at one stage would cascade through the pipeline. That's exactly what happened — and predicting how something fails is harder to fake than claiming it works. See [findings.md](findings.md) for the full cross-model analysis.

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

This is early-stage research from one practitioner, built in stolen evenings and weekends. Hold it lightly.

- **Pipeline is fragile.** Cross-model testing showed pipeline producing catastrophic failures (wrong artifact types, introduced bias) on some models. The pipeline design was created by Claude, for Claude, and was not tuned for other models. Tier 2 optimisation is the universally safe intervention.
- **Process, not polish.** The pipeline stages, handoff specs, and automation were thrown together quickly. The cross-model failures likely reflect implementation fragility as much as fundamental limits. Someone spending more time on the handoff design would likely get better results.
- **LLM-as-judge bias.** The evaluators may prefer longer, more structured output. External blind evaluations (A1, A2, A4) partially control for this, but domain expert evaluation would be stronger.
- **Single runs for A3-A6.** A1 and A2 had 3 runs per tier. A3-A6 had 1. The consistency across experiments partially compensates, but individual results should be held carefully.
- **Pipeline cost.** A pipeline uses 4-12x more tokens than a single prompt. For a legal brief where the pipeline catches compound clause interactions your lawyer missed, the trade-off isn't close. For a quick internal summary, a single prompt is fine.
- **Single researcher.** All design, execution, and evaluation orchestrated by one person. This is a side project, not a funded research programme. There are likely flaws in places that can be tightened up.

What would strengthen this: independent replication, domain expert evaluation, model-specific pipeline tuning, and someone with more time than weekends.

---

## Background

This research grew out of a side project — seven months of building an AI pipeline for Microsoft Conditional Access policy analysis. The full story is in the blog series:

1. [I Built an AI Tool That Does My Job Better Than Me](https://thegrahams.au/blog/what-i-learned-building-ai-tools-that-actually-think/) — The project and what it produced
2. [Why Good Prompting Wasn't Enough](https://thegrahams.au/blog/why-good-prompting-wasnt-enough/) — Seven months of wrong turns and the architecture that fell out
3. [Context Carries Cognitive Mode](https://thegrahams.au/blog/context-carries-cognitive-mode/) — The evidence for mode separation
4. [Evidence & Methods](https://thegrahams.au/blog/the-evidence-for-thinking-in-modes-evidence/) — Full experiment designs and claims tables
5. [Testing the Theory](https://thegrahams.au/blog/testing-the-theory/) — Six experiments against production prompts (this research)

The key experiment from the original project: removing a quality-checking section from a synthesis prompt — making it *smaller* — produced deeper output with zero losses. Same model, same data, 70% of the context window unused. Not a capacity problem. A contamination problem.

---

## License

[MIT](LICENSE) — do whatever you want with this.

---

*Built by [Matt Graham](https://www.linkedin.com/in/matthewgrahamau/), a cloud consultant with no formal AI research background who got curious about why his prompts were producing good output instead of great output. Research conducted with Claude Code (Opus 4.6). External validation by Claude Web and Google Gemini.*
