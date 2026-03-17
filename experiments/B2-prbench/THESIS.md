# B2-PRBench: Pre-Registration Thesis

**Written**: 17 March 2026
**Status**: Pre-registration. Predictions documented before any tier runs.

---

## 1. The Claim

Cognitive mode separation — implemented via trust chain pipeline architecture with epistemic stance interventions and structured handoffs — improves complex analytical judgment quality. The improvement is measurable on externally-scored professional reasoning tasks.

This claim rests on three connected mechanisms from the cognitive prompt research framework:

**The cognitive stack.** Language patterns in a prompt are shaped by layers: epistemic stance ("I'm discovering" vs "I know") cascades through intent, expertise, cognitive mode, register, and language patterns down to the tokens the model processes. Higher-layer interventions cascade further. Setting an epistemic stance reshapes everything below it. Setting a task ("investigate this") leaves the higher layers unset, and the model fills them from whatever is already in the context.

**The trust chain.** In a multi-stage pipeline, each stage's cognitive quality cascades to downstream stages. If Stage 1 uses evaluative language ("finding", "critical"), Stage 2 inherits that evaluative framing regardless of its own prompt. Structured handoffs — schema-bound, compressed — strip cognitive residue. The schema IS the cognitive boundary. Designing the handoff is designing the trust chain.

**Mode interference.** Professional reasoning tasks require multiple conflicting cognitive modes simultaneously: investigation (what's here?), analysis (what does it mean?), evaluation (how does it measure up?), synthesis (what's the narrative?), reframing (what does the client need to hear?). Investigation + evaluation is the classic toxic pair — the model pre-filters, only finding things it can already classify. When these modes share a context, convergent patterns dominate and divergent potential is suppressed. The output looks competent. The gap only appears when you split and compare.

The cognitive load literature provides independent mechanistic support. Context saturation (ICE, arXiv:2509.19517) and proactive interference (PI-LLM, arXiv:2506.08184) describe the same phenomenon in ML vocabulary. A 2025 paper found that when combined load exceeds a "fragility tipping point," LLMs transition from successful reasoning to catastrophic failure — not gradual degradation, but a cliff. The multi-agent decomposition literature (arXiv:2506.06843) finds that distributing cognitive load through agent specialisation improves performance on complex, multi-faceted tasks.

Our specific claim: a trust chain pipeline with explicit epistemic stances at each stage will outperform a monolithic zero-shot prompt on PRBench's professional reasoning tasks, and the improvement will be concentrated in the rubric categories that require cognitive modes incompatible with domain accuracy.

---

## 2. Why PRBench

PRBench is the single most relevant external benchmark for this research. It tests exactly what we care about — complex analytical judgment — with evaluation infrastructure we did not create and cannot bias.

**Scale and rigour.** 1,100 expert-created professional reasoning tasks across law and finance. Rubric criteria authored by 182 domain experts (JD holders, CFAs, 6+ years experience). Tasks span 114 countries and 47 US jurisdictions.

**External rubrics.** 11 rubric categories spanning different cognitive modes — from domain accuracy (convergent) to supplemental insight (divergent) to handling uncertainty (epistemic). The rubrics were created by domain experts for domain evaluation, not by us for our theory. If our predictions about which categories improve turn out to be correct, the result is more credible precisely because we did not design the rubric.

**Validated judging.** PRBench's LLM judge (o4-mini) achieves 80.2% agreement with human experts, compared to 79.6% human-human agreement. The judge is at least as reliable as adding another human expert to the panel.

**Substantial headroom.** Top models (GPT-5 Pro) score only 0.51 on finance and 0.50 on legal. On the Hard subset: 0.39 and 0.37. Models are not close to ceiling on these tasks. There is room for prompt architecture to make a difference.

**PRBench documents our phenomenon.** From the paper: "models frequently reach correct conclusions through incomplete or opaque reasoning." This is "good output hides great output" in benchmark language. Models can get the answer right while getting the process wrong. PRBench's multi-category rubric captures this distinction — a response can score well on accuracy and poorly on transparency, or well on instruction following and poorly on supplemental insight.

