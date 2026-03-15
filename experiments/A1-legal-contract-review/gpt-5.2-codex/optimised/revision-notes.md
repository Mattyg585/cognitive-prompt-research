---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A1
tier: optimised
run: 0
---

# Revision Notes — A1 Legal Contract Review (Tier 2)

## Summary of changes
- Added a **two-pass structure**: a descriptive clause map first, then evaluation, then redlines/strategy.
- Removed **numeric anchors** (e.g., fixed “Top 3–5 issues”) and made outputs **adaptive** to contract complexity.
- Reframed the clause checklist as a **coverage lens**, plus an explicit **nonstandard provision lens**.
- Reduced **fill-the-boxes pressure** by allowing optional sections and skipping irrelevant categories.
- Added guidance to **avoid forced redlines** when an issue is strategic/structural.

## Finding → Change mapping

1. **Investigation ↔ Evaluation interference**
   - **Change**: Inserted “Clause Map (Descriptive Only)” before evaluation; explicitly forbids ratings and redlines in that step.
2. **Investigation ↔ Generation interference**
   - **Change**: Moved redlines to a later step; added guidance to flag strategic issues that aren’t language-fixable instead of forcing redlines.
3. **Evaluation ↔ Synthesis (premature convergence)**
   - **Change**: Negotiation strategy and business impact moved to the end, after deviations are classified.
4. **Output structure as convergent pressure**
   - **Change**: Output format is adaptive; sections are optional and counts are variable.
5. **Seeds vs lenses**
   - **Change**: Clause categories reframed as a coverage lens; added explicit lens to surface nonstandard/bespoke provisions.
6. **Numeric anchors / implicit targets**
   - **Change**: Replaced “Top 3–5 issues” with “most material issues” and removed the “50+ pages” threshold.

## What to watch for when testing
- **Uniformity test**: short vs. complex contracts should yield materially different numbers of findings.
- **Checklist saturation**: ensure output doesn’t mirror clause categories when clauses are absent.
- **Missing oddities**: confirm detection of bespoke clauses (e.g., AI training rights, affiliate cross‑use, hidden security addenda).
- **Redline bias**: verify that strategic issues without clean redlines are still surfaced and framed.
