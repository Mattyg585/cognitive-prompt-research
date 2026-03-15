---
model: GPT-5.2
date: 2026-03-15
experiment: A1
artifact: prompt-architect-analysis
---

# Prompt Architect Analysis — A1 Legal Contract Review (original SKILL)

Source prompt: `experiments/A1-legal-contract-review/original/SKILL.md` (`/review-contract -- Contract Review Against Playbook`).

## 1) What the prompt is actually asking for (cognitive posture)

This skill is a **multi-mode mega-task** masquerading as one workflow. It asks the model to carry, in one context, at least these distinct thinking modes:

- **Orchestration**: run an intake workflow (accept contract in multiple formats, ask for context, look for playbook files, optional CLM routing).
- **Investigation**: read/parse the entire contract; identify contract type; map clauses; notice interactions.
- **Evaluation**: compare each material clause against a playbook (or generic commercial standards) and classify deviations into GREEN/YELLOW/RED.
- **Generation**: draft exact redline language + fallbacks, plus external-facing rationales.
- **Synthesis/Reframing**: compress findings into an executive “Key Findings”, business impact, negotiation strategy, next steps.

The prompt’s intent is “clause-by-clause analysis against a standard + negotiator-ready artifacts”. That’s a legitimate goal; the structural risk is **asking investigation, evaluation, generation, and synthesis to happen in the same cognitive pass**.

## 2) Where modes interfere (mechanisms + evidence)

### A. Investigation is interleaved with evaluation (pre-filtering risk)

The workflow requires: “Analyze each clause, flag deviations” and “Classify each deviation … GREEN/YELLOW/RED”. This places criteria-referenced judgment *in the same pass* as discovery.

**Mechanism** (from the framework): when evaluation criteria are present during investigation, they become a pre-filter. The model preferentially surfaces issues it can already bucket (GREEN/YELLOW/RED) and may drop subtle/novel patterns that are real but harder to classify quickly (e.g., definitional traps, cross-references that invert obligations, hidden precedence clauses).

**Output symptom to watch**: a checklisty review that hits the obvious clause categories but misses “weird” contractual architecture (priority of documents, incorporated policies, security exhibits overriding master terms, waterfall of remedies, etc.).

### B. Investigation is interleaved with generation (solution-shaped discovery)

For every YELLOW/RED item, the prompt demands **ready-to-insert language** (“Be specific: Provide exact language, not vague guidance”).

**Mechanism**: requiring fixes while still finding problems makes discovery “solution-shaped”. Findings that don’t have an obvious redline (or require business decisions rather than legal drafting) are less likely to be surfaced or get reduced to generic advice.

**Output symptom to watch**: the model preferentially selects issues that are easy to redline (caps, notice periods) and under-emphasises issues that are harder to “patch” via clause edits (operational feasibility, service delivery realities, pricing/usage mismatch, governance ambiguity).

### C. Heavy seeding via clause lists + “common issues” examples (anchor-to-known-categories)

The prompt provides a minimum clause checklist plus extensive “Detailed Clause Guidance” and “Common issues” bullets.

**Mechanism**: this is strong **seeding** (telling the model what to find) rather than **lensing** (guiding how to look). In a contract-review setting, a seeded checklist is partly appropriate (review is inherently convergent), but the density of clause guidance can still anchor the search space.

**Likely side-effect**: coverage concentrates on the enumerated categories (LoL, indemnity, IP, DPA, confidentiality, term/termination, etc.) while underweighting clauses that are often material but not foregrounded here (e.g., audit rights, security obligations beyond DPA, SLA/service credits, acceptance criteria, change control, subcontracting, export/sanctions, anti-corruption, publicity, non-solicit, benchmarking, open-source obligations, order-of-precedence, incorporation-by-reference, survival/precedence).

**Output symptom to watch**: “same set of clauses every time” regardless of contract type; minimal attention to exhibits and defined terms.

### D. Numeric anchors and fixed slots (uniformity risk)

The output requires:

- “Top 3 issues” in the Business Impact Summary.
- “Top 3–5 issues” in Key Findings.
- A three-tier deviation system (GREEN/YELLOW/RED) and a three-tier negotiation priority framework.

**Mechanism**: numbers and fixed-slot templates become targets. Even when the contract has 1 major issue (or 9), the model will tend to produce ~3–5 headline items and shape the rest to fit the template.

**Output symptom to watch**: suspiciously stable counts and a “balanced” mix of severities regardless of the input’s actual risk profile.

### E. Output structure pressures “fill the boxes” (hallucination risk)

The template for clause analysis includes “Playbook position: [your standard]” and requires quoting “Current language: ‘[exact quote from the contract]’”.

