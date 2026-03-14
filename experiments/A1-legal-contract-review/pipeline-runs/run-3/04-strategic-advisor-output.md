# Strategic Advisor Output

**Important**: This analysis assists with legal workflows but does not constitute legal advice. All strategic recommendations should be reviewed by qualified legal professionals and business leadership.

## Deal Assessment

This is a $150K/year SaaS procurement for internal operations from a new vendor. The deal is important to daily business but not strategically significant -- it is a tool, not a partnership. That distinction should govern how much negotiating capital you spend and where you spend it.

The contract is built on a Common Paper v2.1 template, which is a publicly recognized standard for cloud service agreements. That choice tells you something about the counterparty: they are organized enough to adopt industry-standard forms, they have likely negotiated these terms with other buyers before, and their counsel will be fluent in the template's structure. It also tells you that the Provider is not trying to ambush you with a bespoke, maximally extractive agreement. The template is designed to be a fair starting point with customization handled through a Cover Page. What makes this contract Provider-favorable is not the template itself but what the Provider has put into Section 1.6 (broad ML training rights), what they have left out of the Standard Terms (security commitments, SLA, breach notification, data portability), and how much core risk allocation has been pushed to a Cover Page that you have not yet seen.

The balance of power is roughly even with a slight tilt toward the Provider. They have the product you want and your 2-week deadline creates mild time pressure. You have alternatives (this is not a sole-source situation for a standard SaaS tool), you are a new revenue opportunity the Provider wants to close, and the fact that implementation has not started means neither side has sunk costs. The most important dynamic is that your asks are standard market positions -- you are not requesting unusual concessions, you are requesting the provisions that a mature SaaS vendor should already have or be willing to provide. That reasonableness is your strongest form of leverage.

The tone of the negotiation should be collaborative and efficient. This is a contract that needs work, but it is not a hostile document. The Provider drafted a template, left some gaps, and pushed on data rights. Your job is to fill the gaps and push back on the data rights. Both sides should be able to get there in two weeks if neither side treats this as adversarial.

## Negotiation Priorities

The deviation list and redline proposals identify 24 items across escalate and negotiate classifications, with 11 marked must-have, 10 should-have, and 3 nice-to-have. That is too many fronts for a $150K deal with a 2-week window. The strategy below regroups them around what actually matters for this deal.

**Priority 1 -- Data sovereignty and post-termination cleanliness**

This is the defining issue of this contract and the area where the deal lives or dies. Three provisions interact to create a single compound problem: Section 1.6 grants broad ML training rights over Customer Content. Section 5.6 makes those rights survive termination. Section 5.5 provides no data export mechanism, only deletion on request. Together, they mean that once you put operational data into this platform, the Provider can train models on it forever and you have no way to get it back out in usable form when you leave.

This is not three separate negotiation items. It is one position: your data is yours, you can get it out, and when the relationship ends, the Provider's rights to derive value from it end too. Negotiate it as a package. The ML training redline (restrict to de-identified Usage Data for the subscribed service, no Customer Content, no third parties, no survival) and the data portability redline (30-day export period in standard formats, automatic deletion after) are two halves of the same ask.

This is also the area where the Provider will push back hardest. ML training on customer data is likely a core part of their product strategy. Expect them to frame it as essential to service quality and to resist eliminating it entirely. Your opening position should be the full restriction as drafted in the redlines. Your fallback should allow Usage Data only (not Customer Content), require outcome-based de-identification, limit scope to the subscribed service, prohibit third-party model training, and terminate the right at contract end. Do not fall back further than this.

**Priority 2 -- Security and data protection baseline**

The contract has a structural security gap: no security standards, no breach notification, no subprocessor controls, no security testing permitted, no alternative assurance mechanism. This is not a single missing clause -- it is a complete absence of security governance for a platform that will hold your operational data.

Your position here should be framed not as a negotiation but as a procurement prerequisite. You require baseline security commitments (encryption, access controls, annual third-party assessment), breach notification within 72 hours, and subprocessor transparency. These are not aspirational asks -- they are the minimum requirements for any SaaS platform processing business data at this investment level. Frame them that way. If the Provider does not have SOC 2 certification or an equivalent, that is a finding worth escalating to your own leadership before proceeding, because it raises questions about operational maturity that go beyond contract language.

The DPA requirement should be resolved before signing, not deferred. If the Provider has a standard DPA, execute it concurrently. If they do not, that is a red flag.

**Priority 3 -- Commercial protections (Cover Page)**

The liability cap structure, indemnification scope, and consequential damages formulation are all items that the Common Paper template intends to be negotiated via the Cover Page. This is where you should spend your effort on commercial terms:

- General Cap at 12-month fees (or $150K floor) is standard and defensible
- Increased Claims should include data protection breach and IP indemnification at 2x the General Cap
- Provider Covered Claims must include IP infringement indemnification at minimum
- The direct lost profits waiver needs to come out -- it eliminates your primary measure of damages for service failure

These are standard mid-market positions. The Provider's counsel will have seen these requests before and likely has pre-approved ranges to work within. Push firmly but do not make this the hill the deal dies on.

