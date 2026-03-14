# Revision Notes: Design Research Synthesis (Tier 2)

## Finding-to-Change Mapping

### Finding 1: Output template forces premature convergence (High)

**Problem**: Fixed theme slots, 2-quote evidence format, Impact/Effort grid, exactly 3 recommendations all act as convergent anchors. The model reads transcripts extractively rather than exploratively.

**Changes made**:
- Replaced the rigid template with a guided structure. Theme section now reads: "For each theme, provide a name, a summary of what this theme captures, supporting evidence from participants, and what it implies for the product. Themes vary — some will have extensive evidence and deep implications; others may be emerging patterns worth noting with lighter support."
- Added a framing instruction above the output structure: "Use the structure below as a guide, not a rigid template. Sections should be responsive to what the data actually contains — expand where the evidence is rich, condense where it's thin, skip sections that don't apply."
- Removed the verbatim `[Same format]` placeholder that implied all themes should be structurally identical.

### Finding 2: Investigation + Evaluation simultaneous (High)

**Problem**: Impact/Effort columns in the Insights-to-Opportunities table bias investigation toward easily-evaluable patterns.

**Changes made**:
- Removed the Impact/Effort columns entirely. These forced evaluation during investigation, creating the classic toxic pair.
- Removed the Size column from User Segments for the same reason — it forced quantitative evaluation of segments that may not be quantifiable from the data.
- Added conditional language to User Segments: "If segment sizes are estimable from the data, include rough proportions — but don't force quantification where the data doesn't support it."

### Finding 3: Insights-to-Opportunities table conflates four thinking types (Moderate)

**Problem**: Each row requires insight (synthesis) + opportunity (generation) + impact (evaluation) + effort (evaluation), forced into a 1:1 linear mapping. Reality is messier.

**Changes made**:
- Replaced the table entirely with a narrative section. New guidance: "For each significant insight, explore what it suggests for the product. Some insights point to clear opportunities. Others raise questions that need further investigation. Some insights may converge on the same opportunity; one insight may open several directions."
- Explicitly noted: "Write this as a narrative, not a grid. The relationships between insights and opportunities are rarely one-to-one."

### Finding 4: Executive Summary appears first (Moderate)

**Problem**: The model commits to a narrative framing before building the evidence base. The summary anchors everything that follows.

**Changes made**:
- Moved the summary to the final section, after all analysis. Relabelled as "Summary" rather than "Executive Summary."
- New description: "Overview of the key findings, written after the analysis above. This is a synthesis of the synthesis — what are the most important things a reader should take away?"

### Finding 5: Implicit count anchors (Moderate)

**Problem**: Template implies 3-5 themes, 2 quotes per theme, exactly 3 recommendations.

**Changes made**:
- Theme count: "The number of themes should reflect what the data contains. A small study might surface a couple of strong patterns. A large or complex dataset might surface many. Let the data decide."
- Quote count: "Some themes may warrant several quotes; others may be well-captured by one. Use what best represents the pattern."
- Recommendation count: "Some datasets produce many clear directions; others produce a few strong ones and several open questions."
- Removed the numbered `Theme 1:` / `Theme 2:` structure that implied a fixed count.
- Removed the numbered 1/2/3 priority recommendation list.

### Finding 6: Recommendations mix generation with evaluation (Moderate)

**Problem**: Generating recommendations AND prioritising them (High/Medium/Lower) simultaneously constrains generation to what fits a priority hierarchy.

**Changes made**:
- Removed the High/Medium/Lower priority labels entirely.
- New guidance: "Recommendations should follow from the strength of the evidence, not a predetermined priority scheme. Order by what the data most strongly supports."
- Evaluation of recommendations is implicit in the evidence strength, not forced into a separate classification.

## Additional Changes

### Added a "How to Approach This" section

Added a scope boundary and process guide before the output structure. This establishes the cognitive sequence — read openly, then structure, then interpret, then summarise — so the model works through the data before converging on output. The key line is the scope boundary: "Start from the data, not from the output structure."

### User Segments made conditional

Added: "Include this section if the data reveals meaningfully distinct groups of users. Skip it if the data doesn't support segmentation." This prevents forced segmentation when the data doesn't warrant it.

### Tip 3 softened

Changed from "Quantify where possible — 'Most users' is vague. '7 of 10 users' is specific" to guidance that acknowledges quantification is useful where accurate but shouldn't be forced onto qualitative patterns. The original tip pushed toward quantification as a universal good, which is a mild convergent anchor on investigation.

## What Was Preserved

- The overall purpose (research synthesis) is unchanged.
- All input types accepted are unchanged.
- The connector integrations are unchanged.
- Tips 1 and 2 are preserved (raw quotes, observations vs interpretations).
- The Questions for Further Research and Methodology Notes sections are preserved.
- The general flow from themes through insights to recommendations is preserved — only the rigidity is removed.

## What to Watch For in Evaluation

- **Theme count variation**: Does the optimised version produce different theme counts for different datasets? If so, the count anchors have been successfully removed.
- **Evidence depth variation**: Do some themes get more quotes than others? Does the model adjust evidence depth to match the data?
- **Insight-opportunity topology**: Does the narrative section capture many-to-one or one-to-many relationships between insights and opportunities that the grid couldn't represent?
- **Summary quality**: Does the summary (now written last) feel like a genuine distillation, or does it still feel like a premature framing?
- **Segment skipping**: When run on data that doesn't support segmentation, does the model skip the section rather than forcing segments?
