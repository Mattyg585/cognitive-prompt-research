# Pipeline Handoff Specification: Contract Review v3

## Pipeline Overview

Reviews a contract against an organization's negotiation playbook by separating investigation, evaluation + redline generation, and negotiation synthesis into three agents with compressed handoffs between each stage.

## Why a Pipeline

The monolithic prompt fuses incompatible types of thinking into a single context. The v3 architect analysis identifies two high-severity mechanisms and one medium-severity mechanism:

**High-severity: Investigation + Evaluation fusion**
The playbook's evaluation criteria are in context before the model reads the contract. This is not simple distraction — it switches the decision architecture from recognition-primed investigation to criterion-referenced checking (Klein's RPD). The model reads *through* the framework, finding what matches the categories and missing what doesn't: unusual provisions, clause interactions, structural features of the risk allocation that don't correspond to the "common issues" checklist. This is a qualitative change in how investigation proceeds, not an overload problem. Prompt-level scope boundaries ("you are investigating, not assessing") are partially effective against attentional residue but cannot prevent the anticipatory narrowing created by having the evaluation framework in context before reading begins.

**High-severity: Proactive interference at synthesis**
Research on proactive interference in LLMs (2025) establishes that accumulated earlier context actively degrades retrieval accuracy log-linearly — and that natural-language instructions to "set aside" prior context yield only marginal improvement. By the time the monolithic prompt reaches the strategy stage, the model is reasoning through the accumulated residue of investigation, evaluation, and generation simultaneously. The strategy produced in this context restates the deviation classifications in strategy-flavoured language rather than engaging in genuine counterparty modeling and sequencing reasoning. This is a structural working-memory problem, not an instruction compliance problem. Pipeline isolation solves it architecturally.

**Medium-severity: Investigation + Generation fusion**
The redline output format (current language / proposed redline / rationale / priority / fallback) is present during investigation. This shapes what gets noticed: findings without obvious redlines get deprioritised. An ambiguity that is genuinely problematic but for which there is no clean market-standard fix is harder to surface when the output format demands a "proposed redline" field be populated.

## Agent Map

| Agent | Cognitive Mode | Receives | Produces |
|-------|---------------|----------|----------|
| **Contract Auditor** | Investigation — recognition-primed, deliberate situation modeling | Contract text, user's side, contract type | Structured clause observations + commercial logic characterisation |
| **Playbook Evaluator** | Evaluation + Generation — convergent then generative | Clause observations + playbook + business context | Classified deviations + redline proposals |
| **Negotiation Strategist** | Synthesis + Reframing — whole-deal strategic reasoning | Deviation list + redlines + business context | Negotiation strategy |

## Execution Order

```
Contract Auditor → Playbook Evaluator → Negotiation Strategist
```

Sequential. Each stage depends on the prior stage's full output.

## Handoff 1: Contract Auditor → Playbook Evaluator

### What crosses