**Priority 4 -- Operational fairness**

Refund on material breach termination, suspension protections, warranty tied to documentation, and a capped auto-renewal notice period. These are reasonable, market-standard, and should not be heavily contested. The refund-on-material-breach point is particularly hard for a Provider to resist because it is a basic fairness argument: if you fail to deliver, you should not keep my money for the period you did not deliver.

The SLA is categorized as should-have in the redlines, and for this deal I would position it as a tradeable item. A 99.5% uptime commitment with service credits is standard, but if the Provider resists contractual SLA language, you can accept an operational commitment (Provider shares monthly uptime reports, commits to commercially reasonable availability) as a fallback. Save your capital for data and security.

**Priority 5 -- Cleanup and concession candidates**

IP ownership clarification, change-of-control notification, logo rights, security testing carveout, change management notification, insurance requirements, and disaster recovery commitments. These are all legitimate improvements, but for a $150K operational tool deal, several of them are concession material. Specifically:

- Logo rights: concede to the fallback (add a revocation right, drop the approval requirement)
- Insurance requirements: drop entirely unless your procurement policy mandates it
- Change management notification: accept the fallback (commercially reasonable efforts)
- Security testing: accept Provider-furnished reports rather than Customer-directed testing if the Provider pushes back

Hold the change-of-control notification and IP ownership clarification -- both are low-cost for the Provider and protect you meaningfully.

## Counterparty Analysis

**What the Provider cares about, based on their drafting choices:**

The ML training provision is the most revealing clause in the contract. It is specific, detailed, and deliberately broad -- covering Customer Content and Usage Data, extending to third-party model components, using an effort-based rather than outcome-based de-identification standard, and surviving termination. This was not boilerplate left in by accident. The Provider's product strategy almost certainly depends on training models with customer data. This is the point where they have the most at stake and will push back hardest.

The absence of security commitments, SLA, and breach notification may reflect a different dynamic. It could be deliberate (the Provider does not want to be contractually bound to specific standards) but it could also be a maturity gap (the Provider has not yet formalized these practices or obtained certifications). The Provider's response to your security asks will tell you which it is. If they readily agree to SOC 2 certification language because they already have it, the omission was a drafting choice. If they resist because they do not have certifications, you have a deeper diligence question.

The heavy deferral to Cover Page variables is a Common Paper design feature, not necessarily Provider strategy. But the Provider benefits from it -- if they control the Cover Page draft, they can set favorable caps and narrow indemnification scope without it looking like they changed the Standard Terms. Ask for the Cover Page early. Do not negotiate Standard Terms in a vacuum.

**Where they will push back:**

1. ML training rights -- this is existential for their product roadmap. Expect their first response to be "we cannot remove this." Your response should be to distinguish Customer Content from Usage Data and to show that the redline permits Usage Data use for service improvement. That gives them most of what they need for product development while protecting your operational data.

2. SLA commitments -- if they have not operationalized SLA tracking, committing to specific percentages and credit mechanisms creates new operational burden. They may offer a "best efforts" alternative.

3. Security certifications -- if they do not have SOC 2 yet, they will resist language that requires it. They may offer a timeline to achieve certification.

**Where they will likely concede:**

- Refund on material breach termination -- indefensible to resist
- Data export on termination -- they likely have export functionality already
- Suspension notice -- low-cost concession, reasonable ask
- Auto-renewal notice period -- 60 days is standard
- Breach notification -- increasingly viewed as table stakes; resistance here is a red flag
- IP ownership clarification -- this is a drafting change, not a substantive concession
- DPA scope broadening beyond GDPR-only -- most vendors have already expanded their DPAs

**Leverage points you hold:**

- You are a new customer who has not signed yet. The Provider has sales targets and pipeline commitments. Walking away costs them revenue they have likely already forecasted.
- Your asks are market-standard. If the Provider's counsel pushes back on breach notification or data export, they are defending a position they would lose in any benchmarking exercise. You can reference Common Paper guidance, peer contracts, and regulatory trends.
- You have not started implementation. There are no sunk costs creating switching inertia.
- The 2-week deadline is bilateral. If the Provider wants to close this deal this month or this quarter, delay costs them too.

**Leverage the Provider holds:**

- They have the product you selected. Switching to an alternative means restarting vendor evaluation.
- The deal is not large enough for you to command bespoke terms -- you are a mid-market buyer, not an enterprise anchor customer.
- If you have already communicated internally that this tool is needed, your internal stakeholders create pressure to close.

## Recommended Approach

**Send the full markup on Day 1, organized by theme, not by section number.** Do not drip-feed changes across multiple rounds. Give Provider's counsel the complete picture immediately. Organize the markup into three sections:

*Section A: Data Governance.* The ML training restriction, data portability, DPA requirement, subprocessor controls, breach notification, and security commitments. Frame this as a single coherent topic: "Here is what we need for our data governance and security requirements." This framing makes it harder for the Provider to pick items off one by one because they are presented as an integrated set of requirements, not a list of objections.

