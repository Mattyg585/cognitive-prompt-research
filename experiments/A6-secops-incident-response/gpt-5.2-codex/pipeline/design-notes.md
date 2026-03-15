---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A6
tier: pipeline
run: 0
---

# Pipeline Design Notes — A6 SecOps Incident Response

## Pipeline overview
Separate triage, communication, and postmortem synthesis into distinct agents to avoid mode interference. A structured incident record is the boundary artifact between phases.

## Agent map
1. **incident-triage-recorder**
   - **Thinking types:** investigation + light structuring
   - **Input:** raw incident description or alert
   - **Output:** structured Incident Record (YAML) + triage summary + follow-up questions
   - **Why separate:** keeps evaluation (severity) after investigation and avoids comms/postmortem contamination

2. **incident-status-communicator**
   - **Thinking types:** generation + reframing
   - **Input:** Incident Record
   - **Output:** status update in markdown for internal or customer audiences
   - **Why separate:** prevents status language from biasing investigation or postmortem synthesis

3. **incident-postmortem-writer**
   - **Thinking types:** synthesis + evaluation
   - **Input:** resolved Incident Record (timeline, impact, actions)
   - **Output:** blameless postmortem document
   - **Why separate:** avoids premature narrative commitment during live response

## Execution order
1. **Triage** → produce Incident Record and triage summary.
2. **Status updates** → run as needed using the latest Incident Record (loop as incident evolves).
3. **Postmortem** → only after resolution and record completion.

## Handoff strategy
- **Structured Incident Record** is the canonical artifact.
- It strips exploratory reasoning while preserving facts, impacts, timeline, and actions.
- Updates to the record happen between stages rather than passing raw prose.

## Execution method
**Sequential with optional loops** (status updates repeat). Each stage depends on the prior stage’s structured output, and a clean handoff is needed to prevent mode bleed.

## Context window notes
- Keep Incident Record concise (facts + timeline entries).
- If timelines or action lists grow large, compress or archive older entries and keep a short “current summary” in the record.
- Postmortem should reference only confirmed facts; use explicit “unknown” tags for gaps.
