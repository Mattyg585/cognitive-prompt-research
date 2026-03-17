# A1 Evaluation: Tier 2 (Optimised) — Five-Run Blind Scoring

**Evaluator**: Claude Sonnet 4.6
**Date**: 2026-03-17
**Task**: Score five optimised-prompt contract review outputs independently, without knowing which are from which revision of the optimised prompt.
**Rubric**: `evaluation/rubric.md` — 5 dimensions plus domain-specific risk identification accuracy
**Focus areas per brief**: Investigation breadth, working theory / commercial logic, redline quality, strategic depth, natural variation

---

## Method

Each run was read and scored independently on the rubric's absolute scale before any comparison was made. Natural Variation (Dimension 3) is scored once across the five runs at the end, since it is a cross-run dimension by design. The domain-specific dimension (Risk Identification Accuracy) is applied to all runs.

---

## Run-by-Run Scores

---

### Run 1

#### Dimension 1: Depth — 4

The output opens with a "Working Theory of the Contract" section that goes beyond enumeration. It identifies the Section 11 / 1.5 / 1.6 interplay as a structural one-way flow — Customer Content in, broad ML training rights retained — and explicitly calls out the "commercially reasonable" de-identification standard as "not a standard; it is an escape hatch." It spots the "damages waiver on direct lost profits hits the Customer harder — the Customer's losses from platform failure are business-operational; the Provider's losses are limited to unpaid fees" asymmetry. The survival of Section 1.6 post-termination creating a "perpetual, irrevocable" condition is identified and called an unusual amplification. Section 8.2's exclusion of "lost profits whether direct or indirect" is correctly flagged as RED rather than YELLOW — a judgment call that most runs miss or soften.

What prevents a 5: the investigation still primarily runs clause-by-clause within the body of the analysis. The Working Theory reads as a thoughtful preamble rather than a perspective that genuinely reorganises the clause findings. The security testing prohibition, payment continuation during suspension, and the undefined aggregation threshold do not appear.

**Score: 4**

#### Dimension 2: Specificity — 4

Section-level references are consistently precise. Key language is quoted, not paraphrased. The direct-lost-profits issue is traced to the specific parenthetical "(whether direct or indirect)" and the redline is calibrated to exactly that language. The Cover Page liability analysis is specifically tied to the $150K figure (12/24 months of fees). The survival / ML training interaction is traced through Section 5.6 with quoted language showing which sections survive. The counterparty analysis in the Negotiation Strategy names specific provider behaviours — "preserving ML/AI training rights, which are increasingly central to SaaS product strategy and valuation narratives" — rather than generic counterparty framing.

**Score: 4**

#### Dimension 4: Completeness — 4

Covers the two RED items comprehensively (ML training, data protection), includes the direct lost profits issue as a third RED (which other runs treat as YELLOW or miss entirely), handles the full gamut of YELLOW items, and specifically addresses the Cover Page deferral as a negotiation consequence rather than just a gap. The Working Theory section is substantive rather than decorative. The Next Steps section is specific and actionable, including an escalation planning item ("If Provider refuses to modify Section 1.6 materially, escalate to senior counsel for a risk acceptance decision"). The BATNA section in the Negotiation Strategy is genuinely analytical — it identifies why $150K is meaningful but not transformative, and why that creates moderate rather than strong leverage. The Order Form checklist in Next Steps is the most comprehensive of any run.

Missing: the security testing prohibition's absolute nature, the "related offerings" scope creep in Section 1.5, payment during suspension, and the undefined aggregation threshold. The warranty is classified GREEN where most thoughtful reviewers would flag it as YELLOW given its extreme narrowness.

**Score: 4**

#### Dimension 5: Audience Awareness — 4

