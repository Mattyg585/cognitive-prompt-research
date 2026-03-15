---
model: GPT-5.2
date: 2026-03-15
experiment: A2
tier: optimised
artifact: revision-notes
---

# Revision Notes — A2 Marketing Content (Tier 2: optimised)

Source inputs:
- Original: `experiments/A2-marketing-content/original/SKILL.md`
- Architect analysis: `experiments/A2-marketing-content/gpt-5.2/analysis/prompt-architect-analysis.md`

## What changed (mapped to architect findings)

### 1) Generation vs evaluation pre-filter (best-practice/SEO checklists suppressing creativity)
**Finding:** Checklist language can shift the model into “audit-compliant” copy and suppress bolder angles.

**Change:** Introduced explicit sequencing:
- **Step 1 (Angle & message discovery)** runs *without* SEO/template pressure.
- **Step 3 (Polish pass)** applies evaluation criteria as a **second-pass shaping tool**, not a first-pass generator.

### 2) Divergence suppression from fixed templates/slot-filling
**Finding:** Fixed slots and required counts push “fill the boxes” behavior and midpoint gravity.

**Change:** Replaced rigid templates (word counts, fixed numbers of sections/blocks/hashtags) with **component-based guidance**:
- “Use components such as…” and “include only what helps.”
- Added: **Defaults are not targets** and “length/sections vary with the brief.”

### 3) Mixed objectives: “write for humans first” vs keyword-placement prescriptions
**Finding:** Keyword placement rules can flatten voice or produce awkward phrasing.

**Change:** Moved SEO into an explicit **optional** section under the final polish pass:
- SEO is applied only when requested/relevant.
- Explicit rule: **must not flatten voice**.
- Avoided hard numeric limits; framed as “common snippet display limits” to reduce anchoring.

### 4) Cross-channel contamination risk
**Finding:** Multiple channel templates in one skill can cause leakage between formats.

**Change:** Added explicit **channel boundary** instructions:
- Only use conventions of requested channels.
- Don’t add extra channels “for completeness.”
- Separate multiple requested assets with clear headings.

### 5) Seeds vs lenses
**Finding:** The original skill is seed-heavy (formulas, fixed structures, enumerations).

**Change:** Converted many prescriptions into **lenses** and decision rules:
- Voice treated as a lens (vocabulary/rhythm/formality) rather than scripted phrases.
- Angle selection guided by audience intent, promise, proof, objection.

### 6) Numbers as anchors / midpoint gravity
**Finding:** Explicit numeric targets cluster outputs around midpoints.

**Change:** Removed most numeric anchors from the skill and added explicit anti-anchoring rules:
- “Don’t force any specific number of options.”
- “Stop when you have real variety, not minor rewordings.”
- “Aim for common display limits without contorting meaning to hit exact counts.”

## What to watch for when testing

- **Variance health signal:** different briefs should yield noticeably different structures/lengths, not the same skeletal shape.
- **Reduced trope dominance:** fewer formula-echo headlines/hooks unless the brief explicitly calls for them.
- **Less SEO-shaped phrasing:** keywords should feel natural when used; voice should remain intact.
- **Less channel leakage:** landing pages should stay punchy; blogs should be explanatory; social should be hook-first.
