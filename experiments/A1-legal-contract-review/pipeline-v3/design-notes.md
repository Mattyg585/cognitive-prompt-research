# Pipeline Design Notes: Contract Review — v3

## What Changed from the Prior Pipeline

The v3 architect analysis sharpened the theoretical grounding in two ways, and identified one structural gap the prior pipeline left open. This v3 pipeline addresses all three.

### 1. The RPD decision architecture switch — stated more precisely

The prior pipeline's design notes described the core contamination as "evaluation criteria pre-filter investigation." The v3 analysis names the mechanism more precisely: when evaluation criteria are present during investigation, the decision architecture switches from recognition-primed to criterion-referenced. This is not simple overload or distraction — it is a qualitatively different processing mode. Klein's RPD model identifies this as the difference between Variation 2/3 (novel situation, deliberate situation modeling required) and criterion-referenced checking (which criteria are met?).

This precision matters for the Contract Auditor's prompt design: the agent's instructions should not just say "don't evaluate yet" — they should establish the recognition-primed posture explicitly. The Auditor is doing deliberate situation modeling. The v3 Contract Auditor prompt names this directly and explains why the evaluation criteria are absent.

### 2. Proactive interference — named as an architectural problem, not an instruction problem

The v3 analysis cites the 2025 research on proactive interference in LLMs: retrieval accuracy declines log-linearly as interference from earlier context accumulates, and natural-language instructions to "set aside" prior context yield only marginal improvement. This matters because it makes explicit why Tier 2 scope boundaries cannot fully solve the problem: it is a structural working-memory limitation, not a compliance problem.

The pipeline's architecture already solves this (each agent has a fresh context), but the v3 handoff specifications are more explicit about what to drop and why: not just "this would contaminate the tone" but "accumulated residue from prior stages is actively interfering with the processing of this stage's task, and instructions cannot remediate it."

### 3. The handoff format as cognitive boundary

The v3 analysis notes that the handoff format is the cognitive boundary — structured data strips cognitive mode; prose carries it. The prior pipeline's handoff spec said this, but the agent prompts themselves didn't specify the format of what they produce with sufficient precision. The v3 agent prompts include explicit output format templates, with structural sections that compress the investigation into the form the evaluation stage needs, and compress the evaluation into the form the synthesis stage needs. The compression is part of the cognitive design, not just a usability consideration.

---

## Pipeline Overview

Three agents, sequential execution, designed around the specific interference mechanisms identified in the v3 analysis.

```
Contract Auditor → Playbook Evaluator → Negotiation Strategist
```

The Redline Writer from the prior pipeline (four agents) is folded into the Playbook Evaluator in v3. The reason: the v3 analysis recommends the split at "investigation → evaluation + redline generation → negotiation synthesis." The evaluation and redline generation stages share a cognitive posture (convergent, criterion-referenced, with specific outputs for each deviation) and the evaluative residue problem that motivated separating them in v4 is less severe than the investigation-evaluation or synthesis-contamination problems. Three agents is the minimum that addresses the core interference mechanisms.

The decision to fold Redline Writer back into Playbook Evaluator is a judgment call with a testable implication: if redlines from this pipeline read as generic "standard market position" boilerplate rather than deal-calibrated language, the evaluation + generation fusion is affecting quality and the prior four-agent structure should be preferred. If redlines are commercially calibrated, three agents is sufficient.

---

## Agent Map

