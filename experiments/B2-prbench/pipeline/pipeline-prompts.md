# Tier 3: Pipeline Prompts

**Tier**: 3 — Trust chain pipeline
**Applies to**: Both tasks (easy finance, hard legal)
**Stages**: 3 (Discovery → Analysis → Advisory Synthesis)
**Execution**: Sequential, separate sessions — not `/clear`, separate context windows

---

## Pipeline overview

Three stages, each with a clean context window. The epistemic stance at each stage is set explicitly and cascades through mode, register, and language patterns. Structured handoffs between stages carry information without cognitive residue — the schema is the cognitive boundary.

Stage 1 discovers without evaluating. Stage 2 analyses without advising. Stage 3 advises without re-discovering. Each stage does one type of thinking, cleanly.

---

## Why three stages, not two or four

The professional reasoning task requires four cognitive modes: investigation, analysis, evaluation, and advisory reframing. Investigation + evaluation is the toxic pair — the pre-filtering mechanism. Separating them is not optional if you want genuinely open investigation.

But a pure four-stage pipeline (one mode each) over-engineers. Analysis and evaluation are compatible in the same context — "understand how things connect, then assess the implications" is a natural sequence that doesn't create interference. So stages 2 and 3 each handle a compatible pair:

- Stage 2: analysis + evaluation (understand connections, assess what they mean)
- Stage 3: advisory synthesis + reframing (commit to a narrative, translate for the professional)

This gives us three stages rather than four, without sacrificing cognitive separation where it matters.

---

## Agent map

### Stage 1: Discovery Agent

**Epistemic stance**: "I am mapping what is here. I have not started evaluating anything yet."

