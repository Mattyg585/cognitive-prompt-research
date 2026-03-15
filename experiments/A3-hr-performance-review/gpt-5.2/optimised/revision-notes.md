---
model: GPT-5.2
date: 2026-03-15
experiment: A3
tier: 2
artifact: revision-notes
---

# A3 Tier 2 (Optimised) — Revision Notes

## Goal
Preserve the skill’s primary function (a clean performance-review **template generator**) while reducing:
- premature evaluative convergence (rating/comp/distribution)
- numeric anchoring (fixed counts / fixed sentence lengths)
- connector hallucination risk

This revision implements the Prompt Architect’s recommended prompt-level interventions without turning the skill into a heavy “analysis agent.”

## What changed (mapped to architect findings)

### 1) Evaluation posture bleeding into generation (Manager template)
**Architect finding:** Rating/comp fields adjacent to narrative boxes pull the model into HR-decision posture and invite premature convergence.

**Change implemented:**
- Added **Operating rules**: “Default = template, not verdicts” and “Only include/complete evaluative fields when inputs exist.”
- Moved rating/comp into an explicitly **optional** section: “Rating & Compensation (optional — only if you have rubric + evidence).”
- Added explicit instruction to **leave blank or omit** if rubric/evidence is missing.

### 2) Connectors introduce investigation without boundaries
**Architect finding:** Retrieval (if available) can mix with evaluation anchors; also risk of implying data was fetched.

**Change implemented:**
- Added **Connector honesty** rule: don’t claim data was pulled unless tools are truly available.
- Updated connector section to explicitly instruct: if unavailable, **ask the user to paste** the missing info or keep placeholders.

### 3) Output structure encourages box-filling + fixed counts
**Architect finding:** Fixed slots (3 goals, 3–5 accomplishments, 2–3 sentences) bias outputs toward uniform counts.

**Change implemented:**
- Replaced fixed-count language with **repeatable 0–N** sections (accomplishments, strengths, development areas, discussion points).
- Converted “Goals for Next Period: 1..2..3” into a **table with unlimited rows**.
- Replaced “2–3 sentence overall assessment” with “brief paragraph,” allowing natural variation.

### 4) Calibration targets act as numeric anchors
**Architect finding:** Target distribution percentages can become an anchor that pulls recommendations toward the numbers.

**Change implemented:**
- Reframed the distribution table as **“reference, not a target”** with an explicit note:
  - do not bend assessments to fit percentages
  - treat targets as a discussion constraint, not an optimization goal

### 5) Seed-only templates lacking upstream lenses
**Architect finding:** Tips exist but aren’t integrated; the skill can produce generic filler without minimal context.

**Change implemented:**
- Added **Quick intake** (minimal, conditional) questions to gather role/level, review period, rubric, and notes **only when needed**.
- Elevated “Tips” into **lenses** (evidence-first, behaviors+impact, separate evidence from decisions).

## Expected behavior changes (diagnostics)
When testing this Tier 2 prompt, look for:
- **Natural variation**: outputs shouldn’t always contain the same number of goals/accomplishments.
- **No invented ratings**: ratings/comp should remain blank/omitted unless rubric + evidence is provided.
- **Evidence-first content**: examples and artifacts appear before conclusions (especially in manager mode).
- **Calibration independence**: assessments shouldn’t drift toward the reference percentages unless the user explicitly wants to reason about constraints.
- **No connector hallucination**: the model should ask for pasted data rather than claiming retrieval.

## Trade-offs
- Slightly less “instant completion” (because rating/comp is gated behind rubric/evidence).
- Slightly more interaction when the user wants a populated draft (Quick intake), but blank-template generation remains immediate.
