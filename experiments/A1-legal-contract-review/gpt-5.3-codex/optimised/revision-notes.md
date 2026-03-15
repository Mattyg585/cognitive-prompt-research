---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A1
artifact: revision-notes
---

# Revision Notes (A1 Optimised Prompt)

## Finding → Change → Rationale

| Finding from analysis | Change in optimised prompt | Rationale |
|---|---|---|
| Investigation and evaluation were fused | Added explicit Step 4 scope boundary: understand contract before any classification | Prevents evaluation criteria from pre-filtering discovery |
| Heavy seeded issue lists constrained discovery | Replaced exhaustive "common issue" seeding with lens questions; kept compact clause guidance | Preserves systematic coverage while enabling novel findings |
| Numeric anchors caused count uniformity | Removed "Top 3-5" style requirements | Allows output depth/count to vary with contract complexity |
| Rigid template flattened priority | Added proportional-depth guidance and permission to group low-risk clauses | Focuses effort where risk is material |
| Redline drafting became generic | Explicitly ties redline calibration to side, relationship, deadline, and focus areas | Increases practical negotiation fit |
| Strategy often restated classifications | Added strategic synthesis requirement centered on counterparty modeling and sequencing | Drives real strategy rather than summary repetition |

## What was intentionally preserved

- Core legal workflow (context gathering, clause analysis, redlines, strategy)
- GREEN/YELLOW/RED triage model
- Requirement to quote contract language in redline work
- Clear non-legal-advice disclaimer

## Test expectations

1. Better risk discovery outside standard categories.
2. Greater run-to-run variation in finding counts and emphasis.
3. Redlines more tailored to deal context.
4. Strategy sections less templated and more negotiation-aware.
