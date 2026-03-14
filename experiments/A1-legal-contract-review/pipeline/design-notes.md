# Pipeline Design Notes: Contract Review

## Design Rationale

This pipeline reconstruction is the Tier 3 intervention for experiment A1. It separates the monolithic `/review-contract` prompt into four agents, each scoped to a single cognitive mode, with compressed handoffs between stages.

### Why four agents, not fewer

The architect analysis identified four fused thinking types: investigation, evaluation, generation, and synthesis. Each adjacent pair in the original prompt creates a specific interference mechanism:

1. **Investigation + Evaluation** — the classic toxic pair. The playbook's 120+ lines of evaluation criteria (54 specific elements, 25 named issues, 12 category table) are in context while the model reads the contract. Investigation becomes subordinate to evaluation — the model reads *through* the framework rather than understanding the contract on its own terms. Provisions outside the 12 categories are underweighted or missed. This is the heaviest contamination in the original prompt and the primary motivation for the pipeline.

2. **Evaluation + Generation** — evaluative posture constrains redline drafting. The model generates "standard market position" language because the evaluative frame is still active. Redlines should be shaped by the deal's specific dynamics (relationship, strategic importance, commercial context), not by the classification that preceded them.

3. **Accumulated context + Synthesis** — by the time the model reaches negotiation strategy (Step 7 in the original), it's reasoning through a slurry of investigation residue, evaluation classifications, generated redline language, and output template structure. The strategy section tends to restate the tier classifications rather than engage in genuine strategic reasoning about the deal.

Each split addresses a specific, identified interference — not architectural purity. I considered whether any agents could be combined:

- **Reader + Comparator**: No. This is the core toxic pair.
- **Comparator + Redline Writer**: Possible with a scope boundary, but the evaluative posture measurably constrains generation toward boilerplate. Worth separating.
- **Redline Writer + Strategic Advisor**: These are both somewhat divergent, but they're different *types* of divergent work — precision clause drafting vs. whole-deal strategic reasoning. The drafting posture (clause-level focus, legal precision) would anchor strategy to a clause-by-clause perspective.

Four agents is the minimum that avoids interference. Not three, not five.

### Why sequential, not parallel

The Redline Writer and Strategic Advisor could theoretically run in parallel since both consume the deviation list. But the Strategic Advisor produces better strategy when it knows what redlines are being proposed — the specific asks shape sequencing advice, trade-off recommendations, and package deal suggestions. The linear dependency is real, not just cautious design.

### Key design choices

**Lenses in the Contract Reader, seeds in the Comparator.** The original prompt's detailed clause guidance (Key elements, Common issues) were seeds applied to investigation — content prescription constraining divergent work. In the pipeline, the Contract Reader uses lenses ("how does risk flow?", "what's unusual?", "what's absent?") and the Comparator uses the playbook's structure as legitimate convergent classification aids. Seeds moved to where they belong.

**"Common issues" lists removed entirely.** The original had ~25 named issues across six clause categories ("Cap set at a fraction of fees paid", "Asymmetric carveouts favoring the drafter", etc.). These told the model what to find. In the pipeline, the Comparator evaluates against the playbook's *positions* (what the organization wants), not against a list of known problems. If the playbook says "liability cap at 12 months of fees", the Comparator can identify a 3-month cap as a deviation without being told that short caps are a "common issue."

**Business context routes around the pipeline.** The user's deal context (relationship, deadline, strategic importance, focus areas) goes directly to Agents 3 and 4, not through investigation or evaluation. This prevents investigation bias (surfacing only what the user is worried about) while ensuring the generative and strategic agents have the context they need.

**"Provisions Outside Playbook Categories" in the Comparator.** The Contract Reader, freed from the 12-category table, may surface unusual provisions that don't map to any playbook category. Without an explicit section for these, the Comparator would silently drop them — evaluation naturally ignores what it can't classify. The dedicated section preserves investigation breadth through the convergent stage.

**All numeric anchors removed.** "Top 3-5 issues" → removed. "Top 3 issues" → removed. Example counts per classification tier → removed. The 12-row category table as a minimum coverage requirement → removed from investigation (the Reader follows the contract), retained implicitly in the Comparator (the playbook defines its own categories). Output counts should respond to the contract's complexity, not to the prompt's suggestions.

**Output formats are responsive, not rigid.** Each agent's format has suggested sections but explicitly says to spend depth proportional to substance/severity/complexity. No uniform template forces a critical IP issue and a trivially acceptable governing law clause into the same structural weight.

### What this tests

The experiment's hypothesis: good output hides great output. The monolithic prompt produces competent, useful contract reviews. The question is whether separated contexts produce qualitatively different output in specific, measurable ways:

- **Investigation breadth**: Does the Contract Reader surface provisions outside the standard categories that the monolithic version misses?
- **Redline creativity**: Are redlines shaped by deal dynamics rather than defaulting to standard market position boilerplate?
- **Strategic depth**: Does the Strategic Advisor model the counterparty and reason about leverage, or does it restate the deviation classifications?
- **Natural variation**: Do output volumes vary with contract complexity, or does anchoring produce uniform counts?

If Tier 2 (the optimised single prompt) improves incrementally and Tier 3 (this pipeline) produces a qualitative leap, the finding supports the core thesis: the monolithic prompt is the ceiling, not the floor.

### Trade-offs

**Added complexity.** Four agents with handoffs are more complex to run than a single prompt. For a one-off contract review, the overhead may not be worth it. For a production legal workflow running repeatedly across many contracts, the pipeline is likely worthwhile.

**Wall-clock time.** Sequential execution means ~4x the latency. Each agent runs faster (smaller context, focused task), but the total is still longer than one pass. This is a real cost for interactive use.

**Orchestration.** Someone (or something) needs to manage the handoffs — extract the right output from each agent, pass it to the next with the right additional context. In a production system, this would be automated. For the experiment, it's manual.

These are the right trade-offs for a Tier 3 reconstruction. The question isn't whether the pipeline is simpler — it's whether it produces meaningfully better output.
