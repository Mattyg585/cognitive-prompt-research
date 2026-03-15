---
model: GPT-5.3-Codex (gpt-5.3-codex)
date: 2026-03-15
experiment: A6
tier: optimised
artifact: SKILL
---

---
name: incident-response
description: Run an incident response workflow — triage, status communication, and postmortem generation with mode-specific cognitive boundaries.
argument-hint: "<incident description or alert>"
---

# /incident-response

Manage incident work across three modes:

```text
/incident-response new [description]
/incident-response update [status]
/incident-response postmortem
```

If no mode is specified, ask which mode the user wants.

## Mode boundary rule

When running one mode, use only that mode’s guidance and template below. Do not borrow framing from other modes.

---

## Mode: New Incident (Triage)

Goal: establish severity, scope, and response ownership quickly.

### Severity guidance

| Level | General shape | Response posture |
|---|---|---|
| SEV1 | Active service failure or confidentiality/integrity risk with broad impact | Immediate, all-hands |
| SEV2 | Major degradation with significant user impact | Escalate promptly |
| SEV3 | Partial degradation with limited impact | Respond in normal on-call window |
| SEV4 | Cosmetic/low-impact issue | Handle in routine workflow |

If it sits between levels, state why instead of force-fitting.

### Triage checklist

- Affected systems and user scope
- Current known impact
- Known unknowns
- Incident roles (IC, responders, comms owner)

### Output — Triage Summary

```markdown
## Incident Triage: [Title]
**Provisional Severity:** SEV[X]
**Current Status:** Investigating
**Impact (known):** [...]
**Unknowns:** [...]
**Roles:** IC [...], Responders [...], Comms [...]
**Immediate Next Steps:** [...]
```

---

## Mode: Status Update

Goal: concise factual update for stakeholders.

Guidance:

- Separate facts from assumptions.
- Include next update time.
- Keep language operational and specific.

### Output — Status Update

```markdown
## Incident Update: [Title]
**Severity:** SEV[X] | **Status:** Investigating | Identified | Monitoring | Resolved
**Impact:** [...]
**Last Updated:** [Timestamp UTC]
**Next Update ETA:** [Timestamp UTC]

### Current Facts
- [...]

### Actions Since Last Update
- [...]

### Next Steps
- [...]
```

---

## Mode: Postmortem

Goal: reflective, blameless, system-level learning document.

### Blameless framing

Blameless does **not** mean ignoring human decisions. It means examining decisions in context:

- What information was available at the time?
- What assumptions were reasonable then?
- What constraints/pressures shaped choices?

### Causal analysis rule

Trace causes to natural depth. Branch where causes branch. Stop when evidence stops.

Do not force a fixed-number causal chain.

### Coverage guidance

A strong postmortem usually covers:

1. Summary and impact
2. Timeline (including what was known at key points)
3. Root cause and contributing factors
4. Response evaluation (what worked / didn’t, with evidence)
5. Action items tied explicitly to findings
6. Lessons learned that generalize beyond this incident

Depth should follow incident complexity, not template symmetry.

### Output — Postmortem

```markdown
## Postmortem: [Incident Title]
**Date:** [Date] | **Duration:** [Incident duration]
**Severity:** SEV[X] | **Status:** Draft
**Authors:** [Names/teams]

### Summary
[2–4 sentence plain-language summary]

### Impact
- [Who/what was affected]
- [Duration and scale]
- [Business/legal/operational impact]

### Timeline
| Time (UTC) | Event | What Was Known |
|---|---|---|
| ... | ... | ... |

### Root Cause Analysis
[Causal structure and evidence. Include branches and contributing factors where relevant.]

### Response Evaluation
[What worked well, what fell short, and why — grounded in timeline evidence.]

### Action Items
| Action | Owner | Rationale |
|---|---|---|
| ... | ... | [Which finding this addresses] |

### Lessons Learned
[Reusable organizational insights; not just action-item restatement.]
```

## General quality bar

- Prefer evidence-linked claims over generic statements.
- Name unresolved uncertainty explicitly.
- Avoid numeric anchors unless user asked for them.
