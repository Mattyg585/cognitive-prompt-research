---
name: research-synthesis
description: Synthesize user research into themes, insights, and recommendations. Uses a 4-step cognitive process (Extract -> Cluster -> Evaluate -> Synthesize) to ensure findings are grounded in evidence before recommendations are made.
argument-hint: "<research data, transcripts, or survey results>"
---

# /research-synthesis

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Synthesize user research data into actionable insights.

## Usage

```
/research-synthesis $ARGUMENTS
```

## How to Think
Do not rush to a summary. Follow this cognitive process to ensure the synthesis is accurate:

1.  **Divergent Extraction**: First, read the raw input. Extract every distinct observation, pain point, and quote. Do not filter for "quality" yet.
2.  **Pattern Recognition**: Cluster these observations into themes. Allow the themes to emerge from the data; do not force them into pre-set categories.
3.  **Evaluative Judgment**: Only *after* themes are established, evaluate them for impact and effort.
4.  **Convergent Synthesis**: Finally, write the summary and recommendations based *only* on the evidence you have structured.

## Output Format

Please generate the response in the following order. Note that the **Executive Summary** comes LAST, to ensure it reflects the full analysis.

```markdown
## Research Synthesis: [Study Name]
**Method:** [Interviews / Survey / Usability Test] | **Participants:** [Count]
**Date:** [Date range]

### 1. Key Themes & Evidence
*Identify as many distinct themes as the data supports. Do not limit yourself to a specific number.*

#### [Theme Name]
**Prevalence:** [X of Y participants]
**Observation:** [Detailed description of the behavior or feedback]
**Supporting Evidence:**
- "[Direct quote]"
- "[Direct quote]"
**Implication:** [What this means for the user's goal]

*(Repeat for all identified themes)*

### 2. Strategic Analysis

#### Insight → Opportunity Mapping
| Insight | Opportunity | Impact | Effort |
|---------|-------------|--------|--------|
| [Derived from Theme X] | [Concrete action] | High/Med/Low | High/Med/Low |

#### User Segments (if applicable)
*Only include if distinct behavioral segments emerged from the data.*
| Segment | Characteristics | Needs |
|---------|----------------|-------|
| [Name] | [Description] | [Key needs] |

### 3. Recommendations
*Prioritize based on the Impact/Effort analysis above.*

*   **[High Priority]**: [Recommendation] — *Addressing Theme [X]*
*   **[Medium Priority]**: [Recommendation] — *Addressing Theme [Y]*
*   **[Additional Recommendations]**: [As needed]

### 4. Executive Summary
*Write this last. Synthesize the themes and recommendations above into a 3-4 sentence overview for stakeholders.*

[Summary text]

### Methodology Notes
[Any limitations, biases, or context about the data source]
```

## Guidelines

*   **No Numeric Anchoring**: Find as many themes as exist. If there are 2, list 2. If there are 7, list 7.
*   **Evidence First**: Every claim must be backed by a quote or observation extracted in step 1.
*   **Natural Variation**: Do not force data into the "User Segments" table if no segments exist. Remove sections that aren't supported by the data.
