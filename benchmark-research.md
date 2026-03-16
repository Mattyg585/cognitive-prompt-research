# Benchmark Research for Prompt Optimization Experiments

**Date**: 2026-03-16
**Purpose**: Identify non-code AI benchmarks suitable for testing whether cognitively scoped pipelines outperform monolithic prompts.

**Selection criteria**: Tasks must involve multi-mode knowledge work (investigation + analysis + synthesis), have modifiable prompts/instructions, offer objective or semi-objective scoring, and be runnable manually without special infrastructure.

---

## Executive Summary: Top Candidates

Ranked by suitability for mode-interference experiments:

| Rank | Benchmark | Why It Fits | Effort to Run |
|------|-----------|-------------|---------------|
| 1 | **PRBench** (Legal/Finance) | Real professional reasoning; rubric-based scoring; models score <40% on hard set; requires investigation+analysis+judgment | Low (open-source, HuggingFace) |
| 2 | **MuSR** | Multi-step soft reasoning over narratives; requires decomposition, commonsense, theory-of-mind; CoT-sensitive | Low (GitHub, 3 domains) |
| 3 | **BBEH** | 23 diverse reasoning tasks; harmonic mean scoring punishes imbalance; best model only 44.8%; long-context | Low (GitHub, DeepMind) |
| 4 | **WildBench** | 1,024 real-world tasks; rubric checklists; high correlation with human preference; diverse task types | Low (GitHub, Allen AI) |
| 5 | **MedHELM** | 35 clinical benchmarks; real EHR data; rubric-based LLM-jury evaluation; multi-category clinical reasoning | Medium (Stanford HELM framework) |
| 6 | **HotpotQA** | Multi-hop reasoning; requires finding+connecting evidence across documents; well-studied prompting effects | Low (public dataset) |
| 7 | **GPQA Diamond** | Graduate-level science; CoT-sensitive; but now largely saturated (~91% for Claude) | Low (public, 198 questions) |
| 8 | **Humanity's Last Exam** | Frontier-hard; expert-level; but mostly single-step knowledge retrieval, not multi-mode work | Medium (public subset) |

---

## Detailed Benchmark Analysis

---

### 1. GPQA (Graduate-Level Google-Proof Q&A)

**What it tests**: 448 multiple-choice questions in biology, physics, chemistry written by PhD-level domain experts. "Google-proof" -- non-experts with web access score only 34%.

**Subsets**:
- GPQA Extended: 546 questions
- GPQA Main: 448 questions
- GPQA Diamond: 198 highest-quality questions (the standard evaluation subset)

**Scoring**: Objective exact-match on multiple choice (A/B/C/D). Random baseline is 25%.

**Prompting approaches tested**: Zero-shot, few-shot, zero-shot CoT, few-shot CoT. Standard format: present question + choices, then "Reason through your answer step-by-step... Answer in the format 'The correct answer is (X).'"

**Can prompts be modified?** Yes. The prompting format is straightforward and fully modifiable.

**Can tasks be cherry-picked?** Yes. Individual questions are self-contained.

**Current Claude performance**: Claude Opus 4.6 scores ~91.3% on Diamond. The benchmark is largely saturated -- frontier models are 20+ points above the PhD expert baseline of ~70%.

**Prompt sensitivity**: Moderate. CoT vs. non-CoT matters significantly. Few-shot exemplar selection affects results.

**Fit for mode-interference research**: **MODERATE-LOW**. Questions are hard but fundamentally single-mode: read question, reason, select answer. There is no investigation phase or synthesis across sources. The high saturation also limits headroom for improvement. However, the science reasoning is genuinely complex and could benefit from separating "understand the question" from "apply domain knowledge" from "evaluate options."

