---

**INSTITUTIONAL ADVISORY REPORT**

# Liquidity and Trading Efficiency Across Three Market Structure Eras: Assessment and Execution Framework for Institutional Investors

---

## I. Executive Summary

This report assesses the evolution of U.S. equity market liquidity and trading efficiency across three structural eras — pre-Reg NMS, the Reg NMS / high-frequency trading (HFT) era, and the current fragmented landscape — and provides a recommended execution framework for institutional portfolio managers operating in today's environment.

The central finding is this: the conventional narrative of continuous improvement — spreads have narrowed, competition has increased, technology has advanced — is accurate on its narrowest terms but misleading as a guide to institutional decision-making. Headline spread compression is real. Whether it translates into lower total execution costs for institutional-scale orders is a different question, and one that current data cannot definitively answer.

Rather than presenting false confidence in a single narrative, this report organizes its conclusions by the degree of certainty behind them. Some things are clear. Some can be managed through professional judgment. Some are genuinely unresolved, and that uncertainty itself has implications for how you structure your execution strategy.

---

## II. What Is Clear

**Reg NMS re-engineered market structure in ways the original rulemaking did not anticipate.** The Order Protection Rule (Rule 611) was designed to prevent trade-throughs and protect displayed quotations. In practice, by guaranteeing quote protection across venues, it legitimized new exchange entrants and made fragmentation self-reinforcing. The Access Rule (Rule 610) lowered barriers to entry while capping access fees at $0.003 per share — a ceiling that simultaneously became the foundation of the maker-taker rebate economy. These rules were intended as transparency and competition tools. They functioned as market structure re-engineering tools. You are operating in an environment created by rules that were not designed with this environment in mind.

**The regulatory framework systematically favors off-exchange execution on key dimensions, and this is by design, not oversight.** The Sub-Penny Rule (Rule 612) prohibits *displaying* sub-penny quotations but does not prohibit *executing* at sub-penny prices. This means dark pools and wholesalers can offer nominal price improvement — a tenth of a cent better than the National Best Bid and Offer — that lit exchanges structurally cannot match. Regulation ATS allows dark pools to operate under lighter obligations than exchanges: no self-regulatory organization duties, no universal access requirements below a 5% volume threshold. These are not loopholes. They are the deliberate consequences of applying different regulatory regimes to different venue types. Your routing decisions between lit and dark venues are not choices within a level playing field. They are choices between venues operating under different rules with different economics.

**Effective bid-ask spreads have narrowed across all three periods.** This is the most frequently cited metric of market quality improvement, and the underlying data is robust. Spreads have compressed, and competitive quoting by algorithmic market makers is a principal driver.

**Displayed depth at the NBBO has declined.** Top-of-book quoted sizes are smaller and update more frequently than in the pre-HFT era. This is the less-cited counterpart to spread narrowing: the quotes are tighter, but there is less size behind them.

**Off-exchange volume has grown to approximately 40-45% of consolidated equity trading.** This includes dark pools (roughly 15-20%) and wholesaler internalization. This is not a marginal phenomenon; it is the structural center of the market.

**The regulatory environment is in active flux.** The SEC's 2022-2023 proposals — the Order Competition Rule, tick size reform, access fee amendments, and Regulation Best Execution — would, if adopted in anything close to their proposed form, materially alter maker-taker economics, the role of wholesalers, and the routing incentives analyzed here.

---

## III. What Requires Judgment

The following conclusions involve genuine analytical uncertainty but are navigable with informed professional judgment.

**Spread narrowing probably reflects genuine execution quality improvement for smaller institutional orders, but the case is weaker for large orders.** For orders that can be completed within displayed depth, tighter spreads are unambiguously beneficial. For orders that require sustained execution over hours or days — the characteristic institutional problem — market impact, information leakage, and opportunity cost dominate the cost picture, and these are not captured by spread metrics. The most honest statement is: the market has become cheaper for small trades and more complex for large ones.

**Dark pools are neither categorically good nor categorically bad for institutional execution — but they are categorically heterogeneous.** The differences between dark pools in counterparty composition, anti-gaming protections, and operator conflicts of interest are at least as large as the differences between dark and lit venues. A dark pool dominated by institutional natural flow is a fundamentally different execution venue from one that permits high-frequency market-making activity. Regulation ATS permits this heterogeneity rather than standardizing it, which means venue selection is a consequential analytical decision, not a category-level one. Generalizations about "dark pools" are unreliable. Venue-specific analysis is essential.

**Maker-taker rebates create a structural conflict between broker economics and client execution quality.** The theoretical conflict is unambiguous: brokers have a financial incentive to route orders to venues paying the highest rebate, which may not be the venue offering the best execution. Whether this conflict produces measurable harm in practice is debatable — the SEC's Transaction Fee Pilot, designed to generate exactly this data, was struck down by the D.C. Circuit in 2020. The empirical gap persists. Your practical response should be to monitor this through independent Transaction Cost Analysis (TCA) and to use directed routing where it is available and appropriate.

