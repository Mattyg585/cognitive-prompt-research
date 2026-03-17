# Cognitive Prompt Research

**Language carries cognitive mode. Intervening at the right level changes everything.**

This repo documents an empirical discovery: that the language patterns in an AI prompt carry cognitive mode, and that deliberately managing those patterns improves output on complex tasks. The improvement is measurable on externally-scored benchmarks and consistent across models.

The research started with a single question — why does removing a QA section from a synthesis prompt produce *better* output? — and has evolved through eight months of experiments into something broader: a design methodology for AI systems that work on complex analytical tasks, grounded in cognitive science rather than engineering intuition.

**Two findings, different weights:**

1. **Cognitive hygiene works universally.** Setting the epistemic stance ("explore the landscape before reaching conclusions") in a single prompt improved professional reasoning output from 0.76 to 0.95 on expert-scored benchmarks (PRBench, 26 criteria, rubrics by 182 domain professionals). This works across all models tested. It's lightweight, zero-risk, and immediately applicable to any complex prompt.

2. **Pipeline separation works specifically.** Splitting prompts into cognitively scoped stages with structured handoffs produces qualitative leaps — but only when the task involves investigating external data the model hasn't seen before. On knowledge-based reasoning (however complex), the pipeline's information loss exceeds its mode-separation benefit. On data-intensive investigation tasks (the original CA policy pipeline), the pipeline is essential because it protects genuine discovery from evaluative pre-filtering.

---

## The Theory

LLMs are language models. Language is the only medium they process. And **language carries the cognitive mode of the person who produced it**.

Different types of human thinking produce different patterns of language. LLMs learned those patterns. The patterns in the context window influence what the model generates next. Mixing incompatible patterns creates distributional interference that degrades output. The output still looks fine — **good output hides great output** — and the gap only appears when you separate the modes and compare.

**I am not claiming LLMs have cognition.** The claim is about distributional interference in the statistical patterns the model learned from human writing.

### The cognitive stack

The key framework: language patterns are shaped by layers of human cognition, and **higher-layer interventions cascade further**.

```
Epistemic stance  →  Intent  →  Expertise  →  Cognitive mode  →  Register  →  Language patterns  →  Tokens
```

Changing a single word at the epistemic level ("observation" vs "finding") cascades through mode, register, and language patterns to produce fundamentally different output. This is why the Tier 2 intervention works so well — setting "explore the landscape before reaching conclusions" intervenes at the top of the stack and everything below follows.

### Two weights of intervention

**Tier 2 (cognitive hygiene):** Set the epistemic stance. Add scope boundaries. Replace seeds with lenses. One prompt, no architectural change. Works universally on complex analytical tasks. The lightweight tool.

**Tier 3 (pipeline separation):** Split into cognitively scoped stages with structured handoffs. Each stage gets its own clean context and explicit epistemic stance. The handoff schema strips cognitive residue — information crosses the boundary, but the thinking style that produced it does not. The heavyweight tool — powerful when the conditions are right, overcooked when they're not.

---

## The Experiments

### A-Series: Knowledge-work prompts (6 domains)

Tested Anthropic's [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) across legal, marketing, HR, design research, engineering, and security operations.

**On Claude (Opus 4.6):** Pipeline won 5/6. Creative writing (A2) was the boundary — pipeline improves process but disrupts prose.

**Cross-model (Copilot CLI):** GPT-5.3-Codex mirrored Claude (6/6). GPT-5.2 favoured Tier 2. GPT-5.2-Codex and Gemini 3 Pro had catastrophic pipeline failures. **Tier 2 was the universally safe improvement across all models.** See [findings.md](findings.md).

### B-Series: External benchmarks

**B1 (SWE-bench):** Dropped. Baseline passed all coding tasks. Convergent work is resilient to mode contamination.

**B2 (PRBench):** Tested on expert-scored professional reasoning (rubrics by 182 domain professionals, not created by us):

| Tier | Score | Criteria Met |
|------|-------|-------------|
| Baseline | 0.759 | 20/26 |
| Pipeline (Tier 3) | 0.849 | 22/26 |
| **Optimised (Tier 2)** | **0.950** | **25/26** |

