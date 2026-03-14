# Pipeline Design Notes: Engineering Debug

## Design Rationale

This pipeline reconstruction is the Tier 3 intervention for experiment A5. It separates the monolithic `/debug` prompt into two agents — Investigator and Fix Designer — with a compressed handoff between stages.

### Why two agents, not more

The original prompt has four steps: Reproduce, Isolate, Diagnose, Fix. The first three are all investigation work. They share the same cognitive posture (open, evidence-following, hypothesis-testing) and benefit from shared context (reproduction findings inform isolation, isolation findings inform diagnosis). Splitting investigation into separate agents would break these natural dependencies and add orchestration overhead for no cognitive benefit. Investigation + Structuring is a compatible combination.

Similarly, fix generation and side-effect evaluation (Step 4) are both convergent work operating on the same problem. Proposing a fix and immediately evaluating its side effects, edge cases, and regression risks is a natural cognitive flow — "design then stress-test" within a single focused context. Splitting these would fragment the fix without reducing interference.

The single split that matters is between Investigation (Steps 1-3) and Generation (Step 4). That is where the mode interference lives. Two agents is the minimum — and the maximum — that addresses the actual problem.

I considered whether this experiment even needs a pipeline (the interference is low-to-moderate and the original prompt is well-structured). But this is precisely the value of A5 as a calibration case: if a well-structured prompt still shows improvement from pipeline separation, that strengthens the thesis. If it doesn't, that calibrates the boundary — there's a threshold of interference below which prompt-level fixes are sufficient.

### Why the Fix Designer doesn't receive the original bug report

The Investigator's structured findings contain everything the Fix Designer needs: what the problem is, what causes it, evidence supporting the diagnosis, confidence levels, blast radius. Passing the original bug report to the Fix Designer would reintroduce investigative context — raw symptoms, unanswered questions, the messy initial picture. The Fix Designer might be tempted to re-investigate rather than trusting the structured findings.

This is a deliberate constraint. In real debugging, the person designing the fix often re-reads the original report and second-guesses the diagnosis. Sometimes that's valuable. But in a pipeline testing whether clean context separation improves output, the Fix Designer should demonstrate what generation looks like when investigation has been fully resolved before it begins.

### Key design choices

**Lenses in the Investigator, structure in the Fix Designer.** The Investigator uses lenses to guide exploration: "What changed? What's the scope? Where does behaviour diverge from expectations? What hypotheses explain the symptoms?" These open the investigation space without prescribing what to find. The Fix Designer uses structured output because generation benefits from clear organisation — the fix, its rationale, its risks, its prevention measures.

**Confidence levels in the handoff.** The Investigator reports confidence in its root cause analysis. This is important for the Fix Designer: a high-confidence root cause warrants a targeted fix; a moderate-confidence root cause warrants a fix that addresses the most likely cause while being robust to alternative explanations. The confidence level shapes the fix design without requiring the Fix Designer to re-investigate.

**No "immediate mitigation vs. permanent fix" distinction in the Investigator.** The original analysis noted that the model often proposes an immediate mitigation and a longer-term fix. This is a valid pattern, but it's the Fix Designer's job to decide whether the situation warrants both. The Investigator provides the root cause and blast radius; the Fix Designer decides the intervention strategy. Prescribing "immediate + permanent" in the Investigator would be telling it to think about fixes during investigation — exactly what the pipeline separates.

**Fix level is explicitly open.** The Fix Designer prompt does not default to code-level fixes. It asks: what level does this fix need to operate at? Code, configuration, architecture, process, organisational? The answer should follow from the root cause. A shared-resource contention issue might need an architectural fix (separate the resources) or a process fix (coordinate the teams that share it) or both. Defaulting to code patches is the proximate-cause trap.

### What this tests

This is a calibration experiment. The original prompt is already reasonably well-structured — clean sequential steps, no numeric anchors, no seeds, lightweight template. The Tier 2 optimisation adds a scope boundary, a diagnosis output section, and reframed fix guidance.

The pipeline tests whether removing fix-awareness from the investigation context entirely — not just de-prioritising it with a scope boundary, but eliminating it — produces meaningfully different investigation output.

Specific things to compare across tiers:

- **Hypothesis count**: How many distinct hypotheses does each tier consider? The pipeline Investigator has no fix to aim at and should explore more broadly.
- **Root cause depth**: Does the analysis stop at the proximate trigger or explore systemic factors? The pipeline Investigator has no incentive to prefer fixable causes over systemic ones.
- **Fix-cause alignment**: When the root cause is systemic, does the fix match? The Tier 2 prompt's reframed fix guidance encourages this, but the fix section is still visible during investigation. The pipeline ensures the root cause is identified without fix-level considerations.
- **Prevention specificity**: Are prevention measures specific to the failure mode discovered? Generic prevention ("add monitoring") suggests the model is filling a template slot rather than reasoning from the diagnosis.

If Tier 2 and Tier 3 produce similar investigation depth, the scope boundary is sufficient for this level of interference and full pipeline separation is overkill for well-structured prompts. That would be a useful finding — it calibrates where the intervention threshold sits.

If Tier 3 produces meaningfully deeper investigation (more hypotheses, systemic root cause analysis, broader consideration of contributing factors), the finding is that even well-structured prompts benefit from pipeline separation, and the scope boundary — while helpful — doesn't fully eliminate the fix-destination effect.

### Trade-offs

**Minimal added complexity.** Two agents with one handoff is the lightest possible pipeline. The orchestration overhead is small — extract the Investigator's output, pass it to the Fix Designer.

**Moderate wall-clock time increase.** Two sequential passes instead of one. Each pass is faster (smaller context, focused task), but the total is still longer. For interactive debugging this is a real cost. For post-incident analysis where thoroughness matters more than speed, it's worthwhile.

**Loss of investigative context in fix design.** The Fix Designer doesn't have the raw bug report or the investigation journey — only the structured findings. If the Investigator's compression loses something important, the Fix Designer can't recover it. This is a deliberate trade-off: clean context at the cost of some information loss. The Investigator's output format is designed to preserve everything material, but edge cases may slip through.
