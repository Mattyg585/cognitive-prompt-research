---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A5
tier: optimised
run: 0
---
---
name: debug
description: Structured debugging session — investigate, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.
argument-hint: "<error message or problem description>"
---

# /debug

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Run a structured debugging session to find and fix issues systematically.

## Working stance (scope boundary)
- **Investigate first.** Do not propose a root cause, fix, or prevention until evidence supports it.
- **If evidence is incomplete**, stop after Investigation and ask for missing info or list hypotheses with confidence and evidence gaps.
- **The human drives the order.** The phases below are a reference, not a required sequence. If the user says a phase is already done, skip or reorder.

## Typical phases (non-linear reference)
- **Reproduce** — expected vs. actual behavior, steps, conditions
- **Isolate** — component, environment, recent changes, logs
- **Diagnose** — evidence-backed root cause (or bounded hypotheses)
- **Fix** — change + verification + prevention

## What I Need From You

Tell me about the problem. Any of these help:
- Error message or stack trace (verbatim)
- Steps to reproduce
- What changed recently
- Logs or screenshots
- Expected vs. actual behavior

## Output (responsive template)

```markdown
## Debug Report: [Issue Summary]

### Investigation
- **Expected**: [What should happen]
- **Actual**: [What happens instead]
- **Reproduction**: [Steps/conditions, if known]
- **Scope/Impact**: [Who/what is affected, environments]
- **Evidence**: [Logs, errors, metrics, traces — cite sources]

### Observations & Anomalies
- [Notable patterns, inconsistencies, or surprising behavior]

### Hypotheses (if evidence is incomplete)
- **[Hypothesis]** — Confidence: [low/med/high]
  - **Supporting evidence**:
  - **Missing evidence**:

### Root Cause (only if confident)
[Root cause with evidence]

### Fix (only when root cause is supported)
[Change required + rationale + verification steps]

### Prevention (optional)
- [Test/guard/monitoring to prevent recurrence]

### Open Questions / Next Steps (if needed)
- [Targeted questions or data needed to proceed]
```

## If Connectors Available

If **~~monitoring** is connected:
- Pull logs, error rates, and metrics around the time of the issue
- Identify spikes, regressions, or recent deploy correlations

If **~~source control** is connected:
- Identify recent commits and PRs that touched affected code paths
- List changes as facts; avoid diagnosis until evidence supports it

If **~~project tracker** is connected:
- Search for related bug reports or known issues
- Create a ticket for the fix once the root cause is supported

## Tips

1. **Share error messages exactly** — Don't paraphrase. The exact text matters.
2. **Mention what changed** — Recent deploys, dependency updates, and config changes are top suspects.
3. **Include context** — "This works in staging but not prod" or "Only affects large payloads" narrows things fast.
