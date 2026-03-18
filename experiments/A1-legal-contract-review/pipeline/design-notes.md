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

---

## Theoretical Grounding

### RPD mechanism: why the Contract Reader is the critical stage

Contract review is an investigation-required task — the model cannot produce the correct analysis without deeply engaging with the specific contract. No two contracts are identical; clause interactions, unusual provisions, and structural features of the risk allocation are discoverable only through situated engagement with the particular document.

Klein's Recognition-Primed Decision (RPD) model explains the specific mechanism by which evaluation criteria degrade this investigation. Klein identifies three variations:
- **Variation 1**: Familiar situation — expert recognises it, applies known response. No deliberate analysis needed.
- **Variation 2/3**: Novel situation or complications — requires deliberate situation modeling before action.

Contract review is a Variation 2/3 task. Each contract is a novel situation with its own commercial logic, clause interactions, and structural features. The expert reader doesn't pattern-match against known clause types — they model the situation first: what is this deal trying to accomplish? How do the parties' interests interact? How does risk flow? Only once that mental model is built does pattern-recognition add value.

When evaluation criteria are in context during this investigation phase, they switch the decision architecture from recognition-primed to criterion-referenced. The model shifts from "what patterns do I see?" to "which of these criteria are met?" — investigation becomes subordinate to the evaluation framework. This is not simple overload; it is a qualitative change in how the investigation proceeds. Criterion-referenced analysis produces competent-looking results (every criterion checked, every finding mapped to a category) while suppressing the recognition-primed discoveries that make contract review genuinely valuable: the unusual provision that doesn't fit any category, the clause interaction that changes what the contract actually delivers, the structural feature of the risk allocation that only emerges from reading the contract as a whole.

The Contract Reader agent IS the deliberate situation modeling step. Its clean context — free from playbook criteria, evaluation categories, and business context about what the user is worried about — enables recognition-primed investigation to proceed unimpeded. This is the design feature that produces Tier 3's qualitative improvement over Tier 2.

### Knowledge-transformation in the Contract Reader

The Contract Reader is framed as a knowledge-transformation task (Bereiter & Scardamalia), not a knowledge-telling task.

Knowledge-telling retrieves and organises existing knowledge — produces a catalogue of what the contract contains. Knowledge-transformation generates new understanding by working through the problem — produces a mental model of what the contract means, how it works, what it implies.

The distinction matters for output quality. A knowledge-telling output enumerates clause contents. A knowledge-transformation output characterises the deal's commercial logic, identifies where the parties' interests create tensions, and surfaces the structural features of the risk allocation that aren't visible at the clause level. This is richer material for the Comparator to evaluate against — and the "Unusual or Non-Standard Provisions" section of the Reader's output is precisely where knowledge-transformation discoveries land.

The "Deal's Commercial Logic" section in the Reader's output template is the explicit prompt for knowledge-transformation: write a description of what the contract is trying to accomplish, not a summary of what you found. This framing pushes toward the generative understanding that produces better handoff material for all subsequent stages.

### Epistemic stance as independent variable

Each pipeline agent carries an explicit epistemic stance appropriate for its cognitive mode. This is not decorative framing — per the cognitive stack, epistemic stance is the highest-leverage intervention point. It cascades through intent, posture, cognitive mode, register, language patterns, and tokens simultaneously.

The four stances in this pipeline:

**Contract Reader — investigative-exploratory**: "You are discovering what's here." Sets epistemic aim of exploration over closure. Activates thoroughness, tolerance for ambiguity, willingness to follow threads. Suppresses premature certainty and framework-first thinking. This stance, combined with clean context (no evaluation criteria), produces the full benefit of Tier 3 for the investigation stage.

**Playbook Comparator — convergent-evaluative**: "You have stable reference points and you are applying them systematically." Sets epistemic aim of measurement against criteria. Activates precision, systematic coverage, correct classification. Prevents drift into investigative mode. The Comparator should measure, not continue exploring.

**Redline Writer — generative-exploratory**: "Each redline is a drafting challenge, not a compliance exercise." Sets epistemic aim of solving a drafting problem shaped by deal dynamics. Activates creativity, commercial calibration, contextual reasoning. Prevents defaulting to boilerplate "standard market position" language — the failure mode when evaluative posture bleeds into generation.

**Strategic Advisor — strategic-synthetic**: "You are reframing, not continuing." Explicit epistemic shift from the prior stages. Sets epistemic aim of whole-deal strategic reasoning over clause-level analysis. Activates counterparty modeling, leverage identification, sequencing reasoning. Prevents the failure mode of restating classification tiers in strategy-flavoured language.

