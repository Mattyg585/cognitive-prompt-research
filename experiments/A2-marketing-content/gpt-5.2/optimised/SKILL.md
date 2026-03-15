---
model: GPT-5.2
date: 2026-03-15
experiment: A2
tier: optimised
artifact: SKILL
name: content-creation
description: >-
  Draft marketing content across channels while preserving creative space first,
  then applying structure/SEO as a second-pass shaping tool.
user-invocable: false
---

# Content Creation Skill (Optimised)

Use this skill to produce **channel-correct marketing assets** without collapsing into template-filling or checklist-compliant blandness.

## Operating principles (how to think)

- **Lenses first, constraints second.** Start by finding the angle, audience intent, and promise. Apply structure, polish, and SEO *after* the message is clear.
- **Defaults are not targets.** If the user provides explicit limits (word count, character limit, required sections), follow them. Otherwise, let length/sections vary with the brief.
- **Channel boundaries matter.** Only use the conventions of the channel(s) requested. Don’t import blog-style exposition into landing pages, or landing-page CTA density into blogs.
- **Voice is a lens, not a script.** Match the brand voice using vocabulary, rhythm, and level of formality—without copying stock phrases.

## Step 0 — Clarify the brief (only ask what’s missing)

Before writing, ensure you know:
- Asset type(s) and channel(s)
- Audience (role, sophistication, pains)
- Goal (awareness, consideration, conversion, retention)
- Offer / next step (what the CTA *actually* is)
- Brand voice (or examples)
- Required facts, claims, constraints (legal/compliance), and any keywords

If key info is missing, ask concise questions. If the user wants you to proceed anyway, make minimal assumptions and label them.

## Step 1 — Angle & message discovery (divergent; no SEO/template pressure)

Generate a small set of **meaningfully distinct** options for:
- Core promise (what changes for the reader)
- Primary hook (why pay attention *now*)
- Supporting proof points (reasons to believe)
- Objection you’ll neutralize (the hesitation you anticipate)

Rules:
- Don’t force any specific number of options; stop when you have real variety, not minor rewordings.
- Keep this phase free of rigid formatting rules and keyword-placement prescriptions.

If the user does not choose an option, select the best-fitting one and state *why* in one sentence (audience + goal alignment).

## Step 2 — Draft the asset (convergent; structure that serves the message)

Write the requested deliverable(s) using **channel-appropriate components**, but include only what helps.

### Blog post (if requested)
Use components such as:
- A benefit-forward title that reflects the angle
- A hooky intro that frames the reader problem and stakes
- Skimmable sections with clear headings (one idea per section)
- Concrete proof (examples, data, mini-case, or mechanism)
- A conclusion that crystallizes the takeaway and offers a next step
- Optional: meta description if the user wants it

### Social post (if requested)
Use components such as:
- A first-line hook
- A short body (bullets or micro-story)
- A single clear next step (comment/click/save/share)
- Optional: a small set of relevant hashtags *only if appropriate for the platform*

### Email (if requested)
Use components such as:
- Subject + preview text that work together (not duplicates)
- A lead that earns attention quickly
- Scannable body blocks (bolding only when helpful)
- One primary CTA aligned to the goal
- Optional: light personalization if inputs exist

### Landing page (if requested)
Use components such as:
- A clear hero promise + supporting subhead
- Benefits framed as outcomes (not feature lists)
- Proof (testimonials, stats, logos) if provided; otherwise write placeholders
- Objection handling (FAQ/trust signals) where it reduces friction
- A consistent primary CTA (repeated only as needed for page flow)

### Press release / case study (if requested)
Use standard conventions for those formats, but prioritize clarity, evidence, and credible specificity over hype.

## Step 3 — Polish pass (evaluation used as a *shaping tool*)

Do a final pass focused on:
- **Clarity:** remove jargon unless the audience expects it; tighten sentences.
- **Persuasion:** benefits are explicit; proof is specific; objections are handled.
- **Voice consistency:** tone matches brand and audience; avoid generic “marketing-ese.”
- **CTA integrity:** the next step is clear and low-friction.

### SEO (only if requested or clearly relevant)
Treat SEO as a constraint that **must not flatten voice**.
- If keywords are given: incorporate them naturally where they fit.
- If keywords are not given but SEO is requested: propose candidate keyword themes and ask for confirmation, or proceed with one sensible choice and label it.
- Provide title/meta/slug only when asked; aim for common snippet display limits without contorting meaning to hit exact counts.

## Output formatting rules

- If multiple assets are requested, separate them with clear headings.
- Don’t add extra channels “for completeness.”
- Avoid rigid, repeated skeletons across unrelated briefs; let structure follow the idea.
- When uncertain about facts, use placeholders and mark them clearly.
