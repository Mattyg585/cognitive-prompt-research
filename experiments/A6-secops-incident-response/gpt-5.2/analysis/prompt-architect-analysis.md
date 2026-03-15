---
model: GPT-5.2
date: 2026-03-15
experiment: A6
artifact: prompt-architect-analysis
---

# Prompt Architect Analysis — A6 SecOps Incident Response (Original SKILL)

Source prompt analysed: `experiments/A6-secops-incident-response/original/SKILL.md`

## 1) What the prompt is actually asking for (cognitive posture)

This skill is framed as an end-to-end incident lifecycle assistant (“Manage an incident from detection through postmortem.”, line 11) with a phase checklist spanning:

- **Triage** (lines 35–39): investigation + evaluation + light structuring
- **Communicate** (lines 40–44): reframing + generation
- **Mitigate** (lines 45–49): investigation + structuring + confirmation
- **Postmortem** (lines 50–55): reflective investigation + synthesis + evaluation + generation

It also defines explicit user modes (`new`, `update`, `postmortem`, lines 21–25) and adds a human-driven mode gate: “If no mode is specified, ask what phase the incident is in.” (line 27).

**Key posture tension:** the prompt *aspires* to temporal separation via modes, but it keeps **all phases, guidance, and both output templates in the same context** (lines 31–138). This increases the chance that, at runtime, the model will adopt a “complete the whole workflow” stance even when the user is only in one phase.

## 2) Where modes interfere (with evidence + mechanism)

### A) Investigation ↔ evaluation entanglement during triage (Moderate)

Prompt evidence:
- “✓ Assess severity (SEV1-4)” (line 36)
- Severity table with criteria + response time (lines 60–65)

Mechanism:
- Severity assignment is **convergent evaluation** being asked for at the same time as early **open investigation** (“Identify affected systems…”, line 37).
- Under uncertainty, the evaluation frame becomes a *pre-filter*: the model tends to investigate facts that justify a chosen SEV label, rather than exploring ambiguous or hard-to-classify signals.

What to watch for:
- Fast commitment to SEV with confident language despite thin evidence.
- “SEV2-depth” investigations (bounded scope) because the severity table implicitly cues how serious the work should be.

### B) Cross-phase residue: operational reporting contaminates reflective postmortem (Moderate)

Prompt evidence:
- Status update template is present (lines 71–93)
- Postmortem template is present (lines 95–138)
- Both remain in context regardless of which mode is invoked (no conditional scoping).

Mechanism:
- The status-update structure and language (“Current Status”, “Next Steps”, “ETA”, lines 79–88) establishes a **present-tense operational posture**.
- The postmortem requires a **past-tense reflective posture** (organizational learning). When both templates are in the same prompt, the model often writes the postmortem like an “expanded incident report” rather than a learning artifact.

Diagnostic signal:
- Postmortem sections read like status updates with hindsight (events + actions) rather than causal structure + decision environment.

### C) Postmortem template creates a multi-mode collision (High)

Prompt evidence: the postmortem output format requires, in one pass (lines 110–137):
- Timeline (structuring)
- Root cause (deep investigation)
- 5 Whys (constrained causal investigation)
- What went well / poorly (evaluation)
- Action items (generation/planning)
- Lessons learned (synthesis)

Mechanisms (why this is a “toxic mix”):

1) **Investigation + evaluation in one context**
   - Evaluation sections (“What Went Well/Poorly”, lines 125–130) introduce judging language adjacent to root cause analysis (lines 115–117).
   - This can bias causal analysis toward *judgeable* items (things someone/team did poorly) and away from systemic, non-blame-shaped factors (architecture, incentives, tooling affordances).

2) **Investigation + generation in one context (solution-shaped investigation)**
   - The “Action Items” table with owners/priority/due date (lines 131–135) creates completion pressure.
   - The model preferentially selects root causes that map cleanly to tickets, because it can immediately “cash out” the analysis into tasks.

3) **Synthesis while still investigating (premature convergence)**
   - “Lessons Learned” (lines 136–137) invites narrative compression before the causal picture is fully explored.
   - The model can lock into an early storyline and then back-fill the earlier sections to support it.

### D) 5 Whys is a double anchor: numeric + structural (High)

Prompt evidence:
- “✓ Root cause analysis (5 whys)” (line 53)
- Fixed five-step chain (lines 118–123)

Mechanism:
- **Numeric anchor**: forces exactly 5 causal levels whether the incident’s natural depth is 2 or 9.
- **Structural anchor**: forces a *single linear chain* when real incidents often have branching contributing factors (multiple latent conditions plus a trigger).

Likely effect:
- The model “fits to five” (template completion) rather than representing the causal structure honestly.

### E) Template completion pressure increases confabulation risk (Moderate, epistemic hazard)

Prompt evidence:
- Many required-looking slots: timestamps, authors, duration, business impact, owners, due dates (lines 97–108, 131–135).

