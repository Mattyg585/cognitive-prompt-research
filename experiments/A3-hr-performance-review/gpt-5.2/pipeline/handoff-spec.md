---
model: GPT-5.2
date: 2026-03-15
experiment: A3
artifact: handoff-spec
tier: pipeline
---

# A3 Tier 3 Pipeline Handoff Spec — `/performance-review` (all modes)

## Pipeline overview

This pipeline generates performance-review artifacts while **separating incompatible cognitive modes**:
- **Orchestration / intake** (routing + gathering context)
- **Investigation / evidence structuring** (what happened; what’s observable)
- **Template generation** (structured writing, placeholders)
- **Evaluation / calibration** (ratings, comp actions, distribution constraints)
- **Final assembly** (merge + polish without adding new judgments)

It supports all `/performance-review` modes:
- `self-assessment`
- `manager [employee]`
- `calibration`

## Stage sequence (filenames)

1. `stage-1-review-router.md` (+ `stage-1-review-router.agent.md`)
2. `stage-2-context-intake.md` (+ `stage-2-context-intake.agent.md`)
3. `stage-3-evidence-dossier.md` (+ `stage-3-evidence-dossier.agent.md`)
4. `stage-4-template-drafter.md` (+ `stage-4-template-drafter.agent.md`)
5. `stage-5-evaluation-calibration.md` (+ `stage-5-evaluation-calibration.agent.md`) — **conditional**
6. `stage-6-final-editor.md` (+ `stage-6-final-editor.agent.md`)

## Conditional execution rules

- **Self-assessment mode**: run stages **1 → 2 → 3 → 4 → 6**.
  - Stage 5 is skipped unless the user explicitly asks for self-rating or promotion/comp framing (in which case Stage 5 may be run, but must still request a rubric and guard against premature rating).

- **Manager review mode**: run stages **1 → 2 → 3 → 4 → 5 → 6**.

- **Calibration mode**: run stages **1 → 2 → 3 → 4 → 5 → 6**.
  - Stage 5 is where distribution targets, trade-offs, and edge cases are handled.

## Strict stage boundaries (input / output contracts)

### Stage 1 — Review Router
**Primary mode**: Orchestration (routing only)

**Receives**: the user’s initial request.

**Produces**:
- `ROUTING_DECISION` (mode + intended deliverable)
- `INTAKE_REQUEST` (what Stage 2 should ask for)

**Forbidden**:
- Drafting any template sections
- Any rating / compensation / distribution recommendations

---

### Stage 2 — Context Intake
**Primary mode**: Investigation + light structuring (no evaluation)

**Allowed inputs**:
- User-provided facts (role/level, period, goals, projects, feedback snippets)
- Connector/tool availability claims **as stated by the user**

**Produces**:
- `REVIEW_CONTEXT` (YAML packet)
- `RAW_NOTES` (verbatim or lightly cleaned notes)
- `OPEN_QUESTIONS` (only if needed)

**Forbidden**:
- Assigning ratings or proposing comp actions
- Using calibration “company targets” as defaults (those belong in Stage 5)
- Claiming any connector retrieval occurred unless tool outputs are explicitly provided

---

### Stage 3 — Evidence Dossier
**Primary mode**: Investigation → compression (evidence extraction and example shaping)

**Allowed inputs**:
- `REVIEW_CONTEXT` + `RAW_NOTES` from Stage 2

**Produces** (structured, mode-stripped):
- `EVIDENCE_ITEMS` table (observable behavior + impact + context)
- `THEMES` (emergent patterns; no judgment)
- `GAPS` (missing evidence areas to request)

**Forbidden**:
- Overall rating labels (Exceeds/Meets/Below)
- Compensation / promotion decisions
- Calibration distribution recommendations

---

### Stage 4 — Template Drafter
**Primary mode**: Structuring + constrained generation (template writing)

**Allowed inputs**:
- `REVIEW_CONTEXT`
- `EVIDENCE_ITEMS` / `THEMES` (structured only)

**Produces**:
- A **mode-appropriate draft artifact** in Markdown:
  - Self-assessment template OR
  - Manager review draft **without ratings/comp populated** OR
  - Calibration prep draft **without distribution decisions populated**

**Hard requirements**:
- **Remove numeric anchors**: avoid “3 goals”, “top 3–5 accomplishments”, “2–3 sentences”. Use optional, repeatable slots (“Add as many as needed”).
- **Evidence-first ordering** for manager reviews: narrative and evidence sections come before rating/comp sections (which remain blank placeholders pending Stage 5).
- **Connector boundary**: never imply data was pulled; include “Source: (user-provided / tool-provided)” fields if relevant.

---

### Stage 5 — Evaluation & Calibration (conditional)
**Primary mode**: Evaluation + synthesis (judgment under explicit rubrics)

**Allowed inputs**:
- Stage 2 `REVIEW_CONTEXT` (including rubric/expectations if provided)
- Stage 3 `EVIDENCE_ITEMS` / `THEMES`
- Stage 4 draft (for placement only; do not let its headings drive evaluation)

**Produces**:
- `EVALUATION_DECISIONS` (rating, goal assessments, promotion/comp recommendation) **with rationale grounded in evidence**
- For calibration: `DISTRIBUTION_SUMMARY` + `DISCUSSION_CASES`

**Forbidden**:
- Backfilling evidence to justify a desired outcome
- Treating company target %s as default truth; they are constraints to confirm and, if used, to **reason about explicitly**

---

### Stage 6 — Final Editor
**Primary mode**: Assembly + reframing (no new judgments)

**Allowed inputs**:
- Stage 4 draft artifact
- Stage 5 decisions (if run)

**Produces**:
- Final, clean Markdown deliverable

**Forbidden**:
- Introducing new evaluative claims, ratings, or comp actions not present in Stage 5
- Inventing evidence, metrics, or tool pulls

## Why this pipeline split (ties to architect findings)

- Prevents **evaluation posture** (ratings/comp/distribution) from shaping what counts as “evidence” during investigation.
- Reduces **numeric anchoring** by moving template drafting later and making slots optional.
- Adds a **connector boundary**: any retrieval claims must be explicit and sourced.
- Treats calibration targets as **adjustable constraints** (Stage 5) rather than a template default (Stage 4).