The Working Theory section repositions the output for a reader who is trying to understand the deal's architecture, not just catalogue its provisions. The Negotiation Strategy section models the counterparty with notable specificity — "Provider's likely priorities: (1) preserving ML/AI training rights... (2) limiting data protection obligations... (3) maintaining broad liability protections" — and connects those priorities to specific drafting choices. The BATNA analysis is written for someone who needs to know whether they can walk away, not someone reading a report. The day-by-day timeline is the most detailed of any run. The concession strategy (Concede / Trade / Hold Firm) is directly actionable.

The output does not fully anticipate what internal decisions the reader needs to make before entering the negotiation — there is no equivalent of "resolve one internal question before you start." But it comes closer than the median run.

**Score: 4**

#### Domain-Specific: Risk Identification Accuracy — 4

Identifies the two core RED risks correctly and, uniquely among the five runs, elevates the direct lost profits exclusion to RED rather than YELLOW. The compound risk of ML training + survival of Section 1.6 is explicitly named and analysed. The Cover Page deferral as a structural risk pattern (not just a collection of undefined variables) is present, though briefly. The Section 11 / 1.6 interaction is correctly identified — Customer's retained ownership is described as "hollow if Provider can train ML models on it indefinitely."

Misses: suspension as a functional termination bypass, payment during suspension, absolute nature of the security testing prohibition, and the warranty's narrowness.

**Score: 4**

**Run 1 Summary**: 4 / 4 / — / 4 / 4 / 4 (Risk ID)

---

### Run 2

#### Dimension 1: Depth — 3

Competent, standard coverage. The Key Findings section is well-framed ("The contract is a reasonably balanced SaaS agreement built on Common Paper's open-source template, but..."), and the compound risk framing is present — feedback + ML training creates a "compound right that exceeds typical SaaS terms." But the clause-by-clause body is analysis-as-checklist: "What the contract says / Deviation from standard / Why it matters / Redline." This format is useful but it predetermines what kind of finding is possible. Structural observations (what does the architecture of the contract create as a whole?) are absent from the body even when they appear briefly in the Key Findings.

The warranty analysis is more developed here than in most runs — a dedicated YELLOW section on Section 6.3 with a specific redline including a 99.5% uptime commitment and conformity-with-documentation warranty. That is a substantive addition not present in most runs. However, the survival clause analysis ("Note that Sections 1.4 and 1.6 survive termination") appears buried as a sub-note rather than treated as its own significant finding.

**Score: 3**

#### Dimension 2: Specificity — 3.5

Quotes key language, provides section references, and grounds redlines in specific contract text. The liability analysis is specific about the tiered cap structure and defers appropriately to Order Form negotiation with specific targets (12 months fees, 2x annual fees for Increased Claims). The warranty redline is specific — "the Cloud Service will be available at least 99.5% of the time during each calendar month, excluding scheduled maintenance" — and clearly drawn from this deal's context.

Loses some points for the counterparty analysis, which is less specific than Run 1's: "The Provider will likely push back hardest on the ML/AI training clause" is accurate but generic. The sequencing section is mostly tier-based rather than conversation-shaping.

**Score: 3.5**

#### Dimension 4: Completeness — 3.5

Covers more clause categories than most runs — the warranty gets dedicated analysis where other runs fold it into GREEN or treat it superficially. The Order Form checklist in Next Steps is detailed. Survival clause is noted, though briefly. Force majeure is called out with a specific payment survival note.

However, the direct lost profits issue is mentioned but not flagged separately — it is buried inside the Limitation of Liability section's analysis rather than elevated as a finding. The Feedback compound risk is identified but the interaction with ML training is not traced through to consequences. Section 11's qualification of Customer's ownership rights is not analysed as its own structural issue.

**Score: 3.5**

#### Dimension 5: Audience Awareness — 3.5

The two-tranche redline sequencing in the Next Steps section is genuinely useful and more specific than other runs ("Within 3 business days: Prepare and send the second tranche of redlines: warranty, termination for convenience, suspension notice, and Usage Data limitations"). The timeline risk section ("Two weeks is tight for a new vendor relationship with material data protection redlines") anticipates the reader's operational reality. The counterparty framing — noting that Common Paper was a deliberate vendor choice signalling willingness to use commercially reasonable terms — is present.

