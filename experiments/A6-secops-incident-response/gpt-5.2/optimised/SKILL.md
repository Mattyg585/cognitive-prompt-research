---
model: GPT-5.2 (gpt-5.2)
date: 2026-03-15
experiment: A6
tier: optimised
artifact: SKILL
---

---
name: incident-response
description: Run an incident response workflow — triage, status communication, and postmortem writing with explicit cognitive boundaries (investigation vs evaluation).
argument-hint: "<incident description or alert>"
---

# /incident-response

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Manage an incident from detection through postmortem.

## Usage

```text
/incident-response $ARGUMENTS
```

## Modes

```text
/incident-response new [description]     # Start / triage a new incident
/incident-response update [status]       # Post a status update
/incident-response postmortem            # Write a postmortem from incident data
```

If no mode is specified, ask which mode the user wants.

## Mode boundary rule (anti-contamination)

When running **one** mode, use only that mode’s guidance and template below.

- Do **not** borrow framing, tone, or sections from other modes.
- Do **not** “complete the whole lifecycle” unless the user explicitly asks.

---

## Mode: New Incident (Triage)

### Goal
Mobilise the right response quickly by establishing: **what’s happening, who/what is impacted, what’s unknown, and who owns what**.

### Investigation-first rule (separate investigation vs evaluation)
In triage, your primary posture is **investigation + structuring**.

- Collect and organise facts and unknowns first.
- Only then assign a **provisional** severity, with rationale and uncertainty.

### Safety / SecOps note
If there’s any indication of a **security incident** (data exposure, suspicious access, integrity compromise), prioritise:
- containment actions that preserve evidence (avoid destructive changes without noting what was done), and
- escalation to the right responders/stakeholders.

### Severity guidance (use as a lens, not a box-filling target)

| Level | General shape | Response posture |
|---|---|---|
| SEV1 | Active service failure or confidentiality/integrity risk with broad impact | Immediate, all-hands |
| SEV2 | Major degradation or credible security concern with significant impact | Escalate promptly |
| SEV3 | Partial degradation or limited-scope concern | Respond in normal on-call window |
| SEV4 | Low-impact issue | Handle in routine workflow |

If it sits between levels, say so (“between SEV2 and SEV3 because…”) rather than force-fitting.

### What to ask for (if missing)
Request only what’s needed to move the investigation forward, e.g.:
- What triggered the alert / report? (error, metric, detection signal)
- Impact: who/what is affected, how severe, when it started
- Current scope: which systems, regions, identities/accounts, data sets
- What changed recently? (deploys, config, access changes)
- What’s been tried already? What happened?

### Output — Triage Summary

```markdown
## Incident Triage: [Title]

**Current Status:** Investigating

### Known Facts
- ...

### Unknowns (Explicit)
- ...

### Immediate Risks / Priorities
- ...

### Provisional Severity
- **Level:** SEV[1–4] (or “between SEVx and SEVy”)
- **Rationale:** ...
- **Confidence:** Low | Medium | High

### Ownership / Roles
- **Incident Commander (IC):** [Name/TBD]
- **Responders:** [Name(s)/TBD]
- **Comms owner:** [Name/TBD]

### Immediate Next Steps (Investigation / Containment)
- ...

### Comms Cadence
- Next update: [time or “TBD”]
```

Do not invent names, timestamps, or actions that weren’t provided. Use **TBD/Unknown** when necessary.

---

## Mode: Status Update

### Goal
Provide a concise, factual stakeholder update.

### Rules
- Separate **confirmed facts** from **working theories**.
- Don’t invent ETAs, root causes, impact, or timestamps. If unknown, say unknown.
- Keep language present-tense and operational.

### Output — Status Update

```markdown
## Incident Update: [Title]
**Severity:** SEV[X] | **Status:** Investigating | Identified | Monitoring | Resolved
**Impact (known):** ...
**Last Updated:** [Timestamp UTC or “TBD”]
**Next Update:** [Timestamp UTC / cadence or “TBD”]

### Current Facts
- ...

### Working Theories (Unconfirmed)
- ...

### Actions Taken
- ...

### Next Steps
- ...
```

---

## Mode: Postmortem

### Goal
Write a reflective, blameless learning document (past-tense), not an expanded status update.

### Internal sequencing rule (separate investigation vs evaluation)
Do **not** mix everything at once. In your own process, sequence the work:

1) **Timeline + facts** (investigation/structuring)
2) **Causal analysis** (investigation; allow depth + branching)
3) **Response evaluation** (evaluation; judge the response, grounded in evidence)
4) **Action items** (generation/planning; tied to causes and response gaps)
5) **Lessons learned** (synthesis; what generalises)

### Blameless means systems thinking (including humans)
Blameless does **not** mean ignoring human decisions. Analyse the decision environment:
- What was known at the time?
- What signals were missing/ambiguous?
- What constraints or pressures shaped choices?
- Why did the decision make sense then?

### Causal analysis: de-anchor (no 5 Whys)
- Follow causes to the **natural depth** supported by evidence.
- **Branch** where causes branch (contributing factors can be parallel).
- Stop when evidence stops; mark unknowns explicitly.
- Avoid forcing a single linear chain or a fixed number of levels.

### Provenance + uncertainty (anti-confabulation)
- If a detail (time, owner, impact, data exposure) isn’t provided or pulled from tools, write **Unknown/TBD**.
- Prefer phrases like “Based on [incident log / user notes / monitoring data], …” when possible.

### Output — Postmortem

```markdown
## Postmortem: [Incident Title]
**Date:** [Date or “TBD”] | **Duration:** [Duration or “TBD”]
**Severity:** SEV[X] | **Status:** Draft
**Authors:** [Names/teams or “TBD”]

### Summary
[Plain-language summary of what happened and why it matters]

### Impact
- **Who/what was affected:** ...
- **Duration/scale:** ...
- **Business/security impact (if known):** ...

### Timeline (Facts)
Use a table if you have timestamps; otherwise use bullets.

| Time (UTC) | Event | What Was Known |
|---|---|---|
| ... | ... | ... |

### Causal Analysis (Root cause + contributing factors)
Describe the causal structure and evidence.
- **Trigger(s):** ...
- **Contributing factors:** ...
- **Latent/systemic conditions:** ...
- **Where evidence runs out:** ...

### Response Evaluation (Evidence-linked)
- **What worked:** ... (link to specific timeline moments)
- **What didn’t:** ... (link to specific timeline moments)
- **Detection/observability notes:** ...

### Action Items (Tied to findings)
Only assign owners/dates if provided. Otherwise use TBD.

| Action | Owner | Due | Rationale |
|---|---|---|---|
| ... | ... | ... | Which cause/gap this addresses |

### Lessons Learned
[What generalises beyond this incident; not just a restatement of action items]
```

---

## If Connectors Available

If **~~monitoring** is connected:
- Pull alert details and relevant metrics
- Summarise key signals (what changed, when, and why it matters)

If **~~incident management** is connected:
- Create/update the incident record
- Page on-call responders and record ownership

If **~~chat** is connected:
- Post status updates to the incident channel
- Create a war room channel and invite roles

## General quality bar

- Make uncertainty admissible: **Unknown/TBD** is better than invented specificity.
- Keep investigation and evaluation cognitively separated (timeline/causes first, judgments second).
- Avoid anchors that force uniform outputs (e.g., fixed-number causal chains).
