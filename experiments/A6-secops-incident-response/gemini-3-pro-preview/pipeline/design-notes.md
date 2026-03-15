# Pipeline Design: Incident Response

## Overview
This pipeline separates the incident response lifecycle into three distinct cognitive modes:
1. **Command & Control**: Managing the incident, making decisions, tracking state.
2. **Communication**: translating technical facts into stakeholder updates.
3. **Analysis**: Retrospective root cause analysis and learning.

## Rationale
The original single-prompt approach suffered from cognitive interference:
- **Command vs. Analysis**: The pressure to resolve the incident (forward-looking) conflicted with the need to understand root cause (backward-looking).
- **Technical vs. Public**: The need for precise technical details for responders conflicted with the need for reassured, simplified communication for stakeholders.
- **Real-time vs. Post-hoc**: The "fog of war" during an incident biases the postmortem if done in the same context.

## Agents

### 1. IncidentCommander
- **Role**: Orchestration & Evaluation.
- **Focus**: Triage, assignment, state tracking, decision making.
- **Input**: Alerts, user reports, system status.
- **Output**: Incident state, directives, raw facts for comms.
- **Why Separate**: Needs to remain objective and decisive. Cannot get bogged down in drafting emails or deep-dive debugging.

### 2. CommsOfficer
- **Role**: Generation & Reframing.
- **Focus**: Internal/External communication.
- **Input**: Structured facts from IncidentCommander.
- **Output**: Drafted emails, status page updates, chat messages.
- **Why Separate**: Requires empathy and polish. Needs to "translate" technical facts into appropriate tones for different audiences without distorting the facts.

### 3. PostmortemAnalyst
- **Role**: Analysis & Synthesis.
- **Focus**: Root cause analysis, learning, process improvement.
- **Input**: Full incident timeline and resolution notes.
- **Output**: Blameless postmortem, 5 Whys, action items.
- **Why Separate**: Needs a "cool" cognitive state, removed from the urgency of the incident. Needs to see the whole picture (start to finish) to analyze effectively.

## Execution Flow
1. **Trigger**: User reports an issue or alert fires.
2. **Phase 1 (Triage/Mitigate)**: `IncidentCommander` runs the show. It may call `CommsOfficer` multiple times to draft updates.
3. **Phase 2 (Resolution)**: `IncidentCommander` confirms resolution and compiles the timeline.
4. **Phase 3 (Analysis)**: `IncidentCommander` hands off the full timeline to `PostmortemAnalyst` for the final report.
