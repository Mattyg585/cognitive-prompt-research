# Prompt Architect Analysis — A2 Marketing Content (GPT-5.3-Codex)

Source prompt analysed: `experiments/A2-marketing-content/original/SKILL.md`
Foundational references used:
- `toolkit/prompt-architect-agent.md`
- `toolkit/cognitive-stance-reference.md`

## 1) What cognitive work the original prompt is really asking for

The original skill looks like a practical content handbook, but when executed as a generation prompt it combines several cognitive modes in one context:

1. **Generation (divergent)** — write engaging launch content.
2. **Evaluation (convergent)** — enforce SEO placement, readability, and formatting checks.
3. **Template completion (convergent)** — fill predefined structures with fixed slots.
4. **Light investigation (divergent but under-specified)** — infer audience pain and angle from the brief.

The dominant posture is not “write the strongest launch story.” It is “produce a compliant marketing artifact that satisfies listed constraints.”

## 2) Where mode interference appears (with mechanism)

### A. Template-first structure turns writing into box-filling

Evidence in prompt:
- “Blog Post Structure” mandates fixed components in fixed order.
- Body sections are explicitly constrained to “3–5 sections.”
- Similar slotting appears across channels.

Mechanism:
Per the stance reference, output format carries mode. Fixed slots induce convergent completion behavior. The model optimizes for “cover each required section” instead of “find the best narrative shape for this brief.”

### B. Numeric anchors become hidden targets

Evidence:
- intro 100–150 words
- conclusion 75–100 words
- body 3–5 sections
- hashtag counts, character limits, link counts, etc.

Mechanism:
Numbers become center-of-range attractors. Even if the brief calls for a shorter or more narrative-first piece, outputs drift toward midpoint counts. Natural variation drops.

### C. Seeds for headlines/hooks constrain divergent generation

Evidence:
The prompt provides many explicit headline and hook formulas with concrete examples.

Mechanism:
For divergent tasks, seed lists narrow search to known patterns. Instead of discovering the strongest angle for Relay’s specific launch, the model often picks a familiar formula shape.

### D. Evaluation criteria sit inside writing context

Evidence:
SEO and best-practice checklists are embedded inline with writing guidance.

Mechanism:
Generation and evaluation coexist. Convergent checklist pressure suppresses voice risk-taking and rhetorical flow. Output remains competent, but less alive.

### E. Missing explicit discovery boundary

Evidence:
The prompt starts with structures and best practices before requiring an explicit “understand the brief” pass.

Mechanism:
Without an investigate-first boundary, the model can commit early to default SaaS-launch tropes and only later retrofit product specifics.

## 3) Diagnostic signals to look for in runs

1. **Template repetition across runs**
   - Similar section counts, same ordering, similar CTA shape despite run-to-run variation.
2. **Midpoint gravity**
   - Intros cluster around ~120 words, conclusions around ~85 words.
3. **Formulaic headline signatures**
   - Repeated “How to…”, “X ways…”, “The guide to…” patterns.
4. **Checklist voice**
   - Technically correct copy with weaker personality and weaker narrative momentum.
5. **Low editorial selectivity**
   - Attempts to include every feature every time, instead of weighting what matters most.

## 4) Recommended interventions

### Prompt-level (Tier 2) interventions

1. **Phase-separate within one prompt**
   - Phase 1: Understand (investigation)
   - Phase 2: Draft (generation)
   - Phase 3: Polish (evaluation)

2. **Convert seeds to lenses where creativity matters**
   - Keep principles of effective hooks/headlines, remove rigid pattern menus.

3. **Relax non-essential numeric anchors**
   - Preserve only hard platform constraints at polish time (e.g., meta description length).

4. **Reweight toward audience-state modeling**
   - Require explicit articulation of reader starting state → ending state before drafting.

Trade-off: Better voice and variation, but slightly less deterministic formatting in early drafts.

### Pipeline-level (Tier 3) interventions

Split incompatible modes into clean contexts:

1. **Brief Explorer** (investigation)
2. **Narrative Architect** (convergent synthesis of angle/structure)
3. **Draft Writer** (pure generation)
4. **Voice+SEO Editor** (evaluation and compliance)

Key handoff rule: pass structured artifacts, not exploratory prose; pass only what the next stage needs.

Trade-off: More orchestration overhead, but stronger protection against mode contamination and often better engagement quality.

## 5) Testable predictions for this A2 experiment

- **Baseline** will likely score well on completeness and compliance, lower on voice distinctiveness.
- **Optimised** should improve tone and run-to-run structural variation.
- **Pipeline** should produce strongest audience empathy and most deliberate narrative arcs, with editor stage preserving discoverability requirements.

## Bottom line

The original skill is useful and operationally competent, but it mixes creative generation with compliance enforcement and template anchors in a single context. According to the architect + stance framework, that pattern predicts “good but less differentiated” writing. Tier 2 should recover part of the lost creative space; Tier 3 should recover more by enforcing clean mode boundaries.