**Sources**:
- [GPQA Paper (arXiv)](https://arxiv.org/abs/2311.12022)
- [GPQA GitHub](https://github.com/idavidrein/gpqa)
- [Epoch AI - GPQA Diamond](https://epoch.ai/benchmarks/gpqa-diamond)

---

### 2. MMLU-Pro

**What it tests**: 12,000+ questions across 14 domains (biology, business, chemistry, CS, economics, engineering, health, history, law, math, philosophy, physics, psychology). Extends MMLU with harder, reasoning-focused questions and 10 answer choices instead of 4.

**Scoring**: Objective accuracy (% correct). Scale 0-100.

**Prompting approach**: 5-shot CoT is standard. CoT delivers massive gains: +19.1% for GPT-4o, +15.3% for GPT-4-Turbo. On original MMLU, CoT was flat or negative -- MMLU-Pro specifically requires deeper reasoning.

**Can prompts be modified?** Yes. The 5-shot CoT examples and instructions are configurable.

**Can tasks be cherry-picked?** Yes. Questions are independent and domain-tagged.

**Current Claude performance**: Claude Opus 4.5 (Reasoning) scores ~89.5%. Approaching saturation.

**Prompt sensitivity**: Surprisingly LOW. Impact of prompt changes is generally ~2%, max 3.74% (vs. 4-5% and up to 11% on original MMLU). The 10-option format reduces lucky guessing and prompt gaming.

**Fit for mode-interference research**: **LOW**. Despite requiring reasoning, each question is still fundamentally a single-step task: read, reason, answer. The low prompt sensitivity means better prompting has limited headroom. Useful as a control benchmark (to show that pipeline approaches help complex tasks but not simple ones).

**Sources**:
- [MMLU-Pro Paper (arXiv)](https://arxiv.org/abs/2406.01574)
- [MMLU-Pro GitHub](https://github.com/TIGER-AI-Lab/MMLU-Pro)
- [Artificial Analysis Leaderboard](https://artificialanalysis.ai/evaluations/mmlu-pro)

---

### 3. ARC-AGI / ARC-AGI-2

**What it tests**: Few-shot visual pattern recognition and abstract reasoning. Grid-based tasks where the model must infer transformation rules from examples and apply them to new inputs. Tests generalization, not knowledge.

**Scoring**: Per-task exact match (all output grids must be pixel-perfect correct). Up to 2 guesses per input. Overall score = % of tasks solved. ARC-AGI-2 adds cost-per-task efficiency metric.

**Can prompts be modified?** Not in a traditional sense. The "prompt" is the grid examples themselves. The system prompt/scaffolding for how the model approaches the task is modifiable, but the core challenge is visual/spatial reasoning, not language-based analysis.

**Can tasks be cherry-picked?** Yes, tasks are independent.

**Current Claude performance**: Claude 3.7 Sonnet scored 0.0% on ARC-AGI-2 at launch (March 2025). ARC-AGI-2 is dramatically harder than ARC-AGI-1.

**Key insight**: What wins is "refinement loops" -- iterative program optimization with feedback. This is fundamentally a pipeline/orchestration challenge, not a prompting challenge.

**Fit for mode-interference research**: **LOW for our purposes**. While the finding that orchestration beats monolithic approaches is directionally aligned with our thesis, the tasks are visual/spatial pattern matching, not knowledge-worker activities. The "modes" involved (pattern recognition, rule induction, rule application) are too specialized.

**Sources**:
- [ARC Prize](https://arcprize.org/)
- [ARC-AGI-2](https://arcprize.org/arc-agi/2/)
- [ARC Prize 2025 Technical Report](https://arxiv.org/html/2601.10904v1)

---

### 4. BIG-Bench Hard (BBH) and BIG-Bench Extra Hard (BBEH)

**What BBH tests**: 23 tasks from BIG-Bench where prior LMs did not outperform average human raters. Tasks include logical deduction, causal judgment, disambiguation, temporal reasoning, object tracking, etc.

**Scoring**: Exact match accuracy. Each task defines its own metric. CoT prompting with manually designed exemplars boosts performance by 13-17 percentage points.

**BBH status**: Largely saturated for frontier models.

**BBEH (February 2025)**: Replaces each BBH task with a harder counterpart. 23 tasks, 4,520 examples total (mini: 460). Context lengths 6x longer, output lengths 7x longer than BBH. Uses **harmonic mean accuracy** to penalize imbalanced performance across tasks.

**BBEH tasks include**: Boardgame QA (many-hop deduction), Disambiguation QA, New Yorker Caption Contest, Sarcasm detection, Hyperbaton, Linguini (linguistic olympiad), Boolean expressions, Causal Judgment, Date Understanding, Object Tracking, SVG interpretation, Temporal reasoning, and more.

**BBEH performance**: Best general-purpose model: 9.8% harmonic mean. Best reasoning model: 44.8%.

**Can prompts be modified?** Yes. Standard prompting with configurable zero-shot, few-shot, and CoT options.

**Can tasks be cherry-picked?** Yes. Tasks are independent, domain-tagged. The mini version (460 examples) is very manageable.

**Prompt sensitivity**: HIGH for BBH (CoT gains of 13-17pp). BBEH is designed to resist shortcuts but prompting strategy still matters significantly.

**Fit for mode-interference research**: **HIGH (BBEH)**. Several BBEH tasks require exactly the kind of multi-step reasoning where mode interference matters: many-hop deduction (investigate, track, conclude), causal judgment (gather evidence, model causation, evaluate), disambiguation (parse, consider alternatives, select). The unsaturated scores provide massive headroom. The harmonic mean scoring means you can not cheat by being good at easy tasks. The diverse task types let you test which reasoning modes benefit most from pipeline separation.

**Sources**:
- [BBEH Paper (arXiv)](https://arxiv.org/abs/2502.19187)
- [BBEH GitHub (DeepMind)](https://github.com/google-deepmind/bbeh)
- [BBH GitHub](https://github.com/suzgunmirac/BIG-Bench-Hard)
- [UK AISI Inspect Evals - BBEH](https://ukgovernmentbeis.github.io/inspect_evals/evals/reasoning/bbeh/)

---

### 5. HELM (Stanford Holistic Evaluation of Language Models)

**What it tests**: Meta-framework evaluating LLMs across 42 scenarios on 7 metrics: accuracy, calibration, robustness, fairness, bias, toxicity, efficiency. Tasks include QA, information retrieval, summarization, sentiment analysis, toxicity detection, code generation.

**Scoring**: Multi-metric per scenario. Standardized across models.

**Extensions**:
- **MedHELM**: 35 medical benchmarks across 5 clinical categories (see below)
- **HELM Long Context**: Long-document evaluation
- **VHELM**: Vision-language models

**Can prompts be modified?** Yes, via the HELM framework's prompt configuration.

**Can tasks be cherry-picked?** Yes, scenarios are modular.

**Fit for mode-interference research**: **MEDIUM**. HELM itself is a framework, not a single benchmark. The individual tasks within it vary in complexity. The most useful thing about HELM is that it provides standardized evaluation infrastructure -- you could use it to run experiments rather than as the experiment subject itself.

**Sources**:
- [HELM Leaderboard](https://crfm.stanford.edu/helm/capabilities/latest/)
- [HELM Paper (arXiv)](https://arxiv.org/abs/2211.09110)
- [HELM GitHub](https://github.com/stanford-crfm/helm)

---

### 6. MedHELM (Medical Holistic Evaluation)

**What it tests**: 35 benchmarks covering 5 clinical categories: clinical decision support, clinical note generation, patient communication, medical research assistance, administration/workflow. Uses real EHR data from Stanford Healthcare. Published in Nature Medicine.

**Scoring**: Mix of exact-match accuracy and rubric-based LLM-jury evaluation. The LLM-jury achieved ICC=0.47 agreement with clinicians (exceeding average clinician-clinician agreement of 0.43).

**Task complexity**: Tasks range from simple (classification) to complex (clinical note generation from EHR records, referral triage, treatment planning). The complex tasks require investigation (read clinical data) + analysis (identify relevant findings) + synthesis (generate coherent clinical output).

**Can prompts be modified?** Yes. Each benchmark has a configurable prompt template (.txt) + dataset (.csv) + config (.yaml).

**Can tasks be cherry-picked?** Yes. Benchmarks are modular.

**Current performance**: Models score 0.56-0.72 on Clinical Decision Support and 0.53-0.63 on Administration/Workflow -- substantial headroom.

**Fit for mode-interference research**: **HIGH**. Clinical decision support and medical research tasks are classic multi-mode work: gather clinical data (investigation), identify patterns (analysis), synthesize into recommendations (judgment/synthesis). The rubric-based evaluation captures quality dimensions that exact-match misses. The open-source framework makes it practical to run.

**Sources**:
- [MedHELM Paper (arXiv)](https://arxiv.org/abs/2505.23802)
- [MedHELM Nature Medicine](https://www.nature.com/articles/s41591-025-04151-2)
- [MedHELM Leaderboard](https://crfm.stanford.edu/helm/medhelm/latest/)

---

### 7. Humanity's Last Exam (HLE)

**What it tests**: 2,500 expert-level questions across mathematics (41%), physics (9%), biology/medicine (11%), humanities/social science (9%), CS/AI (10%), engineering (4%), chemistry (7%), other (9%). Designed to be "Google-proof" and beyond current model capabilities.

**Scoring**: Exact-match for short-answer questions (76% of the set), multiple-choice for the rest (24%). Temperature 0.0 evaluation. o3-mini used as automatic answer extractor/judge.

**Can prompts be modified?** Yes. Models are prompted to give a final answer + confidence estimate. The prompting approach is modifiable.

**Can tasks be cherry-picked?** Yes. Questions are independent and subject-tagged.

**Current Claude performance**: Claude Opus 4.6 leads the leaderboard at ~53.1%.

**Known issues**: ~29% of biology/chemistry answers may be incorrect (FutureHouse audit). HLE-Rolling (dynamic fork) was released October 2025 to address this.

**Prompt sensitivity**: Unknown/unstudied formally. Given the extreme difficulty, better prompting alone is unlikely to move the needle significantly -- the bottleneck is knowledge, not reasoning scaffolding.

**Fit for mode-interference research**: **LOW-MODERATE**. Most questions are single-step expert knowledge retrieval or calculation. They are hard because the knowledge is rare, not because the task structure is complex. There is no investigation+synthesis pattern -- just "know this obscure fact." A few questions in humanities/social science might involve multi-mode reasoning, but they are not the majority.

**Sources**:
- [HLE Website](https://agi.safe.ai/)
- [HLE Paper (arXiv)](https://arxiv.org/abs/2501.14249)
- [Scale AI Leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [FutureHouse Audit](https://www.futurehouse.org/research-announcements/hle-exam)

---

### 8. FrontierMath

**What it tests**: 350 original research-level mathematics problems across number theory, real analysis, algebraic geometry, category theory, etc. Created by 60+ mathematicians including IMO gold medalists and a Fields Medal recipient.

**Scoring**: All-or-nothing exact match. Models submit answers as Python code. "Guessproof" -- <1% chance of correct answer without doing the math.

**Can prompts be modified?** Limited. Models can use Python to compute answers, but the core challenge is mathematical, not linguistic.

**Current performance**: OpenAI o3 scored 25%. Most frontier models under 2%.

**Fit for mode-interference research**: **VERY LOW**. Pure mathematics. The bottleneck is mathematical reasoning ability, not prompt structure. There is no knowledge-worker-style multi-mode task.

**Sources**:
- [FrontierMath (Epoch AI)](https://epoch.ai/frontiermath)
- [FrontierMath Paper (arXiv)](https://arxiv.org/abs/2411.04872)

---

### 9. PRBench (Professional Reasoning Benchmark)

**What it tests**: 1,100 expert-authored tasks in Law (550) and Finance (550), derived from real professional workflows. Tasks span 114 countries and 47 US jurisdictions. Questions come from actual client inquiries and professional experience.

**Scoring**: Rubric-based evaluation using LLM judge (o4 Mini). Each question has 10-30 expert-curated criteria with importance weights. Scores normalized 0-1. Judge achieves 80.2% agreement with human experts (on par with 79.6% human-human agreement). Performance analyzed across 11 rubric categories including Legal/Financial Accuracy, Process Transparency, Risk & Ethical Disclosure.

**Can prompts be modified?** Yes. Standard LLM prompting. The evaluation rubrics are fixed but the system/user prompts to the model are fully configurable.

**Can tasks be cherry-picked?** Yes. Tasks are independent, domain-tagged, and difficulty-rated (full set + hard subset).

**Current performance**: Top models score only 0.37-0.39 on the Hard subset. Even on full set, top is ~0.51. Models reach correct conclusions through incomplete reasoning, reducing practical reliability.

**Key finding**: "Models frequently reach correct conclusions through incomplete or opaque reasoning processes, significantly reducing their practical reliability in professional settings." This is exactly the kind of invisible quality gap that mode interference predicts.

**Fit for mode-interference research**: **VERY HIGH**. This is the ideal benchmark for our research:
1. Tasks require genuine multi-mode professional reasoning (investigate facts, apply domain knowledge, synthesize judgment, communicate reasoning)
2. The rubric captures not just correctness but reasoning quality and process transparency -- exactly where pipeline approaches should shine
3. Massive headroom (<40% on hard set)
4. Open-source (HuggingFace + GitHub)
5. The documented finding that models get answers right but reasoning wrong is precisely the "good output hides great output" phenomenon
6. Professional domain tasks are the target use case for prompt optimization

**Sources**:
- [PRBench Paper (arXiv)](https://arxiv.org/abs/2511.11562)
- [PRBench GitHub](https://github.com/scaleapi/PRBench)
- [Scale AI Legal Leaderboard](https://labs.scale.com/leaderboard/prbench-legal)
- [Scale AI Finance Leaderboard](https://labs.scale.com/leaderboard/prbench-finance)
- [Scale AI Blog](https://scale.com/blog/prbench)

---

### 10. MuSR (Multistep Soft Reasoning)

**What it tests**: Multi-step reasoning over natural language narratives in three domains: murder mysteries, object placement, and team assignment. Narratives are ~1000 words. Requires commonsense reasoning, theory-of-mind, causal reasoning.

**Scoring**: Accuracy on multiple-choice answers. Multiple prompting variants tested: Regular, CoT, CoT+ (with reasoning strategy description), 1-Shot CoT+.

**Dataset generation**: Neurosymbolic approach -- reasoning trees are constructed first, then natural language narratives are generated around them. This means ground truth is verifiable.

**Can prompts be modified?** Yes. Multiple prompting strategies are already part of the evaluation protocol.

**Can tasks be cherry-picked?** Yes. Tasks are domain-tagged and independent.

**Prompt sensitivity**: HIGH. 1-Shot CoT+ significantly outperforms Regular prompting. The choice of prompting strategy is a primary variable in the benchmark.

**Fit for mode-interference research**: **VERY HIGH**. Murder mysteries are a perfect mode-interference test case:
1. Investigation mode: Read the narrative, extract clues, track characters and events
2. Analysis mode: Connect clues, reason about motives and opportunities
3. Judgment mode: Weigh evidence, eliminate alternatives, select answer

The CoT+ prompt variants are already testing something adjacent to our hypothesis -- they are separating "understand the reasoning strategy" from "apply it to this case." A pipeline that cleanly separates investigation from analysis from judgment should produce measurable gains. The narrative format also means context management matters -- a key advantage of pipelines.

**Sources**:
- [MuSR Paper (arXiv)](https://arxiv.org/abs/2310.16049)
- [MuSR GitHub](https://github.com/Zayne-sprague/MuSR)

---

### 11. HotpotQA

**What it tests**: 112,779 multi-hop question-answer pairs requiring reasoning across multiple Wikipedia documents. Questions need finding and connecting information from multiple sources.

**Scoring**: Exact Match (EM) and F1. Sentence-level supporting facts are also evaluated.

**Can prompts be modified?** Yes. Extensive research on prompting strategies (CoT, retrieval augmentation, sub-question decomposition).

**Can tasks be cherry-picked?** Yes.

**Current performance**: State-of-the-art systems achieve ~36-39% EM in zero-shot settings.

**Known issues**: Data contamination risk (Wikipedia-based, models pretrained on Wikipedia). Performance inflation from memorized knowledge documented.

**Prompt sensitivity**: HIGH. Different retrieval and prompting strategies produce large differences. Sub-question decomposition, Expert-CoT, and hybrid retrieval all show significant gains.

**Fit for mode-interference research**: **MODERATE-HIGH**. Multi-hop QA is inherently multi-mode: retrieve relevant docs (investigation), connect information across docs (analysis), synthesize answer (judgment). However, the questions themselves are relatively simple factoid queries -- not the complex professional reasoning that most strongly triggers mode interference. Better suited as a secondary benchmark than a primary one.

**Sources**:
- [HotpotQA Website](https://hotpotqa.github.io/)
- [HotpotQA Paper (arXiv)](https://arxiv.org/abs/1809.09600)

---

### 12. DROP (Discrete Reasoning Over Paragraphs)

**What it tests**: 96K reading comprehension questions requiring discrete reasoning (addition, counting, sorting) over paragraph content.

**Scoring**: Custom F1 and exact match. Answers are typically numbers or names.

**Known issues**: Evaluation methodology problems caused it to be removed from the Open LLM Leaderboard. Scoring implementation in lm-evaluation-harness was overly strict.

**Fit for mode-interference research**: **LOW**. Despite requiring "discrete reasoning," the tasks are relatively mechanical (count entities, sort by attribute, add numbers). Not the kind of complex knowledge work where mode interference would manifest.

**Sources**:
- [DROP Paper (arXiv)](https://arxiv.org/abs/1903.00161)
- [HuggingFace DROP Deep Dive](https://huggingface.co/blog/open-llm-leaderboard-drop)

---

### 13. AlpacaEval / MT-Bench / Chatbot Arena

**AlpacaEval**: ~800 instruction-following tasks. LLM-as-judge (GPT-4 Turbo) compares model output against reference. Length-controlled win rate metric. 0.98 Spearman correlation with human eval. <$10, <3 minutes to run.

**MT-Bench**: 80 curated multi-turn questions. GPT-4 scores on 1-10 scale. Tests conversational and instruction-following ability.

**Chatbot Arena**: Crowdsourced platform. Users pose questions to two anonymous models, pick the winner. Elo ratings from 1.5M+ pairwise preferences.

**Can prompts be modified?** For AlpacaEval and MT-Bench, the system prompts to the evaluated model are modifiable. For Arena, no -- it is a live platform.

**Prompt sensitivity**: All three are sensitive to length bias (longer responses tend to win). AlpacaEval-LC addresses this with regression-based debiasing.

**Fit for mode-interference research**: **LOW-MODERATE**. These benchmarks test general helpfulness and instruction-following, not multi-step reasoning. They could serve as a "does pipeline optimization hurt simple tasks?" control, but are not primary candidates. MT-Bench's multi-turn format is slightly more interesting -- the second turn often requires building on the first, which is a simple form of multi-mode work.

**Sources**:
- [AlpacaEval GitHub](https://github.com/tatsu-lab/alpaca_eval)
- [MT-Bench/Chatbot Arena Blog](https://lmsys.org/blog/2023-06-22-leaderboard/)

---

### 14. WildBench

**What it tests**: 1,024 challenging tasks from real user-chatbot conversations (filtered from 1M+ logs). Published at ICLR 2025.

**Scoring**: Two metrics:
- WB-Reward: Pairwise comparison against 3 baseline models (5 outcome levels). Pearson correlation 0.98 with Chatbot Arena Elo.
- WB-Score: Individual quality score 1-10 from GPT-4-turbo. Pearson 0.95 with Arena.

Task-specific checklists guide evaluation (inspired by how humans evaluate open-ended responses). Length penalty applied to mitigate length bias.

**Can prompts be modified?** Yes. The system prompt and instructions to the evaluated model are configurable. The tasks themselves are fixed real-user queries.

**Can tasks be cherry-picked?** Yes. Tasks are categorized and independent.

**Fit for mode-interference research**: **MODERATE-HIGH**. The real-user queries include complex tasks that require multiple cognitive modes. The task-specific checklists provide structured evaluation criteria that could capture quality differences a pipeline produces. The high correlation with human preference validates the scoring. The diversity of tasks means you could identify which task types benefit most from pipeline approaches.

**Sources**:
- [WildBench Paper (arXiv)](https://arxiv.org/abs/2406.04770)
- [WildBench GitHub](https://github.com/allenai/WildBench)

---

### 15. WritingBench

**What it tests**: 1,239 generative writing tasks across academic, finance, law, art, education, and marketing domains. Fine-grained annotations for writing quality.

**Scoring**: Trained criteria-aware critic model (Qwen-2.5-7B-Instruct) achieves 83% agreement with human preference. Dynamic, query-specific evaluation rubrics.

**Can prompts be modified?** Yes.

**Fit for mode-interference research**: **MODERATE**. Writing tasks inherently involve multiple modes (research/understand requirements, plan structure, draft, refine). The domain diversity is useful. However, the evaluation is via a small fine-tuned critic model, which may not capture the subtle quality differences that pipeline approaches produce.

**Sources**:
- [WritingBench (Emergent Mind)](https://www.emergentmind.com/topics/writingbench)

---

## Recommended Experiment Design

### Primary Benchmarks (run all three tiers)

1. **PRBench (Legal Hard subset)** -- 250 tasks with rubric-based evaluation. The professional reasoning tasks with rubric scoring directly measure both correctness and reasoning quality. The documented finding that models get answers right through opaque reasoning is exactly the phenomenon mode-separated pipelines should fix.

2. **MuSR (Murder Mysteries)** -- Multi-step narrative reasoning with clear investigation/analysis/judgment phases. The murder mystery domain is intuitive to explain and the reasoning structure maps cleanly to cognitive modes.

3. **BBEH (selected tasks)** -- Cherry-pick 3-4 tasks that require multi-hop reasoning and long-context processing: Boardgame QA, Causal Judgment, Disambiguation QA, Temporal Reasoning. The harmonic mean scoring prevents gaming.

### Secondary Benchmarks (spot-check for generalization)

4. **WildBench (complex task subset)** -- Filter for tasks requiring multi-step reasoning. Use as a "real-world validity" check.

5. **MedHELM (Clinical Decision Support tasks)** -- If we want a medical domain experiment.

### Control Benchmarks (expect NO improvement from pipeline)

6. **MMLU-Pro (any domain)** -- Single-step knowledge questions. Pipeline approach should show no benefit or even slight degradation from overhead. This validates that our approach only helps where mode interference actually exists.

---

## Key Observations for the Research

### Alignment with the mode-interference thesis

1. **PRBench explicitly documents the phenomenon we predict**: models reach correct conclusions through incomplete reasoning. A pipeline that forces clean investigation before analysis before synthesis should produce better reasoning transparency scores even when final answers are similar.

2. **MuSR's prompting variants are already testing adjacent hypotheses**: CoT+ separates "understand the strategy" from "apply it." Our pipeline approach takes this further by separating "investigate the narrative" from "analyze the evidence" from "reach a verdict."

3. **BBEH's harmonic mean scoring is ideal**: It prevents a model from coasting on easy tasks. If pipeline approaches help on hard multi-hop tasks but not simple ones, the harmonic mean will capture this.

4. **Prompt sensitivity research confirms our thesis direction**: The finding that "sensitivity goes up as accuracy goes down" and that detailed prompts help inconsistently suggests that the problem is not prompt quality per se, but mode contamination within the prompt.

### Practical considerations

- **PRBench, MuSR, and BBEH** are all open-source with GitHub repos and HuggingFace datasets. No special infrastructure needed.
- **PRBench's rubric-based evaluation** is the most informative for our purposes because it captures reasoning quality, not just answer correctness.
- **Running all three tiers** (original prompt, optimized prompt, pipeline) on even 50-100 PRBench tasks with 3 runs each would produce meaningful signal.
- **Cost**: PRBench evaluation uses o4-mini as judge (~$0.01-0.05 per evaluation). MuSR and BBEH use exact-match scoring (free). The main cost is running the model being tested.
