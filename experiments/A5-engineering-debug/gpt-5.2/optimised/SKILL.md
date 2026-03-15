---
model: GPT-5.2
date: 2026-03-15
experiment: A5
tier: optimised
artifact: SKILL
---

---
name: debug
description: Investigation-first debugging session with explicit evidence gating; produces hypotheses and next checks when uncertain, and a fix plan only when grounded.
argument-hint: "<error message or problem description>"
---

# /debug

Run an investigation-first debugging session. We’ll keep uncertainty explicit and only converge on “root cause + fix” when the evidence supports it.

## Usage

```
/debug $ARGUMENTS
```

## Core rules (mode boundaries)

1) **Investigation comes first.** Prioritize understanding and discriminating tests over proposing fixes.

2) **Evidence gating:**
- If we **cannot** reproduce or otherwise ground the diagnosis in concrete signals, do **not** present a single definitive root cause or a detailed fix.
- Instead, produce **competing hypotheses + the next checks** that would confirm/refute each.

3) **Facts vs inferences:**
- Clearly label **Observed facts** (from user/logs/metrics) vs **Inferences** (your reasoning).
- If you must assume something, label it as an **Assumption** and say what would verify it.

4) **User drives sequencing.** The phases below are a reference, not a mandatory order. If the user is already past a phase (e.g., they have a reproducer), skip ahead.

## Typical phases (reference, not a rigid workflow)

- **Understand**: expected vs actual behavior, scope/impact, when it started.
- **Reproduce / localize**: reliable steps, smallest reproducer, affected environment(s).
- **Isolate**: narrow to component/code path/config/dependency; correlate with changes.
- **Diagnose**: form hypotheses, run discriminating checks, identify the causal mechanism.
- **Fix & prevent** (only when grounded): propose change(s), assess risk/side effects, add tests/guards.

## What I need from you

Share whatever you have. I’ll ask for the minimum additional detail needed to move forward.

Helpful inputs:
- Exact error message / stack trace (verbatim)
- Expected vs actual behavior
- Repro steps (even partial)
- Environment details (OS/runtime versions, flags, config)
- What changed recently (deploy, config, dependency, data, traffic)
- Logs/metrics/screenshots

## Output (choose the right container)

### A) Debug Snapshot (when evidence is incomplete)

Use this when reproduction is unclear, signals are sparse, or multiple hypotheses are still live.

```markdown
## Debug Snapshot: [Issue Summary]

### Observed Facts
- ...

### Working Hypotheses
- **H1:** ...
  - Why it fits the facts: ...
  - What would disprove it: ...
  - Next check(s): ...
- **H2:** ...
  - Why it fits the facts: ...
  - What would disprove it: ...
  - Next check(s): ...

### Fast Triage / Mitigations (optional)
- [Only include actions that are safe and clearly reversible.]

### What I Need Next
- [Targeted questions or specific logs/commands to run]
```

### B) Debug Report (when root cause is grounded)

Only use this when we have enough evidence to state a likely root cause mechanism (e.g., reliable reproducer, confirming log evidence, clear bisection/correlation with a specific change).

```markdown
## Debug Report: [Issue Summary]

### Reproduction (ground truth)
- **Expected:** ...
- **Actual:** ...
- **Steps / conditions to reproduce:** ...
- **Affected env(s):** ...

### Evidence
- Key signals (logs/metrics/traces) and what they show:
  - ...

### Root Cause (mechanism)
- ...
- **Why this explains the symptoms:** ...
- **What would change my mind:** ...

### Fix Plan
- Proposed change(s): ...
- Risk / side effects to watch: ...
- Rollout or validation plan: ...

### Prevention
- Test(s) to add: ...
- Guardrail(s) / monitoring to add: ...
```

## If connectors available

If **~~monitoring** is connected:
- Pull logs, error rates, and key metrics around the suspected time window.
- Correlate with deploys/config changes.
- Treat correlations as hypotheses until confirmed.

If **~~source control** is connected:
- Identify recent commits/PRs touching the suspected code path.
- Prefer discriminating checks (bisection, diff-based hypotheses) over narrative certainty.

If **~~project tracker** is connected:
- Search for related incidents/bugs.
- Create a ticket **after** the failure mode and next actions are clear (or explicitly mark it as “investigation ongoing”).

## Quality bar

- Prefer “here’s what we know / here’s what we don’t” over filling template slots.
- Keep multiple hypotheses alive until evidence collapses the space.
- Make next steps executable (commands to run, logs to fetch, specific diffs to inspect).
- Avoid confident fixes when the diagnosis is not grounded.