**The SEC's pending proposals should be treated as scenario risk, not forecasts.** Assign probabilities if you wish, but do not structure your execution framework on the assumption that they will or will not be adopted. The appropriate response is to understand your exposure under multiple scenarios and ensure your framework is adaptable.

---

## IV. What Is Genuinely Unresolved

These are not hedges or caveats. They are substantive unknowns that affect your risk exposure, and you should understand them as such.

**Whether total execution costs for institutional investors have improved or deteriorated on a like-for-like basis across the three eras cannot be determined with available data.** The measurement challenges are not merely technical inconveniences — they are fundamental. Tick size changes (decimalization in 2001), the shifting boundary between visible and hidden liquidity, odd-lot exclusion from the NBBO, and the growth of ETF-related volume that inflates aggregate statistics all mean that period-to-period metric comparisons do not measure the same thing. Any cross-period comparison you encounter in the literature or from brokers carries irreducible measurement uncertainty. Treat point estimates with skepticism. Prefer ranges and directional conclusions over precise figures.

**Whether HFT is net beneficial or net harmful for institutional investors is the central contested question in market structure, and no reliable decomposition exists.** HFT market making — providing liquidity through continuous quoting — is beneficial and reduces spreads. HFT latency arbitrage — exploiting the finite speed of quote propagation across venues, enabled by the Order Protection Rule's mandatory routing requirements — is a tax on slower participants. These activities coexist within the same firms and sometimes within the same strategies. The net effect depends on the decomposition, and no regulatory definition or empirical methodology reliably separates them. The Order Protection Rule functions in a high-speed environment as a mechanism that transfers value from slower to faster participants. This is a structural feature, not a bug to be fixed incrementally.

**Whether the current market structure is resilient to a flash-crash-magnitude stress event is untested.** Post-2010 safeguards — Limit Up-Limit Down (LULD) bands, market-wide circuit breakers, Rule 15c3-5 risk controls — address the specific failure modes observed in that event. Whether they are sufficient for a different kind of dislocation is unknown. The March 2020 experience provides partial evidence of resilience but is confounded by unprecedented fiscal and monetary intervention. HFT liquidity is voluntary and conditional; it can be withdrawn unilaterally. The "normal times" liquidity that HFT provides is real, but it is not committed liquidity in the sense that designated market maker obligations create.

**Whether off-exchange execution has exceeded the level at which its benefits to individual participants outweigh its costs to price discovery is a normative question that no analytical framework currently answers.** There is a coherent argument that individual institutional investors rationally use dark pools even if the aggregate effect of that usage degrades the lit market on which the dark pool's reference prices depend. This is a classic tragedy-of-the-commons structure. It is relevant to your long-term interests even if it does not affect your next trade.

---

## V. Measurement Methodology: What You Need to Know

Any report comparing execution quality across market eras must confront the fact that the choice of measurement methodology is not neutral — it determines the conclusion. You should insist on the following from any analysis you commission or consume:

- **Implementation shortfall analysis** (measuring against arrival price) is the most common institutional benchmark, but the arrival price itself is affected by the market structure under analysis. In a market where your order's information leakage begins before you finish routing, the benchmark is contaminated by the thing you are measuring.

- **VWAP analysis** is inflated by ETF arbitrage volume and high-frequency activity that adds to consolidated volume without reflecting investable liquidity for your purposes.

- **Effective spread decomposition** into realized spread and price impact is the most analytically rigorous approach but requires trade-level data that may not be available for historical periods.

- **Market data costs** — consolidated feeds, proprietary exchange feeds, depth-of-book data — have risen substantially and must be included in any total execution cost analysis. An analysis that excludes data infrastructure costs understates the total cost of operating in the current environment relative to the pre-Reg NMS era.

Present results under multiple methodologies. Be transparent about where they diverge. Distrust any analysis that presents a single metric as dispositive.

---

## VI. Supplemental Considerations

**Exchange ownership concentration is under-recognized.** Although the number of exchange licenses has grown to sixteen, ownership has consolidated: ICE owns NYSE and its affiliates, Nasdaq owns multiple venues, and Cboe owns four exchanges. Fee competition, order type innovation, and data pricing operate within an oligopolistic ownership structure. "Competition among sixteen exchanges" overstates the competitive intensity you are actually benefiting from.

**The retail/institutional distinction matters for interpreting every aggregate metric.** Retail order flow routes disproportionately to wholesalers; institutional flow splits across lit exchanges, dark pools, and algorithmic strategies. Aggregate statistics blend these populations. Any analysis you review that cites average spreads, average fill rates, or volume share without decomposing by order type and investor category is drawing conclusions about your execution quality from data that includes a substantial proportion of orders that look nothing like yours.

**Counterparty risk in dark pool execution is analytically distinct from exchange execution.** Exchange-traded orders are centrally cleared through NSCC/DTCC. Dark pool trades may involve bilateral counterparty exposure before clearing. For large positions, this is a non-trivial difference that belongs in your risk management framework, not just your execution quality analysis.

**The T+1 settlement transition** reduces counterparty risk but increases operational demands and may reduce securities lending liquidity. This is a structural change within the current era and should be factored into any forward-looking liquidity assessment.

