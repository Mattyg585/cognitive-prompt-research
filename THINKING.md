# Thinking Out Loud

*A working document for threads that aren't resolved yet. Not conclusions — the stuff between conclusions.*

Last updated: 18 March 2026

---

## Where we are (the honest version)

The theory held. The agents work. The experiments confirmed the pattern across three iterations. And I'm clearer now about what this actually is — and where the edges are.

**Tier 2 (cognitive hygiene) is the universal win.** Setting epistemic stance, removing anchors, replacing seeds with lenses. Works on everything. Every model. Every domain. Zero risk. 0.76 to 0.95 on expert-scored benchmarks from a single system prompt. The agents that produce these fixes are now robust — three versions in, they handle both analytical and creative tasks correctly without over-engineering. This is ready.

**Tier 3 (pipeline separation) is specifically powerful.** Not universally. The boundary is sharper than it was:

> Can the correct output be produced without examining the specific input data?
> If yes — recognition-primed. Tier 2 is sufficient.
> If no — investigation-required. Tier 3 earns its cost.

A1 (contract review) is investigation-required: the model must discover clause interactions, compound risks, and counterparty leverage from a specific document it hasn't seen. The pipeline found the suspension compound risk, the data rights cascade, the post-termination ML model persistence — across three versions of the experiment, Tier 2 never found these. The gap didn't close.

B2 (PRBench/HSR law) is recognition-primed: the model is deploying legal knowledge it learned in training. The pipeline lost procedural details in handoffs. Tier 2 won.

A2 (marketing content) sits in the fuzzy middle: Tier 2 gets you 80% there (has a thesis, good structure), Tier 3 gets you voice (reads like someone who lived the problem, not someone who thought about it). Whether that last 20% is worth 2x the cost depends on what you're doing with the output.

**The agents are robust now.** Three iterations of the architect and writer, testing on both analytical (A1) and creative (A2) tasks. The v3 agents fixed the A2 Tier 2 regression — where v2 over-engineered the creative prompt with gates and declared phases that created anticipatory interference. The anti-pattern vocabulary ("criterion gates," "declared vs actual architecture") prevents the same mistake from recurring. The evaluator produces consistent blind scores across versions.

---

## What's resolved (threads that were open, now answered)

### "What exactly is the pipeline's niche?"

**Resolved.** The niche is investigation-required tasks. Multiple cognitive science frameworks converge on the same boundary:

- **Premature closure** (Croskerry, 2003, from diagnostic medicine): The single most common cognitive error — accepting a diagnosis before investigation is complete. The investigation-evaluation toxic pair IS premature closure. Medicine's intervention is the same as our pipeline: force a differential before committing. Stage 1 is a forced differential.

- **Recognition-Primed Decision** (Klein): Under monolithic prompting, the model does RPD — recognizes a pattern, activates the first plausible response template. For recognition-primed tasks, RPD is efficient and appropriate (why Tier 2 works on PRBench). For investigation-required tasks, RPD forces novel situations through familiar templates.

- **Epistemic vs pragmatic actions** (Kirsh & Maglio, 1994): Stage 1 is an "epistemic action" — it doesn't serve the client directly, it changes the computational state available to later stages. Like rotating Tetris pieces to see how they look. The pipeline "wastes" a pass on investigation, but it changes what later stages can see.

- **Expertise reversal effect** (Kalyuga, 2007): The B2 pipeline failure is literally this — scaffolding that helps novices degrades expert performance. The model was already expert at HSR law. The pipeline imposed investigative scaffolding on a task that didn't need investigation.

The reframe that works: **"Recognition-primed vs investigation-required tasks."** Adaptive expertise describes types of experts, not types of tasks. What we need is a task-level predictor. Does the task present patterns the model has already learned from training, or must new patterns be discovered from the input?

### "Why did the A-series pipeline work when PRBench didn't?"

**Resolved.** The A-series tasks had external data that required investigation. PRBench had knowledge-based questions that required recall. The pipeline's value is about whether there's genuine investigation to protect from premature closure — not about data volume, not about task complexity.

The v3 experiments confirmed this: even with a better Tier 2 prompt (three iterations of improvement), the pipeline still found things Tier 2 missed on A1. The investigation-evaluation separation is the critical boundary, and it can't be replicated within a single context.

