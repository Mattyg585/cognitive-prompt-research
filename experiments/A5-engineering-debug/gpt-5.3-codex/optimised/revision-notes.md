# Revision Notes: A5 Engineering Debug (GPT-5.3-Codex Tier 2)

## Summary

The original prompt is already fairly strong. Changes are intentionally surgical and target the main interference: diagnosis being shaped by the visible fix destination.

## Finding -> Change -> Rationale

### 1) Investigation was destination-shaped by the visible fix section

- **Change:** Added an explicit scope boundary near the top: understanding first, fix second.
- **Rationale:** Sets investigative posture before output generation starts, reducing “jump to fix” bias.

### 2) Template skipped explicit reasoning between reproduction and root cause

- **Change:** Added `### Diagnosis` section requiring hypotheses, evidence for/against, and elimination logic.
- **Rationale:** Forces visible investigative work instead of one-shot conclusions.

### 3) Fix framing biased toward local code/config patches

- **Change:** Reframed fix guidance to support interventions at code, config, infrastructure, architecture, or process level.
- **Rationale:** Aligns fix level with root cause level; avoids symptom-only recommendations for systemic failures.

## What Was Preserved

- Original four-step debugging flow (Reproduce -> Isolate -> Diagnose -> Fix)
- No numeric anchors
- Lightweight structure and practical intake guidance
- Connector and tips sections

## Expected Effect

Compared with baseline, this version should produce:

- broader hypothesis coverage,
- clearer evidence-based narrowing,
- stronger alignment between diagnosis and intervention level,
- more specific prevention actions.

