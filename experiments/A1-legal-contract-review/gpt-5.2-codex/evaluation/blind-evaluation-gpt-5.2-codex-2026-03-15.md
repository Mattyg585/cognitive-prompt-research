---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A1
tier: evaluation
run: 0
---

# Blind Evaluation — A1 Legal Contract Review

## Outputs Reviewed (blinded)
- **Output A**: Median run + all runs for natural variation
- **Output B**: Median run + all runs for natural variation
- **Output C**: Median run + all runs for natural variation

## Dimension Scores (absolute scale)

### 1) Depth
- **Output A — 3/5**: Covers the expected risk areas (ML/data use, DPA/security, liability caps, termination, marketing) with solid redlines and rationale. The analysis is competent but does not surface truly novel insights beyond standard SaaS buyer issues.
- **Output B — 3/5**: Similar depth to Output A with clear deviations and redlines, but insight level remains within standard expectations. The clause map adds structure rather than deeper analytical threads.
- **Output C — 2/5**: Focuses on redline proposals with less analytical framing and fewer contextual links between clauses. The reasoning is serviceable but stops short of multi‑layer analysis.

### 2) Specificity
- **Output A — 4/5**: References concrete sections and proposes detailed redlines with numeric caps and defined carve‑outs. Most observations are anchored to identifiable clause language.
- **Output B — 4/5**: Strong anchoring to specific clauses, with precise redlines and fallbacks tied to the text. The descriptive clause map further grounds the review in the document.
- **Output C — 3/5**: Includes clause numbers and some direct language, but several items are structural “missing clause” additions with less linkage to specific text. Still materially grounded, just less precise overall.

### 3) Natural Variation (across runs)
- **Output A — 3/5**: Runs show some variation in emphasis (e.g., liability vs. data protection ordering) and in which secondary clauses are expanded. Structure is consistent but not identical.
- **Output B — 2/5**: Runs are highly templated with similar structure and coverage; differences are mostly in wording and minor additions (e.g., deal context). Variation is limited.
- **Output C — 3/5**: Runs vary in which “missing” clauses are added and in prioritization (e.g., price‑increase controls appear in one run). The structure is similar but emphasis shifts more than in Output B.

### 4) Completeness
- **Output A — 4/5**: Comprehensive coverage of major SaaS risk areas, including liability, data protection, ML training, termination, indemnity, assignment, and marketing. Few notable gaps for a general review.
- **Output B — 4/5**: Also comprehensive across core risk categories with a solid inventory of missing expected terms. Slightly less attention to some secondary topics (e.g., governing law detail) but still robust.
- **Output C — 3/5**: Covers many critical issues but omits or under‑emphasizes indemnity scope, governing law, and confidentiality nuances. As a redline‑only stage, it is less complete as a standalone review.

### 5) Audience Awareness
- **Output A — 4/5**: Fits a customer‑side legal review well, with clear priorities, must‑have/should‑have tiers, and actionable next steps. Tone and structure align with procurement/legal workflows.
- **Output B — 4/5**: Appropriately tailored to a buyer audience with strong prioritization and negotiation framing. The clause map supports quick stakeholder understanding.
- **Output C — 3/5**: Suitable for a legal redlining workflow but provides less executive framing and fewer business‑oriented summaries. The audience fit is narrower and more tactical.

### 6) Risk Identification Accuracy (domain‑specific)
- **Output A — 4/5**: Identifies the genuinely risky clauses (ML training, missing DPA/security, liability caps, indemnity ambiguity) without major false positives. Risk classification is generally accurate for a mid‑market SaaS buyer.
- **Output B — 4/5**: Flags the same core risk drivers with accurate rationale and impact. The risk severity assignments are reasonable and aligned with common legal practice.
- **Output C — 3/5**: Accurately flags several key risks (ML, security, liability), but misses or down‑weights indemnity coverage and some governance items. Accuracy is good where it engages, but the risk set is less complete.

## Summary

| Dimension | Output A | Output B | Output C | Delta (max–min) |
|-----------|----------|----------|----------|-----------------|
| Depth | 3 | 3 | 2 | 1 |
| Specificity | 4 | 4 | 3 | 1 |
| Natural Variation | 3 | 2 | 3 | 1 |
| Completeness | 4 | 4 | 3 | 1 |
| Audience awareness | 4 | 4 | 3 | 1 |
| Risk identification accuracy | 4 | 4 | 3 | 1 |

**Overall preference**: Output A ≈ Output B (tie), both stronger than Output C.  
**Key differences**: Outputs A and B provide fuller, end‑to‑end legal review framing with clearer prioritization and broader clause coverage. Output C is more tactical and redline‑focused, which reduces completeness and audience framing as a standalone review.  
**Magnitude**: Moderate gap between (A/B) and C; negligible difference between A and B. The difference is large enough to matter in practice when a full legal review is required.

## Diagnostic Observations (beyond rubric)
- Output C appears to be a pipeline stage focused on redline proposals, which may explain its narrower scope; as a standalone deliverable it feels incomplete despite good tactical suggestions.
- Outputs A and B read more like full legal review memos, including summaries and next‑step guidance, which improves usability for non‑lawyer stakeholders.
- Output B is more templated/structured, while Output A is slightly more narrative; neither feels “surprising,” but both are solidly professional.

## Mapping (revealed after scoring)
- **Output A = Set 1 (baseline)**
- **Output B = Set 2 (optimised)**
- **Output C = Set 3 (pipeline final)**