**Category-level scoring reveals mode-specific performance.** PRBench reports scores per rubric category. This lets us test not just "does the pipeline help?" but "does the pipeline help on the specific categories our theory predicts?" A monolithic improvement would be interesting. A targeted improvement on mode-interference-sensitive categories would be evidence for the mechanism, not just the effect.

---

## 3. The Three Tiers

### Tier 1: Baseline (Zero-shot)

Give the model the task question with a minimal system prompt. No cognitive scaffolding, no mode-awareness instructions, no pipeline. This is how most people use LLMs for professional reasoning — paste the question, get the answer.

The baseline establishes what the model produces when prompt architecture is not a variable. Any improvement in Tier 2 or Tier 3 is attributable to prompt design, not model capability.

### Tier 2: Optimised (Cognitive Hygiene in a Single Prompt)

Same monolithic prompt, but with cognitive hygiene interventions:
- **Scope boundaries** — explicit instructions about what the model is and is not doing ("you are providing professional analysis, not a definitive legal opinion")
- **Mode awareness** — instructions to separate investigation from judgment ("first identify all relevant considerations, then evaluate their implications")
- **Epistemic stance setting** — language that sets the right relationship to knowledge ("explore the regulatory landscape" rather than "determine the correct answer")
- **Lens-based guidance** — structural prompts that open analytical space rather than seed specific conclusions

This tier tests whether you can improve output by fixing interference within a single context. It intervenes at the register and mode levels of the cognitive stack, without changing the architecture.

### Tier 3: Pipeline (Trust Chain Architecture)

Multiple stages with clean context boundaries and structured handoffs. Each stage has an explicit epistemic stance that cascades through the cognitive stack:

- **Stage 1 — Discovery** (epistemic stance: "I'm mapping what's here"). Identify the relevant legal/financial landscape, applicable rules, key facts, and open questions. Output is structured observations — not findings, not conclusions. The word "observation" matters: it sets an exploratory register that cascades through the entire stage.

- **Stage 2 — Analysis** (epistemic stance: "I'm understanding how these pieces connect"). Receive the structured observations. Analyse relationships, identify tensions, trace implications. Connect rules to facts. Surface what's ambiguous and what's clear. Output is a structured analytical framework — relationships and implications, not recommendations.

- **Stage 3 — Advisory synthesis** (epistemic stance: "I'm advising a professional who needs to act"). Receive the analytical framework. Synthesise into actionable professional guidance. Address uncertainty directly. Provide supplemental context the professional needs but didn't ask for. Reframe for the audience.

The schema between stages strips cognitive residue. Stage 2 receives structured observations, not Stage 1's exploratory prose. Stage 3 receives an analytical framework, not Stage 2's thread-following reasoning. Each stage starts clean.

This is the full cognitive stack intervention. It intervenes at the epistemic stance level (the highest layer), uses structured handoffs as cognitive boundaries, and gives each mode its own context. The pipeline's value is not that it does more work — it's that each stage does its work without the interference of incompatible modes in the context.

---

## 4. What We Predict

### Categories we expect to improve under pipeline separation

**Handling Uncertainty** (shared category, both tasks). Acknowledging what you don't know requires an epistemic stance that directly conflicts with the confident, authoritative mode that produces domain accuracy. In a monolithic prompt, the model is simultaneously trying to be knowledgeable and humble — "here's the definitive legal framework" and "but there's genuine ambiguity here" pull in opposite directions. The confident register dominates. In the pipeline, the discovery stage surfaces open questions without pressure to resolve them. The advisory stage inherits those flagged uncertainties and addresses them explicitly, because it received them as structured input rather than having to discover and acknowledge them while also being authoritative.

PRBench's own findings support this prediction: models universally struggle with "Handling Uncertainty." We predict this is partly a prompt architecture problem, not purely a model capability limitation.

**Supplemental Insight** (shared category, both tasks). Generating connections, implications, and considerations beyond the direct question requires divergent thinking — following threads to see where they lead, making lateral connections, identifying what the questioner needs but didn't ask for. This is suppressed when the model is simultaneously focused on accuracy. In a monolithic prompt, the model satisfices: it answers the question correctly and stops. In the pipeline, the discovery stage can follow threads freely (its job is to map the landscape, not answer the question), and the advisory stage can generate supplemental insight because it received a comprehensive analytical framework rather than having to build one from scratch while also being concise.

