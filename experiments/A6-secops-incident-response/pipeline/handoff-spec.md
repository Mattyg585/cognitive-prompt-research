# Pipeline Specification: Incident Postmortem

## Pipeline Overview

Produces a blameless postmortem for a resolved incident by separating timeline reconstruction, causal analysis, response evaluation, action item generation, and synthesis into five agents with compressed handoffs between each stage.

## Why a Pipeline

The original monolithic postmortem template forces six types of thinking into one context and one pass:

1. **Investigation + Structuring** — reconstruct the timeline
2. **Deep Investigation** — trace causal chains
3. **Evaluation** — judge the incident response
4. **Generation** — produce action items
5. **Synthesis** — compose lessons learned and summary

The core interference: the evaluation sections (What Went Well / What Went Poorly) are in context while the model investigates root causes, making evaluation a pre-filter on causal analysis. The model identifies causes that are evaluable — things someone did wrong or right — and filters out systemic causes that don't fit the evaluation frame. Simultaneously, the action items section shapes causal analysis toward causes with neat fixes, softening architectural or organisational findings that don't produce actionable items.

The 5 Whys template compounds this by constraining causal reasoning to exactly five levels in a linear chain, when real incidents have causal trees that may be shallower, deeper, or branching.

Tier 2 removes the 5 Whys anchor, reframes the blameless directive, and adds scope boundaries. This improves the margins but can't eliminate the core interference — investigation, evaluation, and generation still share a context. The pipeline separates them into clean contexts with compressed handoffs.

## Agent Map

| Agent | Thinking Type | Receives | Produces | Why Separate |
|-------|--------------|----------|----------|-------------|
| **Timeline Reconstructor** | Investigation + Structuring | Incident data, logs, events | Structured annotated timeline | Timeline reconstruction must document what happened without causal or evaluative contamination — pure chronological investigation |
| **Causal Analyst** | Deep Investigation + Synthesis | Structured timeline | Causal analysis with evidence | Causal investigation without evaluation or fix-generation in context allows following threads to uncomfortable conclusions — architectural flaws, organisational blind spots, systemic vulnerabilities that don't have simple fixes |
| **Response Evaluator** | Evaluation | Structured timeline + causal analysis | Structured response evaluation | Evaluation in its own context can be thorough without contaminating investigation. It receives already-investigated material and evaluates it, rather than simultaneously investigating and judging |
| **Action Item Generator** | Generation + light Evaluation | Causal analysis + response evaluation | Owned, prioritised action items | Generation works best when it receives fully investigated and evaluated input. The generator designs interventions based on clear findings, not during investigation |
| **Postmortem Synthesiser** | Synthesis + Reframing | All outputs from Agents 1-4 | Final postmortem document | Synthesis is the last step. It receives all structured material and compresses it into a coherent narrative without needing to investigate, evaluate, or generate |

## Execution Order

```
Timeline Reconstructor → Causal Analyst → Response Evaluator → Action Item Generator → Postmortem Synthesiser
```

Sequential, because each agent depends on the previous agents' output.

**Rationale for sequential**: The Response Evaluator could theoretically start as soon as the Timeline Reconstructor finishes (it doesn't strictly need the Causal Analyst's output). But the causal analysis enriches the response evaluation — understanding *why* things happened makes it possible to evaluate whether the response addressed the right problems. The sequential ordering produces better evaluation.

The Action Item Generator could theoretically run in parallel with the Postmortem Synthesiser. But the Synthesiser produces better lessons learned when it can reference the specific action items — the gap between what happened and what's being done about it is itself a lesson. Sequential is worth the extra step.

## Handoff Specifications

### Handoff 1: Timeline Reconstructor → Causal Analyst

**What crosses**: Structured timeline — events in chronological order, decisions made, information available at each decision point, information that was missing, actions taken, and gaps in the observable record.

**Format**: Structured chronological entries. Each entry: timestamp, event, what was known at this point, what was decided, what information was missing. Factual, descriptive tone.

**What gets dropped**: Investigative reasoning ("this is interesting because..."), exploratory threads that didn't resolve, the reconstructor's analytical journey. The timeline's exploratory framing would bias the causal analyst toward continued investigation of the timeline rather than independent causal reasoning.

### Handoff 2: Timeline Reconstructor → Response Evaluator

**What crosses**: Same structured timeline as Handoff 1.

**Format**: Identical to Handoff 1. The Response Evaluator needs the same factual chronology — it evaluates the response against what actually happened and what was known at each point.

### Handoff 3: Causal Analyst → Response Evaluator

**What crosses**: Causal analysis — root causes with evidence chains, contributing factors, systemic vulnerabilities, causal structure description.

**Format**: Structured findings. Each root cause or contributing factor: what it is, evidence from the timeline, how it contributed, whether it's proximate or systemic. The causal structure (linear, branching, circular) described explicitly.

**What gets dropped**: Deep investigative reasoning, the analyst's thread-following process, tentative hypotheses that were explored and abandoned. The evaluation agent needs the findings, not the investigative journey. Investigative prose would push the evaluator toward continued investigation rather than focused evaluation.

