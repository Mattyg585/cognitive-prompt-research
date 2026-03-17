# B-Series Findings: Benchmark Validation

**Written**: 17 March 2026
**Status**: Complete. Single-run directional findings on two benchmarks.
**Model**: Claude Opus 4.6 (generation), Claude Sonnet 4.6 (judge)

---

## 1. What We Tested and Why

The A-series tested cognitive mode separation on knowledge-work plugins using our own qualitative rubric. The B-series asked a harder question: does it move the needle on externally-scored benchmarks where we did not design the evaluation?

Two benchmarks, two domains:

**B1 — SWE-bench Verified** (coding). Three tasks spanning easy/medium/hard. Binary pass/fail against gold test patches. Tests whether cognitive mode separation improves convergent problem-solving with deterministic answers.

**B2 — PRBench** (professional reasoning). Two tasks: an easy single-turn finance question (16 criteria, 7 rubric categories) and a hard multi-turn legal question (26 criteria, 7 rubric categories). Expert-authored rubrics from 182 domain professionals. Tests whether cognitive mode separation improves complex analytical judgment with multi-dimensional quality scoring.

The B-series was designed to complement the A-series. The A-series showed qualitative improvement but used our own rubrics — we could be seeing what we wanted to see. The B-series uses rubrics we did not create, scoring infrastructure we did not design, and benchmarks documented by their own authors as capturing our exact phenomenon ("models frequently reach correct conclusions through incomplete or opaque reasoning").

---

## 2. B1 Finding: Coding Benchmarks Are Saturated

Anthropic's minimal 5-step SWE-bench scaffold (the baseline) passed all three tasks: scikit-learn (easy), django (medium), sympy (hard). The fixes matched gold patches — correct approach, correct location, correct fix.

There was nothing for Tier 2 or Tier 3 to improve. Binary pass/fail on convergent coding tasks leaves no room for prompt architecture to differentiate. When the task has a clear right answer and the model already gets it right, cognitive mode separation is irrelevant.

This is itself a finding. Cognitive mode separation does not measurably improve dominant convergent thinking. The model compensates for mode interference when the task has a clear convergent answer — it can power through distributional noise when the signal is strong enough. The interference we care about operates on the margins of complex judgment, not on the core of straightforward problem-solving.

B1 was dropped from active experimentation after this result. The finding narrowed the theory: look for pipeline value in tasks requiring divergent analytical judgment, not convergent problem-solving.

---

## 3. B2 Finding: Cognitive Hygiene Works, Pipeline Overcooked

### Overall scores on the hard task

| Tier | Score | Criteria Met |
|------|-------|-------------|
| Baseline | 0.759 | 20/26 |
| Pipeline (Tier 3) | 0.849 | 22/26 |
| Tier 2 (Optimised) | 0.950 | 25/26 |

The prediction was Baseline < Tier 2 < Pipeline. Actual: Baseline < Pipeline < Tier 2.

### Overall scores on the easy task

All three tiers scored 16/16 (1.0). Saturated, same as B1. The easy finance task was not hard enough for prompt architecture to differentiate.

### Category-level breakdown on the hard task

| Category | Baseline | Tier 2 | Pipeline |
|----------|----------|--------|----------|
| Legal Accuracy | 1.000 | 1.000 | 1.000 |
| Application of Law to Facts | 0.722 | 1.000 | 0.722 |
| Supplemental Insight | 0.467 | 1.000 | 1.000 |
| Handling Uncertainty | 0.762 | 1.000 | 0.762 |
| Practical Utility | 0.632 | 1.000 | 0.632 |
| Procedural Correctness | 0.000 | 1.000 | 0.000 |
| Instruction Following | 0.000 | 0.000 | 1.000 |

The pattern here is not the one we predicted. We expected the pipeline to outperform Tier 2 across the board, with concentrated gains in mode-interference-sensitive categories. Instead, Tier 2 swept nearly every category, and the pipeline showed a mixed profile — matching Tier 2 in some places, matching baseline in others.

