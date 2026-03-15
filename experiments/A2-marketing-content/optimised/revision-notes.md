# Revision Notes: Content Creation Skill (A2 Optimised)

## Architect finding → revision mapping

### Finding A: Template slots suppress generative freedom
**What changed:** Replaced fixed-slot numbered templates for divergent content types (blog, social, email, landing page) with principles and lenses about what makes each type work. Blog post guidance now says "the structure should serve the story" and "let the content dictate the shape" instead of prescribing a 5-step numbered template. Kept structured guidance for genuinely convention-bound formats (press release, case study) where templates reflect real industry expectations.

**Why this approach:** The original templates weren't wrong about *what* a blog post needs — a headline, an opening, body sections, a close. But prescribing the exact slots and counts turned generation into template-filling. The revision keeps the domain knowledge (what elements a blog post typically has) while removing the "fill in all the boxes" posture. The model can now decide this particular post needs two deep sections or six short ones.

### Finding B: Numeric anchors throughout
**What changed:** Removed all numeric targets from the generative phase (Phase 2). No word counts for introductions, no section count ranges, no paragraph sentence counts, no character limits except where they're genuine platform constraints. Moved the hard SEO limits (160-char meta description, 60-char title tag) to Phase 3 (Polish) where they function as legitimate evaluation criteria rather than generative constraints.

**Note:** Some numbers from the original (LinkedIn 1,300 characters, Facebook 80 characters) were replaced with qualitative guidance ("front-load value before the fold" for LinkedIn). These are platform realities, but putting specific character counts in the creative context turns them into targets rather than awareness.

### Finding C: Headline/hook formulas are seeds
**What changed:** Replaced 7 headline formula patterns and 6 hook formula patterns with lenses describing what makes headlines and hooks work. Instead of "How to [achieve result] [without common obstacle]", the guidance now says "create a gap between what the reader knows and what they want to know" and "promise specific value for the reader's time." This opens creative space for the model to find the right headline for this specific piece rather than selecting from a menu.

**Addressed differently than recommended:** The architect suggested explaining "what makes a headline work." I did this, but also added guidance about what makes hooks work — the original had hook formulas too, and the same seed-to-lens conversion was needed for both.

### Finding D: Evaluation criteria interleaved with generation
**What changed:** Restructured the entire prompt into three phases with explicit scope boundaries:
- Phase 1 (Understand) explicitly states "you are investigating, not writing yet"
- Phase 2 (Write) explicitly states "you are writing now, not evaluating. Ignore SEO placement, character counts, and formatting checklists — those come in Phase 3"
- Phase 3 (Polish) explicitly states "now shift to evaluation mode"

SEO checklist, on-page SEO, readability guidelines, and channel formatting checks all moved to Phase 3. The "Writing Best Practices" section was dismantled — the principles that support generation (write for one reader, earn every paragraph, let evidence persuade) moved to Phase 2 as generative lenses. The compliance-oriented items (paragraph length, reading level, active voice) moved to Phase 3 as evaluation criteria.

### Finding E: No investigation phase
**What changed:** Added Phase 1 (Understand the Brief) as the opening section of the prompt. This establishes an investigation posture before any generative or evaluative work. The phase uses open questions as lenses: "What's genuinely interesting here?", "Who is reading this?", "What's the emotional arc?", "What's the angle?" These guide exploration without prescribing what the model should find.

The phase explicitly states that this exploration should "shape everything that follows — the structure, the voice, the length, the headline." This creates the strategic foundation that the original prompt lacked.

## What to watch for when testing

1. **Section count variation.** Run on two different briefs. If both blog posts have the same number of sections, the revision hasn't fully freed the model from template-completion posture. Healthy: different briefs produce different structures.

2. **Headlines.** Do they feel specific to this product, or do they match generic formula patterns? The revision should produce headlines that couldn't have been written without understanding the brief.

3. **Voice and personality.** The original prompt's convergent overlay is the main thing being removed. The key test: does the output read like someone who understands and is excited about this product, or like a template being filled? The revision should produce noticeably more human, engaged copy.

4. **Phase boundaries.** Check whether the model actually separates understanding, writing, and polishing — or whether it collapses back into doing all three simultaneously. If the SEO placement feels forced or the structure feels mechanical, the phase boundaries may not be holding.

5. **Introduction word count.** If every introduction is 120-130 words (the midpoint of the original's 100-150 range), the anchor is *still* present in the model's priors from training data. If introductions vary naturally with the content's needs, the anchor removal worked.

## Design rationale

The core move: from **template + checklist** to **understand → write → polish**.

This restructuring creates temporal separation between three types of thinking that interfere when simultaneous:
- **Investigation** (understanding the brief) — divergent, exploratory
- **Generation** (writing the content) — divergent, creative
- **Evaluation** (SEO, formatting, channel compliance) — convergent, criteria-referenced

The original prompt ran all three simultaneously — the model was trying to understand the product, write compelling copy, AND check keyword placement at the same time. The evaluation posture dominated because it was the most concrete and convergent.

The revision sequences them: explore first (builds strategic foundation), write second (with full creative freedom), polish third (convergent work that refines without suppressing). Each phase benefits from the one before it. The scope boundaries between phases are the lightest intervention that addresses the interference.

What's preserved: all the domain knowledge from the original prompt. Channel awareness, SEO fundamentals, CTA principles, platform-specific guidance — none of this was wrong. It was just in the wrong place, contaminating the generative work. Moving it to Phase 3 lets it do its job (ensure quality and compliance) without suppressing the creative work that should come first.
