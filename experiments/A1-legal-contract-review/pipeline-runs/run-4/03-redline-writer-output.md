**Important**: This document assists with legal workflows but does not constitute legal advice. All proposed language should be reviewed by qualified legal professionals before use in negotiations.

# Redline Proposals — Common Paper CSA v2.1

**Deal context**: $150K/year SaaS platform for internal operations. New vendor, not strategic but important. Customer side. Two-week deadline. Data protection and IP ownership are priority areas.

**Drafting posture**: This is a new vendor relationship at a mid-market deal size. The tone throughout is professional and firm but not adversarial — the goal is to land reasonable protections efficiently within the deadline, not to litigate every point. On data protection and IP items (the stated priorities), the language is more exacting. On commercial and operational items, the language aims for standard market position without over-engineering.

---

## Escalate Items

These items involve material risk that warrants senior counsel or business-level input before finalising the redline position. The proposed language below represents a reasonable starting position, but the final position may differ based on internal guidance.

---

### Section 1.6 — Machine Learning Training Rights over Customer Content

**Current language**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes. However, (a) Usage Data and Customer Content must be aggregated before it can be used for these purposes, and (b) Provider will use commercially reasonable efforts consistent with industry standard technology to de-identify Usage Data and Customer Content before such use."

**Proposed redline**: "Provider may use Usage Data to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's own products and services, subject to the following: (a) Usage Data must be aggregated and de-identified before use for such purposes, using techniques that meet or exceed the de-identification standards defined under Applicable Data Protection Laws, including but not limited to rendering the data not reasonably linkable to Customer, any User, or any identifiable individual; (b) Provider will not use Customer Content for the development, training, or enhancement of any artificial intelligence or machine learning model; (c) Provider will not use Usage Data or Customer Content for the development, training, or enhancement of any third-party model or any model not incorporated into the Product; and (d) the rights granted in this Section 1.6 do not survive expiration or termination of the Agreement and will cease upon the effective date of expiration or termination. For clarity, de-identification is an outcome-based obligation — Provider must achieve de-identification, not merely use reasonable efforts toward it."

**Rationale**: The current provision grants broad rights to use Customer Content for ML training, including for third-party model components, with only an effort-based de-identification standard and perpetual survival. Our position is that Customer Content should not be used for ML training at all — the content is provided for the purpose of receiving the contracted service, not for model development. We are comfortable with aggregated, properly de-identified Usage Data being used for Provider's own product improvement, which aligns with standard SaaS practice. We also ask that the de-identification obligation be outcome-based rather than effort-based, reflecting the actual data protection standard, and that the rights terminate with the agreement.

**Priority**: Must-have

**Note for escalation**: The business should confirm whether any Usage Data use for ML training is acceptable, or whether this section should be struck entirely. The proposed language permits Usage Data use with guardrails. If the business preference is no ML training of any kind, the redline simplifies to deleting Section 1.6 and removing it from the survival clause in Section 5.6.

---

### Section 8.2 — Direct Lost Profits Waiver

**Current language**: "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."

**Proposed redline**: "Neither party will be liable for consequential, special, indirect, exemplary, punitive, or incidental damages, including indirect lost profits or revenues, even if informed of the possibility. This exclusion does not apply to direct lost profits or revenues that are the direct and foreseeable result of a party's breach of this Agreement."

**Rationale**: The standard consequential damages waiver is appropriate and mutual. However, the current language also excludes direct lost profits — damages that flow directly and foreseeably from a breach. Excluding direct lost profits removes a significant and standard remedy category. Our proposed language maintains the mutual consequential damages exclusion while preserving the ability to recover direct, foreseeable financial losses, which is the prevailing market position for enterprise SaaS agreements.

**Priority**: Must-have

**Note for escalation**: The liability cap in Section 8.1 still applies to direct lost profits, so exposure is bounded. Senior counsel should confirm whether this position is firm or whether alternative protections (such as a higher liability cap or specific carve-outs for data-related breaches) would be acceptable instead.

---

### Section 2.2 — Suspension Without Notice, Time Limit, or Dispute Process

