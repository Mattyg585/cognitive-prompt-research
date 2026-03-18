# Prompt Architect Analysis v3 — A1 Legal Contract Review

**Prompt**: `experiments/A1-legal-contract-review/original/SKILL.md`
**Date**: 2026-03-18
**Toolkit version**: cognitive-stance-reference.md (updated, with anti-patterns, epistemic stance, and recognition-primed/investigation-required boundary)

---

## 1. What the Prompt Is Actually Asking For

The prompt asks the model to perform eight declared sequential steps on a specific contract provided at runtime: accept the document, gather context, load an organisational playbook, read and analyse each clause, classify deviations, generate redline language, summarise business impact, and route via CLM if connected.

Structurally, the thinking required falls across four distinct types:

- **Investigation**: reading the specific contract, discovering what the clauses actually say, noticing clause interactions and unusual constructions
- **Evaluation**: classifying each clause as GREEN/YELLOW/RED against the playbook position
- **Generation**: drafting specific alternative redline language for YELLOW and RED items
- **Synthesis**: producing a negotiation strategy, priority framework, and business impact summary

These four types are loaded simultaneously in a single context window. The model reads the entire prompt — including the RED/YELLOW/GREEN classification system, the detailed "key elements to review" and "common issues" sub-tables for each clause category, the negotiation priority framework, and the output template — before it sees a single word of the actual contract.

---

## 2. Threshold Questions

### Is this recognition-primed or investigation-required?

**This is an investigation-required task.** The model must discover what a specific, novel contract actually says — its clause interactions, the way one provision qualifies another, unusual constructions that deviate from market standard in ways not anticipated by any checklist. The correct analysis cannot be produced without deeply engaging with the particular input document. Each contract is a unique artefact.

The litmus test: could the correct analysis be produced without seeing the contract? No. Therefore: investigation-required, and pipeline separation earns its cost.

This matters because investigation-required tasks require recognition-primed processing during the reading phase — following threads, noticing what is unusual, discovering emergent patterns (e.g., an uncapped indemnity that interacts with a narrow liability carveout to produce material exposure not visible from reading either clause in isolation). When evaluation criteria are present in context during that reading, the decision architecture switches from recognition-primed ("what do I notice?") to criterion-referenced ("which criteria are met?"). The model stops seeing what is there and starts checking what is expected.

### What is the task type?

**Analytical task** (contracts, policies, code review). Quality is primarily about accuracy, completeness, and insight — what the output says, not how it reads. This means:
- Pipeline separation helps
- Structured handoffs should strip cognitive mode
- Investigation and evaluation are reliably incompatible and should be separated
- The convergent-divergent compression rhythm applies directly

---

## 3. Declared vs Actual Architecture

The prompt declares eight sequential steps. Step 4 even contains an instruction that gestures toward sequencing within investigation: "Read the entire contract before flagging issues." This is intended to protect investigation from premature evaluation — a good instinct.

But the mechanism cannot work. The model reads the entire prompt before generating anything. By the time it reads the actual contract (which arrives at runtime as the `@$1` argument), its context already contains:

- The complete GREEN/YELLOW/GREEN classification taxonomy with worked examples for each tier
- The detailed "key elements to review" checklists for twelve clause categories
- The "common issues" bullet lists for each clause type
- The negotiation priority framework (Tier 1 deal-breakers, Tier 2 strong preferences, Tier 3 nice-to-haves)
- The output template including "Top 3-5 issues with severity flags"
- The redline format template specifying exactly what fields each finding must populate

The instruction "Read the entire contract before flagging issues" is a process note that cannot override the anticipatory awareness created by the evaluation framework already in context. When the model reads the contract, it is reading through the RED/YELLOW/GREEN lens. It is not investigating; it is checking.

This is the **declared architecture that doesn't match actual architecture** anti-pattern from the reference. The declared sequence is: read contract → analyse → classify → redline → summarise. The actual sequence is: absorb full evaluation framework including classification system + redlines format + output template → then read contract through that evaluative lens.

A prompt that is honestly convergent throughout — just a checklist to apply — has no gap between what it promises and what it delivers. This prompt declares sequential cognitive separation that does not exist. That gap produces output that passes all criteria (thorough, clause-by-clause, appropriately flagged) without genuinely inhabiting the investigative phase.

