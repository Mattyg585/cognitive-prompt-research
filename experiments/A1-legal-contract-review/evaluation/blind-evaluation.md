# A1 Evaluation: Legal Contract Review — Three-Tier Comparison

**Evaluator**: Claude Opus 4.6 (1M context)
**Date**: 2026-03-14
**Task**: Review Common Paper Cloud Service Agreement v2.1 from the customer perspective
**Versions compared**: Version A (3 runs), Version B (3 runs), Version C (3 runs)
**Rubric**: 5-dimension scoring from `evaluation/rubric.md` plus domain-specific "Risk identification accuracy"

> **Transparency note**: The evaluator orchestrated the experiment runs and therefore knows the version identities. True blindness was not achievable in this session. The evaluation attempts honest assessment against the absolute rubric scale regardless.

---

## Dimension 1: Depth (1-5)

### Version A — Score: 3

All three runs identify the same core issues: ML training rights over Customer Content (RED), thin data protection framework (RED), and a consistent set of YELLOW findings (feedback clause, liability caps, suspension, logo rights, termination). Analysis follows a predictable pattern — "contract says X, standard position is Y, deviation is Z" — and produces competent, expected findings. Business impact assessments are adequate but read as categorised ("Low risk," "Moderate," "High") rather than reasoned. Compound risks are mentioned in passing (e.g., "the survival of ML rights post-termination is concerning") but not traced through the contract's architecture.

The negotiation strategy in all three runs is a straightforward tiered list. It identifies what to lead with and what to concede but does not model why those priorities matter differently for this specific deal, or how the counterparty's likely responses should shape the approach.

**Assessment**: Covers expected ground competently. Finds what a knowledgeable reviewer would expect to find.

### Version B — Score: 3.5

Same core issues identified as Version A. The improvement is in framing and connection. Key Findings sections open with contextual framing ("The contract is a well-structured, industry-standard cloud service agreement that leans moderately toward the Provider") before listing issues. The "why it matters" explanations are more grounded in the specific deal context. Some compound risk identification appears (feedback + ML training creating a "compound right that exceeds typical SaaS terms").

Negotiation strategy sections are more developed — they model the counterparty's likely pushback, discuss leverage points, and provide more specific sequencing advice. But the strategic reasoning still reads as an extension of the clause analysis rather than independent reasoning about the deal.

Variable depth across clauses is better — important issues get more space, acceptable provisions are grouped or noted briefly. This responds to the contract's actual content rather than giving every clause equal structural weight.

**Assessment**: Goes slightly beyond the expected. Connects some non-obvious dots, particularly in framing compound risks and counterparty positioning.

### Version C — Score: 4.5

The investigation stage (Contract Reader) surfaces findings that neither Version A nor Version B identifies:

- The security testing prohibition is absolute — no carveout for coordinated penetration testing with Provider consent
- The derivative works prohibition is absolute — no carveout for Customer configurations or integrations
- "Aggregated" is undefined, and the threshold for meaningful aggregation is unspecified
- The de-identification standard is "doubly qualified" — both "commercially reasonable" AND "industry standard" — creating a moving target
- Customer's payment obligations continue during suspension with no credit or abatement mechanism
- The entire data rights chain (Sections 1.4 → 1.5 → 1.6 → 5.5 → 5.6 → 11.1) creates perpetual, surviving, compound rights over Customer data
- "Related offerings" in Section 1.5 extends Provider's content license with no definition of scope
- The Cover Page deferral pattern is identified as a systematic feature, not just a collection of undefined variables

The deviation analysis (Playbook Comparator) finds more deviations overall — 5 Escalate + 12 Negotiate in one run, versus 2 RED + 5-7 YELLOW in Versions A and B. It also identifies provisions that fall outside standard categories entirely, which the other versions silently drop.

The strategic reasoning (Strategic Advisor) is qualitatively different from both other versions. It reads the vendor's priorities from their drafting patterns ("the specificity and breadth of Section 1.6 suggest this is strategically important to their product roadmap"), identifies that the contract's risk is "architectural, not clause-level," and provides genuinely surprising observations (e.g., suspension as a mechanism that "achieves the functional equivalent of termination" while "bypassing every procedural safeguard the termination clause provides").

**Assessment**: Surprising insights that reframe how you think about the contract. The investigation discovers things the evaluation-fused versions miss, and the strategy reasons about the deal rather than restating the findings.

---

## Dimension 2: Specificity (1-5)

### Version A — Score: 3.5

