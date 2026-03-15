---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A4
tier: pipeline
run: 0
---
# Handoff Spec — synthesis-extractor → recommendation-builder

## Purpose
Provide structured, mode-neutral findings so evaluation and recommendations can proceed without synthesis contamination.

## Format
A single YAML block named `handoff_packet`.

```yaml
handoff_packet:
  study_name: ...
  method: ...
  participants: ...
  date_range: ...
  researcher: ...
  themes:
    - name: ...
      prevalence: ...
      summary: ...
      evidence:
        - quote: ...
          source: ...
      implication: ...
  insights:
    - observation: ...
      interpretation: ...
      evidence: ...
  segments:
    - name: ...
      characteristics: ...
      needs: ...
      size: ...
  open_questions:
    - ...
  methodology_notes: ...
```

## What Crosses
- Theme names, prevalence, and concise summaries
- Evidence quotes with source identifiers
- Insights split into observation vs interpretation
- Segment definitions and rough size
- Research metadata and limitations
- Open questions / uncertainties

## What Gets Dropped
- Executive summaries or narrative framing
- Opportunities, recommendations, or prioritization
- Impact/Effort ratings
- Exploratory commentary not tied to evidence

## Compression Boundary
- Keep summaries concise (1–3 sentences each).
- Limit evidence to the most representative quotes.
- Use structured fields instead of prose paragraphs.

## Validation Rules
- Use "Unknown" for missing metadata.
- If no clear themes or segments, output empty lists and note in `open_questions` or `methodology_notes`.
- Do not invent new themes or recommendations in the handoff.
