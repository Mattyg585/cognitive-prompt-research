---
model: GPT-5.2
date: 2026-03-15
experiment: A4
artifact: blind-evaluation
---

# A4 — Design research synthesis (blind evaluation)

## Materials reviewed
- Set 1: `experiments/A4-design-research-synthesis/gpt-5.2/baseline-runs/run-1.md`
- Set 2: `experiments/A4-design-research-synthesis/gpt-5.2/optimised-runs/run-1.md`
- Set 3: `experiments/A4-design-research-synthesis/gpt-5.2/pipeline-runs/run-1/05-stakeholder-reframer-output.md`

> Note: “Natural Variation” cannot be scored from a single run per set.

## Quick characterisation (pre-scoring)
- **Set 1** reads like a conventional UX research synthesis template: exec summary → themes with quotes → opportunities/segments/recommendations.
- **Set 2** is similar in structure but is more careful about counter-evidence, uncertainty, and methodological limits; it also carries more direct quote grounding.
- **Set 3** is a stakeholder-ready strategic reframe: it leads with a causal model (“truth model”), uses evidence pointers rather than raw quotes, and translates into exec/design/engineering briefs + de-risking/instrumentation.

---

## Scoring (absolute; 1–5)

### 1) Depth
- **Set 1 — 3/5**
  - Covers the expected layers (friction → stale data → trust collapse; champions; lens-over-tools) but largely stays within well-known SaaS adoption dynamics.
  - Insight is competent but mostly additive rather than reframing; it doesn’t fully formalise the causal mechanism beyond the standard narrative.
- **Set 2 — 4/5**
  - Goes beyond listing themes by explicitly articulating negative feedback loops (e.g., trust decay under partial compliance) and introducing sharper tensions/counter-evidence per theme.
  - Still broadly within a “themes catalogue,” but it does more analytic work connecting themes to opportunity logic.
- **Set 3 — 5/5**
  - Provides a strong, compact causal model (distance-from-work + cost-to-contribute, mediated by trust/attention) and uses it to structure themes, opportunity mapping, and de-risking.
  - This is the only set that clearly *reframes* the problem as reinforcing loops and threshold behaviors, which changes how a team might prioritise.

### 2) Specificity
- **Set 1 — 4/5**
  - Heavily quote-grounded with participant IDs and concrete product details (“four clicks,” “47 tasks,” “60% compliance,” “notifications turned off”).
  - One caution: it assigns numeric segment sizes (e.g., “~60% doers”) that are not really justified by n=6; that slightly weakens evidential specificity even while sounding specific.
- **Set 2 — 5/5**
  - Excellent traceability to the input: every theme includes prevalence counts, multiple quotes, and explicit tensions/counter-evidence.
  - It is also careful about what it *cannot* claim (segment sizes “unclear”), which increases trustworthiness without losing grounding.
- **Set 3 — 3/5**
  - Specific in a different way: it references evidence pointers (`E#`) and makes concrete, testable recommendations (instrumentation, thin-slice integration choices, defaults, opt-out risks).
  - However, without the underlying evidence ledger in this artifact, the reader can’t verify claims directly from quotes; the specificity is “traceable in-system” but not “self-contained.”

### 4) Completeness
- **Set 1 — 4/5**
  - Hits most expected components: themes, opportunities, segments, recommendations, research questions, methodology notes.
  - Minor gaps: it doesn’t explicitly separate “what we know” vs “hypotheses to validate,” and some opportunity items (e.g., compliance prompts via Slack/email) are asserted with limited evidence discussion.
- **Set 2 — 5/5**
  - Most comprehensive and well-balanced as a synthesis deliverable: themes + segments + opportunities + recommendations + follow-up research + methodology notes.
  - The “tensions/counter-evidence” pattern reduces blind spots and helps avoid overfitting to a small sample.
- **Set 3 — 4/5**
  - Very complete for stakeholder use: causal model, themed evidence pointers, opportunity map with risks/dependencies, prioritisation rationale, and role-tailored briefs.
  - The main completeness trade-off is loss of transcript-level grounding (quotes, participant-by-participant nuance) and less explicit coverage of some UX issues (e.g., clutter/default views appear, but subordinate to the strategic frame).

### 5) Audience awareness
- **Set 1 — 3/5**
  - Appropriate for a product/design audience, but reads as a single-register “research doc” rather than differentiated stakeholder needs.
  - Some confident-sounding quantification (segment %s) could backfire with exec/analytics-minded readers.
- **Set 2 — 4/5**
  - Strong for a product trio / research-readership: structured, cautious, and action-oriented with crisp “implication” statements.
  - Still mostly one register; less explicitly packaged for executives/engineering constraints than Set 3.
- **Set 3 — 5/5**
  - Best stakeholder fit: separate exec/design/engineering briefs, explicit limitations, de-risking moves, and instrumentation guidance.
  - It anticipates how decisions get made (thin-slice bets, risk dependencies, defaults) and uses language that an exec can act on without reading the whole doc.

### 3) Natural Variation
- **Set 1 — N/A (single run)**
- **Set 2 — N/A (single run)**
- **Set 3 — N/A (single run)**

---

## RUN-ALL A4 expectation: catalogue themes vs strategic reframing
RUN-ALL’s stated expectation for A4 is: **“pipeline should free the synthesis to reframe rather than catalogue.”**

- **Set 1 and Set 2** primarily **catalogue themes** (albeit high-quality catalogues). They do connect themes into loops and opportunity logic, especially Set 2, but the organising principle remains “Theme 1..N.”
- **Set 3** most clearly delivers the **strategic reframing**: it leads with a “truth model,” makes the adoption problem a causal system (thresholds + reinforcing loops), and then derives opportunities, prioritisation, and de-risking from that model.

---

## Summary

| Dimension | Set 1 | Set 2 | Set 3 |
|---|---:|---:|---:|
| Depth | 3 | 4 | 5 |
| Specificity | 4 | 5 | 3 |
| Completeness | 4 | 5 | 4 |
| Audience awareness | 3 | 4 | 5 |

**Overall preference**: **Set 3** for stakeholder decision-making; **Set 2** for research-grade traceability and “show your work.”

**Key differences**
- Set 2 is the best *classic synthesis*: richly evidenced, cautious with claims, and broadly actionable.
- Set 3 is the best *strategic synthesis*: it reframes the problem into a causal model and provides decision-ready prioritisation + instrumentation, at the cost of being less self-contained on raw evidence.

**Magnitude**: **Moderate**.
- The difference is meaningful in practice if the goal is executive alignment and strategy (Set 3) versus detailed research documentation for product teams (Set 2).

## Diagnostic observations (beyond rubric)
- **Traceability trade-off**: Set 3’s `E#` pointers are a good internal traceability mechanism, but for external readers it can feel like “trust me.” If the evidence ledger is one click away in the workflow, this may be acceptable; if not, it weakens perceived rigor.
- **Over-precision risk**: Set 1’s segment percentage estimates from n=6 may reduce credibility with analytical stakeholders; Set 2 avoids this pitfall.
- **Template feel**: Sets 1 and 2 both use a familiar synthesis template; Set 3 feels less templated because the causal model is doing more work than the headings.
