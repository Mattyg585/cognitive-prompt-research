---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A3
tier: analysis
run: 0
---

# Prompt Architect Analysis — /performance-review (SKILL)

## 1. What the prompt is asking for (cognitive posture)
- Primary posture: **generation + structuring**. The skill is about producing templates for three review artifacts (self-assessment, manager review, calibration). It prescribes sectioned outputs and placeholders rather than asking for judgments about real performance.
- Secondary posture: **light orchestration**. It routes based on mode (`self-assessment`, `manager`, `calibration`) or asks the user to choose if unspecified.
- Optional posture: **investigation/structuring** if connectors exist ("pull prior review history", "pull completed work"), but only to pre-populate templates.

## 2. Where modes interfere (if they do)
- **No hard mode conflicts** in the base prompt. The task is consistently template generation; there is no simultaneous evaluation of an employee or synthesis of evidence.
- **Potential mild ambiguity**: The opening line "Generate performance review templates and help structure feedback" could be interpreted as generating actual feedback. If used that way, the fixed-rating slots and sectioned format may nudge the model into premature evaluation while it is still meant to be templating.
- **Template multiplicity in one context** can cause bleed if mode is not specified (e.g., calibration sections leaking into manager review). The prompt mitigates this by asking for mode when absent.

## 3. What to check for in the output
- **Mode bleed**: Manager review output includes calibration tables or self-assessment sections. This would indicate the "multi-template in one context" bleed.
- **Evaluation leakage**: The model starts judging a real person or assigns ratings instead of leaving placeholders, indicating a shift into evaluation rather than template generation.
- **Anchor rigidity**: Output always fixes counts (e.g., exactly 3–5 accomplishments, 2–3 sentence summaries) even when a user requests a different scope; the numeric anchors in the template are dominating.
- **Fabricated data** (if connectors are implied): The model fills "pulled" review history without actually retrieving anything.

## 4. What to do about it (if anything)
**Prompt-level options (lightweight, only if issues appear):**
- Add a **scope boundary** if evaluation leakage appears: "Produce templates only; do not assign ratings or write evaluative judgments."
- Soften **numeric anchors** if rigidity is a problem: replace "top 3–5" with "top accomplishments (as many as relevant)" or note ranges as examples rather than targets.
- For connector usage, add an explicit rule: "Only pre-populate with retrieved data; otherwise leave placeholders and ask for missing inputs."

**Pipeline/structural changes (only if persistent bleed):**
- Split the three modes into separate skill files or explicitly fence them with strong mode headers so that a single mode’s template is the only active context. Trade-off: higher maintenance overhead vs. cleaner mode isolation.

## 5. Composition signature (runtime skills/sub-agents)
- **Base skill**: Generation + Structuring (template creation), with light Orchestration (mode routing).
- **Optional connector behavior**: Investigation + Structuring (data retrieval to pre-fill templates).
- **Compatibility**: These postures are compatible; no inherent investigation–evaluation or investigation–generation conflict is demanded by the prompt.

Overall: the prompt is structurally clean for its intended purpose (template generation). Any issues are likely to come from users expecting actual evaluative content rather than templates, or from numeric anchors becoming rigid.
