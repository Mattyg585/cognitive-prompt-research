---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A4
tier: optimised
run: 0
---
# Revision Notes — research-synthesis (Tier 2)

## Summary
- Removed numeric anchors and fixed slots.
- Reordered sections to synthesize before summarizing.
- Added explicit scope boundaries to keep synthesis separate from evaluation/generation.
- Made impact/effort and recommendations optional with uncertainty handling.

## Findings → Changes
1. **Premature narrative commitment** → Moved Executive Summary after Key Themes and instructed it to be written after synthesis.
2. **Numeric anchors (themes/recs/length)** → Replaced numbered slots with “as many as warranted” guidance; removed fixed 3–4 sentence length.
3. **Evaluation/generation pre-filtering** → Added “Synthesize first / Translate second” boundary; Impact/Effort is optional and can be Unknown.
4. **Missing ambiguity signals** → Added explicit uncertainty guidance and reinforced Questions for Further Research.

## What to Watch For
- Theme and recommendation counts should vary with input complexity.
- Insights should include messy or ambiguous findings, not only action-ready items.
- Executive Summary should reflect themes, not dictate them.
- Impact/Effort should be Unknown when evidence is thin.
