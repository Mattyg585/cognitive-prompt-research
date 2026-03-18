# Pipeline V3 Design Notes

## What changed from v2 and why

Pipeline v2 won the experiment on voice. The 2-stage structure (creative + compliance) is correct and is preserved in v3. The changes in v3 are narrower: they fix the same anti-patterns in the creative agent's instructions that caused the Tier 2 v2 regression, without touching the architectural decisions that made v2 work.

---

## The v2 regression and its relevance to Stage 1

Tier 2 v2 scored below baseline. The causes were:

1. **Criterion gates inside investigation**: "Do not move to Phase 2 until you have that angle. Commit to one." This is a pass/fail evaluation embedded in what should be open exploration.

2. **Declared thread structure in investigation**: "Thread 1: The product / Thread 2: The reader" structured the investigation as a method to execute rather than a question to follow.

3. **Vivid role-framing**: "you are an editor, not a writer" activates editorial-identity language patterns at exactly the moment the prompt wants the model to preserve writer voice.

4. **Phase labels as false promises**: Phase 1 / Phase 2 / Phase 3 labelling signals cognitive separation that a single context cannot deliver.

These patterns appeared in Tier 2 v2's monolithic prompt. The v2 pipeline creative agent (`investigate-and-write.md`) had similar patterns — notably the explicit "two threads" structure and declarative framing ("A writer reads a brief differently than a strategist or an analyst. You are not extracting information — you are looking for..."). The v2 pipeline performed better than v2 Tier 2 because context isolation does real work: SEO requirements never entering Stage 1's context is a genuine cognitive boundary. But the creative agent's investigation guidance carried some of the same overhead.

v3 addresses this in the creative agent while preserving the structural isolation that made v2 pipeline work.

---

## What changed in the creative agent

**Investigation guidance: from method to orientation**

v2:
> "You are a writer who does their own research... A writer reads a brief differently than a strategist or an analyst. You are not extracting information — you are looking for the thing that makes this piece worth reading."
> "Your investigation has two threads: Thread 1: The product... Thread 2: The reader..."

v3:
> "Read the brief as a writer looking for the piece — not a writer looking for information to put in the piece... Read once for orientation. Then read again for the thing that doesn't announce itself..."

The change: from declared method (two named threads, role contrast) to orientation (how to read, what to follow). v3 gives the same guidance — look at the product's surprising details, identify the specific reader — without structuring it as a numbered process to complete.

**Angle guidance: temporal rather than gated**

v2:
> "Let the investigation run until the angle is clear. Do not start writing before it is."

v3:
> "Write when you have the angle..."

"Do not start writing before it is" is a gate — it implies the model should evaluate whether the condition is met. "Write when you have the angle" is temporal — it implies writing begins naturally when the angle arrives. Both aim at the same behaviour; v3's framing is less likely to activate compliance-checking posture during the investigation.

**Writing guidance: principles without structural overhead**

v2's writing guidance was well-constructed but slightly elaborate in its framing ("Once you have the angle, write. The angle governs every decision from here..."). v3 trusts the model's writing capability more. The same principles are present — one person, earn every section, let evidence hit hard, close with consequence, headline last — stated more directly with less scaffolding around them.

**What was not changed**

The core structural insight from v2 is preserved intact:
- Brief only in Stage 1's context — no SEO requirements, no compliance checklists
- SEO requirements passed as a separate structured block to Stage 2, not embedded in prose
- The editor's explicit scope restriction: do not rewrite for voice, do not improve the prose
- The voice preservation check after editing, with specific flatness signals
- The "sentence wins" principle for keyword placement conflicts
- Editorial notes appended to the final piece documenting every change

These mechanisms worked in v2. v3 does not change what worked.

---

## The cognitive mode picture

```
Stage 1: Creative Agent
  Investigation + Generation (compatible for voice tasks)
  Context: brief only — no evaluation criteria, no compliance checklists
  Stance: curious writer following what's interesting

Stage 2: Compliance Editor
  Evaluation + Compliance (compatible — both criteria-referenced)
  Context: draft + structured SEO requirements (separate block)
  Stance: careful editor with explicit voice-preservation constraint
```

The key structural protection remains identical to v2: SEO requirements never appear in Stage 1's context. The writer writes without knowing the keyword targets. This is a genuine cognitive boundary, not a declared phase that the same context window still contains.

---

## Why 2 stages remains the right architecture

The architect's v3 analysis confirms this. The productive separation for a voice-continuity task is creation versus compliance — not investigation from generation, and not four separated stages of brief normalisation, angle ideation, drafting, and editing.

Investigation and generation are compatible for creative tasks because the investigation IS the voice-finding process. Separating them (as v1 pipeline did) forces the writer agent to reconstruct voice from a description rather than carry it forward from engagement with the material.

Four stages became two in v2 for exactly this reason. v3 keeps two stages.

---

## What to watch for when testing

**Stage 1 output:**
- Does the piece open with something specific to this product and reader, or with a formula hook?
- Does the headline argue something, or label a topic?
- Is the VP Eng quote placed as a narrative beat with weight, or listed among other data points?
- Does the piece sound like it was written by someone who found the material interesting?
- Does the structure vary from run to run, or does every run produce the same 3-5 section shape?

**Stage 2 output:**
- Does the final piece still sound like the Stage 1 writer wrote it?
- Are SEO placements invisible or disruptive?
- Has any sentence been improved into blandness?
- Does the close still feel like a consequence of the piece, or like a bolted-on CTA?

**Cross-tier comparison:**
- Does Stage 1 of v3 pipeline produce more natural investigation (no criterion gates) than v2 pipeline, while preserving the angle-finding discipline?
- Does Tier 2 v3 (lighter, no phase labels) close the gap on voice with Tier 3 v3, or does context isolation still produce a meaningful advantage?
- Do the v3 versions of both tiers outperform their v2 counterparts, reversing the regression?

---

## Prediction

The v2 pipeline won on voice because SEO requirements never entered Stage 1's context. That structural isolation is preserved in v3. The v3 changes to the creative agent remove overhead without removing any of the investigative depth — the model should find sharper angles with less friction. The compliance editor is unchanged; its mechanisms were working.

The v3 Tier 2 prompt removes the criterion gates and phase labels that caused the v2 regression. It should perform closer to v1 Tier 2 (which scored above baseline) while retaining the angle-finding improvement that v2 introduced. Whether it closes the gap with Tier 3 on voice will depend on whether the epistemic stance alone is sufficient when the compliance criteria are in the same context window — even deferred to the end.
