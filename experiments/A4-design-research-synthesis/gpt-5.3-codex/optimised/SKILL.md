---
name: research-synthesis
description: Synthesize user research into themes, insights, and recommendations. Use when you have interview transcripts, survey results, usability test notes, support tickets, or NPS responses that need to be distilled into patterns and strategic next steps.
argument-hint: "<research data, transcripts, or survey results>"
---

# /research-synthesis

Synthesize user research data into actionable insight.

## Usage

```
/research-synthesis $ARGUMENTS
```

## What I Accept

- Interview transcripts or notes
- Survey results (CSV or pasted data)
- Usability test recordings or notes
- Support tickets or feedback
- NPS/CSAT responses
- App store reviews

## How to Approach This

Start from the evidence, not the output structure.

Work in this sequence:

1. **Read openly** — notice patterns, contradictions, surprises, and emotional signals.
2. **Structure second** — cluster observations after reading the full material.
3. **Interpret third** — derive implications and opportunities from pattern relationships.
4. **Summarise last** — write the summary only after completing analysis.

## Output

Use this as a guide, not a rigid template. Expand where evidence is rich, compress where evidence is light.

```markdown
## Research Synthesis: [Study Name]
**Method:** [Interviews / Survey / Usability Test] | **Participants:** [count]
**Date:** [Date range] | **Researcher:** [Name]

### Key Themes
For each theme:
- What pattern it captures
- Supporting evidence (quotes and observed behaviors)
- What it implies for the product

Theme count should match what the data supports.

### Insights and Opportunities
Write as a narrative (not a forced grid).

Show how insights relate:
- many-to-one
- one-to-many
- unresolved / investigatory

### User Segments Identified
(Include only if meaningful segmentation is supported by evidence.)

For each segment:
- who they are
- defining characteristics
- core needs
- rough size only if evidence supports estimation

### Recommendations
Order by evidence strength.

For each recommendation:
- what to do
- why (which findings support it)
- confidence level (strong / exploratory / needs more evidence)

### Questions for Further Research
- [What remains unresolved]

### Methodology Notes
[Method constraints, sampling limits, bias risks]

### Summary
[Write last. Distil the highest-value findings and strategic implications.]
```

## Tips

1. Use direct quotes where they clarify meaning.
2. Keep observations distinct from interpretations.
3. Quantify only where the evidence genuinely supports quantification.