---

## 4. Mode Interference Patterns

### 4a. Investigation + Evaluation: the core contamination

The detailed clause guidance tables (lines 90–192 of the prompt) are present in context when the model reads the contract. These tables prescribe exactly what to look at for Limitation of Liability, Indemnification, IP, Data Protection, Term and Termination, and Governing Law. The "common issues" sub-bullets for each type are evaluation criteria in investigative clothing — they define what counts as a finding before the model has seen the contract.

The mechanism: the model does not read the contract and then evaluate. It reads the contract through the evaluation framework, pre-filtering observations to match the expected categories. Subtle patterns that do not fit an existing "common issues" bullet — an unusual interaction between an assignment clause and a change-of-control definition, a warranty scope that is technically narrow but practically irrelevant given the indemnification structure, an ambiguity in the definition of "confidential information" that creates exposure in a specific way for this party on this deal — get dropped. Not because the model lacks capability, but because criterion-referenced processing does not follow threads that lack a destination in the evaluation framework.

The instruction in Step 4 to "Consider the contract holistically: Are the overall risk allocation and commercial terms balanced?" is an attempt to open space for holistic investigation. But it comes after five numbered sub-steps that establish criterion-referenced processing, and it comes after the context has already been loaded with the classification system. The holistic instruction cannot undo the anticipatory narrowing created by the evaluation framework.

### 4b. Investigation + Generation: solution-shaped reading

Step 6 (generate redlines) is present in full in the context during Step 4 (clause analysis). The model knows that every YELLOW and RED finding must produce a "suggested redline" with "current language," "proposed alternative," "rationale," and a "priority" classification. This shapes what gets noticed during investigation: findings that do not have obvious redlines get deprioritised. An ambiguity that is genuinely problematic but for which there is no clean market-standard fix is harder to surface when the output format demands a "proposed redline" field be populated. Investigation becomes a funnel for recommendations rather than understanding.

### 4c. Synthesis during investigation: premature commitment via the output template

The output template in the "Output Format" section specifies a "Key Findings" section with "Top 3-5 issues." The model holds this target in context while reading the contract. By the time it has read three clauses, it is already forming a working model of which items will occupy the top-3-5 slots. Later clauses get read against that working model rather than freshly. Findings that would reorder the top issues get assimilated into the existing narrative rather than reshaping it. This is premature convergence — synthesis running during investigation.

---

## 5. Anti-Patterns from the Reference

### 5a. Prescribed threads posed as open questions

The twelve-category clause coverage table looks like a structural guide ("here are the areas to cover"). But the "Key Review Points" column functions as a prescribed thread for each category — it tells the model which aspects of each clause to attend to. The Limitation of Liability row specifies: "Cap amount, carveouts, mutual vs. unilateral, consequential damages." These are four specific threads, presented as a parallel equal-weight structure.

Real investigation of a liability cap is asymmetric. Sometimes the cap amount is the issue; sometimes the carveout structure makes the nominal cap irrelevant; sometimes the consequential damages exclusion is doing more work than the cap itself; sometimes the interaction with the indemnification clause makes the entire LOL framework function differently from how it reads in isolation. The parallel equal-weight thread structure normalises bilateral (or quadrilateral) investigation, suppressing the follow-where-it-leads quality that surfaces the non-obvious finding.

### 5b. Criterion gates inside investigation

Step 4 sub-step 4 says "Analyze each material clause against the playbook position." This is a criterion gate embedded in the investigation phase. The model is told to hold the playbook standard in mind while reading each clause, which converts reading-for-understanding into reading-for-deviation. The criterion (playbook position) becomes the filter that determines what counts as worth noting. Clauses that look unremarkable against the playbook but have unusual properties that matter in the specific deal context get passed over.

### 5c. Process notes inside generation

The Redline Generation Best Practices sub-section (lines 250–260) contains the instruction: "Be balanced: Propose language that is firm on critical points but commercially reasonable. Overly aggressive redlines slow negotiations." This is good advice for a human lawyer. For the model in this context, it loads a moderating constraint into the generation phase that shapes what gets generated: the model enters redline drafting with the audience's anticipated reaction already in mind, which may suppress aggressive-but-correct positions that a human reviewer should be deciding on, not the model.

