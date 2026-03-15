---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A2
tier: pipeline
run: 0
---

# Pipeline Design Notes

## Overview
A two‑stage pipeline separates divergent message discovery from convergent channel execution so creative angles are not suppressed by SEO and formatting rules.

## Agent map
1. **Angle Discovery** (divergent)
   - **Input:** campaign brief and constraints
   - **Output:** structured Messaging Brief with multiple angle options
   - **Why separate:** avoids evaluation/formatting pressures during ideation

2. **Channel Execution** (convergent)
   - **Input:** Messaging Brief + selected channel(s)
   - **Output:** channel‑ready copy with optional SEO elements
   - **Why separate:** applies templates and optimization after angle selection

## Execution order
Sequential: Angle Discovery → Channel Execution. The second stage depends on the compressed brief from the first.

## Handoff design
Use a structured bullet brief to strip exploratory tone and prevent handoff contamination. No raw ideation prose crosses the boundary.

## Execution method
Sequential execution, because channel drafting requires the completed Messaging Brief.

## Context window notes
Compression happens in the Messaging Brief. Keep angles and proof points short to avoid flooding the execution stage.