---
model: GPT-5.2
date: 2026-03-15
experiment: A2
artifact: prompt-architect-analysis
---

# Prompt Architect Analysis — `A2-marketing-content/original/SKILL.md`

## 0) What this artifact is
This is **metacognitive prompt analysis**: how the prompt/skill shapes the model’s thinking (cognitive posture), where that helps, where it can interfere, and what signatures to watch for in outputs. It does **not** judge the quality of any specific generated marketing copy.

## 1) What the prompt is actually asking the model to think like
**Primary posture:** *production copywriter operating inside channel templates*, with a strong bias toward:
- **Structuring / templating**: predefined sections and slots for each asset type (blog, social, email, landing page, press release, case study).
- **Heuristic evaluation**: “best practices” and checklists (readability level, CTA rules, SEO placement rules) function as **implicit quality gates**.
- **SEO optimisation** as a co-equal objective to persuasion and clarity.

This is a “**fill the boxes**” posture: the model is encouraged to complete a template and satisfy a checklist.

### Why that matters for A2 (marketing content)
For marketing content, this posture can be beneficial **when the goal is consistent, channel-correct deliverables**. But it can suppress the kinds of divergent moves that often differentiate great marketing: unusual angles, specific voice, emotionally resonant framing, and non-obvious story hooks.

## 2) Mode interference risks (where the modes pull against each other)
This skill mostly bundles **Generation + Structuring + Evaluation** in one context.

### 2.1 Generation vs evaluation (best-practice “rules” as pre-filters)
The “Writing Best Practices” and “SEO Checklist” sections introduce **criteria-referenced language** (e.g., reading level guidance, “one primary CTA,” keyword placement rules, “do not keyword-stuff”). That evaluation posture can become a *pre-filter* on generation:
- The model preferentially generates **safe, conventional** marketing copy that is easy to justify as “best practice.”
- It may avoid bolder, more voice-y moves because those are harder to reconcile with checklist compliance.

**Mechanism:** criteria in-context shift the distribution toward “competent audit-compliant copy,” reducing exploratory rhetoric and surprising angles.

### 2.2 Divergence suppression via fixed templates and slot-filling
The “Content Type Templates” use fixed slots and often fixed counts (e.g., blog: intro 100–150 words, body 3–5 sections, conclusion 75–100, headline length targets; social: 2–4 points; email: 2–3 blocks; landing page: 3–4 value props; etc.). These structures act as **implicit convergent containers**.

This can suppress divergence in two ways:
1) The model optimizes for **completeness** (fill every slot) rather than insight.
2) It tends toward **midpoint solutions** (“3–5” becomes “4”) even when the topic warrants fewer/more.

### 2.3 Mixed objectives: “write for humans first” vs SEO placement prescriptions
The SEO section contains an explicit “write for humans first” constraint, but it also prescribes keyword placement in multiple locations (headline, first paragraph, subheading, meta description, URL). In practice, these can conflict:
- The model may produce copy that *sounds* human but is subtly “keyword-shaped,” flattening voice.
- Or it may hedge/compromise, producing generic phrasing that works for SEO but not for persuasion.

### 2.4 Cross-channel contamination risk
Because multiple channel templates live together, the model can blur patterns across channels (e.g., blog-style explanatory prose showing up in landing pages; landing-page CTA density showing up in blog conclusions). The skill doesn’t explicitly establish hard boundaries like “don’t import blog conventions into ads,” so leakage is plausible.

## 3) Seeds vs lenses (explicitly for creative work)
This skill is **seed-heavy** (content prescriptions) with some useful lenses.

### 3.1 Seeds (content prescriptions / anchors)
Seeds here include:
- **Template slots** (required sections) and **fixed enumerations** (e.g., “3–5 sections,” “2–3 blocks,” “3–5 hashtags”).
- **Numeric length targets** (e.g., headline char limits, word counts, platform “sweet spots”).
- **Formula lists** (“Headline formulas,” “Hook formulas,” CTA verb lists, example headlines/CTAs).

**Effect in creative generation:** seeds strongly steer outputs toward recognizable marketing tropes. This is helpful for baseline competence, but it can *prematurely converge* ideation and reduce novelty.

### 3.2 Lenses (structural guidance that keeps space open)
Lenses present in the skill include:
- “Lead with benefits, not features” and “answer ‘so what?’”
- “Use ‘you’ language” (audience-centric framing)
- “Reduce friction” (conversion lens)

