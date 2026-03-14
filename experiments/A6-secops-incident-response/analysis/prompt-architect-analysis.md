# Prompt Architect Analysis: SecOps Incident Response

## 1. What the Prompt Is Actually Asking For

This prompt manages an incident lifecycle across four phases, each requiring different types of thinking:

**Phase 1 — Triage**: Evaluation (severity assessment), Investigation (identify affected systems), Structuring (assign roles). Mixed but short-duration — acceptable.

**Phase 2 — Communicate**: Reframing (translate technical status for different audiences), Generation (draft updates). Compatible — both serve the same goal.

**Phase 3 — Mitigate**: Investigation (what's happening), Structuring (timeline), Evaluation (confirm resolution). Mixed but focused on operational action.

**Phase 4 — Postmortem**: This is where the modes collide. The postmortem template requires:
- **Timeline reconstruction** — Investigation + Structuring (what happened, in what order)
- **Root cause analysis** — Deep Investigation (why did this happen?)
- **5 Whys** — Constrained Investigation with numeric anchor (exactly 5 causal levels)
- **What went well / What went poorly** — Evaluation (judging the response)
- **Action items** — Generation (producing remediation tasks)
- **Lessons learned** — Synthesis (compressing everything into takeaways)

Six types of thinking in one template. This is the highest mode-mixing density of any experiment in the portfolio.

## 2. Where Modes Interfere

### 2.1 The "5 Whys" Is a Double Anchor (High)

The 5 Whys template is both a **numeric anchor** (exactly 5 levels) and a **structural anchor** (linear causal chain). Real incidents rarely have linear causation — they have causal trees, feedback loops, and contributing factors at multiple levels. Some incidents have 2 meaningful "whys" and some have 8. The 5 Whys format forces:

- **Exactly 5 levels**: The model will stretch shallow causes across 5 levels (adding artificial intermediate causes) or compress deep causal chains to fit 5 levels (truncating the analysis)
- **Linear chain**: Each "why" leads to exactly one next "why." Real root cause analysis reveals multiple contributing factors at each level. The 5 Whys structure prevents the model from branching.

**Mechanism**: The 5 Whys becomes a template-filling exercise rather than genuine causal analysis. The model works backward from "what sounds like a root cause" and fills in 5 steps to get there, rather than genuinely investigating causal structure.

**Severity**: High. This is the most impactful single anchor in the prompt. It doesn't just constrain count — it constrains the SHAPE of causal reasoning.

### 2.2 The Postmortem Template Is a Four-Mode Collision (High)

The postmortem output template places Timeline, Root Cause, 5 Whys, What Went Well, What Went Poorly, Action Items, and Lessons Learned in a single output structure. The model generates all of these in one pass, in one context.

**Mechanism**: The evaluation sections (What Went Well/Poorly) contaminate the investigation sections (Root Cause, Timeline). The model investigates root cause while simultaneously evaluating the response, which means it investigates causes that are response-evaluable — causes where someone did something wrong or right. Systemic causes (architectural vulnerabilities, missing automation, organisational blind spots) get filtered out because they don't fit the "went well / went poorly" evaluation frame.

Similarly, the Action Items section (generation) shapes the Root Cause analysis — the model identifies root causes that have actionable fixes. Causes that require long-term architectural change or organisational restructuring get softened because they don't produce neat action items.

### 2.3 Cross-Phase Template Contamination (Moderate)

All templates (Status Update AND Postmortem) are in the prompt regardless of which mode is invoked. When running in postmortem mode, the Status Update template's operational framing ("what's happening, who's affected, what we're doing") is in context. This pushes the postmortem toward operational reporting rather than reflective analysis.

**Mechanism**: The Status Update template establishes an operational, present-tense, action-oriented posture. The postmortem needs a reflective, past-tense, analytical posture. Having both in context creates posture conflict.

### 2.4 The "Blameless" Directive Pre-Filters Investigation (Moderate)

"Postmortems are blameless — Focus on systems and processes, not individuals" is important and correct as a cultural principle. But as a cognitive directive, it can pre-filter investigation. The model may avoid investigating human decision-making entirely — not just blame, but genuine analysis of decision-making under pressure, information gaps that led to incorrect assumptions, communication failures between individuals.

**Mechanism**: "Blameless" is interpreted as "don't examine human factors" rather than "examine human factors through a systems lens." The investigation drops an entire category of contributing factors. Real blameless postmortems examine human decisions deeply — they just do so through a systems lens (what information was missing? what pressures existed? what made the incorrect decision seem correct at the time?).

### 2.5 Severity Classification as Evaluation Seed (Low-Moderate)

The SEV1-4 classification table with specific criteria acts as a seed — it tells the model exactly what each severity level means. This is appropriate for convergent classification work (severity assignment IS classification) but it can anchor the model's investigation to the severity framing. A SEV2 incident gets SEV2-depth investigation.

## 3. What to Check For in the Output

- **5 Whys linearity**: Does the root cause analysis follow a neat 5-step linear chain? Compare with the incident data — is the actual causal structure linear, or does it have branches and contributing factors that the 5 Whys compressed?
- **Root cause actionability bias**: Is the identified root cause one that conveniently maps to a specific action item? If the root cause is "developer used wrong annotation" rather than "the system allows security-critical behaviour to be determined by a single annotation with no verification layer," the investigation was shaped by the action item destination.
- **Human factors avoidance**: Does the postmortem examine why the developer chose `@Public`? Why QA tested from an authenticated session? Why the security scan only checks dependencies? Or does it stop at the surface level of "what happened" without examining "why did the humans make these decisions?"
- **Evaluation bleeding into investigation**: Does the "What Went Poorly" section contain items that are also discussed as root causes? If so, evaluation is shaping investigation — the model is finding root causes that are simultaneously evaluable as "things that went poorly."
- **Lessons Learned depth**: Are lessons generic ("we should test more") or specific and insight-driven ("our annotation system treats security as an attribute rather than a constraint, creating a class of vulnerability that can't be caught by any of our current verification layers")?

## 4. What to Do About It

### Tier 2 — Prompt-Level Optimisation

1. **Replace "5 Whys" with open causal analysis**: Change to "Root Cause Analysis — Trace the causal chain as deep as the evidence supports. Some incidents have shallow causes; others have deep, branching causal structures. Follow the evidence rather than fitting to a fixed number of levels. If multiple contributing factors exist at the same level, document them all."
2. **Add scope boundary to postmortem mode**: "When writing a postmortem, you are doing reflective analysis, not operational reporting. Take a step back from the incident and examine it as a system — what made this possible, what made it invisible, what made the response effective or ineffective."
3. **Reframe the blameless directive**: Change to "Postmortems are blameless — this means examining human decisions through a systems lens, not avoiding them. Why did the decision seem correct at the time? What information was missing? What pressures existed? Understanding decisions is different from assigning blame."
4. **Lighten the postmortem template**: Remove fixed section ordering. Let the model determine what sections are most relevant for this specific incident. Some incidents need deep timeline analysis; others need deep causal analysis. The template should support both.
5. **Separate the phase templates**: Only include the relevant template for the invoked mode. Don't load Status Update template when in postmortem mode.

### Tier 3 — Pipeline Reconstruction

Pipeline reconstruction should show significant improvement for the postmortem mode specifically.

**Agent 1 — Timeline Reconstructor** (Investigation + Structuring)
- Receives: incident data, logs, events
- Does: reconstructs what happened in chronological order. Documents events, decisions, information flow. Notes what was known at each decision point.
- Produces: structured timeline with annotations — what happened, what was known, what was decided, what information was missing at each point
- Why separate: timeline reconstruction is investigative/structural work that shouldn't be contaminated by evaluation or causal analysis. Pure chronological documentation.

**Agent 2 — Causal Analyst** (Deep Investigation + Synthesis)
- Receives: structured timeline from Agent 1
- Does: traces causal chains from the timeline. Follows causes as deep as the evidence supports — may be 2 levels, may be 7, may branch. Identifies contributing factors, systemic vulnerabilities, and the causal structure (linear, branching, circular).
- Produces: causal analysis — root causes with evidence, contributing factors, systemic vulnerabilities. NOT action items (that's generation, incompatible with investigation).
- Why separate: causal analysis without evaluation or fix-generation in context allows the model to follow threads to uncomfortable conclusions — architectural flaws, organisational blind spots, systemic vulnerabilities that don't have simple fixes.

**Agent 3 — Response Evaluator** (Evaluation)
- Receives: structured timeline from Agent 1 + causal analysis from Agent 2
- Does: evaluates the incident response itself — what worked, what didn't, where was the response effective, where did it fall short. Evaluates against the timeline (was detection fast enough? was communication clear?).
- Produces: structured evaluation — what went well, what went poorly, with specific evidence from the timeline
- Why separate: evaluation in its own context can be thorough without contaminating the investigation. It receives already-investigated material and evaluates it, rather than simultaneously investigating and judging.

**Agent 4 — Action Item Generator** (Generation + light Evaluation)
- Receives: causal analysis from Agent 2 + response evaluation from Agent 3
- Does: generates specific, owned, prioritised action items that address root causes and response gaps. Matches fix depth to cause depth — systemic causes get systemic action items, not band-aid fixes.
- Produces: action items with owners, priorities, and rationale linking each to a specific finding
- Why separate: generation works best when it receives fully investigated and evaluated input. The generator doesn't need to investigate or evaluate — it designs interventions based on clear findings.

**Agent 5 — Postmortem Synthesiser** (Synthesis + Reframing)
- Receives: all outputs from Agents 1-4
- Does: composes the final postmortem document. Writes the summary, synthesises lessons learned, ensures the document tells a coherent story.
- Produces: the final postmortem document
- Why separate: synthesis is the last step. It receives all the raw material and compresses it into a coherent narrative. It doesn't need to investigate, evaluate, or generate — just synthesise and compose.

**Handoff Design**:
- Agent 1 → Agent 2: structured timeline (events, decisions, information state). Strips narrative.
- Agent 1 → Agent 3: same structured timeline
- Agent 2 → Agent 3: causal analysis (root causes, contributing factors). Structured, not prose.
- Agent 2 → Agent 4: causal analysis
- Agent 3 → Agent 4: response evaluation (what worked, what didn't). Structured.
- Agents 1-4 → Agent 5: all structured outputs for final composition.

**Execution**: Mostly sequential. Agent 1 first. Agent 2 depends on Agent 1. Agent 3 depends on Agents 1+2. Agent 4 depends on Agents 2+3. Agent 5 depends on all.

## 5. Composition Signature

Single-prompt skill with three modes. No pairwise composition conflicts between modes (they don't run simultaneously). Within the postmortem mode:
- Investigation + Evaluation (incompatible — simultaneous in template)
- Investigation + Generation (incompatible — action items shape root cause analysis)
- Synthesis during Investigation (incompatible — lessons learned before investigation is complete)
- Investigation with 5 Whys anchor (constraining — numeric and structural anchor on investigative work)

## 6. Overall Assessment

**Severity: High.** The postmortem mode has the highest mode-mixing density of any experiment in the portfolio. Six types of thinking forced into one template, with the 5 Whys as a particularly impactful double anchor (numeric + structural). The "blameless" directive, while culturally important, adds an investigation filter that drops human factors analysis.

**Expected experimental outcome**: Tier 2 should show noticeable improvement (removing 5 Whys anchor, reframing blameless, adding scope boundary). Tier 3 should show significant improvement — the five-agent pipeline separates every incompatible mode pair and provides clean context for each type of thinking. The causal analysis in particular should be deeper and more structurally honest when freed from the 5 Whys constraint and fix-generation pressure.

The key signal: does the pipeline version produce a root cause analysis with genuine causal depth — branching factors, systemic vulnerabilities, human-systems interaction — versus the monolithic version's neat 5-step linear chain to an actionable root cause?
