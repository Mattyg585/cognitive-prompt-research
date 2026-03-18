# Pipeline V2 Design Notes

## The core finding that changed everything

The v1 pipeline (Brief Explorer → Content Architect → Writer → Editor) scored well on technical dimensions but external evaluators detected something the rubric didn't fully capture: the Tier 3 output "reads slightly more 'edited' than 'written'." One evaluator preferred the Tier 2 version on voice — "nails the brief's 'explaining to a smart friend' instruction."

This is not a minor finding. For a voice-continuity task, the dimension that matters most is whether the piece sounds like a person wrote it. The 4-stage pipeline introduced a synthetic boundary between investigation and writing (the Content Architect stage) that doesn't correspond to how a skilled copywriter actually works. A human writer reads a brief and starts writing — the investigation and angle-finding ARE the early drafts. Structuring them as separate pipeline stages forces the writer agent to reconstruct voice from a description rather than carry it forward from discovery.

The Editorial stage's "editedness" residue is a separate but related problem. An editorial pass on voice-continuous prose is inherently risky. The v2 design addresses both problems.

## Why 2 stages instead of 4

**The 4-stage design created two unnecessary separations:**

1. **Brief Explorer → Content Architect**: Both stages were doing convergent-then-divergent work on the same material. The explorer investigated, the architect decided. But investigation and decision-making in creative work are not cleanly separable — the interesting things you find during investigation already shape your creative judgment. Forcing a structured handoff between them required the writer to trust a description of voice rather than inhabit the voice that emerged from reading the material directly.

2. **Writer → Editor (general voice editing)**: The v1 editor was scoped broadly — SEO, formatting, AND voice preservation. The tension between "improve the prose" and "preserve the voice" is unresolvable in a single agent because both are legitimate instructions. When they conflict, something loses.

**The 2-stage design makes one cut, and that cut is the right one:**

The productive separation is **creation versus compliance** — not thinking versus writing.

Stage 1 (Investigate and Write) handles all creative work: reading the brief, finding the angle, writing the piece. Investigation and generation are compatible for voice-continuity tasks because the investigation IS the voice-finding process. The writer discovers what the piece needs to say by engaging with the material, not by reading a summary of what someone else found.

Stage 2 (Editor) handles all compliance work: SEO keyword placement, character counts, heading hierarchy, formatting, and length. It receives only two inputs: the draft and the SEO requirements as a separate structured list. The SEO requirements are never present during writing — they only enter at the editorial stage. The editor's scope is explicitly bounded: compliance, not voice.

## The cognitive mode picture

```
Stage 1: Investigate and Write
  Investigation + Generation (compatible for voice tasks)
  Context: brief only — no evaluation criteria, no compliance checklists
  Posture: curious writer

Stage 2: Editor
  Evaluation + Compliance (compatible — both convergent, criteria-referenced)
  Context: draft + structured SEO requirements (separate from draft)
  Posture: careful editor with explicit voice-preservation constraint
```

The key structural protection: SEO requirements never appear in Stage 1's context. The writer writes without knowing the keyword targets. This prevents the evaluation posture from suppressing generation. When the editor receives the draft, the SEO requirements are passed as a separate structured block — not embedded in prose, not mixed with the draft. This maintains the cognitive boundary even within a single editing pass.

## The voice-flattening risk in Stage 2

The editor's primary risk is voice flattening through well-intentioned improvement. The editor prompt addresses this with three mechanisms:

1. **Explicit scope restriction**: "Do not rewrite for voice. Do not improve the prose." The editor is forbidden from substituting their judgment for the writer's.

2. **Voice preservation check**: After applying edits, the editor re-reads as a reader specifically looking for flatness signals (hedged sentences, formal equivalents of casual phrases, rhythm decay, drift from "you" to "organizations").

3. **Priority hierarchy built into the framing**: When SEO and voice conflict, "the sentence wins" — and the editor is instructed to find a lighter way to satisfy the requirement rather than overriding the writer's phrasing.

## The handoff

What crosses from Stage 1 to Stage 2: the complete draft, as prose.

What crosses separately: the SEO requirements from the brief, as a structured list (primary keyword, secondary keywords, target length, CTA type).

What does not cross: no investigation notes, no angle rationale, no strategic summary. The editor does not need to know why the piece was written the way it was. The editor only needs to know what it says and what compliance requirements apply.

Why this format matters: passing the SEO requirements as a separate structured block (not embedded in the draft, not in prose form) maintains the cognitive boundary. The editor encounters the requirements as a checklist, not as context that shapes how they read the draft.

## Tier 2 remains competitive

For this task class, Tier 2 (single-context with scope boundaries) is a genuine competitor. The v1 Tier 2 prompt was partially effective at voice — one evaluator preferred it over the 4-stage pipeline. The v2 Tier 2 prompt (SKILL-v2.md) strengthens the investigative phase with an explicit angle-finding requirement before writing begins.

The prediction for the experiment:
- **Tier 2 v2**: Strong consistent voice (no editorial residue), angle may be less sharp because the evaluation criteria (Phase 3) are still in the same context window during Phase 2
- **Tier 3 v2**: Strong voice with sharper angle (dedicated creative context), minimal editorial residue (editor scope is explicitly compliance-only)

The experiment should run both. The comparison will tell us whether the context isolation in Stage 1 produces a meaningful angle-discovery difference over the scope-bounded Tier 2 approach.

## What to watch for when testing

**Stage 1 output:**
- Does the piece open with something specific to this product and reader, or with a formula hook?
- Does the headline argue something, or just label a topic?
- Is the VP Eng quote treated as a narrative beat, or buried in a list?
- Does the piece sound like it was written by someone who found the material interesting?

**Stage 2 output:**
- Does the final piece still sound like the Stage 1 writer wrote it?
- Are SEO placements invisible or disruptive?
- Has any sentence been improved into blandness?
- Does the close still feel like a consequence of the piece, or like a bolted-on CTA?

**Cross-tier comparison:**
- Does Stage 1 of the v2 pipeline produce more distinctive voice than the v1 writer (who received a content plan rather than the brief directly)?
- Does the v2 editor produce less "editedness" residue than the v1 editor (who had broader scope)?
- Does Tier 2 v2 or Tier 3 v2 produce stronger consistent voice across runs?
