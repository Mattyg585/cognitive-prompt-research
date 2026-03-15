---
name: research-synthesis
description: Synthesize user research into themes, insights, and recommendations. Use when you have interview transcripts, survey results, usability test notes, support tickets, or NPS responses that need to be distilled into patterns, user segments, and prioritized next steps.
argument-hint: "<research data, transcripts, or survey results>"
model: GPT-5.2
date: 2026-03-15
experiment: A4
tier: optimised
artifact: optimised-skill
---

# /research-synthesis (Optimised for A4)

Synthesize user research into actionable insight **starting from evidence**, then (only after themes are formed) move into opportunities and prioritisation.

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

## Usage

```
/research-synthesis $ARGUMENTS
```

## What I Accept

- Interview transcripts or notes
- Survey results (CSV, pasted data)
- Usability test recordings or notes
- Support tickets or feedback
- NPS/CSAT responses
- App store reviews

## Working method (protect discovery)

### Phase 1 — Evidence-first reading (no solutions yet)
Read the full input openly.

Use lenses (how to look, not what to find):
- **Workarounds:** What are people doing to get around friction?
- **Expectation gaps:** What did users assume would happen vs what happened?
- **Contradictions/tensions:** Where do needs trade off (speed vs control, flexibility vs safety, etc.)?
- **Moments of emotion:** frustration, anxiety, delight, mistrust—what triggered them?
- **Context constraints:** environment, timing, stakeholders, device limits, policy limits.
- **Mental models & language:** what terms users use; what they believe the system is doing.

### Phase 2 — Theme synthesis (still no prioritisation)
Cluster observations into themes that are faithful to the input.

### Phase 3 — Implications → opportunities → recommendations
Only after themes exist, derive implications and opportunities, then prioritise recommendations.

### Phase 4 — Summary last
Write the executive summary **after** all sections are complete.

## Evidence and quantification rules (do not fabricate)

- **Quotes must be verbatim.** Only use quotation marks for text that appears in the provided input.
- **Attribution must be supported.** Only use participant IDs (e.g., P3) if the input includes stable identifiers. Otherwise omit IDs.
- **Prevalence is conditional.**
  - If the input contains participant counts/IDs and you can confidently count: include a numeric prevalence (e.g., “6 of 12”).
  - If not: describe prevalence qualitatively (e.g., “common”, “some”, “rare”, “unclear”) and say what evidence you used.
- **Do not fill boxes just to satisfy a template.** Include sections/items only when the evidence supports them.

## Output

Use the structure below as a **guide**, not a rigid template. Expand where evidence is rich; compress where evidence is thin.

```markdown
## Research Synthesis: [Study/Source Name]
**Method:** [Interviews / Survey / Usability Test / Mixed] | **Participants:** [count if known; otherwise “unknown”]
**Date:** [Date range if known] | **Researcher:** [Name if known]

### Key Themes
(Include as many/few themes as the data supports.)

#### [Theme name]
- **What this theme is:** [1–3 sentences]
- **Prevalence:** [numeric if supported; otherwise qualitative + “participant count unknown/unclear”]
- **Supporting evidence:**
  - [Verbatim quote if available] (source reference/participant id only if present)
  - [Observed behavior / note excerpt / ticket snippet]
- **Tensions / counter-evidence:** [If any]
- **Implication:** [What this means for the product/org]

### User Segments (only if evidence supports meaningful segmentation)
If segmentation is weak or speculative, say so and instead describe the *range of contexts* observed.

| Segment | Characteristics | Needs | Size (only if supported) |
|---|---|---|---|
| ... | ... | ... | ... |

### Insights → Opportunities
Describe the relationships (not a forced grid):
- Many-to-one: several insights converge to one opportunity
- One-to-many: one insight implies multiple opportunity directions
- Unresolved: important but not yet actionable without more evidence

For each opportunity, include:
- **Opportunity:** [what could change]
- **Based on:** [which theme(s)/evidence]
- **Expected impact:** [qualitative; quantify only if supported]
- **Effort/risk considerations:** [qualitative]

### Recommendations (prioritise after synthesis)
List recommendations in an evidence-responsive order (not a fixed count).

For each recommendation:
- **Recommendation:** [what to do]
- **Rationale:** [which findings support it]
- **Confidence:** [Strong / Medium / Exploratory]
- **Notes:** [Dependencies, risks, open questions]

### Questions for Further Research
- [What remains uncertain or contradictory]
- [What to test/measure next]

### Methodology Notes
- [Data limitations, sampling bias, missing metadata, merging sources, etc.]

### Executive Summary (write last)
A concise synthesis of the highest-signal themes and strategic implications.
(Do not introduce claims not supported elsewhere in this report.)
```

## If Connectors Are Available (optional triangulation)

Only do this if the connector is actually available in your environment. If not, skip this section.

- If **~~user feedback** is connected:
  - Pull related support tickets/feature requests/NPS responses to corroborate or challenge themes.
- If **~~product analytics** is connected:
  - Look for behavioral metrics that align with or contradict qualitative patterns.
- If **~~knowledge base** is connected:
  - Search for prior studies/findings that confirm, refine, or conflict with the current synthesis.

When you triangulate, clearly label what came from:
- provided research input vs
- connector-retrieved sources.

## Tips

1. Keep **observations** distinct from **interpretations**.
2. Prefer **specific evidence** (quotes, behaviors, concrete examples) over generic summaries.
3. Quantify only when the evidence genuinely supports it; otherwise be explicit about uncertainty.
