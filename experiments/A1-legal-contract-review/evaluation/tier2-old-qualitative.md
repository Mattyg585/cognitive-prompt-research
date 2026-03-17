# Tier 2 Qualitative Assessment — Optimised Prompt (Original Experiment)

**Reviewer**: Senior legal consultant, acting as independent evaluator
**Date**: 2026-03-17
**Contract under review**: Common Paper Cloud Service Agreement v2.1, customer/buyer perspective, $150K/year SaaS, 2-week deadline
**Tier 2 version**: Optimised prompt (same structural approach as baseline, with cognitive hygiene improvements)

---

## Preliminary Note on Run Availability

The task requests assessment of three optimised-prompt runs (run-1, run-2, run-3). At the original experiment level, only one optimised run exists: `blind-comparison/review-8SNX69.md`, identified as the Optimised (Tier 2) output by `blind-comparison/KEY.md`. Three runs exist for model-specific subdirectories (gemini-3-pro-preview, gpt-5.2, gpt-5.2-codex), which use separately constructed optimised prompts tailored for those models and are assessed separately. The assessment below applies to the single available Tier 2 output from the original prompt version. Where relevant, observations are drawn from the blind evaluation scoring in `evaluation/blind-evaluation.md` and `evaluation/baseline-vs-optimised.md`, which scored this version against its baseline comparator using three runs each.

---

## Run 1 (review-8SNX69.md) — Qualitative Assessment

### Commercial Reasoning

This output understands WHY the clauses matter, not just that they deviate from standard. The treatment of Section 1.6 (Machine Learning) is the clearest example. The output does not simply report that Customer Content is included in ML training — it explains the mechanism of harm: training on operational data creates "risk that patterns, structures, or insights from Customer's operations inform a product used by competitors," it names the specific weakness of the "commercially reasonable efforts" standard as a subjective moving target rather than a firm obligation, and it calls out the third-party model training risk as a distinct exposure because "Customer has no visibility into or control over" those third parties. This is commercial reasoning, not clause comparison.

The negotiation strategy section reflects genuine commercial intelligence. The output reads the counterparty correctly: it recognises that the Provider chose Common Paper as a form signal, not just as a drafting convenience, and extracts commercial meaning from that choice — "the Provider either (a) has a product that relies on customer data for ML training and will resist narrowing those rights, or (b) adopted the template without customizing for data-sensitive use cases." This bifurcation is practically useful, because the negotiating approach differs between those two scenarios. The leverage analysis is also deal-specific rather than generic: "New relationship: Customer has no switching costs yet. Provider should be motivated to win the deal on reasonable terms." This is the kind of framing a senior lawyer actually uses in preparation.

### Investigation Quality

The output finds things a checklist would not. The survival clause analysis (Section 5.6) goes beyond noting that ML rights survive — it frames the survival as conditionally RED, depending on whether the Section 1.6 negotiation succeeds. This is a judgment call, not a mechanical deviation flag. The reservation of rights section (Section 11) makes the same analytical move: it surfaces the "subject to Sections 1.5 and 1.6" qualification as the real issue, noting that Customer "retains all rights" to its content but those rights are "materially qualified by Provider's right to use that content for AI training purposes." That is a specific structural observation — the contractual language creates a nominal ownership right that is eroded by an adjacent clause.

The Feedback + ML interaction is identified explicitly: "Combined with the ML training clause, this creates a channel through which Customer's operational insights could flow to Provider's broader product and, by extension, to competitors." The security testing prohibition in Section 2.1(a)(v) is noted and redirected to the Order Form, which is the correct handling — it is an Order Form negotiation point, not a Standard Terms redline. The output also correctly identifies the distinction between Usage Data and Customer Content as the core line to draw in the ML negotiation, and it proposes fallback language that draws that line precisely.

