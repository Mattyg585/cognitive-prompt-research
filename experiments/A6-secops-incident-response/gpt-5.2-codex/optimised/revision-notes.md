---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A6
tier: optimised
run: 0
---

# Revision Notes — A6 Incident Response (Tier 2)

## Summary of changes
- Introduced explicit **mode boundaries** so triage/update never include postmortem content.
- **Gated templates by mode**: only the relevant template is present for each phase.
- Reordered **triage** so impact and affected systems are surfaced before severity assignment.
- Replaced **numeric anchors** (2–3 sentence summary, 5 Whys) with flexible guidance.
- Added guidance to separate **knowns vs unknowns** and request missing critical info.

## Mapping: Architect Findings → Revisions

1. **Investigation + evaluation interleaving (severity pre-filtering)**
   - **Change:** In triage, impact and affected systems are captured first, then severity is assigned with rationale.
   - **Why:** Prevents severity buckets from narrowing investigation prematurely.

2. **Investigation + generation/communication contamination**
   - **Change:** Mode boundaries explicitly prohibit postmortem content in `new/update` and restrict status updates to `update`.
   - **Why:** Removes pressure to draft communications or narratives before investigation is complete.

3. **Synthesis during investigation (premature postmortem)**
   - **Change:** Postmortem template appears only in `postmortem` mode; new/update modes explicitly avoid root cause conclusions.
   - **Why:** Prevents early narrative commitment while incident data is still emerging.

4. **Output structure carries mode (over-structured early output)**
   - **Change:** Removed fixed counts (2–3 sentences, 5 Whys) and replaced with “length as needed” and “as evidence supports.”
   - **Why:** Reduces slot-filling behavior and allows output depth to vary with input complexity.

## What to watch for when testing
- **Uniformity:** Triage outputs should vary with input depth rather than always filling every slot.
- **Premature closure:** Root cause or lessons should not appear in `new/update` runs.
- **Pre-filtering:** Early summaries should include ambiguous signals, not only items that fit severity buckets.
- **Mode leakage:** Status updates should not include postmortem sections or analysis beyond current facts.