Grounds analysis in the actual contract. Quotes key language, references section numbers, provides specific redline text. Dollar amounts are proposed for liability caps and insurance. But business impact assessments tend toward categorical labels ("Moderate risk") rather than specific reasoning about this deal's particular dynamics. Redlines are specific and insertable.

### Version B — Score: 3.5

Similar level of textual specificity. Slightly better at connecting specifics to the deal context (e.g., "$150K/year is meaningful for a mid-market vendor"). The improvement over Version A in this dimension is marginal.

### Version C — Score: 4.5

The Contract Reader output quotes extensively and precisely, but more importantly, it traces specific clause interactions — mapping the chain from Section 1.5 through 1.6 through 5.6 through 11.1 with quoted language at each step. The Redline Writer produces more detailed alternative language with specific drafting considerations (e.g., aggregation thresholds of "at least 50 other customers," specific de-identification standards like "NIST SP 800-188 or ISO/IEC 20889").

The Strategic Advisor is highly specific to THIS deal:
- "At $150K/year you are a meaningful mid-market customer — large enough that losing you matters to the sales team, small enough that you will not get the vendor's most senior legal resources"
- "Does your organisation accept any ML training on Customer Content with opt-in consent, or does it require complete prohibition? The entire data sovereignty negotiation branches on this answer."
- "If their responses are slow, partial, or non-substantive, that is a negotiation tactic."

Every recommendation is traceable to specific contract provisions, specific deal dynamics, or specific counterparty signals.

---

## Dimension 3: Natural Variation (1-5)

*Scored across multiple runs of the same version.*

### Version A — Score: 2

All three runs produce nearly identical structure: Summary → 5 Key Findings → Clause-by-Clause (same categories, same order) → Negotiation Strategy (3 tiers) → Next Steps. The same RED flags appear in all runs with very similar wording. YELLOW flags vary slightly in count (5-7) but cover the same provisions. The output template imposed by the prompt dominates the structure — different runs feel like slightly rephrased versions of the same document.

### Version B — Score: 2.5

Similar structural consistency to Version A. Key Findings sections all open with a contextual sentence then list 3-5 items. Some variation in emphasis and depth allocation, and slightly more variation in the negotiation strategy section. But the overall shape of the output is consistent across runs.

### Version C — Score: 3.5

More variation across runs, particularly in the investigation stage. The Contract Reader outputs differ meaningfully in what they emphasise, how they organise material, and what they surface as unusual:
- Run 1: 7 unusual provisions, 12 notable absences, 8 material interactions
- Run 2: 7 unusual provisions, 11 notable absences, 8 material interactions
- Run 3: 8 unusual provisions, 11 notable absences, 8 material interactions

The Playbook Comparator classifications vary more across runs (5-7 Escalate items, 12-14 Negotiate items). The Strategic Advisor outputs differ meaningfully in framing and emphasis — one leads with the "accountability vacuum," another with the "compound problem" of data rights, another with the distinction between tool and partnership. The outputs respond to the same contract but with genuinely different analytical emphases.

That said, all three runs converge on the same core findings. The variation is in emphasis, framing, and depth allocation — not in what is identified. This is appropriate for a deterministic contract review (the contract is the same each time).

---

## Dimension 4: Completeness (1-5)

### Version A — Score: 3

Covers major clause categories systematically. Identifies the two most critical issues (ML training, data protection). Includes redlines for YELLOW and RED items with fallback positions. Includes negotiation strategy and next steps. But misses several notable items that the pipeline surfaces: the Cover Page deferral as a systematic risk-shifting pattern, the security testing prohibition's absolute nature, payment continuation during suspension, compound architectural risks, provisions that fall outside standard playbook categories.

Some areas are treated superficially — indemnification exclusions are flagged in only 1 of 3 runs, the SLA absence is noted as an afterthought rather than analysed, and the warranty's 90-day remedy cycle is noted but not connected to the broader remedies landscape.

### Version B — Score: 3.5

Slightly more complete than Version A. Better at noting compound risks. Better at variable depth — boilerplate clauses get less structural weight. Some runs include the SLA and warranty as more substantive findings. Still misses several items the pipeline surfaces. The improvement is incremental, not structural.

### Version C — Score: 5

Significantly more comprehensive at every stage:

- The Contract Reader surfaces things no other version finds: absolute derivative works prohibition without configuration carveout, unqualified user account responsibility for all actions, undefined "aggregated," doubly-qualified de-identification standard, payment obligation during suspension, the entire Cover Page deferral pattern as a systematic feature
- The Playbook Comparator finds more deviations AND identifies "provisions outside playbook categories" — items that a category-driven evaluation would silently drop. This is a structural completeness gain: the evaluation admits the limits of its own framework
- The Redline Writer covers more items with more detailed alternative language, and connects related redlines into negotiation packages
- The Strategic Advisor provides comprehensive counterparty analysis, internal decision requirements, and contingency planning that no other version includes

