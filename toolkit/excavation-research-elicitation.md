# Elicitation Methodologies for the Prompt Excavator

**What this is**: A comprehensive research survey of knowledge elicitation, requirements gathering, coaching, design thinking, and related methodologies — assembled to inform the design of an AI agent that helps people articulate what they need from AI systems.

**What this supports**: The Prompt Excavator — an agent that operates in three modes (Primer, Excavate, Refine) to help everyone from tradies to technical architects surface tacit knowledge about their work processes and convert it into well-designed AI prompts and pipelines.

**How to read this**: Each section covers a domain, its key methods, how those methods apply to our specific problem, and what we can borrow. The connections between sections are where the real design insights live — the methodologies overlap and reinforce each other in ways that aren't obvious from within any single discipline.

---

## 1. Cognitive Task Analysis (CTA) — The Deep Methods

CTA is the backbone discipline for what we're building. It was designed specifically to surface the tacit knowledge that experts can't articulate — the 40-70% of key steps, cues, and decision strategies that experts routinely omit when teaching (Crandall, Klein & Hoffman, 2006). Our existing research base covers CTA at a high level (see `cognitive-science-research.md`, Section 5). This section goes deeper into the specific methods and their variants.

### 1.1 Critical Decision Method (CDM)

**What it is**: A retrospective interview technique developed by Klein, Calderwood, and Clinton-Cirocco (1986). The interviewer asks the expert to recall a specific, challenging incident from their work and then systematically probes that incident through multiple "sweeps," each targeting different cognitive elements.

**The sweep structure**:
1. **Incident identification and timeline**: The expert narrates the incident from beginning to end. The interviewer establishes a timeline of key events and decision points.
2. **Decision point identification**: The interviewer and expert together identify the critical moments where the expert had to make a judgment call, assess a situation, or choose a course of action.
3. **Deepening probes**: For each decision point, the interviewer asks: What cues did you notice? What options did you consider? What knowledge or experience did you draw on? What would a novice have missed? What would have happened if you'd made a different call?
4. **"What if" probes**: The interviewer introduces hypothetical variations — what if this cue had been different? What if you'd had less information? What if a novice had been in your place?

**Why CDM is powerful for our context**: CDM works by grounding the conversation in a specific, concrete event. Experts can't talk abstractly about their expertise (the knowledge is compiled into automatic routines), but they can relive a specific incident and notice — often for the first time — what they actually did and why. The specificity of the anchor forces de-compilation of automated knowledge.

**Application to the Prompt Excavator**: The Primer mode should generate CDM-style probes. Instead of asking "How do you handle client quotes?" (abstract — the expert will give a surface answer), it should prepare questions like "Tell me about a recent quote that was tricky. Walk me through what happened." Then the Excavate mode processes the resulting narrative to extract decision points, cues, and strategies that the expert revealed without realising it.

**Limitations**: CDM requires a skilled interviewer who can read the expert's responses and decide in real time where to probe deeper. It's time-intensive (60-90 minutes per incident). It depends on the expert recalling a suitable incident — and memory is reconstructive, not reproductive. The expert's recall is shaped by what they believe is important, which may not include the tacit elements we most need.

**Key citations**:
- Klein, G., Calderwood, R., & Clinton-Cirocco, A. (1986). Rapid decision making on the fire ground. *Proceedings of the Human Factors Society*, 30, 576-580.
- Klein, G., Calderwood, R., & Macgregor, D. (1989). Critical decision method for eliciting knowledge. *IEEE Transactions on Systems, Man, and Cybernetics*, 19(3), 462-472.
- Wong, B. L. W. (2004). Critical decision method data analysis. In D. Diaper & N. Stanton (Eds.), *The Handbook of Task Analysis for Human-Computer Interaction*. Lawrence Erlbaum Associates.

### 1.2 Applied Cognitive Task Analysis (ACTA)

**What it is**: A streamlined CTA method developed by Militello and Hutton (1998) specifically to make CTA accessible to practitioners who aren't trained cognitive psychologists. ACTA has three structured components:

1. **Task Diagram Interview**: The expert identifies the major steps in the task and flags which steps require difficult cognitive work (judgment, decision-making, assessment). This creates a map of where the cognitive complexity lives.
2. **Knowledge Audit**: For each cognitively demanding step, the interviewer probes across five categories: (a) diagnosing/recognising situations, (b) predicting future events, (c) noticing anomalies, (d) planning and adapting, (e) using workarounds or tricks of the trade.
3. **Simulation Interview**: The expert walks through a challenging scenario (real or constructed), and the interviewer probes at each action point: What are you noticing? What matters here? What are you trying to achieve?

**Why ACTA matters for our context**: ACTA was explicitly designed for non-specialists to use. Its structured categories give the interviewer (or, in our case, the AI agent) a scaffold for probing that doesn't require deep expertise in the domain being elicited. The five knowledge audit categories are particularly useful — they're domain-independent probes that surface tacit knowledge regardless of whether the expert is a builder, a bookkeeper, or a security architect.

**Application to the Prompt Excavator**: The ACTA structure maps almost directly to our three modes. The Task Diagram Interview is the Primer (identify what's cognitively complex about the work). The Knowledge Audit and Simulation Interview are the Excavate (systematically probe the complexity). The structured output format is what the Refine mode iterates on.

The five knowledge audit categories should be adapted as question generators:
- **Diagnosing**: "How do you know when [situation] is actually [X] and not [Y]?"
- **Predicting**: "When you see [early signal], what do you expect to happen next?"
- **Anomalies**: "What would make you stop and look more carefully?"
- **Adapting**: "When the standard approach doesn't work, what do you do instead?"
- **Tricks of the trade**: "What's something you do that you'd never find in a textbook?"

**Limitations**: ACTA trades depth for accessibility. It won't surface the deepest tacit knowledge — the perceptual cues and intuitive pattern-matching that CDM gets at through repeated sweeps. For many of our users, this trade-off is correct (we don't need firefighter-level depth for a bookkeeper's invoicing process). For complex technical work, we may need CDM-level depth.

**Key citations**:
- Militello, L. G. & Hutton, R. J. B. (1998). Applied cognitive task analysis (ACTA): A practitioner's toolkit for understanding cognitive task demands. *Ergonomics*, 41(11), 1618-1641.

### 1.3 Think-Aloud Protocol

**What it is**: The expert performs the task while verbalising their thought process. Developed by Ericsson and Simon (1984, 1993), it comes in two forms:
- **Concurrent think-aloud**: Verbalise while doing. Captures real-time cognitive processes but may alter them.
- **Retrospective think-aloud**: Do first, then describe what you were thinking. Avoids alteration but introduces memory distortion.

**Application to our context**: We can approximate think-aloud by asking users to describe their work as if they're doing it right now. "Imagine you just got a call from a new client who wants a bathroom renovation. Walk me through what you do, step by step — including the stuff that happens in your head." This is essentially a simulated concurrent think-aloud.

The Excavate mode could process recordings or notes from actual work sessions where the expert narrated what they were doing. This is closer to genuine think-aloud than any interview-based method.

**Limitations**: Think-aloud works best for procedural tasks with a clear sequence. It's weaker for judgment-heavy work where the expert's reasoning is pattern-based rather than sequential. A builder assessing structural integrity doesn't think "Step 1, Step 2" — they look and know. Think-aloud may force a sequential rationalisation of what is actually a holistic perceptual judgment.

**Key citations**:
- Ericsson, K. A. & Simon, H. A. (1993). *Protocol Analysis: Verbal Reports as Data* (revised ed.). MIT Press.

### 1.4 Concept Mapping / Knowledge Mapping Techniques

**What it is**: Rather than eliciting through interview, the expert constructs a visual representation of their knowledge. Concept maps (Novak & Canas, 2008) show concepts as nodes and relationships as labelled links. Knowledge maps add layers for procedures, decisions, and contextual factors.

**Application to our context**: For users who struggle with verbal articulation (many tradespeople communicate better through doing than talking), a guided concept mapping exercise could work: "What are the main things you have to think about when quoting a job? Let's map them out." The agent could build the map progressively, showing it back to the user and asking "What connects to what? What am I missing?"

This is particularly useful in the Refine mode — after initial excavation, showing the user a structured representation of what was captured and asking them to validate, correct, and extend it.

**Limitations**: Concept mapping requires a visual interface, which constrains the agent's modality. It also requires the expert to think abstractly about their knowledge structure, which is exactly the thing tacit knowledge resists. Works better as a refinement tool than a primary elicitation tool.

**Key citations**:
- Novak, J. D. & Canas, A. J. (2008). The theory underlying concept maps and how to construct and use them. Technical Report IHMC CmapTools 2006-01 Rev 01-2008, Florida Institute for Human & Machine Cognition.

### 1.5 Repertory Grid Technique

**What it is**: Derived from George Kelly's Personal Construct Theory (1955), the repertory grid technique elicits the constructs (dimensions of judgment) that an expert uses to discriminate between elements (cases, objects, situations) in their domain. The expert is presented with triads of elements and asked "In what way are two of these alike and different from the third?" The resulting distinctions reveal the expert's personal construct system — the implicit dimensions along which they perceive and evaluate their world.

**Why this is relevant**: Experts make distinctions that novices can't see. A master builder looks at a site and sees things that a homeowner doesn't — load paths, drainage implications, soil conditions, access constraints. These distinctions are the expert's construct system, and the repertory grid is one of the few techniques specifically designed to surface it.

**Application to the Prompt Excavator**: We can use a lightweight version in the Excavate mode. Instead of formal triads, the agent could ask: "Think of a job that went really smoothly and one that was a nightmare. What was different about them?" The contrast between cases forces the expert to articulate the dimensions that matter — the constructs they use to assess situations — without requiring them to name those dimensions abstractly.

This is particularly powerful for the "invisible expertise" problem. A bookkeeper who "just knows" when something's wrong with the accounts is using constructs (pattern deviations, unusual ratios, timing anomalies) that they've never named. Contrastive questioning makes them nameable.

**Limitations**: The formal repertory grid technique is cumbersome and feels clinical. Our adaptation needs to feel conversational, not like a psychology experiment.

**Key citations**:
- Kelly, G. A. (1955). *The Psychology of Personal Constructs*. Norton.
- Fransella, F., Bell, R., & Bannister, D. (2004). *A Manual for Repertory Grid Technique* (2nd ed.). Wiley.

### 1.6 Cognitive Work Analysis (CWA)

**What it is**: A comprehensive framework developed by Vicente (1999) and extended by others, CWA analyses work systems at five levels:
1. **Work domain analysis**: What are the purposes, functions, and physical constraints of the system?
2. **Control task analysis**: What decisions need to be made and what information is needed?
3. **Strategies analysis**: What strategies could achieve the control tasks?
4. **Social organisation analysis**: How is work distributed across people and teams?
5. **Worker competencies analysis**: What competencies are needed?

CWA differs from CTA in a crucial way: CTA captures *how experts currently do the work*, while CWA maps *the constraints and possibilities of the work domain itself*. CWA is formative (what could be) rather than descriptive (what is).

**Application to our context**: CWA's formative orientation is relevant because we're not just documenting how people work — we're designing how AI could support that work. The work domain analysis (level 1) is particularly useful: understanding the constraints, purposes, and affordances of a domain tells us where AI assistance would actually help, not just where the expert says they want help (experts often misidentify their own bottlenecks).

The Primer mode could use CWA-style questions: "What are you ultimately trying to achieve? What constraints do you have to work within? What information do you need to make decisions?" These are domain-mapping questions, not task-mapping questions — and the distinction matters.

**Limitations**: Full CWA is extremely resource-intensive (months, not hours). We'd use it as a conceptual lens rather than a literal methodology.

**Key citations**:
- Vicente, K. J. (1999). *Cognitive Work Analysis: Toward Safe, Productive, and Healthy Computer-Based Work*. Lawrence Erlbaum Associates.
- Naikar, N. (2013). *Work Domain Analysis: Concepts, Guidelines, and Cases*. CRC Press.

### 1.7 Cognitive Apprenticeship

**What it is**: Collins, Brown, and Newman (1989) proposed cognitive apprenticeship as a model where experts make their thinking visible to learners through six methods: modelling (expert demonstrates while thinking aloud), coaching (expert provides hints and scaffolding while learner attempts), scaffolding (providing support structures that are gradually removed), articulation (learner explains their reasoning), reflection (learner compares their process to the expert's), and exploration (learner sets their own goals and solves novel problems).

**Application to our context**: The modelling and articulation components are directly relevant. In the Excavate mode, we're essentially asking the expert to model their process (show us what they do and why) and articulate their reasoning (explain decisions that are normally automatic). The coaching component maps to the Refine mode — the agent provides scaffolding that helps the expert articulate increasingly specific knowledge.

The key insight from cognitive apprenticeship is that **making thinking visible requires a social process**. The expert doesn't introspect in isolation — they demonstrate, explain, and respond to questions. The AI agent needs to be a conversational partner that creates the conditions for the expert to make their thinking visible, not a questionnaire that extracts answers.

**Key citations**:
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), *Knowing, Learning, and Instruction: Essays in Honor of Robert Glaser*. Lawrence Erlbaum Associates.

### 1.8 The Expert-Novice Contrast Method

**What it is**: Rather than eliciting from an expert alone, this method has both an expert and a novice perform the same task, then analyses the differences. The gaps between expert and novice performance reveal the tacit knowledge that expertise has compiled away.

**Application to our context**: We can simulate this by asking the expert to imagine how a new hire or apprentice would approach the task. "If you had a brand new person starting tomorrow and they had to do this job, what would they get wrong?" This question is remarkably effective at surfacing tacit knowledge because experts can see novice mistakes much more easily than they can describe their own expertise. The mistake reveals the knowledge by its absence.

Related: "What took you years to learn that you now do without thinking?" This frames tacit knowledge not as something to introspect about but as something that was once conscious and became automatic — a framing that makes it easier for the expert to access.

**Application to Prompt Excavator**: Both the Primer mode (generating these contrastive questions) and the Excavate mode (recognising when the expert is describing novice-expert gaps in their narrative) should leverage this.

### 1.9 Less Common CTA Methods

**Teachback method**: The elicitor attempts to perform the task based on the expert's instructions, with the expert correcting and elaborating. The errors reveal gaps in the initial elicitation. Not directly usable for an AI agent (we can't perform physical tasks), but the principle — having the expert evaluate whether their explanation is sufficient — translates to: "Based on what you've told me, here's how I'd explain your process to someone. What did I get wrong?"

