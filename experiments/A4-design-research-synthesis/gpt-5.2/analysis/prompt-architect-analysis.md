---
model: GPT-5.2
date: 2026-03-15
experiment: A4
artifact: prompt-architect-analysis
---

# Prompt Architect Analysis — A4 /research-synthesis

Analysed prompt:
- `experiments/A4-design-research-synthesis/original/SKILL.md`

## 1) What the prompt is actually asking for (cognitive posture)

At the surface, this is “synthesise research into a report.” Cognitively, it asks the model to perform **a mostly-convergent synthesis**: compress messy qualitative inputs into a *publishable* structure (themes, segments, recommendations), with light evidence-handling.

Primary modes invoked:
- **Synthesis + structuring**: produce a structured markdown deliverable with specific sections and tables (Output template, SKILL.md:30–72).
- **Evaluation / prioritisation**: assign impact/effort and priority levels (Insights→Opportunities table and Recommendations, SKILL.md:51–66).
- **Investigation-lite (evidence selection)**: select quotes as supporting evidence and quantify prevalence “where possible” (SKILL.md:40–46, 90–92).

Secondary/optional modes:
- **Validation** (if connectors are available): cross-reference themes with “user feedback,” “product analytics,” and “knowledge base” (SKILL.md:74–87). This is a different posture from synthesis: it’s closer to verification / triangulation.

**Implicit posture:** “Fill a professional template.” The prompt is less about *how to look* at the research and more about *how to package* what’s found.

## 2) Where cognitive modes may interfere (mechanisms, not vibes)

This prompt is not “toxic” in the classic investigation+evaluation sense, but it has several **predictable interference points** where the packaging/prioritisation posture can suppress deeper sense-making.

### A. Executive framing placed before exploration → premature simplification
The output container puts **Executive Summary first** (SKILL.md:35–37) before themes and evidence.

Mechanism:
- Writing an executive summary is a *compression-for-audience* move.
- When required early, it can pull the whole session into a “already know what matters” register, which tends to **pre-commit to a narrative** before the model has done open theme discovery.

What to watch for:
- Themes later “match” the executive summary rather than reshaping it.
- Low surprise / low emergence: correct-but-predictable themes.

### B. Synthesis + prioritisation in the same pass → solution-shaped synthesis
The prompt asks for:
- “Insights → Opportunities” with **Impact/Effort** ratings (SKILL.md:51–56)
- followed by **Recommendations** with explicit priority ordering (SKILL.md:62–66)

Mechanism:
- Prioritisation language (impact/effort, high/medium/low) activates an evaluative, decision-making posture.
- That posture can become a **pre-filter on what gets surfaced as an insight**: findings that don’t map cleanly to an “opportunity” or recommendation can get dropped or flattened.

What to watch for:
- Over-selection of “fixable” findings; under-reporting of structural tensions, contradictions, or ambiguous needs that are important but not immediately actionable.

### C. Evidence/quantification demands without guardrails → forced completion / fabrication risk
The template includes “Prevalence: X of Y participants” and quotes with participant IDs (SKILL.md:40–46). Tips reinforce quantification (SKILL.md:92).

Mechanism:
- Required numeric slots act as **convergent anchors** (numbers become targets; “fill the box”).
- In many real research inputs, the necessary metadata (Y participants, stable IDs, attributable quotes) may be missing or messy.
- Without an explicit “do not invent” boundary, the model is nudged toward **forced specificity** (confident numbers/quotes) to satisfy the template.

This is a mode issue (completion pressure), not an output-quality judgment.

### D. Optional connector-based validation introduces a second posture mid-stream
The “If connectors available” section (SKILL.md:74–87) mixes in:
- pulling tickets/NPS, validating findings with analytics, searching prior studies, publishing.

Mechanism:
- These steps shift from synthesis to **triangulation / verification**.
- If performed in the same context, the model can drift into a “prove it with data” posture that **narrows** qualitative sense-making.

## 3) Seeds vs lenses

This prompt is relatively light on explicit **seeds** (it does not prescribe specific themes to find), which is good for avoiding content anchoring.

However, it is also light on true **lenses** (guiding questions that shape how to look). Most of the guidance is an *output schema*.

Consequence:
- The model will tend to produce “standard UX research synthesis” patterns (pain points, usability issues, feature asks) even when the data suggests subtler social/emotional dynamics, because the prompt doesn’t provide investigative lenses that invite emergence.

## 4) Numeric anchors and fixed-slot anchors

