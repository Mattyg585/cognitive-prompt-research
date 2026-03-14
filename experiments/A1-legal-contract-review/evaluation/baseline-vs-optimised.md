# Blind Evaluation: Set A vs Set B -- Contract Review Outputs

**Evaluator**: Independent blind evaluation (no knowledge of which set is baseline/optimised)
**Task**: Review of Common Paper Cloud Service Agreement v2.1 from the Customer (buyer) side
**Outputs evaluated**: Set A (3 runs), Set B (3 runs)
**Rubric**: evaluation/rubric.md
**Date**: 2026-03-14

---

## Step 1: Initial Impressions

**Set A** produces long, methodical, clause-by-clause reviews with extensive redline suggestions. The structure is consistent across runs: summary header, key findings, numbered clause-by-clause analysis, negotiation strategy, next steps. The tone is competent and thorough but reads like a structured template being filled in. The runs are remarkably similar to one another in structure, section count, and analytical emphasis.

**Set B** also produces clause-by-clause reviews but with noticeable differences in voice and framing. The key findings section in Set B provides analytical narrative rather than just listing issues -- it characterises the overall contract posture and explains *why* the findings matter before diving into clause-by-clause detail. The negotiation strategy sections model the counterparty's likely positions and suggest specific tactical sequencing. The runs show more variation in emphasis, structure, and which clauses receive detailed treatment.

---

## Step 2: Dimension Scoring

### 1. Depth (1-5)

**Set A: 3.5**

Set A competently identifies the major risk areas -- the ML/AI training clause (Section 1.6), the thin data protection framework (Section 3), the overbroad feedback clause (Section 1.4), liability cap dependency on Cover Page variables, and logo rights without consent. These are the findings a knowledgeable reviewer would expect. Set A follows each clause through the standard contract/deviation/impact/redline framework and does so thoroughly. However, Set A rarely goes beyond the expected. The analysis of each clause tends to identify the issue and then move to a redline suggestion without exploring second-order effects or interconnections between clauses. For instance, Set A Run 1 notes that Section 1.6 survives termination (Section 5.6) and flags it, which is a good connection -- but this insight appears more as a separate finding than as an integrated analysis of how the ML clause, survival clause, reservation of rights clause, and data protection gap compound into a systemic risk.

**Set B: 4**

Set B consistently goes deeper on the same core issues and, critically, connects them. Set B Run 1 explicitly identifies the "compound risk" created by the interaction of the feedback clause (1.4), ML training clause (1.6), and the survival provision (5.6), and explains why these provisions reinforce each other to create a data exploitation pipeline that persists after termination. Set B Run 2 makes a sharp observation about the ML clause's de-identification standard being "effort-based, not outcome-based" -- a precise legal distinction that moves beyond simply noting the standard is weak. Set B Run 3 provides a specific fallback for the ML clause that references defined de-identification standards (NIST SP 800-188, ISO/IEC 20889), showing domain-specific depth rather than generic alternatives. Set B also consistently analyses the Provider's likely motivations and product strategy (e.g., "the Provider chose this form, which signals a willingness to use commercially reasonable terms... Sections 1.4, 1.6, and the thin data protection provisions suggest the Provider either (a) has a product that relies on customer data for ML training and will resist narrowing those rights, or (b) adopted the template without customizing for data-sensitive use cases"), which demonstrates reasoning about the contract as a commercial relationship rather than just a document to mark up.

**Reasoning**: Set A covers the expected ground well. Set B does the same but follows more threads and makes non-obvious connections. The difference is moderate but meaningful -- Set B's analysis would give a lawyer preparing for negotiation more to work with.

---

### 2. Specificity (1-5)

**Set A: 3.5**

Set A consistently references specific section numbers and quotes contractual language. The redline suggestions include current language and proposed language side by side, which is actionable. However, the analysis sometimes falls into templated language -- phrases like "this is below market standard," "standard for SaaS agreements," and "should be reviewed by qualified legal counsel" appear frequently and add little specific value. The recommendations are grounded in the contract text but the reasoning connecting the contract text to the recommendation sometimes relies on general statements rather than specific analysis. For example, when discussing the damages waiver, all three runs note that "direct lost profits" are included, identify this as aggressive, and propose the same redline -- but the reasoning is brief and the same across runs.

**Set B: 4**

Set B is similarly grounded in specific contract text but does more with it. When Set B discusses the ML clause, it does not just say the de-identification standard is weak -- it explains precisely why ("it is effort-based, not outcome-based, and provides no guarantee that re-identification is impossible"). When discussing the data protection gap, Set B Run 1 specifically lists non-GDPR regimes by name (CCPA, PIPEDA, state privacy laws) rather than just saying "other data protection laws." Set B's fallback positions are more specific: Set B Run 3 proposes that Customer Content ML training should require aggregation with "at least [50] other customers" and reference specific de-identification standards (NIST SP 800-188 or ISO/IEC 20889). These are more actionable and specific than Set A's fallbacks, which tend toward general principles ("require strict anonymization" or "replace 'commercially reasonable efforts' with a defined standard").