**Types of thinking**: Investigation + light structuring (lenses guide, they don't constrain)

**Receives**: The task question. For multi-turn tasks: the prior conversation as background context only, explicitly framed as factual background rather than a cognitive mode to inherit.

**Produces**: Structured observations — a schema-bound document with defined fields. Not prose. Not findings. Observations. The word choice matters: "observation" carries an exploratory register; "finding" carries a judgment register.

**Why separate**: This stage must explore freely. If it knows that Stage 3 needs to recommend, it pre-filters — surfacing only what it can already advise on. With a clean context containing only the question and this prompt, there is no advisory pressure. The model follows threads to see where they lead, not to see if they lead somewhere actionable.

---

### Stage 2: Analysis Agent

**Epistemic stance**: "I am understanding how these pieces connect. I am not advising yet."

**Types of thinking**: Analysis (relationship-mapping) + evaluation (what do these connections mean?)

**Receives**: The Stage 1 handoff schema (structured observations). Not Stage 1's prose, not the original task question with Stage 1's exploratory tone. A clean schema document.

**Produces**: A structured analytical framework — relationships, tensions, implications, and uncertainty tiers. Not recommendations. The framework is compressed enough for Stage 3 to hold in context while writing.

**Why separate**: Analysis requires committing to relationships — "these two rules are in tension," "this fact is determinative." That commitment conflicts with the open exploration of Stage 1. And analysis conflicts with the advisory register of Stage 3 — the analytical mode stays close to the text, while advisory mode must step back and ask "what does this person need to hear?" Separating these prevents both contamination directions.

---

### Stage 3: Advisory Synthesis Agent

**Epistemic stance**: "I am advising a professional who needs to act. I have a comprehensive analytical framework. My job is to translate it into guidance."

**Types of thinking**: Synthesis (commit to a narrative) + reframing (translate for the professional audience)

**Receives**: The Stage 2 handoff schema (analytical framework). Not Stage 2's reasoning process — the compressed output of that reasoning.

**Produces**: The final response, in the format specified by the task question.

**Why separate**: The advisory register is clean here because it has not been contaminated by the analytical posture of Stages 1 and 2. The model can make the lateral moves — supplemental insight, uncertainty acknowledgment, practical reframing — because it received a comprehensive framework rather than having to build one from scratch while also being concise. Supplemental insight appears because the analytical work is already done; there is cognitive space to follow threads beyond the direct question.

---

## Handoff schemas

### Stage 1 → Stage 2 handoff

What crosses: Structured observations only. No exploratory prose. No hedged "this might be worth noting" asides. No analysis.

What gets dropped: Stage 1's thread-following prose, tentative observations that didn't resolve into anything specific, the "I'm mapping this out" register.

**Format** (Markdown schema document — Stage 2 receives this, not Stage 1's full output):

```
## Stage 1 Handoff: Structured Observations

### Applicable rules and frameworks
[List each rule, statute, regulation, or principle identified as relevant.
For each: name it, state what it does, note the source/authority.]

### Significant facts
[List the facts in the situation that are analytically significant —
facts that will interact with the rules above. Do not analyse the interaction yet.
Just identify which facts matter and why they are notable.]

### Rule-fact connection points
[Identify where the rules connect with the facts — the specific intersections
that require analysis. Do not analyse the intersections. Name them.]

### Open questions and unsettled law
[List interpretive questions that are genuinely unresolved: contested statutory
meanings, lack of controlling authority, areas of active regulatory development,
questions where reasonable interpretations differ. For each: state what is unsettled
and why it is unsettled.]

### Considerations beyond the direct question
[Identify what a professional advising this client would need to address
that the question did not directly ask about. Surface these without evaluating
their significance yet.]

### What this situation is NOT
[Identify scope boundaries — what rules, frameworks, or analytical paths were
considered and set aside as not applicable, and briefly why.]
```

**Compression note**: Stage 2 receives this schema document as its primary input. The schema forces compression: Stage 1's exploratory prose becomes discrete, structured entries. The schema carries information; it does not carry Stage 1's cognitive posture.

---

### Stage 2 → Stage 3 handoff

What crosses: The analytical framework — compressed conclusions about relationships, implications, and uncertainty. Not the reasoning that produced those conclusions.

What gets dropped: Stage 2's analytical reasoning process, the "I'm working through how X connects to Y" voice, tentative analytical paths that didn't contribute to the framework.

**Format** (Markdown schema document — Stage 3 receives this, not Stage 2's full output):

```
## Stage 2 Handoff: Analytical Framework

### Core analytical conclusions
[State the main conclusions of the analysis — what the rules mean
when applied to these specific facts. Be direct. These are the conclusions
Stage 3 will synthesise into professional guidance.]

### Rule-fact applications
[For each significant rule-fact intersection identified in Stage 1:
state how they interact, what the interaction means, and what it implies.
This is the heart of the analysis.]

### Tensions and ambiguities
[Identify where the analysis reveals genuine tension — conflicting rules,
facts that push toward different conclusions, interpretive choices that
materially affect the outcome. State the tension clearly and what each
resolution implies.]

### Uncertainty tiers
[Classify what is clear, what is uncertain but manageable, and what is
genuinely unresolved. For each uncertain area: state why it is uncertain,
what turns on it, and what a professional would need to know to navigate it.]

### Supplemental considerations
[Analytical observations that extend beyond the direct question but are
relevant to a professional advising this client. Stage 3 will determine
whether and how to include these in the final response.]

### What the analysis does not resolve
[Be explicit about the limits of this analysis. What questions remain
open? What would require additional facts, legal authority, or regulatory
guidance to answer? This is substantive — the advisory stage needs to
know what it cannot confidently tell the client.]
```

**Compression note**: Stage 3 receives this schema as its primary input. Stage 3 does not receive Stage 1's handoff, Stage 2's reasoning, or the task question in analytical framing. It receives compressed analytical conclusions and is responsible for synthesising them into professional guidance.

---

## The prompts

---

### Stage 1 Prompt: Discovery

```
You are mapping the analytical landscape for a professional legal or financial question. Your job at this stage is to identify what is relevant — not to evaluate, advise, or conclude.

You are discovering. You are not finding. An observation is what you notice is there. A finding is a conclusion about what it means. You are producing observations only.

[IF MULTI-TURN TASK — include this block, otherwise omit:]
The question you are answering is a follow-up in a conversation. The prior exchange is provided as background — it tells you what has already been addressed and establishes facts about the situation. Do not let the analytical posture or format of the prior response shape how you explore this question. Approach this question fresh.
[END MULTI-TURN BLOCK]

Work through the following, in order:

First, identify every rule, statute, regulation, framework, principle, or interpretive guidance that is relevant to this question. For each one: name it, state what it does, and note its authority. Do not stop when you have enough — keep going until you have identified all of them, including the less obvious ones. Rules you identify but set aside are still worth naming, with a note on why they don't apply.

Second, identify the facts in the situation that are analytically significant. Which facts will interact with the rules you identified? What about the situation is distinctive or unusual in ways that matter legally or financially?

Third, identify where the rules connect with the facts. Name the specific intersections — the places where a rule bears directly on a fact. Do not analyse what the connection means yet. Just name it.

Fourth, identify what is genuinely unresolved. Where is the law unsettled? Where do reasonable interpretations differ? Where is there no controlling authority? Where is regulatory interpretation actively developing? Surface these openly — unresolved questions are not a failure to answer; they are substantive observations.

Fifth, identify what a professional advising this client would need to address that the question did not ask about directly. Follow threads beyond the direct question to see where they lead.

Produce your output in the Stage 1 handoff schema. Use the schema fields as containers for your observations. Write in direct, precise language. Do not write prose analysis — write structured observations.
```

**Schema to append**: Stage 1 handoff schema (above). Include the full schema structure after the prompt so the model has the output format.

---

### Stage 2 Prompt: Analysis

```
You are analysing the relationship between rules and facts in a professional legal or financial question. You have received a structured set of observations from a discovery phase. Your job is to understand how the pieces connect — not to advise, not to recommend.

You are analysing. You are not yet advising. Analysis commits to understanding what things mean; it does not commit to what a client should do about it.

The Stage 1 observations you received identify relevant rules, significant facts, rule-fact connection points, open interpretive questions, and supplemental considerations. Your job is to work through those connections and produce an analytical framework.

Work through the following:

First, take each rule-fact connection point identified in the observations. Analyse the intersection: what does the rule mean when applied to this specific fact? Is the application clear or contested? What does the intersection imply for the situation?

Second, where the observations identified tensions or unsettled questions, analyse them. What are the competing interpretations? What turns on which interpretation is correct? What would a reviewing authority or court likely look at? What are the strongest arguments on each side?

Third, classify the analytical conclusions by uncertainty. What is clearly established? What depends on interpretive choices where reasonable positions differ? What is genuinely unresolved and cannot be answered confidently without additional facts or authority?

Fourth, trace the implications of the analysis. If the analysis points in a particular direction, what does that mean for the situation? Identify implications even if they are uncomfortable or go beyond what the question directly asked about.

Fifth, note what the analysis cannot resolve. Where do the observations identify open questions that the available rules and facts do not answer? Be explicit about these limits — the advisory stage needs to know what cannot be stated with confidence.

Produce your output in the Stage 2 handoff schema. Be direct. Do not reproduce your reasoning process — state the conclusions of that reasoning. The schema is a compressed analytical framework, not a record of how you worked through it.
```

**Schema to append**: Stage 2 handoff schema (above). Include the full schema structure after the prompt.

**Input to this stage**: Stage 1 handoff document only. Not Stage 1's full prose output, not the original task question with exploratory framing. The handoff document is the complete input.

---

### Stage 3 Prompt: Advisory Synthesis

```
You are a professional adviser writing a response to a legal or financial question on behalf of a client. You have received a comprehensive analytical framework from a prior analysis phase. Your job is to synthesise that framework into professional guidance the client can act on.

You are advising. You have already done the discovery and analysis — that work is in the framework you received. Your job now is to translate it into what this professional needs to hear.

Write as a trusted adviser who knows the full picture: what is clear, what is uncertain, what requires caution, and what additional considerations matter for this client's decisions. Do not perform analysis you have already done — synthesise the conclusions of that analysis.

On handling uncertainty: do not treat uncertainty as a weakness to hedge around at the end. Uncertainty is substantive information. Where the law is unsettled, say so directly, explain why it is unsettled, and tell the client what that means for their decisions and risk exposure. A risk-tiered conclusion — "this is clear, this is a managed risk, this is genuinely unresolved" — is more useful than false confidence.

On supplemental insight: the analytical framework may include considerations beyond the direct question. Use your judgment about which of these belong in the response. A professional adviser surfaces what the client needs to know, not just what the client asked about.

On practical utility: translate analysis into action. Tell the client not just what the law says but what they should do, in what order, and why. Where there are multiple viable paths, explain the trade-offs.

Write the response in the format specified in the question. If the question specifies paragraph form without headers or lists, write in prose. If no format is specified, use the structure that best serves the guidance.

[IF MULTI-TURN TASK — include this block, otherwise omit:]
This response is the second turn in a conversation. The prior exchange covered different regulatory territory. Write this response as a continuation of that conversation — you can reference the prior exchange where relevant, but this question stands on its own and should be answered completely.
[END MULTI-TURN BLOCK]
```

**Input to this stage**: Stage 2 handoff document only. Not Stage 1's handoff, not Stage 2's full reasoning, not the original task question in analytical framing.

**Output**: The final response. For the hard task: prose, no headers, no bullet points, no lists, no charts — exactly as the question specifies.

---

## Execution notes

**Session isolation**: Each stage runs in a completely separate session — not `/clear`, not a new conversation in the same window. Separate context windows. The isolation is the mechanism. Contaminating it recreates the monolithic pattern.

**Handoff execution**:
1. Run Stage 1. Copy the handoff schema section from Stage 1's output (not the full response).
2. Open a new session. Paste Stage 2 prompt + Stage 2 schema template. Add Stage 1 handoff document as the task input. Run Stage 2.
3. Open a new session. Paste Stage 3 prompt. Add Stage 2 handoff document as the task input. Run Stage 3.

**For the easy task (single-turn finance)**:
- Stage 1 input: the task question as-is. Omit the multi-turn blocks from Stage 1 and Stage 3 prompts.
- Stage 3 output: the finance report. No format constraints specified in the question, so use structure that serves clarity.

**For the hard task (multi-turn legal)**:
- Stage 1 input: the Turn 2 question, plus the full Turn 1 conversation (user question + assistant response) as prior context. Include the multi-turn block in Stage 1 and Stage 3 prompts.
- Stage 3 output: prose response, no headers, no bullet points, no lists, no charts — matching the format instruction in the Turn 2 question.
- The Turn 1 assistant response is heavy, structured, bulleted, and authoritative. Stage 1 receives explicit instruction to not inherit that cognitive posture. Stage 2 and Stage 3 never see the Turn 1 response at all — they receive only the handoff schemas.

**What the handoff schemas strip**:
The Stage 1 handoff strips: Stage 1's exploratory prose, tentative threads, "interesting because" framing, and the turn-by-turn voice of discovery.
The Stage 2 handoff strips: Stage 2's analytical reasoning process, the "how I worked through this" voice, and the evaluative register of analysis.
Stage 3 receives clean conclusions and can write from an advisory epistemic stance without fighting the analytical residue.

---

## Predicted mechanism

The pipeline's value is not that it does more work — each stage is roughly the same length as a section of the monolithic response. The value is that each stage does its work without the interference of incompatible modes.

Stage 1 can follow threads that do not lead anywhere actionable, because it has no obligation to advise. This is where supplemental insight originates — not from the advisory stage asking "what else might be useful?" but from the discovery stage following threads without pre-filtering them through "can I recommend something based on this?"

Stage 3 can acknowledge uncertainty directly and substantively, because it received explicit uncertainty tiers in the handoff schema rather than having to surface and acknowledge uncertainty while simultaneously being authoritative. The analytical stage already did the work of classifying what is settled versus unresolved. Stage 3 inherits those classifications and translates them into advisory language.

Application of law to facts improves because Stage 2's dedicated function is exactly that connection — it is not doing it as a compressed section of a comprehensive response. It has a full context window to trace implications, identify tensions, and classify uncertainty before those conclusions are handed to Stage 3.
