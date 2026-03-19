# What Does Cognitive Science Say About Prompt Engineering?

*AI Reasoning Engine — Part 5 of 5*

1. [I Built an AI Tool That Does My Job Better Than Me](https://thegrahams.au/blog/what-i-learned-building-ai-tools-that-actually-think/)
2. [Why Good Prompting Wasn't Enough](https://thegrahams.au/blog/why-good-prompting-wasnt-enough/)
3. [Context Carries Cognitive Mode](https://thegrahams.au/blog/context-carries-cognitive-mode/)
4. [Evidence & Methods](https://thegrahams.au/blog/the-evidence-for-thinking-in-modes-evidence/)
5. What Does Cognitive Science Say About Prompt Engineering?

---

Everyone knows the basics of context management by now. Keep chat sessions short and focused. Reset often. Split complex work into multi-stage workflows. We know this works.

But I wanted to know *why*. Can we predict when we should split and when splitting will make things worse? And more importantly — would you even notice the difference?

That's the part that got me. In my experience, getting this wrong still produces good output. Competent, thorough, professional. Nobody would complain. But getting it right — that's where you see what was being left on the table. That's where good turns to great. And the gap is invisible until you fix the prompt and compare the output to what you had before.

I stumbled onto a theory that cognitive science should have something to say here. Not because LLMs think — they don't — but because they learned from human language, and human language carries cognition. Every word of training data was produced by a human in some cognitive state. Exploratory writing looks statistically different from evaluative writing — different hedging, different sentence structures, different levels of commitment. The model learned those distributions. It doesn't know what exploration *is*, but it knows what exploratory language looks like, because that's all it has.

Cognitive science has spent decades studying how thinking gets encoded in language. If that encoding is what LLMs learned from, then cognitive science isn't a metaphor for what's happening in the model. It's a description of the *training signal*. And it should be able to predict which context splits help (because you're separating incompatible cognitive modes) and which ones hurt (because you're adding scaffolding to a model that already knows the domain) — *before you run anything*.

Every time I leaned into this, the needle moved. Every time things broke, cognitive science explained why. I saw just how bad "good" output was when I understood what my cognitively confused prompts were actually doing.

I'm a cloud infrastructure consultant with seventeen years of Microsoft experience and no formal background in AI or cognitive science. I'm not the person you'd expect to be writing this. But I spent seven months building an AI pipeline that forced me to confront this question, and the answers kept coming. This post is about what happened when I took that seriously and tested it against production prompts across six domains. The [full research repo](https://github.com/Mattyg585/cognitive-prompt-research) is public if you want to evaluate the evidence yourself. What follows is the story.

---

## The question, applied

The previous posts in this series documented seven months of building a Conditional Access policy analysis pipeline. The key finding was that separating different types of thinking into their own contexts — convergent work (compressing, verifying, pinning things down) in one agent, divergent work (exploring, synthesising, following threads) in another — produced measurably deeper output than combining them. Not because of token limits. The context window was 70% empty. The combined prompt was suppressing capability the model already had.

That finding came from one practitioner, one project, one domain. The question that launched the research repo was: does it generalise?

But I didn't just re-run the same experiment in different domains. I went back to cognitive science and asked: if this theory is right — if the language patterns in the context window are pulling the model's generation toward compatible patterns — what does the research say about how to design prompts? What kinds of interference should I look for? What does "cognitive hygiene" actually mean at the level of prompt construction?

The answers were specific. Cognitive science says that numeric anchors (like "identify 3-5 key findings") create anchoring bias — the model will find the number you gave it, not the number that's there. It says that seeded examples function as availability heuristics — they make the model more likely to find things that look like the examples and less likely to find things that don't. It says that mixing evaluative language with investigative language creates something analogous to task-set inertia — the model gets pulled toward one mode and stays there.

These aren't vague principles. They're specific, testable predictions about what you'll find wrong with a given prompt and what will happen when you fix it. So I built agents that look for exactly these patterns.

One thing to flag before the experiments: the Tier 2 results — where a single, better-written prompt dramatically improved output without any separation at all — are the strongest evidence that context isolation isn't the mechanism. You don't need to split anything. You need to fix the cognitive mode of the language that's already there. Sometimes that means splitting. Sometimes it means rewriting. Sometimes it means removing a section entirely. The framework tells you which.

---

## Building tools from cognitive science, not from guessing

This is the part I want to be clear about, because it matters for how you evaluate everything that follows.

I didn't write a bunch of prompts, run experiments, then go find cognitive science frameworks that matched my results. The sequence was the other way around. I started with cognitive science. I built analysis and writing agents grounded in those principles — agents that look for mode interference, anchoring bias, seed contamination, register mismatches. Then I pointed those agents at production prompts and let them do the analysis and the rewriting.

The prompts that went into the experiments were written by agents built on cognitive science principles. The experiment itself was a test of whether grounding prompt design in cognitive science produces better output than not doing so. The agents *are* the methodology.

I took six production prompts from [Anthropic's knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) — same authorship, same quality bar, different domains: legal contract review, marketing content, HR performance reviews, design research synthesis, engineering debugging, and SecOps incident response. Same model quality, different contexts. Good prompts, not straw men.

For each, I ran three tiers:

**Tier 1 (Baseline):** The original prompt, untouched.

**Tier 2 (Optimised):** Same structure, but with cognitive science fixes applied. Remove numeric anchors. Replace seeded examples with analytical lenses. Add scope boundaries between thinking modes. The prompt-writer agent did this — I didn't hand-tune them.

**Tier 3 (Pipeline):** Split into multiple agents, each doing one type of thinking in a clean context, with structured handoffs between stages. Investigation in one agent, evaluation in another, synthesis in a third. The prompt-architect agent designed these decompositions.

The prediction: if cognitive science has explanatory power over prompt design, Tier 2 should improve incrementally (confirming that the interference patterns exist and can be partially fixed) and Tier 3 should produce a qualitative leap (confirming that full separation unlocks capabilities the single prompt suppresses).

---

## It kept working

Each experiment needed test material — you can't review a contract without a contract. For legal, I used a real, open-source SaaS agreement (the Common Paper Cloud Service Agreement v2.1, CC BY 4.0) — I didn't plant anything in it for the pipeline to find. For the other five domains, I created realistic synthetic scenarios: a fictional product launch brief for marketing, a senior engineer's performance data for HR, six user interview transcripts for design research, a production Lambda failure with logs for engineering, and a SEV1 customer data exposure timeline for SecOps. Then the three tiers of each prompt ran against the same test material, and the outputs went through a scoring rubric designed to measure the kind of qualitative differences the theory predicted — not just "is this correct?" but "does this demonstrate investigation or just retrieval?"

Pipeline won five of six domains on Claude cleanly. Creative writing — the sixth — was more complicated, and it turned out to be one of the most interesting results. I'll come back to it.

But the scores aren't the interesting part. The scores say "this one is better." The *outputs* say something different — they show a qualitative shift in what the model produces when given clean cognitive space.

Take the legal contract review. The knowledge-work-plugins prompt tells the model to review a contract against a playbook — it's a well-structured prompt that mixes investigation (reading the contract), evaluation (comparing against standards), and generation (writing the review) in a single context. The baseline output listed clause deviations. The pipeline version identified compound interactions between clauses — how an ML training clause, a survival clause, and a data export restriction combine into a single structural risk. It scripted the negotiation move-by-move. It predicted what the counterparty's responses would reveal about their organisation. Two independent models, given randomised outputs with no project context, both called it the same way. One of them described the difference as treating the contract "as a deal, not a document."

The design research baseline catalogued interview themes. The pipeline version surfaced compound insights that no single interview contained — "workarounds are specifications written in behaviour" and "partial adoption produces negative value, not partial value." Both external evaluators independently said the pipeline output would change how they make decisions. The baseline was "template faithfully executed."

The SecOps baseline produced a standard postmortem with a mechanical root cause analysis. The pipeline version reframed: "confidence accumulates across checkpoints without coverage expanding" and "multiple overlapping checks can produce less safety than one well-scoped check." Organisational learning versus compliance document.

Every baseline was competent. Nobody reading any of them in isolation would say they were bad. The gap only appeared when you ran both and compared. Good output hides great output.

I also ran the same experiments across four additional models — GPT-5.2, GPT-5.3-Codex, GPT-5.2-Codex, and Gemini 3 Pro. GPT-5.3-Codex mirrored Claude: pipeline won six of six. The others were more mixed, and some produced catastrophic failures — wrong artifact types, introduced gender bias, missing critical compliance findings. The pipeline is an amplifier, not a guarantee. On models that handle structured handoffs well, it produces genuine leaps. On models that don't, it makes things worse than the baseline.

But Tier 2 — the prompt-level cognitive science fixes — helped across every model tested without producing a single failure. That's the universally safe intervention. The agents that wrote those fixes were built on cognitive science principles, and the improvements held everywhere.

---

## Then it failed

I wanted to test against something where the scoring rubric wasn't mine.

[PRBench](https://github.com/prbench/prbench) is a benchmark built by 182 domain experts — JDs, CFAs, practitioners. They wrote the tasks. They wrote the scoring rubrics. I had no input into what "good" meant. This was the test that would tell me whether my framework was finding real patterns or whether I'd built a system that was good at confirming itself.

The hard task — a complex regulatory analysis — went through the same three tiers. Baseline scored 0.76. Tier 2 scored 0.95. That's a massive jump from a prompt rewrite that took seconds — the architect agent analysed it, the writer agent revised it, done. Rubric I didn't design, scoring I didn't influence.

Then the pipeline scored 0.85.

Pipeline lost to Tier 2. Not by a little — it was clearly, unambiguously worse.

At 4:17pm on March 17th, I committed the results with the message "pipeline overcooked." Over the next hour, I wrote a working document full of open threads — "I keep circling this", "What exactly is the pipeline's niche?", "I don't know if this is right. But it feels like it's pointing at something." The thesis prediction had failed and I didn't understand why.

---

## Going back to the well

Just over two hours later — around 7:30pm the same evening — I did the thing that had worked every other time the project hit a wall. I went back to cognitive science.

I spun up a sub-agent session — domain expert personas in cognitive science — and laid out the failure. Here's what happened: Tier 2 dramatically improved a task where the pipeline made things worse. The pipeline has been winning everywhere else. Why did it fail here, and what does cognitive science say about when structured decomposition hurts rather than helps?

The answer came back fast. Not one framework — seven, converging independently on the same boundary condition.

**Klein's Recognition-Primed Decision Making:** Experts on familiar territory don't methodically compare options. They pattern-match. The PRBench task was familiar territory — HSR regulatory law is well-represented in training data. The pipeline interrupted fluid expert performance by forcing the model through unnecessary decomposition. It pushed the model *down* the Dreyfus skill ladder, from intuitive expert to deliberate proficient.

**Kahneman and Klein's boundary conditions for expert intuition (2009):** Expert intuition is valid when the environment has learnable regularities *and* the expert has had opportunity to learn them. For an LLM, training data is the learning opportunity. HSR law has stable, well-documented regularities. The model's pattern-matching was already valid. The pipeline added overhead without benefit.

**Kalyuga's Expertise Reversal Effect (2007):** Scaffolding that helps novices degrades expert performance. The pipeline was scaffolding. On this task, the model was already an expert.

**Bereiter and Scardamalia's knowledge-telling versus knowledge-transformation:** The monolithic prompt let the model knowledge-tell — retrieve and organise what it already knew. The pipeline forced knowledge-transformation — reconstruct understanding through each stage. But knowledge-telling is the right approach when the task *is* about applying known frameworks. Forcing transformation added cost without generating insight.

Three more frameworks pointed at the same thing. Seven independent lenses from different researchers, different decades, different sub-disciplines of cognitive science — all explaining why this specific failure was not just expected but *predicted* by the theory.

The explanation wasn't "the pipeline has limitations." It was "cognitive science tells you exactly when the pipeline will fail and why." The failure wasn't a crack in the framework. It was the framework working.

---

## The litmus test

The convergence produced something more useful than an explanation. It produced a decision tool.

**Could the correct analysis be produced without seeing the specific input data?**

If the answer is yes — if the model could produce a competent analysis from its training data alone, with the input mainly providing specific details to slot into a known framework — then you're in recognition-primed territory. The model is already an expert. Use Tier 2: fix the prompt-level interference, give it clean cognitive space, and get out of its way. The pipeline will slow it down.

Think: "Analyse this employment contract for compliance with Australian Fair Work Act requirements." The Fair Work Act is in the training data. The compliance framework is in the training data. The model knows what to look for — the specific contract just tells it *where* to look. That's recognition-primed.

If the answer is no — if the correct analysis requires the model to discover something from the input that it couldn't have known in advance, to follow threads across a specific document or dataset, to synthesise patterns that emerge from *this* data rather than from training — then you're in investigation-required territory. The model needs to think in stages. Use Tier 3: separate the modes, give each one a clean context, structure the handoffs.

Think: "Review this SaaS vendor agreement against our company's procurement playbook." The compound risk — an ML training clause interacting with a survival clause and a data export restriction to create a single structural trap — only exists in *that* contract. No amount of training data tells you it's there. The model has to read, investigate, and discover it. That's investigation-required.

This also explains why the A-series experiments worked. Every test scenario was built with realistic but novel data — a specific contract with specific clause interactions, specific user interviews with specific adoption patterns, a specific incident timeline with specific failure cascades. The answers lived in the input, not in the model's training. The pipeline gave the model the cognitive space to discover them.

The legal contract review (A1) was investigation-required. Pipeline won by a mile.

The PRBench regulatory analysis was recognition-primed. HSR compliance frameworks are well-documented. The model knew the domain. Tier 2 won.

The design research synthesis (A4) was investigation-required. The insight that "workarounds are specifications written in behaviour" only existed across those specific interviews. Pipeline won unanimously.

Every result in the study maps to this heuristic. I didn't design the experiments to test it — I designed them before the heuristic existed. The heuristic fell out of the failure, and then it retroactively explained everything.

---

## The creative writing boundary condition

Marketing content (A2) was where the pattern got more nuanced — and where the project nearly convinced me the pipeline had a hard limit.

On the first pass, pipeline won on scores (29 versus 24 versus 17). But when I iterated the prompts to V2, something broke. Tier 2 came *last*. The evaluator's verdict: "It doesn't do anything badly, which is its problem — it does everything competently and nothing memorably." The headline was called "genuinely bad" — a number was doing the work a real idea should do.

I went back to cognitive science. The diagnosis was specific: evaluation criteria don't need to be in a separate section to suppress voice. Their mere *presence* in the prompt — even if they say "ignore these for now" — activates pre-editing behaviour. The Tier 2 prompt had a three-phase structure (investigate → write → polish) within a single context, and the model could see the polish phase while writing, so it wrote safely. It pre-censored itself into competence.

That's mode contamination operating at micro scale, within a single prompt. The same mechanism as the V3→V4 result from the CA project, just subtler. The writer couldn't stop glancing at the rubric.

The fix was making the Tier 2 prompt lighter — less visible scaffolding. And the pipeline was redesigned from four stages to two (investigate-and-write → editor) to preserve voice continuity. The writer agent literally couldn't see the compliance criteria. V3 restored the expected pattern: Baseline (19) < Tier 2 (23) < Pipeline (28). The evaluator called the pipeline output "the only piece where the voice sounds like someone who had something to say before they sat down to write it." The closing line — "You'll notice what's missing. And what's missing is the point" — was called "the kind of ending that makes people share pieces."

But here's the honest picture: creative writing remains the most contested domain. A fresh blind evaluation ranked the Tier 2 version first — not on process, but on voice. The evaluator said it "reads like it was written by someone at the company who actually uses the product," while the pipeline version "feels like a very good content marketer wrote it." Better craft, slightly less authentic. The pipeline wins on editorial sophistication. Tier 2 wins on sounding like a human who had something to say.

For analytical work — legal, security, design research — the pipeline's advantages are unambiguous. For creative work, the tension between process quality and voice quality is real. The framework doesn't resolve it. It *predicts* it: pipeline separation operates at the cognitive mode layer, but creative voice lives at the register layer, and structured handoffs may disrupt the register-level flow that makes writing feel alive. Whether that trade-off is worth it depends on what you value in the output.

Not everything needs a pipeline. That's a feature of the framework, not a limitation.

---

## The pattern

Here's what I keep coming back to. Across two separate projects — seven months on the Conditional Access pipeline, then this research repo testing against six different domains — every time I hit a wall and didn't know why, I went back to cognitive science. Not to AI research. Not to prompt engineering guides. To cognitive science. And every time, it had an answer.

From the original CA project:

The CTA breakthrough: I was stuck on how to decompose policy analysis. Cognitive science said "interview yourself about how you actually do the work." I discovered I think in stories, not clusters. The output changed immediately.

The seeds crisis: I found planted data in my prompts and thought it unravelled everything. Cognitive science said "those are availability heuristics — they're anchoring the model's pattern-matching." That distinction — seeds versus lenses — became a core design principle.

The V3→V4 experiment: Removing a QA section made the output deeper. Cognitive science said "you mixed convergent and divergent processing — the convergent mode dominated." That became the central thesis.

From this research:

The PRBench failure: Pipeline lost to a simpler prompt. Cognitive science said "you scaffolded an expert — the Expertise Reversal Effect predicts exactly this." That became the litmus test.

The creative writing regression: Pipeline's Tier 2 prompt killed the voice in V2 — competent but forgettable. Cognitive science said "evaluation criteria visible to the writing phase activate pre-editing, even in a single context." Making the prompt lighter and the pipeline unable to see the rubric fixed it.

Two different projects. Different domains. Different time periods. Different types of problems. The same move — go back to cognitive science — kept producing answers that moved the needle.

The pattern isn't "I built a good pipeline." The pattern is: cognitive science is an explanatory and predictive lens for prompt engineering, because the training data is human language and human language carries cognition. The model doesn't need to be cognitive. It needs to have learned from cognition. Which it has, because that's all language is.

This could be an echo chamber. A system built on cognitive science finding that cognitive science explains what it sees. I've tried to control for that — cross-model testing, blind evaluation, the PRBench external benchmark — but the concern is legitimate. The strongest counter-evidence I have is the PRBench failure: a self-confirming system wouldn't predict its own failures, and the framework predicted this one after the fact in a way that generalised backward across every other result.

---

## What this means practically

If you design prompts, build agents, or create skills and plugins:

**Start with Tier 2.** Look at your prompts through a cognitive science lens. Are there numeric anchors telling the model how many things to find? Remove them. Are there seeded examples narrowing the model's pattern-matching? Replace them with analytical lenses. Is there evaluative language sharing context with investigative language? Add scope boundaries. The [prompt-architect agent](https://github.com/Mattyg585/cognitive-prompt-research/blob/main/QUICK-START.md) does this analysis automatically and the prompt-writer rewrites based on what it finds. This is the universally safe improvement — it helped across every model I tested.

**Use the litmus test for Tier 3.** Could the model produce a correct analysis without seeing the specific input? If yes, Tier 2 is probably enough. If no — if the answer lives in the data, not in the model's training — consider pipeline separation. But test it. Pipeline failures cascade, and on some models they cascade catastrophically.

**Watch for skills contamination.** When a base agent loads a skill, the skill's language enters the context. If the skill carries evaluative framing and the agent is doing investigative work, you've just created the same interference the pipeline is designed to prevent — except now it's non-deterministic, depending on which skills load in which session. This might explain why agents sometimes go off the rails on some runs but not others.

---

## What I'm not claiming

I'm not claiming LLMs have cognition. I'm not claiming this is a paper. I'm not claiming the experiments are rigorous by research standards — they're exploratory, single-researcher, heavily AI-assisted, with limited runs and LLM-as-judge evaluation.

What I am claiming is narrower: cognitive science appears to be an underexplored lens for prompt engineering, and every time I applied it, the needle moved. The framework made predictions that held across domains, across models, and across failures. The practical tools — the litmus test, the prompt-architect agent, the Tier 2 fixes — work today, on your prompts, regardless of whether the broader theory holds up.

The repo is public. The agents are ready to run. The experiments are reproducible. If this is wrong, it should be easy to show — point the architect at a prompt, run both versions, and see if the output changes. If it doesn't, I'm pattern-matching where there's nothing.

I think there's something here. I'm sharing it because the only way to find out is to let other people kick the tyres.

**[Full research repo →](https://github.com/Mattyg585/cognitive-prompt-research)**
**[Try the agents on your own prompts →](https://github.com/Mattyg585/cognitive-prompt-research/blob/main/QUICK-START.md)**

---

*Matt Graham is a cloud consultant on the Sunshine Coast, Australia. He has seventeen years of infrastructure experience, no formal AI or cognitive science background, and a side project that got out of hand. The research was conducted with Claude Code (Opus 4.6), with cross-model testing on GPT-5.2, GPT-5.3-Codex, GPT-5.2-Codex, and Gemini 3 Pro. External validation by Claude Web and Google Gemini. He can be reached on [LinkedIn](https://www.linkedin.com/in/matthewgrahamau/).*