**Cognitive walkthrough**: Originally from usability engineering (Wharton et al., 1994), this method walks through a task step by step, asking at each step: Would the user know what to do? Would the correct action be visible? Would the user associate the correct action with the desired effect? Would the user see progress? Adaptable to our context as a way of walking through work processes and finding hidden decision points.

**Precursor event analysis**: Instead of asking about a challenging incident (CDM), ask about the events leading up to a decision or action. "Before you started the quote, what had you already figured out? How did you figure it out?" This surfaces the upstream cognitive work that experts often omit because it happens before the "real work" starts.

---

## 2. Requirements Elicitation in Software Engineering

Software engineering has independently developed a rich set of elicitation techniques, many of which parallel CTA methods but with different emphases. The overlap is instructive — both fields are trying to extract knowledge that stakeholders can't easily articulate.

### 2.1 Contextual Inquiry / Contextual Design

**What it is**: Beyer and Holtzblatt (1998) developed contextual inquiry as a field research method where the analyst goes to the user's workplace and observes them doing actual work, asking questions in context. The key principles:
- **Context**: Go where the work happens. Don't bring users to a lab or a conference room.
- **Partnership**: The user is the expert on their work. The analyst is an apprentice learning the craft.
- **Interpretation**: Share your interpretation in real time and let the user correct it.
- **Focus**: Have a clear focus for the session, but let the work drive what you observe.

The resulting data is modelled using five work models: flow model (communication and coordination), sequence model (step-by-step task procedures), artifact model (the things people create and use), cultural model (constraints and influences), and physical model (the physical environment).

**Application to our context**: Contextual inquiry's master-apprentice model is exactly the posture the Prompt Excavator should adopt. The agent isn't interrogating the expert — it's apprenticing to them. "Show me how you do this" is a fundamentally different conversational frame than "Tell me your requirements."

The five work models provide useful categories for the Excavate mode:
- **Flow**: Who do you communicate with during this process? Who depends on what you produce?
- **Sequence**: Walk me through the steps.
- **Artifact**: What documents, tools, or systems do you use? What do they look like?
- **Cultural**: What rules, expectations, or politics shape how you do this?
- **Physical**: Where does this happen? What's the environment like?

**Limitations**: Contextual inquiry requires being physically present, which doesn't apply to an AI agent. But the principles — context, partnership, real-time interpretation, shared focus — translate to conversational design.

**Key citations**:
- Beyer, H. & Holtzblatt, K. (1998). *Contextual Design: Defining Customer-Centered Systems*. Morgan Kaufmann.

### 2.2 Goal-Oriented Requirements Engineering (GORE)

**What it is**: A family of methods (KAOS, i*, GRL) that start with goals rather than features. The core insight: stakeholders describe what they want in terms of solutions ("I need a button that does X"), but what they actually need is to achieve a goal ("I need to reconcile my accounts quickly"). GORE works backward from goals to identify what capabilities, constraints, and interactions are needed to achieve those goals.

**The KAOS framework** (van Lamsweerde, 2009) decomposes goals into sub-goals, identifies obstacles to those goals, and derives requirements from the goal decomposition. Goals can conflict, and KAOS explicitly models goal conflicts and their resolution.

**The i* framework** (Yu, 1997) models actors, their goals, and their dependencies on each other. It distinguishes between hard goals (clear success criteria) and soft goals (quality attributes that can be "satisficed" but not fully achieved).

**Application to our context**: GORE is directly relevant because our users come to us with solutions ("I need a prompt that writes my quotes") when they actually have goals ("I need to get accurate quotes out faster without missing things"). The Primer mode should be designed to elicit goals before solutions.

Key GORE-inspired questions:
- "What are you trying to achieve?" (goal identification)
- "Why does that matter?" (goal decomposition — the answer reveals higher-level goals)
- "What stops you from doing that now?" (obstacle identification)
- "What would 'good enough' look like?" (soft goal identification)
- "Who else is affected by how you do this?" (actor and dependency modelling)

The "why" ladder (repeatedly asking why a goal matters) is a GORE technique that maps to the "5 Whys" from lean manufacturing and to motivational interviewing's exploration of values. It's a convergence point across multiple disciplines.

**Limitations**: GORE can feel abstract and disconnected from the user's concrete work experience. It works best when interleaved with concrete examples — "You said you want to get quotes out faster. Tell me about the last quote that took too long. What happened?"

**Key citations**:
- van Lamsweerde, A. (2009). *Requirements Engineering: From System Goals to UML Models to Software Specifications*. Wiley.
- Yu, E. (1997). Towards modelling and reasoning support for early-phase requirements engineering. *Proceedings of the 3rd IEEE International Symposium on Requirements Engineering*, 226-235.

### 2.3 User Stories, Use Cases, and Scenarios

**User stories** (Cohn, 2004): "As a [role], I want [feature], so that [benefit]." The "so that" clause is the critical part — it forces articulation of the underlying need, not just the surface request. User stories are deliberately lightweight and conversational.

**Use cases** (Cockburn, 2001): More structured descriptions of interactions between an actor and a system to achieve a goal. Use cases include main success scenarios, extensions (what happens when things go wrong), and preconditions/postconditions.

**Scenario-based requirements** (Carroll, 2000): Rich narrative descriptions of how work happens, including context, motivations, and consequences. Scenarios are stories, not specifications — they capture the lived experience of work in a way that formal requirements miss.

**Application to our context**: User stories give us a template for capturing what the user needs from AI: "As a builder, I want to capture site assessment notes on my phone, so that I don't forget critical details between the site visit and writing the quote." This is more structured than raw conversation but more accessible than formal requirements.

Scenario-based methods are particularly useful for Excavate mode. The expert's narrative about their work IS a scenario. The agent's job is to recognise the scenario structure within the narrative — the actors, goals, actions, exceptions, and outcomes — and extract it into a form that can inform prompt design.

The exceptions and failure cases are where the richest tacit knowledge lives. "What goes wrong?" is often a more productive question than "What do you do?" because failure cases force the expert to articulate the knowledge that prevents failure — knowledge that is otherwise invisible because it works so well.

### 2.4 Ethnographic Methods and Workplace Studies

**What it is**: Extended observation of work as it actually happens, drawing on anthropological methods. Suchman's *Plans and Situated Actions* (1987) demonstrated that the way people actually do work bears little resemblance to the way they describe it or the way procedures prescribe it. Work is improvisational, situated, and responsive to context in ways that formal descriptions miss.

**The gap between work-as-imagined and work-as-done** (Hollnagel, 2017) is a central finding: every organisation has an official way of doing things and an actual way of doing things, and they're often radically different. The actual way embodies decades of adaptation, workaround, and tacit optimisation that formal descriptions don't capture.