Does not anticipate what the reader needs to decide internally before negotiating. The strategy section reads as guidance for conducting negotiation rather than preparation for it.

**Score: 3.5**

#### Domain-Specific: Risk Identification Accuracy — 3.5

Identifies the two core RED risks. The warranty gap is correctly identified as a separate risk rather than just noted in passing. The compound feedback + ML training risk is flagged. The survival clause amplification of ML risk is noted.

Missing: the direct lost profits exclusion as a standalone RED finding, suspension as a business continuity risk with no meaningful notice (it is noted as YELLOW but without the operational impact reasoning), and the Cover Page deferral as a systematic risk-shifting pattern.

**Score: 3.5**

**Run 2 Summary**: 3 / 3.5 / — / 3.5 / 3.5 / 3.5 (Risk ID)

---

### Run 3

#### Dimension 1: Depth — 3.5

The output has a Working Theory section ("Risk flows predominantly toward the Customer once you look beyond the symmetrical surface") that identifies the formal balance / substantive imbalance tension. The Section 1.5 + 1.6 + 11 + 5.6 interaction is mapped — though as a list of related provisions rather than a traced architectural argument. The direct lost profits issue is elevated to RED in the Key Findings section with specific explanation ("The parenthetical 'whether direct or indirect' extends the exclusion beyond the standard consequential damages waiver to cover direct lost profits"). The suspension clause's significance is noted as part of the Working Theory.

The clause-by-clause analysis is less developed than the Key Findings and Working Theory sections — there is a consistent drop in analytical intensity from the opening synthesis to the body of the review. Several clause sections (Warranties, Confidentiality, Indemnification) are notably brief relative to their importance in the deal.

**Score: 3.5**

#### Dimension 2: Specificity — 4

Strong textual specificity throughout. The damages waiver issue is quoted precisely — "lost profits or revenues (whether direct or indirect)" — and the redline targets exactly that parenthetical. The Cover Page liability recommendations include specific numbers (12 months, 24 months, 2x vs 3x fees). The survival clause analysis quotes the specific sections that survive and traces the consequence explicitly.

The Working Theory section is notably specific in its structural analysis: "Provider retains broad rights over Customer Content (Sections 1.5, 1.6), can use Customer data to train AI/ML models including third-party ones, collects and uses Usage Data with minimal constraints, and can suspend access unilaterally" — each claim traceable to a specific provision. The Cover Page deferral pattern is identified as "a secondary structural point" with precise examples.

**Score: 4**

#### Dimension 4: Completeness — 3.5

The Working Theory section adds completeness that the clause-by-clause body does not fully deliver on. The direct lost profits issue is properly elevated. The survival clause gets dedicated YELLOW analysis. The Cover Page as a structural feature is explicitly discussed.

The clause-by-clause body has some inconsistency — Section 6 (Warranties) is classified GREEN without the analysis that would justify it given the warranty's narrow scope. Section 5.1-5.4 (Term and Termination) is also GREEN without the termination-for-convenience redline that most other runs include. These are genuine gaps in coverage, not judgment calls.

**Score: 3.5**

#### Dimension 5: Audience Awareness — 3.5

The Working Theory is well-written for a reader who needs to understand the deal before the details. The negotiation strategy section models the counterparty specifically — "The Provider is likely a mid-stage SaaS company building or integrating AI capabilities. The ML training clause (Section 1.6) is not boilerplate — it is a product strategy decision embedded in legal terms." The DPA discussion correctly identifies the Provider's structural weakness: "Deferring the DPA to a future obligation while expecting the Customer to sign the main agreement is a compliance shortcut, not a principled position."

The sequencing section is coherent and conversation-shaped rather than just issue-ordered. The BATNA section is specific and non-generic. The day-by-day timeline is specific without being over-detailed.

Does not clearly surface what internal decisions the reader must make before the negotiation. The termination-for-convenience omission from the clause-by-clause (classified GREEN without analysis) is likely to confuse a reader who expects to find negotiating guidance there.

