# Intervention: Cognitive Repair

**Original Prompt:** `experiments/A2-marketing-content/original/SKILL.md`
**Intervention Type:** Tier 1 (Prompt-Level Fix) + Internal Strategy Phase

## Problem
The original prompt was a "Checklist Compliance" engine. It forced content into rigid structures (character limits, section counts) without establishing a strategic intent. This leads to structurally perfect but hollow content ("The 3 Benefits of X").

## Changes
1.  **Added Strategy Phase:** Inserted a mandatory `<strategy>` block before generation. This forces System 2 reasoning about audience and goal before System 1 generation begins.
2.  **Softened Constraints:** Replaced hard limits ("60 chars", "3-5 sections") with qualitative targets ("impact over length", "match depth to complexity").
3.  **Injected Persona:** Defined the agent as a "Strategic Content Marketer" to override the default "helpful assistant" tone.
4.  **Added Cognitive Checkpoints:** Explicitly warned against common LLM fallacies (The "Three-Point" Trap, Jargon).

## Hypothesis
The revised prompt will produce content that is less formulaic and more persuasive, with a clearer voice and better alignment to user intent, even if it varies more in structure.
