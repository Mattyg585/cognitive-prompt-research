# Pipeline Specification: Contract Review

## Pipeline Overview

Reviews a contract against an organization's negotiation playbook by separating investigation, evaluation, redline generation, and strategic synthesis into four agents with compressed handoffs between each stage.

## Why a Pipeline

The original monolithic prompt fuses four incompatible types of thinking into a single context:

1. **Investigation** — read and understand the contract
2. **Evaluation** — judge clauses against playbook criteria
3. **Generation** — write redline language for deviations
4. **Synthesis + Reframing** — craft negotiation strategy, model the counterparty

The core interference: the playbook's evaluation criteria (~120 lines of specific elements and named issues) are in context while the model reads the contract, making evaluation a pre-filter on investigation. The model reads *through* the framework, finding what matches the 12 categories and missing what doesn't. The mechanism is a decision architecture switch (Klein's RPD): evaluation criteria shift investigation from recognition-primed pattern discovery to criterion-referenced checking — a qualitatively different degradation, not just overload.

Downstream, accumulated evaluative and generative residue suppresses genuine strategic reasoning — the negotiation strategy restates the tier classifications rather than engaging in independent strategic thinking about the deal. This is proactive interference: earlier context actively degrades processing of later tasks, compounding as the context grows. By the final stage, the model is reasoning through the cognitive residue of every prior stage simultaneously.

Prompt-level fixes (scope boundaries, anchor removal, seed-to-lens conversion) improve the margins but can't eliminate either mechanism. Scope boundaries partially address attentional residue; they cannot address proactive interference, which is a structural working-memory limitation not remediated by instruction. The pipeline separates investigation and evaluation into clean contexts, eliminating the decision architecture switch, and gives each subsequent stage a fresh context free from accumulated residue.

## Agent Map

| Agent | Thinking Type | Receives | Produces | Why Separate |
|-------|--------------|----------|----------|-------------|
| **Contract Reader** | Investigation (knowledge-transformation) | Contract text, user's side, contract type | Structured clause summary with deal's commercial logic | Deliberate situation modeling — RPD Variation 2/3 task. Evaluation criteria in context switch decision architecture from recognition-primed to criterion-referenced, suppressing discovery of provisions outside the 12 standard categories |
| **Playbook Comparator** | Evaluation (pattern-matching against stable criteria) | Clause summary + playbook | Classified deviation list | Evaluation is legitimate convergent work here — stable regularities (playbook positions) + opportunity to learn them. Seeds are appropriate for convergent work. Must not carry investigative prose into context. |
| **Redline Writer** | Generation | Deviation list + contract text + business context | Redline proposals with rationale | Generation needs deal dynamics and generative epistemic stance — evaluative residue constrains drafting toward boilerplate "standard market position" language rather than language calibrated to the specific deal |
| **Strategic Advisor** | Synthesis + Reframing | Deviation list + redlines + business context | Negotiation strategy | Explicit epistemic stance shift from clause-level analysis to whole-deal strategic reasoning. Works from clean structured inputs — no accumulated cognitive residue from prior stages — enabling genuine counterparty modeling and strategic synthesis |

## Execution Order

```
Contract Reader → Playbook Comparator → Redline Writer → Strategic Advisor
```

Sequential, because each agent depends on the previous agent's output.

The Redline Writer and Strategic Advisor *could* run in parallel (both consume the deviation list), but the Strategic Advisor produces better strategy when it can reference the specific redlines being proposed — knowing what's on the table shapes how you advise sequencing and trade-offs. Sequential is worth the extra step.

**Rationale for sequential**: The dependencies are linear. The total wall-clock time is longer than a monolithic prompt, but each agent works in a clean context with compressed inputs, which should produce qualitatively different output — particularly in investigation breadth and strategic depth.

For batch processing (reviewing multiple contracts), the full pipeline can be parallelized *across contracts* while remaining sequential *within each contract*.

## Handoff Specifications

### Handoff 1: Contract Reader → Playbook Comparator

**What crosses**: Structured clause summaries — what each provision says, specific terms and thresholds, notable interactions between clauses, unusual provisions, notable absences. Includes key quotes and specific figures.

**Format**: Structured sections by topic. Factual, descriptive tone. Key contractual language quoted directly so the Comparator can evaluate precise wording.

**What gets dropped**: Exploratory threads ("this is interesting because..."), investigative asides, the reader's analytical journey, tentative interpretations that didn't resolve. The investigation's exploratory framing would bias the comparator toward continued exploration rather than systematic evaluation.

### Handoff 2: Playbook Comparator → Redline Writer

**What crosses**: Classified deviations — what each deviation is, how it's classified (Acceptable / Negotiate / Escalate), what the playbook standard is, section references, quoted contract language.

**Format**: Structured deviation list. Each entry: clause reference, contract provision, playbook standard, classification, substance of the gap.

**What gets dropped**: Evaluative reasoning ("this matters because..."), risk narratives, comparative analysis. The classification result crosses; the classification reasoning does not. Evaluative residue constrains generation toward boilerplate.

**Also passes through (not from pipeline)**: Original contract text (for exact quoting in redlines), business context from user (deal dynamics, relationship, deadline).

### Handoff 3: Redline Writer → Strategic Advisor

**What crosses**: Redline proposals — what's being proposed for each deviation, priority designation, fallback positions, brief rationale.

**Format**: Structured redline list. Each entry: clause reference, proposed language summary, priority, fallback.

**What gets dropped**: Generation reasoning, alternative drafts considered, legal drafting rationale. The advisor needs to know what's being proposed, not how the writer arrived at the language. Generation residue (clause-level focus, drafting posture) would anchor the advisor to a clause-by-clause perspective rather than whole-deal strategic thinking.

**Also passes through (not from pipeline)**: Deviation list from Agent 2 (classifications and substance), business context from user.

## Pre-Pipeline: Context Gathering

Before running the pipeline, gather from the user:

1. The contract (file, URL, or pasted text)
2. Which side they're on (vendor/customer/partner/etc.)
3. Contract type (if not obvious from the document)
4. Deadline, focus areas, deal context, relationship dynamics

**Routing**:
- Items 1-3 → Contract Reader (interpretation context, not evaluative bias)
- Item 2 + playbook → Playbook Comparator (user's side affects which deviations matter)
- Items 2-4 → Redline Writer (relationship and deal dynamics shape tone and drafting)
- Items 2-4 → Strategic Advisor (business context drives strategic reasoning)

The Contract Reader does **not** receive the full business context (deadline, strategic importance). These would bias investigation — the reader should surface what's in the contract, not what the user is worried about.

## Context Window Notes

- **Contract Reader**: May face context pressure with very long contracts (50+ pages). For contracts exceeding context capacity, run multiple Reader instances on contract sections with a lightweight merge step. Most contracts (under 30 pages) fit in a single pass.
- **Playbook Comparator**: Receives the compressed clause summary (substantially smaller than the raw contract) plus the playbook. Manageable in all cases.
- **Redline Writer**: Receives the deviation list (compact) plus the original contract (for quoting) plus business context. Same capacity consideration as the Reader for very long contracts.
- **Strategic Advisor**: Receives only structured data from prior stages plus business context. The lightest context load of all agents. No capacity concerns.

## Optional Extension: CLM Routing

If a Contract Lifecycle Management system is connected, a post-pipeline step can recommend approval workflows and routing paths based on the deviation classifications and overall risk profile. This is a mechanical routing step, not a cognitive agent — it maps classifications to workflow rules.

---

## Mapping: Architect Findings → Pipeline Design

Each finding from the architect analysis maps to a specific pipeline design decision:

| Architect Finding | Pipeline Response |
|---|---|
| **Investigation + Evaluation fusion** (Steps 4-5) — evaluation pre-filters investigation | Separated into Contract Reader (investigation, no playbook) and Playbook Comparator (evaluation, no investigative prose). The playbook never enters the investigation context. |
| **Heavy seeding** (~54 elements, 25 named issues constraining investigation) | Seeds removed from investigation entirely. The Contract Reader uses lenses ("what's unusual?", "how does risk flow?"), not checklists. The playbook's structure is used by the Comparator, where seeds are appropriate convergent aids. The "Common issues" lists are removed — the Comparator evaluates against playbook positions, not against a list of things to find. |
| **Evaluation + Generation in shared context** (Steps 5-6) — evaluative posture constrains redlines | Separated into Playbook Comparator and Redline Writer. The Writer receives classifications as structured input, not evaluative prose. It also receives business context (relationship, deal dynamics) to shape language beyond "standard market position." |
| **Output template as convergent anchor** — fixed fields force uniform depth | Each agent has its own output format matched to its function. Depth is proportional to substance/severity, not uniform across all clauses. |
| **Numeric anchors** ("Top 3-5 issues", "Top 3 issues", tier bullet counts) | All numeric anchors removed. No "top N" in any agent. Output counts respond to the contract. |
| **Synthesis contaminated by accumulated context** (Step 7) — strategy restates classification | Strategic Advisor receives only compressed, structured inputs (deviation list + redlines + business context). No accumulated investigation, evaluation, or generation prose in its context. It reasons about the deal fresh. |
| **12-category table pre-filtering investigation** | Removed from investigation. The Contract Reader surfaces what it finds, organized by what's in the contract rather than by predetermined categories. The Comparator may use playbook categories for evaluation (appropriate), and separately flags provisions that fall outside those categories rather than ignoring them. |

### Findings Addressed Differently Than Recommended

The architect recommended this pipeline structure directly. The implementation follows the recommendation closely, with one refinement: the Playbook Comparator explicitly includes a "Provisions Outside Playbook Categories" section. This ensures that the Contract Reader's broader investigation (which may surface provisions the playbook doesn't cover) doesn't get silently dropped at the evaluation stage. Unusual provisions that don't fit the playbook's categories are flagged for attention rather than forced into existing categories or ignored.

### What to Watch for When Testing

- **Contract Reader breadth**: Run on a contract with unusual provisions (AI-generated content rights, novel regulatory clauses, unusual commercial structures). The Reader should surface these prominently. If it only produces the standard 12 categories, the lenses aren't working.
- **Natural variation**: Run on contracts of different complexity. A 5-page service agreement and a 50-page enterprise deal should produce very different reading depths and deviation counts. If output volume is uniform, something is anchoring.
- **Redline creativity**: Check whether redlines are shaped by the deal context (relationship, strategic importance) or default to generic "standard market position" language. The Redline Writer receives business context specifically to avoid this.
- **Strategic depth**: Does the Strategic Advisor model the counterparty and reason about leverage, sequencing, and concessions? Or does it restate the deviation classifications in strategy-flavoured language? The latter signals that evaluative residue leaked through the handoffs.
- **Provisions outside playbook**: Test with a contract containing clauses that don't map to the playbook. These should appear in the Comparator's "Outside Playbook Categories" section and inform the Strategic Advisor's reasoning, not disappear at the evaluation stage.
