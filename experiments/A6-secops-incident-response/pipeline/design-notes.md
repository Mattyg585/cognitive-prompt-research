# Pipeline Design Notes: Incident Postmortem

## Design Rationale

This pipeline reconstruction is the Tier 3 intervention for experiment A6. It separates the monolithic postmortem mode of the `/incident-response` prompt into five agents, each scoped to a compatible set of cognitive modes, with compressed handoffs between stages.

### Why five agents, not fewer

The architect analysis identified the postmortem mode as having the highest mode-mixing density of any experiment in the portfolio — six types of thinking in one template. Each combination creates a specific interference mechanism:

1. **Investigation + Evaluation** — the classic toxic pair. The model investigates root causes while simultaneously evaluating the incident response. Investigation becomes subordinate to evaluation — the model identifies causes that are evaluable ("someone did something wrong") and filters out systemic causes that don't fit the went-well/went-poorly frame. Architectural vulnerabilities, organisational blind spots, and process design failures get underweighted because they don't produce neat evaluative entries.

2. **Investigation + Generation** — solution-shaped investigation. The action items section is in context while the model traces causal chains. The model identifies root causes that have actionable fixes and softens causes that require long-term architectural change or organisational restructuring. Investigation becomes a funnel for recommendations.

3. **Causal investigation + 5 Whys structure** — double anchor. The 5 Whys template constrains both the count (exactly 5) and the shape (linear chain) of causal reasoning. Real incidents have causal trees. The template converts genuine causal investigation into a template-filling exercise.

4. **Synthesis during investigation** — premature narrative commitment. Lessons Learned and Summary are in the template alongside Root Cause and Timeline. The model commits to a narrative early and confirmation-biases the remaining investigation.

5. **Evaluation bleeding into timeline** — the What Went Well/Poorly sections contaminate timeline reconstruction with evaluative framing. The timeline becomes a record of things that went well or poorly rather than a neutral chronological reconstruction of what happened.

I considered whether any agents could be combined:

- **Timeline Reconstructor + Causal Analyst**: No. Timeline reconstruction is investigative/structural work (what happened, in what order). Causal analysis is deep investigation with synthesis (why did it happen, what made it possible). They need different postures — chronological documentation vs. thread-following causal reasoning. Combined, timeline reconstruction would prematurely commit to causal narratives.

- **Causal Analyst + Response Evaluator**: No. This is the core toxic pair for postmortems. Evaluation pre-filters causal investigation. The analyst must follow causal threads to uncomfortable systemic conclusions without the evaluative frame filtering what gets investigated.

- **Response Evaluator + Action Item Generator**: Possible with a scope boundary, but evaluative posture constrains generation toward obvious fixes. The generator should receive structured findings and design interventions without the evaluative process still active in its context.

- **Action Item Generator + Postmortem Synthesiser**: These have different cognitive postures — generation (produce specific, owned artifacts) vs. synthesis (compress everything into a coherent narrative). The generation posture would anchor the synthesiser to a clause-by-clause, action-item-by-action-item walkthrough rather than genuine narrative synthesis.

Five agents is the minimum that avoids interference. Not three, not six.

### Why sequential, not parallel

The Response Evaluator could start as soon as the Timeline Reconstructor finishes. But the causal analysis informs better evaluation — understanding why things happened changes how you evaluate the response. An evaluator who knows the root causes was an architectural vulnerability evaluates the detection gap differently than one who only sees the timeline.

Similarly, the Synthesiser could theoretically run as soon as Agents 1-3 finish (before action items). But the gap between findings and action items is itself a lesson — the synthesiser produces deeper lessons when it can see what interventions are being proposed for each root cause.

The sequential cost is real (five serial calls), but each agent works in a clean context with compressed inputs. The total wall-clock time is longer than one pass. The question is whether the output quality justifies it.

### Key design choices

**Blameless reframe carried through every agent.** The original prompt's blameless directive ("focus on systems and processes, not individuals") pre-filters investigation, causing the model to avoid examining human decision-making entirely. Each agent in the pipeline carries a reframed version: "examine human decisions through a systems lens — why did the decision seem correct at the time?" This isn't a single directive that might be forgotten — it's embedded in each agent's posture.

**The Timeline Reconstructor documents information state.** The annotated timeline includes what was known at each decision point, not just what happened. This is the foundation for blameless analysis — understanding decisions requires understanding the information available when the decision was made. Hindsight makes decisions look obviously wrong when they were reasonable given what was known.

**The Causal Analyst uses lenses, not the 5 Whys.** The analyst receives four lenses: "What made this possible? What made it invisible? Where did the system's assumptions fail? What human decisions were shaped by missing information?" These guide how to investigate without constraining the shape or depth of the analysis. The analyst follows evidence to natural depth — may be two levels deep, may be seven, may branch into multiple contributing factors at each level.

**Causal structure is described explicitly.** The Causal Analyst documents the shape of the causal analysis (linear, branching, circular, converging) rather than fitting it to a predetermined template. Real incidents have diverse causal structures. A template that assumes linearity forces complex causation into a shape that misrepresents it.

**Action items link to specific findings.** Each action item references the specific root cause or response gap it addresses, with a rationale explaining how the fix matches the depth of the cause. Systemic causes should get systemic action items, not surface-level patches. This linking is explicit in the output format, preventing the common failure mode where action items are generated from general impressions rather than specific findings.

**The Synthesiser composes, it doesn't investigate.** The final agent receives all structured outputs and writes the postmortem document. It writes the summary, synthesises lessons learned, and ensures narrative coherence. It does not dig into new causal threads or generate new action items — those stages are complete. This prevents the synthesis agent from reopening investigation or evaluation, which would introduce mode contamination at the final stage.

**No numeric anchors anywhere.** No "list at least N action items." No "identify N root causes." No fixed counts in any section. Output volume should respond to the incident's complexity, not to the prompt's suggestions.

### What this tests

The experiment's hypothesis: good output hides great output. The monolithic postmortem template produces competent postmortems. The question is whether separated contexts produce qualitatively different output in specific, measurable ways:

- **Causal depth**: Does the Causal Analyst produce root cause analysis with genuine depth — branching factors, systemic vulnerabilities, human-systems interaction — versus the monolithic version's neat linear chain to an actionable root cause?
- **Human factors**: Does the pipeline examine why humans made the decisions they did, or does "blameless" still mean "avoid human decisions"?
- **Action item depth matching**: Do systemic findings get systemic interventions, or are they softened into surface-level patches?
- **Lesson specificity**: Are lessons learned genuine insights about the system ("our annotation system treats security as an attribute rather than a constraint"), or generic platitudes ("we need better testing")?

If Tier 2 (the optimised single prompt) improves incrementally and Tier 3 (this pipeline) produces a qualitative leap, the finding supports the core thesis: the monolithic prompt is the ceiling, not the floor.

### Trade-offs

**Added complexity.** Five agents with handoffs are more complex to run than a single prompt. For a one-off postmortem, the overhead may not be worth it. For an organisation that runs postmortems regularly and wants consistently deep analysis, the pipeline is likely worthwhile.

**Wall-clock time.** Sequential execution means roughly five serial calls. Each agent runs faster (smaller context, focused task), but the total is still longer than one pass. This is a real cost for time-sensitive postmortems.

**Orchestration.** Someone or something needs to manage the handoffs — extract structured output from each agent, pass it to the next with the right format. In a production system, this would be automated. For the experiment, it's manual.

These are the right trade-offs for a Tier 3 reconstruction. The question isn't whether the pipeline is simpler — it's whether it produces meaningfully better output.
