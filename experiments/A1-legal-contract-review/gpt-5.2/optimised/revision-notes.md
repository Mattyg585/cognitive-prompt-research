---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: optimised
artifact: revision-notes
---

# A1 (Tier 2 — optimised) revision notes

Source files:
- Original prompt: `experiments/A1-legal-contract-review/original/SKILL.md`
- Architect analysis: `experiments/A1-legal-contract-review/gpt-5.2/analysis/prompt-architect-analysis.md`

## Summary of changes (what and why)

This revision keeps the original goal (playbook-aligned contract review with negotiator-ready redlines) but restructures the prompt to reduce mode interference and template-driven fabrication risk.

### 1) Separate investigation from evaluation and drafting
**Architect finding:** investigation was interleaved with evaluation (GREEN/YELLOW/RED) and generation (redlines), causing pre-filtering and “solution-shaped” discovery.

**Change:** introduced four explicit phases with hard constraints:
- Phase 1: Investigate & Map (no severities, no redlines)
- Phase 2: Evaluate & Classify (GREEN/YELLOW/RED)
- Phase 3: Draft redlines (YELLOW/RED only)
- Phase 4: Strategy & next steps

**Intended effect:** preserve exploratory bandwidth to catch non-obvious structure (definitions, exhibits, precedence, incorporation-by-reference) before judgments/solutions shape what gets noticed.

### 2) Reduce numeric anchoring and fixed-slot pressure
**Architect finding:** fixed counts (“Top 3 issues”, “Top 3–5 issues”) and rigid templates can become targets, creating uniformity across different contracts.

**Change:** removed fixed quantities and reframed summaries as:
- “prioritized set of asks sized to the actual contract”
- “do not force a certain number of findings per category”

**Intended effect:** allow natural variation (simple contracts may yield few findings; complex contracts may yield many).

### 3) Add evidence integrity constraints to prevent fabricated quotes / section refs
**Architect finding:** template slots like “exact quote” and “playbook position” can pressure the model to invent plausible text or standards.

**Change:** added explicit rules:
- Quote verbatim only when reliable
- Otherwise label as `[PARAPHRASE — needs verification]`
- Never invent section numbers, exhibit titles, or playbook positions

**Intended effect:** improve auditability and reduce overconfident hallucinations, especially with OCR’d PDFs or partial excerpts.

### 4) Strengthen playbook integrity handling
**Architect finding:** risk of “smuggling in” an implied playbook position when none exists.

**Change:** made playbook vs generic baseline a first-class, explicitly labeled basis:
- Only assert playbook positions with a cited source
- Otherwise label as **Generic Commercial Baseline**

### 5) Convert heavy clause seeding into broader lenses (while keeping minimum coverage)
**Architect finding:** dense clause guidance and “common issues” lists can anchor discovery to a checklist and underweight non-obvious architecture.

**Change:**
- Kept a “minimum coverage” list as a floor (convergent evaluation aid)
- Added explicit **architecture lenses** and **operational lenses** in Phase 1 to force attention to: definitions, precedence, exhibits, incorporation, cross-references, and feasibility.

**Intended effect:** improve novelty/coverage beyond the usual LoL/indemnity/IP/DPA checklist.

### 6) Reduce stance drift / disclaimer overload
**Architect finding:** tension between “not legal advice” and providing negotiation-ready drafting can cause oscillation (over-hedging or repeated boilerplate).

**Change:**
- One clear disclaimer up front
- One short reminder at the end
- Focus the body on decision-support outputs with evidence and explicit “missing info” handling.

## What to watch for when testing (diagnostics)

Use the architect’s suggested tests:
- **Uniformity:** do finding counts vary with contract complexity?
- **Novelty:** are non-obvious architectural issues surfaced (precedence, exhibits, incorporation, definitional traps)?
- **Evidence integrity:** are quotes truly verbatim and section refs real? Are paraphrases clearly labeled?
- **Playbook integrity:** if no playbook is found, is the baseline explicitly generic (no implied house positions)?
- **Cross-clause reasoning:** are interactions (e.g., indemnity vs LoL carveouts) discussed when material?
- **Hard-to-fix issues:** are operational/business-process risks surfaced even when no clean redline exists?