**Application to our context**: This finding is critical. When we ask an expert "How do you do X?", they'll often describe the official process or the idealised version. The actual process — including the shortcuts, the tacit checks, the informal information channels — is what we need for prompt design. The Excavate mode should be alert to signals that the expert is describing work-as-imagined versus work-as-done: generalised descriptions ("Usually we..."), lack of exceptions ("It's pretty straightforward"), and absence of judgment ("You just follow the process").

Questions that surface work-as-done:
- "Walk me through the last time you actually did this."
- "What do you do that's different from what the manual says?"
- "Where do you take shortcuts?"
- "What do you check that you're not supposed to have to check?"

**Key citations**:
- Suchman, L. A. (1987). *Plans and Situated Actions: The Problem of Human-Machine Communication*. Cambridge University Press.
- Hollnagel, E. (2017). *Safety-II in Practice: Developing the Resilience Potentials*. Routledge.

### 2.5 Domain Analysis and Feature Modelling

**What it is**: Systematic analysis of a domain to identify commonalities and variabilities across similar systems or processes. Feature modelling (Kang et al., 1990) identifies mandatory features (every instance has them), optional features (some instances have them), and alternative features (each instance has exactly one from a set).

**Application to our context**: When the Prompt Excavator works across multiple users in the same domain (multiple builders, multiple bookkeepers), domain analysis can identify what's common to the role and what's unique to the individual. This matters for prompt design: common features can be built into a standard prompt; unique features need to be parameterised or personalised.

The Refine mode could compare an individual's elicited knowledge against a domain model: "Most builders we've worked with check X and Y at this stage. You didn't mention those — do you skip them, handle them differently, or was that just not top of mind?"

---

## 3. Motivational Interviewing and Coaching Techniques

The CTA and requirements engineering literature focuses on *what* to elicit. The counselling and coaching literature addresses a different problem: *how* to create the conversational conditions where people can articulate things they don't normally say. This is directly relevant because our users' inability to articulate their expertise is as much an emotional and social phenomenon as a cognitive one.

### 3.1 Motivational Interviewing (MI)

**What it is**: Developed by Miller and Rollnick (1991, 2013), MI is a collaborative conversational style for strengthening a person's own motivation and commitment to change. While developed for addiction treatment, its techniques have been widely adopted in coaching, education, healthcare, and organisational change.