*Section B: Commercial Terms.* The Cover Page proposals (liability caps, indemnification scope, Increased/Unlimited Claims designations), the consequential damages revision, refund on material breach, and the auto-renewal notice period. Frame this as "standard commercial terms for a deal at this level."

*Section C: Operational and Administrative.* The suspension protections, warranty revision, SLA, IP ownership clarification, change-of-control notification, logo rights, and any remaining items. Frame this as "operational provisions for a production deployment."

**Negotiate Section A first and hardest.** This is where your business priorities (data protection and IP ownership) align with your strongest negotiating position (market-standard asks). If you secure this section, the deal is sound even if you make concessions elsewhere.

**On the ML training negotiation specifically:** Expect a multi-step conversation. The Provider's opening response will likely be to defend the current language. Your second move should be to separate Customer Content from Usage Data explicitly -- "We understand you want to use platform usage patterns to improve the service. That is reasonable. What we cannot accept is training models on the content we store in your platform." This reframes the negotiation from "we want to take something away from you" to "let us find the line between what is reasonable and what is not." If they accept the Customer Content / Usage Data distinction but resist the other restrictions (third-party training, survival, scope), work through them sequentially. Your final line is: no Customer Content for ML, de-identified Usage Data only, limited to the subscribed service, no third-party models, no survival post-termination.

**What to trade and for what:** Your Section C items are your concession currency. If you need to make a trade to close the ML training or security discussion, offer these in roughly this order:

1. Drop insurance requirements entirely
2. Accept commercially reasonable efforts for change notification instead of specific timelines
3. Accept Provider-furnished security assessment reports instead of Customer-directed penetration testing
4. Accept the fallback logo rights (revocation right only, no approval requirement)
5. Accept a softer SLA (operational commitment rather than contractual credits)

Do not trade data portability, breach notification, or the ML training restrictions. Those are structural protections, not negotiation tokens.

**Handle the Cover Page concurrently.** Request the Provider's proposed Cover Page values on Day 1 alongside your markup. Do not negotiate the Standard Terms in isolation from the Cover Page -- several items (liability caps, indemnification scope, auto-renewal notice, prohibited data categories) are only meaningful once you see the Cover Page values. If the Provider does not produce a Cover Page draft promptly, include your proposed values in your markup so you are negotiating from your numbers, not theirs.

**Escalation path for the ML training discussion:** If the legal teams reach impasse on Section 1.6 by Day 8, escalate to a business-level conversation. The question for business leads is: "Can we agree that customer operational data should not be used for model training, while usage telemetry can be used to improve the service?" Most business leaders will agree on this principle even when their lawyers are stuck on the drafting. Once the principle is agreed, the lawyers can draft to it.

## Timeline Considerations

The 2-week deadline is tight but achievable for a deal of this complexity. The critical path runs through the data governance discussion -- specifically the ML training rights. Everything else can be resolved in parallel.

**Day 1:** Send the complete markup with all three sections. Request the Cover Page simultaneously. Internal preparation: brief your own leadership on the ML training issue so they are ready for an escalation call if needed around Day 8-10.

**Days 2-5:** Provider counsel reviews. Expect initial responses on Section B (commercial terms) and Section C (operational items) first, because those involve familiar positions with established fallback ranges. Section A (data governance) will likely require the Provider to consult internally -- their product team will need to weigh in on ML training, their security team on commitments.

**Days 5-8:** Active negotiation on open items. The Section B and C items should be resolvable in this window. Section A will likely still be in discussion. If the Provider comes back with a blanket rejection of the ML training changes, do not accept "we need this for product improvement" without probing -- ask specifically what they use Customer Content (not Usage Data) for, and whether they can commit to the Customer Content / Usage Data distinction even if other aspects of 1.6 remain under discussion.

**Days 8-11:** Resolve remaining Section A items. If the ML training discussion is stuck, escalate to business leads. In parallel, finalize Section B (Cover Page values should be agreed by now) and Section C (concede remaining nice-to-haves as needed to maintain goodwill and momentum).

**Days 12-14:** Final language review, internal approvals, execution.

**Risk to timeline:** The ML training provision is the single largest risk to closing on time. If the Provider's product strategy genuinely depends on using Customer Content (not just Usage Data) for model training, resolving this will take longer than two weeks. In that case, consider a phased approach: execute the agreement with an amended Section 1.6 that restricts ML training to de-identified Usage Data for the subscribed service, with an agreement to negotiate expanded ML provisions (if any) in a separately executed addendum within 90 days. This lets you go live on time while deferring the most contentious substantive question. Do not, however, sign the agreement with the current Section 1.6 language intact under any circumstances -- the risk of perpetual, broad ML training rights over your operational data is not a risk that time pressure should force you to accept.

**If the Provider is unresponsive or slow:** Follow up on Day 5 if you have not received a substantive response. Remind them that the deadline serves both sides. If by Day 10 you do not have agreement on the data governance essentials (ML training, breach notification, data portability), you need to make a business decision about whether to extend the timeline, accept more risk than you would prefer, or walk away. For a non-strategic vendor at $150K/year, walking away should be a real option, not a bluff.
