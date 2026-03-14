# Pipeline Design Notes: Design Research Synthesis

## Why a pipeline

The architect identified this experiment as the strongest candidate for demonstrating pipeline improvement. The original prompt fuses five types of thinking (investigation, structuring, synthesis, evaluation, reframing) into a single context, all constrained by a rigid output template. The template doesn't just format -- it changes the kind of thinking the model does.

The specific interference mechanisms:

1. **Investigation + Template** -- the most damaging fusion. The output template (theme slots, evidence format, Impact/Effort grid, numbered recommendations) is in context while the model reads transcripts. Investigation becomes extraction: the model reads *for* things that will fill the template rather than reading *to understand* what participants experienced. Patterns that resist easy categorisation get filtered out at the investigation stage, before they have a chance to become insights.

2. **Investigation + Evaluation** -- the classic toxic pair. Impact/Effort columns require the model to evaluate findings it's still in the process of investigating. This biases investigation toward patterns that are easy to evaluate -- clear, actionable, classifiable. Subtle patterns, ambiguous signals, and emerging themes get suppressed because they don't produce clean Impact/Effort ratings.

3. **Synthesis + Reframing** -- moderately compatible but degraded when simultaneous. The model synthesises patterns while also reframing them for business stakeholders, which pulls synthesis toward themes that have obvious product implications and away from themes that are interesting but harder to translate. Research synthesis should capture what the data says, then separately ask what it means for the product.

A Tier 2 revision (scope boundaries, responsive template, summary moved to end) reduces these interferences but can't eliminate them. The evaluation criteria and output structure are still in context during investigation. The model has to actively suppress patterns it's already activated. The pipeline removes the suppression problem entirely by giving each type of thinking its own clean context.

## Why three agents (not two, not four)

### Why not two?

I considered a two-agent split: "Investigator" (reads data, surfaces observations) and "Synthesiser-Translator" (identifies patterns AND translates for stakeholders). But synthesis and reframing are different postures. Synthesis asks "what patterns exist in this data?" -- it follows the evidence. Reframing asks "what does this mean for our product?" -- it follows the audience's needs. Combining them risks reframing contaminating synthesis: the model identifies patterns that translate easily and underweights patterns that are real but harder to act on.

The classic research failure mode is surfacing only "actionable insights" while missing the deeper structural patterns that would have reframed the product strategy entirely. The two-agent design preserves this failure mode.

### Why not four?

I considered splitting the Strategic Translator into "Insight Generator" (what do patterns mean?) and "Recommender" (what should we do?). But generation and light evaluation are compatible cognitive modes -- both are forward-looking, both work from the same synthesised evidence, and the evaluative component in the translator is light (ordering by evidence strength, not scoring on a grid). Splitting them adds orchestration overhead without resolving mode interference. The key separations -- investigation from synthesis, synthesis from reframing -- are already achieved with three agents.

I also considered a fourth "Structurer" agent between investigation and synthesis to organise observations before pattern-finding. But structuring is the lightest of the five thinking types here, and it serves investigation (organising what was found) rather than being a distinct cognitive act. The Data Reader includes light structuring in its output format. Adding a separate agent for structuring alone would produce a handoff that adds latency without cognitive benefit.

Three agents is the minimum that avoids the identified interference patterns. Each split addresses a specific, documented interference -- not architectural purity.

## The rhythm

```
Data Reader → Pattern Synthesiser → Strategic Translator
 (diverge)       (converge)           (diverge/converge)
```

1. **Diverge**: Read the data openly, follow threads, surface what's there without categorising or evaluating
2. **Converge**: Look across all observations for patterns -- what clusters, what contradicts, what's emerging
3. **Diverge then converge**: Translate patterns into implications (divergent: what could this mean?) and then into recommendations (convergent: what should we do?)

The Strategic Translator contains both divergent and convergent elements. This is acceptable because the divergence (exploring implications) and convergence (forming recommendations) are of compatible types -- both are forward-looking and stake-oriented. The incompatible types (investigation + evaluation, open synthesis + audience reframing) have already been separated.

## Key design choices

### Lenses in the Data Reader, not seeds

The original prompt's output template acted as an implicit seed for investigation -- it told the model what categories of things to find (themes, segments, impact ratings). The Data Reader uses lenses instead: "What are people actually doing vs. what they say? Where do participants contradict each other? What's unsaid? What workarounds have they developed?" These open investigation rather than directing it toward predetermined categories.

The lenses are framed as questions, not as finding categories. "What workarounds have they developed?" invites exploration. "Workarounds: [list]" in a template invites extraction.

