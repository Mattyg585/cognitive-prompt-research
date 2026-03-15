---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A3
tier: pipeline
run: 0
---

# Handoff Spec — A3 /performance-review

## Format: `review_request` (YAML)

```
review_request:
  mode: self-assessment | manager | calibration
  review_period: "[Review Period or Date range]"
  review_cycle: "[Calibration cycle, if applicable]"
  employee_name: "[Employee name, if applicable]"
  manager_name: "[Manager name, if applicable]"
  team: "[Team name, if applicable]"
  rating_scale: "[Rating scale or levels, if provided]"
  constraints:
    tone: "[e.g., concise, formal, supportive]"
    length: "[e.g., short, standard, detailed]"
  provided_inputs:
    accomplishments: ["..."]
    goals: ["..."]
    strengths: ["..."]
    development_areas: ["..."]
    impact_notes: ["..."]
  connector_data:
    hris: "[Retrieved data or null]"
    project_tracker: "[Retrieved data or null]"
  missing_info:
    - "[List of missing items, if any]"
```

## Rules
- The router outputs **only** the `review_request` packet (no extra prose).
- Template agents must ignore any text outside the packet and must not infer missing data.
- If `connector_data` is null/unavailable, templates keep placeholders and may list missing inputs.
- Numeric anchors are avoided unless explicitly provided in `rating_scale` or user inputs.

## Transitions
- **review-router → self-assessment-template** when `mode = self-assessment` and the packet is ready.
- **review-router → manager-review-template** when `mode = manager` and the packet is ready.
- **review-router → calibration-prep-template** when `mode = calibration` and the packet is ready.