**Score: 3.5**

#### Domain-Specific: Risk Identification Accuracy — 3.5

Identifies the two core REDs, elevates the direct lost profits issue to RED correctly, and maps the compound ML + survival risk. Suspension is included in the Working Theory but not as a separate finding with its own analysis in the body — the risk is named but not fully developed.

The WARRANTY classification as GREEN without analysis is a miss — the warranty's extreme narrowness (only covers non-reduction of general functionality, no conformity-with-documentation, no uptime) is a genuine risk for an operations platform. No run in this set catches the security testing prohibition's absolute nature.

**Score: 3.5**

**Run 3 Summary**: 3.5 / 4 / — / 3.5 / 3.5 / 3.5 (Risk ID)

---

### Run 4

#### Dimension 1: Depth — 3

Solid, consistent work. Identifies the two core RED issues, provides a structured clause-by-clause analysis, includes reasonable negotiation strategy. The Reservation of Rights section (Section 11) gets explicit analysis of how the "subject to Sections 1.5 and 1.6" qualification undercuts Customer's retained ownership — "Customer 'retains all rights' to its content, but those rights are materially qualified by Provider's right to use that content for AI training purposes." The ML fallback language is unusually specific: it names a threshold ("at least [50] other customers" for aggregation) and specific de-identification standards ("NIST SP 800-188 or ISO/IEC 20889").

What prevents a 4: the Working Theory is absent. The analysis proceeds clause-by-clause without synthesising the contract's overall risk architecture. The counterparty analysis in the Negotiation Strategy is accurate but generic. No structural observation that reframes the analysis.

**Score: 3**

#### Dimension 2: Specificity — 4

The ML fallback language naming specific de-identification standards (NIST SP 800-188, ISO/IEC 20889) and a specific aggregation threshold is more technically specific than any other run. The Section 11 analysis is precisely traced — quoted language, specific consequence identified. The Cover Page liability negotiation targets are specific and calibrated to the deal ($150K/year leading to $150K general cap, $450K increased cap). The redlines throughout are insertable without modification.

**Score: 4**

#### Dimension 4: Completeness — 3.5

Covers the main ground. The ML fallback specificity is a substantive addition. Section 11 (Reservation of Rights) gets real analysis rather than a brief mention. The Survival clause is properly addressed. The security testing prohibition is noted as an Order Form item rather than a redline, which is the right structural judgment.

The warranty gap that Run 2 catches is not present here — Section 6 is GREEN with only brief analysis. The direct lost profits issue is noted as an Order Form item rather than elevated as a RED risk. The Cover Page deferral as a systematic pattern is identified in the structural liability analysis but not synthesised into a broader observation about the agreement's architecture.

**Score: 3.5**

#### Dimension 5: Audience Awareness — 3

Good register. Priority classifications are consistent. Redlines are well-formatted. The concession strategy is direct ("Concede: Logo rights... Trade: Termination for convenience... Hold firm: ML training exclusion for Customer Content").

The strategy section, while organised, is primarily recommendation-oriented rather than preparation-oriented. The order in which items are listed in Next Steps is sensible but does not tell the reader how to walk into the first call, how to read the counterparty's responses, or what internal decisions to resolve first. The counterparty section reads: "The Provider will push back hardest on the ML/AI training clause." This is true and present in almost every run — it is accurate but not strategically generative.

**Score: 3**

#### Domain-Specific: Risk Identification Accuracy — 3.5

Identifies the core RED risks. The Section 11 / 1.6 structural interaction is explicitly analysed. The ML fallback specificity suggests deeper thinking about what de-identification actually requires technically. The survival clause amplification is identified.

The direct lost profits exclusion is not elevated as a RED finding. The warranty gap is not identified. No cross-run finding that distinguishes this run beyond the technical specificity of the ML redline.

**Score: 3.5**

**Run 4 Summary**: 3 / 4 / — / 3.5 / 3 / 3.5 (Risk ID)

