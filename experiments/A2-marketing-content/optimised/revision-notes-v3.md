# Revision Notes: SKILL-v3.md

**Revising from**: SKILL-v2.md (and v1, original)
**Revising to**: SKILL-v3.md
**Date**: 2026-03-18
**Architect findings used**: prompt-architect-analysis-v3.md

---

## The core problem v3 is fixing: v2's regression

v2 scored below baseline. The architect's v3 analysis identified the causes precisely:

1. **Criterion gates inside investigation**: "Do not move to Phase 2 until you have that angle. If you have several candidate angles, choose the one that most directly addresses the reader's emotional state and the product's most surprising truth. Commit to one." This is an evaluation checklist embedded inside what was supposed to be an open investigation. It converts exploration into a pass/fail gate.

2. **Process notes inside generation**: "Your investigation has two threads: Thread 1... Thread 2..." — structuring the investigation as a declared two-part process creates a convergent compliance posture before any writing begins. The model is executing a method, not following curiosity.

3. **Vivid role-framing in later phases**: "The draft exists. Now shift posture: you are an editor, not a writer." The phrase "you are an editor" is vivid role-framing — it activates editorial-mode language patterns at the exact moment the prompt wants the model to preserve the writer's voice. This is the anti-pattern of naming a mode while trying to resist its effects.

4. **Declared multi-phase architecture that couldn't deliver the separation it promised**: Phase labels (Phase 1: Investigate, Phase 2: Write, Phase 3: Polish) signal a sequential cognitive separation that cannot actually happen in a single context. The labels create the *appearance* of mode isolation without the reality. The model processes all phases' context from the start.

v3 removes all four of these patterns.

---

## What changed in v3

### 1. Phase labels removed entirely

v2 had three labeled phases. v3 has three sections with descriptive headings: "Before you write anything," "Writing for the reader," "Once the draft exists."

These headings describe the temporal sequence of tasks without declaring cognitive phases. They do not promise mode isolation. The prose in each section establishes the appropriate stance — the heading does not carry the cognitive load.

This is the most significant structural change. Every phase label was creating a criterion-gate posture ("I have completed Phase 1 and am now entering Phase 2") that is incompatible with how creative writing actually works.

### 2. Investigation boundary: exploration, not checklist

v2 used two declared threads with bold labels:
> "Thread 1: The product / Thread 2: The reader"

This structured the investigation as a two-part process to execute rather than a question to follow. v3 replaces this with a flowing investigation invitation that names what to look for without enumerating a checklist:

> "Follow what surprises you. A beta metric that defies the industry norm, a user quote that sounds human rather than rehearsed, a detail whose implications aren't in the brief explicitly — these are where the piece lives."

The investigation guidance still serves its core purpose (pointing attention toward the brief's most interesting material, away from template-filling) without creating a procedural framework the model must comply with.

### 3. The angle requirement: implicit, not gated

v2 made the angle an explicit gate: "Do not move to Phase 2 until you have that angle." This is a criterion gate — the model must evaluate whether it has met the standard before proceeding.

v3 makes the angle the natural outcome of genuine investigation: "Let the investigation run until you can name it in one sentence." This is temporal guidance (run until you can name it) rather than a pass/fail evaluation. The difference is subtle but the cognitive effect is real: one posture is generative (keep going until something clicks), the other is evaluative (have I met the standard yet?).

The angle requirement is preserved — it remains the pivot between investigation and writing — but it is no longer framed as a gate.

### 4. Writing guidance: lighter and shorter

v2's Phase 2 writing guidance ran through detailed principles and then channel-specific content type guidance. v3 preserves the core principles but with less structural framing around them. The principles are stated concisely rather than elaborated:

v2: "Close with consequence, not summary. The reader should arrive at the CTA already wanting to act — not because you told them to, but because the piece built the case. The CTA should feel like opening a door the reader is already standing at, not like an interruption at the end of an article."

v3: "Close with consequence. The reader should arrive at the call to action already wanting to act, because the piece built the case. The CTA opens a door they're already standing at."

The principle is intact. The elaboration is reduced. For creative work, shorter guidance trusts the model's existing capability more than longer guidance does. This is the "less structure for creative work" principle from the task brief.

### 5. Post-generation phase: functional framing instead of role assignment

v2: "The draft exists. Now shift posture: you are an editor, not a writer."
v3: "The piece is written. Now read it as an editor, not a writer."

Removing "you are an editor" (role assignment) and replacing with "read it as an editor" (functional instruction) avoids the vivid role-framing anti-pattern. The instruction is the same — adopt an editorial posture — but "read it as" activates the editorial perspective without triggering the full editorial-identity language patterns that "you are an editor" would invoke.

### 6. Voice preservation: integrated, not appended

v2 had a dedicated "voice preservation check" section at the end of Phase 3. This was correctly positioned (after compliance checks) but structured as a final checklist item, making it feel like one of several concerns at the same level as formatting.

v3 integrates voice preservation into the section framing itself: "the voice you built is the piece's most important asset — your job here is to check compliance without flattening it." This makes voice preservation the governing constraint of the entire post-generation phase, not a final check among equals.

The specific instruction is also present: "If the editorial pass flattened the voice — go back and restore it, then find a lighter way to satisfy whatever requirement caused the damage." This replaces v2's elaborate list of flatness signals with a single actionable directive.

---

## What was preserved from v2

- The investigation-first sequence (look before you write)
- The angle as the pivot before writing begins — described temporally, not as a gate
- "Write the headline last" — this was new in v2 and correct; kept
- "Do not use a formula" — implicit in v3 ("use what the material gave you") rather than explicit, which is lighter
- Qualitative writing principles: one reader, earn every section, let evidence land, close with consequence
- Channel-specific guidance as principles, not templates
- SEO guidance in the post-generation section with the "sentence wins" constraint
- No numeric anchors in the generative section; technical SEO limits retained

---

## The core structural principle guiding v3

v2 trusted structure more than the model. v3 trusts the model more than structure.

For a recognition-primed creative task where the model has extensive training on marketing writing, the primary intervention needed is epistemic stance (investigate before concluding) and mode separation (compliance after creation). Both are present in v3. Everything else — phase labels, thread enumeration, gating criteria, role assignments — was adding overhead without adding capability.

The architect's v3 analysis states this directly: "the most important single intervention is adding an investigation boundary before any template." v3 is built around that boundary. Everything else is kept as light as possible.

---

## Diagnostic signals to watch for in testing

- **Opening paragraph**: does it recreate a specific experience of the problem, or does it reach for a formula hook?
- **Headline**: does it argue something, or label the topic?
- **The VP Eng quote**: placed as a narrative beat that lands with weight, or listed among other data points?
- **Section count across runs**: does it vary with brief complexity, or converge to 3-5 sections uniformly?
- **Overall register**: one person with conviction, or competent copy produced by committee?

The critical comparison is with v2: does removing the criterion gates and structural scaffolding produce more natural voice without losing the angle-finding discipline that v2 introduced?