---

## 4. What Actually Moved the Needle

The Tier 2 intervention was a single system prompt. No pipeline, no multi-agent architecture, no structured handoffs. It did four things:

**Set an epistemic stance.** "Explore the analytical landscape fully before reaching conclusions." This is the highest level of the cognitive stack. It cascades through intent, mode, register, and language patterns. The baseline's implicit epistemic stance was "answer this professional question authoritatively." The intervention replaced that with "map what is here before deciding what it means."

**Created a scope boundary.** "Phase 1 maps, Phase 2 synthesises — do not conclude in Phase 1." Both phases happened in one response, one context window. But naming them and naming what Phase 1 is NOT doing (concluding) reduced evaluative bleed into the discovery work.

**Elevated uncertainty to substantive analysis.** Not "note limitations" as an afterthought bolted onto the end. The prompt established that surfacing what is unresolved is professionally valuable — it is the analysis, not a caveat to it.

**Gave explicit permission to approach the follow-up question fresh.** The hard task is multi-turn. Turn 1 produced a heavily structured, bulleted, high-confidence analysis. Without intervention, the model inherits that cognitive posture for Turn 2. The Tier 2 prompt said: treat the prior exchange as background factual context, not as a mode to continue. This interrupted mode inheritance.

Result: 0.759 to 0.950. The active ingredient was the epistemic stance intervention at the top of the cognitive stack, cascading through everything below it. No pipeline needed.

---

## 5. Why the Pipeline Underperformed Tier 2

The pipeline (three stages: discovery, analysis, advisory synthesis) scored 0.849 — better than baseline but worse than Tier 2. Here is why.

### What the pipeline lost

**Handoff information loss on procedural details.** Criteria 17-19 (valuation mechanics for tokenized assets, FMV estimation, valuation reporting requirements) were specific procedural details from the original question. They did not map cleanly to any Stage 1 handoff schema field. The schema had fields for "applicable rules," "significant facts," "rule-fact connections," "open questions," and "considerations beyond the direct question." Procedural valuation mechanics fell between these categories — too specific for "rules," too analytical for "facts," too procedural for "considerations." They were lost during structured compression.

**Question details that never reached Stage 3.** Criterion 26 (recent agency commentary — a specific ask in the original prompt) was lost because the original question never reached Stage 3. Stage 3 received only the Stage 2 analytical framework. The question's specific request for "citing any recent SEC commentary" had no path through the handoff schemas to reach the agent responsible for producing the final response.

**Procedural Correctness scored 0.000** — identical to baseline. The pipeline's structured handoffs stripped cognitive residue (as designed) but also stripped procedural details that the monolithic Tier 2 prompt naturally preserved by having the question and the response in a single context. The handoff schema was designed for analytical content, not procedural requirements.

### What the pipeline gained

**Instruction Following scored 1.000** — the only tier to achieve this. The hard task's Turn 2 specified "paragraph form without headers, bullet points, lists, charts." Both baseline and Tier 2 failed this formatting instruction. The pipeline's Stage 3 advisory agent, operating in a clean context with an explicit advisory epistemic stance and no analytical work to perform, followed the format instruction perfectly. It had cognitive space for compliance that the other tiers spent on analysis.

**Supplemental Insight scored 1.000** — matching Tier 2 and dramatically outperforming the 0.467 baseline. The discovery stage surfaced considerations beyond the direct question that the baseline's convergent mode suppressed. This is the pipeline working as predicted: open investigation without advisory pressure finds things that pre-filtered investigation misses.

### The diagnosis

The pipeline was "overcooked" for this task. It added architectural complexity that introduced more information loss than the mode separation benefits were worth. The handoff schemas were designed for analytical structure, not procedural fidelity. Details that naturally survive in a single context — because the model can see both the question and its response — were squeezed out by the compression that makes handoffs cognitively clean.

