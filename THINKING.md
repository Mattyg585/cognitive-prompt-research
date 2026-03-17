# Thinking Out Loud

*A working document for threads that aren't resolved yet. Not conclusions — the stuff between conclusions.*

Last updated: 17 March 2026

---

## Where we are (the honest version)

I had a theory about cognition and AI — that language carries cognitive mode, and managing it deliberately improves output. The theory holds. But its application is more interesting than I expected.

**The lightweight intervention (cognitive hygiene) appears universal.** Setting the epistemic stance — "explore the landscape before reaching conclusions" — improves output on every complex task we've tested, across every model. It's one sentence in a system prompt. No architectural change. No risk of making things worse.

**The heavyweight intervention (pipeline separation) is an amplifier.** When the conditions are right (strong model, novel data to investigate, genuine discovery needed), it turns good output into qualitatively different output — the kind that changes how you think about the problem. When the conditions are wrong (knowledge-based reasoning, weaker models, over-engineered handoffs), it can be catastrophic — information loss, wrong artifacts, introduced bias.

The theory is validated. The lightweight application is ready to share. The heavyweight application has fuzzy edges I can't yet pin down. There's something here but I need help teasing it out.

---

## What we know (solid ground)

**The cognitive stack is real and useful.** Intervening at the epistemic stance level ("explore before concluding") cascades through everything below. 0.76 to 0.95 on expert-scored benchmarks from a single system prompt. This works across models, across domains, and costs nothing architecturally. If you take one thing from this research, this is it.

**Convergent work is resilient to mode contamination.** Coding benchmarks (SWE-bench) — baseline passed everything. Domain accuracy on PRBench — 1.0 across all tiers. When the task has a clear right answer and the model knows the domain, mode mixing doesn't hurt. The model compensates.

**The pipeline is powerful but specific.** CA policy pipeline: massive improvement. A-series on strong models: qualitative leaps. PRBench: overcooked. Cross-model: catastrophic failures on weaker models. The pipeline isn't a universal upgrade — it's a specific tool for specific conditions.

---

## What we think but can't yet prove

**The pipeline's value tracks with "adaptive expertise."** The pattern: pipeline helps when the model must investigate data it hasn't seen before and build novel understanding. Pipeline doesn't help when the model is reasoning from training knowledge (even complex reasoning). The CA pipeline is adaptive expertise — the model discovers naming families, team patterns, policy debt from real data. PRBench is routine expertise — the model organises what it already knows about HSR law.

**Nobody in AI is benchmarking adaptive expertise.** Every benchmark tests recall, accuracy, or convergent reasoning. Nobody tests "can you walk into something you've never seen and figure out what's going on?" PRBench, SWE-bench, MMLU, HELM — all routine expertise. The benchmarks that would validate the pipeline thesis don't exist yet.

**The cognitive framework is actually a design methodology.** Not just theory. CTA for stage boundaries. Cognitive stack for intervention level. Trust chain for handoff design. This tells you HOW to design AI systems for novel data, which is what everyone building agents is trying to figure out through engineering iteration.

---

## The threads I can't resolve yet

### What exactly is the pipeline's niche?

I keep circling this. "Data-intensive adaptive expertise" is the best label but it doesn't fully satisfy. The CA pipeline works because of: real data (50+ policies), genuine investigation (not recall), investigation + evaluation toxic pair on discovered information, repeated use (amortized design cost). PRBench fails because none of these apply. But where's the line? Is a lawyer reviewing ONE specific contract (A1) closer to CA or PRBench? A1 showed pipeline improvement, but the contract was a single document in one context — not 50 policies requiring chunking.

Maybe the line isn't data volume. Maybe it's about whether the model is DISCOVERING or RECALLING. A1 discovers things about a specific contract it hasn't seen. PRBench recalls things about HSR law it's already trained on. Even though A1 has one document and PRBench has a complex question, the cognitive demand is different.

### Why did the A-series pipeline work when PRBench didn't?

The A-series tasks HAD external data (a contract, interview transcripts, incident logs, debug output). PRBench didn't — it was pure knowledge-based reasoning. Maybe the pipeline's value isn't about data VOLUME but about whether there's external data AT ALL. Any external data creates genuine investigation. No external data means the model is organising recall, and Tier 2 is sufficient.