Tier 2 beat the pipeline. The epistemic stance intervention in a single prompt captured nearly all the improvement. The pipeline lost procedural details in its structured handoffs. See [experiments/B2-prbench/FINDINGS.md](experiments/B2-prbench/FINDINGS.md).

### What the A-series improvements look like

On models that handle the pipeline well, it produces **qualitatively different documents**:

**Legal (A1)**: Baseline lists clause deviations. Pipeline identifies compound clause interactions, scripts negotiation moves, predicts what counterparty responses reveal. Independent evaluators: *"treats the contract as a deal, not a document."*

**Design Research (A4)**: Baseline catalogues themes. Pipeline surfaces compound insights — *"workarounds are specifications written in behaviour."* Evaluators: *"would actually change how I make decisions"* vs *"template faithfully executed."*

**SecOps (A6)**: Baseline produces a standard postmortem. Pipeline reframes: *"confidence accumulates across checkpoints without coverage expanding."* Organisational learning vs compliance document.

---

## When to Use What

The framework forming through trial and error:

**Always use Tier 2 (cognitive hygiene).** Set the epistemic stance. Add scope boundaries. Replace seeds with lenses. This works on every complex task, every model, with zero risk. It's a system prompt — not a redesign.

**Consider Tier 3 (pipeline) when:**
- The model must investigate **external data it hasn't seen before** (not reason from training knowledge)
- Data volume exceeds what one context can hold
- The investigation + evaluation toxic pair operates on **discovered** information
- The pipeline runs repeatedly, amortizing design cost
- The task requires what we're calling "adaptive expertise" — building novel understanding from unfamiliar data

**Don't use Tier 3 when:**
- The task is knowledge-based reasoning (however complex) — Tier 2 is sufficient and better
- The question is answerable in one thorough pass
- Procedural details matter and might not map to handoff schema fields

**Boundary conditions:**
- Creative writing — pipeline improves process, Tier 2 preserves prose register
- Convergent work (coding, domain accuracy) — unaffected by any intervention
- Model-dependent — pipeline requires models capable of reconstructing intent across structured handoffs

### The open question

There's something we're still circling. The pipeline's strongest results (the original CA policy pipeline, the A-series qualitative leaps) involved what we're calling "adaptive expertise" — the ability to investigate unfamiliar data, discover patterns nobody predicted, and build novel understanding. This is the work of a consultant who walks into a new environment and sees things the people inside can't see. It's different from answering a hard question from knowledge (which is what PRBench tests, and where Tier 2 is sufficient).

We think this is the high-value niche — and we think nobody in AI is specifically benchmarking or optimizing for it. But we haven't fully defined the boundary yet. See [experiments/B2-prbench/FINDINGS.md](experiments/B2-prbench/FINDINGS.md) for more on what we know and don't know.

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

- **Tier 2 is the safe bet. Pipeline is not.** Cross-model testing showed pipeline producing catastrophic failures on some models. B2 showed pipeline underperforming Tier 2 on knowledge-based reasoning. The pipeline is a powerful tool for specific conditions, not a universal upgrade.
- **B2 used Claude judging Claude.** PRBench validated with o4-mini. We used Sonnet. Binary per-criterion scoring against specific expert-written criteria reduces subjectivity, but self-preference risk exists. The rubrics themselves are external (182 domain experts).
- **Single runs.** A1/A2 had 3 runs per tier. Everything else had 1. These are directional findings, not statistically powered studies.
- **Pipeline cost.** 4-12x more tokens than a single prompt. Only justified when the quality improvement justifies the cost — and B2 showed that for knowledge-based reasoning, it doesn't.
- **Single researcher.** Side project, not funded research. There are likely flaws.
- **The pipeline was v0.1.** The B2 pipeline's handoff schemas were not iterated. Better schema design might reduce information loss. But that iteration cost is itself part of the argument for Tier 2's practicality.

What would strengthen this: independent replication, domain expert evaluation, testing Tier 2 across the full PRBench benchmark, and someone who can articulate the adaptive expertise boundary more precisely than we currently can.

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
