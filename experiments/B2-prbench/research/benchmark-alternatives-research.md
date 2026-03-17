# Benchmark Alternatives Research for B2 Experiment

## What We Need

A knowledge-work benchmark where **the prompt/scaffold is the variable, not the model**. Specifically:

1. **Has real, engineered scaffold/system prompts** that people have iterated on
2. **Prompt engineering matters** — different prompts produce meaningfully different scores
3. **Objective or expert-rubric scoring** — not just vibes
4. **Tests knowledge work** — reasoning, analysis, synthesis, judgment (not code)
5. **Publicly available** — we can access the dataset and prompts

The SWE-bench model is our gold standard: teams (Anthropic, OpenAI, Augment) have built competing scaffolds, and changing the scaffold changes scores dramatically — even with the same model.

---

## Why PRBench Is Actually a Strong Fit (Reassessment)

Before looking at alternatives, it is worth reassessing PRBench against our actual criteria. PRBench was initially "ruled out" because it has no scaffold prompts — but that may be a feature, not a bug.

**What PRBench has:**
- Expert-curated rubrics with weighted criteria across 11 dimensions
- LLM-judge scoring (o4-mini) with 80.2% agreement with human experts
- 1,100 tasks in law and finance — real professional reasoning
- Top models score only 37-39% on Hard — massive headroom
- Support for prefilled responses (`final_response_source: prefilled`)
- The benchmark itself documents our phenomenon: "models frequently reach correct conclusions through incomplete or opaque reasoning"

**What PRBench lacks:**
- No scaffold prompts from different teams to compare against
- No leaderboard of different prompt strategies

**Why this might not matter for our experiment:**
Our B2 experiment does not need existing scaffolds to compare against. We are building our own three tiers (baseline zero-shot, optimised, pipeline). PRBench gives us the rubric and scoring infrastructure. The "prompt is the variable" because *we* are the ones varying the prompt. We just need a benchmark where the rubric can detect the difference our prompt changes make — and PRBench's 11-dimension rubric is purpose-built for exactly that.

**Verdict: PRBench remains the best fit for B2.** The alternatives below are researched for completeness and for potential future experiments.

---

## Tier 1: Strong Candidates (Prompt Engineering Is the Variable)

### 1. Tau-bench (Sierra Research)

**What it is:** A benchmark emulating dynamic customer-service conversations between a simulated user and an agent. The agent receives domain-specific policy documents and API tools. Two domains: airline and retail (tau2-bench adds telecom).

**Why it is interesting for us:**
- **Prompt engineering dramatically changes scores.** Anthropic's "think" tool study showed a 54% relative improvement on the airline domain (pass^1: 0.370 baseline to 0.584 with optimised prompt) using the same model (Claude 3.7 Sonnet). The improvement came entirely from prompt changes — adding structured reasoning examples to the policy prompt.
- **The agent receives a system prompt + policy document** that can be modified. The policy is a substantial natural-language document covering rules, procedures, and edge cases.
- **Multiple scaffold strategies** are supported: tool-calling, Act, ReAct, verification, reflection.
- **Objective scoring:** Compares database state at end of conversation with annotated goal state (pass/fail per task, reported as pass@k).

**Limitations for our research:**
- **Not knowledge work in our sense.** Tasks are procedural customer service (cancel a flight, process a refund) rather than analytical reasoning, synthesis, or professional judgment. The cognitive modes involved are primarily procedural compliance + information retrieval, not the investigation + analysis + synthesis pattern we want to test.
- **Binary scoring.** Pass/fail does not capture reasoning quality — only whether the right database state was achieved. Our theory predicts improvements in reasoning quality that binary scoring would miss.
- **Tool-use heavy.** Success depends heavily on correct API calls, not reasoning quality.

