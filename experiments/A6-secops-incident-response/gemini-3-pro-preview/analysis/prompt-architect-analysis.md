# Prompt Architect Analysis: SecOps Incident Response

**Analyzer**: Prompt Architect (Gemini 3 Pro Preview)
**Target**: `experiments/A6-secops-incident-response/original/SKILL.md`

## 1. Thinking Types & Relations
The prompt asks the model to wear multiple hats across the lifecycle of an incident:
*   **Triage (Investigation/Evaluation)**: "Assess severity (SEV1-4)", "Identify affected systems". Requires analyzing incoming signals against strict criteria.
*   **Communication (Synthesis/Reframing)**: "Draft internal status update". Requires translating technical facts into business-appropriate updates.
*   **Mitigation (Procedural/Action)**: "Document mitigation steps", "Track timeline". Operational logging.
*   **Postmortem (Deep Analysis/Reflection)**: "Root cause analysis", "5 Whys", "Lessons Learned". Requires moving from "what happened" to "why it happened" without blame.

## 2. Mode Interference
This prompt compresses distinct cognitive modes into a single context, creating significant interference risks:

### A. The "Fog of War" vs. "Deep Reflection" Conflict
*   **Mechanism**: Context carries cognitive mode. The session starts with high-urgency, action-oriented commands ("SEV1", "Mitigate", "Status Update").
*   **The Conflict**: When the user switches to `/incident-response postmortem`, the context is full of urgent, tactical, short-term thinking. This "action bias" persists into the Postmortem phase, which requires slow, deep, systemic thinking.
*   **Quote**: The prompt defines `Phase 1: TRIAGE` through `Phase 4: POSTMORTEM` in the same linear flow.
*   **Predicted Degradation**: The Postmortem will likely be a shallow summary of the timeline rather than a true Root Cause Analysis. The "5 Whys" will simply restate the mitigation steps (e.g., "Why? Because we restarted it.") rather than finding process gaps.

### B. The "Blameless" vs. "Ownership" Tension
*   **Mechanism**: Conflicting constraints.
*   **Quote**: "Postmortems are blameless — Focus on systems and processes, not individuals" vs. "Action items with owners".
*   **The Conflict**: The model is asked to be blameless but immediately assign names to actions. In a single context, this often leads to "safe" action items (e.g., "Update documentation") rather than difficult ones that might imply fault (e.g., "Revoke admin access for X").

### C. Numeric Anchoring in RCA
*   **Mechanism**: Numbers become targets.
*   **Quote**:
    ```markdown
    ### 5 Whys
    1. Why did [symptom]? → [Because...]
    ...
    5. Why did [cause 4]? → [Root cause]
    ```
*   **The Conflict**: The template explicitly numbers 1 through 5. The model will gravitate to exactly 5 steps every time, regardless of problem complexity. Simple issues will be padded; complex issues will be truncated.

## 3. Diagnostic Signals (What to look for in output)
*   **The "Timeline Rehash" Postmortem**: Does the RCA section just repeat the events in the Timeline section? (e.g., "Root cause: The server ran out of memory" - this is a proximal cause, not a root cause).
*   **The "Exactly 5" Whys**: Does every postmortem have exactly 5 levels of depth?
*   **Tone Drift**: Does the status update sound like a debug log? (Investigation mode bleeding into Communication mode).
*   **Shallow Action Items**: Are the action items purely technical ("Fix the bug") rather than process-oriented ("Add load testing to CI")?

## 4. Recommendations

### Prompt-Level Fixes (Low Effort)
*   **Remove Numeric Anchors**: Change the "5 Whys" template to "Root Cause Analysis (drill down until you find the systemic cause)". Remove the 1-5 numbering.
*   **Explicit Scope Boundaries**: In the `postmortem` mode instructions, add: "You are now in analysis mode. Shift away from urgent action. Look for systemic causes, not just immediate triggers."
*   **Refine Blameless Instruction**: "Focus on *process* owners, not *incident* actors."

### Pipeline-Level Interventions (High Value)
*   **Split into Two Agents**:
    1.  **Incident Commander Agent**: Handles Triage, Communication, Mitigation. Optimized for speed, clarity, and following procedure.
    2.  **Postmortem Analyst Agent**: Instantiated *after* the incident is resolved. It receives the *logs* from the Commander but runs in a fresh, calm context. It is optimized for critical thinking, skepticism, and systemic analysis.
*   **Rationale**: Separating the "Urgent" context from the "Reflective" context is the only way to get a high-quality RCA. You cannot do deep reflection while the "siren" of the incident context is still ringing in the model's attention.

## 5. Composition Signature
*   **Base**: Operational/Procedural (Incidents)
*   **Skill (Triage)**: Analytical/Evaluative (Severity)
*   **Skill (Comms)**: Synthesis/Reframing (Updates)
*   **Skill (Postmortem)**: Deep Divergent (RCA) - **CONFLICT** with Base urgency.

**Ready for Prompt Writer.**
