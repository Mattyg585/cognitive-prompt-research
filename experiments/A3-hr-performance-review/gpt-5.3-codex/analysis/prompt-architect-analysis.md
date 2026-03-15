---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A3
artifact: prompt-architect-analysis
---

# Prompt Architect Analysis: A3 HR Performance Review

Source prompt analysed: `experiments/A3-hr-performance-review/original/SKILL.md`

## 1) Required thinking modes

The original SKILL combines three operational modes:

1. **Self-assessment template generation** (mostly convergent generation).
2. **Manager review writing** (investigation + evaluation + synthesis + generation).
3. **Calibration prep structuring** (structuring + evaluation).

The manager review path is the cognitively dense path and the primary source of interference.

## 2) Interference points in the original prompt

### A. Evaluation anchor appears too early in manager review

The manager output template places `Overall Rating` before evidence-heavy sections in practice.  
This creates confirmation pressure: once a rating is picked, later sections may be selected to justify it.

### B. Numeric slot anchors flatten evidence-proportional output

Examples in the original prompt encourage fixed counts (e.g., fixed strengths/development bullets).  
This risks producing uniform reviews across employees even when evidence complexity differs.

### C. Investigation guidance is weak relative to template guidance

The prompt strongly specifies structure but under-specifies how to investigate contradictory evidence, trajectory, and scope-level readiness.

### D. Calibration targets can become optimization goals

Distribution references are useful context, but if framed as columns/targets they can bias toward “fitting the curve” rather than reporting true team distribution.

## 3) Diagnostic predictions

If interference is active, outputs will show:

- Similar section counts regardless of employee profile.
- Rating language that appears settled before evidence synthesis.
- Generic development actions (“improve communication”) not tied to concrete incidents.
- Weak treatment of tensions (e.g., high initiative on concrete work + stalling on ambiguous work).

## 4) Prompt-level interventions (Tier 2)

1. Move rating to the end, after evidence and synthesis.
2. Replace fixed slot counts with “as many/few as evidence warrants.”
3. Add explicit investigation lenses:
   - trajectory,
   - ambiguity handling,
   - stakeholder translation,
   - team multiplier effects,
   - sustainability/capacity signaling.
4. Keep calibration distribution as reference prose, not structural target.

## 5) Pipeline interventions (Tier 3)

Split manager review into two contexts:

- **Stage 1 — Performance Investigator:** investigates raw observations, surfaces patterns/tensions, no rating/compensation.
- **Stage 2 — Review Writer:** synthesizes from structured findings, then assigns rating and recommendations.

This directly isolates the toxic pair: investigation contaminated by evaluation/template pressure.

## 6) Expected A3 outcome pattern

A3 is a calibration case (template-heavy domain), so expected gains are moderate rather than extreme:

- Tier 2 should improve specificity and reduce anchor artifacts.
- Tier 3 should produce the cleanest handling of contradictions and fairness-sensitive framing, especially around level readiness vs. promotion timing.
