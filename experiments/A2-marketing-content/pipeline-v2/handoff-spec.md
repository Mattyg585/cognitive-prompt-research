# Pipeline V2 Handoff Specification

## Overview

Two-stage sequential pipeline. Stage 1 produces a draft. Stage 2 receives the draft plus a separately structured SEO requirements block and produces the final, compliant piece.

```
[Product Brief] ──► Stage 1: Investigate and Write ──► [Draft]
                                                           │
[SEO Requirements (extracted from brief)] ─────────────────┤
                                                           ▼
                                                 Stage 2: Editor
                                                           │
                                                           ▼
                                                   [Final Piece]
```

---

## Stage 1: Investigate and Write

**Input**: Product brief (complete)
**Output**: Complete draft — headline, body, meta description. No strategy notes, no editorial flags, no SEO checklist.

**Context contains**: Brief only. No SEO requirements, no compliance checklists, no evaluation criteria.

**Format**: Finished prose, as a reader would encounter it.

---

## Handoff: Stage 1 → Stage 2

**What crosses to Stage 2:**

1. **The draft** — complete, as prose. The full text as produced by Stage 1. No modifications, no annotations, no "writer's notes."

2. **SEO requirements** — extracted from the original product brief and passed as a separate, structured block. Do not embed these in the draft. Pass them as a distinct section so the editor receives them as a checklist, not as prose context.

Format for the SEO requirements block:

```
SEO REQUIREMENTS
Primary keyword: [value from brief]
Secondary keywords: [value from brief]
Target length: [value from brief — e.g., ~1200-1500 words]
CTA: [value from brief — e.g., "Start free trial"]
Channel: Blog post
```

**What does not cross:**

- Investigation notes or exploration reasoning from Stage 1
- Angle rationale or strategic summary
- Any commentary from Stage 1 about what the piece is trying to do

The editor does not need to know why the piece was written the way it was. The editor needs the draft and the compliance targets. Everything else is noise that would shift the editor's cognitive posture from editing toward evaluating the strategy.

**Why this format:**

Passing SEO requirements as a separate structured block (not as prose, not embedded in the draft) maintains the cognitive boundary between creative work and compliance work. The editor encounters the requirements as a checklist to apply, not as context that shapes how they interpret the draft. This is the structural protection that prevents evaluation criteria from contaminating the editorial pass with rewriting impulses.

---

## Stage 2: Editor

**Input 1**: Draft from Stage 1 (prose, as produced)
**Input 2**: SEO requirements (structured block, separate from draft)

**Output**: Final piece (edited, ready to publish) + editorial notes

**Context contains**: Draft + SEO requirements block only. No product brief, no investigation output, no content plan.

**Format**: Complete edited piece, followed by editorial notes documenting changes made.

---

## Execution method

Sequential. Stage 2 depends on Stage 1's complete output and cannot begin until the draft exists.

Stage 1 and Stage 2 must run in separate sessions (separate context windows). The pipeline's value is that SEO requirements never enter Stage 1's context. Running both stages in the same session — even with a clear separator — recreates the monolithic pattern: the model has already processed the SEO requirements when it writes.

---

## Notes for Claude Code execution

Run Stage 1 first:
```
Use the marketing-investigate-and-write agent with [path to product brief]
```

Save Stage 1 output to a file (e.g., `pipeline-v2-runs/run-1/01-draft.md`).

Then run Stage 2 in a new session:
```
Use the marketing-editor agent with:
- Draft: [path to 01-draft.md]
- SEO requirements: [extracted from brief — paste as structured block]
```

Save Stage 2 output to `pipeline-v2-runs/run-1/02-final.md`.

The SEO requirements for the Relay product launch brief (test-material/product-launch-brief.md):

```
SEO REQUIREMENTS
Primary keyword: async collaboration platform
Secondary keywords: distributed teams, timezone collaboration, async-first
Target length: ~1200-1500 words
CTA: Start free trial
Channel: Blog post
```
