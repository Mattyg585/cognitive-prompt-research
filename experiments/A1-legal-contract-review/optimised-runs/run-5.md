## Contract Review Summary

**Document**: Common Paper Cloud Service Agreement -- Standard Terms Version 2.1
**Parties**: Provider (unnamed SaaS vendor) and Customer (our organization)
**Your Side**: Customer (buyer)
**Deadline**: 2 weeks
**Review Basis**: Generic review using widely-accepted commercial standards (no organizational playbook available)

> **Note**: No organizational playbook (`legal.local.md` or equivalent) was found. This review uses widely-accepted commercial standards for enterprise SaaS procurement as the baseline. All analysis should be reviewed by qualified legal counsel before being relied upon for legal decisions.

---

## Working Theory of the Contract

Before evaluating against any standard, here is what this contract is actually doing.

This is a framework agreement for cloud-hosted software. The Provider supplies a SaaS platform; the Customer pays subscription fees and gets access for internal use. The commercial structure is subscription-based with auto-renewal -- revenue predictability for the Provider, operational continuity for the Customer, with lock-in as the trade-off for both sides.

Risk flows primarily to the Customer. The Provider has built several one-way valves into the agreement: it can suspend service with minimal notice (Section 2.2), it claims broad rights over data flowing through the platform for ML/AI purposes (Section 1.6), and the data protection framework is skeletal enough that the Provider bears almost no affirmative security or privacy obligations in the Standard Terms themselves. The limitation of liability structure (Section 8) is formally mutual but the damages waiver on direct lost profits hits the Customer harder -- the Customer's losses from platform failure are business-operational; the Provider's losses are limited to unpaid fees.

The most structurally significant feature is the interplay between Sections 1.5, 1.6, 11, and 5.6. Taken together, they create a ratchet: the Customer retains ownership of Customer Content (Section 11) but grants the Provider processing rights for the service (Section 1.5) *and* for ML training (Section 1.6), and the ML training authorization survives termination (Section 5.6). Ownership without practical control is a hollow right. This is the contract's deepest asymmetry and it is not visible from reading any single clause in isolation.

A secondary structural point: the agreement separates Standard Terms from the Cover Page and Order Form, and several critical commercial terms -- liability caps, the definition of Increased and Unlimited Claims, governing law, notice periods -- live on the Cover Page. The Standard Terms are designed to be a fixed, reusable template. This means the real commercial negotiation happens on the Cover Page, and the Provider will resist modifying the Standard Terms. That dynamic shapes negotiation strategy.

---

## Key Findings

**1. ML/AI Training Rights Over Customer Content (Section 1.6) -- RED.** The single most consequential provision. The Provider claims the right to use both Usage Data and Customer Content to train AI/ML models, including third-party model components. The safeguards -- aggregation and "commercially reasonable efforts consistent with industry standard technology" for de-identification -- are qualitative, not technical, and unenforceable in practice. For an internal operations platform at $150K/year, the data flowing through the system (workflows, employee information, business processes) is the substance of the Customer's operations. Authorizing its use for model training -- especially third-party models -- is an irreversible data transfer. Trained models cannot be "un-trained." Combined with the survival clause (Section 5.6), the Provider retains these rights even after the relationship ends and the data is deleted. This must be fundamentally rewritten or struck.

**2. Absent Data Protection Infrastructure (Section 3) -- RED.** The contract contains almost no operative data protection terms. Section 3.1 requires a DPA "before submitting Personal Data governed by GDPR," but this is a deferred promise, not a binding framework. There is no DPA attached, no breach notification timeline, no security standards, no audit rights, no sub-processor controls, no cross-border transfer mechanism, and no coverage for non-GDPR privacy regimes (CCPA, state laws, etc.). For a platform that will process employee and operational data, this is a compliance gap, not merely a negotiation preference.