**Core principles (the "spirit" of MI)**:
- **Partnership**: The conversation is collaborative, not extractive. The interviewer doesn't have the answers — the interviewee does.
- **Acceptance**: Absolute worth (the person's experience is valid), autonomy support (they get to decide), accurate empathy (the interviewer genuinely understands their perspective), affirmation (acknowledging their strengths and efforts).
- **Compassion**: Prioritising the person's wellbeing and interests.
- **Evocation**: Drawing out what the person already has, rather than installing what's missing. The expertise already exists — the conversation makes it accessible.

**Key MI techniques**:
- **Open questions**: Questions that can't be answered with yes/no. "What does a good day look like in your business?" vs "Is your business going well?"
- **Affirmations**: Acknowledging the person's knowledge and competence. "You clearly know this work inside out — I can hear the depth of experience in what you're describing."
- **Reflective listening**: Restating what the person said in a way that confirms understanding and invites elaboration. Simple reflections repeat back; complex reflections add meaning, feeling, or implication. "So when the measurements don't add up, that's when your alarm bells start going off — even before you can say exactly what's wrong."
- **Summaries**: Collecting and reflecting back multiple things the person has said, often revealing connections they hadn't made explicit.

**The "change talk" concept**: In MI, the interviewer listens for and selectively reinforces statements that move toward the desired direction. In our context, the analog is "expertise talk" — moments when the expert articulates tacit knowledge, often without realising it. The agent should recognise these moments and probe them: "You just said 'you can feel when the timber's not right.' What does that feel like, exactly?"

**Application to our context**: MI's techniques map directly to what the Prompt Excavator needs:
- **Partnership frame**: "I'm here to learn from you, not to test you." This is the same apprentice posture from contextual inquiry.
- **Open questions**: All CTA probes should be open-ended. "Tell me about..." not "Do you..."
- **Reflective listening**: The agent's primary response mode should be reflection — "So what I'm hearing is [structured interpretation]. Is that right?" This accomplishes three things: it confirms understanding, it models the knowledge back to the expert in a more structured form, and it invites correction and elaboration.
- **Summaries**: The Excavate mode's output should include summaries that reveal structure: "You've described three kinds of assessments you do on site: [A, B, C]. A seems to happen first, B is conditional on what you find in A, and C is always last. Am I reading that right?"

**Limitations**: MI was developed for therapeutic contexts where the person has ambivalence about change. Our users aren't ambivalent — they're willing but unable to articulate. The resistance-reduction aspects of MI are less relevant; the evoking-from-within techniques are highly relevant.

**Key citations**:
- Miller, W. R. & Rollnick, S. (2013). *Motivational Interviewing: Helping People Change* (3rd ed.). Guilford Press.

### 3.2 Active Listening and Rogerian Techniques

**What it is**: Carl Rogers (1951, 1961) developed client-centred therapy, which introduced the idea that the therapist's primary job is to create conditions where the client can access their own knowledge and motivation. The three conditions: unconditional positive regard, empathic understanding, and congruence (genuineness).

**Application to our context**: Rogers' insight applies directly: the agent's primary job is to create conditions where the expert can access their own tacit knowledge. The techniques:
- **Paraphrasing**: "So what you're saying is..." — forces the expert to evaluate whether the paraphrase captures their meaning, which often triggers elaboration.
- **Clarifying**: "When you say 'tricky,' what do you mean by that?" — experts use domain-specific shorthand that compresses complex knowledge into single words.
- **Reflecting feeling**: "It sounds like that situation was really frustrating." — acknowledging the emotional dimension of expertise. Frustration, satisfaction, anxiety, and confidence are all signals about where the cognitive complexity lives.
- **Silence**: Allowing space after a question. Experts often fill silence with the deepest knowledge — the stuff that takes time to surface from automatic processing.

**Design implication**: The agent should not rush to the next question. After a reflection or paraphrase, it should wait for the expert to respond. The expert's correction or elaboration of the paraphrase is often more valuable than their answer to the original question.

### 3.3 Clean Language

**What it is**: Developed by David Grove (1989) and formalised by Lawley and Tompkins (2000), Clean Language is a questioning technique that uses the interviewee's own words and metaphors rather than introducing the interviewer's language. The core questions:
- "And what kind of [X] is that [X]?" (developing attributes)
- "And is there anything else about [X]?" (expanding)
- "And where/whereabouts is [X]?" (locating)
- "And what happens next?" (sequencing)
- "And what happens just before [X]?" (sequencing backward)
- "And where does [X] come from?" (sourcing)

**The principle**: Every word the interviewer introduces carries its own associations and potentially overwrites the interviewee's actual experience. By using only the interviewee's words, Clean Language avoids what CTA researchers would call "interviewer contamination" and what our theoretical framework would call "cognitive mode interference" — the interviewer's framing reshaping the expert's recall.

**Application to our context**: Clean Language is directly applicable to the Prompt Excavator. When a builder says "I just get a feel for the site," the agent should ask "And what kind of feel is that?" rather than "You mean you do a visual assessment?" The latter introduces a technical frame that may not match the expert's actual experience. The former stays in the expert's language and invites them to unpack their own metaphor.

This is especially important for non-technical users. Technical jargon from the agent can intimidate, confuse, or — worst of all — cause the expert to reshape their description to match the agent's vocabulary rather than their own experience.

**Key citations**:
- Lawley, J. & Tompkins, P. (2000). *Metaphors in Mind: Transformation through Symbolic Modelling*. Developing Company Press.

### 3.4 Appreciative Inquiry (AI)

**What it is**: Cooperrider and Whitney (1999) developed appreciative inquiry as an alternative to deficit-based problem-solving. Instead of asking "What's wrong and how do we fix it?", AI asks "What works well and how do we do more of it?" The 4-D cycle: Discover (what gives life), Dream (what might be), Design (what should be), Destiny/Deliver (what will be).

**Application to our context**: When eliciting for prompt design, starting with what works well surfaces the expert's strengths, preferences, and successful strategies. "Tell me about a time when everything went perfectly. What made that possible?" is more productive than "What are your biggest problems?" because:
1. Success stories contain embodied expertise — the expert did everything right, and the story reveals what "right" looks like.
2. People are more articulate about positive experiences than negative ones (positive experiences are recalled with more contextual detail).
3. Starting with strengths establishes the partnership frame — the agent values the expert's knowledge.

**However**: Problems, failures, and friction points also contain critical knowledge. The Prompt Excavator should use appreciative inquiry as an opening strategy, then transition to problem-focused probing once rapport is established. "That's great — you clearly know how to handle that well. Now, when does it NOT go that smoothly?"

### 3.5 Solution-Focused Brief Therapy (SFBT) Techniques

**What it is**: De Shazer and Berg (1980s) developed SFBT around the idea that you don't need to understand a problem to solve it — you need to understand what the solution looks like. Key techniques:

- **The miracle question**: "Suppose tonight while you sleep, a miracle happens and the problem is solved. When you wake up tomorrow, what's the first thing you'd notice that tells you things are different?" This bypasses analytical reasoning and accesses the expert's implicit model of what "good" looks like.
- **Exception finding**: "When is the problem less of a problem? What's different at those times?" This surfaces the conditions under which the expert's natural expertise is most effective.
- **Scaling questions**: "On a scale of 1-10, where are you now with this? What would one step higher look like?" This calibrates the expert's sense of complexity and progress.

**Application to our context**: The miracle question, adapted: "If you woke up tomorrow and AI could handle [task] perfectly, what would that look like? How would you know it was doing it right?" This surfaces the expert's implicit quality criteria — the standards they apply but can't normally articulate.

Exception finding is powerful for identifying the conditions that determine when a task is simple versus complex: "When does quoting go really quickly? What makes those easy?" The differences between easy and hard cases reveal the decision variables that the expert uses but hasn't named.

**Limitations**: SFBT techniques work well for relatively bounded problems. For complex, multi-layered expertise, they provide useful entry points but don't give you the depth that CDM or CTA methods achieve.

### 3.6 Socratic Questioning

**What it is**: The systematic use of questions to probe assumptions, examine evidence, explore implications, and surface underlying reasoning. Six types (Paul & Elder, 2007):
1. Clarification: "What do you mean by...?"
2. Probing assumptions: "What are you assuming when you...?"
3. Probing reasons and evidence: "How do you know that...?"
4. Questioning viewpoints: "How would [other person] see this differently?"
5. Probing implications: "If that's true, what follows?"
6. Questions about the question: "Why is this question important?"

**Application to our context**: Socratic questioning is the backbone technique for the Refine mode. Once the expert has provided initial descriptions, the agent uses Socratic probes to deepen understanding: "You said you check the measurements twice. What are you checking for the second time that's different from the first?" This type of question reveals that the first check is for arithmetic accuracy and the second check is for plausibility — two different cognitive operations that the expert lumped together because they both involve "checking."

---

## 4. Design Thinking and Service Design

Design thinking methods are optimised for understanding what people actually need (as opposed to what they say they need). This is precisely our problem — users come to us wanting "a prompt that does X" when what they need is often something quite different.

### 4.1 Empathy Mapping

**What it is**: A collaborative visualisation of what a person says, thinks, does, and feels in relation to a specific experience or task. The four quadrants:
- **Says**: Direct quotes from the user
- **Thinks**: What they're likely thinking (inferred from behaviour and context)
- **Does**: Observable actions and behaviours
- **Feels**: Emotional states and reactions

Extended empathy maps add: **Sees** (environmental influences), **Hears** (what others are telling them), **Pains** (frustrations, obstacles), and **Gains** (wants, needs, measures of success).

**Application to our context**: Empathy mapping provides a structure for the Excavate mode's output. Rather than producing a flat list of process steps, the output should capture the multi-dimensional experience of the work: what the expert says about it, what they seem to be thinking (implied by their language), what they actually do (as described in their narratives), and how they feel about different aspects (frustration signals cognitive complexity; confidence signals compiled expertise; anxiety signals uncertainty or high stakes).

The Pains/Gains extension is particularly useful for prioritising which aspects of the expert's work to target for AI assistance. Pain points are where AI can help most; gains are what the AI must not disrupt.

### 4.2 Journey Mapping

**What it is**: A visual representation of the steps a person goes through in accomplishing a goal, including their experience at each step — emotions, pain points, touchpoints, and channels. Originally from service design (Stickdorn et al., 2018), journey maps capture the temporal flow of an experience from the user's perspective.

**Application to our context**: Journey mapping is useful for understanding the expert's end-to-end workflow. "Take me through a typical job from the first phone call to getting paid." The journey map reveals:
- Where the expert spends the most cognitive effort (these are the steps that need the most careful prompt design)
- Where handoffs happen between people, tools, or systems (handoff points are where information is lost or transformed — prime targets for AI assistance)
- Where the emotional experience is worst (pain points — where AI could reduce cognitive load)
- Where the expert's expertise is most critical (these are the steps where AI must support, not replace, the human judgment)

For the Prompt Excavator, journey mapping serves as a macro-level view that contextualises the micro-level CTA findings. CTA tells you what's happening in the expert's head at a specific decision point; journey mapping tells you where that decision point sits in the overall flow and why it matters.

### 4.3 Jobs To Be Done (JTBD)

**What it is**: Christensen's (1997, 2003) framework argues that people don't buy products or services — they "hire" them to do a "job" in their lives. The job is the unit of analysis, not the user, the product, or the feature. Jobs have:
- **Functional dimensions**: What the person is trying to accomplish practically
- **Emotional dimensions**: How the person wants to feel (or avoid feeling)
- **Social dimensions**: How the person wants to be perceived by others

**Core insight**: People are poor at describing what they want but excellent at describing the outcomes they're trying to achieve. "I want a better invoicing system" is a solution statement. "I want to spend Saturday with my kids instead of doing paperwork" is a job statement. The job statement reveals the actual need — and the actual need can often be met in ways the person hasn't considered.

**Application to our context**: JTBD reframes what the Prompt Excavator is doing. We're not eliciting "what prompts do you need?" (solution statement). We're eliciting "what jobs are you trying to get done, and what makes them hard?" (job statement). The AI assistance is then designed to serve the job, not to implement the user's preconceived solution.

Key JTBD-style questions for the Prompt Excavator:
- "When you [task], what are you really trying to accomplish?"
- "What's the hardest part of [task], and why?"
- "If [task] were easy, what would you do with the time you saved?"
- "Who notices when [task] goes well? Who notices when it goes badly?"

The emotional and social dimensions are particularly important for non-technical users. A builder doesn't just need accurate quotes — they need to feel confident that the quote won't blow up on them, and they need clients to perceive them as professional and reliable. These emotional and social jobs shape the requirements for AI assistance in ways that functional analysis alone misses.

**Key citations**:
- Christensen, C. M., Hall, T., Dillon, K., & Duncan, D. S. (2016). *Competing Against Luck: The Story of Innovation and Customer Choice*. Harper Business.
- Ulwick, A. W. (2005). *What Customers Want: Using Outcome-Driven Innovation to Create Breakthrough Products and Services*. McGraw-Hill.

### 4.4 Problem Framing and Reframing

**What it is**: Dorst (2015) argues that the most important design skill is framing — defining what the problem actually is. Most problems are presented in a frame that constrains the solution space. Reframing the problem opens new possibilities.

Dorst's frame creation model: **What** (the desired outcome) + **How** (a working principle) + **Value** (the frame that connects what and how). The creative act is finding a new frame — a new way of seeing the relationship between what's desired and how it might be achieved.

**Application to our context**: The Prompt Excavator needs to reframe what users think they need. A bookkeeper who says "I need a prompt that categorises my transactions" may actually need a process that flags anomalies — the categorisation is how they currently find problems, but anomaly detection is the actual job. The agent should be alert to frame mismatches between the user's stated need and their described work.

Questions that support reframing:
- "If you couldn't do [stated solution], how else might you achieve [underlying goal]?"
- "What makes you think [stated solution] is the right approach?"
- "What would happen if you didn't do [current process] at all?"

### 4.5 Service Blueprint

**What it is**: A detailed mapping of a service process that shows both the frontstage (what the customer sees) and the backstage (what happens behind the scenes to deliver the service), including support processes and physical evidence. Developed by Shostack (1984) and extended by Bitner, Ostrom, and Morgan (2008).

**Application to our context**: Service blueprinting is useful when the expert's work involves serving clients or customers. The blueprint reveals:
- **Line of visibility**: What the client sees vs what happens behind the scenes. AI prompts need to produce outputs that work on both sides of this line.
- **Line of interaction**: Where the expert and client interact directly. These are moments of truth where the expert's tacit judgment is most visible and most critical.
- **Support processes**: The back-office work that enables the visible service. Often the most tedious and automatable parts of the expert's work — prime targets for AI assistance.

For a builder, the service blueprint reveals that the client-facing quote is the visible artifact, but behind it sits site assessment, material estimation, subcontractor coordination, margin calculation, and risk assessment. Each of these backstage processes has its own tacit expertise and its own potential for AI support.

---

## 5. Adaptive Depth and Progressive Disclosure

One of the hardest problems for the Prompt Excavator: how does the agent know when to probe deeper versus when it has enough? This is the calibration problem — and it's a problem that expert human interviewers solve intuitively but can't easily describe (ironic, given what we're building).

### 5.1 How Expert Interviewers Calibrate Depth

Research on expert interviewing (Kvale & Brinkmann, 2009; Rubin & Rubin, 2012) identifies several signals that experienced interviewers use to decide when to probe deeper:

**Signals that indicate hidden complexity (probe deeper)**:
- **Compression language**: "Basically...", "It's pretty straightforward...", "You just..." — these phrases often precede compressed expertise. The expert is summarising something that is actually complex because it's been compiled into automatic routines.
- **Hedging after confidence**: "I mean, usually... well, it depends..." — the expert catches themselves oversimplifying and hedges, which indicates a decision tree they haven't fully articulated.
- **Category shifts**: The expert jumps from one topic to another without connecting them. The connection exists in their mental model but wasn't articulated.
- **Emotional markers**: Frustration, pride, anxiety, or relief at specific points in the description. These mark moments of cognitive complexity or high stakes.
- **Inconsistency**: The expert says one thing at one point and something different later. This often indicates a conditional that they haven't made explicit — both statements are true, but under different conditions.
- **Speed changes**: The expert slows down when describing cognitively demanding parts of the work and speeds up when describing routine parts. Slowdowns mark complexity.
- **Abstraction level shifts**: Dropping from abstract description ("I assess the site") to concrete detail ("I check whether the soil is clay or sand") often happens at the boundary between compiled and accessible knowledge.

**Signals that indicate sufficient depth (move on)**:
- **Repetition**: The expert is restating the same point in different words. You've reached the bottom of what they can articulate on this topic.
- **Convergence**: Multiple probe paths lead to the same answer. The territory has been mapped.
- **Concrete specificity**: The expert provides specific, detailed examples with clear conditions and outcomes. They're no longer generalising.
- **Comfort with "I don't know"**: The expert can articulate the boundary of their knowledge rather than making something up.

### 5.2 The Depth Calibration Framework

Drawing from CTA methodology and interview research, I propose a four-level depth model for the Prompt Excavator:

**Level 1 — Process Level**: What are the main steps? What happens in what order? This is what most users volunteer without prompting. It's the surface layer — work-as-imagined, not work-as-done.

**Level 2 — Decision Level**: At each step, what decisions are you making? What information do you need? What could go wrong? This is where CDM and ACTA operate. It surfaces the decision architecture of the work.

**Level 3 — Cue Level**: What tells you which way to decide? What do you notice that a novice would miss? How do you know when something's off? This is where tacit perceptual expertise lives — the pattern recognition that experts can't easily describe.

**Level 4 — Model Level**: What's your mental model of how this domain works? What are the causal relationships? How do you predict what will happen? This is the deepest layer — the expert's theory of their domain, which may never have been articulated.

**The calibration rule**: Start at Level 1. When you detect complexity signals (compression language, hedging, category shifts), move one level deeper. When you detect sufficiency signals (repetition, convergence, concrete specificity), move on.

Not every task needs Level 4 depth. A bookkeeper's transaction categorisation might need Level 2 (decisions) but not Level 3 (cues) because the decisions are rule-based, not perceptual. A builder's structural assessment needs Level 3 (cues) because the decisions are perceptual. A security architect's threat modelling might need Level 4 (mental model) because the decisions depend on understanding causal relationships in complex systems.

### 5.3 Progressive Disclosure in Elicitation

**What it is**: Progressive disclosure (Shneiderman, 1998) is an interaction design principle where information is revealed in layers — the most important and general first, with details available on demand. Applied to elicitation, it means starting with broad questions and progressively narrowing based on what the expert's responses reveal.

**Application to our context**: The Prompt Excavator should use progressive disclosure in both directions:

**Forward disclosure (agent to user)**: Start with simple, broad questions. As the conversation develops, the agent's questions become more specific and technical, calibrated to the user's demonstrated level of articulation. Don't ask a builder about their "decision heuristics" — ask "How do you decide?"

**Backward disclosure (user to agent)**: Let the user reveal complexity at their own pace. Some users will describe their work at Level 1 and be done. Others will naturally go deeper. The agent should match the user's depth rather than imposing a depth target.

### 5.4 The Funnel Technique

**What it is**: A standard journalistic and research interviewing technique (Kvale & Brinkmann, 2009) where questions progress from broad and open to narrow and specific:
1. **Opening**: Broad, non-threatening, inviting narrative. "Tell me about your work."
2. **Exploration**: Following threads from the opening. "You mentioned [X]. Tell me more about that."
3. **Probing**: Targeted questions about specific elements. "When you said you check [Y], what exactly are you checking for?"
4. **Confirmation**: Testing understanding and inviting correction. "So if I've understood correctly, the process is [Z]. Is that right?"

**Application to our context**: This should be the default conversational flow for the Prompt Excavator. Each topic follows the funnel: open, explore, probe, confirm. The Refine mode is essentially the probing and confirmation stages applied to material from earlier Excavate sessions.

### 5.5 Branching Based on Domain Complexity

Research on expertise (Ericsson, Charness, Feltovich & Hoffman, 2006) suggests that domain complexity can be roughly assessed along three dimensions:

- **Rule density**: How many rules, constraints, or considerations apply simultaneously? Low = simple decisions; high = complex trade-offs.
- **Uncertainty**: How much of the relevant information is unknown, ambiguous, or probabilistic? Low = deterministic procedures; high = judgment under uncertainty.
- **Interaction effects**: Do the elements of the task interact with each other, or are they independent? Independent = decomposable; interacting = systemic.

These dimensions help the Prompt Excavator decide how deep to go:
- Low rule density + low uncertainty + low interaction = Level 1-2 is sufficient
- High on any dimension = Level 3 minimum
- High on two or more dimensions = Level 4 needed

**Practical application**: After the initial exploration, the agent can assess these dimensions from the expert's responses and calibrate its questioning accordingly. A bookkeeper describing a routine reconciliation process (low on all three) gets Level 2 questions. A builder describing how they assess structural modifications to heritage buildings (high on all three) gets Level 4 questions.

---

## 6. Cross-Cultural and Communication Style Considerations

The Prompt Excavator's users range from tradies who communicate through doing and showing to technical architects who communicate through abstractions and frameworks. These aren't just vocabulary differences — they're fundamentally different communication styles that require different elicitation approaches.

### 6.1 Communication Style Typologies

**High-context vs low-context communication** (Hall, 1976): Some communicators expect meaning to be carried by context, relationship, and implication (high-context). Others expect meaning to be explicit in the words (low-context). Many tradespeople communicate in high-context style — "You know what I mean" carries real content, and demanding explicit articulation feels unnatural or even insulting.

**Concrete vs abstract preference**: Some people think and communicate in concrete, example-based terms ("Let me show you"). Others prefer abstractions and frameworks ("The general principle is..."). Neither is better; they're different cognitive styles. The Prompt Excavator must adapt: for concrete thinkers, ask for examples and stories; for abstract thinkers, ask for principles and patterns.

**Doing vs saying**: Many expert practitioners communicate their knowledge through demonstration, not description. A builder shows you how to assess a wall rather than describing the assessment criteria. An electrician's hands tell you what to check before their words do. This is Polanyi's (1966) tacit knowledge problem — "we can know more than we can tell."

### 6.2 Adapting Elicitation to Communication Styles

**For concrete, action-oriented communicators (builders, trades, many small business operators)**:
- Use example-anchored questions: "Walk me through the last job you quoted."
- Avoid abstract framing: Not "What's your decision framework?" but "How did you figure out the price?"
- Use contrastive cases: "What's the difference between an easy job and a hard one?"
- Accept show-don't-tell: "If you were showing an apprentice, what would you point to?"
- Use their language: Don't translate their terms into formal vocabulary. "Gut feel" is a valid technical term — it means pattern recognition from compiled experience.

**For process-oriented communicators (bookkeepers, administrators, office managers)**:
- Use sequential questions: "What's the first thing you do? Then what?"
- Leverage existing documentation: "Show me the spreadsheet you use. Walk me through it."
- Ask about exceptions: "When doesn't the standard process work?"
- Probe decision points: "At this step, you could do X or Y. How do you decide?"

**For analytical, framework-oriented communicators (technical architects, engineers, consultants)**:
- Ask for mental models: "How do you think about [domain]?"
- Use their abstractions: If they say "threat model," probe within that frame: "What goes into your threat model?"
- Challenge generalisations: "You said 'always check X.' Are there cases where X doesn't apply?"
- Ask for edge cases: "What's the weirdest instance of this you've encountered?"

**For narrative communicators (many people, but especially when trust is being built)**:
- Let them tell stories: "Tell me about a time when..."
- Don't interrupt the narrative to extract facts — extract them afterward
- Use the narrative as anchor material for follow-up: "In that story, you mentioned [X]. Let's dig into that."

### 6.3 Power Dynamics and Expert Reluctance

**The credentialing problem**: Some experts are reluctant to share knowledge because they fear being replaced, judged, or exposed as not-expert-enough. This is particularly acute when the elicitation is explicitly about building AI systems. "You're asking so you can build something that replaces me" is a reasonable concern.

**Mitigation strategies**:
- Frame the AI as an assistant, not a replacement: "We're building something that does the tedious parts so you can focus on the parts that need your brain."
- Acknowledge the expert's irreplaceability: "A machine can't assess a site the way you do. But it might be able to turn your assessment into a quote faster."
- Show the expert what the AI produces and ask them to evaluate it — this reverses the power dynamic. Now they're the judge, not the subject.
- Start with low-stakes, high-tedium tasks. Nobody feels threatened by automating paperwork.

**The impostor problem**: Some experts downplay their expertise because they suffer from impostor syndrome or because they work in domains where expertise isn't formally credentialed. A bookkeeper with 20 years of experience may say "I just do the books" while possessing profound pattern-recognition abilities for detecting anomalies.

**Mitigation**: Validate expertise through observation, not self-report. "You just described spotting a problem that a junior person would have missed. That's expertise." The Prompt Excavator should actively recognise and name expertise when it surfaces, using MI's affirmation technique.

### 6.4 Neurodivergent Considerations

**ADHD**: May produce nonlinear narratives that jump between topics. The agent should track the threads and weave them together rather than forcing sequential description. These jumps often reveal associative connections that linear thinkers miss.

**Autism spectrum**: May prefer precise, structured questions over open-ended ones. "Tell me about your work" may be too broad. "When you receive a new purchase order, what is the first thing you check?" may work better. Concrete over abstract; specific over general.

**Dyslexia and low literacy**: If the interface involves written output, the agent should not assume the user can read and edit long text. Voice-first interfaces and conversational interaction may be essential.

**General principle**: Offer multiple modes of interaction and let the user gravitate to what works. Some people need to talk; some need to type; some need to draw; some need to show.

### 6.5 Language and Jargon

**Domain jargon is a feature, not a bug**: When a builder says "the substrate's shot," that single phrase encodes a complex assessment (the surface layer of the wall or floor has deteriorated beyond the point where new material can be applied to it without remediation). The Prompt Excavator should capture jargon AND ask what it means: "When you say 'the substrate's shot,' what exactly are you seeing that tells you that?"

**Beware of shared words with different meanings**: "Assessment" means one thing to a builder (visual inspection of site conditions), another to an accountant (determining tax liability), and another to a teacher (evaluating student performance). The agent should never assume it knows what a word means in the user's domain.

**Code-switching**: Many experts use different language with different audiences. How a builder talks to a supplier is different from how they talk to a client, which is different from how they talk to another builder. The most authentic knowledge comes when the expert is speaking in their peer language. The agent should aim for peer-register, not formal-register.

---

## 7. Knowledge Representation

Once tacit knowledge has been elicited, it needs to be represented in a form that can inform prompt and pipeline design. The representation isn't a neutral container — it shapes what can be seen and what's invisible.

### 7.1 Decision Tables and Decision Trees

**What they are**: Tabular or tree-structured representations of decision logic. Decision tables map conditions to actions; decision trees branch on conditions to reach outcomes.

**When to use**: When the elicited knowledge is primarily conditional — "If X, then A; if Y, then B; if X and Z, then C." Many business processes have this structure, especially in accounting, compliance, and trades estimation.

**Application to prompt design**: Decision tables translate directly into prompt logic. A decision table for "How to categorise a business expense" becomes the core of a classification prompt. The prompt doesn't need the expert's full knowledge — it needs the decision logic that the expert uses.

**Limitations**: Decision tables can't capture perceptual judgments, trade-offs, or contextual sensitivity. They work for the rule-based parts of expertise but not for the judgment-based parts.

### 7.2 Concept Maps and Knowledge Graphs

**What they are**: Network representations where nodes are concepts and edges are labelled relationships. Concept maps (Novak & Canas, 2008) are hierarchical; knowledge graphs can be any topology.

**When to use**: When the elicited knowledge is primarily relational — "X affects Y, which depends on Z, which constrains W." Domain mental models have this structure. A builder's understanding of how site conditions affect construction methods is a web of relationships, not a decision tree.

**Application to prompt design**: Concept maps inform the prompt's knowledge structure — what the prompt needs to "know" about the domain. They're particularly useful for designing the lenses in an investigative prompt: each major relationship in the concept map is a potential lens.

### 7.3 Process Flows and Swimlane Diagrams

**What they are**: Sequential representations of work processes, optionally showing who is responsible for each step (swimlanes). Standard notation: BPMN (Business Process Model and Notation).

**When to use**: When the elicited knowledge is primarily procedural — "First A, then B, then C, with decision points at D and E." Many operational processes have this structure.

**Application to prompt design**: Process flows map directly to pipeline architecture. Each step in the process flow is a potential pipeline stage. Decision points become routing logic. Swimlane boundaries become agent boundaries.

### 7.4 Cognitive Demand Tables

**What they are**: Tables that map tasks to their cognitive demands — what knowledge is needed, what decisions must be made, what cues are used, what errors are common, and what strategies experts employ. Developed within the CTA tradition (Crandall, Klein & Hoffman, 2006).

**When to use**: When the elicited knowledge spans multiple cognitive types (procedural, perceptual, decisional, strategic). Cognitive demand tables capture the multi-dimensional nature of expertise.

**Application to prompt design**: Cognitive demand tables are the most useful representation for our purpose because they directly inform prompt architecture decisions:
- **Knowledge needed** → What goes in the prompt's context/reference material
- **Decisions to make** → What the prompt asks the AI to do
- **Cues used** → What data the AI needs access to
- **Common errors** → What the prompt should guard against
- **Expert strategies** → What reasoning approach the prompt should elicit

### 7.5 Task-Knowledge Structures (TKS)

**What they are**: Johnson et al. (1988) proposed TKS as a representation that integrates task structure (what's done) with knowledge structure (what's known). TKS has three layers:
- **Goal structure**: What the person is trying to achieve, decomposed hierarchically
- **Procedural structure**: What actions achieve the goals, including conditions, sequences, and alternatives
- **Taxonomic structure**: How the person categorises the objects and concepts in their domain

**Application to our context**: TKS bridges the gap between GORE (goal-oriented) and CTA (task-oriented) approaches. For the Prompt Excavator, it provides a combined representation: the user's goals (why they want AI help), the procedures they currently use (what the AI needs to support), and the domain categories they work with (what the AI needs to understand).

### 7.6 Pattern Language

**What it is**: Alexander's (1977) concept of pattern languages — collections of named, reusable solutions to recurring problems, connected by explicit relationships. Each pattern describes a problem, the context in which it occurs, and a solution, along with links to related patterns.

**Application to our context**: As the Prompt Excavator processes knowledge from multiple experts in the same domain, patterns will emerge — recurring decision structures, common trade-offs, shared mental models. These can be captured as a pattern language for the domain, which then becomes a resource for designing prompts for new users in the same domain.

For example, a "Quoting Pattern Language" for builders might include patterns like "Site Assessment" (problem: unknown conditions; solution: systematic visual inspection with specific checklist), "Margin Calculation" (problem: pricing uncertainty; solution: base cost plus contingency scaled to uncertainty), and "Scope Creep Guard" (problem: client expectations exceeding quote; solution: explicit inclusion/exclusion list). Each pattern captures compiled expertise in a reusable form.

**Key citations**:
- Alexander, C., Ishikawa, S., & Silverstein, M. (1977). *A Pattern Language: Towns, Buildings, Construction*. Oxford University Press.

### 7.7 Sensemaking Frameworks (Dervin, Klein)

**What they are**: Brenda Dervin's Sense-Making methodology (1983, 1992) models information seeking as bridging gaps — a person encounters a gap in their understanding, and they seek information to bridge it. The framework asks: What's the situation? What's the gap? What would bridge the gap? What's the outcome?

Gary Klein's Data/Frame model of sensemaking (2006) describes how people construct and revise explanatory frameworks when encountering complex data. The process alternates between: elaborating an existing frame (fitting data to the story), questioning a frame (noticing data that doesn't fit), reframing (constructing a new explanatory framework), and comparing frames.

**Application to our context**: The Prompt Excavator is a sensemaking tool. The expert is encountering a gap (they can't articulate what they need from AI), and the agent helps them bridge it. Dervin's gap-bridging model maps directly to the three modes: Primer identifies likely gaps, Excavate bridges them through structured conversation, Refine confirms the bridges hold.

Klein's Data/Frame model is useful for designing the Excavate mode's processing logic. When the expert's narrative contains internal contradictions or unexplained jumps, the agent should treat these as "data that doesn't fit the current frame" and probe: "You said X earlier, but now you're describing Y. How do those fit together?" This is frame-questioning — helping the expert refine their own mental model by exposing its inconsistencies.

**Key citations**:
- Dervin, B. (1992). From the mind's eye of the user: The sense-making qualitative-quantitative methodology. In J. D. Glazier & R. R. Powell (Eds.), *Qualitative Research in Information Management*. Libraries Unlimited.
- Klein, G., Phillips, J. K., Rall, E. L., & Peluso, D. A. (2007). A data-frame theory of sensemaking. In R. R. Hoffman (Ed.), *Expertise Out of Context*. Lawrence Erlbaum Associates.

---

## 8. Adjacent and Unexpected Connections

### 8.1 Tacit Knowledge Theory (Polanyi, Nonaka & Takeuchi)

**Michael Polanyi** (1966) established the foundational distinction between tacit and explicit knowledge: "We can know more than we can tell." Tacit knowledge includes skills, intuitions, and perceptual capabilities that resist articulation. Polanyi described two components:
- **Subsidiary awareness**: Knowledge we use as a tool without attending to it directly (a pianist's finger movements, a surgeon's instrument handling)
- **Focal awareness**: What we're consciously attending to (the music, the surgical outcome)

Tacit knowledge resides in subsidiary awareness. When you try to articulate it, you shift it to focal awareness — and this shift can actually disrupt performance (the "centipede's dilemma": the centipede walked fine until asked how it coordinated its legs, and then it couldn't walk at all).

**Nonaka and Takeuchi** (1995) extended this into the SECI model of knowledge conversion:
- **Socialisation** (tacit → tacit): Learning through shared experience (apprenticeship, observing)
- **Externalisation** (tacit → explicit): Articulating tacit knowledge through metaphor, analogy, models, concepts
- **Combination** (explicit → explicit): Systematising and combining explicit knowledge
- **Internalisation** (explicit → tacit): Learning by doing — converting explicit knowledge back into tacit through practice

**Application to our context**: The Prompt Excavator is primarily an externalisation tool — it supports the tacit → explicit conversion. The SECI model tells us that metaphor and analogy are the primary vehicles for externalisation. This means the agent should actively invite metaphorical description: "What's it like? What does it remind you of?" Metaphors aren't imprecise descriptions of precise knowledge — they're the most precise description available for certain types of tacit knowledge.

The socialisation pathway is also relevant: the conversation between agent and expert IS a form of socialisation. The agent's reflections and paraphrases create a shared understanding that helps the expert's tacit knowledge become more accessible. This is why conversational elicitation works better than questionnaires — the social process of making yourself understood is what enables externalisation.

**The centipede's dilemma warning**: There's a real risk that excessive probing disrupts the expert's compiled knowledge rather than surfacing it. When a builder says "I just know" and we push for articulation, we might be asking them to decompose knowledge that works precisely because it's not decomposed. The agent needs to recognise when tacit knowledge should be captured as a holistic capability rather than decomposed into explicit rules.

**Key citations**:
- Polanyi, M. (1966). *The Tacit Dimension*. University of Chicago Press.
- Nonaka, I. & Takeuchi, H. (1995). *The Knowledge-Creating Company: How Japanese Companies Create the Dynamics of Innovation*. Oxford University Press.

### 8.2 Situated Cognition and Distributed Cognition

**Situated cognition** (Brown, Collins, & Duguid, 1989; Lave & Wenger, 1991): Knowledge is inseparable from the activity, context, and culture in which it is used. You can't extract "what the expert knows" independently of the situation in which they know it. A builder's expertise manifests differently on a heritage restoration than on a new build, even though the "same" knowledge is supposedly being applied.

**Distributed cognition** (Hutchins, 1995): Cognitive processes aren't confined to individual heads — they're distributed across people, tools, and environments. A ship navigates not because any single person knows how, but because knowledge and processing are distributed across the navigation team, their instruments, and their procedures.

**Application to our context**: These theories warn us that knowledge elicited in an interview may not accurately represent knowledge-in-practice. The builder who describes their quoting process in a conversation is performing a different cognitive act than the builder who is actually quoting on site with their tools, materials, and environmental cues present.

Design implications for the Prompt Excavator:
- **Elicit in context whenever possible**: "Can you walk me through this while looking at your actual [tool/spreadsheet/site photos]?" Contextual cues trigger recall of situated knowledge.
- **Elicit the tools and artifacts, not just the person**: "What tools do you use? What do they tell you? What information do you get from the environment?" The expertise may live partly in the interaction between the person and their tools.
- **Don't assume portability**: Knowledge that works in one context may not work in another. A prompt designed from one expert's situated knowledge needs to be tested against different contexts.

### 8.3 Dreyfus Model of Skill Acquisition

**What it is**: Dreyfus and Dreyfus (1986) proposed five stages of skill acquisition:
1. **Novice**: Follows context-free rules
2. **Advanced beginner**: Recognises situational elements from experience
3. **Competent**: Consciously chooses among plans and perspectives
4. **Proficient**: Sees situations holistically; decomposes them when needed
5. **Expert**: Acts intuitively from deep experience; deliberates only in novel situations

**Application to our context**: The Dreyfus model predicts what kind of knowledge we'll get at each expertise level:

- **Novice users**: Can describe rules and procedures but not judgment or adaptation. Their knowledge is already explicit — no excavation needed. The Prompt Excavator adds less value here.
- **Competent users**: Can describe their decision-making process because it's still conscious. They know what they do and can explain why. Good candidates for standard elicitation.
- **Proficient and expert users**: Have compiled most of their knowledge into automatic, holistic perception and response. They're the hardest to elicit from — and the most valuable to elicit from. The Prompt Excavator earns its cost here.

This means the agent needs to calibrate not just to the domain but to the user's level of expertise. Expert-level users need deeper probing techniques (CDM, contrastive cases) because their knowledge is more deeply compiled. Competent-level users can describe their processes with lighter scaffolding.

The Dreyfus model also has a crucial implication for the output: **the AI system we build from the elicited knowledge doesn't need to replicate the expert's intuitive processing**. It needs to replicate the *output* of that processing at a competent or proficient level. The expert's holistic perception can't be captured in rules — but a good-enough approximation can, and that approximation is what the prompt embodies.

**Key citations**:
- Dreyfus, H. L. & Dreyfus, S. E. (1986). *Mind Over Machine: The Power of Human Intuition and Expertise in the Era of the Computer*. Free Press.

### 8.4 Boundary Objects (Star & Griesemer, 1989)

**What it is**: Objects that sit at the intersection of different social worlds and are interpreted differently by each, yet maintain enough shared identity to serve as a basis for communication. Star and Griesemer (1989) identified these in the context of museums, but the concept applies broadly.

**Application to our context**: The structured output from the Prompt Excavator — the represented knowledge — is a boundary object. It sits between the expert's world (where they know things tacitly) and the AI designer's world (where knowledge must be explicit and structured). The representation must be interpretable by both sides: the expert must recognise their knowledge in it ("Yes, that's what I do"), and the prompt designer must be able to build from it ("This tells me how to structure the prompt").

This means the knowledge representation should be bilingual — accessible to domain experts AND to prompt/pipeline designers. A purely technical representation (JSON schemas, decision trees) may be optimal for designers but opaque to experts. A purely narrative representation (stories, descriptions) may be accessible to experts but hard for designers to work with. The best representation uses both: narrative with embedded structure, or structure with embedded examples.

### 8.5 Activity Theory (Vygotsky, Leont'ev, Engestrom)

**What it is**: Activity Theory analyses human activity as a system with six components: Subject (who), Object (goal/motivation), Tools (mediating artifacts), Rules (norms and conventions), Community (social group), and Division of Labour (role distribution). These components interact — changing any one changes the activity as a whole.

**Application to our context**: Activity Theory provides the most comprehensive frame for understanding what the expert is actually doing. It captures not just the task (what the CTA methods surface) but the entire activity system — the rules, community expectations, tools, and division of labour that shape how the task is performed.

For the Prompt Excavator, this means eliciting beyond the individual task:
- **Tools**: What tools and systems does the expert use? What do those tools make easy or hard?
- **Rules**: What explicit and implicit rules govern how the work is done? (Industry codes, company policies, unwritten norms)
- **Community**: Who else is involved? What are their expectations? How does the expert's work fit into a larger system?
- **Division of labour**: What does the expert do versus what others do? Where are the handoffs?

This is relevant because the AI system we design will become a new tool in the activity system, and introducing a new tool changes the entire system. Understanding the current system is necessary for predicting how the new tool will integrate — or disrupt.

**Key citations**:
- Engestrom, Y. (1987). *Learning by Expanding: An Activity-Theoretical Approach to Developmental Research*. Cambridge University Press.

### 8.6 Naturalistic Decision Making (NDM) Beyond Klein

Klein's RPD is the most famous NDM model, but the field is broader. Other NDM frameworks relevant to our context:

**Rasmussen's Skills-Rules-Knowledge (SRK) Framework** (1983): Three levels of cognitive control:
- **Skill-based**: Automatic, sensorimotor patterns triggered by familiar signals (typing, driving in familiar territory). Very hard to elicit because it's pre-conscious.
- **Rule-based**: Stored rules triggered by recognised situations (if alarm sounds, check X first). Moderate difficulty to elicit — experts can describe rules when prompted.
- **Knowledge-based**: Analytical reasoning from first principles for novel situations. Easiest to elicit because it's already conscious — but also the most time-intensive processing.

The SRK framework tells us that different levels of the expert's processing require different elicitation approaches. Skill-based knowledge needs observation or simulation. Rule-based knowledge responds to conditional probes ("What do you do when...?"). Knowledge-based reasoning responds to scenario-based probes ("You've never seen this before. How would you approach it?").

**Zsambok's NDM Characteristics** (1997): NDM research identifies several features of real-world decision making that laboratory studies miss:
- Ill-structured problems
- Uncertain, dynamic environments
- Shifting, ill-defined, or competing goals
- Action/feedback loops
- Time stress
- High stakes
- Multiple players
- Organisational goals and norms

These features are present in many of our users' work environments. A builder quoting a complex renovation faces ill-structured problems (every site is different), uncertain environments (hidden conditions), shifting goals (client changes their mind), time stress (competitive quotes), high stakes (margin erosion on a wrong quote), and multiple players (client, council, subcontractors).

The Prompt Excavator should probe for these NDM characteristics because they determine the cognitive complexity of the work — and therefore the depth and sophistication needed in the resulting AI system.

**Key citations**:
- Rasmussen, J. (1983). Skills, rules, and knowledge: Signals, signs, and symbols, and other distinctions in human performance models. *IEEE Transactions on Systems, Man, and Cybernetics*, 13(3), 257-266.
- Zsambok, C. E. & Klein, G. (Eds.) (1997). *Naturalistic Decision Making*. Lawrence Erlbaum Associates.

### 8.7 Knowledge Audit and Organizational Knowledge Management

**SECI Model (reprise)**: Nonaka and Takeuchi's model (Section 8.1) describes how organizations create and share knowledge. The Prompt Excavator is performing the Externalisation step — converting tacit to explicit — but in a context where the "organisation" might be a single-person business.

**After Action Reviews (AARs)**: Military-origin technique for extracting lessons from experience. Structure: What was supposed to happen? What actually happened? Why was there a difference? What should we do differently? AARs are a lightweight form of CDM that many organisations already practice.

**Application to our context**: AARs provide a natural entry point for the Prompt Excavator. Many users already do informal AARs ("What went wrong on that job?"). The agent can scaffold this existing practice: "You mentioned that job didn't go well. Let's do a quick review. What was the plan? What actually happened? Where did it diverge?"

### 8.8 Ecological Interface Design (EID)

**What it is**: A design approach (Vicente & Rasmussen, 1992) that makes the constraints and structure of a work domain visible in the interface, so that expert pattern recognition can operate on the interface the way it operates on the real world.

**Application to our context**: EID's core principle — making the invisible visible — is exactly what the Prompt Excavator does. The expert's tacit knowledge is invisible. The agent makes it visible by eliciting it, structuring it, and presenting it back. The representation should make the structure of the expert's knowledge as perceivable as the structure of the work itself — so that the expert can evaluate whether the representation is accurate by recognising it, not by analytically comparing it.

### 8.9 Cognitive Bias and Elicitation Pitfalls

Elicitation is vulnerable to systematic biases that distort the knowledge captured:

**Availability bias**: Experts recall vivid or recent cases more readily than typical ones. The Prompt Excavator should explicitly ask for typical cases as well as memorable ones: "That's a great example of when things went wrong. Now tell me about a completely routine job — boring, straightforward, nothing interesting happened."

**Hindsight bias**: When recalling past events, experts reconstruct a more rational and deliberate process than actually occurred. CDM's "what if" probes partially counteract this by introducing uncertainty: "At the time, what else could you have thought was happening?"

**Expert blind spots**: Experts forget what it's like to not know something (the "curse of knowledge"). They omit steps that are "obvious" — obvious to them, but invisible to a novice or an AI system. The expert-novice contrast technique (Section 1.8) directly addresses this.

**Social desirability**: Experts describe what they should do rather than what they actually do. They present the textbook version rather than the workaround version. The work-as-imagined vs work-as-done gap (Section 2.4) is partly social desirability in action.

**Coherence bias**: Experts construct a coherent narrative from what is actually a messy, contingent process. The real process had dead ends, backtracking, uncertainty, and ad hoc decisions — but the retelling smooths these away. The agent should probe for messiness: "Were you ever unsure? Did you change your mind? Was there a point where you didn't know what to do?"

### 8.10 Conversational AI Research Relevant to Elicitation

**Grounding in communication** (Clark & Brennan, 1991): Communication requires that both parties establish common ground — shared understanding of what has been said and meant. Grounding happens through back-channel signals (nodding, "uh-huh"), clarification requests, and reformulation. An AI agent lacks many physical grounding mechanisms but can use verbal grounding: summaries, paraphrases, confirmation questions.

**Repair in conversation** (Schegloff, Jefferson & Sacks, 1977): When communication breaks down, people use repair mechanisms — self-repair (the speaker corrects themselves), other-initiated repair (the listener signals non-understanding), and other-repair (the listener corrects the speaker). The Prompt Excavator needs robust other-initiated repair: "I'm not sure I followed that — can you say that differently?" This is especially important for cross-domain communication where jargon creates understanding gaps.

**Conversational memory and coherence**: Long conversations accumulate shared context that both parties draw on. The Prompt Excavator's three modes span multiple interactions, so it needs to maintain coherence across sessions: "Last time, you described [X]. Today I'd like to go deeper on [Y], which you mentioned in passing."

### 8.11 Expertise Research: When Experts Are Wrong

Not all expert knowledge is correct. Shanteau (1992) identified domains where expert judgment is reliable (livestock judges, astronomers, chess masters, physicists) and domains where it is poor (clinical psychologists, stock brokers, court judges, personnel selectors). The distinguishing factors:
- **Reliable expertise**: Static stimuli, decomposable problems, decision aids available, feedback on outcomes
- **Unreliable expertise**: Dynamic stimuli, undecomposable problems, no decision aids, outcomes unavailable or delayed

**Application to our context**: The Prompt Excavator should not assume that elicited knowledge is correct. In domains where expert judgment is unreliable, the elicited knowledge may encode systematic errors. The agent should be designed to flag uncertainty — "You said you always do X in this situation. How often does X turn out to be the right call?" — and the resulting prompts should build in verification rather than blindly implementing the expert's reported process.

This connects back to the Kahneman-Klein boundary conditions (Section 10 of `cognitive-science-research.md`): expert intuition is trustworthy only when the domain has stable regularities and the expert has had opportunity to learn them. The Prompt Excavator should assess these conditions for each piece of elicited knowledge.

### 8.12 Knowledge Elicitation Games and Creative Techniques

Traditional elicitation is interview-heavy. Some approaches use structured activities instead:

**Card sorting**: The expert sorts domain elements into groups, revealing their categorisation structure. Useful for understanding how the expert organises their domain. Open card sort (expert creates categories) is more revealing than closed card sort (pre-defined categories).

**Rich pictures**: From Soft Systems Methodology (Checkland, 1981). The expert draws a picture of their work situation, including people, processes, problems, and emotions. The drawing surfaces elements that verbal description misses.

**Design games**: Structured collaborative activities (Brandt, 2006) where participants use cards, boards, or other materials to model their work. The physical manipulation often surfaces knowledge that conversation alone doesn't reach.

**Provocative questioning**: Deliberately absurd or extreme questions that disrupt routine description: "What would happen if you just skipped this step entirely?" "What if you had unlimited time?" "What if you couldn't see the site?" These provocations force the expert to articulate assumptions that are normally invisible.

**Application to our context**: While the Prompt Excavator is primarily conversational, some of these techniques can be adapted:
- Virtual card sorting: "Here are the things you've mentioned so far. How would you group them?"
- Thought experiments: "What if a robot had to do this job? What would it need to know?"
- Elimination probes: "What's the one thing you couldn't do this job without?"

---

## 9. Synthesis: Design Principles for the Prompt Excavator

Drawing across all the methodologies surveyed, these are the design principles that emerge:

### 9.1 Adopt the Apprentice Posture

Across CTA, contextual inquiry, MI, and Rogerian therapy, the same finding: the elicitor must position themselves as a learner, not an interrogator. The expert is the authority. The agent's role is to help the expert articulate what they already know, not to extract knowledge from them. This is MI's "evocation" principle — drawing out, not putting in.

**Design implication**: The Prompt Excavator's conversational style should be curious, deferential, and reflective. "That's fascinating — I want to make sure I understand..." not "Please describe your process step by step."

### 9.2 Anchor in the Specific, Then Generalise

CDM, scenario-based methods, and narrative approaches all converge: concrete, specific examples produce better elicitation than abstract questions. The expert can navigate a specific remembered experience much more easily than they can describe general principles. Once the specific experience has been explored, the agent can generalise: "You described checking the soil on that job. Is that something you do on every job, or just certain types?"

**Design implication**: The default question type should be example-anchored. "Tell me about [a specific instance]" before "How do you generally [handle this category]?"

### 9.3 Use Contrast and Exception to Surface Tacit Knowledge

The expert-novice contrast, the SFBT exception-finding technique, and the repertory grid all converge: tacit knowledge becomes visible when contrasted against its absence. The expert knows what they know partly by knowing what novices don't know and partly by knowing when their usual approach doesn't apply.

**Design implication**: The agent should systematically use contrastive probes:
- Expert vs novice: "What would a beginner get wrong here?"
- Easy vs hard: "When is this straightforward? When is it not?"
- Success vs failure: "Tell me about a time this went perfectly, and a time it didn't."
- Rule vs exception: "When doesn't the normal approach work?"

### 9.4 Reflect, Don't Just Record

MI's reflective listening, contextual inquiry's real-time interpretation, and Clark & Brennan's grounding theory all converge: the agent must actively demonstrate understanding, not passively collect answers. Reflection serves three purposes: it confirms understanding, it models the knowledge back to the expert in a more structured form, and it invites correction and elaboration.

**Design implication**: After every substantive expert response, the agent should reflect before asking the next question. "So what I'm hearing is [interpretation]. Does that sound right?" This is not just politeness — it's the mechanism by which tacit knowledge becomes explicit. The expert evaluates the agent's interpretation and corrects it, and the correction is where the deepest knowledge often surfaces.

### 9.5 Calibrate Depth to Complexity and Communication Style

The adaptive depth framework (Section 5), the communication style typology (Section 6), and the Dreyfus model all converge: there is no one-size-fits-all elicitation depth. The agent must dynamically calibrate based on:
- The complexity of the domain (rule density, uncertainty, interaction effects)
- The expertise level of the user (novice, competent, expert)
- The communication style of the user (concrete, abstract, narrative, analytical)
- The cognitive depth signals in the user's responses (compression, hedging, emotion)

**Design implication**: The Prompt Excavator needs a dynamic depth-calibration mechanism — not a fixed script. Start shallow, go deeper when complexity signals appear, back off when sufficiency signals appear. This is fundamentally an adaptive expertise problem, which means it connects directly to the cognitive mode framework: the agent must operate in investigation mode (following signals, adapting in real time) rather than evaluation mode (checking off a predetermined list).

### 9.6 Represent Knowledge in Multiple Forms

The knowledge representation section (Section 7) and the boundary object concept (Section 8.4) converge: no single representation captures all types of knowledge, and the representation must be legible to both the expert and the prompt designer. Decision tables for conditional knowledge, concept maps for relational knowledge, process flows for procedural knowledge, cognitive demand tables for multi-dimensional expertise.

**Design implication**: The Excavate mode should produce multiple, linked representations rather than a single monolithic output. Each representation captures a different dimension of the expert's knowledge, and the set of representations forms the basis for prompt and pipeline design.

### 9.7 Respect the Centipede

Polanyi's tacit dimension and the centipede's dilemma converge on a warning: not all tacit knowledge should be made explicit. Some expertise works precisely because it's holistic and automatic. Decomposing it into explicit rules may destroy what makes it work. The agent should recognise when tacit knowledge is better captured as "the expert makes a judgment here" than decomposed into conditional logic.

**Design implication**: The output should include not just explicit knowledge but also markers for tacit judgment: "At this step, the expert uses perceptual expertise that resists decomposition. The AI system should present data for human judgment rather than attempting to automate this decision."

### 9.8 Connect to the Cognitive Mode Framework

Everything in this document exists within the larger framework described in `cognitive-stance-reference.md`. The Prompt Excavator's three modes are cognitive modes, and they should follow the principles:

- **Primer** is investigative work — it should use lenses, not seeds. "What kinds of questions would surface tacit knowledge about this type of work?" not "Ask these specific questions."
- **Excavate** is a mix of investigation (following threads in the narrative) and structuring (organising what's found) — compatible modes that can coexist.
- **Refine** is convergent (pinning down specific gaps) and can include light evaluation (assessing whether the elicited knowledge is sufficient) — but evaluation should not contaminate the investigation that surfaces the missing knowledge.

**Most importantly**: The Prompt Excavator itself should be designed as a pipeline, not a monolithic prompt. The Primer, Excavate, and Refine modes are cognitively distinct and should operate in clean contexts. Primer generates questions from domain knowledge. Excavate processes conversation through those questions' lens but follows the conversation where it leads. Refine evaluates completeness against a structured model and generates targeted follow-up.

---

## 10. Key References (Consolidated)

### Cognitive Task Analysis
- Crandall, B., Klein, G., & Hoffman, R. R. (2006). *Working Minds: A Practitioner's Guide to Cognitive Task Analysis*. MIT Press.
- Klein, G., Calderwood, R., & Clinton-Cirocco, A. (1986). Rapid decision making on the fire ground. *Proceedings of the Human Factors Society*, 30, 576-580.
- Klein, G., Calderwood, R., & Macgregor, D. (1989). Critical decision method for eliciting knowledge. *IEEE Transactions on Systems, Man, and Cybernetics*, 19(3), 462-472.
- Militello, L. G. & Hutton, R. J. B. (1998). Applied cognitive task analysis (ACTA). *Ergonomics*, 41(11), 1618-1641.
- Ericsson, K. A. & Simon, H. A. (1993). *Protocol Analysis: Verbal Reports as Data*. MIT Press.
- Vicente, K. J. (1999). *Cognitive Work Analysis*. Lawrence Erlbaum Associates.

### Requirements Engineering
- Beyer, H. & Holtzblatt, K. (1998). *Contextual Design*. Morgan Kaufmann.
- van Lamsweerde, A. (2009). *Requirements Engineering*. Wiley.
- Cockburn, A. (2001). *Writing Effective Use Cases*. Addison-Wesley.
- Carroll, J. M. (2000). *Making Use: Scenario-Based Design of Human-Computer Interactions*. MIT Press.
- Suchman, L. A. (1987). *Plans and Situated Actions*. Cambridge University Press.

### Motivational Interviewing and Coaching
- Miller, W. R. & Rollnick, S. (2013). *Motivational Interviewing* (3rd ed.). Guilford Press.
- Rogers, C. R. (1961). *On Becoming a Person*. Houghton Mifflin.
- Lawley, J. & Tompkins, P. (2000). *Metaphors in Mind*. Developing Company Press.
- Cooperrider, D. L. & Whitney, D. (1999). *Appreciative Inquiry*. Berrett-Koehler.
- Paul, R. & Elder, L. (2007). *Critical Thinking: Tools for Taking Charge of Your Professional and Personal Life*. Pearson.

### Design Thinking and Service Design
- Stickdorn, M., Hormess, M. E., Lawrence, A., & Schneider, J. (2018). *This Is Service Design Doing*. O'Reilly.
- Christensen, C. M. et al. (2016). *Competing Against Luck*. Harper Business.
- Dorst, K. (2015). *Frame Innovation*. MIT Press.
- Shostack, G. L. (1984). Designing services that deliver. *Harvard Business Review*, 62(1), 133-139.

### Expertise and Tacit Knowledge
- Polanyi, M. (1966). *The Tacit Dimension*. University of Chicago Press.
- Nonaka, I. & Takeuchi, H. (1995). *The Knowledge-Creating Company*. Oxford University Press.
- Dreyfus, H. L. & Dreyfus, S. E. (1986). *Mind Over Machine*. Free Press.
- Ericsson, K. A., Charness, N., Feltovich, P. J., & Hoffman, R. R. (Eds.) (2006). *The Cambridge Handbook of Expertise and Expert Performance*. Cambridge University Press.
- Shanteau, J. (1992). Competence in experts: The role of task characteristics. *Organizational Behavior and Human Decision Processes*, 53(2), 252-266.

### Knowledge Representation
- Novak, J. D. & Canas, A. J. (2008). The theory underlying concept maps and how to construct and use them. IHMC Technical Report.
- Alexander, C., Ishikawa, S., & Silverstein, M. (1977). *A Pattern Language*. Oxford University Press.
- Johnson, P., Diaper, D., & Long, J. (1988). Tasks, skills and knowledge: Task analysis for knowledge based descriptions. *Proceedings of the IFIP TC13 HCI Conference*, 23-28.

### Naturalistic Decision Making
- Klein, G. (1999). *Sources of Power*. MIT Press.
- Rasmussen, J. (1983). Skills, rules, and knowledge. *IEEE Transactions on Systems, Man, and Cybernetics*, 13(3), 257-266.
- Zsambok, C. E. & Klein, G. (Eds.) (1997). *Naturalistic Decision Making*. Lawrence Erlbaum Associates.
- Klein, G. et al. (2007). A data-frame theory of sensemaking. In R. R. Hoffman (Ed.), *Expertise Out of Context*. Lawrence Erlbaum Associates.

### Cognitive Science Foundations
- Kahneman, D. & Klein, G. (2009). Conditions for intuitive expertise. *American Psychologist*, 64(6), 515-526.
- Spiro, R. J. et al. (1992). Cognitive flexibility, constructivism, and hypertext. In Duffy & Jonassen (Eds.), *Constructivism and the Technology of Instruction*. Lawrence Erlbaum Associates.
- Chinn, C. A. et al. (2011). Expanding the dimensions of epistemic cognition. *Educational Psychologist*, 46(3), 141-167.

### Adjacent Fields
- Hutchins, E. (1995). *Cognition in the Wild*. MIT Press.
- Star, S. L. & Griesemer, J. R. (1989). Institutional ecology, 'translations' and boundary objects. *Social Studies of Science*, 19(3), 387-420.
- Engestrom, Y. (1987). *Learning by Expanding*. Cambridge University Press.
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship. In L. B. Resnick (Ed.), *Knowing, Learning, and Instruction*. Lawrence Erlbaum Associates.
- Hall, E. T. (1976). *Beyond Culture*. Anchor Books.
- Dervin, B. (1992). From the mind's eye of the user: The sense-making qualitative-quantitative methodology. In Glazier & Powell (Eds.), *Qualitative Research in Information Management*. Libraries Unlimited.
- Clark, H. H. & Brennan, S. E. (1991). Grounding in communication. In Resnick, Levine, & Teasley (Eds.), *Perspectives on Socially Shared Cognition*. APA.
- Kelly, G. A. (1955). *The Psychology of Personal Constructs*. Norton.
- Hollnagel, E. (2017). *Safety-II in Practice*. Routledge.
- Kvale, S. & Brinkmann, S. (2009). *InterViews: Learning the Craft of Qualitative Research Interviewing* (2nd ed.). Sage.
- Checkland, P. (1981). *Systems Thinking, Systems Practice*. Wiley.

### Interview Research
- Rubin, H. J. & Rubin, I. S. (2012). *Qualitative Interviewing: The Art of Hearing Data* (3rd ed.). Sage.
- Schegloff, E. A., Jefferson, G., & Sacks, H. (1977). The preference for self-correction in the organization of repair in conversation. *Language*, 53(2), 361-382.