---

### Run 5

#### Dimension 1: Depth — 4

The Working Theory section is the strongest in the set: "Ownership without practical control is a hollow right. This is the contract's deepest asymmetry and it is not visible from reading any single clause in isolation." This is not a restatement of clause findings — it is a genuine architectural insight about what the interlocking provisions create as a system. The analysis that follows the Working Theory is more integrated than other runs: specific clause findings are connected back to the architectural thesis rather than standing alone.

The negotiation strategy section is the most analytically developed: BATNA is explicitly calculated (Customer's BATNA is strong because no switching costs, no relationship equity, $150K meaningful but not transformative; Provider's BATNA is acquiring a customer they do not yet have, cost of concession is operational precedent-setting rather than commercial loss). The counterparty section specifically reads drafting choices as signals of strategic priorities: "The ML training clause (Section 1.6) is not boilerplate — it is a product strategy decision embedded in legal terms." The escalation note in Next Steps is the most specific: "If Provider refuses to modify Section 1.6 materially, escalate to senior counsel for a risk acceptance decision."

What prevents a 5: still misses the security testing prohibition's absolute nature, payment continuation during suspension, undefined aggregation threshold, and the warranty gap. The investigation stage does not surface structural features that a separation of investigation from evaluation would enable.

**Score: 4**

#### Dimension 2: Specificity — 4

The Sections 1.5 / 1.6 / 5.6 / 11 interaction is traced with quoted language at each step. The Working Theory's claim — "ownership without practical control is a hollow right" — is grounded in specific provisions rather than asserted generally. The negotiation sequencing is specific to this deal: "Open with data protection. This is the highest-leverage, lowest-friction ask." The BATNA analysis is calibrated to the deal's specifics. Redlines are specific and insertable.

**Score: 4**

#### Dimension 4: Completeness — 4

