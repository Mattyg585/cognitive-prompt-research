# Prompt Architect Analysis: `/review-contract`

**Analysed**: `experiments/A1-legal-contract-review/original/SKILL.md`
**Date**: 2026-03-14

---

## 1. What this prompt is actually asking for

This prompt fuses **four distinct types of thinking** into a single sequential pass:

1. **Investigation** — read and understand the contract, surface what's in it
2. **Evaluation** — judge every clause against playbook criteria, classify deviations as GREEN/YELLOW/RED
3. **Generation** — write specific redline language for each deviation
4. **Synthesis + Reframing** — compress everything into a negotiation strategy, model the counterparty, prioritise

These are presented as sequential steps (4 through 7), but they execute in a single context. By Step 7, the model is reasoning through a cognitive slurry of investigation residue, evaluation classifications, and generated redline language — all shaping how it synthesises strategy.

The dominant posture is **evaluative**. The prompt establishes an evaluative frame from the moment it introduces the playbook (Step 3), and that frame governs everything that follows. Investigation is subordinate to evaluation — the model reads the contract *in order to evaluate it*, not to understand it on its own terms first.

## 2. Where modes interfere

### Investigation + Evaluation: the classic toxic pair (Steps 4–5)

Step 4 asks the model to "read the entire contract" and "analyze each material clause against the playbook position." These sound sequential but execute simultaneously. The playbook criteria are in context *while the model reads the contract*. The evaluation becomes a pre-filter on investigation.

The 12-category table (lines 73–87) and detailed clause guidance (lines 90–193) make this concrete. The model has ~120 lines of specific things to look for — key elements, common issues, named patterns. It will find what's listed and stop. Contract provisions that fall outside these 12 categories are likely to be underweighted or missed entirely.

**Mechanism**: The model doesn't read the contract and then evaluate. It reads *through* the evaluation framework. A clause about AI-generated output ownership, a novel regulatory compliance provision, or an unusual commercial arrangement that doesn't map to the 12 categories will be processed as noise rather than signal.

### Heavy seeding constraining investigation (lines 73–193)

The detailed clause guidance sections are extensive seeds:

- Limitation of Liability: 7 "key elements to review" + 4 "common issues"
- Indemnification: 6 elements + 4 issues
- IP: 6 elements + 4 issues
- Data Protection: 8 elements + 4 issues
- Term & Termination: 6 elements + 5 issues
- Governing Law: 7 elements + 4 issues

That's roughly 54 specific elements and 25 named issues. This is content prescription at scale. The model will anchor to these lists. For a routine SaaS agreement where these categories cover 95% of the risk, this works. For a non-standard contract — a complex partnership, a novel technology arrangement, a cross-border deal with unusual regulatory features — the seeds constrain investigation to known patterns.

### Evaluation + Generation in shared context (Steps 5–6)

After classifying deviations into GREEN/YELLOW/RED (convergent evaluation), the model must generate redline language (generation). The evaluative posture is still active. The redlines will tend toward "standard market position" language — competent, legally sound, predictable — rather than language tailored to the specific commercial dynamics, relationship context, or strategic positioning the user described in Step 2.

### The output template as a convergent anchor (lines 319–352)

The fixed output format forces uniform treatment: every clause gets the same `[Clause Category] -- [GREEN/YELLOW/RED]` structure with the same five fields. A critical IP ownership issue and a trivially acceptable governing law clause get the same structural weight. The template overrides the model's judgment about where to spend analytical depth.

### Numeric anchors

- **"Top 3-5 issues"** (line 332) → will produce 4 every time
- **"Top 3 issues"** (line 276) → will produce exactly 3
- **12-row clause category table** → the model will cover all 12 regardless of whether all are material
- **3 GREEN/YELLOW/RED examples each** (lines 202–240) → anchors how many deviations of each type to find
- **3-tier negotiation framework** (lines 284–305) with bullet-counted examples → shapes the count of items per tier

### Synthesis contaminated by accumulated context (Step 7)

By Step 7, the context carries the full residue of investigation, evaluation, classification, and generation. The "Negotiation Strategy" section asks for synthesis — model the counterparty, prioritise, think strategically. But the model is synthesising *over* all the evaluative, classificatory, and generative material already produced. The strategy section will tend to restate the tier classifications rather than engage in genuine strategic reasoning about the deal's dynamics.

## 3. What to check for in the output

- **Run on contracts of different complexity.** A 5-page service agreement and a 50-page enterprise deal should produce very different analyses. If both produce 12-section clause analyses with 4 key findings, the anchors are dominating.

- **Check for findings outside the 12 categories.** Test with a contract containing an unusual clause — AI-generated content rights, unusual regulatory provisions, novel commercial arrangements. If the output either misses these or awkwardly forces them into one of the 12 categories, the seed table is pre-filtering investigation.

- **Check redline creativity.** Are the redlines "standard market position" boilerplate, or are they shaped by the specific deal context (relationship, strategic importance, deadline) the user provided in Step 2?

- **Check negotiation strategy depth.** Does it model the counterparty's likely positions and strategic dynamics? Or does it restate the tier 1/2/3 framework with the specific items slotted in? The latter is classification dressed up as strategy.

- **Count uniformity.** Across multiple runs on different contracts, do the KEY FINDINGS always have 4 items? Do the negotiation tiers always have 3-4 items each? Uniformity signals anchoring.

