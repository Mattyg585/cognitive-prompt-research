# Bridging Research: From Tacit Knowledge to AI System Specification

**What this is**: Research foundations for the Prompt Excavator -- an agent that helps people surface what they actually need from AI, then structures that knowledge into a brief that a prompt-writing agent can consume.

**The core problem**: Someone says "I want to automate my quoting process." Between that statement and a well-structured prompt (or pipeline) lies an enormous translation gap. The expert has tacit knowledge about edge cases, judgment calls, workflow structure, and cognitive demands that they cannot easily articulate. The prompt designer needs that knowledge in structured, actionable form. The Excavator bridges this gap.

**How this connects to the existing framework**: The cognitive stance reference establishes that different types of thinking need different architectural treatment. The prompt writer agent needs to know what types of thinking a task involves to design the right structure. The Excavator's job is to discover those types of thinking -- and everything else the prompt writer needs -- through structured conversation with the domain expert.

---

## 1. From Tacit Knowledge to System Specification

### The Knowledge Acquisition Bottleneck

The central challenge in building AI systems from human expertise is the same challenge that plagued expert systems in the 1980s: the **knowledge acquisition bottleneck**. Experts routinely omit 40-70% of key steps, cues, and decision strategies when teaching -- not because they're withholding, but because expertise compresses knowledge into automatic routines that are no longer consciously accessible (Militello & Hutton, 1998).

This is not a failure of communication. It is the nature of expertise. The Dreyfus model of skill acquisition (1980) describes how knowledge becomes progressively less articulable as it deepens:

| Stage | How knowledge is held | Articulation challenge |
|-------|----------------------|----------------------|
| **Novice** | Context-free rules, step-by-step | Fully articulable but shallow |
| **Advanced Beginner** | Rules + situational patterns | Can describe rules but not the pattern recognition |
| **Competent** | Problem-solving heuristics, prioritization | Can describe what they do but not always why |
| **Proficient** | Intuitive situation assessment, experience-based | "I just know what's important" -- can describe actions but not the perceptual discrimination |
| **Expert** | Automatic, holistic, non-reflective | "I just do what works" -- cannot decompose their own performance |

**The implication for the Excavator**: The people we're interviewing are typically at the proficient-to-expert level. They can tell you what they do, but not what they notice, not what they weigh, and not what they've stopped thinking about because it became automatic. The Excavator must use techniques that surface what experts cannot volunteer.

### Knowledge Engineering Methods That Work

**Cognitive Task Analysis (CTA)** is a family of methods specifically designed for this problem. The most relevant variants:

**Critical Decision Method (CDM)** -- developed by Gary Klein and colleagues. Uses a specific past incident as an anchor. The interviewer walks the expert through a real event, probing at each decision point: What did you notice? What were you expecting? What would a novice have missed? What would have changed your assessment? CDM works because the concrete incident gives the expert something to reason from rather than asking them to describe abstract processes. It surfaces tacit knowledge by contrasting what the expert did with what they might have done, or what a less experienced person would have done (Klein, Calderwood & Clinton-Cirocco, 1986; Hoffman, Crandall & Shadbolt, 1998).

**Applied Cognitive Task Analysis (ACTA)** -- a streamlined three-component method (Militello & Hutton, 1998):
1. **Task diagram interview**: Map the task structure -- what are the major steps, what makes each step hard?
2. **Knowledge audit**: For each difficult step, probe for the cognitive demands -- what judgments, what attention, what pattern recognition, what strategies?
3. **Simulation interview**: Walk through a scenario and ask the expert to identify key events and unpack their reasoning at each one.

ACTA is particularly relevant because it was designed to be usable by practitioners, not just researchers. It produces structured output (cognitive demand tables) that maps directly to what a prompt designer needs.

**Dervin's Sense-Making Methodology** -- frames knowledge gaps as the central unit of analysis. Dervin's model structures interviews around three elements: **situations** (time-space anchored moments where the expert encounters barriers), **gaps** (the questions, confusions, and judgment calls they face), and **bridges** (the sense-makings by which they resolve gaps). This is useful because it surfaces the uncertainty and judgment that experts smooth over in retrospective accounts. When an expert says "then I just quote it," Dervin's approach asks: what was the gap you were bridging? What could have gone wrong? What did you need to know that wasn't obvious? (Dervin, 1983, 1992).

### What Gets Lost in Translation

Even with good elicitation, the translation from expert knowledge to system specification introduces systematic losses:

1. **Context stripping**: Expert knowledge is deeply situated. "I check the margin" means different things for different customer types, order sizes, and market conditions. Formalizing it as a rule strips the context that makes it work.

2. **Flattening of judgment**: "I adjust the price" involves weighing relationship value, competitive pressure, margin floor, precedent effects, and gut feeling about the customer's budget sensitivity. A specification tends to flatten this into a decision tree that captures the branches but not the weights.

3. **Loss of negative space**: Experts know what NOT to do, what NOT to look for, what signals to ignore. This negative knowledge is rarely captured because elicitation focuses on what experts do, not what they deliberately avoid.

4. **Temporal compression**: Expert workflows have rhythm -- fast parts, slow parts, parts where you wait and think, parts where you act immediately. Specifications tend to represent all steps as equal-weight, losing the temporal structure that carries information about cognitive demand.

### How the Excavator Should Handle This

The Excavator's advantage over traditional knowledge engineering is that it can be iterative and conversational. It does not need to extract everything in one pass. Design principles:

- **Anchor in specifics, not abstractions.** "Tell me about a recent quote that was tricky" surfaces more than "How do you handle complex quotes?"
- **Probe the gaps.** When the expert says "then I decide the price," ask: What makes that hard? What could go wrong? When do you get it wrong?
- **Surface negative knowledge.** "What do you deliberately ignore?" "What would a new person waste time on?"
- **Capture the rhythm.** "Which parts take the most thought?" "Where do you slow down?" "What's automatic?"
- **Use contrast.** "How is this different from a simple case?" "What does a bad version of this look like?"

**Key citations:**
- Klein, G., Calderwood, R., & Clinton-Cirocco, A. (1986). Rapid decision making on the fire ground. *Proceedings of the Human Factors Society*, 30, 576-580.
- Militello, L. G. & Hutton, R. J. B. (1998). Applied cognitive task analysis (ACTA): a practitioner's toolkit for understanding cognitive task demands. *Ergonomics*, 41(11), 1618-1641.
- Hoffman, R. R., Crandall, B., & Shadbolt, N. (1998). Use of the Critical Decision Method to elicit expert knowledge. *Human Factors*, 40(2), 254-276.
- Dreyfus, S. E. & Dreyfus, H. L. (1980). A five-stage model of the mental activities involved in directed skill acquisition. University of California, Berkeley, Operations Research Center.
- Dervin, B. (1992). From the mind's eye of the user: The sense-making qualitative-quantitative methodology. In Glazier, J. D. & Powell, R. R. (Eds.), *Qualitative research in information management*, 61-84.

