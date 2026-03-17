# Blind Evaluation: A2 Marketing Content — V2 (Voice-Continuity Test)

## Setup

Three blog posts written for the same product launch brief (Relay async collaboration platform). Each produced by a different prompting approach. Evaluated blind — the evaluator received candidates labelled A, B, C with no information about which approach produced which output.

**No rubric.** The evaluator was asked only: "Which is the best piece of writing? Which would you publish as the hero content? Why?" No dimensions, no scoring criteria, no priming for what to look for.

**Model**: Sonnet (same model that produced all three outputs)

## The Key

| Candidate | Tier | Approach |
|-----------|------|----------|
| A | Tier 1 (Baseline) | Original SKILL.md prompt |
| B | Tier 3 (Pipeline v2) | 2-stage: investigate-and-write → editor |
| C | Tier 2 (Optimised v2) | Single context, scope-bounded phases |

## The Ranking

**1. Candidate B (Tier 3 — 2-stage pipeline)**
**2. Candidate A (Tier 1 — baseline)**
**3. Candidate C (Tier 2 — optimised)**

## Key Quotes from the Evaluator

**On Candidate B (Tier 3):**
- "B is the best piece of writing, and it's not particularly close."
- "The opening is doing something the other two aren't. It starts with a scene... specific in a way that immediately signals the writer understands the reader's world."
- On the deep work section: "That's a genuine idea, stated with conviction. It earns the feature description that follows rather than just prefacing it."
- "That is not adoption. That is integration." — "a real distinction"
- "The ending closes the loop cleanly — it returns to the eleven-person team from the opening, which gives the piece structural integrity. That's craft, not just technique."

**On Candidate A (Tier 1):**
- "A is well-organized and covers the ground."
- "After the opening, it becomes a product walkthrough."
- "The closing is fine but forgettable."

**On Candidate C (Tier 2):**
- "It doesn't do anything badly, which is its problem — it does everything competently and nothing memorably."
- "The headline is genuinely bad... That number — 47 — is doing the work a real idea should do."
- "The subhead is even worse... This is boilerplate."
- "'We don't love citing our own metrics' is an attempt at self-awareness that backfires."

**The summary diagnosis:**
> "The gap is at the level of thinking, not execution. A and C are both writers who understood the brief and executed it well. B is a writer who had something to say."

## What This Means

### The 2-stage pipeline won on voice AND depth

The previous A2 experiment (4-stage pipeline) found that Tier 3 won on technical dimensions but external evaluators split on voice — one ranked Tier 2 first, detecting that the pipeline output "reads slightly more 'edited' than 'written'."

This 2-stage pipeline won unambiguously on voice. The evaluator described it as craft, conviction, and genuine ideas — not just technical polish. The voice-continuity hypothesis is supported: combining investigation and writing in a single context produces stronger, more sustained voice than separating them.

### Tier 2 came last

This is the most surprising result. In the previous experiment, Tier 2 was the consistent improver — always better than baseline, competitive with pipeline on voice. Here, the optimised v2 prompt was ranked below the baseline.

The evaluator's specific criticism — "the headline is genuinely bad," the subhead is "boilerplate," the metrics hedge "backfires" — suggests that the Tier 2 prompt's three-phase structure (investigate → write → polish) may have produced writing that is technically correct but lacks conviction. The phase boundaries within a single context may create a different kind of interference: the model knows it's about to be evaluated (Phase 3 is in the prompt), so it writes safely.

This is a new finding: **evaluation criteria don't need to be in a separate section to suppress voice. Their mere presence in the prompt — even if they say "ignore these for now" — may activate pre-editing behaviour.**

### The baseline outperformed the optimised prompt

Candidate A (baseline) was ranked second. This may be because the original prompt's template structure, while producing formulaic output, at least produces output with clear conviction about what it is. The optimised prompt's attempt to be both investigative and compliant may have produced neither with full commitment.

### The pipeline's advantage is investigative depth, not just clean context

The evaluator's core insight: "B has a theory of the problem — not just 'distributed teams have too many meetings' but 'the tool is asking teams to perform catch-up as a meeting because the tool can't do the catch-up itself.' That's a real insight, and it organizes everything else in the piece."

This insight — the catch-up meeting as a structural failure of the tool, not a cultural failure of the team — emerged from the investigate-and-write agent having space to explore without compliance pressure. Neither the baseline nor the optimised prompt produced this level of diagnostic thinking.

## Limitations

- Single run per tier (not 3 runs as in previous experiment)
- Same model generating and evaluating
- One evaluator (would benefit from multiple blind evaluators)
- The Tier 2 result may partly reflect prompt quality rather than the approach — the v2 optimised prompt may have specific issues independent of the single-context vs pipeline question

## What to Test Next

1. Multiple runs per tier to check consistency
2. Cross-model evaluation (have a different model evaluate)
3. Whether the Tier 2 underperformance is replicable or an artifact of this specific prompt revision
4. Whether the 2-stage pipeline advantage holds across different briefs and content types
