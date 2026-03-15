---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A1
tier: pipeline
run: 0
---

# Handoff Spec — A1 Legal Contract Review

## 1) clause-mapper → playbook-evaluator

**What crosses**
- Clause Map entries with:
  - Section reference
  - Clause name
  - Plain-language summary
  - Key obligations/rights
  - Dependencies/cross‑references
  - Short excerpt (if available)
- Nonstandard/bespoke provisions (descriptive only)
- Missing-but-expected clauses (descriptive only)
- Deal context and party side

**Format**
- Structured list or table (no prose narrative).

**What gets dropped**
- Any evaluative language
- Any recommendations or redlines
- Any severity labels

**Compression checkpoint**
- Summaries should be concise; avoid full clause text.

---

## 2) playbook-evaluator → redline-strategist

**What crosses**
- Deviations list with:
  - Clause reference/name
  - Classification (GREEN/YELLOW/RED)
  - Playbook position / target state
  - Deviation summary
  - Business impact / risk
  - Priority (if assigned)
  - Reference to clause excerpt
- Any explicit escalation triggers

**Format**
- Structured list or table, ordered by materiality.

**What gets dropped**
- Exploratory notes from clause mapping
- Re-explanations of contract background
- Any drafting language from evaluation

**Compression checkpoint**
- Keep deviations concise; ensure each item is self-contained and references the relevant excerpt.
