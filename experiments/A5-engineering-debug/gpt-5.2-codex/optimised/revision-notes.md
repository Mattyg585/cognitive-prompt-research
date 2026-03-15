---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A5
tier: optimised
run: 0
---

# Revision Notes — /debug (Tier 2 Optimised)

## Summary of changes
- Added an explicit **scope boundary**: investigate first; do not diagnose or fix without evidence.
- Made **diagnosis and fix conditional**, with a hypotheses section for incomplete evidence.
- **Softened the template** so sections can be skipped or marked unknown rather than forced.
- Reframed the **step list as a non-linear reference**, with the human driving order.

## Mapping to architect findings

1. **Investigation + generation interference**
   - Change: Added “Investigate first” boundary and made Fix conditional on supported root cause.

2. **Investigation + synthesis (premature root cause)**
   - Change: Added Hypotheses section with confidence and evidence gaps; Root Cause only when confident.

3. **Template-driven convergence**
   - Change: Output is explicitly responsive; sections are optional, with “unknown/insufficient evidence” allowed.

4. **Numbered step sequence in an interactive setting**
   - Change: Steps rephrased as typical phases (non-linear reference), and user can skip/reorder.

## What to watch for when testing
- Root causes or fixes appearing **before** evidence is gathered.
- Sections being filled with **speculation** when inputs are sparse.
- Outputs that ignore **open questions** and force closure.
- Lack of natural variation (all reports look identical regardless of input complexity).