---

## 6. Seeds vs Lenses

The prompt is almost entirely seeds. The clause coverage table, the detailed "key elements to review" sub-bullets, and the "common issues" lists across six clause types are exhaustive content prescription. They define the ceiling of discovery: the model will find what these lists anticipate, and the lists were written at prompt-authoring time, not at contract-reading time.

There is one gesture toward a lens: "Consider the contract holistically: Are the overall risk allocation and commercial terms balanced?" This is a structural question — it guides how to look rather than what to find. But it arrives after five numbered sub-steps that have established criterion-referenced processing, and it is framed as sub-step 5 of Step 4, equal in weight to the other sub-steps rather than as an overriding epistemic posture.

The effect of the seeding: contract-specific patterns that the checklist does not anticipate will be suppressed. Consider a contract with an unusual interaction between a data processing clause and an IP ownership clause that creates an exposure the drafter did not intend. This finding requires noticing a relationship between two clauses that does not correspond to any "common issues" bullet. In a criterion-referenced context, this thread does not have a destination — the model is unlikely to follow it. In a clean investigative context, with a lens like "what's the gap between how these parties intend this agreement to work and what it actually says?" the model has space to make the connection.

Seeds are not always wrong. For Step 3 (checking whether a playbook exists and what it should contain), the seeded checklist of what a playbook should define is legitimate — that is convergent, classification work. The harm is in applying the same seed-based approach to the investigation of the specific contract.

---

## 7. Numeric Anchors

The output template specifies "Top 3-5 issues with severity flags" in the Key Findings section. This is a numeric anchor. The model will produce 4 issues nearly every time, regardless of whether the contract has two critical problems or eight. On a simple, well-drafted contract, this forces finding padding. On a complex, poorly-drafted contract, this forces triage that should be the human reviewer's decision.

The negotiation priority framework itself (Tier 1, Tier 2, Tier 3) functions as an implicit anchor on issue distribution. The model will attempt to populate each tier, producing a balanced distribution of must-haves, should-haves, and nice-to-haves regardless of whether the contract warrants that distribution.

Natural variation is the health signal. A well-drafted contract reviewed against an aligned playbook might yield one RED item and several GREENs. A heavily one-sided contract might yield five REDs and nothing GREEN. The prompt's output template and priority framework will suppress this variation toward a normalised distribution.

---

## 8. What to Check for in Output

Given these patterns, here is what to look for when running this prompt:

**Consistent issue counts**: Run the prompt on contracts of varying complexity. If Key Findings consistently shows 4 items regardless of input, the "Top 3-5" anchor is dominating. If the tier distribution (Tier 1/2/3) consistently shows items in all three tiers, the priority framework is forcing distribution.

**Clause interaction findings**: Look for whether the output ever surfaces a finding that arises from the interaction between two clauses — a finding that would not appear if you analysed each clause in isolation. A criterion-referenced output will rarely contain these. A recognition-primed output will surface them because the model is following threads rather than checking categories.

**Unexpected finding types**: Check whether any finding is of a type not anticipated by the "common issues" bullets. If every finding maps directly to a listed common issue, the seeds are acting as a ceiling. If the output occasionally surfaces something the checklist did not prescribe, the investigation has some space to work.

**Competent but predictable**: The overall register will be "thorough audit" — correct, well-structured, all the right fields populated. Check whether it ever reads like "someone who understands the commercial relationship and its likely failure modes" rather than "someone who has applied the checklist."

---

## 9. Recommendations

### The threshold judgment

This is an investigation-required analytical task. The investigation and evaluation modes are genuinely incompatible. The evaluation framework is exhaustive and present in full context during investigation. Prompt-level scope boundaries ("you are investigating, not assessing") would help but cannot fully overcome the anticipatory narrowing created by the detailed clause checklists and classification system. The case for pipeline separation is strong.

### Prompt-level fixes (applicable if pipeline reconstruction is not viable)

**Remove the "Top 3-5" anchor.** Replace with "Surface the issues that warrant the user's attention — the count should reflect what you found, not a target."

