---
model: GPT-5.2
date: 2026-03-15
experiment: A5
tier: optimised
artifact: revision-notes
---

# Revision Notes — A5 Engineering Debug (Tier 2)

## Finding → Change mapping

### A) Investigation was coupled to fix generation (solution-shaped investigation) (High)

**Finding (architect):** Mandatory “Root Cause + Fix + Prevention” sections pressure premature convergence so the model can complete the deliverable.

**Change:** Added explicit **evidence gating** and two output containers:

- **Debug Snapshot** when evidence is incomplete: competing hypotheses + discriminating next checks.
- **Debug Report** only when diagnosis is grounded: root cause mechanism + fix plan + prevention.

**Rationale:** Keeps investigation open-ended until the information state supports convergence.

### B) “Interactive session” vs “final report” stance tension (Moderate–High)

**Finding (architect):** The prompt asks for a structured debugging session but forces a polished report artifact, encouraging authoritative conclusions under uncertainty.

**Change:** Reframed the skill as **investigation-first**, with explicit permission to stay in “snapshot” mode and ask targeted questions. The report format is now conditional.

**Rationale:** Preserves collaborative debugging posture and reduces pressure to fabricate completeness.

### C) Mechanical step sequencing reduced responsiveness (Moderate)

**Finding (architect):** A rigid numbered workflow can push “process execution mode” even when the user’s context warrants jumping ahead.

**Change:** Replaced the fixed 4-step diagram with **typical phases (reference, not a mandatory order)** plus a rule that **the user drives sequencing**.

**Rationale:** Keeps structure as a lens without forcing a one-size-fits-all flow.

### D) Template-filling hallucinations under uncertainty (High)

**Finding (architect):** Fixed schema slots can cause invented content (“Steps: …”) when the user didn’t provide it.

**Change:** Added a **Facts vs Inferences vs Assumptions** rule, plus a quality bar that explicitly discourages filling sections without evidence.

**Rationale:** Makes the container responsive to available information and encourages uncertainty disclosure.

## Additional edits

- Clarified that mitigations are optional and should be **safe and reversible** when evidence is incomplete.
- Adjusted connector guidance to treat correlations as **hypotheses until confirmed**, reducing narrative lock-in.

## What to watch in run output

1. For sparse inputs (one-line error), the assistant should produce **Debug Snapshot** (hypotheses + next checks), not a full root cause + fix.
2. When evidence is rich (reproducer/logs/correlation), the assistant should transition to **Debug Report** with a mechanism-grounded diagnosis.
3. “Observed Facts” should contain only user-provided or connector-derived signals (no invented reproduction steps).
