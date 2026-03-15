# Pipeline Design Notes: A5 Engineering Debug (GPT-5.3-Codex)

## Why this pipeline

The original task mixes two modes in one context:

- investigation (reproduce/isolate/diagnose),
- intervention design (fix/prevention).

That encourages diagnosis to converge prematurely on fixable explanations. Splitting these modes removes fix pressure during investigation.

## Why only two stages

Reproduce, isolate, and diagnose are mutually compatible investigative tasks and benefit from shared context. Splitting them further adds overhead without reducing interference.

Similarly, fix design and prevention planning are both convergent and compatible.

So two stages are the minimum effective architecture:

- **Investigator** (divergent evidence work)
- **Fix Designer** (convergent intervention work)

## Handoff philosophy

Structured findings (facts, hypotheses, confidence, blast radius) cross the boundary.
Investigative tone and exploratory residue do not.

This keeps Stage 2 focused on intervention quality rather than re-diagnosis.

## Success criteria for this calibration case

Compared to baseline and Tier 2:

1. broader hypothesis coverage,
2. clearer trigger vs root cause separation,
3. better fix-level matching (systemic causes -> systemic controls),
4. more concrete verification and prevention.

