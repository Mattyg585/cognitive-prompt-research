# Prompt Architect Analysis: Design Research Synthesis (A4)

## 1) What the original prompt is actually asking the model to do

The original `/research-synthesis` prompt asks for five modes in one pass:

- **Investigation**: read interviews and notice what is happening.
- **Structuring**: convert observations into themes, segments, and tables.
- **Synthesis**: turn observations into insights.
- **Evaluation**: score impact/effort and prioritise recommendations.
- **Reframing**: translate findings for product stakeholders.

The interference is not subtle: the output scaffold determines the shape of thought *before* evidence is explored.

## 2) Where cognitive modes interfere

### 2.1 Fixed output scaffold causes premature convergence (High)

Numbered themes, fixed evidence slots, a required insights matrix, and a fixed recommendation pattern pull the model toward catalogue behavior. The model starts hunting for fields to fill instead of discovering structure in the data.

### 2.2 Investigation + evaluation happen simultaneously (High)

Impact/effort judgments sit inside the same step as insight extraction. That biases the model toward findings that are easy to rate, while ambiguous but strategically important patterns get underweighted.

### 2.3 Executive summary appears first (Moderate)

Writing an executive summary before the full evidence map is assembled anchors later interpretation. The body tends to justify early framing instead of challenging it.

### 2.4 Implicit count anchors distort natural variation (Moderate)

The scaffold implies expected counts (themes, quotes, recommendations, segments). Those counts become hidden targets, reducing response to true data complexity.

### 2.5 Insight-to-opportunity grid enforces false 1:1 mapping (Moderate)

In practice, one insight can open several opportunities, and several insights can converge on one strategic move. Grid format forces linearity where networked reasoning is needed.

## 3) Diagnostic signals to look for in outputs

- Uniform theme counts regardless of input richness.
- Equal treatment of weak and strong patterns.
- Recommendations that mirror template fields more than evidence weight.
- “Good report” quality but limited strategic reframing.
- Output that catalogues pain points without changing the problem frame.

## 4) Interventions

### Tier 2 (optimised single prompt)

1. Add explicit scope boundary: *start from data, not structure*.
2. Move summary to the end.
3. Replace rigid table instructions with narrative guidance.
4. Remove forced count anchors.
5. Make segmentation conditional on evidence.
6. Prioritise recommendations by evidence strength, not fixed labels.

### Tier 3 (pipeline)

Separate incompatible modes into sequential agents:

1. **Data Reader**: investigation only (per-participant observations).
2. **Pattern Synthesiser**: cross-participant pattern finding only.
3. **Strategic Translator**: stakeholder reframing + recommendations.

Handoffs should pass structured findings and drop process residue.

## 5) Composition signature

The original prompt is a high-mixing composition with strong convergent anchors. It can produce competent synthesis, but likely caps strategic insight quality.

## 6) Expected result pattern for A4

- **Baseline**: mostly catalogues themes in template-shaped form.
- **Optimised**: better weighting and narrative coherence, still monolithic.
- **Pipeline**: highest chance of reframing from “list of issues” to “system dynamics and strategic choices.”

For Step 7, the key test is exactly the A4 criterion: **catalogue vs reframe**.
