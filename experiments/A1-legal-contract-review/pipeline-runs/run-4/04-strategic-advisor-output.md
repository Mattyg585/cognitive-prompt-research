**Important**: This document assists with legal workflows but does not constitute legal advice. All strategic guidance should be reviewed by qualified legal professionals before use in negotiations.

# Negotiation Strategy — Common Paper CSA v2.1

**Deal**: $150K/year SaaS platform for internal operations. New vendor relationship. Customer side. Two-week deadline. Data protection and IP ownership are stated priority areas.

---

## Deal Assessment

This is a mid-market SaaS procurement with an unusual risk profile. The deal size is modest — $150K/year does not command the leverage of a seven-figure enterprise agreement — but the contract was drafted with a distinctly Provider-favourable tilt that goes beyond what the deal size would normally warrant. This is not a contract written for a specific counterparty; it is a framework document (Common Paper standard terms) designed to be Provider-friendly by default, with the expectation that enterprise customers will negotiate it back toward centre.

That framing matters. The counterparty is not being aggressive — they are using a template that starts from their preferred position. This means pushback on standard enterprise protections should not be read as adversarial. It is the expected dynamic. The contract is a starting position, not a statement of intent to hold every line.

The pattern of drafting choices tells a clear story: the Provider has prioritised operational flexibility and liability containment above all else. Broad ML training rights, unilateral suspension power, blanket prohibition on security testing, waiver of direct lost profits, zero security commitments in the standard terms, no transition assistance — these are not the marks of a predatory contract. They are the marks of a Provider that drafted for maximum flexibility and minimum obligation, expecting negotiation to fill in the protections. The Cover Page dependency reinforces this: the standard terms are deliberately skeletal, with the real commercial terms meant to be specified per deal.

The negotiation landscape is moderately favourable. The two-week deadline creates some time pressure, but this is a new vendor for an internal operations platform — not a strategic partnership — which means there is a credible walk-away alternative. The Customer is not locked into this vendor. That said, the Customer presumably selected this vendor for operational reasons, so switching costs are real even at the procurement stage. The balance of leverage is roughly even: the Provider wants the deal (mid-market revenue), but the Customer needs the platform (selected for operational fit).

The tone should be efficient and professional. This is not a deal that justifies protracted negotiation. The goal is to move the contract from Provider-default to reasonable enterprise standard within two weeks, focusing effort on the items that matter most for the Customer's stated priorities.

---

## Negotiation Priorities

The deviation analysis surfaced five Escalate items and nine Negotiate items. But strategic importance does not track classification tiers mechanically. Here is what actually matters for this deal, reordered by negotiation priority.

**Tier 1 — Non-negotiable for this deal:**

1. **ML training rights over Customer Content (Section 1.6).** This is the single most important item. It sits at the intersection of both stated priority areas — data protection and IP ownership. Allowing Customer Content to train third-party models, with effort-based de-identification and perpetual survival, is a material data and IP risk. The proposed redline — removing Customer Content from training entirely, restricting to Provider's own models, requiring outcome-based de-identification, and ending rights at termination — is the right position. This is where the Customer should be firmest. The business needs to decide whether even Usage Data training is acceptable, but Customer Content training is a clear no.

2. **Security commitments (new Section 3.3) and security testing (Section 2.1(a)(v)).** These two items are a single negotiation unit. The contract currently offers zero security commitments and prohibits the Customer from verifying security independently. For an operational platform handling business data, this is a structural gap. SOC 2 certification, encryption standards, breach notification within 72 hours, and sub-processor controls are baseline enterprise expectations. The security testing carve-out is the fallback if Provider resists direct audit rights — at minimum, Customer needs one mechanism to verify security posture. Bundle these together.

3. **DPA scope expansion (Section 3.1).** The GDPR-only DPA requirement leaves non-GDPR personal data unprotected. This is a straightforward ask — expand the DPA requirement to all personal data under applicable data protection laws. Provider should accept this readily because it aligns with their own compliance obligations. If they resist, it raises questions about their data handling practices that would warrant further diligence.

**Tier 2 — Important, worth spending capital on:**

