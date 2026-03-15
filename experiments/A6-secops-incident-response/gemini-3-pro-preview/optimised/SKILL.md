---
name: incident-response
description: Run an incident response workflow — triage, communicate, and write postmortem. Trigger with "we have an incident", "production is down", an alert that needs severity assessment, a status update mid-incident, or when writing a blameless postmortem after resolution.
argument-hint: "<incident description or alert>"
---

# /incident-response

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Manage an incident from detection through postmortem.

## Usage

```
/incident-response $ARGUMENTS
```

## Modes

You operate in two distinct cognitive modes. Do not mix them.

1.  **COMMANDER MODE** (Urgent, Tactical, Action-Oriented)
    *   `/incident-response new [description]`
    *   `/incident-response update [status]`
    *   Focus: Speed, clarity, mitigation, containment.

2.  **ANALYST MODE** (Reflective, Systemic, Slow)
    *   `/incident-response postmortem`
    *   Focus: Root cause, process gaps, prevention.
    *   **CRITICAL:** When entering this mode, stop acting urgently. The incident is over. Shift to deep analysis.

If no mode is specified, ask what phase the incident is in.

## Phase 1-3: Commander Mode (Triage, Communicate, Mitigate)

### Severity Classification

| Level | Criteria | Response Time |
|-------|----------|---------------|
| SEV1 | Service down, all users affected | Immediate, all-hands |
| SEV2 | Major feature degraded, many users affected | Within 15 min |
| SEV3 | Minor feature issue, some users affected | Within 1 hour |
| SEV4 | Cosmetic or low-impact issue | Next business day |

### Communication Guidance

Provide clear, factual updates at regular cadence. Include: what's happening, who's affected, what we're doing, when the next update is.

### Output — Status Update

```markdown
## Incident Update: [Title]
**Severity:** SEV[1-4] | **Status:** Investigating | Identified | Monitoring | Resolved
**Impact:** [Who/what is affected]
**Last Updated:** [Timestamp]

### Current Status
[What we know now]

### Actions Taken
- [Action 1]
- [Action 2]

### Next Steps
- [What's happening next and ETA]

### Timeline
| Time | Event |
|------|-------|
| [HH:MM] | [Event] |
```

---

## Phase 4: Analyst Mode (Postmortem)

**STOP.** You are no longer in incident response mode. You are now in analysis mode.
*   **Disregard urgency.** The fire is out.
*   **Focus on systems.** Look for process failures, not human errors.
*   **Be skeptical.** "The server ran out of memory" is a symptom, not a cause. Why did it run out? Why wasn't it caught?

### Output — Postmortem

```markdown
## Postmortem: [Incident Title]
**Date:** [Date] | **Duration:** [X hours] | **Severity:** SEV[X]
**Authors:** [Names] | **Status:** Draft

### Summary
[2-3 sentence plain-language summary]

### Impact
- [Users affected]
- [Duration of impact]
- [Business impact if quantifiable]

### Timeline
| Time (UTC) | Event |
|------------|-------|
| [HH:MM] | [Event] |

### Root Cause Analysis (Drill Down)
*   **Proximal Cause:** [Direct trigger, e.g., memory leak]
*   **Systemic Cause:** [Why the system allowed it, e.g., no memory limits in container config]
*   **Process Cause:** [Why the process failed, e.g., load testing didn't catch it]

### 5 Whys (Depth Check)
Drill down until you find the systemic cause. Do not stop at human error.
1. Why did [symptom]? → [Because...]
2. Why did [cause]? → [Because...]
... (Continue until root cause is found)

### What Went Well
- [Things that worked]

### What Went Poorly
- [Things that didn't work]

### Action Items
Assign to **process owners** (e.g., "Platform Team"), not incident actors.
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| [Systemic Fix] | [Team/Role] | P0/P1/P2 | [Date] |

### Lessons Learned
[Key takeaways for the team]
```

## If Connectors Available

If **~~monitoring** is connected:
- Pull alert details and metrics
- Show graphs of affected metrics

If **~~incident management** is connected:
- Create or update incident in PagerDuty/Opsgenie
- Page on-call responders

If **~~chat** is connected:
- Post status updates to incident channel
- Create war room channel

## Tips

1.  **Start writing immediately** — Don't wait for complete information. Update as you learn more.
2.  **Keep updates factual** — What we know, what we've done, what's next. No speculation.
3.  **Postmortems are blameless** — Focus on systems and processes, not individuals.
