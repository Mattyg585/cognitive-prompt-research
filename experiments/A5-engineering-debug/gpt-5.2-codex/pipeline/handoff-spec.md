---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A5
tier: pipeline
run: 0
---

# Handoff Spec — /debug Pipeline

## Pipeline overview
Two-stage flow that separates **investigation** from **diagnosis/fix** to avoid premature convergence. Investigation outputs structured evidence; resolution consumes that evidence to commit to root cause and fix.

## Handoff: debug-investigate → debug-resolve

### Information that crosses
- Issue snapshot (expected vs actual)
- Reproduction steps and conditions
- Scope/impact (who/what/where)
- Evidence (logs, errors, metrics, traces — verbatim + sources)
- Observations and anomalies
- Recent changes (facts only)
- Open questions / missing data

### Format
Structured bullets with labeled fields (no narrative). Use the Investigation Handoff template from the agent prompt.

### What gets dropped
- Speculative root causes
- Fix ideas or prevention recommendations
- Exploratory asides and “this might be because…” reasoning

### Compression rule
Prefer concise bullets over prose. Each bullet should be a fact, observation, or question that can be independently evaluated.

### Failure mode handling
If investigation evidence is insufficient for diagnosis, the resolve agent returns a targeted request for missing data and hands back to investigation rather than fabricating a root cause.