4. **Suspension protections (Section 2.2).** The compound risk of unilateral suspension plus continued fees plus no dispute process is real, but it is an operational risk rather than a data/IP risk. The full redline — notice, cure period, time limit, fee relief, dispute mechanism — is comprehensive. In negotiation, lead with notice and cure (which are easy to concede) and use fee relief during suspension as the critical protection. The 30-day termination trigger if suspension continues is the most important safeguard; it prevents indefinite suspension as a de facto lock-in.

5. **Direct lost profits waiver (Section 8.2).** This matters because it interacts with liability caps to severely constrain Customer's remedies. The proposed position — preserve direct lost profits while maintaining the mutual consequential damages exclusion — is market standard. Provider pushback here is likely, because damages provisions are where legal teams tend to dig in. But the position is defensible: the liability cap still bounds total exposure, so this is about preserving the right category of recovery, not creating unlimited risk for Provider.

6. **Transition assistance (Section 5.5).** For an operational platform, the ability to export data in a usable format is essential. This is a practical lock-in concern more than a legal one. The 60-day transition window with machine-readable export is reasonable. If Provider resists the full proposal, the fallback — a data export in CSV/JSON within 30 days — is the minimum acceptable position.

**Tier 3 — Standard asks, do not spend significant capital:**

7. **Warranty expansion (Sections 6.3/6.4).** Documentation conformance and shortened timelines are standard but unlikely to be deal-breakers on either side. Use the fallback readily: keep existing scope but get 30+30 day timelines and fee credits.

8. **Convenience termination (Section 5.1/new 5.3(c)).** Worth asking for as a new vendor relationship, but this is where Provider will likely push back hardest among the Negotiate items — convenience termination directly threatens their revenue predictability. Be prepared to accept the fallback (month-to-month after initial term).

9. **Change of control termination right (Section 12.6).** Standard ask. Provider should accept the notification requirement easily. The termination right may get pushback, but the fallback (limited to competitor acquisitions) is reasonable.

10. **Customer Content scope — remove "related offerings" (Section 1.5).** Simple deletion. Should be uncontroversial.

11. **Feedback rights (Section 1.4), logo rights (Section 12.8).** Standard clean-up items. Raise them, but do not spend negotiation capital here. Accept fallbacks readily.

---

## Counterparty Analysis

The Provider's drafting choices reveal a company that values operational flexibility and liability limitation above relationship-building. The ML training clause is the most revealing: extending training rights to third-party models, with effort-based de-identification, suggests a Provider that either uses Customer data as a product input (for ML capabilities) or has drafted aspirationally for future business models. Either way, they care about retaining broad data use rights.

The absence of security commitments is likely a template choice rather than a reflection of actual security posture. Most mid-market SaaS providers have SOC 2 certification; they simply do not put it in their standard terms because it creates a contractual obligation they would rather handle operationally. Expect the Provider to agree to security commitments relatively easily, possibly by pointing to existing certifications. If they resist, that is a red flag worth investigating before signing.

**Where the Provider will push back:**

- **ML training rights.** This is likely their highest-priority retention item. If their product roadmap depends on training models with customer data, they will resist removing Customer Content from training scope. The compromise space is around guardrails (no third-party models, outcome-based de-identification, no survival) rather than a complete prohibition. But if Customer Content training is truly off the table for the Customer, hold firm — Usage Data with proper guardrails gives them what they need for product improvement.

- **Direct lost profits.** Legal teams on both sides will have strong views. The Provider will argue that the liability cap is sufficient protection. The Customer's position is that the cap bounds quantum but the waiver eliminates the category. Expect this to be one of the last items resolved.

- **Convenience termination.** Directly affects revenue predictability. The Provider will push back on a full convenience termination right. The fallback (month-to-month after initial term) is where this likely lands.

**Where the Provider has room:**

- **Security commitments.** If they already have SOC 2, adding it to the contract costs them nothing. Breach notification timelines may get negotiated (72 hours to "without unreasonable delay"), but the principle should be easy.

- **DPA scope expansion.** Aligns with Provider's own compliance obligations. Low resistance expected.

- **Suspension process.** Notice and cure requirements are standard. Provider may resist fee suspension during suspension periods, but the 30-day termination trigger should be achievable.

- **Logo rights, feedback, "related offerings."** Standard clean-up items where Provider has no material interest in the current language. Easy concessions that build goodwill.

