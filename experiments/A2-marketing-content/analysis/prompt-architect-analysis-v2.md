# Prompt Architect Analysis: A2 Marketing Content — V2 (Voice-Continuity Aware)

**File analysed**: `experiments/A2-marketing-content/original/SKILL.md`
**Prior analysis**: `experiments/A2-marketing-content/analysis/prompt-architect-analysis.md`
**Date**: 2026-03-17
**Context**: Re-analysis with updated toolkit including voice-continuity and data stance concepts

---

## 1. What the prompt is actually asking for

The prompt presents as a reference guide but operates as a generation instruction: when loaded into context alongside a product brief, it is the cognitive environment in which a model must produce compelling marketing copy.

The cognitive work the task actually requires:

- **Audience investigation** — understanding this specific reader's experience, frustrations, and what would make them stop scrolling
- **Angle discovery** — finding what makes this specific product interesting, what reframe unlocks the story
- **Generation** — writing copy that sustains voice, earns the reader's attention paragraph by paragraph
- **Compliance** — ensuring SEO requirements, character limits, and structural conventions are met

The prompt's cognitive posture delivers: template-filling (fixed structural slots for every content type), evaluation criteria (SEO checklist, readability rules, channel conventions, character counts), and content seeds (headline formula list, hook formula list, CTA examples). The actual generative work — the investigation and writing — receives no posture-establishing guidance at all. The model is given the frame but not the picture.

---

## 2. Threshold question: recognition-primed or investigation-required?

This task sits at the boundary. That ambiguity is itself the finding.

**The case for recognition-primed**: Marketing content for a SaaS product launch is a well-trodden genre. The model has extensive training data on how to write product launch blog posts, what async collaboration tools are, who engineering managers are, and what their frustrations look like. It can pattern-match from training to produce competent copy without investigating the specific brief deeply.

**The case for investigation-required**: The quality ceiling on this task is not "does the copy follow genre conventions" — it is "does the copy make an engineering manager feel seen." Achieving that requires discovering what this specific audience's morning looks like, what the emotional stakes of timezone collaboration are, what's interesting about THIS product's angle rather than the category's angle. The insight that "the engineering manager becomes middleware" is not in the brief and does not come from pattern recognition — it comes from investigation of what the brief implies about the reader's daily experience.

**Resolution**: Recognition-primed execution reaches the floor (competent copy, correct structure). The ceiling requires investigation. Tier 2 can meaningfully raise the floor. Tier 3 can raise the ceiling — but whether that ceiling gain is worth the pipeline cost depends on the voice-continuity question.

---

## 3. Voice-continuity assessment (NEW)

**This is a voice-continuity task.** The brief specifies a distinctive brand voice ("explain to a smart friend, confident but not arrogant, empathetic to pain, slightly witty"). The output will be read for persuasion and engagement. The quality gap between "competent" and "great" is primarily about how it reads, not what it covers. A human writer would develop their angle and voice through the same process of exploring the material.

**Evidence from previous runs**: The external blind evaluators split on voice:
- Claude Web ranked Tier 2 first on voice — "nails the brief's 'explaining to a smart friend' instruction," Tier 3 "reads slightly more 'edited' than 'written'"
- Gemini ranked Tier 3 first — "superior voice, expert-level SEO integration"

The split is diagnostic. The Claude Web evaluator detected something real: the 4-stage pipeline's editorial pass (Stage 4) introduced "editedness" that a careful reader could sense. The pipeline produced higher peak moments (best individual sentences) but the Tier 2 version had more consistent, natural-feeling voice because there was no post-processing editorial stage.

**What this means for pipeline design**: For this task class, investigation + generation may be a *compatible* pair. The investigation funnels toward expression, not solutions. The writer discovers voice by engaging with the material. Separating them with a structured handoff (plan about voice) forces reconstruction from descriptions rather than organic development.

---

## 4. Where modes interfere

### Primary: evaluation criteria suppressing voice

The SEO checklist, writing best practices, and character count targets create an evaluation posture active during generation. Baseline runs scored 2/5 on Voice and Engagement. The evaluation criteria switch the model from "what does this reader need to feel" to "which criteria am I satisfying."

### Secondary: numeric anchors producing structural uniformity

Baseline runs showed "remarkably uniform" structure: same headline formula across 2/3 runs, same 5-7 section count, similar word counts. Natural variation scored 2/5 — the lowest in the experiment.

### Tertiary: seed-based headline/hook formulas

The headline formula list produced formula headlines in every baseline run: "Relay: The Async Collaboration Platform Built for [X]." Removing the formula list freed angle discovery.

---

## 5. What to do about it

### Tier 2: Prompt-level optimisation

Same recommendations as v1 analysis, confirmed by experimental results:
1. Remove numeric ranges from blog post template → qualitative guidance
2. Replace headline formula list with a lens (what's the headline's job)
3. Add explicit pre-generation investigation phase
4. Relocate SEO checklist and writing best practices to post-generation review
5. Keep templates for genuinely convergent formats (press release, case study)

### Tier 3: Pipeline reconstruction — REVISED from 4-stage to 2-stage

**Previous design (4-stage)**: Brief Explorer → Content Architect → Writer → Editor
**Revised design (2-stage)**: Investigate-and-Write → Editor

**Stage 1: Investigate and Write** (investigation + generation, single context)
The same agent understands the brief and writes the copy. No structural outline crossing between investigation and writing — the angle emerges from engagement with the material. No SEO criteria, character counts, or compliance checklists in context. The only instruction is: understand this product, this audience, and write the piece that would make an engineering manager stop scrolling.

**Stage 2: Editor** (evaluation + compliance, clean context)
Receives only: the draft and the SEO requirements (primary keyword, secondary keywords, target length, CTA) as a separate structured list. No investigation notes, no strategic rationale. Applies channel conventions, keyword placement, compliance. Explicit instruction: polish for compliance, preserve voice.

**Why 2 stages instead of 4**: The Content Architect stage created a synthetic boundary between investigation and writing that doesn't exist when a human writer works. A skilled copywriter reads the brief and starts writing — the investigation and angle-finding ARE the early drafts. The Editor stage's risk is concentrated and manageable with proper scoping ("do not rewrite for voice").

### The trade-off to test

Tier 2 may produce stronger consistent voice (no editorial "editedness" at all).
Tier 3 (2-stage) may produce stronger peak moments (dedicated creative context) with minimal editorial residue.
The experiment should test both against the original baseline.

---

## 6. Diagnostic signals for the re-run

- **Opening paragraph**: Question hook from formula = template completion. Scenario that recreates reader's experience = genuine voice.
- **Headline type**: Keyword string = seeds anchoring. Reframe or argument = angle discovery working.
- **VP Eng quote treatment**: One data point among many = template. Staged with narrative beat = craft.
- **CTA quality**: "Start your free trial" = convergent completion. Pragmatic challenge = voice held through.
- **Section count across runs**: Uniform = anchors dominating. Variable = model responding to material.
- **"Edited" vs "written" feel**: Does the piece sound like one person wrote it with conviction, or like competent copy that was polished by committee?
