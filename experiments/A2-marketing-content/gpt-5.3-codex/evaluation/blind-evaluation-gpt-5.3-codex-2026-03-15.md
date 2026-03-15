# Blind Evaluation — A2 Marketing Content (GPT-5.3-Codex, 2026-03-15)

Method used:
- Evaluator framework: `evaluation/evaluator-prompt.md`
- Rubric: `evaluation/rubric.md`
- Domain-specific dimension added: **Voice and Engagement**
- Blind labels assigned before scoring: **Group A / Group B / Group C**

Inputs compared (3 runs each):
- Group A: unknown tier during scoring
- Group B: unknown tier during scoring
- Group C: unknown tier during scoring

---

## Dimension scoring

### 1) Depth (1-5)

- **Group A: 3**  
  Covers expected launch ground well (problem, product, proof, pricing) but mostly describes what is already in the brief.
- **Group B: 5**  
  Reframes the problem at a systems level (continuity/memory/middleware) and ties product mechanisms to managerial reality.
- **Group C: 4**  
  Offers clear reframes and stronger argument shape than Group A, though not as consistently sharp as Group B.

### 2) Specificity (1-5)

- **Group A: 3**  
  Accurate references to metrics/features but phrasing is often portable to many SaaS launch posts.
- **Group B: 5**  
  Repeatedly grounds claims in practical scenarios and mechanism-level detail (handoffs, re-explanation burden, focus interruption cost).
- **Group C: 4**  
  Strong specificity and concrete language, but occasionally reverts to generalized launch diction.

### 3) Natural Variation (1-5)

*(scored across all three runs per group)*

- **Group A: 2**  
  Highly consistent structure and headline style; resembles template-driven execution.
- **Group B: 4**  
  Distinct opening frames and argument metaphors across runs with stable quality.
- **Group C: 4**  
  Meaningful variation in framing and pacing; less structural repetition than Group A.

### 4) Completeness (1-5)

- **Group A: 4**  
  Very complete feature and pricing coverage.
- **Group B: 4**  
  Completeness is strong, with selective emphasis rather than exhaustive feature-by-feature coverage.
- **Group C: 4**  
  Balanced completeness and readability; generally includes all required launch ingredients.

### 5) Audience Awareness (1-5)

- **Group A: 3**  
  Correct target audience language, but emotional modeling is lighter.
- **Group B: 5**  
  Consistently models engineering-manager lived experience and decision posture.
- **Group C: 4**  
  Good audience fit and empathy; occasionally less incisive than Group B on emotional texture.

### 6) Voice and Engagement (Domain-specific, 1-5)

- **Group A: 2**  
  Clear and competent, but mostly informational and less compelling as hero-content prose.
- **Group B: 5**  
  Strong point of view, memorable lines, and sustained reading momentum.
- **Group C: 4**  
  Distinctly more engaging than Group A, with confident voice and cleaner flow.

---

## Summary table

| Dimension | Group A | Group B | Group C |
|---|---:|---:|---:|
| Depth | 3 | 5 | 4 |
| Specificity | 3 | 5 | 4 |
| Natural Variation | 2 | 4 | 4 |
| Completeness | 4 | 4 | 4 |
| Audience Awareness | 3 | 5 | 4 |
| Voice and Engagement | 2 | 5 | 4 |
| **Total** | **17** | **28** | **24** |

**Overall preference:** Group B > Group C > Group A  
**Magnitude:** Group A -> Group C = Moderate to large; Group C -> Group B = Moderate.

## Key differences observed

- Group A is reliable and complete, but reads more like polished template output.
- Group C introduces stronger narrative intent and audience empathy while keeping launch clarity.
- Group B shows the strongest mechanism-level storytelling: it explains *why* the workflow changes, not just *what* features exist.

## Diagnostic notes (outside strict rubric)

1. **Headline strategy quality** improves from descriptive (A) to reframing/argument-led (C/B).
2. **Evidence handling** in Group B is strongest: metrics are interpreted, not merely listed.
3. **CTA quality** shifts from standard launch CTA language (A) to momentum-aligned challenge framing (B/C).
4. **Editorial selectivity** is healthiest in B/C, where emphasis is weighted by reader impact.

---

## Blind label reveal

- **Group A = Baseline** (`gpt-5.3-codex/baseline-runs/`)
- **Group B = Pipeline final stage outputs** (`gpt-5.3-codex/pipeline-runs/run-*/04-voice-seo-editor.md`)
- **Group C = Optimised** (`gpt-5.3-codex/optimised-runs/`)

## Conclusion

The ranking aligns with the expected A2 pattern: baseline is competent, optimised materially improves voice and framing, and pipeline delivers the strongest engagement and audience-model depth while retaining required launch information.