This is a genuine trade-off, not a design flaw. Stripping cognitive residue and stripping procedural detail use the same mechanism: structured compression. You cannot have one without risking the other. The question is whether the cognitive benefit outweighs the information cost, and on this task, it did not.

---

## 6. What This Tells Us About When Pipelines Matter

### Cognitive hygiene (Tier 2) works broadly

Any complex analytical task benefits from epistemic stance intervention. "Explore before concluding" is a near-universal improvement for knowledge-based reasoning. The intervention is lightweight — a system prompt, not an architecture — with high impact (0.759 to 0.950 on PRBench's hard task). It works because it sets the highest level of the cognitive stack (epistemic stance), which cascades through mode, register, and language patterns without requiring structural changes.

This is the practical takeaway. If you are running a professional reasoning task through an LLM, a system prompt that sets an exploratory epistemic stance and creates a scope boundary between discovery and synthesis will likely improve output quality. You do not need a pipeline for this.

### Pipelines work specifically

Pipelines earn their cost when all of these conditions are met:

1. **The model must investigate external data it has not seen before** — not reason from training knowledge. The investigation stage's value is protecting genuinely open discovery from evaluative pre-filtering. When the model is recalling knowledge (as in PRBench), the investigation is less susceptible to pre-filtering because the model already "knows" the domain.

2. **Data volume exceeds what one context can hold.** If everything fits in one context, the pipeline's compression at handoff boundaries loses information without the compensating benefit of making large datasets tractable.

3. **The investigation + evaluation toxic pair operates on discovered information** — patterns in specific data, not general knowledge. When the model discovers something unexpected in real data (the naming-families pattern in the CA pipeline), evaluative pre-filtering would have prevented that discovery. When it is applying known legal frameworks to a described scenario, the pre-filtering is less damaging because the frameworks are already in training data.

4. **The pipeline runs repeatedly**, amortizing the design cost of the handoff schemas. A one-off pipeline analysis does not justify the effort of designing schemas, testing handoffs, and iterating on information loss.

5. **The task requires what we are calling "adaptive expertise"** — building novel understanding from unfamiliar data, not applying known frameworks to described scenarios.

### Pipelines do not help when

1. The task is knowledge-based reasoning, however complex. The model is recalling and organizing knowledge, not discovering patterns in data it has never seen.

2. The question is answerable in one thorough pass. No data volume problem, no context overflow.

3. Procedural details matter and might not map to handoff schema fields. The compression that strips cognitive residue also strips anything that does not fit the schema.

4. The pipeline is a one-off. The design cost is not amortized.

The CA policy pipeline — the original project that motivated this research — hit all the pipeline-favoring conditions: 50+ real Conditional Access policies to investigate, data that could not fit in one context, the investigation + evaluation toxic pair operating on genuinely unfamiliar policy data, repeated execution across tenants. PRBench hit none of them.

---

## 7. The Deeper Question We Cannot Yet Name

There is something we are circling that we have not fully articulated. The distinction seems to be between two types of expertise:

**Routine expertise.** Applying domain knowledge to answer questions. The model already "knows" the domain. Better prompting (Tier 2) helps it organize that knowledge more effectively — set a better epistemic stance, create scope boundaries, elevate uncertainty. The knowledge is in training data. The task is deploying it well. PRBench tests this. Most benchmarks test this. The model is good at this, and getting better.

**Adaptive expertise.** Walking into an unfamiliar situation with domain knowledge and building novel understanding from what you find there. The model must discover patterns it could not predict from training data. This is the work of a professional who encounters a new environment — a systems engineer troubleshooting a novel outage, a consultant assessing a new client's infrastructure, a lawyer reviewing a specific contract they have never seen before, a security analyst examining an organization's actual policy configuration. The patterns emerge from the data, not from training.

The pipeline's value is protecting the adaptive expertise process — specifically, the investigation stage where the model discovers patterns in unfamiliar data. Without mode separation, evaluation pre-filters investigation, and the model only finds things it can already classify. The naming-families discovery in the CA pipeline is the canonical example: no checklist predicted it, no training data contained it, it emerged from genuinely open investigation of specific data.

This distinction — routine versus adaptive expertise — may be the sharper version of our thesis. The original claim ("monolithic prompts are fundamentally flawed for complex tasks") was too broad. The refined claim is something like: monolithic prompts without cognitive hygiene are flawed for all complex reasoning; with cognitive hygiene they handle routine expertise well; pipelines are specifically needed for adaptive expertise, where the model must discover rather than recall.

### What we do not yet know

- Whether "adaptive expertise" is the right framing or whether there is a sharper concept we are missing.
- Whether the AI research community is working on this distinction. Initial survey suggests not — everyone is benchmarking routine expertise because it is measurable. Adaptive expertise requires providing novel data for the model to investigate, not questions for the model to answer from knowledge.
- Whether we can build a benchmark that tests adaptive expertise. It would need to provide genuinely unfamiliar data (documents, configurations, datasets the model has not seen in training) and evaluate the quality of pattern discovery, not answer correctness.
- Whether the pipeline findings from the CA project generalize across domains or are specific to security policy analysis.
- Whether there is a spectrum between routine and adaptive expertise, and where on that spectrum the pipeline becomes worth its cost.
- Whether stronger future models will make pipelines unnecessary even for adaptive expertise. The decomposition literature (arXiv:2506.06843) finds that pipeline advantages diminish as models improve. If a sufficiently capable model can sustain open investigation even with evaluative pressure in the context, the architectural separation becomes unnecessary.

---

## 8. What the B-Series Proved and What It Did Not

### Proved

**Cognitive hygiene significantly improves professional reasoning on external benchmarks.** The Tier 2 epistemic stance intervention produced a 0.759 to 0.950 improvement on PRBench's hard task (25/26 criteria met, up from 20/26). This is a substantial, externally-validated result on a benchmark we did not design, scored against rubrics created by 182 domain experts.

**Convergent accuracy is unaffected by prompt architecture.** Legal Accuracy scored 1.000 across all three tiers. All B1 coding tasks passed at baseline. Convergent, knowledge-based reasoning is not degraded by mode mixing — the model compensates when the answer is clear. This confirms B1's finding at the category level.

**The active ingredient is epistemic stance, not pipeline architecture.** The Tier 2 intervention operated at the highest level of the cognitive stack. The pipeline operated at the architectural level. The higher-level intervention produced better results. This is consistent with the cognitive stack model: higher interventions cascade further.

**Easy tasks are saturated across all tiers.** The easy finance task scored 16/16 (1.000) for baseline, Tier 2, and pipeline. All B1 tasks passed at baseline. Prompt architecture improvements only manifest on genuinely difficult tasks. If the model already gets it right, there is nothing for better prompting to improve.

### Did not prove

**That pipeline separation produces a qualitative leap beyond Tier 2.** This was the core prediction, and it failed. The pipeline scored 0.849 — better than baseline (0.759) but worse than Tier 2 (0.950). On this benchmark, the pipeline was not worth its architectural cost.

**That pipeline architecture is necessary for complex analytical judgment.** Tier 2 was sufficient. A single system prompt with the right epistemic stance outperformed a three-stage pipeline with structured handoffs.

**Our specific category-level predictions.** We predicted Handling Uncertainty and Practical Utility would improve under the pipeline. They did not — both scored 0.762 and 0.632 respectively, matching baseline. We predicted Instruction Following would be unchanged. It was the pipeline's strongest category (1.000, the only tier to achieve it). The theory's predictive power at the category level was poor on this task.

### Reframed

The thesis narrows. The original claim — "monolithic prompts are fundamentally flawed for complex tasks" — is too broad. The evidence now supports a more specific version:

- **Monolithic prompts without cognitive hygiene** are flawed for complex reasoning. Epistemic stance intervention produces large, measurable improvements.
- **Monolithic prompts with cognitive hygiene** are surprisingly effective for knowledge-based reasoning, even on difficult professional judgment tasks.
- **Pipelines are specifically needed** for data-intensive adaptive expertise — tasks where the model must investigate genuinely unfamiliar data and discover patterns it could not predict from training.

The original CA pipeline results remain the strongest evidence for the pipeline thesis, precisely because that use case (real data, genuine investigation, pattern discovery across a large dataset) is what pipelines are for.

---

## 9. Methodology Notes

**Model.** Claude Opus 4.6 for all generation (baseline, Tier 2, and all pipeline stages). Same model across tiers — the comparison tests prompt architecture, not model capability.

**Judge.** Claude Sonnet 4.6. PRBench validated their judge protocol with o4-mini, which achieved 80.2% agreement with human experts (compared to 79.6% human-human agreement). We used Sonnet instead of o4-mini. The judge choice should not substantially affect results on binary per-criterion scoring against specific expert-written criteria, but we note the difference.

**Rubrics.** PRBench's own expert-created criteria. 16 criteria for the easy task (finance), 26 for the hard task (legal). Criteria authored by domain professionals with JD or CFA qualifications and 6+ years of experience. We did not create or modify the rubrics.

**Single run per tier.** This is a directional study, not a statistically powered one. Each tier ran once per task. PRBench's granularity (26 binary criteria per task on the hard task) provides internal measurement points, but this is not a substitute for multiple runs. The findings are directional, not definitive.

**Self-preference risk.** Claude (Opus) generated the outputs and Claude (Sonnet) judged them. This creates a potential self-preference bias. Mitigated by binary per-criterion scoring against specific expert-written criteria — the judge is not rating holistic quality but checking whether specific factual and analytical requirements are met. Noted as a limitation regardless.

**Pipeline v0.1.** The pipeline handoff schemas were designed once and not iterated. The information loss we documented (criteria 17-19, criterion 26) might be addressable through schema refinement. But that iteration cost is itself part of the argument for Tier 2's practicality — a system prompt that works on the first attempt versus a pipeline that requires schema debugging.

---

## 10. What to Do Next

**Update `research-foundations.md` with the refined thesis.** The evidence now supports a three-part claim: cognitive hygiene works broadly; pipelines work for adaptive expertise specifically; convergent accuracy is unaffected by prompt architecture. The original framing ("monolithic prompts are fundamentally flawed") needs to be narrowed.

**Consider testing Tier 2 interventions on a larger PRBench sample.** Two tasks is a directional probe. Running Tier 2 against 20-50 PRBench tasks across law and finance would provide statistical power for the cognitive hygiene finding, which is currently the strongest practical result.

**Investigate the adaptive expertise concept.** Is this a known construct in AI research? Is anyone working on enabling it? The routine/adaptive distinction may be the high-value theoretical contribution — it explains both when pipelines help and when they do not.

**Consider building an adaptive expertise benchmark.** This would require providing genuinely novel data (documents, configurations, datasets) for the model to investigate, then evaluating pattern discovery quality. Existing benchmarks test recall and reasoning over known domains. A benchmark that tests discovery in unfamiliar data would test something no existing benchmark captures.

**Investigate whether pipeline information loss can be reduced.** The handoff schema lost procedural details and specific question requests. Can schemas be designed to preserve these without reintroducing cognitive residue? Or is there a fundamental trade-off between cognitive cleanliness and information fidelity that cannot be resolved?

**Test model dependence.** The A-series cross-model testing found that pipeline benefits were model-dependent — strong models benefited from pipelines, weaker models were harmed by them. Running B2 on a different frontier model would test whether the Tier 2 finding (cognitive hygiene works) is model-general while the pipeline finding (overcooked for this task) is specific to Opus.

**Try the pipeline on a genuine adaptive expertise task.** The CA pipeline is the strongest evidence for pipelines, but it is a single domain. Running the three-tier framework on a task that requires investigating genuinely unfamiliar data — a novel codebase, an unseen contract, an unfamiliar regulatory filing — would test whether the pipeline thesis holds outside security policy analysis.