- The Auditor's complete structured output:
  - Contract Overview (type, parties, user's side, commercial structure, key dates)
  - The Deal's Commercial Logic (characterisation of what the deal is trying to accomplish)
  - Clause Observations (per-area: what the contract provides, specific terms, key quoted language, interactions)
  - Unusual or Non-Standard Provisions
  - Notable Absences
  - Material Clause Interactions

### Format

Structured sections by topic. Factual and descriptive. Key contractual language quoted directly.

The format must be structured — not free prose. Structured output strips the investigative cognitive mode before it enters the Evaluator's context. Exploratory prose in the handoff would pull the Evaluator toward continued investigation rather than systematic measurement, regardless of the Evaluator's own convergent-evaluative prompt.

### What gets dropped

- Exploratory threading ("this is interesting because...")
- Investigative asides and tentative interpretations that didn't resolve
- The discovery process — how the Auditor arrived at observations
- Any analytical hesitancy or qualification that belongs to the investigation phase

The Auditor's exploratory framing enabled discovery; it should not persist into evaluation. Only the findings cross.

### Additional context added at this stage (not from pipeline)

- The organization's negotiation playbook
- Business context: deal size, strategic importance, relationship type, deadline, focus areas

Business context routes to the Evaluator (not through investigation) to shape redline drafting without biasing what the Auditor discovered.

---

## Handoff 2: Playbook Evaluator → Negotiation Strategist

### What crosses

- **Deviation analysis**: For each material area:
  - Classification (Acceptable / Negotiate / Escalate)
  - Contract provision (with key quotes)
  - Playbook standard
  - Specific gap description
- **Redline proposals**: For each Negotiate and Escalate deviation:
  - Proposed redline language
  - Priority (Must-have / Should-have / Nice-to-have)
  - Fallback position
- **Provisions Outside Playbook Categories**: Any findings from the investigation stage that don't map to playbook categories, preserved through the evaluation stage

### Format

Structured list. Each deviation and each redline as a discrete entry. Enough information for strategic reasoning — the Strategist does not need the contract text or investigation prose.

### What gets dropped

- Evaluative reasoning narratives ("this matters because...", risk exposure calculations)
- Classification rationale — the result crosses, not the reasoning behind it
- Generation reasoning — alternative drafts considered, clause-interaction concerns the Writer addressed
- The Acceptable provisions list — these have been confirmed as not requiring strategic attention

The critical drop: accumulated evaluative and generative residue is the specific mechanism that produces strategy-flavoured deviation lists rather than genuine strategic reasoning. The Strategist's context should contain only what strategic reasoning actually needs.

### Additional context added at this stage (not from pipeline)

Business context: which side the user is on, deal size, strategic importance, deadline, relationship dynamics, focus areas.

This routes directly to the Strategist rather than through the pipeline. It shapes strategic reasoning without having biased investigation.

---

## Pre-Pipeline: Context Gathering

Before running the pipeline, gather from the user:

1. The contract (file, URL, or pasted text)
2. Which side they're on (vendor/customer/partner/etc.)
3. Contract type (if not obvious from the document)
4. Deadline, focus areas, deal context, relationship dynamics

**Routing:**

| Item | Contract Auditor | Playbook Evaluator | Negotiation Strategist |
|------|-----------------|-------------------|----------------------|
| Contract text | Yes | For quoting redlines | No |
| User's side | Yes (interpretation) | Yes (which deviations are favourable) | Yes (business context) |
| Contract type | Yes (if known) | Yes | No |
| Playbook | No | Yes | No |
| Deadline / focus areas / deal dynamics | **No** | Yes (shapes redline drafting) | Yes (shapes strategy) |

The Auditor receives the user's side and contract type as interpretation context — these shape how to read the document without biasing what gets discovered. The Auditor does **not** receive deadline, strategic importance, or focus areas: these would bias investigation toward what the user is worried about rather than what the contract actually says.

---

## Context Window Notes

- **Contract Auditor**: For contracts exceeding 30 pages, run multiple Auditor instances on contract sections with a lightweight merge step. Most contracts fit in a single pass.
- **Playbook Evaluator**: Receives compressed clause observations (smaller than raw contract) plus playbook. Also receives original contract text for quoting. Manageable in all but the most extreme cases.
- **Negotiation Strategist**: Receives only structured deviation list, redline proposals, and business context. The lightest context load. No capacity concerns.

---

## Architect Finding → Pipeline Design Mapping

| Architect Finding (v3) | Pipeline Response |
|---|---|
| **Investigation + Evaluation fusion — RPD decision architecture switch** | Contract Auditor runs with no playbook, no evaluation criteria, no business context. Evaluation framework never enters the investigation context. |
| **Detailed clause guidance seeds (prescribed threads in investigation)** | Entirely absent from the Auditor. The Auditor uses lenses ("how does risk flow?", "what's unusual?", "what's absent?") with no predetermined checklist. Seeds remain legitimate in the Playbook Evaluator where convergent work is appropriate. |
| **Declared sequential architecture that doesn't match actual architecture** | Pipeline makes the sequencing real, not declared. Investigation genuinely completes before evaluation begins. |
| **"Common issues" lists constraining investigation** | Removed from all stages. The Evaluator measures against the playbook's positions, not against a list of expected findings. |
| **Proactive interference at synthesis** | Negotiation Strategist receives only compressed structured outputs — no contract text, no investigation prose, no evaluative reasoning. The accumulated residue of prior stages is architecturally absent, not instructed-away. |
| **Investigation + Generation fusion (redline format present during reading)** | Redline format absent from investigation stage. The Evaluator's generation phase is a separate cognitive mode, separate context, with business context available for deal-calibrated drafting. |
| **Output template with fixed structural weight per clause** | Each agent has its own format matched to its function. Depth is proportional to substance. |
| **Numeric anchors ("Top 3-5", tier bullet counts)** | All numeric anchors absent from all agents. Output counts respond to the contract's complexity. |

---

## What to Watch for When Testing

- **Auditor breadth**: Run on the Common Paper CSA with its data processing structure, IP provisions, and unusual clauses. Does the Auditor surface the "Provisions Outside Playbook Categories" section with genuine content? If the Auditor produces only the standard 12-category structure, the investigation lenses aren't working — the model is defaulting to criterion-referenced checking despite the clean context.
- **Clause interaction findings**: Does the Auditor's "Material Clause Interactions" section contain discoveries that wouldn't emerge from clause-by-clause reading? If this section is empty or perfunctory, the recognition-primed investigation isn't fully engaging.
- **Evaluator vs. Auditor breadth comparison**: Compare what the Evaluator classifies against what the Auditor found. Did anything from the Auditor's "Unusual Provisions" or "Notable Absences" make it into the Evaluator's "Provisions Outside Playbook Categories" section? If those Auditor findings disappeared at the evaluation stage, the Evaluator is silently filtering what doesn't fit the playbook.
- **Redline calibration**: Are redlines shaped by the deal context (relationship, strategic importance) or generic "standard market position" boilerplate? The deal-calibrated test: would the same deviation produce differently-worded redlines for a strategic partnership vs. a commodity vendor relationship?
- **Strategist register**: Does the strategy model the counterparty (their needs, constraints, what their drafting choices reveal) or restate the deviation list? The test: remove all deviation-specific language from the strategy section. Does anything remain? If not, it's a reorganised list, not strategy.
- **Count variation**: Run on the Common Paper CSA (a well-drafted, balanced agreement) and a more one-sided contract. Do the deviation counts and strategy depth vary proportionately? If outputs are similar in volume regardless of input complexity, something is anchoring.