**Process Transparency & Auditability** (finance category, easy task). Showing your reasoning requires meta-cognitive reflection — stepping back from the analysis to describe what you did and why. This conflicts with the direct problem-solving mode that produces the analysis itself. The pipeline produces transparency as a structural byproduct: each stage's output IS the visible reasoning process. The discovery observations show what was identified. The analytical framework shows how it was connected. The advisory synthesis shows how conclusions were reached. Transparency doesn't require the model to do extra work — it emerges from the architecture.

**Practical Utility** (shared category, both tasks). Reframing analysis for the person who needs to act on it requires a shift from analytical mode to advisory mode — from "what is true" to "what should you do." In a monolithic prompt, the model often stays in analytical register throughout, producing technically correct but practically unhelpful output. The pipeline's third stage has a clean context with an explicit advisory epistemic stance. It receives structured analysis and reframes it for the professional, without the analytical register of the preceding work contaminating its advisory output.

**Application of Law to the Facts** (legal category, hard task). Bridging from legal rules to specific facts requires holding both in working memory and reasoning about their interaction. In a monolithic prompt, the model often mechanically inserts statutory citations without genuine application. In the pipeline, the discovery stage identifies both rules and facts. The analysis stage explicitly connects them — its job is to understand relationships, not to reach conclusions. The application is deeper because it happens in a stage dedicated to connection-making, not compressed into a paragraph of a comprehensive response.

### Categories we expect to be unchanged

**Legal/Financial Accuracy** (domain-specific, both tasks). Getting the law or finance right is convergent, fact-retrieval work. The model either knows the applicable rule or it doesn't. Pipeline separation doesn't add legal knowledge — it changes how that knowledge is deployed. We expect accuracy to be roughly equivalent across tiers. If anything, the pipeline's discovery stage might surface slightly more relevant law by exploring without the pressure to evaluate, but the effect should be modest.

**Instruction Following** (shared category, both tasks). Following the prompt's specific instructions (format, scope, focus areas) is procedural compliance. It's generally mode-compatible — you can follow instructions while doing any type of thinking. Pipeline separation shouldn't substantially affect this. The hard task's instruction to respond "in paragraph form without headers, bullet points, lists, charts" is a formatting constraint that applies equally to all tiers.

**Procedural Correctness** (legal category, medium and hard tasks). Getting procedures, filings, and process steps right is convergent work similar to accuracy. The pipeline shouldn't substantially change whether the model correctly identifies procedural requirements.

### The predicted pattern

If our theory is correct, the improvement pattern will show:
- A modest gap between Tier 1 and Tier 2 (cognitive hygiene within a single prompt helps, but the architecture is still the ceiling)
- A larger gap between Tier 2 and Tier 3 (pipeline separation produces a qualitative shift on mode-sensitive categories)
- The gap concentrated in Handling Uncertainty, Supplemental Insight, Process Transparency, and Practical Utility
- Little to no gap on Accuracy, Instruction Following, and Procedural Correctness

This is the signature of mode interference, not general capability improvement. If the pipeline improved everything equally, that would suggest we're just giving the model "more room to think" — a capacity explanation, not a cognitive mode explanation. If it improves specifically the categories that require modes incompatible with domain accuracy, that's evidence for the mechanism.

---

## 5. What Would Falsify This

**If Tier 3 does not outperform Tier 1 on overall mean_clipped score.** The pipeline adds complexity. If it doesn't improve aggregate quality, the cognitive mode thesis doesn't justify the architecture for professional reasoning tasks. This would be a clear negative result — not a "the effect is subtle" result.

