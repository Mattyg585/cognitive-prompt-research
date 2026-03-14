---
name: research-synthesis
description: Synthesize user research into themes, insights, and recommendations. Use when you have interview transcripts, survey results, usability test notes, support tickets, or NPS responses that need to be distilled into patterns and next steps.
argument-hint: "<research data, transcripts, or survey results>"
---

# /research-synthesis

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Synthesize user research data into actionable insights. See the **user-research** skill for research methods, interview guides, and analysis frameworks.

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

## How to Approach This

Start from the data, not from the output structure. Read the research material fully before organising your response. Let patterns emerge from what participants said and did rather than fitting observations into pre-existing categories.

Work through the data in this order:
1. **Read openly first** — notice what's interesting, what recurs, what surprises you, what contradicts. Follow the threads in the data.
2. **Then structure** — group your observations into themes once you've seen the full picture. The data determines how many themes there are and how much evidence supports each one.
3. **Then interpret** — explore what the patterns mean for the product and the people using it.
4. **Then summarise** — write the summary last, as a genuine distillation of everything above.

## Output

Use the structure below as a guide, not a rigid template. Sections should be responsive to what the data actually contains — expand where the evidence is rich, condense where it's thin, skip sections that don't apply.

```markdown
## Research Synthesis: [Study Name]
**Method:** [Interviews / Survey / Usability Test] | **Participants:** [count]
**Date:** [Date range] | **Researcher:** [Name]

### Key Themes

For each theme, provide a name, a summary of what this theme captures, supporting evidence from participants, and what it implies for the product. Themes vary — some will have extensive evidence and deep implications; others may be emerging patterns worth noting with lighter support.

The number of themes should reflect what the data contains. A small study might surface a couple of strong patterns. A large or complex dataset might surface many. Let the data decide.

Supporting evidence should include direct participant quotes where they are revealing. Some themes may warrant several quotes; others may be well-captured by one. Use what best represents the pattern.

### Insights and Opportunities

For each significant insight, explore what it suggests for the product. Some insights point to clear opportunities. Others raise questions that need further investigation. Some insights may converge on the same opportunity; one insight may open several directions.

Write this as a narrative, not a grid. The relationships between insights and opportunities are rarely one-to-one.

### User Segments Identified
*(Include this section if the data reveals meaningfully distinct groups of users. Skip it if the data doesn't support segmentation.)*

Describe each segment: who they are, what characterises them, what they need. If segment sizes are estimable from the data, include rough proportions — but don't force quantification where the data doesn't support it.

### Recommendations

Recommendations should follow from the strength of the evidence, not a predetermined priority scheme. Some datasets produce many clear directions; others produce a few strong ones and several open questions. Order by what the data most strongly supports.

For each recommendation, explain which findings it addresses and why it matters.

### Questions for Further Research
- [What we still don't know]

### Methodology Notes
[How the research was conducted, any limitations or biases to note]

### Summary
[Overview of the key findings, written after the analysis above. This is a synthesis of the synthesis — what are the most important things a reader should take away?]
```

## If Connectors Available

If **~~user feedback** is connected:
- Pull support tickets, feature requests, and NPS responses to supplement research data
- Cross-reference themes with real user complaints and requests

If **~~product analytics** is connected:
- Validate qualitative findings with usage data and behavioural metrics
- Quantify the impact of identified pain points

If **~~knowledge base** is connected:
- Search for prior research studies and findings to compare against
- Publish the synthesis to your research repository

## Tips

1. **Include raw quotes** — Direct participant quotes make insights credible and memorable.
2. **Separate observations from interpretations** — "5 of 8 users clicked the wrong button" is an observation. "The button placement is confusing" is an interpretation. Both are valuable; the distinction matters.
3. **Quantify where the data supports it** — Prevalence counts (e.g. "7 of 10 users") are useful where accurate, but don't force quantification onto qualitative patterns where counts would be misleading.