**Set an explicit epistemic stance before Step 4.** Before the clause-by-clause analysis, add: "You are discovering what this contract actually says — observations about what is present, absent, and unusual. You are not yet assessing against the playbook. Note what you see before you evaluate what it means." This is lightweight but creates some epistemic protection even if the evaluation criteria remain in context.

**Demote the clause checklists from seeds to lenses.** Instead of "Key elements to review: Cap amount, carveouts, mutual vs. unilateral..." reframe as "For Limitation of Liability, ask: does this clause do what the parties probably intend it to do? Where does it interact with other provisions?" The lens opens space for the non-obvious finding; the seed closes it.

**Move the negotiation priority framework out of the investigation context.** Step 7's Tier 1/Tier 2/Tier 3 framework should not be loaded during Step 4. Keep Step 7 instructions separate — ideally in a second turn or a separate context.

### Pipeline reconstruction (recommended for production use)

The natural split is: investigation → evaluation + redline generation → negotiation synthesis.

**Agent 1: Contract Auditor (investigation only)**
No evaluation criteria in context. No classification system. No output template with fixed slots. The epistemic stance: "You are reading this contract to understand what it actually says — clause interactions, unusual constructions, the gap between apparent intent and actual language. Surface observations. Do not classify them. Do not assess them against any standard. Follow the threads that seem interesting regardless of whether they correspond to a common issue type."

The handoff from Agent 1 is a structured list of observations — not prose, not evaluated findings. Descriptive data: what the clause says, what interaction it has with other clauses, what is unusual or unexpected. This strips cognitive mode from the investigation before it enters the evaluation context.

**Agent 2: Playbook Evaluator (evaluation + redline generation)**
Receives the structured observation list from Agent 1 plus the playbook. Now applies the GREEN/YELLOW/RED framework. Has all the detailed clause guidance. Generates specific redline language. This agent is doing criterion-referenced work — that is appropriate here, because the investigation is already complete and the evaluation framework no longer suppresses it.

**Agent 3: Negotiation Strategist (synthesis)**
Receives structured evaluation output from Agent 2. Produces the priority framework, negotiation strategy, and business impact summary. No contract text in context. No investigation output in context. Clean synthesis from structured findings.

**Trade-off**: three agents versus one adds orchestration complexity and latency. For a one-off review where the user is present and driving, the prompt-level fixes above combined with a two-turn interaction (investigate first, classify in second turn) may be sufficient. For a production pipeline that runs repeatedly, the three-agent split is worth building.

**Handoff design note**: Agent 1's output should be in structured form (per-clause observations as key-value or bullet items, not prose). The structured form strips the exploratory register before it enters Agent 2's context. If Agent 1 outputs prose and Agent 2 receives it raw, Agent 2 will be biased toward continued exploration regardless of its own evaluation-oriented prompt.

---

## Summary

| Issue | Severity | Fix level |
|---|---|---|
| Investigation + evaluation fusion (evaluation criteria in context during contract reading) | High — switches decision architecture from recognition-primed to criterion-referenced | Pipeline reconstruction |
| Detailed "common issues" seeds define ceiling of discovery | High — findings constrained to what prompt author anticipated | Replace seeds with lenses at prompt level; eliminate from investigation agent in pipeline |
| Declared sequential architecture is simultaneous contextual presence | High — investigation knowing evaluation criteria in advance | Pipeline reconstruction |
| "Top 3-5 issues" numeric anchor | Medium — normalises finding count regardless of contract complexity | Prompt-level fix |
| Negotiation priority framework present during investigation | Medium — shapes what gets noticed toward pre-defined tier structure | Move to synthesis stage; pipeline reconstruction |
| Investigation + generation fusion (redline format known during reading) | Medium — investigation becomes funnel for fixable findings | Pipeline reconstruction |
| Prescribed threads in clause coverage table suppress asymmetric investigation | Medium — equal-weight parallel structure inhibits follow-where-it-leads | Replace with open lenses at prompt level |
| Epistemic stance not set | Medium — model defaults to evaluative register | Add explicit exploratory stance before investigation |

The prompt is well-structured for its declared purpose and will produce competent, professional output. The contamination described here is invisible in that output — it looks thorough. The gap only appears when you run a clean investigation agent on the same contract and compare what surfaces. That comparison is the experiment.
