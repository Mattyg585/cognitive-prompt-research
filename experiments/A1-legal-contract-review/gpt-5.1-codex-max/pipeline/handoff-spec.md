---
model: GPT-5.1-Codex-Max
date: 2026-03-15
experiment: A1
tier: pipeline
author: prompt-writer
---

# Handoff Specification — A1 Legal Contract Review

## 00-intake-config → 01-contract-reader
- **Crossing:** Intake config (side, contract type if known, deadline, focus areas), playbook location/absence note, baseline summary (standard positions or “generic standards” flag), file/URL for contract, assumptions list.
- **Format:** Compact YAML block with keys: `party_side`, `deadline`, `focus_areas`, `contract_type`, `playbook_status`, `playbook_summary` (bullet list), `assumptions`, `contract_pointer`.
- **Dropped:** Any dialog text, gating questions, apologies, negotiation advice.
- **Compression:** Keep playbook summary to ≤10 bullets; assumptions as short bullets.

## 01-contract-reader → 02-playbook-comparator
- **Crossing:** Clause map with extracted snippets, presence/absence flags, unlisted/atypical clauses, cross-clause interaction notes.
- **Format:** List of records with fields: `clause_id` (stable label), `location` (section ref), `clause_type` (free text), `snippet` (1–2 sentences), `observations` (bullets), `interactions` (optional bullets). No severity.
- **Dropped:** Any speculative risk judgments, redline ideas, business impact narratives.
- **Compression:** Observations capped to 3 bullets per clause; interactions only if material.

## 02-playbook-comparator → 03-redline-writer
- **Crossing:** Evaluated issues with severity and rationale.
- **Format:** Records for each clause/issue: `clause_id`, `clause_type`, `snippet`, `playbook_delta` (what differs), `severity` (GREEN/YELLOW/RED), `risk_rationale` (2–4 sentences), `evidence` (optional cite/section), `priority_hint` (must/should/nice). Only YELLOW/RED forwarded for redline drafting.
- **Dropped:** GREEN items unless needed for context; any suggested language; negotiation framing.
- **Compression:** Keep `risk_rationale` concise; one evidence cite per issue.

## 03-redline-writer → 04-strategic-advisor
- **Crossing:** Redline packages for YELLOW/RED issues plus brief triage summary.
- **Format:** For each issue: `clause_id`, `clause_type`, `severity`, `risk_rationale` (short), `proposed_redline` (exact language), `fallback` (if applicable), `rationale_for_counterparty` (1–2 sentences), `priority` (must/should/nice), `dependencies` (related clauses). Summary block: `overall_risk`, `key_themes`, `counts` (by severity), `deadline`.
- **Dropped:** Drafting deliberations, alternate phrasings not chosen, exploratory tone.
- **Compression:** Limit proposals to primary + one fallback; keep summary thematic (3–5 bullets).