**Access:** Fully open source. [GitHub](https://github.com/sierra-research/tau-bench), [Paper](https://arxiv.org/abs/2406.12045)

**Fit score: 6/10.** Strong evidence that prompts matter, but wrong type of knowledge work and wrong granularity of scoring for our theory.

---

### 2. GAIA (Meta, HuggingFace)

**What it is:** 466 real-world questions requiring reasoning, web browsing, multi-modality handling, and tool use. Questions have unambiguous short answers. Three difficulty levels.

**Why it is interesting for us:**
- **Scaffold architecture matters enormously.** Scores range from ~7% (GPT-4 Turbo with basic scaffold) to 75% (h2oGPTe Agent) — a 10x range driven primarily by scaffold/prompt engineering, not model capability alone.
- **Leaderboard with many competing agent architectures.** Different teams submit agents with different scaffolds, making it a natural scaffold-comparison venue.
- **Inspect AI integration** with a swappable `solver` parameter — you can plug in different agent architectures and directly measure their impact.
- **Custom `input_prompt` parameter** allows modifying the question prompt template.

**Limitations for our research:**
- **Tool-use and web-browsing heavy.** Most tasks require the agent to search the web, parse files, or execute code. The "reasoning" is in service of information retrieval, not professional judgment.
- **Short-answer scoring** (exact match or close match). This measures whether you found the right answer, not the quality of reasoning, analysis, or synthesis.
- **Not domain-expert knowledge work.** Questions are "general assistant" tasks (find a fact, calculate something, answer a trivia question requiring research), not professional reasoning in law, finance, or medicine.
- **The scaffold matters, but mostly for tool orchestration** — how well the agent plans its web searches, handles errors, manages multi-step retrieval. This is engineering, not cognitive mode management.

**Access:** Dataset on HuggingFace (requires access request). Leaderboard at [huggingface.co/spaces/gaia-benchmark/leaderboard](https://huggingface.co/spaces/gaia-benchmark/leaderboard). Inspect evals implementation available.

**Fit score: 5/10.** Strong proof that scaffolds matter, but the tasks test tool orchestration rather than knowledge-work reasoning.

---

### 3. HAL — Holistic Agent Leaderboard (Princeton)

**What it is:** A meta-leaderboard tracking 9 benchmarks (AssistantBench, CORE-Bench, GAIA, Mind2Web, SciCode, ScienceAgentBench, SWE-bench, TAU-bench, USACO) with explicit scaffold comparison. Validated through 21,730 agent rollouts.

**Why it is interesting for us:**
- **Explicitly designed to compare scaffolds.** HAL's three-dimensional analysis (model x scaffold x benchmark) directly addresses our question: does the scaffold matter independently of the model?
- **Dramatic scaffold effects documented.** On CORE-Bench Hard, Claude Code scaffold achieves 77.8% vs CORE-Agent scaffold at 51.1% — same model, different scaffold.
- **Surprising finding:** Higher reasoning effort *reduced* accuracy in 21 of 36 runs — directly relevant to our mode-interference thesis.
- **Open-source harness** at [github.com/princeton-pli/hal-harness](https://github.com/princeton-pli/hal-harness).

**Limitations for our research:**
- **Not a benchmark itself** — it is a harness for running other benchmarks. We would still need to pick which benchmark(s) to run through it.
- **Most tracked benchmarks are code/tool-use** (SWE-bench, SciCode, WebArena). The knowledge-work benchmarks it includes (TAU-bench, GAIA) have the limitations noted above.
- **Infrastructure is complex** — orchestrates parallel evaluations across hundreds of VMs.

**Access:** Open source. [Website](https://hal.cs.princeton.edu/), [Paper](https://arxiv.org/abs/2510.11977), [GitHub](https://github.com/princeton-pli/hal-harness)

**Fit score: 4/10 as a benchmark, 8/10 as evidence.** HAL proves that scaffolds matter enormously, but it does not provide a knowledge-work benchmark we can use directly. Its finding that higher reasoning effort reduces accuracy is strong supporting evidence for our mode-interference thesis.

---

## Tier 2: Partial Fits (Knowledge Work but Prompt Is Not the Primary Variable)

### 4. LegalBench (Stanford/Hazy Research)

**What it is:** 162 legal reasoning tasks covering six types of legal reasoning (issue-spotting, rule-recall, rule-application, rule-conclusion, interpretation, rhetorical understanding). Collaboratively built by 40 legal professionals.

**Why it is interesting for us:**
- **Real legal reasoning tasks** — exactly the domain-expert knowledge work we want.
- **Prompt templates are provided and swappable** — each task has a template stored as a text file with placeholders. Users can contribute new templates via pull request.
- **Prompt sensitivity documented:** Plain language prompts outperform technical language prompts. Models show high sensitivity to choice of in-context examples. Prompt changes produced 11.3% improvements in sensitivity scores.
- **Automated scoring** for most tasks (balanced accuracy, F1). About 7 tasks require manual evaluation.
- **Few-shot design** — training splits have <10 examples, designed as few-shot demonstrations for prompts.
- **Integrated with HELM** for standardised evaluation.

**Limitations for our research:**
- **Tasks are mostly classification/short-answer**, not extended professional reasoning. "Does this clause violate X?" (yes/no) rather than "Analyse this contract for risks and recommend next steps" (the kind of task PRBench tests).
- **No scaffold prompts from competing teams.** The prompt templates are for task presentation, not agent scaffolding.
- **Evaluates model capability more than prompt engineering.** While prompt sensitivity exists, the benchmark was designed to compare models, not prompts.
- **Limited cognitive complexity per task.** Each task tests one type of legal reasoning. Our theory predicts the biggest gains when multiple cognitive modes must be combined — which these single-type tasks do not require.

**Access:** Fully open source. [GitHub](https://github.com/HazyResearch/legalbench), [Website](https://hazyresearch.stanford.edu/legalbench/), [HuggingFace](https://huggingface.co/datasets/nguha/legalbench)

**Fit score: 5/10.** Right domain, wrong task complexity. Good for testing specific legal reasoning types but not for testing mode separation in complex professional reasoning.

---

### 5. PromptBench (Microsoft)

**What it is:** A unified library for evaluating LLMs that specifically tests different prompting strategies (CoT, zero-shot CoT, expert prompting, emotion prompting, generated knowledge, least-to-most) across multiple datasets (GLUE, MMLU, BigBench Hard, Math, GSM8K, SQuAD, etc.).

**Why it is interesting for us:**
- **Prompt engineering is explicitly the variable.** The benchmark is designed to compare prompting strategies, not just models.
- **Leaderboard showing prompt strategy x model x dataset scores.** This is exactly the structure we want.
- **Supports custom prompt modules** — you can add new prompting strategies and measure their impact.
- **Covers reasoning tasks** (GSM8K, Math, BigBench Hard) that require multi-step reasoning.

**Limitations for our research:**
- **Prompting strategies are generic techniques** (CoT, few-shot) rather than domain-specific scaffold prompts. Our theory is about cognitive mode separation, not generic prompting tricks.
- **Tasks are mostly multiple-choice or short-answer.** No extended professional reasoning, no rubric-based quality assessment.
- **No agent scaffolding.** These are single-turn prompt-in/answer-out evaluations, not multi-stage pipelines.
- **The prompting strategies tested are well-known techniques** — there is no equivalent to SWE-bench's competing scaffold architectures where teams have deeply engineered their approaches.

**Access:** Fully open source. [GitHub](https://github.com/microsoft/promptbench), [Paper](https://arxiv.org/abs/2312.07910)

**Fit score: 4/10.** Right philosophy (prompt as variable) but wrong task type and wrong granularity. Tests generic prompting techniques on simple tasks rather than scaffold engineering on complex knowledge work.

---

### 6. HELM (Stanford CRFM)

**What it is:** A comprehensive evaluation framework testing models across 16 scenarios and 7 dimensions (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency). Modular prompt system with scenario-specific templates.

**Why it is interesting for us:**
- **Modular prompt templates** — scenarios use official prompt templates from papers, and these can be swapped.
- **Full prompt-level transparency** — all prompts are documented and reproducible.
- **DSPy+HELM framework** exists for structured prompting evaluation across frontier models.
- **Extensible** — designed for adding new scenarios, models, metrics, and prompting strategies.
- **Enterprise extensions** (IBM HELM) cover finance, legal, climate, cybersecurity domains.

**Limitations for our research:**
- **Primarily a model comparison framework**, not a prompt comparison framework. Prompts are standardised to enable fair model comparison — the opposite of what we want.
- **Knowledge-work scenarios are limited.** Most scenarios test NLP capabilities (classification, summarisation, QA) rather than professional reasoning.
- **No scaffold/agent architecture.** Single-turn evaluations with prompt templates, not multi-stage pipelines.
- **Complexity of the framework** — very heavyweight for our focused experiment.

**Access:** Fully open source. [GitHub](https://github.com/stanford-crfm/helm), [Website](https://crfm.stanford.edu/helm/), [Docs](https://crfm-helm.readthedocs.io/)

**Fit score: 3/10.** Good infrastructure but wrong purpose. Designed for model comparison with standardised prompts, not for testing prompt engineering impact.

---

### 7. FinBen (Financial Benchmark)

**What it is:** 35 datasets across 23 financial tasks organised into three difficulty spectrums (foundational, complex, general intelligence). Covers extraction, quantification, reasoning, generation, forecasting, and stock trading.

**Why it is interesting for us:**
- **Domain-expert financial reasoning** — right knowledge-work domain.
- **Three difficulty levels** based on cognitive complexity (inspired by Cattell-Horn-Carroll theory).
- **Expert-designed prompts** — domain experts designed diverse prompts and reformulated datasets into instruction-response pairs.

**Limitations for our research:**
- **Designed for zero-shot model evaluation**, not prompt comparison.
- **No scaffold prompts or competing prompt architectures.**
- **Tasks are individual benchmarks** (sentiment analysis, NER, question answering) rather than complex professional reasoning scenarios.
- **No rubric-based scoring** — standard NLP metrics (accuracy, F1, etc.).

**Access:** Open source. [Paper](https://arxiv.org/abs/2402.12659), [HuggingFace](https://huggingface.co/papers/2402.12659)

**Fit score: 3/10.** Right domain but wrong evaluation structure for our needs.

---

## Tier 3: Poor Fits (Ruled Out)

### 8. MMLU-Pro

**Why ruled out:** Explicitly designed to be *robust* to prompt variations. Prompt changes only affect scores by ~2% (vs 4-5% for MMLU). The benchmark's entire value proposition is that results reflect model capability, not prompt phrasing. This is the opposite of what we need.

### 9. BigBench / BigBench Hard

**Why ruled out:** Collection of 200+ diverse tasks, mostly short-answer or classification. No scaffold prompts, no agent architecture. Tasks test specific capabilities in isolation rather than complex multi-mode reasoning. CoT prompting helps on BigBench Hard, but this is well-documented generic technique, not the scaffold engineering we want to test.

### 10. MedQA

**Why ruled out:** Multiple-choice medical exam questions. Prompt engineering matters (OpenMedLM shows prompt engineering can outperform fine-tuning), but scoring is binary (right/wrong answer choice). No rubric-based quality assessment. Tasks require medical knowledge recall more than multi-mode professional reasoning.

### 11. GPQA (Graduate-Level Q&A)

**Why ruled out:** 448 multiple-choice questions in biology, physics, chemistry. Very difficult (experts get 65%), but still multiple-choice format. Tests domain knowledge retrieval with reasoning, not professional judgment/synthesis. Prompt strategies are tested (zero-shot, few-shot, CoT) but these are generic techniques.

### 12. WebArena

**Why ruled out:** Web browsing tasks (e-commerce, forums, content management). Tests tool use and web navigation, not knowledge-work reasoning. Scaffold architecture matters (planner/executor/memory pattern) but for web automation, not professional analysis.

### 13. WorkArena (ServiceNow)

**Why ruled out:** Knowledge worker tasks on ServiceNow platform, but tasks are enterprise UI navigation and data entry, not professional reasoning. Tests web-agent capability more than cognitive work.

### 14. BrowseComp (OpenAI)

**Why ruled out:** 1,266 web-browsing challenges. Tests ability to find hard-to-locate information online. Pure information retrieval, not analysis or synthesis. Deep Research dramatically outperforms other approaches, but the skill being tested is search strategy, not reasoning quality.

### 15. LiveBench

**Why ruled out:** Contamination-resistant benchmark with monthly updates. Tests math, coding, reasoning, data analysis, language, instruction following. Good for model comparison but uses standardised prompts (zero-shot CoT) specifically to ensure fair model comparison. No scaffold/prompt engineering component.

### 16. IFEval (Instruction Following)

**Why ruled out:** Tests whether models follow specific formatting instructions (write exactly N paragraphs, avoid letter X, etc.). Programmatically verifiable but tests compliance, not reasoning quality. Highly sensitive to prompt phrasing (IFEval++ shows up to 61.8% performance drops from nuanced prompt modifications), but the sensitivity is about surface-level instruction parsing, not cognitive mode management.

---

## The Inspect AI Angle

One finding worth highlighting: **Inspect AI** (UK AISI) provides a framework where the `solver` component (the scaffold/prompt strategy) is a first-class, swappable module. Any benchmark implemented in Inspect can be run with different solvers. GAIA, for example, uses Inspect and accepts a custom solver parameter.

This means the right approach may not be to find a benchmark that already has competing scaffolds, but rather to **take a knowledge-work benchmark and run it through Inspect with our three tiers as different solvers**. The framework handles the plumbing; we just need a benchmark with:
- Rich, rubric-based scoring (not binary pass/fail)
- Tasks requiring multiple cognitive modes
- Sufficient difficulty that prompt quality matters

PRBench meets all three criteria and already has its own evaluation infrastructure.

---

## Synthesis and Recommendation

### The core finding

No existing benchmark perfectly matches our need for "knowledge-work SWE-bench" — a benchmark where competing teams have built scaffold prompts for professional reasoning tasks and where changing the scaffold changes scores. This gap exists because:

1. **Agent benchmarks** (GAIA, tau-bench, WebArena) have scaffold competition but test tool orchestration, not professional reasoning quality.
2. **Knowledge-work benchmarks** (PRBench, LegalBench, FinBen) test professional reasoning but were designed for model comparison with standardised prompts.
3. **Prompt-engineering benchmarks** (PromptBench) test generic prompting techniques on simple tasks.

### The evidence that prompts matter for knowledge work

Even without a perfect benchmark, the evidence is strong:

| Source | Finding |
|--------|---------|
| **Tau-bench** (Anthropic) | 54% relative improvement from prompt optimisation alone (same model) |
| **HAL** | Scaffolds "dramatically impact both accuracy and cost" across 9 benchmarks |
| **HAL** | Higher reasoning effort *reduced* accuracy in 21/36 runs (supports mode interference) |
| **LegalBench** | Plain language outperforms technical language; 11.3% improvement from prompt structure |
| **SWE-bench** | Same model (GPT-4o) doubles score (16% to 33.2%) with better scaffold |
| **GAIA** | 10x score range across different scaffolds |

### Recommendation: Stay with PRBench

PRBench is the right choice for B2. Here is why:

1. **We are the ones varying the prompt.** We do not need existing scaffold competition — we are building the three tiers ourselves. PRBench gives us the rubric infrastructure to measure the difference our prompt changes make.

2. **The rubric captures what we predict will change.** PRBench's 11 dimensions (Process Transparency, Handling Uncertainty, Supplemental Insight, etc.) map directly to cognitive modes. A binary pass/fail benchmark would miss the quality improvements we predict.

3. **The benchmark documents our phenomenon.** "Models frequently reach correct conclusions through incomplete or opaque reasoning" — this is exactly "good output hides great output."

4. **Professional reasoning tasks require mode combination.** A complex legal analysis requires investigation + analysis + evaluation + synthesis — exactly the multi-mode pattern where our theory predicts pipeline separation helps.

5. **Massive headroom.** Top models score 37-39% on Hard. There is room for prompt engineering to make a visible difference.

### Future experiment: Build a scaffold-comparison benchmark

For a future B3 or C-series experiment, the ideal setup would be:
- Take tau-bench or GAIA as the benchmark harness
- Replace the tasks with professional-reasoning tasks from PRBench or LegalBench
- Build competing scaffolds (monolithic vs pipeline) as Inspect AI solvers
- Run the same model through both and measure the difference

This would create the "knowledge-work SWE-bench" that does not yet exist.

---

## Sources

### Benchmarks researched
- [HELM (Stanford CRFM)](https://crfm.stanford.edu/helm/) — [GitHub](https://github.com/stanford-crfm/helm)
- [Tau-bench (Sierra Research)](https://github.com/sierra-research/tau-bench) — [Paper](https://arxiv.org/abs/2406.12045)
- [Tau2-bench](https://github.com/sierra-research/tau2-bench)
- [GAIA (Meta)](https://arxiv.org/abs/2311.12983) — [Leaderboard](https://huggingface.co/spaces/gaia-benchmark/leaderboard)
- [HAL (Princeton)](https://hal.cs.princeton.edu/) — [Paper](https://arxiv.org/abs/2510.11977) — [GitHub](https://github.com/princeton-pli/hal-harness)
- [LegalBench (Stanford/Hazy Research)](https://github.com/HazyResearch/legalbench) — [Website](https://hazyresearch.stanford.edu/legalbench/)
- [PromptBench (Microsoft)](https://github.com/microsoft/promptbench) — [Paper](https://arxiv.org/abs/2312.07910)
- [FinBen](https://arxiv.org/abs/2402.12659)
- [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) — [Paper](https://arxiv.org/abs/2406.01574)
- [BigBench](https://github.com/google/BIG-bench)
- [MedQA](https://www.emergentmind.com/topics/medqa-and-medmcqa)
- [GPQA](https://arxiv.org/abs/2311.12022) — [GitHub](https://github.com/idavidrein/gpqa)
- [WebArena](https://webarena.dev/) — [Paper](https://arxiv.org/abs/2307.13854)
- [WorkArena (ServiceNow)](https://servicenow.github.io/WorkArena/) — [GitHub](https://github.com/ServiceNow/WorkArena)
- [BrowseComp (OpenAI)](https://openai.com/index/browsecomp/) — [Paper](https://arxiv.org/abs/2504.12516)
- [LiveBench](https://livebench.ai/) — [GitHub](https://github.com/LiveBench/LiveBench)
- [IFEval](https://arxiv.org/abs/2311.07911)
- [PRBench (Scale AI)](https://arxiv.org/abs/2511.11562) — [GitHub](https://github.com/scaleapi/PRBench)

### Key evidence papers
- [Anthropic: The "think" tool](https://www.anthropic.com/engineering/claude-think-tool) — 54% improvement on tau-bench from prompt engineering
- [Inspect AI (UK AISI)](https://inspect.aisi.org.uk/) — [GitHub](https://github.com/UKGovernmentBEIS/inspect_ai)
- [DSPy+HELM structured prompting](https://github.com/StanfordMIMI/dspy-helm)