Explicit and implicit anchors that can standardise output:
- “Executive Summary: 3–4 sentence overview” (SKILL.md:35–37)
- “Prevalence: X of Y participants” (SKILL.md:40–42)
- Template strongly implies **multiple themes** via “Theme 1 / Theme 2” (SKILL.md:40–49)
- “Recommendations: 1…2…3…” implies **exactly three** priority tiers (SKILL.md:62–66)
- Impact/Effort restricted to High/Med/Low (SKILL.md:53–56)
- Evidence block shows two quote bullets (SKILL.md:43–46), which can become an implicit “always include two quotes” target.

Health signal to look for:
- Does the number of themes/segments/recommendations vary meaningfully with input complexity, or does it converge to the same count each run?

## 5) Output structure carries cognitive mode (the “fill the template” posture)

The output spec is a strong convergent container:
- multiple required sections,
- multiple tables,
- “Prevalence / Evidence / Implication” per theme.

This is great for consistent artefacts, but it can suppress divergent capability:
- The model optimises for *coverage of slots* over *depth of insight*.
- It may create segments/opportunities simply because the structure expects them.

## 6) What to check for in downstream output (diagnostics)

Use these as “contamination detectors” (since the output will usually look competent):

1. **Uniformity across runs**
   - Always ~2 themes, ~3 recommendations, always 2 quotes/theme, regardless of data richness.

2. **Premature narrative lock-in**
   - Executive summary contains claims not strongly evidenced later; later sections feel like backfilling.

3. **Forced quantification**
   - Precise prevalence counts appear even when source data likely doesn’t support it (e.g., pasted notes without participant IDs).

4. **Solution-shaped synthesis**
   - Insights that don’t map to an immediate opportunity disappear.

5. **Evidence handling drift**
   - Quotes feel generic, paraphrased, or suspiciously “perfect” (a symptom of template pressure rather than an accusation about behaviour).

## 7) What to do about it (interventions to consider)

### Prompt-level optimisations (within one prompt)
These are “light” interventions if you want to keep a single skill:
- **Reorder to protect exploration:** move theme discovery + evidence selection *before* the executive summary.
- **Make numeric fields conditional:** “include prevalence *only if the input includes participant counts/IDs; otherwise describe prevalence qualitatively and mark as ‘unknown’.”
- **Loosen fixed-slot requirements:** allow variable number of themes/segments/recommendations; avoid numbering that implies fixed counts.
- **Add an explicit evidence boundary:** instruct that quotes and participant IDs must be drawn verbatim from provided data; otherwise label as paraphrase and don’t attribute to P[X].
- **Introduce lenses (not seeds):** add a small set of investigative questions (e.g., tensions, unmet needs, workarounds, moments of delight/anger, context constraints) to guide theme discovery without prescribing content.

### Pipeline reconstruction (when you want maximum depth)
If you routinely see “competent but predictable” synthesis, separate into phases:
1) **Extract & structure evidence** (observations, quotes, frequency only when supported)
2) **Synthesize themes and segments** (no prioritisation yet)
3) **Evaluate/prioritise opportunities** (impact/effort, recommendations)
4) **Write executive summary last**

This separation reduces pre-filtering and prevents executive framing from contaminating discovery.

Trade-off:
- More orchestration overhead; better emergence and less anchor-driven uniformity.

## 8) Composition signature (runtime composition / skills)

This file is itself a skill (`/research-synthesis`) and explicitly references another skill: “See the **user-research** skill…” (SKILL.md:11). That referenced skill was not found in this repo snapshot, so its cognitive posture is unknown here.

Composition signature (from what’s visible):
- **research-synthesis (this skill):** synthesis + structuring, with embedded evaluation/prioritisation.
- **connector-driven steps (if available):** validation/verification posture (analytics triangulation) + retrieval.
- **user-research (referenced):** unknown; likely investigation/method guidance.

Potential composition conflict to check at runtime:
- If `user-research` carries an *investigative* posture and is loaded alongside the prioritisation table/recommendations, you may get **investigation suppressed by evaluation** (the “only surface what we can prioritise” effect).

## 9) Overall structural assessment

This prompt is well-structured for producing a consistent, stakeholder-ready artefact. The main risk is that the **template and prioritisation scaffolding dominate the cognitive posture**, making outputs uniform and action-shaped, and pushing premature executive framing.

If the experiment goal is to measure “design research synthesis” quality, the strongest levers to test are:
- moving executive summary to the end,
- loosening numeric anchors and fixed counts,
- separating synthesis from prioritisation (even if only via an explicit scope boundary).

---

## Handoff readiness

Prompt-level interference points, anchors, and likely contamination mechanisms have been identified. Ready to hand off to the `prompt-writer` agent to propose revisions/pipeline designs.