**Current language**: "If Customer (a) has an outstanding, undisputed balance on its account for more than 30 days; (b) breaches Section 2.1 (Restrictions on Customer); or (c) uses the Product in violation of the Agreement or in a way that materially and negatively impacts the Product or others, then Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical. Provider will reinstate Customer's access to the Product only if Customer resolves the underlying issue."

**Proposed redline**: "If Customer (a) has an outstanding, undisputed balance on its account for more than 30 days; (b) breaches Section 2.1 (Restrictions on Customer); or (c) uses the Product in a way that materially and negatively impacts the Product or other customers' use of the Product, then Provider may temporarily suspend Customer's access to the Product as follows:

(i) Except in cases of imminent security risk or material harm to other customers, Provider will give Customer at least 5 business days' prior written notice describing the grounds for suspension and a reasonable opportunity to cure the issue before suspension takes effect.

(ii) In cases of imminent security risk or material harm to other customers, Provider may suspend immediately upon notice, provided that Provider gives written notice describing the grounds no later than one business day after suspension.

(iii) Any suspension will be limited in scope to the minimum necessary to address the underlying issue.

(iv) If suspension continues for more than 30 consecutive days, Customer may terminate the affected Order Form upon written notice and receive a prorated refund of prepaid Fees for the remainder of the Subscription Period.

(v) Fees will not accrue during any period of Provider-initiated suspension.

(vi) If Customer disputes the grounds for suspension in writing, the parties will follow the dispute resolution process in Section 4.6, and Provider will reinstate access pending resolution unless continued access poses an imminent security risk or material harm to other customers."

**Rationale**: The current suspension provision allows suspension without prior notice, without a cure period, without a time limit, and without fee relief. For an operational SaaS platform, unilateral suspension without process creates significant business continuity risk. Our proposed language preserves Provider's ability to act quickly in genuine emergencies while adding standard procedural protections: prior notice and cure opportunity in non-emergency cases, a maximum suspension duration, fee suspension during Provider-initiated downtime, and a dispute mechanism. These are standard protections in enterprise SaaS agreements.

**Priority**: Must-have

**Note for escalation**: The interaction between suspension, continued fees, and the non-refundable fees clause creates a compound risk. This redline addresses suspension specifically. Senior counsel should also consider whether the non-refundable fees clause in Section 4.1 needs a corresponding carve-out for Provider-initiated suspension periods.

---

### Section 3 — No Security Commitments in Standard Terms

**Current language**: Section 3 contains only two provisions: a DPA requirement before submitting GDPR-governed Personal Data (3.1) and a prohibition on Prohibited Data unless authorised (3.2).

**Proposed redline — add new Section 3.3**:

"**3.3 Security Standards.** Provider will maintain administrative, technical, and physical safeguards designed to protect Customer Content and Personal Data against unauthorized access, destruction, loss, alteration, or disclosure. Without limiting the foregoing, Provider will:

(a) maintain SOC 2 Type II certification (or a substantially equivalent third-party security certification) covering the systems used to process Customer Content, and make the most recent audit report available to Customer upon written request, no more than once per twelve-month period;

(b) encrypt Customer Content in transit using TLS 1.2 or higher, and at rest using AES-256 or equivalent;

(c) notify Customer in writing without unreasonable delay and in any event within 72 hours after confirming a Security Incident — meaning any unauthorized access to, or acquisition, disclosure, or loss of, Customer Content or Personal Data. The notification will include, to the extent known: the nature of the incident, the categories and approximate volume of data affected, the measures taken or proposed to address the incident, and a contact point for further information;

(d) not materially reduce the security measures applicable to Customer Content during the Subscription Period; and

(e) prior to engaging any new sub-processor that will have access to Customer Content or Personal Data, provide Customer with at least 30 days' advance written notice identifying the sub-processor and the nature of the processing. If Customer reasonably objects to the new sub-processor within that notice period on legitimate data protection grounds, the parties will work together in good faith to find an alternative. If no alternative is agreed within 30 days of Customer's objection, Customer may terminate the affected Order Form and receive a prorated refund of prepaid Fees for the remainder of the Subscription Period."