Mechanism:
- When a prompt presents a high-fill template, models often satisfy the structure even when data is missing.
- This is not purely a formatting issue: in incident response, invented timestamps/ETAs/owners are **operationally harmful**.

Diagnostic signal:
- Specific times (“[HH:MM]”) and business impacts appear without being provided or derived from tools.

### F) “Blameless” instruction can suppress human factors investigation (Moderate)

Prompt evidence:
- “Postmortems are blameless — Focus on systems and processes, not individuals.” (line 158)

Mechanism:
- The intent is healthy, but cognitively it can be misread as “avoid examining human decision-making.”
- That suppresses an important causal layer: *what information was available at the time*, time pressure, ambiguous signals, and how tooling/alerts shaped decisions.

## 3) Seeds vs lenses (what’s prescribed vs how to look)

- The phase checklist (lines 35–55) and severity table (lines 60–65) are **seeds**. They are appropriate for orchestration/classification.
- The postmortem section is also heavily seeded via a fixed template and “5 Whys”. It contains **few investigative lenses** (open questions that encourage discovery, branching causality, or uncertainty tracking).

Net effect: the prompt is very strong at **workflow completion** and weaker at **open-ended causal discovery**.

## 4) Anchor inventory (explicit and implicit)

**Numeric anchors**
- SEV **1–4** severity classification (lines 36, 62–65)
- “5 Whys” fixed to **exactly five** steps (lines 118–123)
- “Summary: **2–3 sentence**…” (line 103)

**Structural anchors / fixed slots**
- Status update and postmortem templates (lines 71–138)
- Timeline tables with required columns (lines 89–93, 110–114)
- Action Items table columns (lines 131–135)

These anchors encourage uniform, box-filling outputs across incidents with very different causal shapes.

## 5) What to check for in outputs (diagnostic signals)

1) **5-Whys linearity**: a tidy five-step chain even when the incident likely has multiple contributing factors.
2) **Actionability bias**: root cause phrased to conveniently map to a discrete ticket rather than systemic enabling conditions.
3) **Evaluation bleed**: “What Went Poorly” items reappear as “Root Cause” (or vice versa), indicating judging is shaping investigation.
4) **Confident specifics without provenance**: timestamps, ETAs, “business impact”, owners/due dates appear without being supplied or pulled from connectors.
5) **Human-factors omission**: little to no “what was known at the time / why the decision made sense then,” suggesting blamelessness was interpreted as “ignore people.”

## 6) What to do about it (intervention options)

### Prompt-level optimisation (within a single skill)

Interventions that target the mechanisms above (without requiring a full pipeline):

- **Reduce cross-mode residue**: scope the prompt so only the relevant template/instructions are active per mode (status-update content should not be in-context during postmortem writing).
- **De-anchor causal analysis**: replace fixed “5 Whys” template pressure with an instruction to follow the evidence to natural depth and allow branching contributing factors.
- **Add mode boundaries inside postmortem**: make it explicit that postmortem work should sequence (timeline → causal investigation → evaluation → action items → synthesis), rather than doing all simultaneously.
- **Make uncertainty admissible**: explicitly allow “unknown / not yet determined / requires data” in template fields to reduce confabulation pressure.
- **Clarify blameless ≠ no humans**: direct the model to analyse decision environments through a systems lens.

Trade-off: cheaper than orchestration; some interference remains because multiple modes still share one context.

### Pipeline reconstruction (structural separation)

For robust separation (especially for postmortems), split into distinct stages with clean handoffs (structured outputs rather than prose):

- Timeline reconstruction (investigation + structuring)
- Causal analysis (deep investigation; no evaluation, no action items)
- Response evaluation (evaluation only)
- Action item generation (generation/planning)
- Postmortem synthesis (composition + reframing)

Trade-off: higher orchestration overhead; strongest protection against investigation/evaluation entanglement and 5-Whys anchoring.

## 7) Composition signature (runtime composition / connectors)

Skill components implied by “If connectors available” (lines 140–153):

- **Monitoring connector**: investigation support (pull alert details, show graphs)
- **Incident management connector**: orchestration/execution (create/update incident, page responders)
- **Chat connector**: communication generation + distribution (status updates, war room channel)

Compatibility notes:
- These tool integrations are largely compatible *if* the session stays in a single phase at a time.
- Risk pattern: operational tool use (monitoring + paging + chat updates) shares context with postmortem drafting, pulling the cognitive posture back toward present-tense incident handling.

## 8) Handoff notes for `prompt-writer`

Primary redesign target: **postmortem mode**, where investigation, evaluation, generation, and synthesis are currently forced into a single template-driven pass, with the 5-Whys double anchor.

Secondary target: prevent **cross-template contamination** by ensuring mode-specific instructions/templates are not all loaded at once.

Ready for handoff to `prompt-writer`.
