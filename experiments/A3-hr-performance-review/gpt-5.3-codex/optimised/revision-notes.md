---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A3
artifact: revision-notes
tier: optimised
---

# Revision Notes: A3 Optimised Prompt

## Finding → change mapping

### 1) Evaluation anchoring
- **Finding:** rating pressure can distort evidence collection.
- **Change:** explicit investigation-first instructions and rating moved to end.
- **Rationale:** evaluation becomes a conclusion, not a starting premise.

### 2) Slot-count anchoring
- **Finding:** fixed counts produce templated uniformity.
- **Change:** “as many/few as evidence warrants” for strengths/development/goals.
- **Rationale:** output volume should follow evidence complexity.

### 3) Weak investigation behavior
- **Finding:** original prompt over-specifies format, under-specifies analysis lens.
- **Change:** six investigation lenses added (trajectory, scope, ambiguity, stakeholder translation, sustainability, contradictions).
- **Rationale:** preserves structure while improving quality of thought before writing.

### 4) Calibration target contamination
- **Finding:** target ranges can become optimization goals.
- **Change:** ranges reframed as reference context only.
- **Rationale:** protects fairness and factual reporting in calibration prep.

## Expected impact in runs

- Better handling of mixed signals (initiative vs ambiguity tolerance).
- More tailored development plans.
- Improved fairness-sensitive language (behavior-focused, evidence-linked, lower assumption risk).