### Handoff 4: Causal Analyst → Action Item Generator

**What crosses**: Same causal analysis as Handoff 3.

**Format**: Identical structured findings. The Action Item Generator needs to understand what caused the incident to design interventions that match cause depth.

### Handoff 5: Response Evaluator → Action Item Generator

**What crosses**: Structured response evaluation — what worked, what didn't, where detection, communication, or mitigation fell short, with specific evidence from the timeline.

**Format**: Structured evaluation entries. Each finding: what aspect of the response, what happened, evidence from timeline, whether it worked or not. No investigative prose — just the evaluated findings.

**What gets dropped**: Evaluative reasoning process, comparative analysis, any remaining investigative threads. The generator needs the conclusions to design fixes, not the evaluation process itself. Evaluative residue would constrain generation toward obvious fixes rather than systemic interventions.

### Handoff 6: All Agents → Postmortem Synthesiser

**What crosses**: All four structured outputs — timeline, causal analysis, response evaluation, and action items.

**Format**: Each agent's output in its structured format. The Synthesiser receives the complete set and composes the final document.

**What gets dropped**: Nothing at this stage. The Synthesiser is the integration point — it needs all the material to compose a coherent postmortem. The material is already compressed through the structured handoff formats.

## Context Window Notes

- **Timeline Reconstructor**: Context pressure depends on the volume of incident data (logs, event records, communications). Most incidents fit comfortably. For very long-running incidents with extensive logs, pre-process the logs to extract key events before passing to the Reconstructor.
- **Causal Analyst**: Receives the compressed timeline (substantially smaller than raw incident data). Manageable in all cases.
- **Response Evaluator**: Receives the compressed timeline plus the compressed causal analysis. Combined volume is moderate. No capacity concerns.
- **Action Item Generator**: Receives causal analysis plus response evaluation — two structured documents. The lightest context load aside from the Synthesiser's structured inputs.
- **Postmortem Synthesiser**: Receives all four outputs. This is the heaviest context load in the pipeline, but all inputs are structured and compressed. For typical incidents, well within capacity.

---

## Mapping: Architect Findings → Pipeline Design

| Architect Finding | Pipeline Response |
|---|---|
| **"5 Whys" double anchor** (numeric + structural) — forces exactly 5 levels in a linear chain | Eliminated entirely. The Causal Analyst follows evidence to natural depth with no numeric or structural constraints. Uses lenses ("What made this possible? What made it invisible?"), not a template. |
| **Postmortem template is a four-mode collision** — six thinking types in one template | Separated into five agents, each scoped to one or two compatible thinking types. No agent does investigation and evaluation simultaneously. |
| **Evaluation contaminates investigation** — the model identifies evaluable causes, not systemic ones | Causal Analyst has no evaluation in its context. Response Evaluator runs separately, after causal analysis is complete. The causal findings are locked in before evaluation begins. |
| **Fix-generation shapes root cause analysis** — causes with neat action items are preferred | Action Item Generator receives completed causal analysis. The causes are identified before the generator considers what to do about them. Systemic causes that require long-term architectural change are preserved. |
| **Cross-phase template contamination** — status update framing in postmortem context | Pipeline agents receive only their specific inputs. No operational templates in the postmortem context. |
| **"Blameless" directive pre-filters investigation** — avoids human factors entirely | Each agent carries the reframed blameless posture: "examine human decisions through a systems lens." The Timeline Reconstructor documents what was known at each decision point. The Causal Analyst investigates why decisions seemed correct at the time. Human factors are investigated, not avoided. |
| **Synthesis during investigation** — premature narrative commitment | The Postmortem Synthesiser runs last. It composes the narrative after all investigation, analysis, evaluation, and action item generation are complete. No premature commitment. |

### What to Watch for When Testing

- **Causal depth and structure**: Does the Causal Analyst produce a branching causal analysis with systemic findings? Or a linear chain to an actionable root cause? The latter signals that evaluative or generative contamination leaked through the handoffs.
- **Human factors investigation**: Does the causal analysis examine why the developer chose `@Public`, why QA tested from an authenticated session, why the security scan checks only dependencies? Or does it stop at surface-level descriptions of what happened? The former requires the blameless reframe to be working.
- **Response evaluation specificity**: Does the Response Evaluator link each finding to specific moments in the timeline? Or does it produce generic evaluations ("communication was good")? Specific evidence linking signals clean evaluation.
- **Action item depth matching**: Do systemic causes (architectural vulnerabilities, organisational blind spots) get systemic action items (design changes, process restructuring)? Or do they get surface-level patches ("add a check")? The Action Item Generator should match fix depth to cause depth.
- **Natural variation**: Run on incidents of different complexity. A simple configuration error and a complex cascading failure should produce very different causal analysis depths and action item counts. Uniform output signals anchoring.
- **Lessons learned depth**: Does the Synthesiser produce insights that go beyond restating the action items? Lessons should reveal something about the system that wasn't visible before the incident — not just summarise what went wrong and what's being done.
