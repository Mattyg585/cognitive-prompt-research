---
model: GPT-5.2
date: 2026-03-15
experiment: A4
tier: optimised
artifact: revision-notes
---

# Revision Notes: A4 Design Research Synthesis (GPT-5.2)

## Finding → change mapping (from Prompt Architect)

### A) Executive framing placed before exploration → premature simplification
- **Change**: Moved executive summary to the end and added explicit “write last” + “don’t introduce new claims” guardrail.
- **Why**: Prevents narrative lock-in before theme discovery and evidence selection.

### B) Synthesis + prioritisation in the same pass → solution-shaped synthesis
- **Change**: Introduced phased workflow inside one prompt:
  - Phase 1: evidence-first reading (no solutions)
  - Phase 2: themes (still no prioritisation)
  - Phase 3: implications → opportunities → recommendations
- **Why**: Creates a scope boundary that reduces evaluation becoming a pre-filter on what counts as an insight.

### C) Evidence/quantification demands without guardrails → forced completion / fabrication risk
- **Change**: Added explicit evidence rules:
  - Quotes must be verbatim
  - Attribution/participant IDs only when present
  - Prevalence numeric only when countable; otherwise qualitative + explicit uncertainty
  - Participants/date fields “unknown” when not provided
- **Why**: Removes template-driven pressure to invent specificity.

### D) Connector-based validation introduces a second posture mid-stream
- **Change**: Kept connectors as explicitly **optional triangulation** with a “only if actually available” instruction and a “label what came from where” rule.
- **Why**: Reduces posture drift into verification/analytics when the task is primarily synthesis.

### Seeds vs lenses (prompt was structure-heavy, lens-light)
- **Change**: Added a small set of investigative lenses (workarounds, expectation gaps, contradictions, emotion triggers, context constraints, mental models).
- **Why**: Encourages emergence beyond “standard UX synthesis” patterns without seeding specific themes.

### Numeric anchors and fixed-slot anchors
- **Change**: Removed implied fixed counts (themes, quotes per theme, recommendations) by reframing the output as a guide and repeatedly signaling “as many/few as evidence supports.”
- **Why**: Restores natural variation and reduces slot-filling behavior.

## Preserved from original

- Core purpose, accepted input types, and stakeholder-ready markdown deliverable.
- Emphasis on evidence (quotes/behaviors) and separating observation from interpretation.

## Expected behavioral shift (what to watch for when testing)

- More emergence and explicit tensions/contradictions.
- Fewer “perfect” prevalence numbers and attributable quotes when metadata is missing.
- Recommendations that are better grounded in evidence and clearer about confidence/uncertainty.
