---
model: GPT-5.1-Codex-Max
date: 2026-03-15
experiment: A1
tier: pipeline
author: prompt-writer
---

# Design Notes — A1 Legal Contract Review Pipeline

## Overview
Sequential five-stage pipeline separating orchestration, investigation, evaluation, generation, and strategy to eliminate mode interference from the original single-pass prompt. Handoffs compress to structured data to strip exploratory tone before evaluative/generative stages.

## Agent Map
- **00-intake-config** — Orchestration only. Gathers user side, contract type, deadline, focus areas, and playbook location; emits a compact intake config and baseline summary (or generic baseline notice). Avoids mixing gating with execution.
- **01-contract-reader** — Investigation + structuring. Reads full contract, builds clause map (including unlisted/atypical clauses and cross-clause interactions), extracts snippets; no severity, no redlines.
- **02-playbook-comparator** — Evaluation/triage. Applies playbook/generic baseline to clause map; assigns GREEN/YELLOW/RED with rationale and risk notes; no language drafting.
- **03-redline-writer** — Generation. Produces specific redlines + fallbacks + rationale for YELLOW/RED only; does not change severity or invent new issues.
- **04-strategic-advisor** — Reframing/synthesis. Crafts negotiation strategy, business impact, prioritization, and next steps using prior structured outputs; does not rewrite redlines.

## Ordering Rationale
Convergent-divergent rhythm: 00 compresses intake; 01 diverges across contract text but stays descriptive; 02 converges into triage; 03 diverges to generate language; 04 converges into strategy. Each divergent step is preceded by compression to fit context and prevent back-propagation of later postures.

## Execution Method
Sequential. Each stage depends on the prior compressed output. Parallelization unnecessary unless contract chunking is later introduced.

## Handoff Philosophy
Use structured tables/JSON-like blocks to pass only necessary fields (clause id, snippet, concern, severity, playbook delta, rationale, redline package). Drop exploratory narrative, user Q&A tone, and template scaffolding to prevent cognitive bleed.

## Context Window Notes
- 01 outputs condensed clause records (clause name, location, 1-3 bullet concern notes, 1-2 sentence snippet). 
- 02 further compresses into triage entries with severity + short rationale.
- 03 limits to YELLOW/RED issues only to keep redline payload small.
- 04 consumes only summaries and selected exemplars, not full text.

## Interference Mitigation
- Investigative pass (01) is free of evaluation/generation cues to avoid solution-shaped reading and checklist tunnel vision.
- Evaluation (02) separated from generation (03) to prevent fix-ready bias.
- Strategy (04) isolated so narrative/negotiation framing cannot contaminate issue discovery or severity.
- Orchestration (00) quarantined to remove gating tone from execution stages.