**3. Damages Waiver Covers Direct Lost Profits (Section 8.2) -- YELLOW, trending RED.** The damages waiver excludes "lost profits or revenues (whether direct or indirect)." Most SaaS agreements exclude only indirect or consequential lost profits. Including direct lost profits means that if the Provider's platform fails and causes quantifiable, direct revenue loss, the Customer has no claim for those losses. For an operations platform, this is material.

**4. Post-Termination Data Rights Are Weak (Section 5.5) -- YELLOW.** Data deletion is available only on request, with a 60-day window, no specified export format, no transition assistance, and no certification of completion. For a platform embedded in daily operations, migration planning requires stronger exit terms.

**5. Suspension Without Meaningful Notice (Section 2.2) -- YELLOW.** The Provider may suspend access "with or without notice" and will merely "try to inform" the Customer beforehand. For an operations platform, unannounced suspension is a business continuity risk.

---

## Clause-by-Clause Analysis

### Service, Access, and User Accounts (Sections 1.1--1.3) -- GREEN

The access grant is scoped appropriately to internal business purposes. The Affiliate structure -- separate Order Forms creating separate agreements -- is clean and limits cross-entity liability. User account responsibilities and security obligations are standard. No issues.

### Feedback and Usage Data (Section 1.4) -- YELLOW

**What the contract says**: Feedback is given "AS IS" and the Provider may use it "freely without any restriction or obligation." Usage Data may be collected and used freely for product improvement, but external disclosure must be aggregated and non-identifying.

**Deviation**: The "without any restriction or obligation" language on Feedback is broader than necessary. Market-standard clauses grant a license to use Feedback for product improvement but do not purport to override all other contractual obligations. The concern is compounded by the ML clause -- Feedback could be treated as an additional vector for training data.

**Redline**:

> **Current**: "Provider may use all Feedback freely without any restriction or obligation."
>
> **Proposed**: "Provider may use Feedback to develop, improve, and enhance the Product and Provider's other products and services. Provider's use of Feedback remains subject to Section 10 (Confidentiality) to the extent Feedback contains Customer's Confidential Information."
>
> **Rationale**: Preserves Provider's product improvement rights while ensuring Confidential Information protections are not inadvertently waived.
>
> **Priority**: Should-have
>
> **Fallback**: Add a clarifying sentence: "For clarity, this section does not limit Customer's rights under Section 10 (Confidentiality) with respect to Feedback that constitutes Confidential Information."

### Customer Content (Section 1.5) -- GREEN

Provider's usage rights are limited to what is needed to provide and maintain the Product. This is standard and appropriately scoped. Note that Section 11 qualifies Customer's retained ownership "subject to Sections 1.5 and 1.6" -- the Section 1.5 qualification is reasonable; the Section 1.6 qualification is not (addressed below).

### Machine Learning / AI Training (Section 1.6) -- RED

**What the contract says**: Both Usage Data and Customer Content may be used to train AI/ML models, including third-party model components. Customer "authorizes" this processing. Safeguards: aggregation required, "commercially reasonable efforts consistent with industry standard technology" for de-identification. Carves out that it does not reduce obligations under Applicable Data Protection Laws.

**Why this is the critical clause**: This is not a standard data use provision. It is an authorization to feed operational business data into models the Customer does not control, including third-party models. The de-identification standard is aspirational rather than technical -- "commercially reasonable efforts" is a negligence-adjacent standard, not a performance guarantee. There is no opt-out mechanism, no consent requirement for third-party model use, and no audit right over how data is actually used in training. Combined with the survival clause (Section 5.6), this authorization is perpetual and irrevocable even after the contract ends.

For an internal operations platform, the data at stake includes business process details, internal workflows, employee data, and potentially customer information. Once embedded in a trained model, this data cannot be retrieved, deleted, or contained.

**Redline**:

> **Current (Section 1.6, first sentence)**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes."
>
> **Proposed**: "Provider may use Usage Data (excluding Customer Content) to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, provided that: (a) Usage Data must be aggregated and de-identified using industry-standard technical measures (such as differential privacy or k-anonymity) before any such use; (b) Provider will not use Usage Data for training or developing third-party models or model components without Customer's prior written consent; and (c) Customer may opt out of such use upon 30 days' written notice to Provider, after which Provider will cease using Customer's Usage Data for new model training. Customer Content will not be used for any machine learning, artificial intelligence training, or model development purpose under any circumstances."
>
> **Rationale**: The Customer supports product improvement through aggregated, de-identified usage analytics but cannot authorize Customer Content -- which contains proprietary business data -- for model training. Technical de-identification standards replace the subjective "commercially reasonable efforts" qualifier. Third-party model training requires explicit consent.
>
> **Priority**: Must-have
>
> **Fallback**: If Provider insists on retaining some ML rights over Customer Content: (1) require explicit opt-in rather than default authorization; (2) require technical de-identification standards, not "commercially reasonable efforts"; (3) prohibit third-party model training entirely; (4) remove Section 1.6 from the survival clause (Section 5.6) so rights terminate with the agreement.

### Restrictions on Customer (Section 2.1) -- GREEN

Standard SaaS restrictions. The reverse engineering exception for applicable law is appropriate. The prohibition on security/vulnerability testing (Section 2.1(a)(v)) is worth flagging -- Customer may want to reserve the right to conduct penetration testing with reasonable notice -- but this is not a priority for this deal.

### Suspension (Section 2.2) -- YELLOW

**What the contract says**: Provider may suspend for undisputed balances over 30 days, breach of restrictions, or use that "materially and negatively impacts the Product or others." Suspension may be "with or without notice." Provider will "try to inform Customer before suspending... when practical."

**Deviation**: "Try to inform" is weaker than market practice. Enterprise SaaS agreements typically require written notice before suspension, with an exception for imminent harm or security emergencies. The "materially and negatively impacts... others" trigger is subjective and Provider-determined.

**Redline**:

> **Current**: "Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical."
>
> **Proposed**: "Provider will give Customer at least 5 business days' prior written notice before any suspension, except where immediate suspension is reasonably necessary to prevent imminent security threats or material harm to the Product or other customers, in which case Provider will notify Customer as soon as reasonably practicable and in any event within 24 hours after suspension."
>
> **Rationale**: For an operations platform, advance notice of suspension is an operational necessity, not a courtesy. The exception for genuine emergencies preserves Provider's ability to act quickly when needed.
>
> **Priority**: Should-have
>
> **Fallback**: Accept current language but add: "Provider will provide Customer with at least 48 hours' prior notice before suspending access due to an outstanding balance under Section 2.2(a)."

### Privacy & Security (Section 3) -- RED

**What the contract says**: Customer must enter a DPA before submitting GDPR-governed Personal Data. Customer may not submit Prohibited Data unless the Order Form authorizes it.

**What is missing**: Nearly everything that constitutes an operational data protection framework. Specifically:

- No DPA is attached or referenced -- it is a future obligation with no timeline
- Scope limited to GDPR; no coverage for CCPA, US state privacy laws, or other regimes
- No security baseline (SOC 2, ISO 27001, encryption requirements)
- No breach notification obligations or timeline
- No sub-processor disclosure, consent, or audit rights
- No cross-border transfer mechanisms (SCCs, adequacy decisions)
- No data residency commitments
- No data return format or portability provisions on termination

**Why it matters**: A $150K/year SaaS platform for internal operations will inevitably process personal data -- employee records, business contacts, internal communications. Operating without a DPA in place is a regulatory compliance gap from day one. The absence of security standards means the Customer has no contractual baseline against which to measure the Provider's data handling practices.

**Redline**:

> **Current (Section 3.1)**: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider."
>
> **Proposed**: "The parties will execute a Data Processing Addendum ('DPA') in the form attached as Exhibit [X] concurrently with, and as a condition precedent to the effectiveness of, this Agreement. The DPA will govern all processing of Personal Data under this Agreement, including Personal Data subject to GDPR, CCPA, and any other Applicable Data Protection Laws. At minimum, the DPA will address: (a) data breach notification to Customer within 48 hours of Provider becoming aware of a breach affecting Customer's Personal Data; (b) sub-processor disclosure, with prior written notice of changes and Customer's right to object; (c) annual audit rights, which may be satisfied by Provider's provision of a current SOC 2 Type II report; (d) cross-border data transfer mechanisms compliant with Applicable Data Protection Laws; and (e) data return in machine-readable format and certified deletion upon termination."
>
> **Rationale**: A DPA must be executed alongside the main agreement, not deferred as a future task. The minimum terms reflect enterprise standards for platforms processing employee and operational data.
>
> **Priority**: Must-have
>
> **Fallback**: At minimum: (1) DPA execution as a condition precedent; (2) 72-hour breach notification (GDPR standard); (3) Provider to supply current SOC 2 Type II report before execution.

### Payment & Taxes (Section 4) -- GREEN

Standard payment provisions. Non-refundable fees with exceptions for termination rights are market standard. The payment dispute process (Section 4.6) -- notice before due date, undisputed amounts paid on time, 15-day resolution window -- is balanced and reasonable. No concerns.

### Term & Termination (Sections 5.1--5.4) -- YELLOW

**What the contract says**: Auto-renewal unless notice given before the Non-Renewal Notice Date (Cover Page variable). Termination for cause with 30-day cure period. Immediate termination for incurable breach, dissolution, insolvency. Force Majeure termination after 30 consecutive days of material disruption, with prorated refund.

**Deviation**: Two gaps:

1. **No termination for convenience.** Neither party can exit early without cause. Standard for SaaS but creates full-term lock-in.
2. **Non-Renewal Notice Date is a Cover Page variable.** If set aggressively (90+ days), it creates an auto-renewal trap.

**Redline**:

> **Proposed addition (new Section 5.3(c))**: "Either party may terminate an Order Form for convenience upon not less than 90 days' prior written notice. Upon such termination, Customer will pay all Fees accrued through the effective date of termination and Provider will refund any prepaid Fees for the period following the effective date on a pro rata basis."
>
> **Rationale**: Termination for convenience is standard in enterprise SaaS agreements and prevents lock-in to an underperforming vendor. The 90-day notice period and payment through termination date protect Provider's revenue expectations.
>
> **Priority**: Should-have
>
> **Fallback**: If termination for convenience is rejected: (1) negotiate a Non-Renewal Notice Date of no more than 60 days; (2) ensure renewal terms are capped at one year regardless of initial term; (3) add a right to terminate without penalty if Provider materially reduces functionality (strengthening Section 6.4 beyond the existing cure-then-terminate framework).

### Post-Termination Effects (Section 5.5) -- YELLOW

**What the contract says**: Customer loses access. Provider deletes Customer Content within 60 days on request. Confidential Information returned or destroyed. Final invoice for outstanding fees.

**Deviation**: Deletion is request-dependent, not automatic. No data export format specified. No transition assistance obligation. No certification of deletion. 60 days is on the longer end.

**Redline**:

> **Current**: "Upon Customer's request, Provider will delete Customer Content within 60 days."
>
> **Proposed**: "Upon termination or expiration, Provider will, at Customer's election within 30 days: (a) return Customer Content in a machine-readable, industry-standard format (such as CSV, JSON, or API export) within 30 days of Customer's request; and/or (b) delete all Customer Content within 30 days of Customer's request (or, if Customer has requested return, within 30 days of completing the return). Provider will certify in writing that all Customer Content has been deleted from Provider's systems and backup media, except as required to be retained by Applicable Laws. If Customer does not make an election within 30 days of termination, Provider will delete Customer Content within 60 days of termination."
>
> **Rationale**: Data portability in a standard format is essential for migration to a replacement platform. Certification of deletion is standard enterprise practice.
>
> **Priority**: Should-have
>
> **Fallback**: Accept 60-day timeline but add: data return in machine-readable format on request and written certification of deletion.