Critically, the depth is proportional to significance. The most important findings receive the most analytical weight. Minor items are noted efficiently. The output earns its length — there is no padding or uniform-depth-across-all-clauses inflation.

---

## Dimension 5: Audience Awareness (1-5)

### Version A — Score: 3

Appropriate register for a legal/procurement audience. Priority classifications (Must-have / Should-have / Nice-to-have) are useful. Redline formatting is consistent and professional. But the output reads as a report about the contract rather than advice to someone who is about to negotiate it. The negotiation strategy section tells you what to do but not how to do it or why specific approaches would work.

### Version B — Score: 3.5

Similar register with slightly better framing. Key Findings sections contextualise before listing. Negotiation strategy sections include more practical advice about sequencing and counterparty positioning. Some runs anticipate the reader's internal dynamics ("the Customer should not accept risk it would not otherwise accept simply because of time pressure"). But the output still primarily reads as analysis rather than preparation.

### Version C — Score: 5

The Strategic Advisor output is written for someone about to walk into a negotiation, not someone reading a report:

- "Frame everything as 'our procurement process requires this' rather than 'your contract is unfair.' The former is a problem to solve together; the latter is an argument to win."
- "Do not drip-feed issues — it frustrates the counterparty, invites piecemeal responses, and wastes time on sequential exchanges."
- "A 60-minute call resolves more than three rounds of email."
- "Before entering the negotiation, resolve one internal question: Does your organisation accept any ML training on Customer Content with opt-in consent, or does it require complete prohibition?"
- "If their responses are slow, partial, or non-substantive, that is a negotiation tactic."

The output anticipates what the reader needs to know, what decisions they need to make before they can act, and how the counterparty will respond. It understands that its audience is not evaluating a contract — they are preparing for a conversation. This is the difference between describing findings and equipping the reader to use them.

The Contract Reader output correctly serves its downstream audience (the comparator), using quoted language and factual descriptions that enable systematic evaluation without investigative bias. The Redline Writer calibrates tone and aggressiveness to the specific relationship (new vendor, mid-market, standard procurement). Each stage is audience-aware for its specific audience.

---

## Domain-Specific: Risk Identification Accuracy (1-5)

### Version A — Score: 3

Identifies the genuinely risky clauses (ML training, data protection). The two RED flags are the right two RED flags. But misses some second-order risks — the compound effect of multiple provisions working together, the systemic pattern of Cover Page deferral, and the suspension clause's functional equivalence to termination without safeguards.

### Version B — Score: 3.5

Same core risk identification with slightly better compound risk awareness. The feedback + ML training interaction is noted. The survival clause's amplification of ML risk is identified. But the risk analysis is still primarily clause-level rather than architectural.

### Version C — Score: 4.5

Identifies more risks and — critically — maps their interactions into architectural patterns:
- "This contract's risk is architectural, not clause-level"
- The data rights chain (1.4 → 1.5 → 1.6 → 5.5 → 5.6 → 11.1) as a compound system
- Suspension as a termination bypass mechanism
- The accountability vacuum: no performance standards to breach + no audit rights to discover failures + no notification to surface incidents = structural unaccountability
- ML rights + change of control + survival as a compound scenario
- Cover Page deferral as a systematic vendor advantage

These are not just more findings — they are a different kind of finding. The pipeline surfaces architectural risks that a clause-by-clause analysis structurally cannot see because the evaluation framework pre-organises the analysis by clause.

---

## Summary

| Dimension | Version A | Version B | Version C | A→B Delta | B→C Delta |
|-----------|-----------|-----------|-----------|-----------|-----------|
| Depth | 3.0 | 3.5 | 4.5 | +0.5 | +1.0 |
| Specificity | 3.5 | 3.5 | 4.5 | 0.0 | +1.0 |
| Natural Variation | 2.0 | 2.5 | 3.5 | +0.5 | +1.0 |
| Completeness | 3.0 | 3.5 | 5.0 | +0.5 | +1.5 |
| Audience Awareness | 3.0 | 3.5 | 5.0 | +0.5 | +1.5 |
| Risk Identification | 3.0 | 3.5 | 4.5 | +0.5 | +1.0 |
| **Average** | **2.9** | **3.3** | **4.5** | **+0.4** | **+1.2** |

**Overall preference**: Version C