---

## VII. Recommended Execution Framework

Given the analysis above, the following framework is designed to be robust across the known uncertainties and adaptable to a shifting regulatory landscape.

### A. Venue Selection and Routing Governance

1. **Conduct venue-specific dark pool analysis, not category-level assessment.** Evaluate each dark pool individually on counterparty composition, anti-gaming protections, operator conflicts of interest, and fill quality for your order profile. The regulatory framework (Reg ATS, Fair Access Rule thresholds) permits wide variation. Exploit the venues that serve your interests; avoid the ones that do not.

2. **Implement directed routing capability where feasible.** Do not rely solely on broker smart order routers, whose optimization functions may weight rebate capture alongside execution quality. Directed routing gives you control over venue selection for orders where venue choice materially affects outcome.

3. **Require broker disclosure beyond Rule 606 minimums.** Amended Rule 606 disclosures are aggregated and may not reveal order-by-order routing rationale. Negotiate for more granular reporting — by strategy, by order size bucket, by venue — as a condition of your brokerage relationships.

### B. Execution Cost Measurement

4. **Deploy independent TCA that decomposes execution cost into its full components.** Effective spread, market impact, information leakage, opportunity cost from unfilled orders, and explicit costs including data fees and access charges. Do not accept TCA that reports only spread-based metrics. Ensure the TCA provider is independent of your executing brokers.

5. **Benchmark against multiple methodologies.** Use implementation shortfall, VWAP, and effective spread decomposition in parallel. Where the methodologies produce different conclusions for the same period or the same order set, investigate the divergence — it is telling you something about which costs are visible and which are hidden.

6. **Include market data costs in total cost of execution.** Data infrastructure has become a material line item. Exclude it, and you are understating the cost of operating in the current structure.

### C. Maker-Taker Conflict Management

7. **Monitor the relationship between broker routing patterns and rebate economics.** Cross-reference Rule 606 data with venue fee schedules to identify whether rebate-maximizing venues are disproportionately represented in your broker's routing. This does not prove a conflict, but it identifies where to ask questions.

8. **Consider all-in cost analysis that includes rebate-adjusted fees.** If your broker is capturing rebates on your flow, that is economically equivalent to a cost to you — the rebate could alternatively be passed through. Understand the economic structure, even if you ultimately accept it.

### D. Regulatory Risk Management

9. **Map your execution framework's exposure to each pending SEC proposal.** The Order Competition Rule would affect wholesaler routing of smaller orders. Tick size reform would change spread dynamics and rebate economics for sub-dollar-spread stocks. Access fee reduction would compress the maker-taker incentive structure. Regulation Best Execution would formalize and potentially raise the standard your brokers must meet. For each proposal, identify what changes in your framework if the rule is adopted, adopted in modified form, or withdrawn.

10. **Build adaptability into your execution infrastructure.** The regulatory trajectory is genuinely unknowable. The execution framework that serves you best is one that can adjust to multiple outcomes, not one optimized for a single predicted state of the world.

### E. Stress Resilience

11. **Maintain execution capability across venue types, including lit markets, during periods when dark pool liquidity may be unavailable or unreliable.** Voluntary liquidity sources — including HFT market makers and dark pool operators — may withdraw during stress events. Your execution framework should not be dependent on any single venue category.

12. **Understand your exposure to liquidity withdrawal scenarios.** Review the counterparty composition of your primary dark pool venues and the conditions under which those counterparties might reduce their activity. Stress-test your execution assumptions against a scenario where off-exchange liquidity contracts rapidly.

### F. Priority Sequencing

If you are building or revising your execution framework, the highest-impact actions in order of priority are:

1. Independent TCA deployment (this is the foundation; without it, you cannot evaluate anything else)
2. Venue-specific dark pool analysis and selection
3. Broker routing governance and rebate transparency
4. Regulatory scenario mapping
5. Stress resilience review

Items 1 and 2 produce immediate, measurable improvements in execution oversight. Items 3 and 4 are structural governance measures that protect against conflicts and forward risk. Item 5 is insurance against tail events.

---

## VIII. Conclusion

The U.S. equity market structure has changed fundamentally across the three eras under analysis. Spreads are tighter. Liquidity is more fragmented, more conditional, and more hidden. The regulatory framework creates asymmetries that favor off-exchange execution and creates economic incentives — particularly through the maker-taker model — that may not align with your interests. The measurement infrastructure you rely on to evaluate execution quality is itself affected by the structural changes you are trying to measure.

The honest conclusion is not that the market is better or worse for institutional investors. It is that the market is more complex, that the complexity creates both opportunities and risks, and that the institutional investors who will fare best are those who invest in understanding the structure they are operating within — rather than accepting headline metrics at face value.

The execution framework above is designed around that principle. It prioritizes independent measurement, venue-level analysis, conflict monitoring, and regulatory adaptability. It accepts the uncertainties identified in this report as features of the landscape to be managed, not problems to be solved in a footnote.

We are available to discuss any element of this analysis and to assist in implementing the recommended framework.