**Rationale**: The current Standard Terms contain no security commitments — no encryption requirements, no audit rights, no breach notification, and no sub-processor transparency. For a platform handling operational data, baseline security commitments in the main agreement are a standard expectation. The proposed language reflects widely adopted enterprise standards: SOC 2 certification, encryption, 72-hour breach notification (consistent with GDPR timelines), and sub-processor notice with an objection right. These provisions should apply to all Customer data, not only GDPR-governed data.

**Priority**: Must-have

---

### Section 2.1(a)(v) — Security Testing Prohibition

**Current language**: "conduct security or vulnerability tests on, interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product"

**Proposed redline**: "interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product. Customer may conduct or commission security or vulnerability assessments of the Product, provided that Customer (a) gives Provider at least 15 business days' advance written notice; (b) conducts such testing in a manner designed to minimize disruption to the Product; and (c) promptly shares with Provider any material findings. Provider may, at its option, participate in or observe such testing."

**Rationale**: The current restriction prohibits all security testing without exception. Combined with the absence of audit rights and security commitments, this leaves Customer with no mechanism to verify the security posture of a platform processing its operational data. The proposed language removes the blanket prohibition on security testing while retaining protections against interference and degradation. The advance notice, minimal disruption, and findings-sharing requirements protect Provider's legitimate operational interests.

**Priority**: Should-have

**Fallback**: If Provider will not permit Customer-commissioned testing, an acceptable alternative is for Provider to (a) conduct annual third-party penetration testing of the Product, (b) make the executive summary of testing results available to Customer under NDA, and (c) remediate critical and high-severity findings within defined timelines (30 days for critical, 90 days for high).

---

## Negotiate Items

---

### Section 12.8 — Provider Logo Rights Without Consent

**Current language**: "Provider may use Customer's name and logo in marketing."

**Proposed redline**: "Neither party may use the other party's name, logo, or trademarks in marketing materials without the other party's prior written consent, which may be withheld in that party's sole discretion. Notwithstanding the foregoing, Provider may include Customer's name in a list of customers on Provider's website or in Provider's sales materials without prior consent, provided that such use does not imply any endorsement by Customer."

**Rationale**: Our organisation's brand usage policy requires internal approval before third parties use our name or logo in marketing. A mutual consent requirement is standard practice and protects both parties' brand interests. We are comfortable with inclusion in a customer list, which is standard industry practice.

**Priority**: Nice-to-have

**Fallback**: If mutual consent is not acceptable, an opt-out right: "Customer may opt out of any logo or marketing use by providing written notice to Provider, and Provider will cease such use within 30 days of receiving notice."

---

### Sections 6.3, 6.4 — Narrow Provider Warranty with Extended Remedy Timeline

**Current language (6.3)**: "Provider represents and warrants to Customer that it will not materially reduce the general functionality of the Cloud Service during the Subscription Period."

**Current language (6.4)**: "If Provider breaches the warranty in Section 6.3, Customer must give Provider notice within 45 days of discovering the issue. Within 45 days of receiving sufficient details, Provider will attempt to restore the general functionality. If Provider cannot resolve the issue, Customer may terminate the affected Order Form and Provider will pay a prorated refund."

**Proposed redline (6.3)**: "Provider represents and warrants to Customer that (a) the Cloud Service will perform materially in accordance with the Documentation during the Subscription Period; and (b) Provider will not materially reduce the general functionality of the Cloud Service during the Subscription Period."

**Proposed redline (6.4)**: "If Provider breaches the warranty in Section 6.3, Customer must give Provider notice within 30 days of discovering the issue. Within 30 days of receiving sufficient details from Customer, Provider will use commercially reasonable efforts to restore conformance. If Provider cannot resolve the issue within that 30-day cure period, Customer may terminate the affected Order Form and Provider will pay a prorated refund of prepaid Fees for the remainder of the Subscription Period, plus a credit for Fees paid during the period between Customer's initial notice and the date of termination."