### "Is 'adaptive expertise' even the right frame?"

**Partially resolved.** "Adaptive expertise" (Hatano & Inagaki) describes a real phenomenon but is academic language that doesn't land. The better frame for non-academic audiences is premature closure: "When AI must investigate something it has never seen before, mixing investigation with evaluation causes it to see only what it already knows how to classify. Separating them lets it discover what is actually there."

The litmus test is intuitive: **Could the correct analysis be produced without seeing the data?** If you could answer correctly from training alone, it's recognition-primed. If the answer lives in the specific data, it's investigation-required.

### "Would Tier 2 have matched Tier 3 on A-series with better prompting?"

**Answered by v3 experiments.** No. The v3 Tier 2 prompt was three iterations better than v1. On A1, it still missed the compound risks the pipeline found. The gap is architectural, not prompt-quality. On A2 (creative), Tier 2 got much closer to pipeline quality — confirming that creative tasks are genuinely a different category where the pipeline's advantage is about voice quality, not about discovering missing information.

---

## What's sharper (threads still open but better understood)

### The Tier 2.5 question

Still open, but the theory now predicts what will happen. If the investigation session receives no evaluative instructions, it's functionally Tier 3. If it gets a combined prompt with phases, it's Tier 2 with extra cost — the recognition-primed patterns still activate. The cognitive science is clear: premature closure operates at the level of what's in context, not at the level of explicit instructions. You can't instruction your way out of it; you need context isolation.

The 2-stage pipeline for A2 (creative agent + compliance editor) is effectively a Tier 2.5 that works — but it works because the two stages have genuinely different cognitive modes (creative generation vs editorial compliance), not because it's a lighter pipeline. The reduction from 4 stages to 2 stages didn't lose quality because the boundary that mattered (creation vs editing) was preserved.

### The agent iteration story

Three versions of the agents told us something important about creative vs analytical tasks:

**Analytical tasks respond to progressive refinement.** Each version of the A1 architect analysis and writer output improved incrementally. More precise diagnosis, cleaner separation, better lenses. v1→v2→v3, each measurably better.

**Creative tasks have an over-engineering trap.** The v2 A2 Tier 2 prompt regressed below v1 because the writer added criterion gates, declared phases, and prescribed parallel threads. These sounded good analytically but created anticipatory interference in creative work — the model could see the evaluation criteria while trying to write, so it wrote toward the criteria instead of toward the reader. v3 fixed this by going lighter: "Read the brief as a writer, not as someone filling a template."

The lesson: for creative tasks, the ceiling is reached by doing less, not more. The anti-pattern vocabulary we added to the agents ("criterion gates create anticipatory interference") is what prevented the same mistake in v3.

### The RAG implication

This emerged late and feels important. Standard RAG is a monolithic prompt: stuff retrieved chunks into context, ask the model to answer. The model does RPD on the retrieved data — recognizes patterns it already knows, activates familiar templates, produces a competent answer that looks like it engaged with the documents.

The premature closure dynamic is identical to what we saw in A1:

- **Standard RAG**: Retrieve → Generate. Investigation and evaluation in the same context. The model sees the chunks through the lens of what it already knows how to say.
- **Tier 2 RAG**: Same architecture, better epistemic stance. "Investigate these documents" instead of "answer from these documents." Cheap improvement, same ceiling.
- **Tier 3 RAG**: Separate investigation pass over retrieved chunks — what is actually in this data, what's surprising, what doesn't fit familiar patterns — before a second pass that synthesizes/answers. Forced differential before diagnosis.

The litmus test maps directly: **Is the answer already in the model's training, with RAG just providing citation support?** Standard RAG is fine. **Must the answer be discovered from the retrieved documents?** Standard RAG causes premature closure.

This matters because most production RAG is deployed on investigation-required tasks: legal discovery, medical records, financial filings, compliance review, codebase Q&A. The retrieved documents contain novel information. And every production RAG system just stuffs the chunks in and generates.

