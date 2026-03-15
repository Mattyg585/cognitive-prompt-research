---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A4
tier: optimised
run: 0
---
---
name: research-synthesis
description: Synthesize user research into themes, insights, and recommendations. Use when you have interview transcripts, survey results, usability test notes, support tickets, or NPS responses that need to be distilled into patterns, user segments, and evidence-backed next steps.
argument-hint: "<research data, transcripts, or survey results>"
---

# /research-synthesis

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Synthesize user research data into themes, insights, segments, and (after synthesis) opportunities and recommendations. Preserve what the data supports; do not filter findings based on actionability.

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

## Process Boundaries

1. **Synthesize first** — surface themes, insights, and segments without evaluating impact, effort, or solutions.
2. **Translate second** — only after synthesis, map insights to opportunities/recommendations if supported by evidence.
3. **State uncertainty** — if evidence is thin or ambiguous, say so rather than filling slots.

## Output

```markdown
## Research Synthesis: [Study Name]
**Method:** [Interviews / Survey / Usability Test] | **Participants:** [X]
**Date:** [Date range] | **Researcher:** [Name]

### Key Themes
- **Theme: [Name]**
  - **Prevalence:** [X of Y participants | % | "Unknown"]
  - **Summary:** [What this theme is about]
  - **Supporting Evidence:**
    - "[Quote]" — P[X] / [Source]
    - "[Quote]" — P[X] / [Source]
  - **Implication:** [What this means for the product] (optional)

(Repeat for each theme warranted by the data. If no clear themes, state that explicitly.)

### Executive Summary
[Short overview sized to the findings. Write after synthesizing themes; do not force a fixed length.]

### Insights → Opportunities (optional)
| Insight | Opportunity | Impact | Effort | Evidence |
|---------|-------------|--------|--------|----------|
| [What we learned] | [What we could do] | High/Med/Low/Unknown | High/Med/Low/Unknown | [Theme/Quote ref] |

(Only include Impact/Effort when the evidence supports it; otherwise use "Unknown" or leave blank.)

### User Segments Identified (optional)
| Segment | Characteristics | Needs | Size |
|---------|----------------|-------|------|
| [Name] | [Description] | [Key needs] | [Rough %] |

(If no clear segmentation, state that explicitly.)

### Recommendations (optional)
- **[Priority label if warranted]** — [Recommendation] — [Why, citing findings]

(List as many recommendations as the evidence supports; omit if none are justified.)

### Questions for Further Research
- [What we still don't know]

### Methodology Notes
[How the research was conducted, limitations or biases]
```

## If Connectors Available

If **~~user feedback** is connected:
- Pull support tickets, feature requests, and NPS responses to supplement the evidence base
- Cross-reference themes with real user complaints and requests (do not rank or prioritize yet)

If **~~product analytics** is connected:
- Corroborate qualitative findings with usage data and behavioral metrics
- Quantify prevalence where possible; avoid assigning impact/effort unless evidence supports it

If **~~knowledge base** is connected:
- Search for prior research studies and findings to compare against
- Publish the synthesis to your research repository

## Tips

1. **Include raw quotes** — Direct participant quotes make insights credible and memorable.
2. **Separate observations from interpretations** — "5 of 8 users clicked the wrong button" is an observation. "The button placement is confusing" is an interpretation.
3. **Quantify where possible** — "Most users" is vague. "7 of 10 users" is specific.
4. **Allow natural variation** — The number of themes and recommendations should expand or shrink with the data.
5. **Surface uncertainty** — If evidence is mixed, say so and capture it in Questions for Further Research.