Epistemic stance works independently of context isolation — Tier 2 benefits from stance even within a monolithic prompt. But Tier 3 gets both: the stance shapes how each agent approaches its task, and the clean context removes the contamination that would persist despite the stance. The combination is the source of Tier 3's qualitative improvement.

### Proactive interference: why clean context matters

The 2025 paper "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length" found that LLM retrieval accuracy declines log-linearly as interference from earlier context accumulates — and that natural language prompts for "strategic forgetting" yield only marginal improvements. This is a fundamental working-memory limitation, not a prompting problem.

This maps directly to the growing-middle problem in the monolithic prompt. By Step 7 of the original prompt, the context carries accumulated residue from investigation (reading notes, clause summaries), evaluation (classifications, risk descriptions), and generation (redline language, rationale). The Strategic Advisor is reasoning through this slurry. Earlier content is not just occupying space — it is actively interfering with the processing of the strategic reasoning task. The degradation compounds: each stage is impaired by all prior stages' cognitive residue.

Pipeline isolation solves proactive interference structurally. Each agent gets a fresh context window — the Strategic Advisor's context contains only the deviation list, the redline proposals, and the business context. The accumulated residue of investigation, evaluation, and clause drafting is absent. Scope boundaries within the monolithic prompt cannot achieve this: the cognitive residue persists at a distributional level regardless of instructions to ignore it.

This is why proactive interference is the specific mechanism that makes Tier 3 valuable beyond what Tier 2 can achieve. Epistemic stance addresses attentional residue (the framing contamination from evaluation criteria during investigation). Proactive interference cannot be addressed within a single context at all — it requires architectural separation.

### Kahneman-Klein boundary: when pattern-matching is appropriate

The Kahneman-Klein framework (2009) specifies the conditions under which expert intuition (pattern-matching) is valid: stable regularities in the environment AND adequate opportunity to learn those regularities. When these conditions hold, recognition-primed decision-making is efficient and accurate. When they don't, deliberate analysis is required.

The pipeline design deliberately maps its stages to this boundary:

**Contract Reader**: Unstable regularities — each contract is novel. Pattern-matching against known clause types would produce criterion-referenced analysis. Deliberate situation modeling is required. This is why the Reader runs in clean context with investigative epistemic stance.

**Playbook Comparator**: Stable regularities — the playbook defines the standard positions, and clause types (liability, indemnification, IP, etc.) are well-established categories. Pattern-matching against the playbook is appropriate and efficient. This is why the Comparator uses convergent-evaluative stance and the playbook's structure as legitimate seeding.

**Redline Writer**: Partially stable regularities — standard legal language patterns exist, but the appropriate draft depends on the specific deal dynamics. The Writer uses learned language patterns but shapes them to the novel context.

**Strategic Advisor**: Novel situation — negotiation strategy is inherently situational. The Advisor can draw on learned patterns (counterparty modeling, leverage analysis) but must apply them to the specific deal's commercial logic and dynamics.

The pipeline's sequencing respects this boundary. Deliberate analysis (Reader) precedes pattern-matching (Comparator), which precedes contextually calibrated generation (Writer), which precedes strategic synthesis (Advisor). Each stage gets the cognitive mode that matches its epistemological requirements.

---

### What this tests

The experiment's hypothesis: good output hides great output. The monolithic prompt produces competent, useful contract reviews. The question is whether separated contexts produce qualitatively different output in specific, measurable ways:

- **Investigation breadth**: Does the Contract Reader surface provisions outside the standard categories that the monolithic version misses? Does knowledge-transformation produce richer handoff material than knowledge-telling?
- **Redline creativity**: Are redlines shaped by deal dynamics rather than defaulting to standard market position boilerplate?
- **Strategic depth**: Does the Strategic Advisor model the counterparty and reason about leverage, or does it restate the deviation classifications?
- **Natural variation**: Do output volumes vary with contract complexity, or does anchoring produce uniform counts?

If Tier 2 (the optimised single prompt) improves incrementally and Tier 3 (this pipeline) produces a qualitative leap, the finding supports the core thesis: the monolithic prompt is the ceiling, not the floor.

### Trade-offs

**Added complexity.** Four agents with handoffs are more complex to run than a single prompt. For a one-off contract review, the overhead may not be worth it. For a production legal workflow running repeatedly across many contracts, the pipeline is likely worthwhile.

**Wall-clock time.** Sequential execution means ~4x the latency. Each agent runs faster (smaller context, focused task), but the total is still longer than one pass. This is a real cost for interactive use.

**Orchestration.** Someone (or something) needs to manage the handoffs — extract the right output from each agent, pass it to the next with the right additional context. In a production system, this would be automated. For the experiment, it's manual.

These are the right trade-offs for a Tier 3 reconstruction. The question isn't whether the pipeline is simpler — it's whether it produces meaningfully better output.