### Raw data stays with the Data Reader

The Pattern Synthesiser and Strategic Translator do not receive the raw transcripts. This is a deliberate design choice. If the Synthesiser had access to raw data, it could re-investigate -- and it would re-investigate through the lens of themes it's beginning to form, which is exactly the premature convergence the pipeline is designed to prevent. The Data Reader's structured observations are the canonical representation of the data for all downstream agents.

This means the Data Reader's thoroughness is critical. If it misses something in the data, that observation is lost to the pipeline. This is a real trade-off. But the alternative -- giving every agent access to raw data -- recreates the monolithic context problem. The Data Reader's clean investigative context is the pipeline's primary intervention.

### No study context for downstream agents

The Pattern Synthesiser and Strategic Translator receive only the previous agent's output. They don't receive the research question, study method, or participant demographics separately. This information is available to the Data Reader (who may reference it in observations) and flows through the structured handoffs as needed. Passing study context directly to downstream agents would introduce a mild framing bias -- knowing the research question ("why does usage drop after 3-4 months?") would bias pattern synthesis toward attrition-related themes.

### Output format responsive, not rigid

Each agent has a suggested output structure but explicit permission to adapt it. The Data Reader surfaces observations in whatever categories the data warrants -- not a fixed list. The Pattern Synthesiser identifies as many or as few themes as the evidence supports. The Strategic Translator produces recommendations proportional to the evidence strength. No numeric anchors in any agent.

### Scope boundaries are explicit and negative

Each agent prompt includes a clear statement of what it does NOT do. The Data Reader does not identify themes. The Pattern Synthesiser does not evaluate business impact. These negative scope boundaries are more effective than positive ones ("focus on investigation") because they name the specific temptation to resist.

## What this tests

The experiment's hypothesis: good output hides great output. The monolithic prompt produces competent research synthesis. The question is whether separated contexts produce qualitatively different output in specific, measurable ways:

- **Investigation breadth**: Does the Data Reader surface observations that the monolithic version misses -- particularly subtle patterns, emotional signals, contradictions between said and done, and workarounds that reveal unmet needs?
- **Theme originality**: Does the Pattern Synthesiser find themes that the monolithic version doesn't -- not just more themes, but structurally different ones that emerge from open investigation rather than template-shaped extraction?
- **Tension and contradiction**: Does the Synthesiser capture genuine tensions in the data, or does it present themes as cleanly independent categories? Real research data is contradictory. The synthesis should reflect that.
- **Strategic depth**: Does the Translator produce genuine product implications, or does it restate themes with "recommendation" language bolted on? The translator should reason about what patterns mean for the product and its users.
- **Natural variation**: Do output volumes vary with data complexity? A 6-interview study and a 30-interview study should produce very different syntheses -- in depth, in theme count, in recommendation specificity.

If Tier 2 (the optimised single prompt) improves incrementally and Tier 3 (this pipeline) produces a qualitative leap, the finding supports the core thesis: the monolithic prompt is the ceiling, not the floor.

The key signal: after reading the pipeline output, re-read the transcripts. Are there patterns in the pipeline output that the monolithic version missed? If so, the investigation separation worked. Are the pipeline's themes structured differently -- capturing tensions and relationships rather than presenting independent categories? If so, the synthesis separation worked.

## Trade-offs

**Reduced self-correction.** In the monolithic prompt, the model can re-read the data if a theme doesn't hold up during synthesis. In the pipeline, the Pattern Synthesiser works only from the Data Reader's observations. If the Reader missed something, it's gone. This places high demands on the Reader's thoroughness -- but the Reader's clean investigative context is the primary reason it should be more thorough than the monolithic version.

**Added complexity.** Three agents with handoffs are more complex to orchestrate than a single prompt. For a quick synthesis of a few interviews, the overhead may not be worth it. For a production research workflow processing studies repeatedly, the pipeline structure becomes an asset.

**Wall-clock time.** Sequential execution means approximately 3x the latency. Each agent runs faster (smaller context, focused task), but the total is still longer than one pass. For interactive use, this is a real cost. For batch processing or production workflows, it's acceptable.

**Loss of holistic context.** The monolithic prompt has access to everything simultaneously -- raw data, themes, implications, recommendations. This allows a certain coherence. The pipeline sacrifices this for cognitive purity at each stage. The handoffs are designed to preserve the information that matters while dropping the cognitive residue that contaminates. Whether this trade-off nets positive is exactly what the experiment tests.

These are the right trade-offs for a Tier 3 reconstruction. The question isn't whether the pipeline is simpler -- it's whether it produces meaningfully better research synthesis.