## 4. What to do about it

### Prompt-level optimisation (Tier 2)

These fixes stay within the existing single-prompt structure:

1. **Add a scope boundary between reading and evaluating.** Before the clause table, insert: *"First, read and understand the contract as a whole — what it's trying to accomplish, how risk is allocated, what's unusual or notable. Then evaluate against the playbook."* This won't fully separate the modes (the playbook criteria are still in context) but it gives the model permission to notice things that don't map to the 12 categories.

2. **Remove numeric anchors.** "Top 3-5 issues" → "Key findings." "Top 3 issues" → "Most important issues." Let count respond to the contract.

3. **Replace seeds with lenses where possible.** The detailed "Common issues" lists (lines 103–107, 119–124, etc.) are the most anchoring seeds. Replace with lenses: *"How does the risk allocation in this clause compare to what a balanced commercial agreement would provide, given the parties' roles?"* Keep the "Key elements to review" lists — these are legitimate convergent aids for a systematic review — but remove the "Common issues" lists that tell the model what to find.

4. **Lighten the output template.** Instead of fixed fields for every clause, use: *"For each material clause, cover: what the contract says, how it deviates from the playbook, and why it matters. Spend depth proportional to materiality — a minor acceptable variation warrants a line, a critical deviation warrants a full analysis with redline."*

5. **Remove the GREEN/YELLOW/RED examples.** The classification definitions are fine. The 3-4 examples per tier are anchors that tell the model what shape its output should take. Let the playbook and the contract determine what's GREEN/YELLOW/RED.

### Pipeline reconstruction (Tier 3)

The fundamental issue is that investigation, evaluation, generation, and synthesis are running in a single context with accumulating cognitive residue. Prompt-level fixes will improve the margins but can't eliminate the core interference. For production use, this prompt is a strong candidate for splitting:

**Agent 1: Contract Reader (Investigation)**
Read and understand the contract. Surface what's there — clause structure, risk allocation, unusual provisions, notable absences. No evaluation against the playbook. No classification. Output: structured summary of what the contract says, organised by topic.

**Agent 2: Playbook Comparator (Evaluation)**
Receives the structured summary + the playbook. Evaluates each clause against standard positions. Classifies deviations. Output: structured deviation list with classifications and evidence.

**Agent 3: Redline Writer (Generation)**
Receives the deviation list + the original contract text (for quoting). Generates specific alternative language for each deviation. Clean generative context — no evaluation residue. Output: redline suggestions with rationale.

**Agent 4: Strategic Advisor (Synthesis + Reframing)**
Receives the deviation list + redlines + the user's business context (from Step 2). Synthesises a negotiation strategy. This agent gets the most cognitive freedom — it models the counterparty, considers deal dynamics, prioritises based on business context. The deviation classifications and redlines are its inputs, not its cognitive frame.

**Handoff design**: Each handoff compresses to structured form. The Contract Reader outputs structured summaries, not exploratory prose. The Playbook Comparator outputs classified deviations, not evaluative narrative. Each schema boundary strips the cognitive residue of the prior stage.

**The trade-off**: This adds orchestration complexity. For a one-off contract review, the prompt-level fixes (Tier 2) are probably sufficient. For a production legal workflow that runs repeatedly across many contracts, the pipeline reconstruction is likely worth it — the investigation will catch more, the redlines will be more creative, and the strategic advice will be genuinely strategic rather than a restatement of the classification.

### What I'd expect to see

**Tier 2 (optimised prompt)**: Incremental improvement. Slightly more findings, especially outside the 12 seeded categories. More variation in finding counts across different contracts. Slightly deeper strategic analysis in the negotiation section. The improvements will be real but modest — the fundamental investigation-evaluation fusion is still present.

**Tier 3 (pipeline)**: The Contract Reader, freed from evaluation criteria, will surface provisions and patterns that the monolithic version misses — unusual clauses, subtle interactions between provisions, structural features of the risk allocation that don't map to any category. The Strategic Advisor, working from clean classified inputs rather than accumulated context, will produce genuine strategic reasoning — modelling the counterparty's likely positions, identifying leverage points, recommending sequencing. The gap between Tier 2 and Tier 3 is where the experiment's hypothesis lives.

## 5. Composition signature

This is a single-prompt skill, not a multi-agent system. No composition analysis needed.

However, it's worth noting that this skill will load into a base agent's context. The skill carries a **strongly evaluative** posture. If the base agent has been conducting investigation or open-ended conversation before this skill triggers, the skill's evaluative frame will override the session's prior cognitive posture — which is fine, since that's the intent. The risk is the reverse: if this skill is loaded early and additional skills load later expecting an exploratory posture, this skill's evaluative residue will bias them.

---

**Bottom line**: This is a well-structured legal workflow with a clear, practical output. The issues aren't about quality — the output will be competent and useful. The issues are about the gap between competent and genuinely insightful: investigation pre-filtered by evaluation criteria, output counts anchored by numeric targets, strategy that restates classification rather than engaging in independent strategic reasoning. The heaviest contamination is the 12-category seed table governing a process that should start with open investigation. Tier 2 fixes (scope boundary, anchor removal, seed-to-lens conversion) will help incrementally. Tier 3 reconstruction (separate agents for reading, evaluating, redlining, and strategising) is where the qualitative leap would appear — if the hypothesis holds.
