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

```
/incident-response new [description]     # Start a new incident
/incident-response update [status]       # Post a status update
/incident-response postmortem            # Generate postmortem from incident data
```

If no mode is specified, ask what phase the incident is in.

Each mode uses its own guidance below. When running in one mode, work from that mode's section — the other modes' templates and framing are not relevant to your current task.

---

## Mode: New Incident (Triage)

When an incident is reported, triage it quickly. The goal is to understand scope and mobilise the right response.

### Severity Assessment

Assess severity based on the actual impact and urgency of the incident. Use these levels as guidance:

| Level | General Shape | Response Posture |
|-------|--------------|-----------------|
| SEV1 | Service down or data integrity at risk, broad user impact | Immediate, all-hands |
| SEV2 | Major feature degraded, significant user impact | Escalate promptly |
| SEV3 | Partial degradation, limited user impact | Respond within a reasonable window |
| SEV4 | Cosmetic or low-impact issue | Handle during normal workflow |

The severity should reflect what's actually happening, not be forced into a bucket. If the incident doesn't fit neatly, say so — "this sits between SEV2 and SEV3 because..." is better than a forced classification.

### Triage Checklist

- What systems are affected?
- Who is impacted — and how?
- What roles are needed? (Incident Commander, comms lead, responders)
- What's known so far, and what's still uncertain?

---

## Mode: Status Update

Provide clear, factual updates. Include: what's happening, who's affected, what we're doing, and when the next update is.

Keep updates grounded in what's known. Separate confirmed facts from working theories. Avoid speculation — if something is uncertain, say that rather than presenting it as fact.

### Output — Status Update

```markdown
## Incident Update: [Title]
**Severity:** [Level] | **Status:** Investigating | Identified | Monitoring | Resolved
**Impact:** [Who/what is affected]
**Last Updated:** [Timestamp]

### Current Status
[What we know now]

### Actions Taken
[What's been done so far]

### Next Steps
[What's happening next and when we'll update again]

### Timeline
| Time | Event |
|------|-------|
| [HH:MM] | [Event] |
```

---

## Mode: Postmortem

You are doing reflective analysis, not operational reporting. Step back from the urgency of the incident and examine it as a system — what made this incident possible, what made it invisible until it manifested, and what made the response effective or ineffective.

### Blameless Means Systems Thinking, Not Avoidance

Postmortems are blameless. This means examining human decisions through a systems lens, not avoiding them. Ask: why did the decision seem correct at the time? What information was missing? What pressures existed? What alternatives were visible to the person making the decision?

Understanding why people made the choices they did — given what they knew and the constraints they faced — is different from assigning blame. A postmortem that avoids human factors entirely misses an entire category of contributing causes.

### Root Cause Analysis

Trace the causal chain as deep as the evidence supports. Some incidents have shallow causes — a misconfigured flag, a typo. Others have deep, branching causal structures — multiple contributing factors, systemic vulnerabilities, feedback loops.

Follow the evidence rather than fitting to a fixed number of levels. If the causal chain branches (multiple contributing factors at the same level), document all branches. If you reach a genuine root cause after two levels, stop there. If the causes run seven levels deep, follow them.

The shape of the causal analysis should reflect the shape of the incident, not a predetermined template.

Ask at each level: is this a proximate cause, or is there something deeper that made this proximate cause possible? Stop when you reach causes that are either fundamental (architectural decisions, organisational constraints) or where the evidence runs out.

### What to Cover

A postmortem typically needs to address these areas, but their relative depth should respond to what matters for this specific incident. Some incidents need deep timeline analysis; others need deep causal analysis; others reveal the most through evaluating the response itself.

- **Summary** — What happened, in plain language. Enough for someone unfamiliar with the incident to understand the situation.
- **Impact** — Who was affected, for how long, and what was the business consequence.
- **Timeline** — Chronological reconstruction of events, decisions, and information flow. Note what was known at each decision point — hindsight makes decisions look obviously wrong when they were reasonable given what was known at the time.
- **Root Cause Analysis** — The causal chain, traced as deep as the evidence supports. See guidance above.
- **Response Evaluation** — What worked well in the response, and what didn't. Be specific — link evaluations to specific moments in the timeline.
- **Action Items** — Concrete next steps that address the root causes and response gaps identified above. Match the depth of the fix to the depth of the cause — systemic causes deserve systemic action items, not surface-level patches.
- **Lessons Learned** — What this incident reveals about the system, the process, or the organisation that wasn't visible before.

### Output — Postmortem

```markdown
## Postmortem: [Incident Title]
**Date:** [Date] | **Duration:** [Duration] | **Severity:** [Level]
**Authors:** [Names] | **Status:** Draft

### Summary
[Plain-language summary — what happened and why it matters]

### Impact
[Who was affected, duration, business impact where quantifiable]

### Timeline
| Time (UTC) | Event | What Was Known |
|------------|-------|---------------|
| [HH:MM] | [Event] | [Information available at this point] |

### Root Cause Analysis
[Trace the causal chain. Follow the evidence — branch where the causes branch, go deep where the evidence goes deep, stop where the evidence stops.]

### Response Evaluation
[What worked well, what didn't, linked to specific timeline events]

### Action Items
| Action | Owner | Rationale |
|--------|-------|-----------|
| [Action] | [Person] | [Which root cause or response gap this addresses] |

### Lessons Learned
[What this incident reveals that wasn't visible before]
```

---

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

1. **Start writing immediately** — Don't wait for complete information. Update as you learn more.
2. **Keep updates factual** — What we know, what we've done, what's next. No speculation.
3. **Postmortems examine the system** — Including the human decisions within it, through a systems lens.
