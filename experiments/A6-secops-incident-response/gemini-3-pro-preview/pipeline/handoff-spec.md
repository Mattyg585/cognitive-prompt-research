# Handoff Specification

## 1. IncidentCommander -> CommsOfficer

**Trigger**: When a status update is needed (start, update, resolution).

**Data Transferred**:
- **Incident State**: Severity (SEV1-4), Current Phase (Investigating, Identified, Monitoring, Resolved).
- **Facts**: What is broken, who is affected, what is being done.
- **Next Steps**: ETA for next update, current action items.

**Format**: Structured Bullet Points (Strictly Factual).
> *   **Severity**: SEV1
> *   **Impact**: Checkout system down, 100% of users.
> *   **Current Action**: Rolling back deploy v123.
> *   **ETA**: 15 minutes.

**Dropped**:
- Internal speculation about root cause.
- Technical jargon not relevant to stakeholders.
- "Panic" or urgency markers not needed for the public.

---

## 2. IncidentCommander -> PostmortemAnalyst

**Trigger**: Incident is marked RESOLVED.

**Data Transferred**:
- **Full Timeline**: Chronological log of all events, alerts, and actions.
- **Resolution Details**: What fixed it, timestamps.
- **Initial Notes**: Any raw observations from the responders.

**Format**: Raw Log / Chronological Transcript.

**Dropped**:
- Drafts of communications (unless relevant to timeline).
- Intermediate "noise" or false alarms that were ruled out (though Analyst may review them if relevant to *why* it took so long).

**Cognitive Shift**:
- From "Fix it NOW" (Forward-looking, Convergent) to "Understand WHY" (Backward-looking, Divergent).