---

## 2. Task Decomposition Methods

### Hierarchical Task Analysis (HTA)

HTA decomposes a task into a hierarchy of goals, sub-goals, operations, and plans. Each goal is broken down until you reach operations that don't need further decomposition. Plans specify the conditions under which sub-goals are pursued (sequential, parallel, conditional).

**What it does well for our problem**: HTA gives you the structural skeleton of a task. "Process a quote" breaks into "gather requirements," "calculate pricing," "assess risk," "prepare document," "review and send." Each of these breaks further. The hierarchy shows which parts are nested inside others and what the control flow looks like.

**What it misses**: HTA is fundamentally about observable behavior and procedural structure. It does not capture cognitive demands, judgment calls, or the type of thinking required at each step. An HTA of "assess risk" might decompose it into "check credit history," "review order size," "evaluate market conditions" -- but it won't tell you that the first is a lookup (convergent), the second is a comparison (convergent), and the third is a judgment call requiring investigation and synthesis (divergent, requiring different architectural treatment).

**How it maps to prompt/pipeline design**: HTA gives you candidate task boundaries. But not all task boundaries are cognitive mode boundaries. Two adjacent HTA steps that require the same type of thinking can share an agent. One HTA step that requires incompatible types of thinking may need to be split. HTA is the skeleton; cognitive analysis puts the muscles on it.

### GOMS (Goals, Operators, Methods, Selection Rules)

GOMS models human-computer interaction as a hierarchy of goals, with operators (basic actions), methods (sequences of operators to achieve goals), and selection rules (how to choose between methods). It was developed for predicting human performance with computer interfaces (Card, Moran & Newell, 1983).

**What it does well**: GOMS is excellent at modeling procedural tasks where there are clear action sequences. It can predict execution time and identify inefficiencies. For routine, well-structured tasks, GOMS gives precise decomposition.

**What it misses**: GOMS assumes the user knows what to do and is choosing between known methods. It does not model problem-solving, diagnosis, or judgment. For the kinds of tasks where people say "I just know" -- exactly the cases the Excavator needs to handle -- GOMS has nothing to say. As the GOMS literature itself acknowledges, the framework is designed for "skilled, error-free performance" and breaks down for novel situations.

**How it maps to our problem**: GOMS is useful for the routine parts of a workflow -- the parts that are already well-structured and where the expert has a clear procedure. These are often the parts that need simple prompts, not pipelines. The interesting parts for the Excavator are the parts where GOMS breaks down -- where the expert departs from procedure to exercise judgment.

### Activity Theory

Activity Theory (Engestrom, 1987; Vygotsky, Leontiev) models human activity as mediated by tools, rules, community, and division of labor. An activity has a subject (the actor), an object (what they're working on), and an outcome. These are mediated by tools (instruments and signs), rules (norms and conventions), community (other participants), and division of labor (how the work is shared).

**What it does well**: Activity Theory captures the sociotechnical context of work. It reveals that "processing a quote" isn't just a cognitive task -- it involves tools (CRM systems, spreadsheets, price lists), rules (approval thresholds, discount policies), community (sales team, management, the customer), and division of labor (who gathers requirements vs. who prices vs. who approves). This social and material context shapes the cognitive demands.

**What it maps to for our problem**: Activity Theory tells you what the Excavator needs to capture beyond the task itself: What tools does the expert use? What rules constrain them? Who else is involved? What's the division of labor? These contextual factors determine whether a task can be fully automated, partially automated, or needs human-in-the-loop design. They also reveal where the "it depends" lives -- often in the rules and community interactions, not in the core task logic.

### Cognitive Work Analysis (CWA) and Rasmussen's Abstraction Hierarchy

CWA, developed by Jens Rasmussen and Kim Vicente, models work constraints rather than procedures. Its core tool is the Abstraction Hierarchy (AH), which describes a system at five levels: functional purpose, abstract function, generalized function, physical function, and physical form. Moving up the hierarchy answers "why"; moving down answers "how."

**What makes CWA distinctive**: CWA describes the space of possible behaviors, not a single prescribed procedure. This is crucial for our problem because expert work is rarely procedural -- experts adapt their approach based on the situation. CWA captures what the constraints are and what the degrees of freedom are, which is exactly what a prompt designer needs to know.

**Rasmussen's SRK framework** adds a layer: at any point in a task, the expert may be operating at the skill level (automatic, signal-based), rule level (IF-THEN pattern matching), or knowledge level (deliberate reasoning from first principles). These map directly to different AI architecture needs:

| SRK Level | Expert behavior | AI architecture implication |
|-----------|----------------|---------------------------|
| **Skill-based** | Automatic, pattern-driven | Simple prompt, recognition-primed, Tier 2 sufficient |
| **Rule-based** | IF condition THEN action | Decision logic, can be explicit in prompt |
| **Knowledge-based** | Novel reasoning, problem-solving | Investigation required, Tier 3 pipeline likely needed |

**The key insight for the Excavator**: Much of what experts do is skill-based or rule-based, and they can't always tell you which. The Excavator needs to determine the SRK level for each part of the task, because this directly predicts what architecture the prompt writer should use.

**Key citations:**
- Card, S. K., Moran, T. P., & Newell, A. (1983). *The Psychology of Human-Computer Interaction*. Lawrence Erlbaum Associates.
- Engestrom, Y. (1987). *Learning by Expanding: An Activity-Theoretical Approach to Developmental Research*. Orienta-Konsultit.
- Vicente, K. J. (1999). *Cognitive Work Analysis: Toward Safe, Productive, and Healthy Computer-Based Work*. Lawrence Erlbaum Associates.
- Rasmussen, J. (1983). Skills, rules, and knowledge; signals, signs, and symbols, and other distinctions in human performance models. *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-13(3), 257-266.

---

## 3. Decision Logic Extraction

### The "I Just Know" Problem

When an expert says "I just know," they are reporting accurately. At the expert level of the Dreyfus model, decisions are made through holistic pattern recognition, not conscious rule-following. The expert doesn't compare options -- they recognize the situation as an instance of a familiar pattern and act accordingly (Klein's RPD model). Extracting the decision logic means reverse-engineering a process that doesn't exist as explicit logic in the expert's mind.

### Methods for Extraction

