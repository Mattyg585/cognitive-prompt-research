# A5 Tier 3 Pipeline — Engineering Debug

This pipeline separates incompatible debugging modes into clean contexts to avoid solution-shaped investigation and template-filling under uncertainty.

## Sequence (filenames)

1. `01-hypothesis-generation` (hypotheses + discriminators)
2. `02-evidence-gathering` (collect/inspect evidence; update hypotheses)
3. `03-fix-plan` (choose fix strategy + test plan)
4. `04-verification` (verify fix; regression + rollback readiness)

Each stage produces a **Handoff Packet** designed to be pasted into the next stage with minimal cognitive residue.

---

## Execution model

**Default:** sequential.

**Allowed loops:**
- If `04-verification` fails, hand back to `03-fix-plan` (or `02-evidence-gathering` if the failure indicates missing/ambiguous evidence).
- If `02-evidence-gathering` can’t collect decisive evidence, it should request the minimal additional evidence and pause (do not guess a root cause).

---

## Handoff contracts (what crosses, what gets dropped)

### 01 → 02 (Hypotheses → Evidence)

**Crosses (structured):**
- Problem statement (expected vs actual)
- Environment + recent changes (if known)
- Hypotheses list with discriminators
- Prioritised evidence checklist (what would confirm/deny)
- Clarifying questions for user

**Dropped:**
- Any fix ideas, patch sketches, or “what I would change” language.
- Polished narrative conclusions.

**Format:** `Hypothesis Packet` (see `01-hypothesis-generation` prompt).

### 02 → 03 (Evidence → Fix Plan)

**Crosses (structured):**
- Evidence digest (facts only, with references)
- Updated hypothesis status (supported / weakened / unknown)
- Candidate root cause(s) with confidence level + missing evidence
- Constraints (time, risk tolerance, deployment constraints)

**Dropped:**
- Exploratory wandering, long investigative prose.
- Unscoped fix brainstorming.

**Format:** `Evidence Packet` (see `02-evidence-gathering` prompt).

### 03 → 04 (Fix Plan → Verification)

**Crosses (structured):**
- Selected root cause + evidence references
- Fix steps (ordered) + risk notes
- Test plan (commands, expected outcomes, rollback triggers)
- Observability plan (what metrics/logs confirm success)

**Dropped:**
- Hypothesis alternatives that weren’t chosen (keep only brief “rejected alternatives” if important for context).

**Format:** `Fix Plan Packet` (see `03-fix-plan` prompt).

### 04 → (Exit or Loop)

**Crosses back to 03 (if fail):**
- What verification failed (exact symptom)
- What changed (what was applied)
- New evidence produced during verification
- Updated diagnosis (if verification falsified the selected root cause)

**Dropped:**
- Blameful language; avoid rewriting history.

**Format:** `Verification Packet` (see `04-verification` prompt).

---

## Storage / sharing guidance

- Keep packets **copy/paste friendly**.
- Use citations for any concrete evidence (paths + line ranges; command + output snippet; log timestamp).
- Separate **Observed facts** from **Inferences** in every packet.
- Make sections **conditional**: if unknown, say `Unknown` and list the smallest next check.