### Survival (Section 5.6) -- YELLOW (tied to Section 1.6)

The survival of Sections 1.4 (Feedback and Usage Data) and 1.6 (Machine Learning) means the Provider's data use rights -- including the ML training authorization -- persist indefinitely after termination. If Section 1.6 is revised to exclude Customer Content and add an opt-out, survival of the revised clause is acceptable. If Section 1.6 remains in its current form, it must be removed from the survival clause.

> **Priority**: Must-have (conditional on Section 1.6 outcome)

### Representations & Warranties (Section 6) -- GREEN

Mutual representations are standard (authority, good standing, legal compliance). Provider's warranty against material reduction of functionality (Section 6.3) is a reasonable baseline. The remedy -- 45 days to discover, 45 days to cure, then termination with prorated refund (Section 6.4) -- is acceptable though the 45-day discovery window starts running regardless of whether the Customer detects the issue. For a $150K/year platform, a formal SLA with uptime commitments and service credits should be negotiated in the Order Form, but that is outside the scope of these Standard Terms.

### Disclaimer of Warranties (Section 7) -- GREEN

Standard mutual disclaimer of implied warranties (merchantability, fitness for a particular purpose, title, non-infringement), subject to the express warranties in Section 6. Appropriate and unremarkable.

### Limitation of Liability (Section 8) -- YELLOW

**What the contract says**: Three-tier cap structure -- General Cap, Increased Cap, Unlimited Claims. The damages waiver covers lost profits "whether direct or indirect," consequential, special, indirect, exemplary, punitive, and incidental damages. The waiver does not apply to Increased Claims or breach of Confidentiality.

**Deviation**: The framework is sound. Three issues:

1. **Cap amounts are Cover Page variables.** The actual dollar values of the General Cap and Increased Cap, and the classification of which claims are Increased vs. Unlimited, are undefined in the Standard Terms and must be negotiated.
2. **Direct lost profits exclusion.** Most enterprise SaaS agreements exclude only indirect or consequential lost profits. Excluding direct lost profits is aggressive -- if the platform fails and the Customer loses quantifiable revenue as a direct result, there is no remedy for those losses.
3. **Confidentiality breach carveout from damages waiver (Section 8.4) is favorable** to the Customer and should be preserved.

**Redline**:

> **Cover Page**: Negotiate General Cap at 12 months' Fees paid or payable; Increased Cap at 24 months' Fees. Provider's data breach obligations, confidentiality breach, and IP indemnification should be classified as Increased Claims at minimum; Unlimited Claims is the preferred position.
>
> **Section 8.2**: Change "lost profits or revenues (whether direct or indirect)" to "indirect lost profits or revenues."
>
> **Rationale**: Fee-based liability caps are market standard. Direct lost profits should remain recoverable where Provider's performance failures cause quantifiable business losses.
>
> **Priority**: Must-have (cap amounts); Should-have (direct lost profits revision)
>
> **Fallback**: Accept the direct lost profits exclusion if General Cap is set at 24 months' Fees.

### Indemnification (Section 9) -- GREEN

Mutual structure with standard procedural requirements (prompt notice, reasonable assistance, sole control of defense, no settlement with admission of fault without consent). Provider Covered Claims and Customer Covered Claims are Cover Page variables -- ensure Provider Covered Claims include IP infringement and data breach at minimum. The exclusive remedy provision (Section 9.6) is standard. Exclusions for unauthorized modification, unauthorized use, and combination with non-Provider items are reasonable.

### Confidentiality (Section 10) -- GREEN

Standard provisions: non-use, non-disclosure, standard exclusions (prior knowledge, public availability, independent development, authorized third-party receipt), required disclosure with reasonable advance notice, permitted disclosure to need-to-know personnel under equivalent confidentiality obligations. Adequate and unremarkable.

### Reservation of Rights (Section 11) -- GREEN (contingent)