Covers all major RED and YELLOW items. The Working Theory adds genuine analytical value above what the clause-by-clause delivers. The BATNA section is substantive. The internal escalation path (brief business stakeholders on ML, escalate to senior counsel if Section 1.6 won't move) is present and specific — this kind of internal decision tree is not present in most runs. The Order Form checklist is comprehensive. The Cover Page deferral pattern is identified as a deliberate agreement structure, not just a collection of gaps.

The warranty gap and direct lost profits issue as an independent RED are absent, which is a coverage miss. But no run in this set catches both of those; Run 1 catches the direct lost profits issue and Run 2 catches the warranty gap.

**Score: 4**

#### Dimension 5: Audience Awareness — 4.5

This is the only run that explicitly stages the reader's preparation: "Before entering the negotiation, resolve one internal question" does not appear verbatim, but the equivalent appears in the BATNA section ("Does your organisation accept any ML training on Customer Content with opt-in consent, or does it require complete prohibition?") and in the escalation planning item ("If Provider refuses to modify Section 1.6 materially, escalate to senior counsel for a risk acceptance decision — The combination of ML training rights on Customer Content, survival post-termination, and vague de-identification standards creates a risk that should not be accepted at the procurement level").

The negotiation section models the counterparty as a real entity with motivations rather than as a generic adversary. The day-by-day timeline explicitly includes a buffer day (Day 14) and an escalation path if the Provider is non-responsive. The statement "A non-responsive legal team on a two-week timeline is a risk signal worth flagging to the business stakeholders" is the only run that specifically anticipates what non-response means and what to do about it.

**Score: 4.5**

#### Domain-Specific: Risk Identification Accuracy — 4

Identifies the two core RED risks with the strongest architectural framing of any run. The ML + survival interaction is traced as an "irreversible data transfer" with the specific observation that "trained models cannot be 'un-trained'" — the most precise articulation of why this risk matters in any run. The Section 11 / 1.6 interaction is named explicitly. The compound risk of ML + change of control is present in the BATNA section. The Cover Page as a structural risk-shifting mechanism is properly identified.

**Score: 4**

**Run 5 Summary**: 4 / 4 / — / 4 / 4.5 / 4 (Risk ID)

---

## Natural Variation: Cross-Run Score (Dimension 3)

*Scored across all five runs together.*

All five runs share the same overall structure: Header → (Working Theory in some runs) → Key Findings (2-3 RED, 2-3 YELLOW) → Clause-by-Clause (same 14-16 categories, same format within each) → Negotiation Strategy → Next Steps. The clause-by-clause structure is strongly templated — even the section order and the sub-header format ("What the contract says / Deviation from standard / Why it matters / Redline") are consistent across runs.

The meaningful variation is in two places: (1) whether a Working Theory section appears and how substantive it is (present in Runs 1, 3, 5; absent in Runs 2, 4), and (2) how the Key Findings section frames the top-line risk characterisation. Runs 1 and 5 elevate the direct lost profits issue as a RED. Run 2 adds the warranty gap as a separate finding. These are genuine differences in what each run identifies as worth flagging.

Within the clause-by-clause body, the findings are highly consistent across runs. All five identify the same core RED items (ML training, data protection), all five cover the same set of YELLOW items (Feedback, Suspension, Post-Termination, Survival, Liability caps, Logo rights), and all five miss the same items (security testing prohibition, payment during suspension, undefined aggregation threshold). The structural template is functioning as a ceiling on what the analysis can discover.

The variation that exists is in depth and quality of analysis within each section, not in what provisions are covered. This is a lower variation score than 4, but higher than 2 because the Working Theory divergence and the different RED flag elevations are meaningful.

**Natural Variation Score: 3** (some variation in findings count and emphasis, but structure and core findings are highly consistent)

---

## Comparative Summary

| Dimension | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
|-----------|-------|-------|-------|-------|-------|
| Depth | 4 | 3 | 3.5 | 3 | 4 |
| Specificity | 4 | 3.5 | 4 | 4 | 4 |
| Completeness | 4 | 3.5 | 3.5 | 3.5 | 4 |
| Audience Awareness | 4 | 3.5 | 3.5 | 3 | 4.5 |
| Risk Identification Accuracy | 4 | 3.5 | 3.5 | 3.5 | 4 |
| **Average** | **4.0** | **3.4** | **3.6** | **3.4** | **4.1** |

Natural Variation (across all five runs): **3**

### Rankings

1. **Run 5** — 4.1 average. Strongest Working Theory, most architecturally integrated analysis, best counterparty modelling, most developed BATNA reasoning, and the only run to anticipate escalation conditions explicitly. Audience awareness score of 4.5 is the highest in the set. The output reads as preparation for a negotiation rather than a report on a contract.

2. **Run 1** — 4.0 average, effectively tied with Run 5. Elevates the direct lost profits issue to RED correctly (unique to this run among the five). Strong on depth and completeness. The Cover Page deferral is analysed as a structural negotiating dynamic. The day-by-day timeline is the most specific. Slightly weaker than Run 5 on audience awareness — the counterparty analysis is less specific and the BATNA is less developed.

3. **Run 3** — 3.6 average. Working Theory is present and substantive. Elevates the direct lost profits issue to RED correctly (shared with Run 1). Strong specificity in the coverage it provides. The DROP in analytical intensity from the opening synthesis (Working Theory + Key Findings) to the clause-by-clause body is the main weakness — promising architecture, inconsistent execution. Termination-for-convenience classified GREEN without analysis is a specific gap.

4. **Run 2** — 3.4 average, tied with Run 4. Strongest on the warranty gap — the only run to give Section 6.3 substantive YELLOW analysis with a specific redline including uptime commitment. The two-tranche Next Steps sequencing is useful. The compound feedback + ML risk is well-framed. Misses the direct lost profits issue as a RED flag. Strategy section is less developed than Runs 1, 3, and 5.

4. **Run 4** — 3.4 average, tied with Run 2. Standout for the ML fallback specificity (NIST SP 800-188, ISO/IEC 20889 de-identification standards, [50] customer aggregation threshold). Section 11 analysis is precise. No Working Theory section, and the strategy section is the least prepared-to-negotiate of any run. The technical precision in the ML redlines is the distinguishing feature.

---

## Key Observations

### Investigation breadth

All five runs operate within the same investigative ceiling. The structural template — clause-by-clause analysis in section order — determines what gets noticed. None of the five runs identifies the security testing prohibition's absolute nature (no carveout for agreed penetration testing), payment continuation during suspension without credit or abatement, or the undefined aggregation threshold in Section 1.6. These gaps are consistent across all runs, which suggests they are a product of the prompt's structure rather than individual variation.

### Working theory / commercial logic

Runs 1, 3, and 5 include a Working Theory section. Run 5's is the most integrated — the thesis (ownership without practical control is hollow) is carried forward into the clause analysis. Run 1's Working Theory identifies the ML + survival ratchet as the key structural feature. Run 3's is present but the clause-by-clause body does not consistently refer back to it. Runs 2 and 4 lack a Working Theory, and the absence is noticeable — their Key Findings sections open mid-issue rather than with a frame that contextualises the analysis.

### Redline quality

Run 4's ML redline is the most technically specific (named de-identification standards, specific aggregation thresholds). Run 1's liability redlines are the most calibrated to deal context. Across all runs, the redlines are competent and insertable. The gap between these runs and a genuinely context-specific redline (one that varies tone and aggressiveness based on relationship dynamics, rather than defaulting to market-standard framing) is consistent — no run achieves redline language that reads as written for this particular negotiation rather than for any enterprise SaaS negotiation.

### Strategic depth

Run 5 is distinctly ahead. The BATNA section is explicitly calculated rather than asserted. The counterparty is analysed as a specific entity with identifiable motivations. The escalation conditions are specified. The internal decision requirements are surfaced. Runs 1 and 3 are strong in sequencing and framing but do not develop the full BATNA logic. Runs 2 and 4 provide actionable but less strategically sophisticated guidance.

### Structural ceiling

The most significant finding across the five runs is what they consistently do not do. The template inherited from the optimised prompt — whatever revision distinguishes the five runs from each other — does not enable the structural, architectural analysis that a separated investigation would produce. All five runs identify the same core issues, miss the same non-obvious issues, and produce roughly similar negotiation guidance. The variation is in quality of execution within a shared frame, not in the frame itself.

---

## Overall Assessment

**Best output for real work**: Run 5, with Run 1 as a close second. A practitioner receiving Run 5 would have a clearer sense of the deal's architecture, stronger negotiation preparation, and a more actionable strategy. Run 1 adds the direct lost profits RED elevation and the most specific timeline, which are practical advantages.

**Weakest output**: Runs 2 and 4 are tied. Run 2 compensates with the warranty gap finding; Run 4 compensates with the ML redline technical specificity. Neither has a Working Theory. Neither models the counterparty with the specificity that Runs 1, 3, and 5 achieve.

**Magnitude of variation within the set**: Small to moderate. The range from Run 2/4 (3.4) to Run 5 (4.1) is real but the outputs are recognisably from the same prompt generation process. They cover the same issues, miss the same issues, and reach the same conclusions. The differences are in how the analysis is framed, how the counterparty is modelled, and how well the output equips the reader for the negotiation. These are meaningful differences for a practitioner, but they do not represent different analytical frameworks — they represent better and worse execution of the same framework.

**Against the Tier 2 label from prior evaluation**: The five runs are consistent with the prior evaluation's Version B characterisation: "incremental improvements over baseline — better framing, better compound risk awareness, better variable depth — but staying within the same analytical ceiling." The best of these five runs (Run 5) reaches the upper end of what the prior evaluation called Version B (3.5 average). Run 5's Working Theory and BATNA sections are slightly more developed than the median Version B output, which suggests some within-version variation pushed one run to the high end. None of these runs approaches the structural qualities identified in Version C (the pipeline). The investigative ceiling is the same.
