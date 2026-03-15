# Design Notes — A5 Tier 3 Debugging Pipeline

## Why a pipeline (vs a single /debug prompt)
The original A5 “/debug” skill compresses reproduction → diagnosis → fix into one pass with a mandatory report container. The Prompt Architect analysis flags the resulting interference:
- **Investigation + generation**: pressure to commit early so a fix can be produced.
- **Interactive session vs final report**: stance drift into authoritative conclusions under thin evidence.
- **Template-filling**: fixed slots (“Root Cause”, “Fix”, “Prevention”) invite hallucinated completeness.

This Tier 3 pipeline uses **clean context boundaries** to separate incompatible modes and replaces fixed-slot reporting with **conditional, evidence-gated packets**.

## Cognitive-mode mapping

1) **01-hypothesis-generation**
- Mode: Divergent investigation + light structuring.
- Goal: widen the search space without proposing fixes.

2) **02-evidence-gathering**
- Mode: Investigation (empirical, citation-first) + light structuring.
- Goal: turn “possible causes” into evidence-backed candidates.

3) **03-fix-plan**
- Mode: Convergent generation (design a change) + evaluation (risk/side effects).
- Goal: pick a fix strategy only after evidence is adequate.

4) **04-verification**
- Mode: Convergent verification.
- Goal: confirm the fix and guard against regressions; if falsified, loop back.

## Key mechanisms (implemented)

### 1) Evidence gating
Each stage has explicit “do not proceed unless…” criteria:
- Fix planning requires a *named hypothesis* plus *referenced evidence*.
- Verification requires *explicit expected outcomes* and *rollback triggers*.

### 2) Facts vs inferences separation
Every packet requires:
- **Observed facts** (from user/tools, cited)
- **Inferences** (clearly labeled)

This directly counters template-filling and overconfident root-cause claims.

### 3) Structured handoffs strip cognitive residue
Handoffs are bullet/record oriented (packets) rather than narrative. This reduces mode-carryover (e.g., fix language contaminating investigation).

### 4) Human-driven progression
Even though this is a pipeline, the prompts assume interactive debugging:
- Agents ask for the **minimum additional evidence** required.
- Sections are conditional; “Unknown” is acceptable and actionable.

## How to run

1. Start with `01-hypothesis-generation` using the user’s problem description and any artifacts.
2. Paste its `Hypothesis Packet` into `02-evidence-gathering` along with logs/code/stack traces.
3. Paste the resulting `Evidence Packet` into `03-fix-plan`.
4. Paste the `Fix Plan Packet` into `04-verification` and execute the test/verification plan.

## Success signals
- Natural variation: sometimes the right output is “we don’t know yet; here are the discriminating checks.”
- Hypotheses get falsified explicitly.
- Fix details appear **only** after evidence is grounded.
- Verification produces crisp pass/fail with cited outputs.