| Agent | Cognitive Mode | Receives | Produces | Why Separate |
|-------|---------------|----------|----------|-------------|
| **Contract Auditor** | Investigation — recognition-primed, deliberate situation modeling | Contract text, user's side, contract type (no playbook, no business context) | Structured clause observations with commercial logic characterisation, unusual provisions, notable absences, material clause interactions | RPD decision architecture switch: evaluation criteria present during investigation shift the mode from recognition-primed to criterion-referenced. Investigation must run in clean context — no playbook, no evaluation framework, no business context that would bias what gets surfaced. |
| **Playbook Evaluator** | Evaluation + Generation — convergent, criterion-referenced; generative drafting calibrated to deal dynamics | Clause observations from Auditor + playbook + user's side + business context | Classified deviations with specific redline language, rationale, priority, and fallback | Evaluation is legitimate convergent work once investigation is complete. Seeds are appropriate here — the playbook's standards are the right framework for this stage. Business context routes here (not to investigation) to shape redline drafting without biasing what the Auditor discovered. |
| **Negotiation Strategist** | Synthesis + Reframing — whole-deal strategic reasoning | Deviation list + redline proposals + business context (no contract text, no investigation prose) | Negotiation strategy | Proactive interference: by the strategy stage, accumulated investigative, evaluative, and generative residue actively degrades strategic reasoning — the model restates classifications rather than reasoning about the deal. Clean context with compressed structured inputs enables genuine counterparty modeling and sequencing reasoning. |

---

## Why Three Agents, Not Four

The prior pipeline separated Redline Writer from Playbook Comparator on the grounds that evaluative posture constrains generation toward boilerplate. This is a real mechanism. The v3 analysis rates it as a medium-severity issue (investigation + generation fusion) compared to the high-severity investigation + evaluation fusion and the proactive interference problem at synthesis.

The judgment here is that a well-framed epistemic stance in the Evaluator's generation phase — combined with business context routed directly to the Evaluator rather than through the pipeline — should be sufficient to produce deal-calibrated redlines without requiring a separate agent. The test is whether the redlines that emerge are shaped by deal dynamics or default to standard market language.

If the experiment shows that Evaluator redlines are still generic despite the deal-context routing, the four-agent structure should be restored. The experiment design should test for this specifically.

---

## Execution Order

Sequential, because each agent depends on the prior agent's full output.

The Negotiation Strategist could theoretically run with only the deviation list (before redlines are generated), but it produces better strategy when it knows what specific redlines are being proposed — the specific asks shape sequencing advice, trade-off recommendations, and package deal suggestions.

For batch processing across multiple contracts, the full pipeline can be parallelised across contracts while remaining sequential within each contract.

---

## Handoff Design

### Handoff 1: Contract Auditor → Playbook Evaluator

**What crosses**: Structured clause observations — what each provision says, key quoted language, specific terms and thresholds, clause interactions, unusual provisions, notable absences, the Auditor's characterisation of the deal's commercial logic.

**Format**: Structured sections by topic. Factual and descriptive. Key contractual language quoted directly — the Evaluator needs exact wording to evaluate against playbook positions and to produce accurate redline current-language quotes.

**What gets dropped**: Exploratory threading, investigative asides ("this is interesting because..."), tentative interpretations that didn't resolve. The exploration enabled discovery; it should not persist into evaluation. Exploratory prose in the handoff would bias the Evaluator toward continued investigation rather than systematic measurement.

**Critical**: The Auditor's output must be in structured form — not free prose. Structured output strips the investigative cognitive mode before it enters the Evaluator's context. If the Auditor produces prose and it enters the Evaluator raw, the Evaluator will be pulled toward investigative register regardless of its own evaluation-oriented prompt.

### Handoff 2: Playbook Evaluator → Negotiation Strategist

**What crosses**: Classified deviations (classification, playbook standard, specific gap, key quoted language) plus redline proposals (proposed language, priority, fallback). Also passes: business context from the user (not through the pipeline — routed directly to the Strategist).

**Format**: Structured list of deviations and redlines. Each entry contains enough information for strategic reasoning; the Strategist does not need the contract text or the investigation prose.

**What gets dropped**: Evaluative reasoning narratives, risk exposure calculations, the classification rationale. The classification results cross; the reasoning behind them does not. The generation reasoning (alternative drafts considered, clause-interaction concerns addressed in drafting) also does not cross. Accumulated evaluative and generative residue is the specific mechanism that produces strategy-flavoured deviation lists rather than genuine strategic reasoning.

**Critical**: The Strategist works from compressed, structured data — no contract text, no investigation output, no evaluative prose. This is not a limitation; the compression is what allows it to hold the whole deal in view at once rather than being anchored to any single clause.

