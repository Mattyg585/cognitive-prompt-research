# Revision Notes: A6 SecOps Incident Response — Tier 2 Optimisation

## Finding → Change Map

### 1. "5 Whys" Is a Double Anchor (High)

**Finding**: The 5 Whys template is both a numeric anchor (exactly 5 levels) and a structural anchor (linear causal chain). Real causes may be shallower, deeper, or tree-shaped. Forces template-filling over genuine causal analysis.

**Change**: Removed the entire 5 Whys section and its numbered template. Replaced with open-ended "Root Cause Analysis" guidance that explicitly instructs: follow the evidence rather than fitting to a fixed number of levels. If causes branch, document all branches. If you reach root cause after two levels, stop. If causes run seven levels deep, follow them.

Added a shaping question ("is this a proximate cause, or is there something deeper?") as a lens for depth — guides how to look rather than prescribing how many levels to find. The output template now has a free-form root cause section with a comment reinforcing the principle: "branch where the causes branch, go deep where the evidence goes deep, stop where the evidence stops."

### 2. Postmortem Template Is a Four-Mode Collision (High)

**Finding**: Timeline, root cause, 5 Whys, what went well/poorly, action items, and lessons learned all in one rigid template forces six types of thinking simultaneously. Evaluation contaminates investigation; fix-generation shapes root cause analysis.

**Change**: Restructured the postmortem section with two interventions:

First, added a scope boundary at the top of the postmortem mode: "You are doing reflective analysis, not operational reporting. Step back from the urgency of the incident and examine it as a system." This sets the epistemic stance before any template is encountered.

Second, lightened the template. The "What to Cover" section presents the areas as guidance ("a postmortem typically needs to address these areas") rather than a fixed template with fixed ordering. Added the explicit instruction: "their relative depth should respond to what matters for this specific incident." The output template keeps named sections (they're still useful as a document structure) but each section is more open — no fixed number of bullet slots, no implication that each section should be equal length.

Merged "What Went Well" and "What Went Poorly" into a single "Response Evaluation" section. This is a lighter structural commitment — the model can discuss what worked and what didn't without being forced into a binary sorting exercise.

### 3. Cross-Phase Template Contamination (Moderate)

**Finding**: All templates loaded regardless of which mode is invoked. Status Update's operational framing contaminates postmortem's reflective framing.

**Change**: Split the prompt into three clearly separated mode sections with horizontal rules between them. Added an explicit instruction at the top of the Modes section: "Each mode uses its own guidance below. When running in one mode, work from that mode's section — the other modes' templates and framing are not relevant to your current task."

The modes are now: "Mode: New Incident (Triage)", "Mode: Status Update", and "Mode: Postmortem" — each self-contained with its own guidance and output template. The Status Update template no longer sits adjacent to the Postmortem template in the same undifferentiated space.

### 4. "Blameless" Directive Pre-Filters Investigation (Moderate)

**Finding**: "Focus on systems and processes, not individuals" is interpreted as "don't examine human factors" rather than "examine human factors through a systems lens." Drops an entire category of contributing causes.

**Change**: Replaced the one-line tip with a full subsection in the postmortem mode: "Blameless Means Systems Thinking, Not Avoidance." The new text explicitly instructs: examine why decisions seemed correct at the time, what information was missing, what pressures existed, what alternatives were visible.

Added the framing: "Understanding why people made the choices they did — given what they knew and the constraints they faced — is different from assigning blame. A postmortem that avoids human factors entirely misses an entire category of contributing causes."

This reframe preserves the blameless cultural principle while opening investigation to human decision-making.

### 5. Severity Classification as Evaluation Seed (Low-Moderate)

**Finding**: SEV1-4 with specific criteria and fixed response times acts as a classification seed that can anchor investigation depth to severity level.

**Change**: Softened the severity table. Changed column headers from "Criteria | Response Time" (precise, seed-like) to "General Shape | Response Posture" (descriptive, lens-like). Removed fixed response time targets ("Within 15 min", "Within 1 hour") and replaced with posture descriptions ("Escalate promptly", "Respond within a reasonable window").

Added explicit permission to not force-fit: "If the incident doesn't fit neatly, say so — 'this sits between SEV2 and SEV3 because...' is better than a forced classification."

## Additional Changes

### Action Items table
Removed "Priority" (P0/P1/P2) and "Due Date" columns from the action items table. These are numeric/evaluative anchors that push toward convergent classification during what should be a generative exercise (designing interventions). Replaced with a "Rationale" column that links each action item to the specific root cause or response gap it addresses — this is more useful than a priority label and keeps the thinking grounded in the analysis rather than in a severity classification system.

### Timeline table
Added a "What Was Known" column to the postmortem timeline template. This supports the blameless reframe — it makes visible what information was available at each decision point, which is essential for understanding decisions through a systems lens rather than with hindsight bias.

### Triage mode restructured
Separated triage into its own mode section (previously embedded in the overview diagram). The overview diagram mixed operational phases with cognitive work in a way that implied all four phases were always active. The separated mode section makes triage self-contained.

### Overview diagram removed
The "How It Works" diagram listing all four phases with checkmarks was removed. It served as a visual table of contents but also loaded all four phases' framing into every invocation. The mode-separated structure makes it unnecessary.

### Tips section
Changed Tip 3 from "Postmortems are blameless — Focus on systems and processes, not individuals" to "Postmortems examine the system — Including the human decisions within it, through a systems lens." Aligns with the reframed blameless guidance.