**Key differences**: Version C produces qualitatively different output, not just incrementally better output. The investigation discovers things that the evaluation-fused versions structurally cannot see. The strategic reasoning models the counterparty and reasons about the deal rather than restating deviation classifications. The redlines are shaped by deal context rather than defaulting to generic "standard market position" language.

Version B improves on Version A incrementally — better framing, better compound risk awareness, better variable depth. But the improvement is marginal and stays within the same analytical ceiling. A→B is a refinement. B→C is a qualitative leap.

**Magnitude**: **Large.** The difference between Versions A/B and Version C is large enough to matter materially in practice. A lawyer receiving Version C output is better prepared for the actual negotiation — they understand the counterparty's likely motivations, they know what internal decisions to make before the first call, and they have a coherent strategy rather than a prioritised list of deviations. The investigation surfaces findings that would change how a careful reviewer approaches the contract. The gap is not about polish or formatting — it is about what the analysis sees and how it equips the reader.

---

## Diagnostic Observations

### What the rubric doesn't fully capture

1. **Structural coherence of strategy.** Version C's Strategic Advisor produces strategy that reads as a unified approach to a deal, not a collection of clause-level recommendations assembled into tiers. The difference is striking — Versions A and B produce tiered lists of issues with brief connecting text. Version C produces a negotiation arc with internal logic (lead with data, present security as a gate, package operational items, hold concessions). This coherence is more than the sum of the dimension scores.

2. **The investigation ceiling.** The most important finding may be what the Contract Reader discovers that the monolithic versions miss entirely. When investigation and evaluation share a context, the evaluation criteria pre-filter what the investigator notices. The pipeline's Contract Reader — which has no evaluation criteria in its context — surfaces findings (absolute security testing ban, payment during suspension, undefined aggregation threshold, doubly-qualified de-identification) that the monolithic versions consistently miss across all runs. This is the core claim of the cognitive mode interference theory, and the evidence supports it.

3. **Redline calibration.** Version C's Redline Writer produces language calibrated to the deal relationship ("new vendor, mid-market, standard procurement"), while Versions A and B produce redlines that could apply to any SaaS contract review. The difference is visible in tone, in how aggressively positions are stated, and in how fallback positions are framed. Version C's fallbacks read as genuine alternative positions; Versions A and B's fallbacks often read as slightly diluted versions of the primary ask.

4. **The counterparty as a real entity.** Version C's Strategic Advisor treats the counterparty as a specific vendor with motivations, constraints, and a product roadmap — not as a generic "the other side." It reads drafting choices as signals of strategic priorities, predicts where resistance will be principled versus reflexive, and identifies where the vendor has genuine flexibility. This transforms the strategy section from "here's what to ask for" into "here's how the conversation will go and how to navigate it."

5. **Internal decision requirements.** Version C consistently identifies decisions the reader must make BEFORE negotiating (e.g., "Does your organisation accept opt-in consent for ML training, or only complete prohibition?"). Neither Version A nor Version B surfaces these upstream dependencies. This is perhaps the most practically valuable difference — it prevents the reader from entering a negotiation without having resolved the internal questions that determine what outcomes are acceptable.

---

## Version Identity Reveal

| Label | Identity | Description |
|-------|----------|-------------|
| Version A | **Baseline (Tier 1)** | Original monolithic prompt, as-is |
| Version B | **Optimised (Tier 2)** | Same structure, cognitive hygiene improvements (numeric anchors removed, seeds converted to lenses, scope boundaries added, investigation separated from evaluation in prompt structure) |
| Version C | **Pipeline (Tier 3)** | Four cognitively scoped agents (Contract Reader → Playbook Comparator → Redline Writer → Strategic Advisor), each running in a clean context with compressed structured handoffs |

---

## Conclusion

The experiment's core hypothesis is supported by the results:

- **Tier 2 (Optimised) improves incrementally over Tier 1 (Baseline).** Average delta: +0.4 points across dimensions. The improvements are real but marginal — better framing, better compound risk awareness, better variable depth. The output stays within the same analytical ceiling.

- **Tier 3 (Pipeline) produces a qualitative leap over both Tier 1 and Tier 2.** Average delta from Tier 2: +1.2 points. The improvement is not marginal — it is structural. The pipeline discovers things the monolithic versions cannot see, reasons about the deal in ways the monolithic versions do not, and equips the reader for action in ways the monolithic versions fail to.

The finding is consistent with the hypothesis: **the monolithic prompt is the ceiling, not the floor.** Prompt-level optimisation (Tier 2) improves the margins but cannot eliminate the core interference between investigation and evaluation. The pipeline separates the cognitive modes into clean contexts, and the result is output that is qualitatively different — not just quantitatively better.
