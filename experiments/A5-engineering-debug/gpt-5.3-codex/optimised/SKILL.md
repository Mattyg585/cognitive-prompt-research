---
name: debug
description: Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.
argument-hint: "<error message or problem description>"
---

# /debug

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Run a structured debugging session to find and fix issues systematically.

Your primary job is to understand **why** the failure is happening. The fix follows from understanding. Do not let the desire to produce a fix narrow your investigation prematurely. Follow evidence, including threads that may point to systemic causes.

## Usage

```
/debug $ARGUMENTS
```

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                       DEBUG                                     │
├─────────────────────────────────────────────────────────────────┤
│  Step 1: REPRODUCE                                              │
│  ✓ Understand expected vs. actual behavior                      │
│  ✓ Identify exact reproduction conditions                       │
│  ✓ Determine scope (when started, who is affected)             │
│                                                                 │
│  Step 2: ISOLATE                                                │
│  ✓ Narrow down component, service, or code path                │
│  ✓ Check recent changes (deploys, config, dependencies, jobs)  │
│  ✓ Review logs, traces, and system metrics                     │
│                                                                 │
│  Step 3: DIAGNOSE                                               │
│  ✓ Form multiple hypotheses                                    │
│  ✓ Test each against available evidence                         │
│  ✓ Distinguish proximate trigger vs systemic root cause         │
│                                                                 │
│  Step 4: FIX                                                    │
│  ✓ Propose intervention with rationale                          │
│  ✓ Consider side effects and edge cases                         │
│  ✓ Suggest verification and prevention                          │
└─────────────────────────────────────────────────────────────────┘
```

## What I Need From You

Tell me about the problem. Any of these help:
- Error message or stack trace
- Steps to reproduce
- What changed recently
- Logs or screenshots
- Expected vs. actual behavior

## Output

```markdown
## Debug Report: [Issue Summary]

### Reproduction
- **Expected**: [What should happen]
- **Actual**: [What happens instead]
- **Steps/Conditions**: [How and when it reproduces]

### Diagnosis
Hypotheses considered, evidence for and against, and investigation threads followed.
Show the narrowing logic: what was considered, what was eliminated, and why.

### Root Cause
[Explanation of why the bug occurs]

### Fix
What should change, and at what level?
Possible levels include code, configuration, infrastructure, architecture, and process.
Match the intervention to the root cause. If the cause is systemic, avoid symptom-only patches.

### Prevention
- [Specific regression test(s)]
- [Specific guardrails/operational controls]
```

## If Connectors Available

If **~~monitoring** is connected:
- Pull logs, error rates, and metrics around the time of the issue
- Show recent deploys and config changes that may correlate

If **~~source control** is connected:
- Identify recent commits and PRs that touched affected code paths
- Check if the issue correlates with a specific change

If **~~project tracker** is connected:
- Search for related bug reports or known issues
- Create a ticket for the fix once identified

## Tips

1. **Share exact errors** — exact text usually matters.
2. **Mention what changed** — deploys/config/dependency/scheduled-job changes are common triggers.
3. **Include context** — intermittent vs deterministic behavior sharply changes diagnosis strategy.