**What the Provider would trade:** The Provider would likely accept security commitments, DPA expansion, suspension process improvements, and several Negotiate items in exchange for retaining some form of ML training rights (even if narrowed) and the current damages structure (or a compromise on the lost profits waiver). The Provider's real priorities are data use flexibility and liability containment. Everything else is negotiable.

---

## Recommended Approach

**Lead with the easy wins.** Open the negotiation with the items where agreement is most likely: DPA scope expansion, security commitments (if they have SOC 2), removal of "related offerings" from Section 1.5, logo consent, and feedback tightening. Resolving five or six items early establishes momentum and a collaborative tone. It also demonstrates that the Customer's redlines are reasonable and market-standard, which sets the frame for the harder conversations.

**Package the data protection cluster.** ML training, security commitments, DPA expansion, and security testing are interconnected. Present them as a unified data protection position rather than four separate asks. The framing: "We need a coherent data protection framework — we are comfortable with your platform, but we need standard protections around how our data is handled, secured, and used." This makes it harder for the Provider to concede on DPA scope while resisting on ML training, because the Customer's position is principled rather than item-by-item.

**Hold firm on ML training and security.** These are the must-holds. Customer Content must not be used for ML training — full stop. Security commitments must be in the agreement. If Provider resists both, the Customer should be prepared to walk, because a Provider that will not commit to basic security standards or limit data use for a $150K deal is signalling something about how they operate.

**Be flexible on damages and commercial terms.** The direct lost profits waiver is important but tradeable. If Provider will not move on lost profits, explore alternatives: a higher liability cap, specific carve-outs for data breaches or confidentiality violations (which are common even in contracts that waive consequential damages), or an uncapped category for wilful misconduct. The goal is adequate remedies for serious failures, not a specific drafting formulation.

**Use the convenience termination ask strategically.** This is a concession chip. Ask for it, argue for it (new vendor, need flexibility), but be prepared to give it up in exchange for something the Customer cares about more — like holding firm on ML training or getting better suspension protections. The fallback (month-to-month after initial term) is acceptable and probably where this lands.

**Handle Escalate items with clarity.** For items flagged for senior counsel — particularly the ML training position and the damages structure — bring a recommendation to the senior discussion, not an open question. The recommendation: no Customer Content for ML training, Usage Data is acceptable with guardrails; preserve direct lost profits if possible, accept higher cap or carve-outs as alternative. Senior counsel can override, but having a clear recommendation speeds the process.

**Sequence the negotiation:**

1. **Round 1 (Days 1-3):** Send the full redline. Group items by theme (data protection, commercial terms, operational protections) rather than by severity. Include a cover note framing the changes as bringing the agreement to enterprise standard.

2. **Round 2 (Days 4-7):** Review Provider's response. Expect acceptance on easy items, pushback on ML training and damages, and mixed responses on operational items. Resolve the easy items and narrow the open list.

3. **Round 3 (Days 8-11):** Negotiate the remaining items. This is where package deals happen. Trade convenience termination for ML training firmness. Explore damages alternatives if the lost profits position is stuck.

4. **Close (Days 12-14):** Final language review. Ensure the Cover Page variables are confirmed — liability caps, non-renewal notice period, subscription period length, and any additional warranties. The Cover Page is where the remaining commercial risk lives.

---

## Timeline Considerations

The two-week deadline is tight but workable for this deal. The contract is template-based (Common Paper standard terms), which means Provider's legal team should be familiar with the redline points — these are the same issues every enterprise customer raises. This is not a bespoke contract requiring novel drafting.

The main timeline risk is internal, not external. The Escalate items — ML training position and damages structure — require senior counsel or business-level decisions before the Customer can finalise its position. If those decisions are delayed, the negotiation timeline compresses. Get the escalation conversations scheduled in the first two days, so the Customer's full position is firm before Round 2.

If time pressure intensifies, prioritise ruthlessly. The data protection cluster (ML training, security commitments, DPA scope) is non-negotiable. Suspension protections and transition assistance are important but can be simplified (accept shorter cure periods or narrower scope to close faster). Everything in Tier 3 can be resolved with fallback positions in a single exchange.

Do not let the deadline push the Customer into accepting the contract without security commitments or with unrestricted ML training rights. Those are risks that outlast any deadline pressure. If the Provider cannot agree to baseline data protection within two weeks, the Customer should consider whether this is the right vendor — a Provider that resists standard protections at the contracting stage is unlikely to be more accommodating during the relationship.
