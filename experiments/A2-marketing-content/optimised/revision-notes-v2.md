# Revision Notes: SKILL-v2.md

**Revising from**: SKILL.md (v1 optimised) and original/SKILL.md
**Revising to**: SKILL-v2.md
**Date**: 2026-03-17
**Architect findings used**: prompt-architect-analysis-v2.md

---

## What changed and why

### 1. Phase structure: two phases instead of three

**v1 structure**: Understand → Write → Polish
**v2 structure**: Investigate → Write (combined) → Polish

The v1 prompt correctly separated evaluation (Phase 3) from generation (Phase 2). But it kept "Understand" and "Write" as distinct phases with a hard stop between them — "Do not move to Phase 2 until you understand what this piece needs to do."

The v2 prompt merges investigation into writing by making the angle-finding a prerequisite for writing rather than a completed prior phase. The investigation runs until the angle clicks, then writing begins. This is closer to how a skilled writer actually works: the investigation and early writing are the same process. A human copywriter doesn't stop exploring after a "research phase" — they keep discovering through the act of writing.

**Architect finding addressed**: "Voice-continuity assessment — investigation + generation may be compatible for creative tasks because the investigation IS the voice-finding process."

**What this changes in practice**: The v2 prompt does not tell the model to produce an investigation output and then pivot to a new posture. The investigation runs until one moment — the angle — and then continues directly into writing. No posture shift, no phase boundary to cross.

---

### 2. The angle requirement: explicit and binding

**v1**: Asked "what's the angle?" as one of four investigation questions
**v2**: Makes angle-finding the explicit gate before writing begins

"Do not move to Phase 2 until you have that angle. If you have several candidate angles, choose the one that most directly addresses the reader's emotional state and the product's most surprising truth. Commit to one."

This addresses the architect's finding that the v1 investigation questions were parallel and non-committal — the model could tick all four boxes without actually arriving at a creative decision. The angle requirement forces the investigation to converge before writing begins, without imposing an evaluation checklist that would suppress creative direction.

**Architect finding addressed**: v1's investigation was a checklist rather than a funnel toward commitment. The angle requirement turns it into a genuine convergent endpoint.

---

### 3. Numeric anchors removed from generative phase

**Original**: "Introduction (100-150 words)", "Body sections (3-5 sections)", "Conclusion (75-100 words)", "use at least one data point per section", subheadings "every 200-300 words"
**v1 optimised**: Removed some anchors but retained "two deep sections or six short ones" as an example range
**v2**: No numeric ranges in the generative phase. "Length varies with content — let depth match the complexity of what you're saying."

The v2 does include a length target in Phase 3 (SEO review), because at that stage a target length is a compliance requirement being checked, not a creative anchor constraining generation. This is the correct placement: count words after writing them, not before.

**Architect finding addressed**: "Secondary: numeric anchors producing structural uniformity." Baseline runs showed uniform section counts and similar word counts across runs. The anchors were producing structural sameness even when the content warranted different shapes.

---

### 4. Headline guidance: job description instead of formula list

**Original**: Seven headline formula examples with worked instances
**v1**: Replaced formulas with a description of what headlines must do (gap, specific value, mental state match, honesty) — but framed as generative guidance
**v2**: Moved headline guidance to be explicitly post-writing: "Write the headline last. The headline should capture what the piece actually became — its real argument or reframe — not what you intended before writing it."

This is a meaningful change from v1. The v1 headline guidance was still structured as pre-writing direction (here is what a good headline does — now write one). The v2 makes the sequence explicit: write the piece, then write the headline that reflects what the piece became. This matches how skilled copywriters work and prevents the headline from anchoring the piece prematurely.

**Architect finding addressed**: "Tertiary: seed-based headline/hook formulas produced formula headlines in every baseline run." The formula list was the proximate cause. The v1 removed the formulas but left headline guidance as a pre-writing checkpoint. The v2 relocates headline writing to post-draft.

---

### 5. Hook guidance: principle instead of formula

**Original**: Six named hook formulas (surprising statistic, contrarian statement, question, scenario, bold claim, story opening) with examples
**v1**: Kept the principle ("it earns the next sentence") but removed the formula names
**v2**: Frames the opening as a reader-specific decision: "This is whatever creates the specific tension that makes this reader, with this problem, unable to stop. Do not use a formula. Use what the material gave you."

The explicit instruction "do not use a formula" directly addresses what the architect found: hook formulas in the original prompt produced question-hook openings in nearly every baseline run. Making the formula-avoidance explicit rather than implicit (by removing the formulas) is a stronger intervention.

**Architect finding addressed**: Baseline diagnostic signal — "Question hook from formula = template completion. Scenario that recreates reader's experience = genuine voice."

---

### 6. Phase 3 framing: posture shift, not section transition

**v1**: "Now shift to evaluation mode. The draft exists — review it against these channel and SEO guidelines."
**v2**: "The draft exists. Now shift posture: you are an editor, not a writer. Review the piece against these guidelines and adjust what needs adjusting — without flattening the voice you built in Phase 2."

Minor but deliberate change. The v1 said "shift to evaluation mode" — which names the cognitive mode accurately but frames the shift as one among several sequential modes, suggesting the model should activate evaluation-posture language from the start of Phase 3. The v2 frames it as a role change ("you are an editor") and immediately pairs the evaluation instruction with its constraint ("without flattening the voice"). The constraint is in the same sentence as the instruction, not at the end of the section where it competes less effectively.

**Architect finding addressed**: The Phase 3 voice preservation check ("read the piece aloud — does it sound like a person or a template?") was in v1 but appeared after the SEO and formatting checklists, making it feel like a final cleanup step. In v2 it is embedded in the phase framing itself.

---

### 7. What was preserved from v1

- The three-phase sequential structure (understand/write first, evaluate later)
- Qualitative voice guidance ("write for one reader," "earn every section," "close with momentum")
- Channel-specific guidance kept as principles, not templates (blog, social, email, landing page, press release, case study)
- SEO guidance moved to Phase 3 intact
- The voice check at the end of Phase 3 with the specific signal: "If the Phase 2 voice got flattened — go back."

These parts of v1 were working. The architect's v2 analysis confirmed them. The revisions address the specific mechanisms identified, not the prompt's overall structure.

---

## What to watch for when testing v2

**Diagnostic signals (per architect v2 analysis):**

- Opening paragraph: does it recreate the reader's specific experience, or use a formula hook?
- Headline: does it argue something or reframe something, or does it label the topic?
- VP Eng quote: is it placed as a narrative beat with weight, or listed among other data points?
- CTA: does it feel like a natural consequence of the piece, or a sales interruption?
- Section count across runs: does it vary with the content, or does every run produce the same structure?
- Overall register: does it sound like "one person wrote it with conviction" or "competent copy that was polished by committee"?

**The critical comparison**: Does v2 produce stronger angle-finding (the explicit convergence requirement) and more distinctive voice (no formula hooks) than v1, while preserving v1's gains over baseline on structural coherence and Phase 3 compliance?
