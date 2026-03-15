---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A4
tier: pipeline
run: 0
---
# Pipeline Design Notes — research-synthesis (Tier 3)

## Pipeline Overview
Two-stage pipeline: (1) synthesize themes/insights/segments into a structured handoff, then (2) translate those findings into an executive summary, opportunities, and recommendations. This isolates synthesis from evaluation/generation to prevent action-shaped filtering and premature narrative lock-in.

## Agent Map
### 1) synthesis-extractor
- **Thinking types:** investigation + structuring + synthesis (convergent)
- **Receives:** raw research data (transcripts, surveys, tickets, NPS)
- **Produces:** structured YAML `handoff_packet` (themes, insights, segments, evidence)
- **Why separate:** prevents evaluation or recommendation criteria from pre-filtering what gets surfaced

### 2) recommendation-builder
- **Thinking types:** evaluation + reframing + generation (convergent → divergent within constraints)
- **Receives:** `handoff_packet` only
- **Produces:** final research synthesis report with executive summary, opportunities, recommendations
- **Why separate:** avoids synthesis being shaped by actionability or impact/effort judgments

## Execution Order
Sequential: synthesis-extractor → recommendation-builder. The second stage depends entirely on the structured synthesis output.

## Handoff Specifications
See `handoff-spec.md`. The handoff is intentionally structured to strip exploratory tone and prevent cognitive contamination.

## Execution Method
Sequential execution. Each stage requires the previous stage’s full output; no parallelization needed for typical study sizes.

## Context Window Notes
- Stage 1 is the compression checkpoint; it must keep outputs concise and evidence-based.
- If raw input is too large for one context, run synthesis-extractor in parallel on chunks and merge the YAML packets before stage 2.