**Rationale**: The current warranty covers only Provider actively degrading functionality — it does not cover failures to perform in accordance with documentation, outages, or defects. Adding a documentation-conformance warranty is standard for enterprise SaaS. The remedy timeline is shortened from 45+45 days to 30+30 days, which is the prevailing market standard, and we have added fee credits for the degradation period so that Customer is not paying full price for a non-conforming service.

**Priority**: Should-have

**Fallback**: If Provider will not accept a documentation-conformance warranty, retain the existing warranty scope but shorten the timelines to 30+30 days and add the fee credit for the degradation period.

---

### Sections 5.1, 4.1 — Auto-Renewal Lock-In with No Convenience Termination

**Current language (5.1)**: "...automatically renew for additional Subscription Periods unless one party gives notice of non-renewal to the other party before the Non-Renewal Notice Date."

**Current language (4.1)**: "...Fees are non-refundable."

**Proposed redline — add new Section 5.3(c)**: "(c) Either party may terminate an Order Form for convenience upon 90 days' prior written notice to the other party. If Customer terminates for convenience, Provider will refund a prorated portion of any prepaid Fees for the remainder of the Subscription Period following the effective date of termination."

**Rationale**: The combination of auto-renewal, non-refundable fees, and no convenience termination right creates a rigid lock-in structure. For an initial engagement with a new vendor, a convenience termination right with reasonable notice provides flexibility to exit if the service does not meet operational needs, without requiring Customer to manufacture a material breach claim. The 90-day notice period gives Provider adequate planning time.

**Priority**: Should-have

**Fallback**: If a full convenience termination right is not acceptable, add a termination right triggered by the end of the initial Subscription Period with 60 days' notice, and limit auto-renewal terms to month-to-month (rather than full-year renewals) after the initial Subscription Period.

---

### No Data Breach Notification Obligation (gap — no existing section)

**Current language**: None. No provision in the Standard Terms addresses breach notification.

**Proposed redline**: Addressed in the proposed new Section 3.3(c) above (Security Standards). The breach notification obligation is included there as part of the comprehensive security framework, requiring written notice within 72 hours with specified content.

**Priority**: Must-have (addressed within the Section 3.3 redline above)

---

### Section 5.5 — No Transition Assistance on Termination

**Current language**: "(b) Upon Customer's request, Provider will delete Customer Content within 60 days."

**Proposed redline — replace Section 5.5(b)**: "(b) For a period of 60 days following the effective date of expiration or termination (the 'Transition Period'), Provider will make Customer Content available to Customer for export in a structured, commonly-used, machine-readable format. Provider will provide reasonable cooperation to facilitate Customer's data migration, at Customer's expense for any out-of-scope professional services. Upon expiration of the Transition Period, or upon Customer's earlier written request, Provider will delete Customer Content in accordance with Provider's standard deletion processes and certify such deletion in writing within 30 days."

**Rationale**: The current provision only allows Customer to request deletion — it provides no export rights, no required format, and no transition period. For an operational SaaS platform, the ability to extract data in a usable format after termination is essential to avoid vendor lock-in and ensure business continuity. The proposed language provides a 60-day transition window with export in a standard format, followed by deletion with certification.

**Priority**: Should-have

**Fallback**: If Provider will not offer a full transition period with continued access, an acceptable minimum is a requirement to provide a complete data export in a machine-readable format (such as CSV or JSON) within 30 days of termination, at no additional charge.

---

### Section 12.6 — Assignment on Change of Control with No Termination Right

**Current language**: "No assignment without consent, except in merger/acquisition/change of control."

**Proposed redline**: "Neither party may assign this Agreement without the other party's prior written consent, except in connection with a merger, acquisition, corporate reorganization, or sale of all or substantially all of the assigning party's assets, provided that the assignee agrees in writing to be bound by the terms of this Agreement. If Provider undergoes a change of control, Provider will notify Customer within 30 days of the change of control event. Customer may terminate this Agreement upon 60 days' written notice given within 90 days of receiving such notification, and Provider will pay Customer a prorated refund of any prepaid Fees for the remainder of the Subscription Period."

**Rationale**: If Provider is acquired by a competitor or by an entity with materially different privacy or security practices, Customer should have the option to exit the relationship. A termination right on change of control is a standard protection in enterprise SaaS procurement. The 60-day notice period and 90-day exercise window give both parties adequate time to plan.

