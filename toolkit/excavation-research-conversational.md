# Conversational Elicitation Research for the Prompt Excavator

**What this is**: A divergent research exploration covering conversational interview design, knowledge elicitation, adaptive questioning, and related fields -- assembled to inform the design of an AI agent that helps people articulate what they need from AI systems.

**What this isn't**: A finished design document. This is raw research with threads to pull. Some threads will be dead ends. The downstream prompt writer takes what's useful and discards the rest.

**How it connects**: The Prompt Excavator operates across three modes -- Primer (generating smart questions for a domain expert), Excavate (processing meeting notes into structured findings), and Refine (targeted follow-up). This research covers the conversational and cognitive foundations for all three.

---

## 1. Conversational Interview Design for AI

### The core tension

Traditional interviewing rests on a trade-off: structured surveys enable scale but constrain depth; conversational interviews provide depth but are resource-intensive. The Prompt Excavator sits at the intersection -- it needs the adaptability of a skilled interviewer at the scale of a tool anyone can use.

### AI as adaptive interviewer

Recent research directly addresses this. Ziebell et al. (2024) introduced "AI Conversational Interviewing" (AICI) -- replacing human interviewers with LLMs to conduct semi-structured interviews at scale. Their study randomly assigned university students to AI or human interviewers and found AI-conducted interviews produced data quality comparable to human interviewers, with the added benefit of scalability. The LLM maintained conversational flow, generated contextually appropriate follow-ups, and adapted probing depth based on response quality.

Key findings from this work:
- **Probing capability**: The LLM chatbot was "capable of multiple types of probing, including to elicit depth and to verify the meaning of responses" -- not just generic follow-ups but functionally differentiated probes.
- **Excessive probing risk**: Results suggest that "excessive probing early in surveys can increase respondent dropout." The preliminary recommendation: place probes in the middle or end sections. This has direct implications for the Excavator's pacing.
- **Role assignment matters**: Hasanuzzaman et al. (2025) found that assigning the AI specific interviewer roles (e.g., "empathetic listener" vs "critical examiner") significantly affected the quality and depth of follow-up questions generated. Role framing at the epistemic stance level -- consistent with the cognitive stack.

### What makes a question productive vs superficial

The qualitative research literature distinguishes between questions that open space and questions that fill checkboxes. Roulston (2023) provides a theoretical and practical framework for probing in qualitative interviews:

- **Probing achieves extra depth** via verbal prompts to clarify, elaborate, illustrate, or explain a prior answer. The key word is "prior" -- a good probe responds to what was actually said, not to what the interviewer expected.
- **Laddered probes**: Probes can be chained in sequence -- the interviewer probes the response to the previous probe, following threads deeper. This maps directly to the Excavator's "refine" mode.
- **The funnel technique**: Start broad and open-ended, then gradually narrow to specifics. Each main question begins a new funnel -- broad opening, then progressively targeted follow-ups. The purpose is "to avoid influencing user behavior or perceptions as much as possible" (Nielsen Norman Group).

### Practical design implications

- The Excavator's questioning should follow the funnel pattern: open exploration first, targeted probing second. In Primer mode, generate questions that start broad ("Tell me about your current invoicing process") before drilling down ("What happens when a client disputes a charge?").
- Probing should be responsive to what was said, not prescriptive. The "refine" mode is inherently probe-based -- it takes specific findings and generates questions that dig into those findings.
- Pacing matters. Front-loading deep probes creates cognitive load and increases abandonment. The Excavator should build conversational momentum before going deep.

### Key citations

