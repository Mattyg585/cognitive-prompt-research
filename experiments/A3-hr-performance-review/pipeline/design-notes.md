# Pipeline Design Notes: Manager Performance Review

## Why a pipeline only for manager review

The architect analysis identified three modes in the original prompt: self-assessment, manager review, and calibration. Only the manager review benefits from pipeline reconstruction.

**Self-assessment** is template generation — clean convergent work. The model produces a structured template with placeholder guidance. There is no investigation, no evaluation of real data, no synthesis. Tier 2 fixes (removing numeric anchors from slot counts) are sufficient.

**Calibration** is structuring + evaluation — a compatible convergent pair. The model organizes team data and compares against distribution references. Both operations are convergent, criteria-referenced work. They don't interfere. Tier 2 fixes (reframing distribution targets from table columns to prose context) are sufficient.

**Manager review** is where the modes collide. Investigation (understanding the performance data), evaluation (rating, goal assessment), synthesis (performance narrative), generation (development plan), and reframing (constructive feedback language) all operate in a single context. The primary interference is investigation + evaluation: the model knows it will need to produce a rating, strengths, and development areas, so it reads the performance data through that template rather than genuinely investigating what the data reveals.

## Why two agents, not more

The architect analysis identified five thinking types in the manager review. But not all adjacent pairs interfere.

**Investigation + Evaluation**: This is the toxic pair. The evaluation template pre-filters investigation — the model maps data to template slots rather than investigating the person's trajectory, contradictions, and growth patterns. Separating these is the core intervention.

**Evaluation + Synthesis + Generation**: These are all convergent work. Synthesis compresses investigated findings into a narrative. Evaluation assigns ratings based on evidence. Generation produces development plans and compensation recommendations. All three operate on the same material (the investigated findings) with compatible cognitive postures. Splitting them into separate agents would add orchestration overhead without resolving real interference.

I considered three possible splits:

1. **Two agents** (Investigator | Writer): Separates the toxic pair. Writer combines evaluation + synthesis + generation. This is the design I chose.

2. **Three agents** (Investigator | Synthesizer | Evaluator+Generator): Separates synthesis from evaluation. But synthesis and evaluation are compatible here — "understand the performance picture, then rate it" is a natural sequence. The evaluative posture doesn't constrain synthesis in the way it constrains investigation. Adding a third agent would test a theoretical concern without a demonstrated interference.

3. **Three agents, different split** (Investigator | Writer | Development Planner): Separates development plan generation from the review body. But development plans should flow from the same understanding that produces the performance summary — they're the "what next" that follows "where they are." Splitting them would likely produce a development plan disconnected from the review's narrative.

Two agents addresses the identified interference. Adding more would be architectural purity, not problem-solving.

## The rhythm

```
Performance Investigator → Review Writer
  (diverge)                  (converge)
```

A single expansion-compression cycle. The Investigator diverges — following threads, surfacing patterns, naming tensions. The Review Writer converges — synthesizing findings into a review, assigning a rating, committing to development actions.

This is the simplest pipeline structure: one cognitive mode separation, one handoff. The simplicity is proportional to the interference — the manager review has one primary toxic pair, so the pipeline has one split.

## Key design choices

**Lenses in the Investigator, template in the Writer.** The Investigator uses lenses (trajectory, growth patterns, contradictory signals, team impact, gap between potential and current level) to guide open investigation. The Review Writer uses the review template structure (performance summary, strengths, development areas, goal assessment, rating) as legitimate convergent output format. Lenses moved to where divergent work happens. Template moved to where convergent work happens.

**No rating in the Investigator's output.** The Investigator does not classify, rate, or judge. It surfaces what it finds. This is the structural intervention that eliminates evaluation-first ordering — the rating simply cannot come before the investigation because the investigator has no mechanism to produce one. The Review Writer arrives at a rating as a conclusion from the investigated evidence.

**No raw data in the Writer's context.** The Review Writer receives the Investigator's structured findings but not the original performance observations. If the writer also had the raw data, it might re-investigate in an evaluative context, reintroducing the contamination the pipeline removes. The writer trusts the investigation and synthesizes from its output.

**Promotion and compensation context withheld from the Investigator.** The manager's compensation and promotion intentions are evaluative conclusions. If the Investigator knows "not ready for IC5 this cycle," it will investigate in a way that confirms that conclusion rather than openly assessing readiness. The Review Writer receives these as context for the compensation recommendation section — appropriate at the evaluation stage.

**Bullets, not prose, in the handoff.** The Investigator produces structured findings as bullets and short descriptions, not as a narrative. Prose carries the investigative cognitive mode — exploratory framing, hedging, thread-following language. Bullets compress the findings and strip the mode, giving the Review Writer clean material for synthesis.

## What this tests

The experiment's hypothesis: the monolithic manager review template produces competent reviews, but the template-filling posture prevents genuine investigation, and the investigation quality determines the review's depth.

Specific predictions:

- **Investigation breadth**: The Investigator should surface patterns that aren't explicitly stated in the raw observations. For the Jordan Chen scenario: the raw data says "struggles with ambiguity" and "volunteered for cost optimization." A genuine investigation should notice the tension — initiative in one register (technical problem with clear scope) and avoidance in another (open-ended strategic problems). The monolithic version tends to list these as separate items; the pipeline should connect them.

- **Contradictory signals**: The Investigator should name tensions rather than resolving them prematurely. "Strong individual contributor who doesn't flag capacity problems" is a tension worth naming. "Great documentation that serves others but limited ability to communicate at executive level" is another. The monolithic version tends to smooth these into "strengths" and "development areas" without naming the underlying pattern.

- **Review depth**: The Review Writer, working from rich investigated material, should produce a Performance Summary that feels like genuine synthesis — capturing trajectory and nuance — rather than a restated rating. The development plan should name the specific capability gap (navigating ambiguity at IC5 level) rather than generic actions.

- **Natural variation**: If the pipeline were run on a different employee profile — someone with fewer contradictions, or someone with a clear promotion case — the Investigator should produce a different volume and focus of findings. The monolithic version tends toward uniform output regardless of input complexity.

## Trade-offs

**Added complexity.** Two agents with a handoff are more complex than one prompt. For a manager writing a quick review, the overhead may not be worth it. For an HR system processing reviews at scale, or for high-stakes reviews (promotion cycles, performance improvement plans), the deeper investigation is likely worthwhile.

**Orchestration.** Someone or something needs to run Stage 1, extract the findings, and pass them to Stage 2 with the right additional context. For the experiment, this is manual. In production, it would be automated.

**Wall-clock time.** Two sequential calls instead of one. Each is faster (smaller context, focused task), but the total is longer. A real cost for interactive use.

**Partial pipeline.** The pipeline only covers manager review mode. Self-assessment and calibration still use the Tier 2 single prompt. An orchestration layer would need to route by mode — straightforward but an additional design consideration for production use.

These are proportional trade-offs for the interference being addressed. The manager review has moderate mode interference with a clear toxic pair. The pipeline is a targeted intervention, not a wholesale reconstruction.
