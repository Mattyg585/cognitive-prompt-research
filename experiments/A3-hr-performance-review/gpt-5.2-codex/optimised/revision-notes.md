---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A3
tier: optimised
run: 0
---

# Revision Notes — A3 /performance-review (Tier 2)

## Summary
Refined the prompt to keep it strictly template-oriented, reduce evaluation leakage, and loosen numeric anchors while preserving the original structure.

## Changes mapped to architect findings
- **Finding:** Opening line could be interpreted as generating actual feedback (evaluation leakage risk).
  **Change:** Added a scope boundary stating the output is templates only, with explicit rules to avoid assigning ratings or judgments unless the user provides them.
- **Finding:** Template multiplicity may cause mode bleed when the mode is unspecified.
  **Change:** Added an explicit instruction to ask for the mode and output only the selected template.
- **Finding:** Numeric anchors may rigidly fix output counts (e.g., 3–5 accomplishments, 2–3 sentences, fixed % targets).
  **Change:** Replaced fixed counts with “as many as relevant,” removed numbered goal lists, and replaced rating distribution targets with placeholders.
- **Finding:** Risk of fabricated data when connectors are implied.
  **Change:** Added explicit rules to pre-populate only with retrieved data, leave placeholders otherwise, and never fabricate.

## What to watch for in testing
- Ratings and compensation are left as placeholders unless explicitly provided.
- The number of accomplishments/goals varies with input complexity rather than defaulting to fixed counts.
- Only the requested template appears; no bleed from other modes.
- No fabricated “pulled” data when connectors are not actually used.