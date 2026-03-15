---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A6
tier: pipeline
run: 0
---

# Handoff Specification — Incident Response Pipeline

## Canonical artifact: Incident Record (YAML)
```yaml
incident_id: [if known]
title: [short title]
status: Investigating | Identified | Mitigating | Monitoring | Resolved
start_time: [timestamp if known]
reported_by: [source if known]
impact: [plain description]
affected_systems:
  - [system/service]
affected_users:
  - [user group]
severity: SEV1 | SEV2 | SEV3 | SEV4
severity_rationale: [why this level fits the impact]
signals:
  - [alert/symptom/error]
timeline:
  - time: [timestamp]
    event: [what happened]
actions_taken:
  - [action]
roles:
  incident_commander: [name or TBD]
  comms: [name or TBD]
  responders:
    - [name or TBD]
open_questions:
  - [missing critical info]
```

## Handoff: Triage → Status Update
- **What crosses:** Incident Record (facts, impact, timeline, severity, actions, roles).
- **Format:** Structured YAML/JSON only.
- **What gets dropped:** exploratory reasoning, hypotheses, narrative language.
- **Compression:** keep timeline entries brief; consolidate duplicate signals.

## Handoff: Status Update → Postmortem
- **What crosses:** Updated Incident Record with resolution status, final impact, timeline, and actions.
- **Format:** Structured YAML/JSON only.
- **What gets dropped:** communication phrasing, cadence details, speculative cause statements.
- **Compression:** ensure causal facts are concise; unresolved items go into `open_questions`.

## Record update responsibility
- The incident record is updated between stages (by humans or tooling).
- Agents consume the record as ground truth and do not invent missing data.