What the output does not find: the double qualification in Section 1.6 (de-identification must be both "commercially reasonable" AND "consistent with industry standard technology" — a standard that shifts with industry practice AND requires Provider's own judgment), the undefined aggregation threshold, the absolute nature of the security testing restriction (no carveout even for Provider-coordinated testing), and the payment continuation obligation during suspension. These are not obvious items, but a deep investigator would surface them.

### Advice Quality

A senior lawyer would find this a strong starting point. The redlines are insertable — they are not concept drafts but actual alternative language with rationale and fallback positions. The ML training redline is precise: it draws the Customer Content / Usage Data distinction in operative language, restricts third-party model providers, and provides a detailed fallback that specifies an aggregation threshold (50 other customers), named de-identification standards (NIST SP 800-188, ISO/IEC 20889), and an opt-out mechanism. A junior associate could take this markup and send it. The data protection redline takes a similar approach, specifying the DPA requirements with enough detail that Provider cannot simply agree in principle and deliver a thin document.

The advice goes beyond "here are the issues and redlines" in the negotiation strategy. The concession matrix — concede logo rights and suspension notice period, trade termination for convenience, hold firm on ML training and DPA execution — is concrete and deal-calibrated. The recommended sequencing logic is sound: frame the ML and data protection asks together as compliance-driven rather than adversarial, because regulatory framing "is harder to resist than a pure commercial objection." This is the kind of tactical framing that makes a difference in practice. The next steps are specific and executable: request DPA and SOC 2 report immediately, send redlines within three days, target substantive agreement on Tier 1 items by end of week one, with a named escalation trigger if they are not resolved.

What a senior lawyer would still need to do: develop the Cover Page negotiating positions in more detail (the output provides minimum numbers but not the reasoning behind them), think through the combination exclusion in Section 9.5 more carefully (not addressed), and probe whether the warranty in Section 6.3 is meaningfully weaker than market standard (rated GREEN here, rated YELLOW with substantive analysis in one of the baseline comparison runs from the other model).

### Tone and Register

This reads like competent legal analysis prepared by a senior associate. The register is appropriate throughout — it is not academic or hedging, it states positions and explains them. The key findings section opens with a characterisation of the contract's overall posture ("structurally balanced but has three areas requiring serious attention before signing") rather than jumping directly into a list, which is the correct register for a memo to a decision-maker. The "Classification: RED — Escalate" labelling is used with restraint and judgment: the survival clause's classification is explicitly made conditional on the outcome of the Section 1.6 negotiation, which avoids the false precision of a categorical rating when the analysis actually calls for a contingent one.

The output does not read like a compliance checklist with headers. The transitions between clause analysis and commercial impact are smooth, and the negotiation strategy section does not feel stapled on — it reads as the logical extension of the clause analysis. The disclaimer language is appropriately placed and does not dominate. The one register weakness is occasional use of generic phrases that a senior lawyer would mentally edit out: "below market standard" and "this is standard SaaS practice" appear several times without adding precision. These are minor — they do not undermine the overall quality — but they are the verbal residue of a template-driven process showing through the analysis.

---

## Cross-Run Observations (from blind-evaluation.md, baseline-vs-optimised.md)

The blind comparison evaluated three optimised runs against three baseline runs. Observations about the optimised tier as a whole:

The optimised prompt produces genuine improvements over the baseline on compound risk identification and counterparty modelling. The feedback + ML interaction, the survival clause amplification, and the counterparty pushback analysis are consistently better across runs than in the baseline. The negotiation strategy sections model the other side of the table rather than listing priorities in the abstract.

However, the optimised runs show more variation than the baseline runs in structure, formatting, and which secondary issues receive treatment — some runs rate the warranty section GREEN, one rates it YELLOW with substantive redline analysis. This variation is in some respects healthy (it reflects genuine judgment rather than template execution) but also signals that some findings are unstable: the output discovers them on some passes and misses them on others, which is a reliability limitation.

The output stays within the same analytical ceiling as the baseline on depth and completeness. It does not surface the second-order structural observations — undefined aggregation threshold, doubly-qualified de-identification standard, suspension as functional termination bypass, the Cover Page deferral as a systematic risk-shifting mechanism — that would require a clean investigative pass unconstrained by evaluation categories. The improvement from baseline to optimised is real and meaningful for a practitioner; it is not transformative.

---

## Summary Assessment

The Tier 2 output would be genuinely useful to a senior lawyer preparing for this negotiation. It is better than the baseline in the ways that matter most in practice: it connects clauses into compound risks, it models the counterparty, it provides specific and executable fallbacks, and it produces advice that can be used rather than just read. A lawyer receiving this output would spend less time on preparation than one receiving the baseline.

The ceiling is visible. The output does not find what it is not looking for. Because investigation and evaluation share the same context, the analysis tends to confirm expected findings rather than surprise with unexpected ones. The structural gaps the pipeline surfaces — the accountability vacuum created by absent audit rights combined with absent breach notification combined with absent performance standards, or the suspension clause's functional equivalence to termination — are not present here. The output is competent and strategically aware; it is not the kind of analysis that makes you reconsider how you have been reading the contract.

For a $150K mid-market SaaS procurement with a two-week deadline, this is a workable starting point that would get most of the negotiation right.