- Ziebell et al. (2024). [AI Conversational Interviewing: Transforming Surveys with LLMs as Adaptive Interviewers](https://arxiv.org/abs/2410.01824). ACL Anthology, LaTeCH-CLfL 2025.
- Hasanuzzaman et al. (2025). [Harnessing the Power of AI in Qualitative Research: Role Assignment and AI-Generated Follow-Up Questions](https://arxiv.org/html/2509.12709v1).
- Roulston (2023). [Probing in qualitative research interviews: Theory and practice](https://www.tandfonline.com/doi/full/10.1080/14780887.2023.2238625).
- [The Funnel Technique in Qualitative User Research](https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/) -- Nielsen Norman Group.

---

## 2. Socratic Method and Guided Discovery

### The expression gap

The most directly relevant recent work is "Closing the Expression Gap in LLM Instructions via Socratic Questioning" (2025). The paper identifies the fundamental problem our Excavator faces:

> "The intention expression gap -- the difficulty for humans to effectively convey complex, high-dimensional thoughts to AI -- often traps users in inefficient trial-and-error loops and is exacerbated by diverse expertise levels."

Their solution: an agent called **Nous** that reframes the interaction from "passive instruction following" to a "Socratic collaboration paradigm." Instead of waiting for the user to perfectly articulate what they want, Nous "actively probes for information to resolve its uncertainty about user intent."

The core mechanism is grounded in information theory: **information gain from dialogue serves as an intrinsic reward signal**, equivalent to the reduction of Shannon entropy over a structured task space. Each question-answer turn is designed to maximize convergence toward shared understanding.

This is exactly what the Excavator does -- but framed through information theory rather than conversational design. The connection is powerful: the Excavator isn't just "asking good questions" -- it's systematically reducing uncertainty about what the user needs.

### Paul and Elder's Socratic questioning taxonomy

Richard Paul and Linda Elder developed a taxonomy of Socratic questions based on elements of thought. The six categories are not hierarchical -- they're complementary lenses:

1. **Questions of clarification**: "What do you mean by...?" "Can you give an example?" -- surfacing what's actually being said.
2. **Questions probing assumptions**: "What are you assuming when you say...?" "Is that always the case?" -- making implicit beliefs explicit.
3. **Questions probing reasons and evidence**: "What led you to that conclusion?" "How do you know that?" -- grounding claims in experience.
4. **Questions about viewpoints and perspectives**: "How would your clients see this?" "What would someone who disagrees say?" -- expanding the frame.
5. **Questions probing implications and consequences**: "If that's true, what follows?" "What would happen if...?" -- tracing downstream effects.
6. **Questions about the question**: "Why is this question important?" "What does this assume?" -- meta-level reflection.

Each type serves a different epistemic function. For the Excavator:
- **Primer mode** should generate questions across all six types, weighted by what's most likely to surface useful information from a domain expert.
- **Excavate mode** should use types 1-3 (clarification, assumptions, evidence) when processing notes -- flagging where claims are unclear, where assumptions are hidden, where evidence is missing.
- **Refine mode** should lean on types 2, 4, and 5 -- probing assumptions, perspectives, and implications that the initial excavation revealed as gaps.

### Socratic agents in practice

Several implementations of Socratic AI agents exist:

- **SocraticLLM** (educational AI tutor): Trained to guide students through Socratic-style dialogue, it "asks structured, thought-provoking questions that lead students to their own understanding" rather than giving answers directly. The design principle: changing the focus from providing answers to formulating questions.

- **Socratic Human Feedback (SoHF)** (Amazon Science, code generation): Expert programmers used Socratic feedback strategies to guide LLMs through problems the models initially failed. By "employing a combination of different Socratic feedback strategies across multiple turns, programmers successfully guided models to solve 74% of the problems that the models initially failed to solve on their own." This is the inverse of our scenario (human guiding AI rather than AI guiding human), but the strategy repertoire transfers.

- **SocraticAI** (Princeton NLP): Multiple LLMs engage in Socratic dialogue with each other, with one playing the Socratic role -- demonstrating that the method works even without a human partner. The key insight: "different instantiations of LLMs themselves might collaboratively discover or 'recollect' knowledge to solve problems" -- suggesting the method has intrinsic value beyond human-AI interaction.

### The anti-leading principle

Socratic questioning has a critical constraint: **you must not lead the witness**. The questions should help the person discover what they know, not confirm what the questioner assumes. This maps directly to the "lenses not seeds" principle from the cognitive stance reference:

- A leading question seeds a specific answer: "Don't you think your invoicing process would benefit from automation?" (convergent -- the answer is pre-shaped).
- A Socratic question opens discovery: "Walk me through what happens from when a job is completed to when you get paid. Where do things slow down?" (divergent -- the answer space is open).

For the Excavator, this means:
- Questions in Primer mode should be lenses, not seeds. They should guide the consultant's attention without prescribing what they'll find.
- The Excavator should resist the temptation to be "helpful" by suggesting answers inside questions. That's the expression gap in reverse -- the AI projecting its assumptions onto the human.

### Key citations

- [Closing the Expression Gap in LLM Instructions via Socratic Questioning](https://arxiv.org/abs/2510.27410) (2025).
- Paul, R. & Elder, L. (2006). [The Thinker's Guide to Socratic Questioning](https://www.criticalthinking.org/files/SocraticQuestioning2006.pdf). Foundation for Critical Thinking.
- [SocraticLLM: From Answers to Understanding](https://www.starspark.ai/blog/socratic-llm-tutors) (2025).
- [Socratic Human Feedback: Expert Steering Strategies for LLM Code Generation](https://www.amazon.science/publications/socratic-human-feedback-sohf-expert-steering-strategies-for-llm-code-generation) -- Amazon Science.
- [The Socratic Method for Self-Discovery in Large Language Models](https://princeton-nlp.github.io/SocraticAI/) -- Princeton NLP Group.
- [Reflecting in the Reflection: Integrating a Socratic Questioning Framework into Automated AI-Based Question Generation](https://arxiv.org/html/2601.14798v1) (2025).

---

## 3. Active Listening Techniques Adapted for AI

### The research baseline

Xiao et al. (2020) conducted the definitive study on active listening in AI chatbots: "If I Hear You Correctly: Building and Evaluating Interview Chatbots with Active Listening Skills." They identified specific active listening techniques and tested their effects:

- **Paraphrasing**: Restating the interviewee's response in different words to confirm understanding.
- **Verbalizing emotions**: Naming the emotional content detected in the response ("It sounds like that's frustrating").
- **Summarizing**: Condensing multiple points into a compact restatement.
- **Encouraging**: Brief verbal signals that invite continued elaboration ("Tell me more about that").

The findings were clear: **chatbots with active listening skills outperformed baseline chatbots on multiple dimensions**. Participants found them more engaging, showed higher interest in future interaction, and -- critically -- **produced higher-quality responses measured by Gricean Maxims** (informativeness, relevance, specificity, and clarity).

### Why this matters for AI specifically

In text-based interaction, the absence of non-verbal feedback creates a signaling gap. In face-to-face conversation, a nod or "mm-hmm" signals comprehension without interrupting flow. In text, the AI must explicitly signal that it understood before moving to the next question -- otherwise the human doesn't know if their input landed.

The mechanism: **active listening signals create a grounding check** (in the sense of Clark & Brennan's conversational grounding theory -- see Section 8). The AI demonstrates it parsed and understood the input, which gives the human confidence to continue sharing.

### Specific techniques for the Excavator

**In Excavate mode** (processing meeting notes):
- **Structured paraphrasing**: "From these notes, I understand that [X]. The core workflow appears to be [Y]. Is that right, or am I missing something?" -- This isn't just summarizing; it's making the AI's interpretation explicit so the user can correct it.
- **Flagging emotional content**: If meeting notes contain frustration signals ("This process is a nightmare"), the Excavator should acknowledge the frustration rather than sanitizing it: "The notes suggest real friction around [X] -- multiple references to problems and workarounds. Is this the primary pain point?"
- **Summary-and-check**: After processing a block of notes, produce a structured summary and explicitly ask: "What did I get wrong? What's missing?"

**In Refine mode** (follow-up):
- **Reflective questions**: "You mentioned [X] earlier. When you say [specific phrase], do you mean [interpretation A] or something more like [interpretation B]?" -- This surfaces ambiguity without assuming an answer.
- **Encouraging depth**: "That's interesting -- can you walk me through a specific example of when that happened?" -- Moving from abstract to concrete.

**In Primer mode** (generating questions for a consultant):
- The questions themselves should embed active listening guidance: "When they describe [X], reflect back what you heard and ask if you've got it right before probing further." The consultant preparation should include not just what to ask, but how to listen.

### The Gricean connection

Grice's maxims of conversation (quantity, quality, relation, manner) provide a framework for evaluating both the Excavator's outputs and the inputs it receives:
- **Quantity**: Is the user providing enough information? If responses are terse, the Excavator should probe for elaboration.
- **Quality**: Is the information reliable? The Excavator should flag claims that seem uncertain or contradictory.
- **Relation**: Is the response relevant to the question asked? Tangential answers may contain valuable information about what the user actually cares about (versus what was asked).
- **Manner**: Is the response clear? Ambiguous or jargon-heavy responses need clarification.

### Key citations

- Xiao, Z. et al. (2020). [If I Hear You Correctly: Building and Evaluating Interview Chatbots with Active Listening Skills](https://arxiv.org/abs/2002.01862). CHI 2020.
- Clark, H.H. & Brennan, S.E. (1991). Grounding in communication. In Resnick, L.B. et al. (Eds.), *Perspectives on Socially Shared Cognition*. APA.
- Grice, H.P. (1975). Logic and conversation. In Cole, P. & Morgan, J.L. (Eds.), *Syntax and Semantics 3: Speech Acts*. Academic Press.

---

## 4. Adaptive Questioning and Dialogue Management

### Detecting expertise level

The Excavator must serve users ranging from non-technical small business owners to advanced AI engineers. Research on adaptive dialogue systems identifies several signals for detecting user expertise:

**Vocabulary and jargon usage**: Novices describe goals and contexts using everyday language; experts specify technical constraints and use domain-specific terminology. Srinivasan et al. (2021) found that "novice users may know technical expressions only for the most commonplace domain objects, intermediate users may have knowledge of a few related concepts... and experts may know names for almost all the domain objects."

**Response length and structure**: Experts engage in slightly longer dialogues (10.68 messages average) with longer utterances (17.3 words) compared to novices (9.87 messages, 14.0 words). Experts provide more structured, specification-like responses; novices provide narrative, goal-oriented descriptions.

**Implicit detection via jargon probing**: One adaptive approach uses deliberate jargon insertion: "by using jargon expressions, [the system] can discover the user's knowledge about the domain, because users will ask for clarification questions when presented with jargon that they do not know." This is elegant but risky for the Excavator -- using jargon with a non-technical user might feel alienating rather than diagnostic.

**Better approach for the Excavator**: Start with natural, accessible language and observe how the user responds. If they use technical terms unprompted, match their register. If they describe things in everyday language, stay in everyday language. Let the user's language set the register rather than testing them with jargon.

### Conversational style adaptation

Research on conversational recommender systems identifies two contrasting styles:

- **High involvement**: Fast-paced, direct, proactive with frequent prompts. Better for users who know what they want and prefer efficiency.
- **High considerateness**: Polite, accommodating, prioritizing clarity and user comfort. Better for users who are uncertain or unfamiliar with the domain.

The finding: "adapting conversational strategies based on user expertise and allowing flexibility between styles can enhance both user satisfaction and the effectiveness of recommendations."

### Dialogue state management

Google's AMIE system (Articulate Medical Intelligence Explorer) provides the most sophisticated example of AI-driven adaptive dialogue. AMIE uses a **state-aware dialogue framework** that progresses through three phases (History Taking, Diagnosis & Management, Follow-up), each with clear objectives. Transitions between phases are "triggered automatically when the system assesses that the objectives of the current phase have been met."

AMIE's "chain of reasoning" strategy at each turn:
1. Summarize what's known so far
2. Formulate the next response/question
3. Revise for accuracy, clarity, and empathy

In a randomized double-blind study comparing AMIE to primary care physicians in text-based consultations, AMIE demonstrated "greater diagnostic accuracy and superior performance on 30 out of 32 axes according to specialist physicians and 25 out of 26 axes according to patient-actors."

### Design implications for the Excavator

The AMIE architecture suggests a pattern for the Excavator's dialogue management:

**Internal state tracking**: At each turn, the Excavator should maintain an internal model of:
- What's known (facts established so far)
- What's uncertain (ambiguous or contradictory information)
- What's missing (expected information not yet surfaced)
- User expertise level (inferred from language and response patterns)

**Phase-aware behavior**: In Primer mode, the Excavator progresses from domain understanding to question generation. In Excavate mode, from raw processing to structured findings to gap identification. In Refine mode, from gap targeting to specific probing. Phase transitions should be adaptive, not prescribed.

**The register adaptation rule**: Match the user's language. If they say "we need to figure out our RAG pipeline's retrieval accuracy," respond at that technical level. If they say "we need to make the search work better," respond at that level. Never talk up or down -- mirror.

### Key citations

- [Know Your Users! Estimating User Domain Knowledge in Conversational Recommenders](https://arxiv.org/abs/2512.13173) (2025).
- [Identifying users' domain expertise from dialogues](https://dl.acm.org/doi/pdf/10.1145/3450614.3461683) (2021).
- [Adaptive Dialogue Management for Conversational Information Elicitation](https://www.researchgate.net/publication/361830507) (2022).
- [Towards Conversational Diagnostic AI (AMIE)](https://arxiv.org/html/2401.05654v1) (2024). Published in [Nature](https://www.nature.com/articles/s41586-025-08866-7) (2025).
- [Adaptive Generation in Dialogue Systems Using Dynamic User Modeling](https://direct.mit.edu/coli/article/40/4/883/1487/) -- Computational Linguistics.

---

## 5. The Primer/Preparation Problem

### How experts prepare for unfamiliar domains

The Primer mode faces a distinctive challenge: generating smart questions for a domain you don't know. This is precisely what consultants do when preparing for client engagements in unfamiliar industries.

**The consulting preparation pattern**:
1. **Map the domain structure**: What are the key processes, roles, stakeholders, constraints? Not deep understanding -- enough to ask non-stupid questions.
2. **Identify the decision-makers**: "Who will be making the final decisions on this project and who will be in charge of implementation?" Amateur consultants learn this the hard way.
3. **Force specificity**: "What is your number one priority for this business unit during this fiscal year?" -- questions that force the expert out of generalities and into specifics.
4. **Adapt frameworks to the situation**: The consulting case interview literature emphasizes that "one of the most common mistakes is applying a generic framework without adapting it to the actual problem." Always listen to the specific situation before applying a framework.

**What makes a prepared interviewer effective**:
- They know enough about the domain to ask questions at the right level of abstraction -- not so high that the answers are generic, not so low that they miss the forest for the trees.
- They've identified what they don't know and crafted questions specifically targeting those gaps.
- They have a mental model of what a "complete picture" would look like, so they can notice when key pieces are missing.

### Applied Cognitive Task Analysis (ACTA) as a primer framework

ACTA (Militello & Hutton, 1998) was designed exactly for the primer problem: enabling non-experts to extract expert knowledge through structured interviews. It has three phases:

1. **Task diagram**: A high-level map of the major steps in the expert's work. This is the "what do you do?" overview that establishes the terrain.

2. **Knowledge audit**: Probes for specific types of expert knowledge:
   - **Perceptual cues**: What do you notice that a novice wouldn't?
   - **Situational awareness**: How do you build a picture of what's happening?
   - **Anomaly recognition**: When do you know something is wrong?
   - **Job smarts/workarounds**: What shortcuts or unofficial methods do you use?
   - **Improvisation**: What do you do when standard procedures don't work?
   - **Self-monitoring**: How do you know if you're doing well or poorly?

3. **Simulation interview**: Walk through a specific scenario, probing at key decision points.

This is directly applicable to Primer mode. The Excavator can use the ACTA probe categories as a lens for generating interview questions -- not prescribing specific questions, but providing the consultant with question types that are known to surface tacit knowledge.

### The Critical Decision Method (CDM)

For more experienced interviewers, CDM (Klein, Calderwood & Clinton-Cirocco, 1986) provides a deeper protocol:

1. Select a specific critical incident from the expert's experience
2. Walk through it chronologically, identifying key decision points
3. At each decision point, probe:
   - What cues did you notice?
   - What were you expecting to happen?
   - What goals were competing?
   - What options did you consider?
   - How did you decide?
   - What would a novice have missed?

CDM is particularly good at surfacing **tacit knowledge** -- "experts routinely omit 40-70% of key steps, cues, and decision strategies when teaching without CTA." The omission isn't intentional; expertise compresses knowledge into automatic routines that are no longer consciously accessible.

### Design implications for Primer mode

The Excavator's Primer output should include:

1. **Domain orientation**: A brief structural map of the domain (key processes, roles, tools, constraints) -- enough for the consultant to have a mental model before the meeting.

2. **Question bank organized by type**: Not a flat list, but questions categorized by what they surface:
   - Process questions (what happens, in what order)
   - Decision questions (where choices are made, what drives them)
   - Exception questions (what goes wrong, how it's handled)
   - Pain point questions (where friction is, what causes frustration)
   - Aspiration questions (what "good" looks like, what they wish were different)

3. **ACTA-inspired probes**: For each major process area, include probes that target tacit knowledge: "What would someone new to this role miss?" "When do you just know something is off?"

4. **Anti-leading guidance**: Remind the consultant to listen first, probe second, and avoid projecting assumptions.

### Key citations

- Militello, L.G. & Hutton, R.J.B. (1998). [Applied Cognitive Task Analysis (ACTA): A Practitioner's Toolkit](https://pubmed.ncbi.nlm.nih.gov/9819578/). *Ergonomics*, 41(11), 1618-1641.
- Klein, G., Calderwood, R. & Clinton-Cirocco, A. (1986). Rapid decision making on the fire ground. *Proceedings of the Human Factors Society*, 30, 576-580.
- Hoffman, R.R., Crandall, B. & Shadbolt, N. (1998). [Use of the Critical Decision Method to Elicit Expert Knowledge](https://journals.sagepub.com/doi/10.1518/001872098779480442). *Human Factors*, 40(2), 254-276.
- Brown, O., Power, N. & Gore, J. (2025). [Cognitive Task Analysis: Eliciting Expert Cognition in Context](https://journals.sagepub.com/doi/10.1177/10944281241271216). *Organizational Research Methods*.
- [An Easier Method for Extracting Tacit Knowledge](https://commoncog.com/an-easier-method-for-extracting-tacit-knowledge/) -- Commoncog (practical guide to ACTA).

---

## 6. Processing Unstructured Input

### The challenge

Excavate mode takes meeting notes, voice transcriptions, stream-of-consciousness text, and email threads -- and must extract structured knowledge from them. The input is messy by nature. What gets lost, what should be flagged, and how do you distinguish what's clear from what's ambiguous?

### What gets lost in unstructured input

Research on information extraction identifies several systematic losses:

**Context collapse**: Meeting notes often capture conclusions without the reasoning that led to them. "We decided to use Xero" doesn't tell you what alternatives were considered, what criteria drove the decision, or who pushed for it. The Excavator should flag decisions that lack supporting rationale.

**Implicit knowledge**: Experts omit what they consider obvious. A builder's meeting notes might say "standard NCC specs" -- which is a specific technical reference that a non-expert reader would miss. The Excavator needs to identify domain-specific shorthand and flag it for expansion.

**Hedging and certainty levels**: In conversation, people hedge ("I think," "probably," "we might") in ways that carry important information about confidence levels. Transcription flattens these into equally weighted statements. The Excavator should preserve and surface hedging signals.

**Relational information**: Meeting notes often capture facts but not relationships between facts. "Client wants faster turnaround" and "Current turnaround is 3 weeks" are related but may appear pages apart. The Excavator should surface relationships that the notes don't make explicit.

### Processing approaches

Modern AI approaches to unstructured text use several complementary strategies:

**Semantic chunking**: Breaking documents into logical sections while preserving context, rather than splitting at arbitrary boundaries. Meeting notes often have natural break points (topic changes, speaker changes, timeline shifts) that should be respected.

**Entity and relation extraction**: Identifying people, organizations, processes, tools, timelines, and the relationships between them. This is the foundation of structured output.

**Schema-based extraction**: Processing input against a target schema -- what information do we need? What's present? What's missing? This directly supports gap detection (see Section 7).

### What the Excavator should produce

From unstructured input, the Excavator should produce:

1. **Structured findings**: Key facts, decisions, requirements, constraints, preferences -- organized by topic.
2. **Confidence markers**: What's clearly stated vs what's inferred vs what's assumed. The Excavator should explicitly mark its confidence level.
3. **Ambiguity flags**: Where the input is unclear, contradictory, or could be interpreted multiple ways. Don't resolve ambiguity -- surface it.
4. **Missing information markers**: What you'd expect to find but didn't. What questions the notes raise but don't answer.
5. **Relationship maps**: How the extracted facts relate to each other -- dependencies, conflicts, prerequisites, implications.

### The data stance principle

This connects directly to the cognitive stance framework's concept of data stance. The Excavator's output carries a cognitive stance that shapes what downstream agents (including the Prompt Writer) can do with it:

- **Descriptive output** (what was said, without interpretation): Opens the widest space for downstream processing.
- **Classified output** (organized by topic/category): Useful but constrains -- the Prompt Writer sees through the Excavator's classification lens.
- **Evaluated output** (this matters, this doesn't): Most constrained -- downstream agents inherit the evaluation and can only work within its boundaries.

**The Excavator should produce primarily descriptive and classified output, not evaluated output.** Evaluation is the downstream agent's job. The Excavator's job is to surface everything relevant and flag what's ambiguous, not to judge what matters.

### Key citations

- [Exploring AI-driven approaches for unstructured document analysis](https://link.springer.com/article/10.1186/s40537-024-00948-z) (2024). *Journal of Big Data*.
- [NLP Techniques for Extracting Information from Unstructured Text](https://www.width.ai/post/extracting-information-from-unstructured-text-using-algorithms) -- Width.ai.
- [Information Extraction overview](https://www.ibm.com/think/topics/information-extraction) -- IBM.

---

## 7. Follow-up and Gap Detection

### How do you identify what's missing?

This is one of the hardest problems in elicitation: detecting the absence of information that should be present. You can't search for what you don't know to look for.

### The information-gap-driven approach

Recent research on follow-up question generation provides a directly applicable framework. The approach (2025) works by:

1. **Generate a hypothetical "complete" response**: A teacher LLM generates what a comprehensive answer to the initial question would look like.
2. **Contrast with the actual response**: Compare the complete response to the often-incomplete initial answer.
3. **Identify information gaps**: The delta between complete and actual = the gaps.
4. **Formulate gap-bridging follow-up questions**: Each question targets specific missing information.

This is powerful because it explicitly models the gap rather than just probing generically. The mechanism: "By generating multiple follow-up questions, each targeting some unanswered information, this approach ensures diversity and informativeness."

### Gap-focused question generation for assessment

A complementary approach from educational dialogue systems (Ruckdeschel & Rueckert, 2023) frames gap detection through the lens of common ground:

- **Information overlap** between what's known (teacher/system) and what's been shared (student/user) = common ground.
- **The gap** = what the system expects to know but the user hasn't shared.
- Drawing on Grice's maxims: "speakers don't communicate what is already known, so teachers should not ask about what is already in the common ground with the student."

The implication for the Excavator: **don't ask about what you already know. Ask about what you don't know.** This sounds obvious but most interview systems repeat questions about established facts rather than targeting specific gaps.

### Types of gaps

Not all gaps are created equal. For the Excavator, gaps fall into several categories:

**Structural gaps**: Key components of the system/process that weren't mentioned at all. If someone describes a quoting process but never mentions how they handle changes after a quote is accepted, that's a structural gap.

**Decision gaps**: Decisions that are mentioned but not explained. "We use Xero" without any discussion of why, or what alternatives were considered.

**Exception gaps**: Happy-path descriptions with no mention of what happens when things go wrong. The exceptions are often where the real complexity lives.

**Constraint gaps**: Requirements or limitations that affect the design but weren't surfaced. Regulatory requirements, existing integrations, budget limitations, timeline constraints.

**Preference gaps**: What the user wants but hasn't articulated because they didn't know to state it. "I want it to be easy to use" is stated; "I need it to work on my phone while I'm on-site" is often unstated until specifically asked.

**Contradiction gaps**: Places where different parts of the input imply conflicting requirements. These are especially valuable to surface because the user may not be aware of the conflict.

### The schema approach to gap detection

The most systematic approach to gap detection: define what a "complete" knowledge representation would look like for the domain, then check the actual input against that schema. Missing fields = gaps.

This connects to the Excavator's primer function: if the Primer mode generates a structural map of what information is needed, and the Excavate mode processes actual input, then the Refine mode is literally the diff between expected and actual -- gap-bridging questions that target specific missing schema fields.

### Design implications

The Excavator's Refine mode should:

1. **Explicitly state what's known**: "Here's what I understand about your situation: [summary]"
2. **Explicitly state what's missing**: "I don't yet understand: [gap list]"
3. **Generate targeted questions for each gap**: Not generic probes but specific questions designed to fill specific holes.
4. **Prioritize gaps by impact**: Which missing information would most change the downstream output? Ask about those first.
5. **Distinguish types of gaps**: "I'm missing information about [structural gap]" vs "This seems contradictory: [contradiction gap] -- which is right?"

### Key citations

- [Bridging Information Gaps with Comprehensive Answers: Improving the Diversity and Informativeness of Follow-Up Questions](https://arxiv.org/abs/2502.17715) (2025).
- [Covering Uncommon Ground: Gap-Focused Question Generation for Answer Assessment](https://arxiv.org/html/2307.03319) (2023).
- [From Superficial to Deep: Integrating External Knowledge for Follow-up Question Generation](https://arxiv.org/html/2504.05801v1) (2025).
- [Requirements Elicitation Follow-Up Question Generation](https://arxiv.org/abs/2507.02858) (2025).

---

## 8. Rapport and Trust in AI Interactions

### The disclosure paradox

Research reveals a paradox: people sometimes disclose *more* to AI than to humans, but for different reasons than those that drive trust. A literature review on self-disclosure to conversational AI (2024) found that "chatbot conversations can contain as much self-disclosure as human-human conversations, likely due to their perceived anonymity and lack of judgment compared to more trusted human interlocutors."

This is important: **disclosure does not equal trust**. People may share freely with an AI because they don't care what it thinks, not because they trust it. For the Excavator, this distinction matters -- we want both disclosure (getting the information) AND trust (the user believing the output will be handled well).

### What builds trust in human-AI interaction

A systematic review of trust in AI chatbots (2025) identifies several factors:

**Competence demonstration**: The AI showing that it understands what you said. This is where active listening (Section 3) meets trust -- when the Excavator paraphrases accurately, it demonstrates competence, which builds trust.

**Reciprocal disclosure**: Research shows that "exposing users to AI self-disclosures, which include expressions of vulnerability, fosters a sense of intimacy and connection." For the Excavator, this might mean occasionally acknowledging its limitations: "I'm not sure I understand the technical details of [X] well enough -- can you explain it differently?"

**Ephemerality framing**: Users are more comfortable sharing when they perceive the conversation as ephemeral. This has design implications for how the Excavator presents itself and handles data.

**Avoiding the interrogation feeling**: There's a fine line between thorough elicitation and feeling interrogated. The research suggests that pacing, acknowledgment, and explaining why you're asking ("I'm asking about this because it'll help me generate better questions for your meeting") all reduce the interrogation feeling.

### Conversational grounding and common ground

Clark and Brennan's (1991) theory of conversational grounding provides the theoretical foundation for trust-building in dialogue. Their key concepts:

**Common ground**: The "mutual knowledge, mutual beliefs, and mutual assumptions" that conversation participants share. Successful communication requires continuously updating common ground.

**The grounding process**: Participants use a cycle of presentation and acceptance to establish shared understanding. The speaker presents information; the listener signals acceptance (or non-acceptance). This cycle repeats until both parties believe they share the same understanding.

**The principle of least collaborative effort**: "Participants try to minimize their collaborative effort to reach mutual understanding." It's often more efficient to present a provisional message and ask for confirmation than to try to produce a perfect message on the first attempt.

For the Excavator, this means:
- **Make your understanding explicit and checkable**: "Here's what I think you're saying: [summary]. Is that right?" -- This is a grounding move. It's more efficient than trying to perfectly parse the input silently.
- **Build common ground incrementally**: Don't try to understand everything at once. Establish understanding of one area, confirm it, then move to the next.
- **Signal when grounding fails**: "I'm not sure I follow -- when you say [X], do you mean [A] or [B]?" -- This is a clarification request, which is a repair mechanism for failed grounding.

### Conversational repair

Repair is what happens when communication breaks down. Research on dialogue repair in AI systems (2024) identifies several repair strategies:

- **Self-initiated repair**: The AI notices its own misunderstanding and corrects it.
- **Other-initiated repair**: The user signals that the AI misunderstood.
- **Third position repair**: The user responds based on the AI's misunderstanding, the AI detects the mismatch, and corrects course.

Current AI systems "significantly underperform compared to humans" at repair sequences -- particularly third-position repair, which requires detecting that a previous exchange went wrong even though neither party explicitly flagged it.

For the Excavator, repair capability is essential. When processing messy input, misunderstandings are guaranteed. The system should:
- **Check frequently**: Don't accumulate assumptions. Check understanding early and often.
- **Make it easy to correct**: "If I've misunderstood any of this, just tell me where I went wrong."
- **Handle correction gracefully**: When corrected, update the model and acknowledge the correction explicitly: "Got it -- so [X] is actually [Y]. Let me revise."

### Key citations

- [Self-disclosure to conversational AI: a literature review and emergent framework](https://link.springer.com/article/10.1007/s00779-024-01823-7) (2024). *Personal and Ubiquitous Computing*.
- [Trust in AI chatbots: A systematic review](https://dl.acm.org/doi/10.1016/j.tele.2025.102240) (2025). *Telematics and Informatics*.
- [Self-Disclosure to AI: The Paradox of Trust and Vulnerability](https://arxiv.org/html/2412.20564v1) (2024).
- Clark, H.H. & Brennan, S.E. (1991). [Grounding in communication](https://web.stanford.edu/~clark/1990s/Clark,%20H.H.%20_%20Brennan,%20S.E.%20_Grounding%20in%20communication_%201991.pdf). In *Perspectives on Socially Shared Cognition*. APA.
- [An analysis of dialogue repair in virtual assistants](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1356847/full) (2024). *Frontiers in Robotics and AI*.
- [A Benchmark to Assess Common Ground in Human-AI Collaboration](https://arxiv.org/html/2602.21337v1) (2026).

---

## 9. Multi-Session Elicitation

### The excavation lifecycle

The Prompt Excavator operates across a lifecycle: Primer (before the meeting) -> Meeting (human conducts) -> Excavate (process notes) -> Refine (follow-up questions) -> possibly multiple Refine cycles. This is inherently multi-session. What needs to persist across sessions, and how?

### Memory architecture

Research on AI agent memory systems (2024-2025) identifies three layers of memory that map to the Excavator's needs:

1. **Session memory** (current conversation state): What's been discussed in this interaction, current focus, active questions.
2. **User/project memory** (persists across sessions): What's been established about this user's domain, their requirements, their constraints, their preferences. This is the accumulated knowledge graph.
3. **Institutional memory** (domain knowledge): What the Excavator knows about the domain in general -- distinct from what it knows about this specific user's situation.

Several recent frameworks address this:
- **Memoria** (2025): Integrates "dynamic session-level summarization and a weighted knowledge graph-based user modeling engine that incrementally captures user traits, preferences, and behavioral patterns."
- **Mem0** (2025): "Dynamically captures, organizes, and retrieves salient information from ongoing conversations to maintain coherent reasoning across extended conversations across different sessions."

### What needs to persist

For the Excavator specifically:

**Known facts**: Established information about the user's situation -- their domain, processes, tools, constraints, preferences.

**Confidence levels**: How certain are we about each fact? Some things were stated clearly; others were inferred or are based on a single mention.

**Open questions**: What gaps have been identified but not yet filled? What contradictions remain unresolved?

**Conversation history (compressed)**: Not the full transcript, but a structured summary of what was discussed, what was decided, what was deferred.

**User model**: Expertise level, communication style preferences, areas of deep knowledge vs areas of uncertainty.

### Knowledge state tracking

The most important tracking challenge: distinguishing between what's **known**, what's **assumed**, and what's **unknown**. Over multiple sessions, assumptions can harden into "facts" if they're never checked. The Excavator should maintain explicit tagging:

- **Stated**: The user directly told us this.
- **Inferred**: We concluded this from what the user said, but they didn't say it directly.
- **Assumed**: We're operating on this assumption, but it hasn't been confirmed.
- **Unknown**: We know we don't know this.
- **Contradicted**: Information from different sessions conflicts.

Research shows that "knowledge update scenarios involve handling cases where newer information contradicts or supersedes older facts" -- this is a known challenge in multi-session AI systems. The Excavator should handle this explicitly: "In our earlier conversation, you mentioned [X]. Today you've said [Y], which seems different. Has something changed, or did I misunderstand earlier?"

### Session boundaries and the cognitive stance framework

This is where the cognitive stance framework applies directly. Each Excavator session has its own cognitive mode:

- **Primer**: Divergent exploration of the domain space. Output: questions and a structural map.
- **Excavate**: Convergent processing of raw input into structured findings. Output: facts, gaps, ambiguities.
- **Refine**: Targeted investigation of specific gaps. Output: answers to specific questions, updated knowledge state.

The handoff between sessions should follow the trust chain principles: compress into structured form, strip cognitive residue. A Refine session shouldn't carry the exploratory tone of the Primer -- it should receive structured findings and target specific gaps.

### Design implications

- The Excavator needs a persistent knowledge store across sessions -- not just conversation history but a structured representation of what's known, unknown, and uncertain.
- Each session should begin with a grounding check: "Here's what I understand about your situation so far: [summary]. Has anything changed?"
- The knowledge store should explicitly tag confidence levels and flag when assumptions haven't been verified.
- Session transitions should be clean: compress the previous session's output into structured form before starting the next session.

### Key citations

- [Memoria: A Scalable Agentic Memory Framework for Personalized Conversational AI](https://arxiv.org/html/2512.12686v1) (2025).
- [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/pdf/2504.19413) (2025).
- [AI Meets Brain: A Unified Survey on Memory Systems from Cognitive Neuroscience to Autonomous Agents](https://arxiv.org/html/2512.23343v1) (2025).
- [Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey](https://arxiv.org/pdf/2503.22458) (2025).
- [How to Ensure Consistency in Multi-Turn AI Conversations](https://www.getmaxim.ai/articles/how-to-ensure-consistency-in-multi-turn-ai-conversations/).

---

## 10. Domain Adaptation

### The range problem

The Excavator must work for:
- A builder discussing quoting and project management
- A bookkeeper discussing invoicing and BAS lodgement
- An engineer discussing RAG pipeline architecture
- A retail shop owner discussing inventory and POS systems
- A therapist discussing client intake workflows

These domains have radically different vocabularies, process complexities, stakeholder structures, and user expertise levels. How does a single agent adapt?

### Expertise-level-based adaptation

Research on domain adaptation in conversational AI (2025) provides a framework:

**Low domain knowledge**: Infrequent and superficial engagement with the domain. Limited vocabulary. Describes goals in everyday language. Needs more guidance, more explanation, simpler questions.

**Medium domain knowledge**: Familiar with key concepts and some terminology. Can describe their workflows but may not know alternative approaches. Can engage with moderately technical questions.

**High domain knowledge**: Frequent, expert-level engagement. Refined understanding, precise vocabulary. Prefers efficiency over explanation. Can handle -- and benefits from -- technical depth.

The Excavator should adapt along multiple dimensions:

**Question complexity**: For a non-technical user, ask process questions ("Walk me through what happens when a new job comes in"). For a technical user, ask structural questions ("What's the current data flow between your CRM and your invoicing system?").

**Explanation depth**: For a non-technical user, explain why you're asking what you're asking. For a technical user, skip the preamble and get to the point.

**Output format**: For a non-technical user, produce narrative summaries with clear language. For a technical user, produce structured specifications with precise terminology.

**Probing strategy**: For a non-technical user, probe through concrete examples ("Can you walk me through the last time this happened?"). For a technical user, probe through edge cases and constraints ("What happens when the API rate limit is exceeded?").

### Domain-independent question patterns

Despite the range of domains, certain question patterns work universally:

1. **The workflow question**: "Walk me through [process] from start to finish." Works for builders (quoting process), bookkeepers (month-end close), engineers (deployment pipeline).

2. **The exception question**: "What happens when something goes wrong?" Universally valuable -- the exceptions reveal the real complexity.

3. **The workaround question**: "Are there things you do that aren't part of the 'official' process?" Surfaces tacit knowledge and hidden requirements.

4. **The frustration question**: "What's the most annoying part of this?" Identifies pain points that drive requirements.

5. **The aspiration question**: "If you could wave a magic wand, what would be different?" Surfaces unstated goals.

6. **The stakeholder question**: "Who else is affected by this?" Identifies hidden requirements from other parties.

7. **The constraint question**: "What can't change?" Identifies fixed points that the solution must work around.

### Domain-specific adaptation strategy

Rather than building domain knowledge into the Excavator itself, the adaptation strategy should be:

1. **Start with universal questions** that work in any domain.
2. **Listen for domain signals** in the responses -- terminology, process descriptions, complexity indicators.
3. **Adapt follow-up questions** based on what you learn about the domain from the user's own language.
4. **Build a domain model incrementally** from the user's responses rather than from pre-built templates.

This approach avoids the "one of the most common mistakes: applying a generic framework without adapting it to the actual problem." The Excavator should let the domain emerge from the conversation rather than imposing a pre-built domain model.

### Key citations

- [Know Your Users! Estimating User Domain Knowledge in Conversational Recommenders](https://arxiv.org/abs/2512.13173) (2025).
- [Identifying users' domain expertise from dialogues](https://dl.acm.org/doi/pdf/10.1145/3450614.3461683) (2021).
- [LLMREI: Automating Requirements Elicitation Interviews with LLMs](https://arxiv.org/html/2507.02564v1) (2025).
- [Teaching Agile Requirements Engineering: A Stakeholder Simulation with Generative AI](https://arxiv.org/html/2603.12925v1) (2025).

---

## 11. Adjacent Fields and Unexpected Connections

### Motivational Interviewing and the OARS Framework

Motivational interviewing (MI) is a clinical technique designed to help people articulate and resolve ambivalence about change. Its core framework, OARS, maps remarkably well to the Excavator's needs:

- **Open-ended questions**: Questions that can't be answered with yes/no and "challenge clients to think more deeply and invite them to share experiences freely."
- **Affirmations**: Acknowledging strengths, efforts, and past successes. "Help to build the person's hope and confidence."
- **Reflective listening**: "Based on careful listening and trying to understand what the person is saying, by repeating, rephrasing or offering a deeper guess about what the person is trying to communicate."
- **Summarizing**: Condensing and reflecting back what's been shared.

The **Elicit-Provide-Elicit** (EPE) technique from MI is particularly relevant:
1. **Elicit**: Find out what the client already knows. Be curious, enquire, clarify.
2. **Provide**: Fill in gaps or explore misconceptions. Short bursts of information.
3. **Elicit**: Check their understanding of what you just provided. Gauge comprehension and emotional response.

The EPE framework directly applies to the Excavator's interaction pattern: first understand what the user knows (elicit), then provide structured findings or questions (provide), then check if the output matches what they intended (elicit). This prevents the "irrelevant lecture" problem -- maintaining involvement and rapport while uncovering useful information.

A key MI principle: "You are not the expert or authority on the client's life, but rather a partner." This epistemic stance -- the Excavator as partner in discovery, not authority on the user's domain -- is critical for the right conversational posture.

### Information Foraging Theory

Pirolli and Card's information foraging theory (1999) applies optimal foraging concepts to information seeking. The central concept: **information scent** -- cues in the environment that indicate the likelihood of finding valuable information in a given direction.

Applied to conversational elicitation:
- **Strong scent**: When a user mentions something that suggests rich information nearby ("We had a really weird situation last month with a client's billing"), the Excavator should follow that scent -- it's likely to surface valuable, specific knowledge.
- **Weak scent**: When responses are generic or formulaic ("It works pretty well"), there may be nothing to find or the user may need a different type of prompt to open up.
- **Patch exploration**: Information foraging theory says foragers should exploit a rich patch until the rate of return drops, then move to a new patch. For the Excavator: keep probing a productive topic until the responses become repetitive, then shift to a new area.

This provides a principled framework for deciding when to probe deeper vs when to move on -- one of the hardest judgment calls in interviewing.

### Requirements Elicitation from Software Engineering

The requirements elicitation literature provides battle-tested frameworks for exactly what the Excavator does: extract from stakeholders what a system needs to do.

**LLMREI** (2025): An LLM-based system designed to "conduct requirements elicitation interviews with minimal human intervention, aiming to reduce common interviewer errors and improve the scalability of requirements elicitation." The system builds on a framework of "common interviewer mistake types" -- an empirically grounded list of things that go wrong in elicitation interviews:

- Asking leading questions
- Assuming shared understanding
- Missing follow-up opportunities
- Jumping to solutions before understanding the problem
- Not probing exceptions and edge cases

A separate study (2025) found that "LLM-generated [follow-up] questions outperform human-authored questions when guided by common mistakes types" -- suggesting that an AI specifically trained to avoid common interviewer mistakes can produce better questions than untrained human interviewers.

The requirements engineering field also emphasizes that **only 2% of practitioners believe AI could handle elicitation independently without human intervention** -- the human remains essential. This supports the Excavator's design as a tool that supports human elicitation rather than replacing it.

### Vygotsky's Zone of Proximal Development

Vygotsky's ZPD -- the space between what a learner can do alone and what they can do with guidance -- has a surprising application to elicitation. The Excavator isn't teaching, but it is helping users articulate knowledge that's at the edge of their explicit awareness:

- **What the user can articulate independently**: Their explicit knowledge, easily stated facts and preferences.
- **What the user can articulate with scaffolding**: Tacit knowledge, implicit preferences, unstated assumptions -- things they know but can't easily express without the right questions.
- **What the user can't articulate even with help**: Deep tacit knowledge that may require observation or experimentation to surface.

The Excavator's value lies in the middle zone -- helping people say what they know but haven't put into words. This frames the Excavator as a scaffold: providing the structure that helps the user express knowledge they couldn't articulate without support.

### Cognitive Task Analysis and AI-Augmented Elicitation

Recent work (2025) explores using AI to augment traditional CTA methods:

> "Traditional CTA is time-intensive; interviews and transcript analyses demand substantial expert and analyst effort. In response, researchers have begun leveraging AI technologies, including NLP and machine learning, to streamline interviews, extract key concepts, and automate knowledge representation via ontologies and knowledge graphs, enhancing CTA scalability in fast-evolving domains."

The Excavator is essentially an AI-augmented CTA tool. It automates the knowledge extraction and representation steps while keeping the human in the loop for the knowledge elicitation step. The primer mode prepares for CTA-style interviews; the excavate mode performs the analysis step; the refine mode generates additional probes.

### The Dreyfus Model Applied to Users

The Dreyfus skill model (novice -> advanced beginner -> competent -> proficient -> expert) applies not just to the AI's task (as discussed in the cognitive stance reference) but to the *users* of the Excavator:

- **Novice users** (first time using the Excavator): Need explicit guidance about what to provide, in what format, and why. The system should explain itself.
- **Competent users** (have used it a few times): Understand the process, can provide more targeted input, benefit from less scaffolding and more efficiency.
- **Expert users** (AI engineers who understand what's happening under the hood): Want direct control, minimal hand-holding, ability to customize the output format.

The Excavator should adapt not just to the user's domain expertise (Section 10) but to their *tool expertise* -- how familiar they are with the elicitation process itself.

### DialogLab and Conversational Design Tools

DialogLab (2025) is a tool for "authoring, simulating, and testing dynamic" dialogue systems. The key insight from this work: dialogue design benefits enormously from being able to simulate conversations before deploying them. For the Excavator, this suggests that the Primer mode could include a simulated conversation -- "Here's how a typical exchange with this type of domain expert might go" -- giving the consultant a mental rehearsal before the actual meeting.

### Key citations

- Miller, W.R. & Rollnick, S. (2013). *Motivational Interviewing: Helping People Change*. Guilford Press.
- [OARS Motivational Interviewing](https://www.relias.com/blog/oars-motivational-interviewing) -- Relias.
- [Elicit-Provide-Elicit in Motivational Interviewing](https://www.relias.com/blog/elicit-provide-elicit-motivational-interviewing) -- Relias.
- Pirolli, P. & Card, S. (1999). Information Foraging. *Psychological Review*, 106(4), 643-675.
- [Information Foraging: A Theory of How People Navigate on the Web](https://www.nngroup.com/articles/information-foraging/) -- Nielsen Norman Group.
- [LLMREI: Automating Requirements Elicitation Interviews with LLMs](https://arxiv.org/html/2507.02564v1) (2025).
- [Requirements Elicitation Follow-Up Question Generation](https://arxiv.org/abs/2507.02858) (2025).
- [DialogLab: Authoring, Simulating, and Testing Dynamic Dialogue](https://erzhenh.com/pdfs/uist25_DialogLab.pdf) (2025).
- Dreyfus, H.L. & Dreyfus, S.E. (1986). *Mind Over Machine: The Power of Human Intuition and Expertise*. Free Press.
- Vygotsky, L.S. (1978). *Mind in Society: The Development of Higher Psychological Processes*. Harvard University Press.
- [Scaffolding Human Champions: AI as a More Competent Other](https://link.springer.com/article/10.1007/s42087-022-00304-8) (2022). *Human Arenas*.

---

## 12. Synthesis: Design Patterns for the Excavator

This section pulls threads from the research above into design patterns that the downstream prompt writer can use.

### Pattern 1: The Elicit-Check-Deepen Loop

From active listening, conversational grounding, and the EPE framework:

```
Elicit   ->  Ask an open question
Check    ->  Paraphrase/summarize what you heard, ask for confirmation
Deepen   ->  Based on confirmation (or correction), probe deeper
```

This loop serves three functions simultaneously: it gathers information (elicit), builds trust and common ground (check), and increases specificity (deepen). Every interaction in Refine mode should follow this pattern. In Excavate mode, the "check" step is the structured summary that the user reviews.

### Pattern 2: The Information Scent Tracker

From information foraging theory:

When processing responses (in any mode), the Excavator should track "scent" -- signals of rich information nearby:
- Specific incidents ("last month we had a situation where...")
- Emotional language ("the most frustrating thing is...")
- Hedging on specifics ("usually it works, but sometimes...")
- Named exceptions ("except when [unusual case]...")
- Contradictions with earlier statements

Strong scent = probe deeper. Weak scent = move to a new topic. This replaces rigid interview scripts with adaptive exploration.

### Pattern 3: The Gap Schema

From gap detection research and requirements elicitation:

Maintain an explicit model of what you know and what you don't:

```
Known        ->  Stated facts, confirmed understanding
Inferred     ->  Conclusions drawn from stated facts
Assumed      ->  Operating assumptions, unconfirmed
Unknown      ->  Known gaps, things you know you don't know
Contradicted ->  Conflicting information from different sources
```

Each item in the model has a source (which session, which statement) and a confidence level. Gap detection = checking the model against a domain-appropriate completeness schema. Follow-up question generation = targeting Unknown and Contradicted items.

### Pattern 4: The Expertise Adapter

From adaptive dialogue management and domain adaptation research:

Detect expertise level through:
- Vocabulary sophistication (everyday language vs domain jargon vs technical specification language)
- Response structure (narrative vs structured vs specification-like)
- Response length and detail level
- Proactive information volunteering (experts anticipate what you'll need)

Adapt along:
- Question complexity (process questions for novices, structural/constraint questions for experts)
- Explanation depth (explain the why for novices, skip to the what for experts)
- Probe style (concrete examples for novices, edge cases and constraints for experts)
- Output format (narrative for novices, structured specifications for experts)

### Pattern 5: The Primer Generator

From ACTA, CDM, and consulting preparation:

Generate primer questions in five categories:
1. **Process**: "Walk me through [X] from start to finish"
2. **Decisions**: "Where are the key decision points? What drives those decisions?"
3. **Exceptions**: "What goes wrong? What's the weirdest thing that's happened?"
4. **Tacit knowledge**: "What would someone new to this miss? When do you just 'know' something?"
5. **Aspirations**: "What would make this better? What do you wish were different?"

Include meta-guidance for the interviewer:
- Start broad, narrow progressively (funnel technique)
- Reflect back what you hear before probing deeper (active listening)
- Follow the energy -- if the expert lights up on a topic, stay there
- Don't lead -- ask what IS, not what SHOULD BE

### Pattern 6: The Structured Excavation Output

From data stance theory and the trust chain:

Excavate mode output should include:
1. **Facts** (descriptive, high confidence): What was clearly stated
2. **Inferences** (classified, medium confidence): What the Excavator concluded from the facts
3. **Gaps** (structural): What's missing from the picture
4. **Ambiguities** (flagged): What could mean multiple things
5. **Contradictions** (flagged): Where the input conflicts with itself
6. **Questions** (generated): Specific follow-up questions for each gap and ambiguity

The output should be primarily descriptive and classified, not evaluated. Evaluation is the downstream prompt writer's job.

### Pattern 7: The Session Boundary Protocol

From multi-session research and the cognitive stance framework:

At the start of each session:
1. Load the persistent knowledge state
2. Summarize what's known: "Here's my current understanding..."
3. Check for changes: "Has anything changed since we last spoke?"
4. State the session's purpose: "Today we're focusing on [X]"

At the end of each session:
1. Summarize what was learned
2. Update the knowledge state (facts, inferences, gaps, confidence levels)
3. Identify next steps: "Here's what I still need to understand..."
4. Compress into structured form (strip cognitive residue from the session)

---

## 13. Cognitive Mode Implications

### How the Excavator's modes map to the cognitive stance framework

Each Excavator mode has a primary cognitive posture:

**Primer mode**: Divergent exploration. The Excavator is investigating a domain it doesn't know, generating questions that open space rather than close it. The epistemic stance should be: "I'm discovering what this domain is about -- what matters, what's complex, where the interesting questions are."

Incompatible mixing to avoid: Don't evaluate or prioritize questions during generation. Generate broadly first, then compress/prioritize as a separate step.

**Excavate mode**: Convergent structuring with divergent thread-following. The Excavator is processing raw input into structured form -- but it also needs to follow interesting threads (information scent) and flag unexpected patterns. The epistemic stance should be: "I'm organizing what was said, noticing what's interesting, and identifying what's missing."

Incompatible mixing to avoid: Don't generate solutions or recommendations during excavation. The Excavator should surface problems and gaps, not solve them. Evaluation of what matters should be light-touch (structural completeness checking), not heavy (prioritization or recommendation).

**Refine mode**: Targeted investigation. The Excavator is pursuing specific gaps identified by previous modes. The epistemic stance should be: "I know what I'm looking for -- these specific gaps -- and I need precise answers."

Incompatible mixing to avoid: Don't reopen broad exploration during refinement. Stay focused on the identified gaps. If the refinement conversation reveals new areas to explore, flag them for a new Primer cycle rather than pursuing them in the Refine session.

### The pipeline implication

The three modes map to a natural pipeline:

```
Primer (divergent) -> [meeting happens] -> Excavate (convergent + light divergent) -> Refine (targeted investigation)
```

The handoffs between modes should follow the trust chain principles:
- Primer output to the consultant: questions + domain orientation (structured, lens-like)
- Meeting notes to Excavate: raw input (descriptive data stance, not pre-processed)
- Excavate output to Refine: structured findings with explicit gaps (classified data stance)
- Refine output to the prompt writer: updated knowledge state (comprehensive, but descriptive/classified, not evaluated)

Each transition compresses and structures. No mode carries the cognitive residue of the previous mode into the next.

### Where mode contamination could hurt

The biggest risk: the Excavator starting to generate prompt specifications (convergent, solution-oriented) before the excavation is complete (divergent, problem-understanding). If the Excavator shifts too early from "what does this person need?" to "how should we build the prompt?", it will generate prompts shaped by early, incomplete understanding.

The fix: strict separation between excavation (understanding the problem) and prompt writing (solving the problem). The Excavator's job ends with a structured understanding of what the user needs. The Prompt Writer's job begins with that structured understanding. The handoff between them is the cognitive boundary.

---

## Summary of Key Frameworks Referenced

| Framework | Source | Application to Excavator |
|-----------|--------|-------------------------|
| OARS / Motivational Interviewing | Miller & Rollnick | Interaction posture: open questions, affirmations, reflection, summarizing |
| Elicit-Provide-Elicit | MI framework | Interaction loop: understand first, share second, check third |
| Funnel Technique | Qualitative research | Question sequencing: broad to narrow within each topic |
| Paul-Elder Socratic Taxonomy | Paul & Elder (2006) | Question type classification for Primer mode |
| ACTA / Knowledge Audit | Militello & Hutton (1998) | Tacit knowledge probe categories for Primer mode |
| Critical Decision Method | Klein et al. (1986) | Decision-point probing for complex domains |
| Information Foraging | Pirolli & Card (1999) | When to probe deeper vs move on |
| Conversational Grounding | Clark & Brennan (1991) | Trust-building through explicit understanding checks |
| Gricean Maxims | Grice (1975) | Evaluating response quality and detecting gaps |
| Information-Gap-Driven QG | (2025) | Systematic gap detection via hypothetical completeness |
| Expression Gap / Nous | (2025) | AI that probes to reduce uncertainty about user intent |
| AMIE Dialogue Framework | Google Research (2024) | State-aware, phase-progressing dialogue architecture |
| Zone of Proximal Development | Vygotsky (1978) | The Excavator as scaffold for articulating tacit knowledge |
| Data Stance | Cognitive stance framework | Output should be descriptive/classified, not evaluated |
| Dreyfus Skill Model | Dreyfus & Dreyfus (1986) | Adapting to both domain expertise and tool expertise |