**If Tier 3 improves accuracy categories rather than judgment/insight categories.** Our theory predicts that the pipeline helps most where mode interference is worst — the categories requiring divergent, epistemic, or meta-cognitive work. If the pipeline instead improves Legal Accuracy and Financial Accuracy while leaving Handling Uncertainty and Supplemental Insight unchanged, something other than mode separation is driving the improvement. Possibly the pipeline just gives the model more tokens to work with, producing more thorough responses that hit more accuracy criteria. That would be a capacity finding, not a cognitive mode finding.

**If Tier 2 matches or exceeds Tier 3.** This would mean pipeline separation isn't needed — cognitive hygiene within a single prompt captures the full benefit. The mode interference thesis specifically predicts that there's a ceiling on within-prompt optimisation that pipeline separation breaks through. If Tier 2 hits the same ceiling as Tier 3, the architecture doesn't matter, just the prompting technique. This would still be a useful finding (cognitive hygiene works!), but it would not support the pipeline thesis.

**If the improvement pattern doesn't match our predicted category breakdown.** We've made specific predictions about which categories improve (Handling Uncertainty, Supplemental Insight, Process Transparency, Practical Utility) and which don't (Accuracy, Instruction Following, Procedural Correctness). If the actual pattern is random — some predicted categories improve, some don't, some unpredicted ones do — the theory doesn't have predictive power. We're not just predicting "the pipeline helps." We're predicting where and why.

**If the easy task shows larger improvement than the hard task.** Mode interference should be worse on harder tasks that require more simultaneous cognitive modes. If the easy single-turn finance task shows a bigger pipeline benefit than the hard multi-turn legal task, the mechanism isn't mode interference — it's something else.

---

## 6. Methodology

### Tasks

Two tasks selected from PRBench, chosen to span difficulty and domain:

| | Easy | Hard |
|---|---|---|
| **Task ID** | f7ebc3860e344d78e2e801d6 | 5e55b0517dddde7548a4b66a |
| **Domain** | Finance | Legal |
| **Topic** | Market Microstructure, Trading & Liquidity | Regulatory & Administrative Law |
| **Turns** | 1 (single-turn) | 2 (multi-turn) |
| **Criteria** | 16 | 26 |
| **Categories** | 7 | 7 |

The easy task asks for a market microstructure comparison report with actionable recommendations — a single-turn finance question requiring investigation, analysis, synthesis, and advisory reframing. Sixteen criteria across seven categories.

The hard task involves a multi-turn legal analysis of tokenized asset platforms. The first turn covers exchange/broker definitions, digital asset custody, and structuring approaches under securities law. The second turn shifts to HSR reporting requirements for complex fund structures with convertible instruments. Twenty-six criteria across seven categories, weighted heavily toward critically important. The multi-turn structure adds complexity: the model must track context across turns, and the second turn explicitly requests "paragraph form without headers, bullet points, lists, charts" — a formatting constraint that forces prose-based reasoning.

A medium task (English property law tenant dispute, 24 criteria, 7 categories) is available but not included in the initial run. It can be added for validation if results are ambiguous.

### Model

- **Generation**: Claude Opus (for all three tiers)
- **Judging**: Claude Sonnet 4 against PRBench's original rubric criteria

### Judge Protocol

For each criterion in the rubric, present the model's response to Sonnet with the criterion description using PRBench's judge template. The judge returns `criteria_met: true/false` with an explanation. This matches PRBench's binary per-criterion grading approach.

PRBench validated with o4-mini as judge. We document the use of Sonnet and can re-run with o4-mini for cross-validation. The judge choice should not substantially affect results — PRBench showed judge agreement with humans exceeds human-human agreement regardless of specific model, as long as the model is frontier-class.

### Scoring

PRBench's formula:
1. Per-criterion: `criteria_met` -> 1 or 0
2. Weighted sum: `total_points = sum(grade * weight)` for all criteria
3. Clipped score: `score = total_points / sum(positive_weights)`, clipped to [0, 1]

The reported metric is **mean_clipped** — the mean of clipped scores across tasks.

Category-level scoring uses the same formula restricted to criteria within each category. This is what enables the predicted-category analysis.

### Runs

Each tier runs once per task in this initial test. This is a directional test, not a statistical study. If results are promising, we can add repetitions and the medium task for robustness.

