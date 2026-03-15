---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A4
tier: analysis
run: 0
---

# Prompt Architect Analysis — research-synthesis skill

## 1. What the prompt is asking the model to *think like*
The skill establishes a **research synthesis** posture: compress raw research into **themes, insights, segments, and recommendations**. It blends:
- **Synthesis/structuring** (key themes, segments, executive summary).
- **Reframing** (executive summary, implications for the product).
- **Evaluation** (impact/effort ratings in the opportunities table).
- **Generation** (opportunities and recommendations).

The overall stance is convergent (pin down themes, quantify prevalence, fill structured sections), with pockets of divergent generation (opportunities/recommendations).

## 2. Where modes interfere (and how)
**Potential interference points** come from mixing synthesis with evaluation and generation in a single pass:
- The **“Insights → Opportunities | Impact | Effort”** table introduces evaluation criteria while the model is still synthesizing. This can **pre-filter insights** toward what can be scored or acted on, suppressing nuanced or ambiguous findings.
- The **Recommendations** section pushes the model toward solution-shaping, which can **bias which themes are surfaced** (“findings that lead to clear actions” over “findings that are important but messy”).
- The **Executive Summary** appearing first in the output template invites **premature narrative commitment**, which can then shape how later sections are framed (summary-first compression in the same context).

These aren’t fatal in a synthesis workflow, but they can narrow exploration and reduce the depth of emergent themes.

## 3. Numeric anchors and structural constraints
The output template contains several **implicit numeric anchors**:
- “**3-4 sentence** overview” (exec summary).
- **Theme 1 / Theme 2** slots (suggests two themes).
- **Recommendations 1–3** (suggests three recommendations).

These anchors can make the output mechanically consistent across runs (e.g., always two themes, always three recs), regardless of input complexity. The **fixed slots** also force “box-filling” behavior, which can compress or distort findings to fit the template.

## 4. Seeds vs lenses
The prompt is **not heavily seeded** with specific content to find. It mostly provides **structural lenses** (themes, insights, segments, opportunities) and quality tips (quotes, quantification). This is generally good for synthesis.

However, the structured template behaves like a **seeded container**: it prescribes *how many* sections and what kind of content each should contain, which can constrain discovery even without explicit content seeds.

## 5. What to check for in output
Use these checks to detect suppression or anchoring:
- **Uniform counts**: If you consistently get two themes and three recommendations across diverse inputs, numeric anchors are dominating.
- **Action-shaped findings**: If insights are only the ones that map cleanly to opportunities, synthesis is being filtered by generation/evaluation.
- **Narrative lock-in**: If the executive summary reads like a commitment that the rest of the document dutifully supports, you likely have premature convergence.
- **Missing ambiguity**: If no “uncertain” or “needs more research” insights appear, the format may be forcing overconfidence.

## 6. What to do about it
### Prompt-level optimisations (lightweight)
- **Remove numeric anchors**: Replace “Theme 1/2” and numbered recommendations with language like “List as many themes/recommendations as warranted by the data.”
- **Reorder for exploration first**: Place **Key Themes** before **Executive Summary** to reduce premature convergence.
- **Add a scope boundary**: “Surface themes and insights first; do not filter based on actionability. Recommendations come after synthesis.”
- **Make evaluation optional**: “Only include Impact/Effort when the data supports it; otherwise leave blank or mark ‘unknown’.”

### Pipeline reconstruction (when higher rigor is needed)
If the synthesis is used repeatedly in production workflows:
- **Separate synthesis from recommendations** into two calls/agents with a structured handoff (themes/insights only).
- **Evaluate impact/effort in a second pass** to avoid evaluative criteria shaping the initial synthesis.

These add orchestration overhead but typically improve depth and reduce solution-shaped bias.

## 7. Composition signature (skills/connectors)
**Base skill posture:** synthesis + structuring (convergent), with light generation.

**Optional runtime components:**
- **User feedback connector:** investigation/triangulation (divergent) → can pull in new data mid-synthesis.
- **Product analytics connector:** evaluation/validation (convergent) → introduces criteria-based checking.
- **Knowledge base connector:** orchestration/publishing (meta) → low cognitive conflict.
- **“User-research” skill reference:** likely adds structuring frameworks; generally compatible unless it introduces evaluative scoring during synthesis.

**Potential conflict pairings:** synthesis + evaluation (impact/effort) + investigation (fresh data pull) in a single pass can create a mixed-mode slurry. If connectors are active, consider splitting: gather/validate → synthesize → recommend.

---

**Handoff ready** to prompt-writer.
