---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A6
tier: optimised
run: 0
---
---
name: incident-response
description: Run an incident response workflow by phase: triage, status update, or postmortem.
argument-hint: "<incident description or alert>"
---

# /incident-response

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Manage an incident from detection through postmortem with clear phase boundaries.

## Usage

```
/incident-response $ARGUMENTS
```

## Modes

```
/incident-response new [description]     # Start triage for a new incident
/incident-response update [status]       # Post a status update mid-incident
/incident-response postmortem            # Generate a postmortem after resolution
```

If no mode is specified, ask which phase the incident is in.

## Mode boundaries (do not mix)

- **new/update:** No postmortem sections, root cause conclusions, or lessons learned.
- **postmortem:** No live status update template; focus on synthesis after resolution.
- **All modes:** Stay factual. Separate knowns vs unknowns. Ask for missing critical info.

## Severity classification (use after impact is described)

| Level | Criteria | Response Time |
|-------|----------|---------------|
| SEV1 | Service down, all users affected | Immediate, all-hands |
| SEV2 | Major feature degraded, many users affected | Within 15 min |
| SEV3 | Minor feature issue, some users affected | Within 1 hour |
| SEV4 | Cosmetic or low-impact issue | Next business day |

## Mode: new (triage)

Goal: surface impact and affected systems first, then assign severity and immediate actions.

### Triage output

```markdown
## Triage Summary: [Title]
**Current status:** Investigating | Identified | Mitigating | Monitoring
**Impact (who/what):** [Plain description]
**Affected systems/users:** [List]
**Signals observed:** [Alerts, symptoms, errors]
**Known timeline:**
- [Time] [Event]

**Severity:** SEV[1-4] — [Rationale based on impact]

**Roles (if known):**
- Incident Commander:
- Comms:
- Responders:

**Immediate actions:**
- [Action]

**Open questions / info needed:**
- [Question]
```

If critical information is missing, ask focused follow-ups after the summary.

## Mode: update (status)

Provide a factual update using current incident data. Do not speculate or conclude root cause.

### Status update output

```markdown
## Incident Update: [Title]
**Severity:** SEV[1-4] | **Status:** Investigating | Identified | Monitoring | Resolved
**Impact:** [Who/what is affected]
**Last Updated:** [Timestamp]

### Current Status
[Brief, plain-language summary of what is known now]

### Actions Taken
- [Action]

### Next Steps
- [What happens next / ETA if known]

### Timeline (if timestamps are known)
| Time | Event |
|------|-------|
| [HH:MM] | [Event] |

### Next Update
[When the next update is expected]
```

## Mode: postmortem

Only generate after resolution and with incident data (impact, timeline, actions). If missing, request it.

### Postmortem output

```markdown
## Postmortem: [Incident Title]
**Date:** [Date] | **Duration:** [Time] | **Severity:** SEV[1-4]
**Authors:** [Names] | **Status:** Draft | Final

### Summary
[Plain-language summary, length as needed]

### Impact
- [Users affected]
- [Duration of impact]
- [Business impact if known]

### Timeline
| Time (UTC) | Event |
|------------|-------|
| [HH:MM] | [Event] |

### Root Cause & Contributing Factors
[Explain causal chain supported by evidence; note uncertainty]

### Detection & Response
[How the incident was detected and how response unfolded]

### What Went Well
- [Item]

### What Went Poorly
- [Item]

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| [Action] | [Person] | P0/P1/P2 | [Date] |

### Lessons Learned (optional)
[Key takeaways]
```

## If Connectors Available

- **~~monitoring**: Pull alert details and metrics relevant to the current phase.
- **~~incident management**: Create or update the incident record and page responders.
- **~~chat**: Post status updates or create a war room channel as requested.