**Reasoning**: Both sets reference the contract text well. Set B provides more precise and actionable analysis, particularly in its fallback positions and its characterisation of why specific language is problematic. Set A is solid but occasionally generic in its reasoning.

---

### 3. Natural Variation (1-5)

*Scored across runs within each set.*

**Set A: 2**

Set A's three runs are strikingly similar. All three runs:
- Identify the same 5 key findings in the same order (Section 1.6 RED, Section 3 RED, Section 1.4 YELLOW, Section 8 YELLOW, Section 12.8 YELLOW)
- Analyse the same ~20 clauses in the same order
- Classify all clauses identically (same GREEN/YELLOW/RED ratings)
- Include essentially the same redline suggestions with minor wording variation
- Include the same "NOT ADDRESSED" sections (Insurance in all three, SLA in Run 2)
- Follow the identical structure: Summary -> Key Findings -> Clause-by-Clause -> Negotiation Strategy -> Next Steps
- Produce the same negotiation strategy tiers with the same items in the same priority order

The wording varies between runs, and there are minor differences in emphasis (Run 2 adds an SLA section not present in Run 1 or 3; Run 1 includes slightly different insurance minimums). But the overall shape, count, and substance of the outputs are near-identical. If you removed the wording variation, the analytical skeleton is the same document three times.

**Set B: 3**

Set B shows more variation across runs, though all three share the same core analysis (as they should -- the contract is the same). Notable differences:

- **Structure**: Set B Run 1 uses blockquote formatting for redlines and a "Why it matters" subheading that the other runs use inconsistently. Set B Run 2 uses a different emphasis pattern -- it gives the representations and warranties section (Section 6) a YELLOW rating and provides a detailed redline proposing conformity-with-documentation and availability warranties, which neither Set B Run 1 nor Run 3 does. Set B Run 3 uses the "Classification: YELLOW -- Escalate" labelling convention.
- **Clause coverage**: Set B Run 2 is the most expansive -- it rates the warranty section YELLOW and provides a substantive SLA redline directly in the warranties analysis. Set B Run 1 and Run 3 rate warranties GREEN with briefer treatment. Set B Run 3 has a notably different termination-for-convenience proposal (60 days with an early termination fee equal to 3 months of Fees, rather than 90 days with prorated refund).
- **Negotiation strategy**: The counterparty modelling varies -- Set B Run 1 discusses the Provider's product roadmap motivation in detail; Set B Run 3 includes a specific "Concession Strategy" table (concede/trade/hold firm) that is more structured than the other two runs.
- **Finding count**: Set B Run 1 identifies 5 key findings; Set B Run 2 identifies 3 key findings plus 2 supplementary items; Set B Run 3 identifies 3 key findings with expanded narrative.

The variation is genuine but moderate. The core analysis is consistent (it should be -- the same contract is being reviewed), but the emphasis, structure, and level of detail on secondary issues shift between runs.

**Reasoning**: Set A is nearly identical across runs, suggesting a rigid template is being followed regardless of analytical judgment. Set B shows more organic variation in emphasis and structure. Neither set truly demonstrates complexity-responsive output (since the input is the same contract each time, this dimension is somewhat limited), but Set B at least demonstrates that different runs can prioritise differently and format differently.

---

### 4. Completeness (1-5)

**Set A: 4**

Set A is comprehensive. It covers all major contract sections, identifies the key risk areas, flags issues that depend on the Cover Page/Order Form, notes missing provisions (insurance, SLA), and provides redline suggestions for each flagged issue. The negotiation strategy covers three tiers of priorities. The next steps are actionable. There is no major gap in coverage. The one weakness is a degree of padding in the GREEN sections -- many GREEN clauses receive 3-4 lines of analysis that effectively say "this is standard and acceptable," which adds volume without value.

**Set B: 4.5**

Set B covers the same material as Set A but with better weighting. The GREEN sections are handled more efficiently -- some are grouped together (Set B Run 1 groups Assignment, Force Majeure, Governing Law, and other general terms into a single combined GREEN section rather than giving each its own multi-paragraph analysis). This is not a loss of completeness; it is better calibration of analytical effort to risk. The RED and YELLOW sections receive proportionally more depth and analysis in Set B, particularly the ML training clause and the data protection framework. Set B also captures the survival clause interaction (Section 5.6 + Section 1.6) as a distinct issue, which Set A also does but with less emphasis. Set B Run 2 uniquely flags the warranty section as YELLOW and provides a substantive SLA/conformity redline, which is a genuine analytical contribution not present in Set A.