Single runs are defensible here because PRBench's rubric is detailed (16-26 criteria per task) and the scoring is binary per-criterion. The granularity of the rubric provides internal replication — each criterion is an independent measurement point. A single run with 26 binary measurements per category is more informative than three runs with a single holistic score.

### Tier-specific protocols

**Tier 1 (Baseline)**: Minimal system prompt. The task question is presented as-is. No cognitive scaffolding.

**Tier 2 (Optimised)**: Single system prompt with cognitive hygiene. Specific interventions determined by architect analysis of the baseline, but guided by the mode interference patterns identified in Section 4.

**Tier 3 (Pipeline)**: Three stages (discovery, analysis, advisory), each in a completely separate session. Not `/clear` — separate session. Handoffs via structured schema (JSON or markdown with defined fields). The schema is designed to carry information without cognitive residue.

---

## 7. What This Doesn't Test

**Model capability.** We're testing prompt architecture, not Claude vs GPT. All tiers use the same model. If the pipeline helps, it helps because of the architecture, not because a different model answered.

**Whether the rubric is good.** PRBench's rubric was created by 182 domain experts and validated at 93.9% inter-expert agreement. We accept it as given. If the rubric has blind spots, those blind spots affect all three tiers equally.

**Whether creative work benefits.** Professional reasoning is analytical, not creative. The mode interference thesis predicts different dynamics for creative work, where tension between modes may be productive rather than destructive. This experiment does not test that boundary.

**Whether coding tasks benefit.** B1 (SWE-Bench) showed that coding tasks with deterministic pass/fail evaluation leave limited room for prompt architecture to help — the baseline already performs well on convergent, verifiable work. PRBench tests the other end: divergent, judgment-based work where the baseline demonstrably struggles.

**Statistical significance across the benchmark.** We're testing two tasks, not 1,100. This is a directional probe to determine whether the effect exists and whether it matches the predicted pattern. If it does, scaling to more tasks is the next step. If it doesn't, we've falsified the thesis with minimal wasted effort.

**Whether the pipeline is worth the cost.** Three stages cost roughly 3x the tokens and 3x the latency of a single prompt. Even if the pipeline produces better output, the practical question of whether the improvement justifies the cost is a deployment decision, not a research finding. We're testing whether the improvement exists, not whether it's economical.

---

## 8. Connection to B1 (SWE-Bench)

B1 tested the same three-tier framework on coding tasks (SWE-Bench). The core finding: on deterministic, convergent tasks where the baseline already performs well, prompt architecture has limited room to improve. SWE-Bench's pass/fail evaluation doesn't capture the nuances that mode separation is supposed to improve — either the bug is fixed or it isn't.

B2 is the complement. PRBench tests professional reasoning — open-ended, judgment-based, evaluated on a quality spectrum across multiple dimensions. This is where mode interference should matter most, and where PRBench's multi-category rubric should reveal the pattern that SWE-Bench's binary evaluation couldn't capture.

If B1 showed "pipeline doesn't help when the task is convergent and the evaluation is binary" and B2 shows "pipeline helps when the task requires multiple modes and the evaluation captures them separately," the two results together tell a coherent story about when and why cognitive mode separation matters.

---

## 9. What Success Looks Like

The strongest possible result:
- Tier 3 mean_clipped exceeds Tier 1 by a meaningful margin on both tasks
- The improvement is concentrated in Handling Uncertainty, Supplemental Insight, Process Transparency, and Practical Utility
- Accuracy and Instruction Following are roughly unchanged
- The hard task shows a larger pipeline benefit than the easy task
- Tier 2 shows partial improvement (cognitive hygiene helps, but the pipeline helps more)

A good result:
- Tier 3 outperforms Tier 1 on overall score
- The category pattern partially matches predictions (at least 2 of 4 predicted categories show improvement, accuracy doesn't improve more than judgment categories)

A negative result:
- Any of the falsification conditions in Section 5 are met

A negative result is still a result. If professional reasoning tasks on external benchmarks don't benefit from cognitive mode separation, that constrains the theory to the original domain (security policy analysis) and suggests the effect may be domain-specific rather than general. That's worth knowing.