**Decision trees and tables**: The traditional approach. Map each decision point to a tree of conditions and outcomes. Works well for rule-based decisions (Rasmussen's SRK rule level) where the expert CAN articulate the conditions. "If the order is over $50K and the customer is new, require management approval" -- this is explicit rule-based logic that maps directly to a prompt instruction or a conditional in a pipeline.

**Limitations**: Decision trees assume discrete conditions and clean branching. Expert judgment rarely works this way. "The margin depends on the relationship, the market, and my gut feeling about whether this will lead to more business" has continuous variables, interactive effects, and tacit weighting that a tree cannot represent without becoming unwieldy.

**Fuzzy logic**: Represents "it depends" through membership functions and linguistic variables. Instead of "order size > $50K," fuzzy logic can express "order size is large" with a gradual transition. A fuzzy inference system uses IF-THEN rules with fuzzy inputs: "IF order size is large AND relationship is new THEN margin is conservative."

**How this maps to prompts**: Fuzzy logic's linguistic variables map naturally to prompt language. A prompt can say "for large orders with new customers, be conservative on margin" -- and the LLM can interpret the fuzziness through its training distribution. This is arguably what LLMs are good at: working with the kind of graded, contextual, linguistically-expressed judgment that formal systems struggle with. The Excavator's job is to surface the linguistic variables and the fuzzy rules, not to formalize them into mathematical membership functions.

**Case-based reasoning (CBR)**: Instead of extracting rules, CBR captures exemplary cases and reasons by analogy. "This quote is like the one we did for Acme Corp last year, but with a tighter timeline." CBR is well-suited to experts who think in cases rather than rules -- and most experts do, even when they believe they're following rules. Research in knowledge engineering has found that what experts report as "rules" are often post-hoc rationalizations of case-based reasoning (Kolodner, 1993).

**How this maps to prompts**: CBR suggests that the Excavator should collect representative cases, not just rules. "Give me an example of a straightforward quote. Now a tricky one. Now one that went wrong." These cases can be included in the prompt as few-shot examples, or -- more powerfully -- the Excavator can extract the dimensions of variation across cases (what makes a case easy vs. hard) and encode those as lenses for the prompt writer.

**Pattern-based extraction**: Rather than asking for rules or cases, ask the expert to describe the patterns they notice. "What signals tell you this is going to be a problem?" "What does a good one look like vs. a bad one?" This maps to Klein's recognition-primed decision making: experts decide by recognizing patterns, so ask them about the patterns. The Critical Decision Method is specifically designed for this -- it surfaces the cues, patterns, and mental models that drive expert recognition.

### Representing "It Depends"

"It depends" is the most informative thing an expert can say, because it reveals the dimensions of variation. When the expert says "it depends," the Excavator should ask: **depends on what?** Each answer reveals a variable that matters. The collection of variables and their interactions IS the decision logic, even if it can't be captured in a clean tree.

For the Excavator's structured output, "it depends" should map to:
- **Dimensions of variation**: What factors affect the decision?
- **Interaction effects**: Which factors interact with each other?
- **Boundary conditions**: At what point does the approach change qualitatively (not just quantitatively)?
- **Representative cases**: An easy case, a hard case, and an edge case that illustrates the "it depends."

This representation is more useful to a prompt writer than a decision tree, because the prompt writer can encode it as context and lenses rather than trying to specify every branch.

**Key citations:**
- Kolodner, J. L. (1993). *Case-Based Reasoning*. Morgan Kaufmann.
- Klein, G. (1999). *Sources of Power: How People Make Decisions*. MIT Press.
- Zadeh, L. A. (1965). Fuzzy sets. *Information and Control*, 8(3), 338-353.

---

## 4. Mapping Cognitive Demands to AI Architecture

### The Novel Bridge

This is the question at the heart of the Prompt Excavator project: given that we know a task involves specific types of thinking, how do we systematically map from "what types of thinking this needs" to "what prompt/pipeline structure serves it"?

The existing cognitive stance reference provides the compatibility matrix (investigation + evaluation is toxic; investigation + structuring is fine). But there's a prior question: **how do you discover which types of thinking a task involves?** And a downstream question: **once you know, how do you choose the architecture?**

### Who's Doing This?

Based on thorough research, **nobody is doing this systematically**. The closest work:

**Cognitive Design Patterns (Wray, Kirk & Laird, 2025)** catalogs recurring patterns from cognitive architectures (SOAR, ACT-R) and maps them to LLM agent systems. The identified patterns include observe-decide-act cycles, hierarchical decomposition, memory commitment stages, and knowledge compilation. But these are architectural patterns, not a mapping from task cognitive demands to architecture choice. They tell you what patterns exist; they don't tell you which pattern a specific task needs.

**CoALA (Cognitive Architectures for Language Agents, 2023)** proposes a modular architecture with working memory, long-term memory (semantic, episodic, procedural), and a structured action space. CoALA gives you the building blocks but not the decision framework for which blocks to use when.

**SOFAI (Thinking Fast and Slow in AI)** implements a dual-process architecture with fast solvers (System 1 pattern matching), slow solvers (System 2 deliberate reasoning), and a metacognitive module that routes between them. This is the closest to a systematic mapping: the metacognitive module decides whether a task needs fast or slow processing. But it operates at the binary level (fast/slow), not at the richer level of cognitive mode differentiation that our framework identifies.

**REprompt (2026)** maps requirements engineering stages to prompt generation: elicitation, analysis, specification, validation. It treats prompts as requirements and applies RE methodology to optimize them. The structured output includes dependency-aware task lists and five-component system prompt decomposition (Role Definition, Knowledge, Available Tools, Context Information, Work Modes). This is interesting because it formalizes the brief-to-prompt translation, but it starts from software requirements, not from tacit expert knowledge.

**Knowledge Activation (Anthropic's Agent Skills, 2025-2026)** encodes institutional knowledge into Atomic Knowledge Units with seven components: intent declaration, procedural knowledge, tool bindings, organizational metadata, governance constraints, continuation paths, and validators. The pipeline has three stages: codification (extract tacit knowledge), compression (distill into dense units), injection (deliver at runtime). This explicitly addresses the tacit-to-formal translation using Nonaka and Takeuchi's SECI model, but focuses on encoding knowledge for consumption by coding agents, not on mapping cognitive demands to architectural decisions.

### A Proposed Mapping Framework

Synthesizing across the research, here's a candidate mapping from cognitive demand signals to architectural decisions. This is the novel contribution -- it connects the elicitation work to the design work.

**Step 1: Identify the types of thinking the task requires.**

Use the cognitive mode taxonomy from the stance reference (investigation, structuring, evaluation, synthesis, reframing, generation, orchestration). The Excavator surfaces these through questions like:
- "Where do you need to figure out what's going on?" (investigation)
- "Where do you organize or categorize?" (structuring)
- "Where do you judge quality or correctness?" (evaluation)
- "Where do you pull everything together into a conclusion?" (synthesis)
- "Where do you translate for a different audience?" (reframing)
- "Where do you create something new?" (generation)

**Step 2: Determine the SRK level for each cognitive demand.**

For each identified type of thinking, determine whether the expert operates at the skill, rule, or knowledge level (Rasmussen's SRK). This maps to architecture:
- **Skill-level**: The expert does it automatically. The LLM can likely handle it with a simple prompt instruction. No pipeline separation needed.
- **Rule-level**: The expert follows IF-THEN logic (even if implicit). The prompt can encode these as explicit conditions. Tier 2 with clear instructions is likely sufficient.
- **Knowledge-level**: The expert reasons from first principles, adapts to novelty, or makes judgment calls that require genuine investigation. This is where Tier 3 pipeline separation earns its cost.

**Step 3: Check the compatibility matrix.**

Which types of thinking need to coexist? Apply the interference principles from the stance reference:
- Investigation + evaluation: separate (evaluation pre-filters investigation)
- Investigation + generation (analytical): separate (only investigates what it can fix)
- Investigation + generation (creative/voice): may be compatible (exploration IS the creative process)
- Evaluation + synthesis: compatible (assess then commit)
- Any mode + orchestration: separate (coordinator goes down rabbit holes)

**Step 4: Apply the recognition-primed vs. investigation-required test.**

Could the correct output be produced without seeing the specific input data? If yes -- recognition-primed, Tier 2 with proper epistemic stance. If no -- investigation-required, Tier 3 with clean context separation.

**Step 5: Determine the pipeline structure.**

If pipeline separation is warranted:
- Map the cognitive modes to pipeline stages (one mode per stage, or compatible modes combined)
- Order them in the compression-expansion rhythm (converge-diverge-converge-diverge)
- Design handoffs that strip cognitive mode (structured data, not prose)
- Set epistemic stance at each stage boundary

### The Decision Framework as a Whole

```
Task description (vague)
    |
    v
[Excavator: elicit through CDM/ACTA-style probing]
    |
    v
Cognitive demand map: what types of thinking, at what SRK level
    |
    v
[Check compatibility matrix + recognition-primed test]
    |
    v
Architecture decision: single prompt | Tier 2 optimised | Tier 3 pipeline
    |
    v
[If pipeline: stage design, handoff design, epistemic stance per stage]
    |
    v
Structured brief for prompt writer
```

**Key citations:**
- Wray, R. E., Kirk, J. R., & Laird, J. E. (2025). Applying cognitive design patterns to general LLM agents. *Proceedings of AGI 2025*. [arXiv:2505.07087](https://arxiv.org/html/2505.07087v2)
- Sumers, T. R. et al. (2023). Cognitive architectures for language agents. [arXiv:2309.02427](https://arxiv.org/abs/2309.02427)
- Bergamaschi Ganapini, M. (2025). Fast, slow, and metacognitive thinking in AI. *npj Artificial Intelligence*.
- REprompt (2026). Prompt generation for intelligent software development guided by requirements engineering. [arXiv:2601.16507](https://arxiv.org/abs/2601.16507)
- Knowledge Activation (2026). AI skills as the institutional knowledge primitive. [arXiv:2603.14805](https://arxiv.org/html/2603.14805v1)

---

## 5. The Brief as Interface

### What the Prompt Writer Needs

The prompt writer agent (from the existing toolkit) works from briefs. Looking at what it does with a brief, we can reverse-engineer what the brief must contain:

1. **Types of thinking required**: The writer maps the brief to investigation, structuring, evaluation, synthesis, reframing, generation, orchestration. The brief should surface these explicitly, or provide enough information that the mapping is unambiguous.

2. **Compatibility assessment**: The writer determines which types can coexist and which need separation. The brief should flag known incompatibilities or at least identify the high-judgment, high-uncertainty areas where incompatibility is likely.

3. **Architecture decision inputs**: Is this recognition-primed or investigation-required? Does the input data contain novel patterns that must be discovered, or is this applying known frameworks? The brief needs to answer this question or provide the information to answer it.

4. **Edge cases and exceptions**: What makes the task hard? What are the unusual cases? What judgment calls must be made? These determine where the prompt needs flexibility vs. structure.

5. **Domain constraints**: What rules, policies, tools, and conventions constrain the task? These become explicit prompt instructions.

6. **Audience and voice**: Who receives the output? What register, tone, and level of detail is appropriate? This determines whether voice continuity matters (which affects pipeline design).

7. **Input/output specification**: What goes in? What comes out? What format? This is the engineering layer that turns cognitive design into executable specification.

### Candidate Brief Structure

Drawing from requirements engineering, knowledge management research, and the specific needs of the prompt writer:

```
## Task Overview
- What the AI system should accomplish (1-2 sentences)
- Who it serves (the end user, not the AI)
- What success looks like (observable outcomes, not process)

## Cognitive Demand Map
- Types of thinking required (from the taxonomy)
- SRK level for each (skill/rule/knowledge)
- Known incompatibilities or tensions
- Recognition-primed vs investigation-required assessment

## Workflow Structure
- Major phases/steps (from HTA-style decomposition)
- Control flow (sequential, conditional, parallel)
- Where the hard parts are (cognitive demand hotspots)
- Where judgment is required vs. where rules apply

## Decision Logic
- Key decisions and what they depend on
- Dimensions of variation ("it depends on...")
- Boundary conditions (where the approach changes qualitatively)
- Representative cases: easy, hard, edge case

## Domain Context
- Rules and constraints (policies, thresholds, approval gates)
- Tools and systems involved
- Stakeholders and their concerns
- Terminology and conventions

## Input Specification
- What the AI receives
- Volume and complexity range
- What the input looks like in easy vs hard cases

## Output Specification
- What the AI produces
- Format and structure requirements
- Quality criteria (what makes output good vs bad)
- Who receives it and what they do with it

## Edge Cases and Failure Modes
- Known tricky scenarios
- Common mistakes (what goes wrong)
- What the expert watches for
- Negative knowledge (what to deliberately ignore)

## Complexity Assessment
- Simple prompt | Optimised prompt | Pipeline recommendation
- Rationale for the recommendation
- Key factors driving complexity
```

### Design Principles for the Brief

**The brief is a boundary object.** Star and Griesemer (1989) define boundary objects as artifacts that are "plastic enough to adapt to local needs and constraints of the several parties employing them, yet robust enough to maintain a common identity across sites." The brief serves two communities: the domain expert (who validates it) and the prompt writer (who builds from it). It must be readable by the expert ("yes, that's what I mean") and actionable by the writer ("I know what to build").

**Structured data over prose.** The trust chain principle from the existing framework applies: structured handoffs strip cognitive mode. If the Excavator produces exploratory prose, the prompt writer inherits that exploratory posture. If it produces structured fields with specific content, the prompt writer receives information without cognitive residue.

**Preserve the expert's language where it matters.** Some domain terminology carries meaning that paraphrasing would lose. The brief should include actual expert phrases for key concepts, edge cases, and quality criteria. These become candidate prompt language.

**Include representative cases.** A brief with examples is worth ten briefs without. The cases anchor the abstraction in concrete reality and give the prompt writer material for few-shot examples.

**Flag uncertainty.** Not everything will be resolved in one excavation session. The brief should mark areas where more information is needed, where the expert was uncertain, or where different experts might disagree. This prevents the prompt writer from building false precision into the specification.

**Key citations:**
- Star, S. L. & Griesemer, J. R. (1989). Institutional ecology, translations, and boundary objects. *Social Studies of Science*, 19(3), 387-420.
- Nonaka, I. & Takeuchi, H. (1995). *The Knowledge-Creating Company*. Oxford University Press.

---

## 6. Complexity Signals and Triage

### The Triage Question

Early in an excavation conversation, you need to determine: does this task need a simple prompt, an optimised prompt (Tier 2), or a full pipeline (Tier 3)? Getting this wrong in either direction is costly -- over-engineering wastes effort, under-engineering leaves performance on the table.

### Complexity Frameworks

**Wood's Task Complexity Theory (1986)** identifies three dimensions:

1. **Component complexity**: How many distinct acts and information cues are involved? A task with three steps and five inputs is simpler than one with fifteen steps and forty inputs.

2. **Coordinative complexity**: How do the components relate to each other? Sequential steps are simpler than steps with feedback loops, conditional branching, and parallel paths. When the output of step 3 depends on the interaction of steps 1 and 2, coordinative complexity is high.

3. **Dynamic complexity**: Does the task change while you're doing it? Are the relationships between inputs and outputs stable, or do they shift based on context, time, or accumulated results?

**The Cynefin Framework (Snowden, 1999)** offers a different lens -- not the complexity of the task itself but the complexity of the domain:

| Domain | Characteristic | AI approach |
|--------|---------------|-------------|
| **Clear** | Known cause-and-effect, best practices exist | Simple prompt with explicit rules |
| **Complicated** | Cause-and-effect discoverable through analysis | Tier 2 with domain expertise encoded |
| **Complex** | Cause-and-effect only visible in retrospect, emergent patterns | Tier 3 with investigation stage; probing required |
| **Chaotic** | No apparent cause-and-effect | Not suitable for AI automation without human-in-the-loop |

### Triage Signals

From the research, here are signals the Excavator can detect early in conversation that predict complexity tier:

**Signals pointing to Simple Prompt (Tier 1)**:
- The expert can describe the task in a few sentences
- Steps are sequential and non-conditional
- "It's pretty straightforward"
- One type of thinking dominates (usually generation or structuring)
- Low component complexity, low coordinative complexity
- Clear domain -- known best practices

**Signals pointing to Optimised Prompt (Tier 2)**:
- The task involves judgment but within known frameworks
- "It depends" appears but the dimensions of variation are enumerable
- Multiple types of thinking, but compatible ones (evaluation + synthesis)
- Recognition-primed -- the expert's training knowledge is the primary source
- Complicated domain -- analysis required but patterns are stable
- Moderate component complexity, low dynamic complexity

**Signals pointing to Pipeline (Tier 3)**:
- "Every case is different" -- high dynamic complexity
- The expert describes needing to figure out what's going on BEFORE deciding what to do -- investigation required
- Incompatible types of thinking in the same task (investigation + evaluation)
- The input data contains patterns that must be discovered (not just classified)
- "I can't tell you the rules because it really depends on what I find"
- Complex domain -- emergent patterns, cause-and-effect not predictable
- High coordinative complexity -- many interacting parts

**Signals pointing to Human-in-the-Loop (not fully automatable)**:
- "Sometimes I just go with my gut and I can't explain why"
- Chaotic domain characteristics
- Ethical judgment required
- Relationship management or negotiation involved
- The expert describes frequent exceptions that override all rules

### A Lightweight Decision Framework

```
1. How many distinct types of thinking does this task require?
   - 1-2 compatible types → likely Tier 1 or 2
   - 3+ types, or incompatible pairs → likely Tier 3

2. Could the correct output be produced from training knowledge alone?
   - Yes → Tier 2 ceiling
   - No, must investigate specific data → Tier 3 likely

3. Does the expert say "it depends" more about the approach or the content?
   - Content ("the price depends on volume") → rules in prompt, Tier 2
   - Approach ("how I handle it depends on what I find") → pipeline, Tier 3

4. How much of the task is automatic (skill-level) vs deliberate (knowledge-level)?
   - Mostly automatic → simple prompt or Tier 2
   - Significant knowledge-level reasoning → Tier 3

5. Does the task require discovering patterns in novel data?
   - No → Tier 2
   - Yes → Tier 3
```

**Key citations:**
- Wood, R. E. (1986). Task complexity: Definition of the construct. *Organizational Behavior and Human Decision Processes*, 37(1), 60-82.
- Snowden, D. J. & Boone, M. E. (2007). A leader's framework for decision making. *Harvard Business Review*, 85(11), 68-76.

---

## 7. From Business Process to AI Workflow

### Process Mining and BPM

Business Process Management (BPM) and process mining offer mature methodologies for turning observed work into formal specifications. The relevance to our problem: someone says "I want to automate my quoting process" -- BPM has spent decades figuring out how to capture, model, and optimize such processes.

**Process mining** works from event logs -- it observes what actually happens (as opposed to what people say happens) and discovers process models. The output is typically a visual model showing the actual flow, variants, bottlenecks, and deviations. Modern platforms (Celonis, SAP Signavio) can generate BPMN models directly from event data.

**Task mining** extends this to the desktop level, capturing user interactions (clicks, form fills, copy-paste operations) to model how people actually perform tasks. This surfaces the micro-level workflow that experts take for granted.

**How this maps to our problem**: Process mining reveals the actual workflow structure, including the variations and exceptions that experts omit in interviews. If we have access to event logs or can observe the expert's workflow, this is a powerful complement to interview-based elicitation. The discovered process model gives the Excavator a map to probe against: "The data shows you go back to the pricing step 30% of the time -- what triggers that?"

### BPMN as Intermediate Representation

Business Process Model and Notation (BPMN) provides a standard visual language for workflow specification. It can represent:
- Sequential and parallel flows
- Conditional branching (gateways)
- Events (triggers, timers, exceptions)
- Subprocesses (nested task groups)
- Swim lanes (role-based task assignment)

**What we can borrow**: BPMN's notation for gateways (decision points), events (triggers), and subprocesses (nested complexity) maps naturally to prompt/pipeline design decisions. A BPMN gateway where the expert makes a judgment call becomes a candidate for pipeline separation. A BPMN subprocess with multiple steps becomes a candidate for a single agent. Parallel lanes become candidates for fan-out architecture.

**What we should not borrow**: BPMN is designed for executable process automation -- every path must be fully specified. This creates pressure toward false precision that the Excavator should resist. The expert's process has fuzzy boundaries, contextual adaptation, and judgment calls that BPMN forces into explicit branches. Use BPMN's structural vocabulary without its requirement for completeness.

### The Process-to-Pipeline Translation

| BPM concept | Pipeline analog |
|-------------|----------------|
| Task | Agent or prompt instruction |
| Gateway (XOR) | Conditional routing in orchestrator |
| Gateway (parallel) | Fan-out architecture |
| Subprocess | Pipeline stage or sub-pipeline |
| Swim lane | Agent with specific cognitive posture |
| Event (trigger) | Input condition for pipeline initiation |
| Exception handler | Error handling / fallback agent |
| Loop | Iterative refinement stage |

The translation is structural, not direct. A BPM task "Review quote for accuracy" might be a single task in the process model but require two cognitive modes (investigation + evaluation) that need separate pipeline stages. The Excavator's cognitive demand analysis adds the layer that BPM misses.

### Agentic Process Intelligence

The field is converging: process mining platforms are integrating AI agents, and AI agent frameworks are incorporating process awareness. A 2025 paper describes a multi-agent framework for autonomous process mining and optimization. Process intelligence platforms now include "Action Flows" -- automated workflows that can orchestrate across systems.

**The opportunity for the Excavator**: Rather than choosing between interview-based elicitation and process-based discovery, combine them. Use process mining (where available) to discover the actual workflow, then use interview-based elicitation to fill in the cognitive demands, judgment calls, and tacit knowledge that process data can't capture. The process model provides the structural skeleton; the expert interview provides the cognitive muscles.

**Key citations:**
- van der Aalst, W. M. P. (2016). *Process Mining: Data Science in Action*. Springer.
- OMG (2011). Business Process Model and Notation (BPMN) Version 2.0. Object Management Group.

---

## 8. Knowledge Transfer and Handoff Design

### The Excavator's Output as Handoff

The Excavator produces a structured brief. The prompt writer consumes it. This is a handoff -- and everything the existing framework says about handoff contamination applies.

### What Knowledge Management Research Says

**Nonaka and Takeuchi's SECI Model** describes four modes of knowledge conversion:

1. **Socialization** (tacit to tacit): Shared experience transfers tacit knowledge. The Excavator's conversation with the expert is socialization -- the Excavator develops an understanding through interaction that goes beyond what's explicitly stated.

2. **Externalization** (tacit to explicit): Making tacit knowledge explicit through metaphors, analogies, models, hypotheses. This is the Excavator's core function -- taking what the expert "just knows" and expressing it in structured form.

3. **Combination** (explicit to explicit): Combining, editing, restructuring explicit knowledge. The prompt writer does this -- taking the brief's explicit knowledge and combining it with prompt design principles to produce a specification.

4. **Internalization** (explicit to tacit): Learning by doing, embodying explicit knowledge. This happens when the AI system runs and its users develop intuitions about how to use it effectively.

**The SECI model tells us** that the Excavator's brief is doing the hardest conversion -- externalization. It's trying to crystallize tacit knowledge into a form that survives transfer to a different context (the prompt writer's context). The research says this works best through metaphors, analogies, and models -- not through exhaustive rule lists.

**For the brief design**: Include metaphors and framings, not just facts. "This is like a doctor's differential diagnosis" or "Think of it as triage, not thorough examination" -- these carry more useful information for the prompt writer than a detailed process description, because they invoke the right cognitive posture.

### Structured Handoff Design for AI Agents

Recent work on AI agent handoff (2025-2026) identifies the core problem: context loss between agents. The solutions converge on structured briefings over raw context passing:

**What gets lost in naive handoff:**
- Reasoning chains (the "why" behind decisions)
- Constraints that were discovered during processing
- Confidence levels and uncertainty markers
- The distinction between facts and inferences

**What structured handoff preserves:**
- Decisions and non-negotiable constraints
- Artifacts (actual deliverables)
- Preferences and patterns accumulated during processing
- Timeline (what was done, when, and in what order)

**The design principle**: Treat inter-agent transfer like a public API. Use JSON Schema-based structured outputs, not free-text summaries. Each field has a defined type and purpose. The receiving agent can query specific information rather than searching through a text dump.

### Applying This to the Excavator-Writer Handoff

The brief structure from Section 5 is the handoff schema. Additional design principles:

1. **Separate observations from interpretations.** The Excavator should mark which parts of the brief are direct from the expert ("expert says: every case over $100K gets special handling") and which are the Excavator's interpretation ("this suggests knowledge-level reasoning triggered by order size threshold"). The prompt writer needs both, but needs to know which is which.

2. **Preserve access to lower-level data.** The data stance principle from the existing framework: higher-stance summaries should be accompanied by lower-stance evidence. The brief should include representative expert quotes, not just the Excavator's synthesis. This lets the prompt writer pull on threads the Excavator didn't follow.

3. **Flag confidence and completeness.** Not everything will be fully excavated. Mark areas where the elicitation was thin, where the expert was uncertain, or where more probing would be valuable. This prevents the prompt writer from treating gaps as certainties.

4. **Include the cognitive mode markers explicitly.** Don't make the prompt writer infer what types of thinking are involved. State them: "This phase requires investigation (the expert must figure out what's going on in the specific data before they can assess it)." "This step is rule-based evaluation (clear criteria, known thresholds)."

**Key citations:**
- Nonaka, I. & Takeuchi, H. (1995). *The Knowledge-Creating Company*. Oxford University Press.
- Star, S. L. & Griesemer, J. R. (1989). Institutional ecology, translations, and boundary objects. *Social Studies of Science*, 19(3), 387-420.

---

## 9. Unexpected Connections and Adjacent Fields

### Sensemaking as Excavation Method

Karl Weick's organizational sensemaking (1995) and Brenda Dervin's sense-making methodology (1983) offer something the CTA methods don't: a framework for how people create meaning from ambiguous situations. Weick argues that sensemaking is retrospective, social, ongoing, focused on extracted cues, driven by plausibility rather than accuracy, and grounded in identity construction.

**Why this matters for the Excavator**: The expert is sensemaking when they describe their work. They are constructing a retrospective narrative that may or may not reflect what they actually do. Weick's insight that sensemaking is driven by plausibility, not accuracy, warns us that expert self-reports are stories that make sense to the expert, not objective descriptions of cognitive processes. The Excavator must account for this -- using incident-based probing (CDM) to get past the retrospective narrative to the actual decision points.

**Dervin's gap-bridging model** is directly applicable as an excavation technique. Structure the conversation around: What situation were you in? What gap did you face? How did you bridge it? This surfaces the judgment calls that experts smooth over in procedural descriptions.

### Boundary Objects and the Brief

The brief functions as a **boundary object** (Star & Griesemer, 1989) -- an artifact that spans two communities (domain experts and prompt designers) and must be interpretable by both while maintaining useful specificity.

Star and Griesemer identified four types of boundary objects:
1. **Repositories** (shared databases, indexes)
2. **Ideal types** (diagrams, atlases, abstract models)
3. **Coincident boundaries** (objects with shared boundaries but different content per community)
4. **Standardized forms** (templates that standardize working methods)

The brief is closest to a **standardized form** -- a template that structures the knowledge transfer. But it should incorporate elements of **ideal types** (the cognitive demand map is an abstract model) and **coincident boundaries** (the domain expert sees their workflow in it; the prompt writer sees architectural decisions in it).

### Knowledge Compilation and the Dreyfus Paradox

The Cognitive Design Patterns paper (Wray, Kirk & Laird, 2025) identifies **knowledge compilation** as a critical pattern: converting expensive multi-step reasoning into compact, reusable representations. In SOAR, this is "chunking" -- turning deliberate problem-solving into automatic rules.

**The Dreyfus paradox for AI**: We're asking experts to decompose their compiled knowledge back into the deliberate steps that a novice would follow. This is inherently lossy -- compiled knowledge has thrown away the scaffolding. But the AI needs the scaffolding, because it doesn't have the compiled knowledge (unless the task matches training data well enough for recognition-primed processing).

**The implication**: The Excavator is not just extracting knowledge. It is **de-compiling** expert knowledge back into a form that can be re-compiled into a different medium (AI prompts). This reframe helps explain why the extraction is hard and why the output will never be a perfect representation -- de-compilation is lossy by nature.

### Ecological Interface Design and the Abstraction Hierarchy

Vicente's work on Ecological Interface Design (EID) offers a principle that applies to the brief: **display the work domain at multiple levels of abstraction simultaneously**. The brief should include:
- **Functional purpose**: Why does this task exist? What value does it create?
- **Abstract function**: What principles govern how it works? (e.g., margin must exceed cost, customer satisfaction must be maintained)
- **Generalized function**: What are the general processes? (e.g., gather requirements, calculate pricing, assess risk)
- **Physical function**: What specific actions occur? (e.g., look up part numbers, check discount schedules)
- **Physical form**: What tools and data sources are used? (e.g., the CRM system, the price list spreadsheet)

This multi-level representation gives the prompt writer the context to make architectural decisions at the right level. A functional purpose statement like "maintain margin while retaining customers" tells the prompt writer something about the task's cognitive character that a physical-level description of steps does not.

### The Ethnographic Turn in Knowledge Engineering

Recent work in knowledge engineering is borrowing from anthropology. A 1995 paper on "Using anthropological interview strategies to enhance knowledge acquisition" found that ethnographic approaches -- treating the expert as an informant in their own culture, attending to artifacts and rituals, not just stated procedures -- captured knowledge that traditional structured interviews missed.

**For the Excavator**: Don't just ask what the expert does. Ask what they look at (their screen, their notes, their email). Ask what tools they keep open. Ask what they do when they're stuck. These contextual details reveal the cognitive support infrastructure that the AI system will need to replicate or replace.

### The Meta-Reasoning Connection

Ackerman and Thompson (2017) found that metacognitive judgments are often based on **heuristic cues** -- fluency, feeling of effort, elapsed time -- rather than direct access to cognitive performance. People use proxies to assess how well they're thinking.

**For the Excavator**: When an expert says "this is the hard part," they may be reporting high cognitive effort, or they may be reporting low fluency (the task feels hard because it's unfamiliar, even if it's cognitively simple). The Excavator should probe what "hard" means: Is it hard because there's a lot to consider? Because the answer is uncertain? Because the consequences of getting it wrong are high? Because it requires knowledge they don't always have? Each type of "hard" maps to a different architectural intervention.

### Process Mining as Validation

A powerful use of process mining that's underexplored: using it to **validate** the expert's account against actual behavior. Process mining can reveal that the expert claims they always check credit before pricing, but event data shows they often skip it for returning customers. This gap between espoused process and actual process is exactly where tacit knowledge lives -- the expert has an implicit rule ("I don't need to check credit for customers I know") that they didn't report because it's so automatic they don't notice it.

### The Knowledge Activation Pipeline as Precedent

Anthropic's Knowledge Activation work (2026) is the closest existing system to what we're building, but operating in a different domain (encoding institutional knowledge for coding agents). Their three-stage pipeline -- codification, compression, injection -- maps to our problem:

| Knowledge Activation | Prompt Excavator |
|---------------------|------------------|
| **Codification**: extract tacit knowledge from experts, runbooks, policies | **Excavation**: surface tacit knowledge through structured conversation |
| **Compression**: distill into Atomic Knowledge Units | **Brief generation**: structure into the handoff document |
| **Injection**: deliver at runtime decision points | **Prompt writing**: the downstream agent that builds from the brief |

Their Atomic Knowledge Unit structure (intent declaration, procedural knowledge, tool bindings, organizational metadata, governance constraints, continuation paths, validators) is interesting as a candidate structure for our brief's domain context section.

**Key citations:**
- Weick, K. E. (1995). *Sensemaking in Organizations*. Sage Publications.
- Vicente, K. J. & Rasmussen, J. (1992). Ecological interface design: Theoretical foundations. *IEEE Transactions on Systems, Man, and Cybernetics*, 22(4), 589-606.
- Ackerman, R. & Thompson, V. (2017). Meta-reasoning: Monitoring and control of thinking and reasoning. *Trends in Cognitive Sciences*, 21(8), 607-617.

---

## 10. Synthesis: What This Means for the Prompt Excavator

### The Excavator's Core Design Challenge

The Excavator must do three things simultaneously:
1. **Elicit** tacit knowledge from domain experts (knowledge engineering)
2. **Analyse** the cognitive demands of the elicited task (cognitive task analysis)
3. **Structure** the results into a brief that a prompt writer can build from (knowledge representation)

These are themselves different types of thinking -- and they need to be managed carefully. Elicitation is investigative (follow threads, surface what's there). Analysis is evaluative (classify cognitive demands, check compatibility). Structuring is convergent (compress into defined fields). By our own framework, mixing investigation and evaluation in the same context degrades both.

### Proposed Excavator Architecture

The Excavator should likely be a **two-phase agent with a clean handoff between phases**, or a **single agent with explicit temporal mode transitions** driven by the conversation's natural rhythm:

**Phase 1: Elicitation (investigation mode)**
- Open, exploratory conversation with the expert
- Uses CDM/ACTA-style probing techniques
- Follows threads, captures specifics, collects cases
- Does NOT classify or evaluate -- just surfaces knowledge
- Epistemic stance: "discovering what's here"

**Phase 2: Analysis and Structuring (evaluation + convergent mode)**
- Works from the elicitation output
- Classifies cognitive demands against the taxonomy
- Checks the compatibility matrix
- Runs the triage/complexity assessment
- Produces the structured brief
- Epistemic stance: "organizing what was found"

Whether these should be separate agents (pipeline) or separate phases of one agent (temporal separation with human-driven transitions) depends on how the Excavator is used. If it's interactive (human present), temporal separation is natural -- the expert conversation IS Phase 1, and the brief generation IS Phase 2. If it's autonomous (processing a recorded interview or written description), pipeline separation is cleaner.

### Key Design Principles

1. **The Excavator elicits; it does not prescribe.** Its job is to discover what the task actually requires, not to impose a structure. The structure comes from the cognitive demand analysis, which is downstream of elicitation.

2. **Probe what "hard" means.** The expert's report of difficulty is a signal. Unpack it into cognitive demand dimensions: uncertainty, volume, judgment, novelty, consequences.

3. **Collect cases, not just rules.** Cases are the richest knowledge representation for our purpose. They give the prompt writer examples, edge cases, and dimensions of variation all at once.

4. **Surface the negative space.** What the expert doesn't do, doesn't look at, and deliberately ignores is as important as what they do.

5. **Separate observation from interpretation.** In the brief, mark what came from the expert and what came from the Excavator's analysis. The prompt writer needs both, but needs to know the provenance.

6. **Flag the triage early.** Within the first few exchanges, the Excavator should have a working hypothesis about complexity tier. This shapes the depth of subsequent probing -- a Tier 1 task doesn't need deep cognitive demand analysis.

7. **The brief is a boundary object.** It must be readable by the expert ("yes, that's my process") and actionable by the prompt writer ("I know what architecture to use"). Design for both audiences.

8. **Iterate.** The Excavator doesn't need to get everything in one pass. The brief can be partial, flagging areas for further probing. This is how real knowledge engineering works -- multiple passes with increasing depth.

### Open Questions

1. **How interactive should the Excavator be?** Pure conversation vs. structured interview vs. form-filling. The research says conversation surfaces more tacit knowledge, but structured approaches produce more consistent output.

2. **Can the triage be automated?** Can the Excavator reliably determine complexity tier from early signals, or does this require human judgment?

3. **How much cognitive science vocabulary belongs in the brief?** The prompt writer understands "investigation mode" and "evaluation mode." The domain expert does not. The brief needs to serve both -- but it's primarily for the prompt writer. Should there be two views?

4. **What's the minimum viable excavation?** Some tasks are simple enough that a brief conversation plus the triage framework is sufficient. What's the "good enough" threshold for each complexity tier?

5. **How should the Excavator handle disagreement between experts?** If two experts describe the same task differently, that's a signal about the task's ill-structuredness (Spiro's CFT). The Excavator should capture the disagreement, not resolve it -- the prompt writer needs to know the task has multiple valid approaches.

---

## Sources

### Knowledge Elicitation and CTA
- [Tacit knowledge elicitation process for Industry 4.0](https://link.springer.com/article/10.1007/s44163-022-00020-w)
- [Applied cognitive task analysis (ACTA)](https://pubmed.ncbi.nlm.nih.gov/9819578/)
- [Critical Decision Method for eliciting knowledge](https://journals.sagepub.com/doi/10.1518/001872098779480442)
- [CDM - Gary Klein](https://www.gary-klein.com/cdm)
- [Unveiling the Unspoken: AI-Enabled Tacit Knowledge Co-Evolution](https://www.mdpi.com/2673-9585/6/1/1)
- [Knowledge acquisition bottleneck in AI](https://www.alphanome.ai/post/the-lingering-shadow-understanding-the-knowledge-acquisition-bottleneck-in-artificial-intelligence)

### Task Decomposition and Cognitive Engineering
- [GOMS Models for Task Analysis (Kieras)](https://web.eecs.umich.edu/~kieras/docs/TA_Modeling/GOMSforTA.pdf)
- [Cognitive Work Analysis - Wikipedia](https://en.wikipedia.org/wiki/Cognitive_work_analysis)
- [Rasmussen's SRK Framework](https://taproot.com/skill-rule-and-knowledge-models/)
- [Dreyfus Model of Skill Acquisition](https://en.wikipedia.org/wiki/Dreyfus_model_of_skill_acquisition)
- [Hierarchical Task Decomposition](https://www.emergentmind.com/topics/hierarchical-task-decomposition)

### Decision Logic and Knowledge Representation
- [Fuzzy Logic in Decision Support](https://www.researchgate.net/publication/350164537_Fuzzy_Logic_in_Decision_Support_Methods_Applications_and_Future_Trends)
- [Case-Based Reasoning and Expert Systems (Springer)](https://link.springer.com/chapter/10.1007/978-3-642-32986-9_1)
- [Knowledge-driven fuzzy logic framework (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1568494625007264)

### Cognitive Architecture and AI Agent Design
- [Cognitive Design Patterns for LLM Agents (Wray, Kirk, Laird 2025)](https://arxiv.org/html/2505.07087v2)
- [CoALA: Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427)
- [Fast, slow, and metacognitive thinking in AI (npj AI)](https://www.nature.com/articles/s44387-025-00027-5)
- [Knowledge Activation: AI Skills as Institutional Knowledge Primitive](https://arxiv.org/html/2603.14805v1)
- [REprompt: Requirements Engineering-Guided Prompt Generation](https://arxiv.org/abs/2601.16507)

### Knowledge Transfer and Handoff
- [AI Agent Handoff: Why Context Breaks & How Structured Memory Fixes It](https://xtrace.ai/blog/ai-agent-handoff-why-context-gets-lost-between-agents-and-how-to-fix-it)
- [SECI Model of Knowledge Dimensions - Wikipedia](https://en.wikipedia.org/wiki/SECI_model_of_knowledge_dimensions)
- [Boundary Objects, Knowledge Integration, and Innovation Management](https://www.sciencedirect.com/science/article/pii/S0166497222001961)
- [Memory for AI Agents: Context Engineering](https://thenewstack.io/memory-for-ai-agents-a-new-paradigm-of-context-engineering/)

### Complexity and Triage
- [Wood (1986) - Task complexity: Definition of the construct](https://www.sciencedirect.com/science/article/abs/pii/0749597886900440)
- [Cynefin Framework](https://en.wikipedia.org/wiki/Cynefin_framework)
- [Task Triage: AI Suitability & Risk Assessment Framework](https://tasktriage-ai.netlify.app/)
- [Task Complexity in Human-AI Decision Making](https://dl.acm.org/doi/fullHtml/10.1145/3565472.3592959)

### Business Process and Workflow
- [Process Mining and AI in BPM](https://www.researchgate.net/publication/401597756_Process_Mining_and_Artificial_Intelligence_in_Business_Process_Management_Improvement)
- [Multi-agent Framework for Process Mining and Optimization](https://www.jait.us/articles/2025/JAIT-V16N10-1487.pdf)
- [Process Mining using BPMN (Springer)](https://link.springer.com/article/10.1007/s10270-015-0502-0)

### Sensemaking and Methodology
- [Dervin's Sense-Making Theory](https://www.researchgate.net/publication/284311730_Dervin's_Sense-Making_Theory)
- [Sense-making systematic review (2025)](https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.24866)
- [Sensemaking in Organizations (Weick)](https://www.researchgate.net/publication/257397559_Sensemaking_in_organizations_by_Karl_E_Weick_Thousand_Oaks_CA_Sage_Publications_1995_231_pp)

### Specification and Brief Design
- [How to write a good spec for AI agents (Addy Osmani)](https://addyosmani.com/blog/good-spec/)
- [Accelerating ontology engineering with LLMs (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1570826825000022)
- [Ontology in AI - 2025 Guide](https://dev.to/bikashdaga/ontology-in-ai-2025-guide-structure-semantics-applications-in-knowledge-representation-44aa)