**Reasoning**: Both sets are comprehensive. Set B gets the slight edge because its depth is better allocated -- more analysis where it matters, less padding where it does not. The GREEN sections in Set A repeat the same "standard, no deviation, low risk" analysis across 8-10 clauses, while Set B handles low-risk sections more efficiently and invests the analytical budget in the high-risk areas.

---

### 5. Audience Awareness (1-5)

**Set A: 3**

Set A reads like a structured contract review memo. It is professional and thorough. The register is appropriate for a legal audience -- it uses proper contract terminology, references market standards, and provides actionable redlines. However, it does not particularly anticipate the audience's perspective. The tone is neutral and informational throughout, regardless of whether the issue is critical or minor. A lawyer reading Set A would know what the issues are and what to propose, but would need to do their own work to develop a negotiation strategy and anticipate counterarguments. The negotiation strategy section in Set A lists priorities by tier but does not model the counterparty's likely responses or suggest tactical sequencing beyond a basic timeline.

**Set B: 4.5**

Set B reads like a memo written by a lawyer who is preparing the reader to go into a negotiation. The key findings sections in Set B do not just list issues -- they characterise the contract's overall posture ("The contract is structurally balanced but has three areas requiring serious attention before signing") and frame the analysis in terms the reader can immediately use. The negotiation strategy sections model the counterparty explicitly: what the Provider is likely to push back on, why, and how to frame the Customer's asks to maximise the chance of acceptance. Set B Run 1's observation that Provider chose Common Paper "because it is perceived as balanced and vendor-friendly enough to avoid heavy negotiation" and that the Provider "will likely resist changes to the Standard Terms themselves and push modifications to the Cover Page and Order Form" is the kind of strategic insight a reader preparing for a real negotiation would value. Set B also consistently frames asks as "compliance-driven rather than adversarial" and suggests using regulatory requirements as leverage -- this is practical negotiation advice, not just legal analysis.

**Reasoning**: Set A serves the audience adequately. Set B serves the audience notably better by modelling how the reader will use the analysis -- not just "here are the issues and redlines" but "here is how to present these redlines to the other side, here is what they will push back on, and here is where to give ground."

---

### 6. Risk Identification Accuracy (Legal Domain Addition)

**Set A: 4**

Set A correctly identifies the genuinely risky clauses. The two RED flags (ML training on Customer Content and thin data protection framework) are the right calls. The YELLOW flags (feedback clause, liability caps, logo rights, suspension, termination) are all legitimate concerns. Set A does not produce false positives -- the GREEN classifications are appropriate. The one notable gap is that Set A does not consistently flag the survival of Section 1.6 as a standalone risk; Run 1 addresses it in the termination section but Runs 2 and 3 mention it only in passing.

**Set B: 4.5**

Set B identifies the same core risks with slightly better calibration. The RED flags are the same and equally well-justified. Set B adds value in three ways: (1) it more consistently and prominently flags the survival clause issue as amplifying the ML training risk; (2) Set B Run 2 uniquely identifies the warranty section as YELLOW on the basis that the warranty is narrower than market standard (protecting against functionality regression but not against performance failures, security deficiencies, or non-conformity with documentation) -- this is a genuine insight that Set A misses by rating the warranty GREEN across all runs; (3) Set B's analysis of the "combination with non-Provider items" exclusion in the indemnification section (flagged in Set A Run 2 and Run 3, but more systematically in Set B Run 2) correctly identifies a practical risk for a platform that will necessarily integrate with other systems.

**Reasoning**: Both sets identify the genuinely risky clauses accurately. Set B provides slightly better calibration on secondary risks and more consistently connects related provisions to show compound risk.

---

## Step 3: Summary

| Dimension | Set A | Set B | Delta |
|-----------|-------|-------|-------|
| Depth | 3.5 | 4 | +0.5 B |
| Specificity | 3.5 | 4 | +0.5 B |
| Natural Variation | 2 | 3 | +1 B |
| Completeness | 4 | 4.5 | +0.5 B |
| Audience Awareness | 3 | 4.5 | +1.5 B |
| Risk Identification Accuracy | 4 | 4.5 | +0.5 B |

**Overall preference**: Set B

**Key differences**: Set B does four things that Set A does not:

1. **Models the counterparty**: Set B's negotiation strategy sections anticipate the Provider's likely pushback, explain why, and suggest framing strategies. Set A lists priorities by tier but does not model the other side of the table.

2. **Connects clauses into compound risks**: Set B consistently analyses how the ML training clause (1.6), feedback clause (1.4), survival clause (5.6), and reservation of rights (11) interact to create a data exploitation pipeline that persists after termination. Set A addresses each clause but treats them more as independent findings.

