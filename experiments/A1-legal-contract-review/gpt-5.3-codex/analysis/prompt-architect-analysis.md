---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A1
artifact: prompt-architect-analysis
---

# Prompt Architect Analysis — A1 Legal Contract Review

Analysed prompt: `experiments/A1-legal-contract-review/original/SKILL.md`

## 1) What types of thinking this prompt requires (and how they relate)

The original `/review-contract` prompt asks one context to perform four major cognitive modes:

1. **Investigation** — read and understand the whole contract, clause interactions, and notable absences.
2. **Evaluation** — judge each clause against playbook standards and assign GREEN / YELLOW / RED.
3. **Generation** — draft concrete redline language with rationale and fallback positions.
4. **Synthesis/Reframing** — produce negotiation strategy and business-impact guidance.

These are not all compatible in a single pass. Investigation needs open exploration; evaluation narrows; generation optimizes for language production; strategy synthesis needs a whole-deal perspective. In the original prompt these modes are interleaved in one context, so later sections inherit cognitive residue from earlier sections.

## 2) Where modes interfere (with evidence and mechanism)

### A. Investigation is pre-filtered by evaluation

Prompt evidence:
- Step 4 asks to read holistically, but immediately forces analysis through a seeded framework.
- The clause category table and detailed clause guidance enumerate many expected elements and common issues.

Mechanism:
- Because evaluation criteria are present during reading, the model tends to look for known buckets first and underweight out-of-framework issues.
- This is classic investigation + evaluation interference: "find what fits known categories" dominates "notice what is genuinely unusual."

### B. Heavy seeds constrain divergent discovery

Prompt evidence:
- Detailed clause lists include extensive "Key elements" and "Common issues".
- The output format encourages fixed category-by-category coverage.

Mechanism:
- Seeds are appropriate for convergent classification, but over-seeding at the reading stage reduces chance of detecting novel risk interactions (for example, ML training rights + survival + change-of-control compounding effects).

### C. Numeric and structural anchors flatten variation

Prompt evidence:
- "Top 3–5 issues" and "Top 3 issues" instructions.
- Fixed output skeleton with uniform clause treatment.

Mechanism:
- Numbers become targets; outputs converge to similar list sizes regardless of complexity.
- Fixed templates can force equal space for low-impact and high-impact clauses, reducing proportional depth.

### D. Evaluation + generation in one context produces boilerplate redlines

Prompt evidence:
- Redline writing follows directly after classification.

Mechanism:
- Once the context is strongly evaluative, generation tends toward standard-form language and may underuse specific deal context (new vendor, 2-week deadline, customer focus on data/IP).

### E. Strategy section is contaminated by accumulated context

Prompt evidence:
- Strategic recommendations come after long classification and drafting sections in the same context.

Mechanism:
- Rather than true strategic reasoning, the model often restates classifications in priority order. The output can look strong but be less adaptive to counterpart behavior and leverage dynamics.

## 3) Diagnostic signals and testable predictions

When you run this prompt, look for:

1. **Uniform counts across runs**
   - If findings often cluster at similar counts (e.g., always around 4–5), anchors are dominating.

2. **Checklist-shaped outputs**
   - If output always mirrors the same clause table depth regardless of contract quirks, seeds are over-controlling.

3. **Weak out-of-category detection**
   - If unusual provisions are forced into standard buckets or barely discussed, investigation breadth is suppressed.

4. **Boilerplate redlines**
   - If language is generic and weakly tied to this specific deal context, evaluation residue is constraining generation.

5. **Strategy-as-restatement**
   - If strategy mostly repeats risk tiers rather than modeling counterparty incentives and concession sequencing, synthesis is contaminated.

## 4) What to do about it

### Prompt-level fixes (Tier 2)

1. Separate reading and evaluation with explicit scope boundary:
   - "First understand the contract; do not classify or recommend during this phase."
2. Remove numeric anchors:
   - "Key findings" instead of "Top 3–5".
3. Convert heavy seeds to lenses in exploratory portions:
   - Keep material clause guidance, remove exhaustive "common issues" lists as discovery targets.
4. Make depth proportional:
   - Permit brief grouping of low-risk clauses and deeper treatment where risk is material.
5. Preserve deal-context instructions for redlines and strategy.

Expected result: measurable but moderate improvement; still limited by single-context mode fusion.

### Pipeline-level reconstruction (Tier 3)

Split into four stages with structured handoffs:

1. **Contract Reader (investigation only)**
2. **Playbook Comparator (evaluation only)**
3. **Redline Writer (generation only)**
4. **Strategic Advisor (synthesis/reframing only)**

Key design principle: each handoff passes compressed structured outputs and drops process residue.

Expected result: better risk-identification accuracy (especially cross-clause interactions), less boilerplate redlining, and materially better strategic recommendations.

## Trade-off statement

- Tier 2 is lower overhead and suitable for one-off review.
- Tier 3 adds orchestration cost but is likely superior for repeatable production review, where latent quality gains matter.

## Composition note

The source is a single SKILL prompt rather than an explicit multi-agent runtime composition. Composition risk is therefore low at file level, but high **within** the monolithic prompt due to mixed cognitive posture.
