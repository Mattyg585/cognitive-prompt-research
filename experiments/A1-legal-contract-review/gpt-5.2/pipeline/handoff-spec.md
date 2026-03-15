---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: pipeline
artifact: handoff-spec
---

# A1 Tier 3 Pipeline — Legal Contract Review

## Overview (end-to-end)
A sequential, multi-agent workflow for contract review that **separates investigation → evaluation → drafting → synthesis** to reduce checklist anchoring, solution-shaped discovery, and template-driven hallucination.

## Stage sequence (explicit)
1. `01-intake-and-basis.md` / `01-intake-and-basis.agent.md`
2. `02-contract-map-and-issue-spotting.md` / `02-contract-map-and-issue-spotting.agent.md`
3. `03-playbook-evaluation.md` / `03-playbook-evaluation.agent.md`
4. `04-redline-drafting.md` / `04-redline-drafting.agent.md`
5. `05-negotiation-brief.md` / `05-negotiation-brief.agent.md`

## Artifacts passed between stages (handoff contracts)

### Artifact A — Context & Basis Pack (from Stage 01 → Stage 02)
**Purpose:** isolate orchestration/intake from substantive review.

**Format:** YAML (preferred) or JSON. Keep it short.

**Required fields:**
- `document`:
  - `title_or_id` (string | null)
  - `source` (file | url | pasted_text)
  - `language` (string | null)
- `party_context`:
  - `our_role` (vendor/supplier | customer/buyer | licensor | licensee | partner | other | unknown)
  - `counterparty` (string | null)
- `deal_context`:
  - `deadline` (string | null)
  - `deal_size_or_tier` (string | null)
  - `strategic_importance` (string | null)
  - `focus_areas` (list[string])
- `review_basis`:
  - `basis` (playbook | generic_standards)
  - `playbook_files_used` (list[path])
  - `playbook_found` (bool)
  - `missing_inputs` (list[string])
- `assumptions` (list[string])

**Drop at handoff:** negotiation strategy, severities, redlines, “common issues” checklists.

---

### Artifact B — Contract Map & Evidence Pack (from Stage 02 → Stage 03)
**Purpose:** compress raw contract into a structured map + verbatim evidence blocks so later stages don’t invent quotes.

**Format:** YAML with stable IDs.

**Required fields:**
- `contract_map`:
  - `contract_type_guess` (string | null)
  - `parties` (list[string] | null)
  - `structure`:
    - `sections` (list of `{id, heading, section_ref}`)
    - `exhibits_and_schedules` (list of `{id, title, ref}`)
  - `architecture_lenses`:
    - `order_of_precedence` (present | absent | unclear)
    - `incorporation_by_reference` (present | absent | unclear)
    - `defined_terms_pressure_points` (list[string])
    - `cross_clause_interactions` (list of `{note, refs:[EX-…]}`)
- `evidence_index`:
  - list of verbatim excerpts: `{ex_id: EX-001, section_ref, heading, quote_verbatim, notes}`
- `candidate_issues` (NO severities):
  - list of `{issue_id: I-001, title, description, why_it_matters, evidence_refs:[EX-…], missing_info_questions:[…]}`

**Drop at handoff:** GREEN/YELLOW/RED labels, playbook positions, any proposed clause text.

---

### Artifact C — Evaluated Findings Table (from Stage 03 → Stage 04)
**Purpose:** convergent judgment in a clean context; make drafting downstream deterministic.

**Format:** Markdown table + machine-friendly YAML list.

**Required fields per issue:**
- `issue_id`
- `severity` (GREEN | YELLOW | RED)
- `negotiation_priority` (Must-have | Should-have | Nice-to-have | Escalate)
- `playbook_position` (verbatim from playbook if available; otherwise `GENERIC`)
- `deviation_summary`
- `business_impact`
- `escalation_trigger` (yes/no + reason)
- `evidence_refs` (EX ids only)
- `open_questions` (if any)

**Drop at handoff:** any drafted replacement clause language.

---

### Artifact D — Redline Pack (from Stage 04 → Stage 05)
**Purpose:** generation in isolation; no re-litigating severities.

**Format:** Markdown sections per issue.

**Required fields per issue:**
- `issue_id`
- `clause_ref`
- `current_language` (MUST be verbatim from `evidence_index` via EX refs; if unavailable, mark `NEEDS VERIFICATION`)
- `proposed_redline`
- `fallback_positions` (0+)
- `external_rationale` (shareable)
- `internal_notes` (optional)

**Drop at handoff:** long contract map, raw excerpts beyond those referenced.

---

### Final Output — Negotiation Brief (Stage 05)
**Purpose:** synthesis/reframing for business + counsel; avoid numeric anchors.

**Format:** executive summary + prioritized issue list (no fixed counts) + next steps.

## Execution method
**Default: sequential.** Each stage depends on a compressed artifact from the previous stage.

**Long-contract option:** Stage 02 may be *sharded* by section/exhibit (multiple runs) with a manual merge into one `Contract Map & Evidence Pack` before Stage 03.

## Guardrails applied across the pipeline
- **Evidence integrity:** downstream stages may only quote contract language by referencing `EX-*` excerpts.
- **Playbook integrity:** only assert playbook positions when a playbook is present and cited; otherwise label as `GENERIC`.
- **Anti-anchoring:** no fixed “Top 3” / “3–5 findings” unless the user explicitly requests counts.
- **Mode separation:**
  - Stage 02 does *not* classify or propose fixes.
  - Stage 03 does *not* draft redlines.
  - Stage 04 does *not* change severities.
  - Stage 05 does *not* re-open clause analysis; it summarizes and plans.
