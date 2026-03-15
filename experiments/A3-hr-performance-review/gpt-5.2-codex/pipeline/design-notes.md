---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A3
tier: pipeline
run: 0
---

# Pipeline Design Notes — A3 /performance-review

## Pipeline overview
Route the user’s request to a single, mode-specific template generator to eliminate cross-mode bleed while keeping the task strictly template-focused.

## Agent map
| Agent | Thinking modes | Input | Output | Why separate |
|---|---|---|---|---|
| review-router | Orchestration + light structuring | User request | Structured `review_request` packet | Keeps routing separate from template generation and prevents multi-template bleed. |
| self-assessment-template | Generation + structuring | `review_request` (mode=self-assessment) | Self-assessment template | Isolates self-assessment context from manager/calibration sections. |
| manager-review-template | Generation + structuring | `review_request` (mode=manager) | Manager review template | Keeps evaluative cues limited to placeholders and avoids calibration bleed. |
| calibration-prep-template | Generation + structuring | `review_request` (mode=calibration) | Calibration prep template | Separates calibration tables from other templates. |

## Execution order
1. **review-router** gathers mode and inputs, then emits a structured request packet.
2. **One** template agent runs based on the selected mode.

## Execution method
Sequential with routing. The router asks clarifying questions only as needed; once a request packet is formed, the user transitions to the appropriate template agent.

## Handoff design
The router outputs a compact `review_request` packet (YAML) that strips exploratory text and carries only structured fields. Template agents ignore any prose outside the packet, preventing handoff contamination.

## Context window notes
Inputs are typically small. Compression happens at the router via a structured packet, so downstream agents receive minimal, mode-clean context.