---

## Business Context Routing

Before running the pipeline, gather from the user:
1. The contract (file, URL, or pasted text)
2. Which side they're on
3. Contract type (if not obvious)
4. Deadline, focus areas, deal context, relationship dynamics

Routing:
- Items 1–3 → Contract Auditor (interpretation context that shapes reading without biasing discovery)
- Items 1–3 + playbook → Playbook Evaluator
- Items 2–4 → Playbook Evaluator (business context shapes redline tone and deal-calibrated drafting)
- Items 2–4 → Negotiation Strategist (business context drives strategic reasoning)

The Auditor does **not** receive the full business context (deadline, strategic importance, focus areas). These would bias investigation — the Auditor should surface what's in the contract, not what the user is worried about. The user's side (item 2) and contract type (item 3) are interpretation context, not evaluative bias: knowing the user is the customer shapes which side of a mutual provision matters, but doesn't pre-filter what provisions exist.

---

## Context Window Notes

- **Contract Auditor**: For very long contracts (50+ pages), run multiple Auditor instances on contract sections with a lightweight merge step. Most contracts (under 30 pages) fit in a single pass.
- **Playbook Evaluator**: Receives compressed clause observations (substantially smaller than raw contract) plus playbook. Also receives the original contract text for quoting. Volume is manageable in all but the most extreme cases.
- **Negotiation Strategist**: Receives only structured deviation list, redline proposals, and business context. The lightest context load of all agents. No capacity concerns.

---

## Theoretical Grounding

### Why the Auditor is the critical stage

Every quality difference between the monolithic prompt and this pipeline originates in the Auditor stage. If the Auditor produces richer findings than the monolithic prompt's investigation phase — specifically, findings that don't map to the standard category checklist — then the downstream stages can evaluate and strategise over those richer findings. The pipeline's quality ceiling is the Auditor's discovery breadth.

The Auditor stage enables this by giving the model what recognition-primed investigation requires: a context free from evaluation criteria, with an epistemic stance that frames the task as deliberate situation modeling. The model is not checking categories — it is building a mental model of what this deal is and how it works. The findings that emerge from that process include clause interactions, unusual constructions, and structural features of the risk allocation that criterion-referenced checking would not surface.

### Proactive interference as the structural justification

The pipeline's value is not just separation — it is the structural elimination of proactive interference. Within a monolithic context, every prior stage's output accumulates. By the strategy stage, the model is reasoning through the cognitive residue of investigation, evaluation, and generation simultaneously. Earlier content is not just occupying space; it is actively interfering with the processing of the strategic reasoning task.

Pipeline isolation solves this architecturally. The Negotiation Strategist's context contains only the deviation list, the redline proposals, and the business context. The accumulated residue of clause-by-clause investigation, playbook comparison, and redline drafting is absent. The Strategist can reason about the deal, not through a slurry of prior stages' outputs.

This is the specific mechanism that makes Tier 3 valuable beyond what Tier 2 can achieve with epistemic stance and scope boundaries. Tier 2 improves the margins; Tier 3 changes the architecture. The experiment tests whether the architectural change produces measurable quality differences in investigation breadth, redline calibration, and strategic depth.

---

## What This Tests

The experiment's hypothesis: the monolithic prompt is the ceiling, not the floor.

The pipeline should produce measurably different output in three dimensions:
- **Investigation breadth**: Does the Auditor surface provisions outside the standard categories that the monolithic version misses? Specifically: unusual provisions, clause interactions, and structural features of the risk allocation that don't correspond to the "common issues" bullets.
- **Redline calibration**: Are redlines shaped by deal dynamics rather than defaulting to standard market position language?
- **Strategic depth**: Does the Strategist model the counterparty and reason about sequencing, leverage, and concession strategy? Or does it restate the deviation classifications?

If Tier 2 (v3) improves incrementally and Tier 3 produces a qualitative leap on any of these dimensions, the finding supports the core thesis.