research-foundations.md already has a data stance section that covers the theoretical angle. What's new here is the direct connection: our A1 contract review IS a RAG task. The contract is the "retrieved document." The pipeline's findings that Tier 2 missed are exactly what you'd predict happens in production RAG over novel documents.

This is testable. Same three-tier design, applied to a RAG system over documents the model definitely hasn't memorized.

### Knowledge-telling vs knowledge-transformation

Bereiter & Scardamalia's framework (surfaced by the cognitive science research) sharpens something: monolithic prompts let the model knowledge-tell (dump training in order). Pipelines force knowledge-transformation (reconstruct understanding from prior stage output). Wasteful when telling is appropriate, valuable when transformation is needed.

This maps perfectly to the recognition-primed / investigation-required split. Knowledge-telling is recognition-primed. Knowledge-transformation is investigation-required. The pipeline forces transformation by giving each stage the output of the previous stage, not the original training distribution.

---

## What's still genuinely unresolved

### Where exactly does the fuzzy middle sit?

Creative tasks (A2) are clearly in the fuzzy middle. What other task types live here? I suspect: tasks where the model has partial knowledge — it knows the domain but not the specific situation. Consulting engagements, code review of unfamiliar codebases, organizational assessments. The model knows HOW to do the analysis but must discover WHAT to analyze from novel data. Is this investigation-required (pipeline) or recognition-primed with some novel data (Tier 2)?

The theory says investigation-required, but A2 showed that the pipeline's advantage can be about quality/voice rather than about missing findings. Maybe there's a spectrum: "how much of the answer lives in the data vs in the model's training?" The more answer-in-data, the more pipeline earns its cost.

### Does the RAG prediction hold empirically?

Strong theoretical case. No empirical test yet. This is probably the single most impactful next experiment — because RAG is deployed everywhere and if the premature closure dynamic applies, the implications are enormous.

The experiment design is straightforward: take a document the model hasn't seen. Ask analytical questions where the answer requires genuine investigation of the document. Compare standard RAG, Tier 2 RAG (epistemic stance), and Tier 3 RAG (investigation pass then synthesis). Score with domain experts.

### What's the minimal viable pipeline?

For investigation-required tasks, we've shown that 3 stages works as well as 4 (A1 v3 reduced from 4 to 3 without quality loss). For creative tasks, 2 stages works (A2 creative + editor). Is there a general principle? The theory suggests: the critical boundary is investigation/evaluation. Everything else is optimization. So the minimal viable pipeline is 2 stages: investigate, then evaluate-and-act. Additional stages are warranted only when the second stage would itself contain incompatible modes.

### The benchmark gap

Still true: nobody benchmarks investigation of novel data. The recent papers (2024-2026) are starting to bridge cognitive science and LLMs — "Cognitive Load Limits in LLMs" (2025), "Proactive Interference" (2025), a Nature Reviews Psychology piece on dual-process theory in LLMs. The field is converging on similar ideas from different directions. But the benchmarks don't exist yet.

---

## What I'm considering doing next

- **Test the RAG prediction.** Most impactful next experiment. Documents the model hasn't seen, analytical questions, three-tier comparison. If the premature closure dynamic applies to RAG, that's a finding with immediate practical implications for every production RAG system.
- **Run Tier 2 on more PRBench tasks** to confirm statistical power.
- **Design an investigation-required benchmark.** Novel data, genuine investigation, expert evaluation. Start in a domain where I can evaluate (CA policy, or my brother's codebase analysis space).
- **Write up the Tier 2 finding standalone.** "One prompt intervention that improves professional reasoning by 25%" is immediately shareable and doesn't depend on the pipeline story.
- **Let the pipeline niche percolate.** The premature closure frame is sharp. The RPD mapping is clean. The litmus test is intuitive. But I want to sit with it before committing — some things will spark new ideas, some will die off.

---

## The sentences I keep coming back to

> When AI must investigate something it has never seen before, mixing investigation with evaluation causes it to see only what it already knows how to classify. Separating them lets it discover what is actually there.

> Could the correct analysis be produced without seeing the data? If yes — Tier 2. If no — Tier 3.

> Good output hides great output. The gap is invisible until you split and compare.

> Most production RAG systems are leaving their most valuable findings on the table, and nobody knows because the output looks competent.