**Mechanism**: rigid slots push convergent completion behaviour. If the playbook isn’t found (and/or the contract text isn’t easily quotable due to formatting, OCR, or missing section references), the model is nudged toward inventing plausible-sounding “standard positions” or paraphrased “quotes”.

**Output symptom to watch**:

- Playbook positions stated with high confidence despite Step 3 allowing “no playbook configured”.
- “Exact quote” blocks that don’t appear verbatim in the source contract.

### F. Stance drift: “not legal advice” vs negotiation-ready redlines

The prompt says: “You assist with legal workflows but do not provide legal advice.” Yet it also asks for negotiation strategy, prioritised redlines, and insert-ready clause language.

**Mechanism**: competing safety posture + directive to draft legal language can yield inconsistent register:

- Over-hedged, non-committal redlines (to avoid ‘advice’), or
- Boilerplate disclaimers repeated in every section (wasting context and reducing clarity), or
- The model refusing to provide exact language (depending on policy stance).

**Output symptom to watch**: oscillation between precise drafting and “consult your lawyer” caveats that reduce actionability.

## 3) What to check for in outputs (diagnostics for hidden contamination)

Use these as **tests**, not judgments of quality:

1. **Uniformity test** (anchors): Across contracts of different complexity, do “Key Findings” stay at ~3–5 and “Top 3 issues” always look similarly weighted?
2. **Novelty test** (seeds): Does the review surface material issues *outside* the seeded clause list (e.g., precedence, exhibits, operational obligations), or does it stay inside the checklist?
3. **Evidence integrity test** (template pressure): Are “Current language” quotes verifiably present and accurate? Are section references real?
4. **Playbook integrity test** (runtime assumptions): When no playbook exists, does the output clearly switch to “generic standards” without smuggling in an implied playbook?
5. **Cross-clause reasoning test** (holistic claim): The prompt instructs holistic reading (e.g., uncapped indemnity mitigated by LoL). Does the output actually model interactions, or does it treat clauses independently?
6. **Solution-shaped discovery test** (generation bleed): Are there important “hard-to-fix” issues raised even if no clean redline exists (e.g., business process misfit), or are most findings drafted as tidy clause swaps?

## 4) What to do about it (interventions, matched to mechanism)

This section is **about prompt structure**, not rewriting.

### Prompt-level interventions (lighter weight)

- **Temporal separation by explicit phase boundaries** inside one run: first *map/understand* the contract (investigation) without severities or redlines; then evaluate/classify; then draft redlines; then synthesise negotiation strategy.
- **Reduce numeric anchoring**: make “key findings” responsive to actual materiality (avoid fixed counts where possible).
- **Add anti-hallucination constraints tied to the template slots**: only quote verbatim text when available; otherwise mark as paraphrase/needs verification; only state playbook positions when sourced.
- **Convert some seeds to lenses**: keep the minimum clause checklist, but add explicit lenses that force attention to “non-obvious architecture” (definitions, incorporation by reference, precedence, exhibits) and “operational reality”.

### Pipeline reconstruction (heavier, more robust)

If you repeatedly see checklist outputs, uniformity, or weak cross-clause reasoning, the likely cause is **mode fusion**. A robust fix is to separate modes into clean contexts:

1. **Investigation agent**: build a contract map + list candidate issues without classifying or proposing fixes.
2. **Evaluation agent**: compare candidates to playbook/generic baseline; assign GREEN/YELLOW/RED; identify escalation triggers.
3. **Drafting agent**: generate redlines/fallbacks only for the issues already selected.
4. **Strategy agent**: negotiation sequencing + business impact summary.

**Trade-off**: better discovery depth and less solution-shaped filtering, at the cost of orchestration complexity and more tokens.

## 5) Composition signature (runtime loading / connectors)

Even though this is a single skill file, it references runtime composition:

- **Base skill posture**: multi-mode (investigation + evaluation + generation + synthesis + orchestration).
- **Optional connector/CLM posture**: additional **orchestration** and routing steps (“If CLM connected…”; “If you see unfamiliar placeholders… CONNECTORS.md”).

**Compatibility note**: tool/connector routing is mostly compatible if it stays procedural. The risk is indirect: orchestration language plus fixed workflows can reinforce a “mechanical checklist execution” posture, amplifying the template/anchor effects above.

## 6) Handoff notes for Prompt Writer

Focus areas for revision experimentation (without committing to a specific rewrite here):

- Separate investigation from evaluation/generation (either by explicit phases or multi-agent pipeline).
- Reduce fixed-count anchors (“Top 3”, “3–5”) or make them conditional.
- Protect against template-driven fabrication of quotes and playbook positions.
- Add lenses for non-obvious contract architecture so seeds don’t dominate.

---

Ready for handoff to the `prompt-writer` agent.