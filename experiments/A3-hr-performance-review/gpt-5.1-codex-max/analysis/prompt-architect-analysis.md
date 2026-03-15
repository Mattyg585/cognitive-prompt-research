---
model: GPT-5.1-Codex-Max
date: 2026-03-15
experiment: A3
tier: analysis
---

# Prompt Architect Analysis — experiments/A3-hr-performance-review/original/SKILL.md

## 1) What the prompt is actually asking for (cognitive posture)
- Primary posture: **Convergent structuring + generation** — produce structured templates for three modes (self-assessment, manager review, calibration) with fixed sections and tables (e.g., rating fields, goal tables, compensation recommendation).
- Secondary posture: **Evaluation framing baked into templates** — rating labels (“Exceeds / Meets / Below”), compensation recommendations, and rating distributions embed evaluative posture even when the task is ostensibly template generation.
- Light **investigation scaffolding**: asks to pull prior review history or project data if connectors exist, but this is additive context, not open exploration.
- Overall: a generator of forms that already presume evaluation workflows and normative distributions.

## 2) Where modes interfere or create risks (with fairness/bias notes)
- **Evaluation framing inside generation**: Even when only generating templates, the inclusion of ratings, compensation decisions, and rating distributions sets an evaluative posture. For users expecting neutral scaffolding, this preloads judgments (risk: premature evaluation bias).
- **Numeric anchors**: Calibration rating distribution table supplies target percentages (~15–20% Exceeds, ~60–70% Meets, ~10–15% Below). This is a strong anchoring cue that can bias reviewers toward quota-like distributions (fairness risk: pressures outcomes independent of actual performance).
- **Seeds vs lenses**: Templates seed specific sections (e.g., “Key Strengths”, “Areas for Development”, compensation recommendation). This is appropriate for convergent structuring, but combined with the evaluative posture it may suppress alternative framings (e.g., strengths-based vs deficit-first) and lead to confirmation bias.
- **Compensation + performance coupling**: Co-locating compensation recommendations within the performance template invites financial judgment in the same pass as performance reflection (risk: over-coupling and potential disparate impact if upstream bias exists).
- **Calibration prompts**: “Discussion points” and “Promotion candidates” are fine, but the embedded distribution targets plus promotion/comp tables encourage comparison framing that can amplify systemic bias if evidence quality is uneven.
- **Fairness/EEO sensitivity**: No explicit guardrails against protected-class inferences; templates invite free-text notes, which could capture biased rationales. Absent prompts to cite objective evidence, risk of subjective or demographic proxies entering summaries.

## 3) What to check for in output (diagnostics)
- Does the model **bake in target counts** (e.g., always present three strengths/areas, fixed number of calibration discussion points, or default to midpoints of the suggested distribution)?
- Do generated templates **presuppose ratings/comp outcomes** (e.g., inserting default categories or language that nudges to “Meets”/quota percentages)?
- Are there **implicit fairness cues missing** (e.g., lack of reminders to use evidence, avoid protected-class references)? Look for outputs that normalize quota thinking or compensation linkage without justification.
- Is the **manager template** pulling the user into evaluative tone even when they only wanted structure (e.g., language that assumes judgments already made)?

## 4) What to do about it (prompt-level, not rewriting here; handoff to prompt-writer)
- Prompt-level mitigations to consider:
  - Separate **neutral scaffolding** from **evaluative posture**: keep template generation neutral; let users add rating frames explicitly when desired.
  - Soften or gate **numeric anchors**: make distribution targets optional context rather than default sections; avoid ranges that become anchors.
  - Add **evidence-first lenses**: encourage “evidence + examples” before ratings/comp to reduce subjective bias; nudge against protected-class references.
  - Decouple **compensation** from initial performance write-up (or make it an optional add-on section).
- No pipeline-level issues (single skill). Composition signature: Base skill = convergent structuring with embedded evaluation anchors; no additional skills referenced.

**Ready for handoff to `prompt-writer` to implement adjustments while preserving scope.**
