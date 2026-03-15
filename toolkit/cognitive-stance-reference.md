# Context Carries Cognitive Mode

**What this is**: A set of principles for understanding how AI prompts shape thinking, how mixing incompatible types of thinking degrades output, and what to do about it.

**What this isn't**: A classification system. The labels and categories here are lenses for seeing patterns, not boxes to sort things into. They might be pointing at something real without naming it precisely. Use them when they're useful. Discard them when they're not.

**Origin**: These principles emerged from seven months of building production AI pipelines. Every pattern was discovered through iteration against real output and validated by comparing versions. The full evidence is documented in [Context Carries Cognitive Mode](https://grahams.au/blog/context-carries-cognitive-mode/) and its [evidence companion](https://grahams.au/blog/the-evidence-for-thinking-in-modes-evidence/).

**Why these principles work**: LLMs learned the language patterns that different types of human thinking produce. Exploratory writing has different statistical properties than evaluative writing — different sentence structures, hedging patterns, transition words, levels of commitment. When you put evaluative language in the context, you activate distributional patterns associated with evaluation. The model doesn't need to "have cognition" for this to work — it just needs to have learned that evaluative language predicts more evaluative language. The cognitive science (task-switching costs, proactive interference, cognitive load theory) explains why *humans* write differently in different modes. Those differences are what the model learned. See [Why This Works](#why-this-works-cognitive-science-foundations) for the research grounding.

---

## Six Principles

### 1. Context carries cognitive mode

The context window isn't just carrying information. It's carrying the *thinking style* of everything in it.

When the context contains exploratory, thread-following prose, it activates distributional patterns associated with exploration. When it contains criteria-referenced evaluation, it activates patterns associated with judging. The content and the language patterns travel together. You can't put convergent output into a context and expect the next step to generate divergent output — the convergent patterns are already shaping what comes next.

This applies at every scale:
- Within a single prompt (a QA section contaminates a synthesis section)
- Between prompt phases (output from step 1 shapes how step 2 thinks)
- In growing-middle architectures (accumulated output becomes a cognitive slurry)
- In sub-agent handoffs (what the parent passes down carries its mode)

### 2. Good output hides great output

Mode contamination doesn't produce bad results. It produces good results that prevent you from seeing what great results look like.

The V3/V4 experiment: a synthesis agent with a QA section was already producing genuinely strong output — published, customer-ready. Removing the QA section (making the prompt *smaller*) produced twelve findings instead of eight, four entirely new themes, zero losses, and a register shift from "competent audit" to "consultant who understands the humans on the other side of the table."

The mixed agent produced "Open with the naming families (builds trust, no judgment)." The separated agent produced "Open with what works well... Start here to establish credibility and avoid triggering defensiveness." Same model, same data. The capability was latent. The convergent context was suppressing it.

**Implication**: You cannot detect contamination by reading the output. V3 looked complete. The gap only appears when you split and compare. If you think your prompt is "good enough," it might be — or it might be good output hiding great output.

### 3. Lenses, not seeds

There's a difference between telling the model **what to find** and guiding **how to look**.

- **Seeds** (content prescription): "Look for these specific issues: missing MFA, weak passwords, orphaned accounts..." The model anchors to the seeds. It finds what you listed and stops.
- **Lenses** (structural guidance): "What's the gap between this policy's stated intent and its actual configuration?" The model investigates through the lens and finds what's actually there.

Seeds feel more helpful because they're more specific. But they constrain the output to what you already knew to look for. Lenses open the space for the model to find things you didn't anticipate.

In one experiment, replacing seeded themes with open lenses produced findings that matched expert review *plus* discoveries the seeded version missed entirely. The seeds had been written months earlier and forgotten — invisible anchors shaping every run.

**This connects to mode contamination**: content prescription pushes toward convergent work (pin things down, classify against known categories). Structural guidance keeps space open for divergent work (explore, follow threads, surface what's unexpected). Two types of instruction that sound similar but push in opposite directions.

**Important nuance**: seeds are not universally bad. In convergent work — classification, categorisation, framework mapping — seeding known categories is legitimate and effective. Seeding Zero Trust archetypes as starting categories for policy grouping works well because classification into known buckets IS convergent work. Seeds are harmful specifically when applied to divergent work, where they constrain exploration to what you already knew to look for.

### 4. Numbers become targets

Any specific number in a prompt becomes a psychological anchor. "Find 5-10 issues" produces 7-8 issues every time, regardless of what's actually there. A simple policy and a complex policy get the same count.

Removing all numeric guidance and using lenses instead: for the first time, a simple policy got two findings (because two was right) and a complex policy got seven. The output responded to the data instead of to the prompt's suggestion.

**Natural variation is a health signal.** If every run produces roughly the same number of outputs, something is anchoring. Healthy output varies 50-100% based on input complexity. Uniformity signals mechanical execution.

This applies beyond explicit numbers. Anything that implies a target quantity — examples with consistent counts, templates with fixed slots, output formats with specific numbers of sections — becomes an anchor.

### 5. Separate when they interfere, not by default

Not every prompt needs restructuring. Not every mixing of modes is harmful. The question isn't "is this pure?" but "is the mixing actually degrading the output?"

Some combinations work fine:
- Investigation with light structuring (lenses guiding exploration) — the structuring supports rather than constrains
- Evaluation followed by synthesis in the same context — "assess then commit" is natural
- Simple 2-3 step workflows where the middle accumulates some mode residue — mild contamination, not worth the overhead of separating

Some combinations reliably degrade output:
- Investigation mixed with evaluation — the model pre-filters, only finding things it can already classify
- Investigation mixed with generation — the model skips findings it can't fix, investigation becomes a funnel for recommendations
- Synthesis running alongside investigation — premature commitment to a narrative

When you do need to separate, use the lightest mechanism that works. A scope boundary in the prompt ("you are investigating, not assessing") is cheaper than splitting into sub-agents. Sub-agents with clean context are cheaper than adding a database. Match the intervention to the actual problem.

### 6. For interactive agents, let the human drive mode transitions

When a single agent must support multiple incompatible modes — investigation, evaluation, recording, generation — there are two ways to separate them:

- **Structural separation**: split into separate agents, each with a single mode (pipeline architecture)
- **Temporal separation**: keep one agent, but make mode transitions explicit and human-triggered

Temporal separation works when a human is present and driving the session. The consultant says "let's investigate this policy" (investigation mode). Later they say "draft the entry" (convergent recording mode). Later still, "generate the fix" (generation mode). The mode transitions happen at natural cognitive boundaries — when the human shifts intent — rather than at artificial prompt-prescribed boundaries.

This is preferable to structural separation for interactive work because:
- The human has context about *when* to switch that no prompt can prescribe
- The session maintains conversational continuity (shared context across modes)
- It avoids the overhead of orchestrating multiple agents for what is fundamentally a conversation

**The anti-pattern**: prescribing mode transitions as a numbered sequence. "Step 1: Define target state. Step 2: Read entries. Step 3: Verify policy. Step 4: Cross-reference..." Numbered steps create a mechanical execution posture — the model follows the sequence regardless of where the human's attention actually is. If the human wants to jump to step 4, the model resists or awkwardly redirects to step 1. The prescription conflicts with the responsive-partner posture the prompt otherwise establishes.

**The fix**: describe what a session typically touches (as a reference, not a workflow) and explicitly state that the human drives the sequence. "A typical story walkthrough touches these elements: [list]. The consultant decides the order based on what's interesting."

**When temporal separation fails**: when no human is present. An autonomous agent running a multi-mode workflow has no one to drive transitions. For autonomous execution, use structural separation (pipeline) or explicit mode-switching triggers in the prompt. Temporal separation via human control is only valid when a human is actually in the loop.

---

## Convergent and Divergent: A Useful Shorthand

These labels are imprecise. They may be pointing at something real without naming it precisely — possibly "scope control" is the deeper mechanism. But they're useful for seeing patterns.

**Convergent work** compresses, verifies, classifies, pins things down. It narrows. Quality gates, compliance checks, severity ratings, structured categorisation — these all pull toward convergence.

**Divergent work** explores, synthesises, follows threads, generates. It expands. Investigation, creative generation, narrative synthesis, empathetic reframing — these all require space to go somewhere unexpected.

When convergent and divergent work share a context, the convergent posture tends to dominate. This isn't always visible — the output looks complete, professional, correct. But the divergent potential is suppressed. The model doesn't follow threads it would have followed. It doesn't make the empathetic leap. It produces the competent version instead of the version that understands the humans on the other side.

The strongest evidence for this: removing convergent work from a divergent context made the output deeper, not shallower. The capability was always there. The context was suppressing it.

### Emergence and Divergence: The Chain

These are two distinct phenomena that work together:

**Emergence** is when properties become visible at a level above the components. "This environment was built three times by three different teams" is emergent — it's in the data (three naming families, overlapping objectives, different exclusion groups) but doesn't exist in any single policy. Emergence is closer to convergent work — it's compression that preserves relationships.

**Divergent generation** is what happens *on top of* emergence. "The customer team will feel defensive" isn't in any data. The agent inferred human intent from naming patterns and made a strategic communication decision. That's generative — producing something that didn't exist in the input or even in the relationships between inputs.

The chain: **convergent compression → preserves relationships → makes emergent patterns visible → divergent stage recognises those patterns AND generates novel framings that weren't in the data at any level.** Emergence is the precondition. Divergence is what you do with emergent patterns once they're visible.

This sharpens the contamination finding. When convergent and divergent work shared a context, the emergence was there (it found the naming families, the duplication). But the divergent generation was muted — "roughly half the policies duplicate baseline controls" is true and emergent, but not generative. Freed from convergent work, the agent took the same emergent patterns and went somewhere with them.

**Convergent compression is the precondition for good divergent work, not its opposite.** Separating them doesn't mean isolating them. It means sequencing them properly and not running them in the same cognitive pass.

---

## Types of Thinking (Reference, Not Classification)

When analysing a prompt, it helps to recognise which types of thinking are being asked for. These aren't rigid categories — they're lenses for seeing what's happening.

| Type | What it does | Feels like |
|------|-------------|-----------|
| **Investigation** | Surface what's there, follow threads | "What's interesting here? Where do the threads lead?" |
| **Structuring** | Group, categorise, map relationships | "How do these relate to each other?" |
| **Evaluation** | Judge against criteria | "How does this measure up against X?" |
| **Synthesis** | Compress into a working model, commit to narrative | "What does this all mean?" |
| **Reframing** | Translate between audiences or perspectives | "What does this mean for person/audience X?" |
| **Generation** | Produce new artifacts within constraints | "Create something that satisfies these requirements" |
| **Orchestration** | Decide what to do next, delegate, route | "What should happen now, and who should do it?" |

The convergent/divergent shorthand maps roughly: Investigation and Generation are divergent. Structuring, Evaluation, and Synthesis are convergent. Reframing can be either depending on whether it's compressing or expanding. Orchestration is meta — convergent about process, not content.

**The useful question isn't "which type is this line?"** It's: "is this prompt asking the model to think in two incompatible ways at the same time?"

---

## How Mode Contamination Actually Works

The mechanism isn't mysterious. When a prompt says "find issues AND assess their severity," the model doesn't do investigation and then evaluation. It does both simultaneously — which means it only investigates things it can already evaluate. The evaluation criteria become a pre-filter on investigation. Subtle, hard-to-classify patterns get dropped because they don't fit a severity bucket yet.

This shows up differently depending on what's mixing:

**Investigation + Evaluation**: Pre-filtering. The model finds what it can classify and stops. Subtle patterns that don't fit existing categories are dropped.

**Investigation + Generation**: Solution-shaped investigation. The model skips findings it can't fix. Investigation becomes a funnel for recommendations rather than understanding.

**Synthesis during Investigation**: Premature convergence. The model commits to a narrative based on early findings, then confirmation-biases the rest. Later findings get forced into the early narrative instead of reshaping it.

**Reframing before Evaluation**: Premature simplification. Executive framing infects technical assessment — things get compressed for an audience before they're fully understood.

**Orchestration + Investigation**: The coordinator goes down rabbit holes. It should be deciding what to do next, but it starts doing the work itself and loses the ability to see the whole picture.

But not all mixing is harmful:

**Investigation + Structuring**: Lenses guide investigation without constraining it. "Use these lenses: anomalies, gaps, conflicts" gives the model orientation while preserving space to find unexpected things.

**Evaluation + Synthesis**: Assess then commit is a natural progression. These can share a context productively.

**The principle**: if both types of thinking benefit from the same posture (both convergent, or light structuring over divergent), they can coexist. If they pull in opposite directions (one needs open exploration, the other needs pinning down), they interfere.

### Output structure carries mode too

It's not just the prompt that carries cognitive mode — the **output format** does too. Required database fields, template slots, structured sections — these all push toward convergent completion behaviour. "Fill in all the boxes" is a convergent posture regardless of what the boxes are about.

In one experiment, required schema fields (found/checked/assumed/not_checked) forced convergent behaviour in a divergent investigation agent. The agent filled fields because the schema demanded it, not because there was something to say. Making fields responsive rather than required (write what's relevant, skip what isn't) improved the investigation.

Templates with fixed slots, schemas with required fields, output formats with specific numbers of sections, examples that all have the same structure — these are implicit convergent anchors. For divergent work, make the output container lighter.

---

## Separation: Match the Mechanism to the Problem

When types of thinking interfere, give them separate contexts. The question is how much separation is actually needed.

### Scope boundaries within a prompt

The lightest intervention. Tell the model what it's NOT doing.

*"You are investigating, not assessing. Assessment is a separate phase. Surface patterns worth discussing — do not rate severity, do not recommend fixes."*

This works when the contamination risk is mild — when the types of thinking are adjacent (investigation with light structuring) or when one is clearly primary and you're just preventing bleed from a secondary concern. It's unreliable for fundamental mode conflicts because the previous section's output is still in context, carrying its cognitive style.

### Clean context (sub-agents or separate calls)

Give each type of thinking its own context window. The investigation agent explores freely. Its output is curated by an orchestrator before being passed to the evaluation agent, which gets a clean context with only structured findings.

This works for most toxic combinations. The key design decision is **what gets passed between agents** — that handoff IS the convergent gate. The orchestrator decides what information carries forward and what cognitive residue gets stripped.

**Watch the orchestrator**: if the orchestrator is purely routing (deciding what to do next based on status), it stays clean. If it's accumulating results and making content judgments, it becomes a cognitive mode accumulator itself. Sometimes this trade-off is fine — an orchestrator with mild mode accumulation is simpler than adding infrastructure. Sometimes it's not.

### Structured store between agents

Write output to a database, JSON schema, or any structured format. The next agent queries the store rather than reading the previous agent's prose. The schema strips cognitive mode by forcing information into a defined shape — a database row doesn't carry the exploratory tone of the investigation that produced it.

This is the heaviest mechanism and the most robust. It solves orchestrator accumulation because the orchestrator queries status from the store rather than holding everything in context. The schema IS the cognitive architecture — it determines what information crosses between phases and in what form.

**When this is worth it**: long-running multi-phase pipelines, high contamination risk, when the orchestrator accumulation problem is real. **When it's not**: simple 2-3 step workflows where a scope boundary or clean handoff is sufficient.

### The pragmatism check

Before choosing a mechanism, ask:
- Is the mixing actually degrading output, or is it theoretically impure but practically fine?
- Could a scope boundary solve this? (Try the cheapest thing first.)
- Is the overhead of sub-agents or a database justified by the improvement?
- For mega-prompt architectures: is the growing middle actually causing problems, or is mild accumulation an acceptable trade-off for simplicity?

The goal is better output, not architectural purity. A slightly contaminated single-agent workflow that ships is better than a perfectly separated multi-agent system that never gets built.

---

## The Growing Middle

In mega-prompt architectures — single prompts where output accumulates in a "middle" section between the system instructions and the current task — the middle is a cognitive mode accumulator.

Every step's output carries both information and cognitive style. By step 5, the middle contains investigation-flavoured prose, evaluation-flavoured judgments, and synthesis-flavoured commitments, all mixed together. The model reading this middle for step 6 is reading a slurry of every thinking mode that came before.

Sub-agent spawning with a "clean middle" is one solution — it works because clearing the middle clears the accumulated mode. The parent deciding what to pass down to the sub-agent is, whether the architect knows it or not, curating what cognitive residue carries forward.

The deeper pattern: **whatever mechanism manages the growing middle IS the cognitive architecture**. Whether you clear it between phases, compress it into structured form, write it to a database, or selectively pass sections to sub-agents — that decision determines how much mode contamination crosses between phases.

For simple workflows (2-3 steps, mild mode mixing), the growing middle is fine. For complex multi-phase work, the middle needs management — and the form that management takes is an architectural choice with cognitive consequences.

---

## Pipeline Sequencing: Why Order Matters

When a prompt needs to be split into multiple agents, the order of those agents matters — not just what each one does, but how they sequence, what crosses between them, and whether the sequence creates interference patterns that individual analysis would miss.

### The n-2 repetition cost

Returning to a recently abandoned cognitive mode is *harder* than switching to a new one. Research on task switching (Monsell 2003) shows that in an A→B→A sequence, the second A is impaired because A was actively inhibited to enable the switch to B. That inhibition persists.

For pipeline design, this means:

- **Bad**: investigate → evaluate → investigate again. The second investigation fights against the inhibition of the first.
- **Better**: investigate fully → synthesise → evaluate. Each stage is distinct, no returns to recently abandoned modes.
- **Worst**: rapid alternation — investigate → evaluate → investigate → evaluate. Each switch accumulates inhibition.

If your process *requires* returning to a mode (e.g., investigate, then evaluate, then investigate deeper based on evaluation), use a clean context for the second investigation rather than continuing in the same context. The fresh context doesn't carry the inhibition.

### Handoff contamination

When Agent 1 passes output to Agent 2, it's not just passing information — it's passing the cognitive style the information was produced in. If Agent 1 was investigating (exploratory, thread-following prose), that exploratory framing enters Agent 2's context and biases Agent 2 toward continued exploration, even if Agent 2 is supposed to be evaluating.

Signs of handoff contamination:
- An evaluation agent that keeps exploring instead of judging
- A synthesis agent that investigates new threads instead of committing to a narrative
- An agent that takes longer than expected because it's fighting against the framing of its input

The fix is **compression at handoffs**. Don't pass raw prose between agents. Compress findings into structured form — key points, evidence references, structured data. The structure strips the cognitive mode. A bullet list of findings doesn't carry the exploratory tone of the investigation that produced them.

### The compression-expansion rhythm

The healthiest pipeline pattern alternates between convergent compression and divergent reasoning:

```
Compress data → Reason over it → Compress findings → Reason over those
  (converge)     (diverge)        (converge)          (diverge)
```

This is an inverted Double Diamond — it starts with convergence because the pipeline starts data-rich, not data-poor. Each convergent stage chunks material so the next divergent stage can hold it in working memory. Each divergent stage produces new material that needs chunking before the next stage.

Every transition has a switching cost. But **discrete switching costs at clean boundaries are much cheaper than continuous interference from mixed modes in a single context**. Four clean stages with three transitions outperforms one mega-prompt doing all four simultaneously.

### Missing compression stages

The most common pipeline problem: raw output from one agent floods the next agent's context. Agent 1 produces 2000 words of investigation. Agent 2 receives all 2000 words and tries to evaluate. The investigation's exploratory framing, the thread-following digressions, the "this is interesting because..." asides — all of it enters the evaluation context as extraneous cognitive load.

The fix: add a compression step between agents. It doesn't need to be a separate agent — it can be part of Agent 1's output format ("produce structured findings, not prose") or part of the orchestrator's handoff logic ("extract key findings before passing to evaluation"). The compression is the cognitive boundary.

### Pipeline analysis vs prompt analysis

These aren't separate workflows — they're two zoom levels on the same analysis:

**Prompt-level**: "This individual prompt mixes investigation and evaluation internally — split them or add a scope boundary."

**Pipeline-level**: "These prompts are fine individually, but the sequence creates interference — Agent 3 outputs investigative framing that contaminates Agent 4's evaluation, and there's no compression step between them."

Pipeline analysis catches what individual prompt analysis misses:
- **Sequencing problems**: n-2 repetition costs from cycling through the same mode transitions
- **Handoff contamination**: one agent's cognitive style bleeding into the next agent's context
- **Missing compression stages**: raw output flooding downstream agents
- **Cumulative context bloat**: each agent adds material, so later agents work with progressively more interference
- **Redundant mode switches**: the pipeline cycling through the same transition multiple times unnecessarily

When analysing a pipeline, look at each prompt individually *and then* zoom out to look at the sequence. The individual analysis catches within-prompt conflicts. The pipeline analysis catches between-prompt interference.

---

## Runtime Composition: Skills, Sub-agents, and Progressive Loading

Pipelines have a fixed sequence — Agent 1 always runs before Agent 2. But modern agent architectures introduce **runtime composition**, where the full set of instructions active in a context isn't known until the session is running.

### How runtime composition works

In GitHub Copilot, Claude Code, and similar platforms, agents can load **skills** — additional instruction sets that extend the agent's capabilities on demand. Skills are loaded progressively: the agent starts with its base instructions, then skills are loaded into context when triggered by relevance or explicit invocation.

Similarly, a main agent may call **sub-agents** during execution. The sub-agent's output returns to the main agent's context, carrying both information and cognitive style (the same handoff contamination described in Pipeline Sequencing).

The key difference from pipelines: **you can't see the full cognitive context by reading any single file.** The agent's actual cognitive posture at runtime is: *base instructions + whatever skills loaded + whatever sub-agent output returned*. Mode conflicts may not exist in any individual file — they emerge when files combine.

### Why this matters for cognitive mode

Skills carry cognitive mode just like any other context. A skill written with an investigative posture (exploratory, thread-following) will push the agent toward investigation when loaded. A skill written with an evaluative posture (criteria-checking, severity-rating) will push toward evaluation. If both load into the same context, you get the same mode contamination as if both were written into a single prompt.

The risk is harder to detect because:
- **No single author sees the full context.** The base agent author and the skill author may be different people (or different sessions). Neither designed for the combination.
- **Combinations are non-deterministic.** Which skills load depends on the session. The agent might be clean in one session and contaminated in another, depending on which skills triggered.
- **The loading order matters.** A skill loaded early establishes posture. Later skills enter a context already carrying that posture — the same task-set inertia from Principle 1.

### What to look for

When analysing an agent that uses skills or sub-agents:

1. **Identify the agent's base cognitive posture.** What mode does the base prompt establish?
2. **Identify each skill's cognitive posture.** What mode does each skill carry?
3. **Check pairwise compatibility.** If skill A (investigation) and skill B (evaluation) could both be active, that's a potential mode conflict — even if neither conflicts with the base agent.
4. **Check for posture override.** Does a skill's framing override or contradict the base agent's established posture? A base agent that says "you are investigating, not assessing" breaks if a loaded skill says "assess each finding against these criteria."
5. **Note the composition signature.** Record what cognitive mode each component carries, so that composition conflicts can be identified without re-reading every file. Example: "Base: investigation. Skill A: investigation + light structuring. Skill B: evaluation. Skill C: generation. Conflict: B + base (evaluation overrides investigation posture)."

### Sub-agents are pipelines

When a main agent calls a sub-agent, the analysis is identical to pipeline analysis. The sub-agent's output returns to the main agent's context → handoff contamination applies → compression at the boundary matters. This isn't a new mechanism — it's the pipeline sequencing pattern operating within a single session.

### The pragmatism check

Not every skill combination creates problems. Many skills are additive (they provide domain knowledge, tool access, or formatting guidance without carrying a strong cognitive posture). Only flag combinations where the skills carry **incompatible cognitive postures** — investigation + evaluation, investigation + generation, or synthesis alongside ongoing investigation. Compatible combinations (investigation + structuring, evaluation + synthesis) are fine even when loaded together.

---

## How to Detect Contamination

Mode contamination is invisible in the output. You can't see what's missing by reading what you have. The method that works:

1. **Build, run, debrief.** Run the prompt on real work, then ask: where was the tension? What felt forced? Where was the output flat — because the task was hard, or because the prompt was triggering the wrong kind of thinking?

2. **Split and compare.** The gap between good and great only appears when you separate modes and run both. If you suspect contamination, split the suspect section into its own context and compare outputs.

3. **Watch for uniformity.** If every run produces roughly the same number of outputs regardless of input complexity, something is anchoring — either explicit numbers or implicit targets from examples, templates, or evaluation criteria.

4. **Look for suppressed capability.** "The output was always good enough to stop at. Until you see what it looks like when the modes aren't fighting each other." If the model seems to be playing it safe, producing competent-but-predictable output, that might be convergent contamination suppressing divergent potential.

5. **Check what you removed.** Counter-intuitively, removing a section sometimes improves output. If removing a QA section makes synthesis deeper, removing evaluation criteria makes investigation richer, or removing examples makes generation more creative — that's contamination you were carrying without knowing it.

---

## Why This Works: Cognitive Science Foundations

The effects described in this document aren't AI-specific discoveries. They map to established cognitive science mechanisms that explain *why* mode mixing degrades performance — in humans and, as recent research shows, in LLMs too.

### Task-switching costs (Rubinstein, Meyer, Evans 2001; Monsell 2003)

When humans switch between cognitive tasks, there's a measurable performance cost — slower response times, lower accuracy. Two mechanisms:
- **Goal shifting**: updating working memory with new task goals
- **Rule activation**: enabling new task rules while disabling old ones

Crucially, **task-set inertia** means the prior task's cognitive configuration persists and interferes with the new task, even beyond voluntary control. This is the scientific mechanism behind "context carries cognitive mode" — the previous task's posture lingers.

The **n-2 repetition cost** finding adds nuance: returning to a recently abandoned task (A→B→A) is *harder* than switching to a new task (C→B→A), because the abandoned task was actively inhibited. This may explain why interleaving modes (investigate→evaluate→investigate) is worse than clean separation.

A 2025 paper directly modelled "Attentional Residue" in LLMs as analogous to task-switching costs, finding that when a prompt shifts cognitive framing mid-context, the earlier framing persists as interference.

### Proactive interference in working memory (demonstrated in LLMs, 2025)

Working memory is subject to proactive interference — earlier information disrupts processing of newer information, especially when the items are semantically related. A paper titled "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length" found that LLM retrieval accuracy declines log-linearly as interference from earlier content accumulates — and that natural language prompts for "strategic forgetting" yielded only marginal improvements.

This maps directly to the growing middle problem. Earlier phases' output isn't just taking up space — it's actively interfering with the processing of later phases. The interference worsens as the context grows. The solution isn't "use more context" — it's managing what's in the context.

A separate "Cognitive Workspace" paper found that naive "add-all" approaches to context lead to "catastrophic interference" — the same pattern as mode contamination in growing-middle architectures.

### Cognitive Load Theory (Sweller)

Sweller's framework distinguishes three types of load on working memory:
- **Intrinsic load**: the inherent complexity of the task
- **Extraneous load**: imposed by how the task is presented — competes with intrinsic processing without contributing to the goal
- **Germane load**: productive effort spent building understanding

Mode mixing adds **extraneous load**. When a prompt asks for investigation AND evaluation, the evaluation framing consumes processing capacity without contributing to the investigation (and vice versa). A 2025 paper found that when combined load exceeds a "fragility tipping point," LLMs transition from successful reasoning to catastrophic failure — not gradual degradation, but a cliff.

Note: germane load (learning, schema-building) doesn't transfer to LLMs since they don't learn during inference. The mapping is strongest for intrinsic vs extraneous load competition.

### Chunking and the context window as working memory (Miller 1956, Cowan 2001)

Miller's "magical number seven" (revised by Cowan to approximately 4 items) describes working memory limits. Chunking — compressing complex information into manageable units — effectively expands what working memory can hold.

The convergent stages in a pipeline are doing chunking. They compress 55 policies into structured observations so a synthesis agent can hold them all simultaneously. The context window IS working memory. Convergent agents chunk. Divergent agents reason over chunks. You can't reason divergently over material you haven't chunked — not because of a philosophical principle, but because the material doesn't fit in working memory without compression.

### Guilford's Structure of Intellect (1956)

The popular convergent/divergent binary is an oversimplification of Guilford's own work. He proposed **five** mental operations: Cognition (understanding), Memory, Divergent Production, Convergent Production, and Evaluation. The types of thinking described in this document map closer to Guilford's full model than to the binary the field extracted from it:

| This Document | Guilford's Operation |
|---------------|---------------------|
| Investigation | Cognition |
| Structuring | Convergent Production |
| Evaluation | Evaluation |
| Generation | Divergent Production |
| Orchestration | (meta-operation, not in Guilford's model) |

A 2025 paper applied Guilford's full five-operation model to LLM prompt engineering with measurable performance gains. The multi-stance approach has empirical support beyond the practitioner evidence documented here.

### What this means for the framework

The five principles aren't prompt engineering heuristics. They're applications of established cognitive science to a new medium:

| Principle | Cognitive Science Mechanism |
|-----------|---------------------------|
| Context carries cognitive mode | Task-set inertia — prior configurations persist and interfere |
| Good output hides great output | Extraneous load competes below conscious detection thresholds |
| Lenses, not seeds | Content prescription adds extraneous load to divergent tasks |
| Numbers become targets | Anchoring interacts with convergent production to constrain output |
| Separate when they interfere | Task-switching costs and proactive interference are real but have varying severity |
| Human-driven mode transitions | Voluntary task switching at natural boundaries has lower switching costs than externally imposed switching (Arrington & Logan 2004) |

The mechanisms are well-established. The application to AI prompt design is recent and still developing. The labels used here may not be the final vocabulary — but the effects they describe have scientific grounding beyond one practitioner's experience.

### Further reading

- Rubinstein, Meyer, Evans (2001) — Executive Control of Cognitive Processes in Task Switching
- Monsell (2003) — Task switching (Trends in Cognitive Sciences)
- Sweller (1988) — Cognitive Load During Problem Solving
- Miller (1956) — The Magical Number Seven, Plus or Minus Two
- Guilford (1956) — The Structure of Intellect (Psychological Bulletin)
- Kramer (2025) — Cognitive Prompts Using Guilford's SOI Model ([arXiv:2503.22036](https://arxiv.org/html/2503.22036))
- PI-LLM (2025) — Proactive Interference Reveals Working Memory Limits in LLMs ([arXiv:2506.08184](https://arxiv.org/abs/2506.08184))
- Cognitive Load Limits in LLMs (2025) — ([arXiv:2509.19517](https://arxiv.org/pdf/2509.19517))
- Meta-R1 (2025) — Empowering LLMs with Metacognition ([arXiv:2508.17291](https://arxiv.org/pdf/2508.17291))
- Nelson & Narens (1990) — Metamemory: A Theoretical Framework and New Findings
- Wray, Kirk, Laird (2025) — Cognitive Design Patterns for LLM Agents ([arXiv:2505.07087](https://arxiv.org/html/2505.07087v2))
