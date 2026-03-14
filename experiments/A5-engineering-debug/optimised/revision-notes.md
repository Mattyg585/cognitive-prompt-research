# Revision Notes: A5 Engineering Debug (Tier 2)

## Overall Assessment

This is a calibration case. The original prompt is already reasonably well-structured — clean sequential steps, no numeric anchors, no seeds, lightweight template. The revisions are deliberately modest: three targeted changes that address the one real interference pattern (investigation shaped by fix destination) without disrupting what already works.

## Changes Made

### 1. Added scope boundary (new paragraph after intro)

**Added**: "Your primary job is to understand WHY this is happening. The fix follows from understanding — don't let the desire for a fix shape your investigation. Investigate thoroughly, including threads that might not lead to simple fixes."

**Why**: The analysis identified that the presence of the Fix section in the output template shapes the investigation — the model only follows threads that terminate in fixable causes. This boundary sets the epistemic stance before the model encounters the step structure: understanding first, fixing second. It's a single sentence that reframes the cognitive priority without restructuring anything.

**What it should do**: Allow the model to follow investigation threads that lead to systemic, architectural, or process-level root causes, even when those don't have clean code-level fixes.

### 2. Added Diagnosis section to output template

**Added**: A `### Diagnosis` section between Reproduction and Root Cause, with the guidance: "Hypotheses considered, evidence for and against, investigation threads followed. Show the reasoning — what was considered and why this narrowed to the root cause below."

**Why**: The original template jumped from Reproduction straight to Root Cause. This implicitly asked the model to compress investigation into a conclusion — present only the winning hypothesis with no record of the diagnostic process. Adding the Diagnosis section gives the model space to document the investigation itself: hypotheses tested, evidence weighed, threads followed and abandoned.

**What it should do**: Produce richer diagnostic reasoning in the output. The model should document what it considered and why, not just present a conclusion. This also serves as a forcing function: if the model has to write down its hypotheses, it's more likely to actually form and test multiple hypotheses rather than locking onto the first plausible cause.

### 3. Reframed the Fix section guidance

**Changed**: "Code changes or configuration fixes needed" became "What should change, and at what level? Some fixes are code changes. Some are architectural. Some are process changes. Match the fix to the root cause — if the root cause is systemic, a code patch is treating symptoms."

**Why**: The original framing ("code changes or configuration fixes") implicitly scoped fixes to the code/config level. This nudges the model toward proximate-cause fixes even when the root cause is deeper. The reframing opens the fix to match whatever level the root cause lives at, without prescribing what that level should be.

**What it should do**: When the root cause is architectural or systemic, the fix section should address it at that level rather than defaulting to a code patch.

## What Was Preserved

- **The 4-step sequential structure** (Reproduce, Isolate, Diagnose, Fix) — this is already well-designed and mirrors real debugging workflow.
- **The lightweight output template** — still minimal, no fixed slot counts.
- **The "What I Need From You" section** — clean, uses lenses not seeds.
- **The Tips section** — practical, no numeric anchors.
- **The Connectors section** — unchanged.
- **No numeric anchors or seeds** — the original was already clean on this.

## Expected Effect

Modest improvement. The scope boundary should reduce fix-shaped investigation, the Diagnosis section should surface richer diagnostic reasoning, and the reframed Fix section should allow systemic-level fixes. But the gains should be smaller than in experiments where the original prompt had higher interference severity. That's the point of including a calibration case.
