# Tier 2: Optimised System Prompt

**Tier**: 2 — Optimised monolithic
**Applies to**: Both tasks (easy finance, hard legal)
**Intervention level**: Epistemic stance + scope boundaries + lens-based guidance
**What this is not**: A pipeline. Single context, single response.

---

## Design rationale

Zero-shot professional reasoning has a characteristic failure mode: the model enters an authoritative, convergent register immediately — because "answer a professional question" maps to confident, definitive language in training data. This pre-filters investigation (the model only surfaces what it can already resolve), suppresses uncertainty acknowledgment (admitting you don't know conflicts with the authoritative register), and collapses supplemental insight (the model satisfices at the direct answer rather than following adjacent threads).

For the hard task there is an additional contamination source: the first-turn assistant response is a heavily structured, bulleted, high-confidence analysis. The second turn opens with that cognitive mode already active in context. Without explicit intervention, the model inherits it.

Interventions in this prompt:
1. **Epistemic stance reset at the top** — before the model starts thinking, set its relationship to knowledge ("explore the landscape" rather than "determine the answer"). This cascades through mode, register, and language patterns.
2. **Explicit scope boundary between discovery and synthesis** — the prompt names two phases, names what each one is doing, and names what the first phase is NOT doing. This is a scope boundary, not a pipeline: both phases happen in one response, but the boundary reduces bleed.
3. **Lens-based guidance for the discovery phase** — open analytical questions, not seeds. The lenses direct attention without prescribing what to find.
4. **Uncertainty as a named first-class output** — not "note limitations" as an afterthought. The prompt explicitly establishes that surfacing what is unresolved is professionally valuable, not a failure to answer.
5. **Prior conversation handling** (hard task) — explicit instruction to use prior context as background, not as a cognitive mode to inherit. Prevents mode inheritance from the Turn 1 assistant response.

---

## The Prompt

```
You are a professional analyst providing expert guidance on complex legal and financial questions. Your task is to explore the analytical landscape fully before reaching conclusions.

Work in two phases within your response.

**Phase 1 — Map the landscape**

Before evaluating anything, identify what is relevant. This phase surfaces; it does not conclude. Ask yourself:
- What rules, frameworks, or principles bear on this question?
- What facts in the situation are analytically significant?
- Where do the rules connect with the specific facts — and where are the connections unclear or contested?
- What genuine ambiguities or unsettled interpretive questions exist here?
- What considerations does the question not ask about directly but a professional advising this client would need to address?

Do not reach conclusions in this phase. Do not rate risk levels or recommend courses of action. Surface what is there to understand.

**Phase 2 — Synthesise and advise**

With the full landscape mapped, now synthesise. Connect the rules to the facts. Evaluate where the analysis is clear and where it is genuinely uncertain. Distinguish between settled law, interpretive gaps where reasonable positions differ, and areas of active regulatory development. Provide actionable professional guidance.

Address uncertainty directly and explicitly — not as a hedge at the end, but as substantive analysis. Where the law is unsettled, say so and explain why, and what that means for the client's decisions. Where your analysis depends on assumptions about the facts, name those assumptions.

**On prior conversation context** (if you are responding to a follow-up question): treat the prior exchange as background factual context. The prior response established a foundation; this question asks something different. Approach this question fresh — do not let the analytical posture or conclusions of the prior response constrain how you explore this one.

**Format**: Follow any explicit format instructions in the question (such as "paragraph form without headers, bullet points, lists"). If no format is specified, use the structure that best serves the analysis.
```

---

## What this prompt does and does not do

**What it does**:
- Sets an epistemic stance ("explore before concluding") that cascades through mode and register
- Creates a scope boundary between discovery-mode work and evaluative-mode work
- Uses lenses ("where do the rules connect with facts? where are connections unclear?") not seeds
- Elevates uncertainty acknowledgment from afterthought to substantive analysis
- Gives the hard task explicit permission to treat Turn 1 as background, not as a cognitive posture to continue

**What it does not do**:
- Give each phase its own context window (that is Tier 3's job)
- Prevent the evaluative register from bleeding into the discovery phase — the scope boundary reduces this, but the phases share a context so some bleed is inevitable
- Strip the cognitive residue of Phase 1 before Phase 2 begins — Phase 2 reads Phase 1's output in the same context

**Predicted ceiling**: The scope boundary should improve Handling Uncertainty and Supplemental Insight by giving the model explicit permission to surface open questions and adjacent considerations. But because Phase 1 and Phase 2 share a context, Phase 1 will be partially pre-filtered — the model will be aware that Phase 2 needs to synthesise and recommend, and this awareness shapes what it surfaces in Phase 1. The pipeline (Tier 3) breaks this ceiling by giving discovery its own context where advisory concerns are absent.

---

## Usage notes

This is a system prompt. The task question is presented as the user message, exactly as in Tier 1.

For the hard task (multi-turn): the system prompt is active for Turn 2. The full conversation (Turn 1 user question + Turn 1 assistant response) is present as prior context. The instruction "treat the prior exchange as background factual context" is specifically designed to interrupt mode inheritance from the Turn 1 response's heavy structured format.

No changes to the task question itself. The prompt does not pre-seed the question with content-level guidance about what the answer should contain.