Provider retains Product rights; Customer retains Customer Content rights "subject to Sections 1.5 and 1.6." The qualification by Section 1.6 is the practical consequence of the ML training clause -- Customer owns its content but has authorized the Provider to use it for training. If Section 1.6 is revised as proposed, this becomes unproblematic. If not, the Customer's ownership of its content is substantively hollow.

### Logo Rights (Section 12.8) -- YELLOW

**What the contract says**: Provider may use Customer's name and logo in marketing, with no consent requirement, no review right, and no opt-out.

**Redline**:

> **Current**: "Provider may use Customer's name and logo in marketing."
>
> **Proposed**: "Provider may include Customer's name and logo in Provider's customer lists and marketing materials, subject to Customer's trademark usage guidelines, if any. Customer may request removal of its name and logo at any time upon written notice, and Provider will comply within 30 days."
>
> **Rationale**: Standard practice to allow an opt-out right and require compliance with trademark guidelines.
>
> **Priority**: Nice-to-have
>
> **Fallback**: Accept as-is with the addition of an opt-out right on written notice.

### Assignment (Section 12.6), Force Majeure (Section 12.12), Governing Law (Section 12.3), Remaining General Terms -- GREEN

Assignment requires consent with a mutual change-of-control exception -- standard and balanced. Force Majeure is standard with appropriate carveout preserving payment obligations. Governing Law and Chosen Courts are Cover Page variables to be negotiated (prefer Customer's jurisdiction or a neutral forum). Remaining general terms (entire agreement, modifications, notices, independent contractors, export controls, anti-bribery, government rights, signature) are standard and raise no concerns.

---

## Negotiation Strategy

### Understanding the Other Side of the Table

The Provider selected Common Paper's standard form. This is a deliberate choice: Common Paper is marketed as a balanced, efficiency-oriented framework that reduces negotiation friction. The Provider's underlying message is "this is already fair -- let's not re-litigate standard terms." This framing creates an implicit burden on the Customer to justify any deviation as necessary rather than preferential.

The Provider is likely a mid-stage SaaS company building or integrating AI capabilities. The ML training clause (Section 1.6) is not boilerplate -- it is a product strategy decision embedded in legal terms. The Provider may view broad training data access as essential to its competitive position and product roadmap. This means the ML clause will draw the strongest resistance. However, the Provider also knows this clause is increasingly contested in enterprise procurement, and a well-reasoned alternative that preserves aggregated Usage Data rights while excluding Customer Content gives them a face-saving path to agreement.

On data protection, the Provider's position is structurally weak. Deferring the DPA to a future obligation while expecting the Customer to sign the main agreement is a compliance shortcut, not a principled position. Most SaaS vendors of this scale have a standard DPA -- the absence of one attached to the agreement likely reflects process informality rather than opposition to data protection terms. This is the easiest "win" in the negotiation because it aligns with the Provider's own regulatory interest.

### Sequencing the Conversation

**Open with data protection.** This is the highest-leverage, lowest-friction ask. Frame it as a mutual compliance requirement: "We need a DPA executed concurrently -- what does your standard DPA look like?" This positions the Customer as collaborative, not adversarial, and the Provider cannot credibly resist. Request the SOC 2 report and sub-processor list at the same time -- this is standard vendor diligence and normalizes the ask.

**Move immediately to the ML/AI training clause.** The natural bridge from data protection is: "While we are on data -- Section 1.6 presents a challenge for us." Position the Customer as supportive of product improvement through anonymized usage analytics (this is true and reasonable) while drawing a hard line on Customer Content. The key framing: "We cannot authorize Customer Content for model training, and we need an opt-out on Usage Data. We are happy for you to use aggregated, de-identified usage patterns." This gives the Provider most of what they need while protecting the Customer's core interest.

**Bundle the commercial terms.** Suspension notice, termination for convenience, post-termination data portability, and liability caps should be presented as a single coherent package: "These are our standard commercial requirements for an operations platform at this scale." Bundling achieves two things: it signals that the Customer is organized and has done this before, and it creates room for trade-offs within the package. The Provider can give on suspension notice if they hold on termination for convenience, for example.

**Hold back the concessions.** Logo rights, the Feedback clause refinement, and security testing rights are low-priority items the Customer can afford to concede. Do not offer them upfront -- hold them as chips. When the Provider pushes back on a Tier 1 or Tier 2 item, offer to accept the Standard Terms on logo rights or Feedback in exchange for movement on the item that matters. Explicit concessions on named terms feel more significant to the other side than they are.

### The BATNA Calculus

The Customer's BATNA is strong. This is a new vendor, not a strategic partnership. There is no existing integration, no switching cost, no relationship equity the Provider can leverage. The $150K/year deal size is meaningful for a mid-market vendor -- large enough that losing it is commercially painful, but not so large that it triggers the Provider's executive team to take extraordinary positions. The Customer can credibly walk away, and the Provider knows it. This leverage supports firmness on the must-haves.

The Provider's BATNA is acquiring a customer they do not yet have. Their cost of losing this deal is the revenue and the reference value. Their cost of conceding on the ML clause and DPA is operational -- they have to process differently for this customer, or more likely, they have to acknowledge concessions they will need to make for other enterprise customers too.

### Timeline Management

Two weeks is workable but leaves no room for delay. Recommended cadence:

- **Day 1**: Send the redline with a concise cover note organizing asks by priority. Simultaneously request the Provider's DPA, SOC 2 report, and sub-processor list.
- **Days 2-5**: Expect initial response. If the Provider's counsel engages quickly, schedule a call for days 4-5 to address the must-haves (ML clause, DPA, liability caps) directly.
- **Days 6-10**: Resolve should-haves. Finalize Cover Page terms. Trade concessions on nice-to-haves for movement on remaining issues.
- **Days 11-13**: Final review, sign-off, execution.
- **Day 14**: Buffer.

If the Provider does not respond within the first 3 days, escalate through the commercial relationship (sales contact) rather than waiting. A non-responsive legal team on a two-week timeline is a risk signal worth flagging to the business stakeholders.

---

## Next Steps

1. **Request Provider's DPA, SOC 2 Type II report, and sub-processor list immediately.** This is independent of the redline process and should start in parallel. If the Provider does not have a standard DPA, that is a significant finding that affects the risk assessment.

2. **Prepare the consolidated redline.** Organize by priority:
   - *Must-haves*: Section 1.6 (ML training -- exclude Customer Content, add opt-out), Section 3 (DPA as condition precedent), Section 8 (liability cap amounts on Cover Page), Section 5.6 (remove Section 1.6 from survival if not revised).
   - *Should-haves*: Section 2.2 (suspension notice), Section 5.1/5.3 (termination for convenience or tight non-renewal terms), Section 5.5 (data portability and deletion certification), Section 8.2 (direct lost profits), Section 1.4 (Feedback clause tightening).
   - *Nice-to-haves*: Section 12.8 (logo opt-out). Hold as concession chips.

3. **Review the Cover Page and Order Form.** Several critical terms are undefined in the Standard Terms: General Cap Amount, Increased Cap Amount, Increased Claims, Unlimited Claims, Provider Covered Claims, Customer Covered Claims, Governing Law, Chosen Courts, Non-Renewal Notice Date, Subscription Period, and Fees. These must be reviewed and negotiated alongside the Standard Terms -- they are where much of the real commercial risk sits.

4. **Conduct vendor due diligence.** New vendor, operations-critical platform. Confirm: security certifications, financial stability, customer references for similar deployments, incident response history, and data center/infrastructure details.

5. **Engage qualified legal counsel** to review the redlines before sending, particularly the data protection and ML training positions. This analysis is based on general commercial standards and does not constitute legal advice.

---

*This review is based on widely-accepted commercial standards for enterprise SaaS procurement. No organizational playbook was available. This analysis does not constitute legal advice and should be reviewed by qualified legal professionals before being relied upon for legal decisions.*