These guide *how to look at the content problem* rather than prescribing exact content.

### 3.3 Are constraints suppressing or supporting generation?
- **Supporting generation** when: you already have a concept/angle and need to produce **channel-correct, scannable, SEO-aware** assets quickly.
- **Suppressing generation** when: you need to **discover** the angle/hook/voice, because the model starts optimizing for compliance (counts, slots, keyword placement) before it has explored distinctive positioning.

**Key point:** For creative work, constraints are best as a *second-pass shaping tool*, not the first-pass generator.

## 4) Numbers as anchors (where to expect “midpoint gravity”)
This skill contains many explicit numeric anchors that are likely to become targets:
- SEO headline/meta limits (e.g., ~60 chars / <160 chars)
- Word-count ranges for intro/conclusion
- “3–5 sections,” “2–4 points,” “2–3 blocks,” “3–4 value props,” “3–5 hashtags,” etc.
- Platform guidance like LinkedIn “sweet spot” character count

**Predicted signature:** outputs cluster around midpoints (e.g., 4 sections, 3 blocks, 4 hashtags), regardless of topic complexity.

## 5) What to check for in the output (contamination/suppression signatures)
When this skill is active, look for:
1) **Template completion over insight**: every slot is filled, but the copy is generic.
2) **Midpoint counts**: repeated “4 sections / 3 blocks / 4 hashtags” across unrelated tasks.
3) **Tropes dominance**: hooks and headlines echo the provided formulas too closely (high surface similarity).
4) **SEO-shaped phrasing**: unnatural keyword repetition or awkwardly placed primary keyword in first paragraph/subheading.
5) **Channel leakage**: e.g., landing page reads like a blog post; social copy reads like email subject lines.
6) **Over-constraint symptoms**: overly safe tone, hedging, or bland “professional” register even when the brand voice should be distinctive.

A useful diagnostic is *variance*: if different briefs (very different products/audiences) produce outputs with the same skeletal shape, the anchors/templates are dominating.

## 6) What to do about it (interventions; prompt-level vs pipeline-level)
This section describes interventions **conceptually** (not a rewrite), to reduce interference while keeping the skill’s benefits.

### 6.1 Prompt-level optimisation (lightest fixes)
- **Scope boundary / sequencing cue:** explicitly separate phases: *ideate hook/angle first (no SEO/template constraints), then apply this skill as a formatting/optimisation pass.*
- **Constraint loosening instruction:** treat word/section counts as “defaults” not “targets,” allowing the model to vary based on message complexity.
- **Lens-first framing:** instruct the model to prioritise lenses (“so what,” benefits, audience intent) before slot-filling.

### 6.2 Pipeline reconstruction (when creative differentiation matters)
If A2 is testing “marketing content quality” where novelty/voice matters, consider splitting into clean phases:
1) **Divergent ideation agent/context** (angles, hooks, voice, narratives) with minimal formatting constraints.
2) **Convergent production agent/context** that applies this skill’s templates + SEO checklist to the chosen concept.

This follows the “compress → reason → compress” rhythm: generate options (diverge) → select/commit (converge) → format/optimise (converge with light creative).

## 7) Output structure carries mode (template as cognitive container)
Even when the model *could* be more exploratory, a template with many required slots forces convergent behaviour. If the experiment’s goal includes creative variance, consider using a **lighter output container** early (e.g., hook + thesis + proof points) and only later expanding into full channel templates.

## 8) Composition signature (runtime prompt composition risk)
Because this file is a **skill** likely to be loaded into a broader agent prompt, it has a strong composition effect.

**Component mode signature:**
- **This skill:** Generation + Structuring + Evaluation (best-practice/SEO constraints), with heavy numeric anchoring.

**Potential conflicts when combined with a base agent prompt:**
- Base agent wants **open-ended creative exploration** → this skill injects **checklist compliance** and can suppress divergence.
- Base agent wants **audience empathy / reframing** → this skill can help (benefits/“you” language) but may still compress into formulaic copy.

**Compatibility note:** this skill is most compatible when invoked explicitly for “produce channel-ready copy” rather than as always-on background context during brainstorming.

---

## Ready for handoff
Analysis complete and saved. Ready to hand off to the `prompt-writer` agent for any prompt revision/pipeline design work (if desired).
