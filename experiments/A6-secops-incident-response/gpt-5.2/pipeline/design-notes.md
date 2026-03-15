# A6 SecOps Incident Response — Tier 3 Pipeline (Design Notes)

## Goal
Produce a post-incident analysis that is (1) evidence-grounded, (2) causally honest (branching, natural depth), (3) explicit about systemic contributors, and (4) converted into organisational learning and actions **without contaminating upstream investigation**.

## Why a pipeline (and why these four stages)
The original A6 skill mixes timeline, root-cause investigation, evaluation, action planning, and synthesis in one context, and anchors causality with a fixed **5 Whys** template. Architect findings show this creates:
- **Evaluation bleed** into investigation (judging language shapes what “counts” as cause)
- **Solution-shaped investigation** (root causes chosen because they map cleanly to tickets)
- **Premature convergence** (lessons learned narrative back-fills earlier sections)
- **5-Whys double anchor** (numeric + linear chain forces tidy but false structure)

This Tier 3 pipeline separates the prompt into four incompatible postures:
1. **Evidence reconstruction**: divergent “what happened?” with light structuring.
2. **Causal analysis**: deep investigation + model-building, explicitly avoiding actions/evaluation.
3. **Contributing factors/systemic issues**: broader systems lens and categorisation, still no actions.
4. **Organisational learning/actions**: generation and reframing, where actions are finally allowed.

## Handoff design (mode stripping)
Each stage ends with a **single structured YAML block** intended to be the only thing passed forward.
- Structured artifacts strip exploratory tone and reduce cross-mode residue.
- The schema is designed to be **responsive** (unknowns allowed) to reduce template-filling confabulation.

## Avoiding 5 Whys anchoring
Stage 02 uses a **branching causal map** (paths + hypotheses) rather than a fixed-depth chain.
- Natural depth: stop when the next step is unsupported or becomes a broader org decision.
- Branches: allow multiple preconditions/controls/failures to contribute to the outcome.

## Human factors without blame
To avoid “blameless ⇒ ignore people,” Stage 02 includes a **decision_environment** section:
- What was known at the time
- Constraints and pressures
- Why the decision made sense then (systems framing)

This preserves learning about decision-making while avoiding individual blame.

## Uncertainty and provenance
To reduce operationally harmful invention (times, owners, impacts):
- Stage 01 requires evidence refs and confidence labels.
- All stages permit `unknown` / `needs confirmation`.
- Stage 04 forbids fabricated owners/dates: use `TBD` unless provided.

## What this pipeline does *not* do
- Live incident triage, paging, or status updates (operational mode).
- Severity classification (SEV) during postmortem drafting.

Those are valuable in an incident commander workflow, but they contaminate reflective postmortem cognition if kept in-context.
