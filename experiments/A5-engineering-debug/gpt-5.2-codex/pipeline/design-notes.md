---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A5
tier: pipeline
run: 0
---

# Design Notes — /debug Pipeline (Tier 3)

## Why a pipeline
The original /debug prompt mixes investigation, synthesis, and fix generation in one context, which risks solution-shaped investigation and premature root cause commitment. Splitting the workflow creates clean context boundaries: one agent explores and captures evidence; the next converges on diagnosis and fix only when evidence supports it.

## Agent map
1. **debug-investigate** — Investigation + light structuring
   - Produces structured evidence and open questions
   - Avoids diagnosis and fixes to prevent convergence pressure

2. **debug-resolve** — Diagnosis + generation
   - Consumes structured evidence and commits to root cause/fix
   - Returns to investigation if evidence is insufficient

## Execution order and method
**Sequential**: investigation must finish before diagnosis/fix can be reliable. This minimizes handoff contamination and ensures a clean convergence boundary.

## Handoff design
The handoff is structured, bulletized evidence. This strips exploratory tone and avoids carrying investigative framing into the diagnosis context. Fix ideas and speculative causes are explicitly dropped.

## Context window notes
Investigation output is intentionally compact; long logs should be summarized with key excerpts and references. If inputs are large, run investigation on subsets and aggregate into a single structured handoff before resolution.

## When to use this pipeline
Use for ambiguous incidents, high-stakes regressions, or when early convergence is costly. For simple or obvious issues, the Tier 2 optimised single prompt is sufficient.