But the A-series pipelines were also v0.1 and evaluated by LLM judges. Would they have shown the same pattern against expert rubrics? Would Tier 2 have matched them on A-series with better epistemic stance prompting? We don't know because A-series Tier 2 prompts were designed before we understood that epistemic stance was the active ingredient.

### Is there a "Tier 2.5"?

The gap between Tier 2 (one prompt) and Tier 3 (full pipeline) is big. Is there something in between? Maybe: a single prompt with multiple phases that explicitly manages epistemic stance shifts within the response. Or: two stages instead of three. Or: a pipeline that passes full context (not compressed handoffs) between stages, getting clean epistemic stance at each stage without the information loss.

The B2 pipeline's failure mode was information loss in handoffs. The Tier 2 prompt's success was holding everything in one context with an epistemic stance reset. A Tier 2.5 might be: separate sessions (clean context) but without aggressive schema compression. Each stage gets the full prior output, not a compressed handoff. You get mode separation without information loss. But then you lose the "schema strips cognitive residue" benefit. Trade-offs all the way down.

### What's the thing my brother is building?

He's working on AI that handles code it hasn't seen before. That's the same problem. The model has domain expertise (knows how to code) but must investigate unfamiliar data (a new codebase) and figure out what's going on. That's adaptive expertise. The cognitive pipeline methodology would predict: the model needs to investigate without evaluating, build understanding before committing to changes, and separate the "what's here" question from the "what should I do about it" question. Which is... kind of what good coding agents already do (explore → plan → implement → verify). But they do it through engineering intuition, not through CTA-derived cognitive mode boundaries.

### Is "adaptive expertise" even the right frame?

When I try to explain this to someone who isn't in my head, "adaptive expertise" doesn't land. It's too academic. The thing I'm trying to point at is more like: the ability to figure out something you haven't seen before. A troubleshooter. A consultant. A detective. Someone who holds uncertainty while they investigate and resists the urge to pattern-match to something familiar.

Maybe the frame is simpler than I'm making it. Maybe it's just: **AI is great at answering questions but struggles with investigating situations.** Questions have answers. Situations have patterns that must be discovered. The pipeline protects the discovery process. The epistemic stance gives the model permission to discover. Both serve the same thing — helping the model investigate rather than just answer.

### Why does nobody benchmark this?

Because it's hard to measure. "Did you find the right answer?" is easy to score. "Did you discover the interesting pattern in this unfamiliar data?" requires domain experts who can assess whether the pattern is genuine and valuable. PRBench's rubric gets close (it has "Supplemental Insight" and "Handling Uncertainty" categories) but it tests knowledge-based reasoning, not investigation of novel data.

To benchmark adaptive expertise, you'd need to: provide real, novel data that the model can't have trained on. Ask it to investigate. Have domain experts evaluate whether the investigation surfaced genuine, valuable patterns. That's expensive, slow, and domain-specific. Nobody funds it because it doesn't produce leaderboard numbers.

---

## What I'm considering doing next

- **Run Tier 2 on more PRBench tasks** to confirm the improvement isn't a fluke (statistical power)
- **Re-run A-series with the improved Tier 2 prompt** (epistemic stance framing) to see if Tier 2 would have matched Tier 3 on the original experiments
- **Design an adaptive expertise test** — real data, genuine investigation, expert evaluation. Maybe in the CA policy domain where I already have the expertise to evaluate.
- **Try a "Tier 2.5"** — two sessions with full context passing (not compressed handoffs) to test whether clean epistemic stance at each stage captures pipeline benefits without information loss
- **Write up the cognitive hygiene finding** as something immediately shareable — "one prompt intervention that improves professional reasoning by 25%" is a strong standalone finding
- **Keep thinking about what I can't name yet** — the pipeline niche, adaptive expertise, the thing about discovering vs recalling. There's something here that I haven't articulated and I think it matters.

---

## The sentence I keep coming back to

> The AI field is optimising for routine expertise while the highest-value professional work requires adaptive expertise. The cognitive pipeline methodology enables adaptive expertise — but nobody has the benchmarks to prove it because nobody is measuring it.

I don't know if this is right. But it feels like it's pointing at something.