**Priority**: Should-have

**Fallback**: If a unilateral termination right is not acceptable, limit the right to cases where the acquirer is a direct competitor of Customer, or where the acquirer does not agree to maintain equivalent data protection standards.

---

### Section 3.1 — DPA Requirement Limited to GDPR

**Current language**: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider."

**Proposed redline**: "Before submitting Personal Data to the Product, Customer and Provider will enter into a data processing agreement that addresses the requirements of all Applicable Data Protection Laws governing such Personal Data, including but not limited to GDPR, CCPA/CPRA, LGPD, and POPIA. If the parties have a DPA, each party will comply with its obligations in the DPA, the terms of the DPA will control each party's rights and obligations as to Personal Data, and the terms of the DPA will control in the event of any conflict with this Agreement."

**Rationale**: The current DPA requirement applies only to GDPR-governed Personal Data. Personal Data governed by other privacy regimes — including CCPA, LGPD, and POPIA — has no DPA requirement under the Standard Terms and therefore no contractual processing restrictions. A DPA requirement for all Personal Data, regardless of governing law, is standard practice and necessary to operationalise compliance obligations that exist independently under applicable law.

**Priority**: Must-have

**Fallback**: At minimum, expand the DPA requirement to cover all Personal Data governed by any Applicable Data Protection Law, without enumerating specific statutes.

---

### Section 1.4 — Feedback Rights

**Current language**: "Provider may use all Feedback freely without any restriction or obligation."

**Proposed redline**: "Provider may use Feedback for the purpose of developing, improving, and enhancing Provider's products and services, without any obligation of attribution or compensation to Customer. For clarity, this grant does not convey to Provider any rights in Customer's Confidential Information or Customer Content that may be included in or referenced by such Feedback."

**Rationale**: The current "without any restriction or obligation" language is broader than necessary for legitimate product improvement purposes. The proposed language preserves Provider's ability to use feedback for product development — which is standard and reasonable — while clarifying that the feedback licence does not inadvertently expand Provider's rights over Customer's Confidential Information or Customer Content.

**Priority**: Nice-to-have

**Fallback**: Retain the current language but add the clarification sentence regarding Confidential Information and Customer Content.

---

### Section 1.5 — Customer Content Use for "Related Offerings"

**Current language**: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings."

**Proposed redline**: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product."

**Rationale**: "Related offerings" is undefined and could extend Provider's use rights to products and services that Customer did not contract for. Limiting use to the contracted Product is the standard position and ensures Customer Content is used only for the purpose for which it was provided.

**Priority**: Should-have

**Fallback**: If Provider needs flexibility to use Customer Content across integrated services, define "related offerings" as "services that are integrated with and necessary for the operation of the Product as described in the Documentation."

---

## Summary of Redline Priorities

### Must-Have
| Section | Issue |
|---------|-------|
| 1.6 | ML training rights — remove Customer Content, outcome-based de-identification, no third-party models, no survival |
| 8.2 | Direct lost profits — preserve as recoverable damages |
| 2.2 | Suspension — add notice, cure, time limit, fee relief, dispute process |
| 3 (new 3.3) | Security commitments — SOC 2, encryption, breach notification, sub-processor controls |
| 3.1 | DPA scope — expand beyond GDPR to all Applicable Data Protection Laws |

### Should-Have
| Section | Issue |
|---------|-------|
| 2.1(a)(v) | Security testing — permit with notice and safeguards |
| 6.3, 6.4 | Warranty — add documentation conformance, shorten timelines, add credits |
| 5.1/new 5.3(c) | Convenience termination — 90 days' notice with prorated refund |
| 5.5(b) | Transition assistance — 60-day export window in machine-readable format |
| 12.6 | Change of control — Customer termination right with prorated refund |
| 1.5 | Customer Content scope — remove "related offerings" |

### Nice-to-Have
| Section | Issue |
|---------|-------|
| 12.8 | Logo rights — mutual consent requirement |
| 1.4 | Feedback — limit to product improvement, protect Confidential Information |