3. **Calibrates depth to risk level**: Set B spends less time on GREEN sections and more time on RED sections. Set A gives roughly equal analytical treatment to every section, resulting in padding on low-risk clauses and less depth on high-risk clauses.

4. **Provides more precise fallbacks**: Set B's fallback positions reference specific de-identification standards (NIST SP 800-188, ISO/IEC 20889), specific aggregation thresholds, and specific tactical moves. Set A's fallbacks tend toward general principles.

**Magnitude**: Moderate. The difference is meaningful in practice. A lawyer receiving Set B's output would be better prepared for a negotiation than one receiving Set A's output. The core risk identification is similar, but the analytical depth, strategic framing, and practical specificity in Set B would save the lawyer meaningful preparation time. The difference is most pronounced in audience awareness and natural variation.

---

## Step 4: Diagnostic Observations

### Count Uniformity

**Set A exhibits high count uniformity.** All three runs produce 5 key findings, analyse approximately 20 clause sections, identify 2 RED / 5 YELLOW / 13 GREEN issues, and produce a 3-tier negotiation strategy with approximately the same number of items per tier. This is a hallmark of template-driven output -- the structure is determined before the analysis, not by it.

**Set B exhibits moderate count uniformity.** The key findings count varies (5, 3+2, 3). The clause sections analysed vary slightly (some runs group low-risk sections together). The classification counts are similar but not identical across runs (Run 2 rates the warranty section YELLOW; Runs 1 and 3 rate it GREEN). The negotiation strategy structure varies between runs (Run 3 includes a concede/trade/hold-firm table). This is closer to what you would expect from a reviewer exercising independent judgment on each pass.

### Out-of-Category Findings

**Set A** flags two out-of-category issues: missing insurance provisions and (in Run 2) missing SLA/uptime commitments. These are findings that go beyond the four corners of the contract text to identify what *should* be present but is not. This is good practice and is consistent across runs.

**Set B** also flags missing insurance provisions but does so less consistently -- not all Set B runs call it out as prominently. However, Set B Run 2 provides the unique out-of-category finding of rating the warranty section YELLOW and proposing an SLA-like warranty, which is a more analytically interesting finding because it identifies a hidden risk in an apparently acceptable clause rather than just noting a missing provision.

### Negotiation Strategy Quality

This is the widest gap between the two sets.

**Set A's** negotiation strategy sections list priorities in three tiers and provide a basic timeline. They do not model the counterparty's likely positions, do not suggest framing strategies, and do not identify leverage points beyond the inherent commercial dynamics. The recommended approach in Set A is essentially "send redlines in priority order and trade Tier 3 for Tier 2." This is adequate but generic -- it could apply to any contract negotiation.

**Set B's** negotiation strategy sections are substantially more useful. They model the Provider's likely positions ("Provider will likely push back hardest on the ML/AI training clause, as this may be core to their product roadmap"), suggest specific framing strategies ("frame the ML/AI redline as a data governance issue, not a commercial objection -- this is harder to resist than a pure commercial objection because it aligns with regulatory trends"), identify specific leverage points ("new relationship: Customer has no switching costs yet"), and provide tactical sequencing advice ("lead with data protection -- this is the strongest negotiation position because it is grounded in regulatory compliance, not preference"). Set B Run 3 includes a concede/trade/hold-firm framework that maps concession strategy explicitly. This is the kind of strategic thinking that distinguishes a good lawyer from a thorough one.

### Register

**Set A** reads like a contract review checklist produced by a paralegal or junior associate. It is competent, thorough, and reliable -- but it is fundamentally a document review exercise. The reader is given the findings and told what to do, but not how to think about the negotiation.

**Set B** reads like a senior associate or counsel preparing a partner for a negotiation. It provides the same findings but frames them in terms of strategic objectives, counterparty dynamics, and practical execution. The reader is not just told what the issues are -- they are told how to present them, what resistance to expect, and where to give ground.

This difference in register is consistent across all three runs of each set and is the most immediately noticeable qualitative distinction between the two.

---

## Overall Assessment

**Set B is the better output.** The difference is moderate -- not transformative, but clearly meaningful. Both sets correctly identify the core risks and provide reasonable redline suggestions. The gap is in the quality of analysis around those findings: how they are connected to each other, how they are framed for the audience, and how the negotiation strategy anticipates real-world dynamics.

If I were a lawyer receiving one of these outputs to prepare for a contract negotiation, I would prefer Set B. Set A would require me to do additional work to develop a negotiation strategy and anticipate counterarguments. Set B has already done much of that work for me.

The difference is large enough to matter in practice, particularly for the audience awareness and negotiation strategy dimensions. The risk identification is comparable; the analytical framing and practical utility are not.
