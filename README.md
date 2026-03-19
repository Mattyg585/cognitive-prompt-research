\# Cognitive Prompt Research

**Good AI output hides great output. Cognitive science showed me why.**

Everyone knows the basics: keep contexts focused, split complex work into stages, use subagents. We know this works. But would you notice when it doesn't? In my experience, getting this wrong still produces good output — competent, thorough, professional. The gap only appears when you fix the interference and compare the output to what you had before. Good hides great.

I wanted to know *why* splitting helps when it helps, and whether I could predict when it would hurt. Cognitive science had answers. Human language carries cognitive patterns — exploratory writing looks statistically different from evaluative writing. LLMs learned those patterns from training data. When incompatible patterns share a context, they interfere. When you know *what's* interfering, you can predict whether splitting will help (because you're separating incompatible modes) or hurt (because you're scaffolding a model that already knows the domain).

I tested this across six domains, five models, and an external benchmark. On [PRBench](https://github.com/prbench/prbench) (rubrics from 182 domain experts), a cognitively restructured *single* prompt scored 0.95 versus 0.76 baseline — and the pipeline scored *lower* at 0.85. Splitting hurt. On five other domains, splitting produced qualitative leaps. The difference was predictable: cognitive science told me which was which before I ran anything.

**[The full story →](#the-full-story)** | **[Try the agents on your prompts →](QUICK-START.md)** | **[Full results →](findings.md)**

---

## Try it yourself

Point the analysis agent at any prompt and see what cognitive science finds wrong with it.

```
# Claude Code
Use the prompt-architect agent to analyse path/to/your/prompt.md
Use the prompt-writer agent to revise based on the analysis

# GitHub Copilot
@prompt-architect analyse path/to/your/prompt.md
@prompt-writer revise based on the analysis
```

Run both versions. Compare. **[Full walkthrough →](QUICK-START.md)**

---

## The litmus test

The most useful output of this research is a decision tool for when to use what.

**Could the model produce a correct analysis without seeing the specific input data?**

**If yes → use Tier 2 (prompt-level fixes).** The model already knows the domain. Fix the interference in the prompt — remove numeric anchors, replace seeded examples with analytical lenses, add scope boundaries between thinking modes — and get out of its way. The prompt-architect and prompt-writer agents do this automatically.

Example: "Analyse this contract for Fair Work Act compliance." The compliance framework is in the training data. The contract tells the model *where* to look, not *what* to look for.

**If no → consider Tier 3 (pipeline separation).** The answer lives in the input, not in the model's training. Split investigation, evaluation, and synthesis into separate agents with clean contexts and structured handoffs.

Example: "Review this SaaS vendor agreement against our procurement playbook." The compound risk — an ML training clause interacting with a survival clause and a data export restriction — only exists in *that* contract. The model has to discover it.

---

## What I found

Six experiments against production prompts from [Anthropic's knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) — legal, marketing, HR, design research, engineering, and SecOps. Three tiers: original prompt, cognitively optimised prompt, and a multi-agent pipeline with cognitive mode separation. Cross-model testing on Claude Opus 4.6, GPT-5.2, GPT-5.3-Codex, GPT-5.2-Codex, and Gemini 3 Pro.

**Tier 2 (prompt-level cognitive science fixes) helped across every model without a single failure.** That's the universally safe intervention.

**Pipeline won 5/6 analytical domains on Claude**, confirmed 6/6 on GPT-5.3-Codex. On other models, results were mixed — and on some, the pipeline produced output *worse than baseline* (wrong artifact types, introduced bias, missing critical findings). Pipeline is an amplifier, not a guarantee.

**On an external benchmark ([PRBench](https://github.com/prbench/prbench)) with rubrics from 182 domain experts**, the Tier 2 rewrite took a hard task from 0.76 to 0.95. The pipeline scored 0.85 — it *lost*. That failure, explained by seven converging cognitive science frameworks, produced the litmus test above and was arguably the most important result in the study.

**Creative writing is genuinely contested.** Pipeline wins on editorial craft and process. Optimised prompts win on voice and authenticity. The framework predicts this tension rather than resolving it.

Independent blind evaluators described the qualitative gap: pipeline output "treats the contract as a deal, not a document" and "would actually change how I make decisions" versus baseline output that was "template faithfully executed." Every baseline was competent. The gap only appeared in comparison. **[Full results →](findings.md)**

---

## Caveats

- **AI marked its own homework.** Experiments designed, run, and evaluated with heavy AI assistance. External validation (independent models, blind evaluation, external benchmark) partially controls for this. The qualitative differences in the outputs are what I actually trust — read them yourself.
- **Limited rigour.** Single runs for most experiments. No statistical power. One practitioner, no formal AI or cognitive science background. This is exploratory, not a paper.
- **Possible echo chamber.** A system built on cognitive science finding that cognitive science works. The PRBench failure partially addresses this — a self-confirming system wouldn't predict its own failures — but the concern is legitimate.

---

## What's in this repo

| What | Where |
|------|-------|
| Try the agents on your prompts | **[QUICK-START.md](QUICK-START.md)** |
| Full experiment results and cross-model analysis | [findings.md](findings.md) |
| The theoretical framework — cognitive stack, mode interference | [research-foundations.md](research-foundations.md) |
| Unresolved threads, open questions | [THINKING.md](THINKING.md) |
| Run the full experiment suite | [RUN-ALL.md](RUN-ALL.md) |
| Agent invocation across platforms | [USAGE.md](USAGE.md) |
| Full experiment data (prompts, outputs, evaluations) | [experiments/](experiments/) |
| Project history | [project-history.md](project-history.md) |

---

## The full story

This research grew out of a seven-month side project building an AI pipeline for Microsoft Conditional Access policy analysis. The key discovery — that separating different types of thinking into their own contexts produced deeper output, even with 70% of the context window empty — led to the question: does this generalise?

The full narrative, including the PRBench failure that nearly broke the thesis and the cognitive science frameworks that explained it, is in the blog series:

1. [I Built an AI Tool That Does My Job Better Than Me](https://thegrahams.au/blog/what-i-learned-building-ai-tools-that-actually-think/) — The project and what it produced
2. [Why Good Prompting Wasn't Enough](https://thegrahams.au/blog/why-good-prompting-wasnt-enough/) — Seven months of wrong turns
3. [Context Carries Cognitive Mode](https://thegrahams.au/blog/context-carries-cognitive-mode/) — The evidence for mode separation
4. [Evidence & Methods](https://thegrahams.au/blog/the-evidence-for-thinking-in-modes-evidence/) — Full experiment designs and claims tables
5. [What Does Cognitive Science Say About Prompt Engineering?](https://thegrahams.au/blog/testing-the-theory/) — Six experiments against production prompts (this research)

---

[MIT License](LICENSE)
