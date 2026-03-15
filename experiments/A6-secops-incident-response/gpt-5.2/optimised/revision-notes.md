---
model: GPT-5.2 (gpt-5.2)
date: 2026-03-15
experiment: A6
tier: optimised
artifact: revision-notes
---

# A6 — Tier 2 (Optimised) Revision Notes

Source files:
- Original prompt: `experiments/A6-secops-incident-response/original/SKILL.md`
- Architect analysis: `experiments/A6-secops-incident-response/gpt-5.2/analysis/prompt-architect-analysis.md`

## Goals of this revision

1) **Remove anchors**, especially the fixed “5 Whys” chain and other template-driven box-filling pressures.
2) **Separate investigation vs evaluation**, with explicit cognitive boundaries (triage and postmortem).
3) **Reduce confabulation risk** by making uncertainty admissible and banning invented operational specifics.
4) **Prevent cross-mode residue** (status-update posture contaminating postmortems) via stronger mode scoping.

## Mapping: architect findings → changes implemented

### A) Investigation ↔ evaluation entanglement during triage
**Finding:** Severity evaluation can pre-filter investigation.

**Change:** Added an explicit **“Investigation-first rule”** in *Mode: New Incident (Triage)*. The prompt now instructs: collect facts/unknowns first, then assign **provisional** severity with rationale + confidence.

### B) Cross-phase residue (status reporting contaminates postmortem)
**Finding:** Status-update template language establishes an operational posture that bleeds into postmortems.

**Change:** Introduced a global **Mode boundary rule (anti-contamination)** and rewrote the mode sections so each mode is self-contained, with an explicit instruction to not borrow framing/sections from other modes.

### C) Postmortem multi-mode collision (investigation + evaluation + generation + synthesis)
**Finding:** The original postmortem template forces incompatible modes in one pass.

**Change:** Added an **Internal sequencing rule** inside *Mode: Postmortem* that instructs a clear order:
1) timeline/facts → 2) causal analysis → 3) response evaluation → 4) action items → 5) lessons learned.

This is a prompt-level (Tier 2) intervention to reduce simultaneous-mode collision without requiring a full pipeline.

### D) “5 Whys” double anchor (numeric + structural)
**Finding:** Forces exactly five levels and a single linear chain.

**Change:** Removed “5 Whys” entirely. Replaced with **de-anchored causal analysis guidance**: follow evidence to natural depth, allow branching contributing factors, stop where evidence stops.

### E) Template completion pressure → confabulation risk
**Finding:** Required-looking slots increase invented timestamps/owners/ETAs.

**Change:** Added explicit **Provenance + uncertainty** rules across modes:
- “Do not invent names, timestamps, owners, ETAs, or impacts.”
- Use **Unknown/TBD** when not provided or not pulled from tools.

Action items now include **Owner/Due** but explicitly instruct to fill as TBD unless provided.

### F) “Blameless” suppressing human factors
**Finding:** Blamelessness can be misread as “avoid people,” losing decision-environment causality.

**Change:** Expanded blameless guidance in postmortem: analyse human decisions via systems lens (what was known, constraints, pressures, why it made sense at the time).

## What to watch for when testing Tier 2

- **Severity anchoring:** Does the model still commit to SEV too early, or does it surface unknowns first?
- **Postmortem posture:** Does the postmortem read as reflective learning (past tense), not an expanded status update?
- **Causal shape:** Does causal analysis branch naturally, or does it still become a tidy single chain?
- **Confabulation:** Are timestamps/owners/ETAs left as TBD when missing (good) vs invented (bad)?
- **Human factors:** Are decision contexts described without blame?

## Notes

This Tier 2 revision uses **scope boundaries and sequencing** to reduce mode interference within a single skill. A future Tier 3 pipeline could further strengthen separation by splitting postmortem work into distinct agents (timeline → causal analysis → response evaluation → action planning → synthesis) with structured handoffs.
