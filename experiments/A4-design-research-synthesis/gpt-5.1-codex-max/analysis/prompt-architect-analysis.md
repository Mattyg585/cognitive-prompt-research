---
model: GPT-5.1-Codex-Max
date: 2026-03-15
experiment: A4
tier: analysis
---

## 1) What the prompt is actually asking for
- Core cognitive posture: **synthesis** of varied user-research artifacts into themes, insights, and recommendations (divergent → convergent narrative).
- Embedded convergent scaffolding: fixed output template with named sections (Executive Summary, Key Themes with prevalence counts and quotes, Insights→Opportunities table, Segments table, Recommendations list, Questions, Methodology notes). This pushes toward **cataloguing/fill-the-boxes** behavior.
- Minor evaluative threads: prevalence counts and impact/effort ratings introduce light evaluation/classification alongside synthesis.
- Guidance is largely **seeded by structure** rather than lenses: the template prescribes what to produce (themes, opportunities, segments, recommendations) but offers no lenses for how to look in the data.

## 2) Where modes might interfere (and synthesis vs catalogue risk)
- **Synthesis co-present with required classification**: The template (themes with prevalence, impact/effort table, segments table) can pull the model into convergent completion, suppressing divergent emergence of unexpected themes. Likely outcome: a tidy catalogue of expected sections rather than deep integrative synthesis.
- **Implicit numeric anchors**: “3-4 sentence overview,” numbered recommendations (1–3), prevalence per theme, tables with fixed columns. These anchors can normalize output regardless of input complexity (catalogue risk: always 3 themes, 3 recs, one segment table row per slot).
- **Seeds via sectioning, not lenses**: Section headings act as seeds (themes → opportunities → segments → recommendations) without investigative lenses (e.g., tensions, contradictions, journey breakdowns). This biases toward known buckets and may pre-filter out emergent patterns.
- **Order enforces premature convergence**: Executive summary and theme naming precede any exploratory step. Without an explicit “explore first” posture, the model may commit to early narratives and then backfill evidence (premature synthesis bias).
- **Evidence quota effect**: Each theme demands quotes and prevalence. When data are thin, the model may fabricate or overfit; when data are rich, it may truncate to fit the template (catalogue compression over synthesis depth).

## 3) What to look for in output (symptoms)
- **Uniform counts**: Same number of themes/recommendations across different datasets (e.g., always 3 themes, 3 recs) → numeric/template anchoring.
- **Predictable section fillers**: Boilerplate impact/effort rows and segments that mirror the template rather than the data; absence of surprising or contradictory insights.
- **Shallow quotes/evidence**: Quotes that are generic or loosely tied; prevalence numbers that look neat (e.g., “7/10” repeatedly) rather than reflecting variability.
- **Narrative flattening**: Executive summary restating headings without integrating tensions, conflicts, or temporal/user-journey nuance.
- **Missed emergence**: No cross-cutting patterns (e.g., role-based differences, context effects) and no reframing for audience; output reads like a categorized list, not a synthesized argument.

## 4) What to do about it (interventions)
- **Prompt-level**: Add a clear exploration-first boundary before filling the template (e.g., investigate, surface tensions/contradictions, then commit to themes); introduce **lenses** for exploration (e.g., breakdowns by journey stage, role, expectation vs experience) before applying the template; relax numeric anchors (remove fixed counts, allow variable numbers of themes/recs); allow responsive section counts (omit/merge sections if not supported by data).
- **Output-structure tuning**: Permit variable rows in tables and optional sections; make prevalence/evidence responsive (only where warranted) to reduce forced catalogue behavior.
- **Pipeline option (if available)**: Split into two passes: (1) exploratory emergence pass to surface patterns with quotes; (2) synthesis/structuring pass that maps emergent findings into the template with clean context. This preserves divergent depth before convergent formatting.
