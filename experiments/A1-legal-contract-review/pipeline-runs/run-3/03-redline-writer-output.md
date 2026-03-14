# Redline Writer Output

**Important**: This analysis assists with legal workflows but does not constitute legal advice. All proposed language should be reviewed by qualified legal professionals before use in negotiations.

**Deal context**: Customer side, $150K/year SaaS platform for internal operations, new vendor (not strategic but important), standard procurement process, 2-week deadline. Data protection and IP ownership are priorities.

---

## Escalate Items

*These deviations represent material departures from commercial standards. The proposed language below reflects standard market positions. Because these are escalation items, the appropriate position should be confirmed by senior counsel or business leadership before the redlines are finalized and delivered to Provider.*

---

### Section 1.6 — Machine Learning / AI Training Rights

**Current language**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes. However, (a) Usage Data and Customer Content must be aggregated before it can be used for these purposes, and (b) Provider will use commercially reasonable efforts consistent with industry standard technology to de-identify Usage Data and Customer Content before such use."

**Proposed redline**: "Provider may use Usage Data, after aggregation and de-identification such that it cannot reasonably be used to identify Customer, its Users, or any individual, to maintain, improve, and enhance the Cloud Service subscribed to by Customer. Provider will not use Customer Content to develop, train, or enhance artificial intelligence or machine learning models. Provider will not make Usage Data or Customer Content available, whether aggregated or otherwise, to any third party for purposes of developing, training, or enhancing artificial intelligence or machine learning models. The rights granted in this Section 1.6 do not survive expiration or termination of this Agreement."

**Rationale**: Customer requires clear boundaries between its operational data and Provider's ML/AI development activities. This language permits Provider to use anonymized usage patterns to improve the specific service Customer subscribes to — a reasonable and common arrangement — while preventing use of Customer Content for model training and preventing any data flow to third-party model development. The de-identification standard is outcome-based rather than effort-based, reflecting the practical reality that effort-based standards provide limited assurance once data has been incorporated into a trained model.

**Priority**: Must-have

---

### Section 2.1(a)(v) — Security Testing Prohibition

**Current language**: "conduct security or vulnerability tests on, interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product"

**Proposed redline**: "interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product. Notwithstanding the foregoing, Customer may conduct security assessments and penetration testing of the Product, provided that (a) Customer gives Provider at least 10 business days' prior written notice describing the scope and methodology of the proposed testing; (b) such testing is conducted by a qualified third-party security firm or Customer's internal security team; (c) testing is limited to Customer's own tenant or instance and does not target shared infrastructure; and (d) Customer promptly shares results with Provider and does not publicly disclose identified vulnerabilities without giving Provider a reasonable opportunity to remediate. In addition, Provider will, upon Customer's written request and no more than once per calendar year, provide Customer with a copy of Provider's most recent third-party penetration test report or SOC 2 Type II report."

**Rationale**: Customer's internal security policies require the ability to assess the security posture of platforms that process its operational data. The proposed language respects Provider's legitimate interest in infrastructure protection through advance notice and scope limitations, while providing Customer with the assurance pathway that is standard in mid-market SaaS agreements.

**Priority**: Must-have

---

### Absence of Security Commitments (new Section 3.2)

**Current language**: No security commitments exist in the Standard Terms.

**Proposed redline** (new Section 3.2, with subsequent sections renumbered):

"3.2 Security Standards. Provider will implement and maintain administrative, technical, and physical safeguards designed to protect Customer Content, Personal Data, and Usage Data against unauthorized access, use, alteration, or destruction. These safeguards will include, at a minimum: (a) encryption of Customer Content in transit (using TLS 1.2 or later) and at rest (using AES-256 or equivalent); (b) access controls limiting access to Customer Content to Provider personnel with a legitimate business need; (c) logging and monitoring of access to Customer Content; and (d) annual independent third-party security assessments. Provider will maintain SOC 2 Type II certification (or an equivalent industry-recognized certification) and will provide Customer with a copy of its most recent certification report upon written request."

**Rationale**: For a SaaS platform processing Customer's internal operational data at this investment level, baseline security commitments are a standard and expected component of the agreement. The proposed safeguards reflect practices that established cloud service providers already implement operationally. Specifying these obligations contractually aligns the agreement with Customer's vendor management requirements and standard market terms.

**Priority**: Must-have

---

### Absence of Data Breach Notification (new Section 3.3)

**Current language**: No breach notification provision exists in the Standard Terms.

**Proposed redline** (new Section 3.3):

"3.3 Security Incident Notification. Provider will notify Customer in writing without undue delay, and in any event within 72 hours, after becoming aware of any unauthorized access to, or unauthorized acquisition, disclosure, or use of, Customer Content or Personal Data (a 'Security Incident'). Such notification will include: (a) a description of the nature of the Security Incident, including the categories of data affected; (b) the approximate number of records involved, to the extent known; (c) the measures Provider has taken or proposes to take to address the Security Incident and mitigate its effects; and (d) a designated contact point for further information. Provider will cooperate with Customer's reasonable requests in connection with Customer's incident response and any required notifications to regulators or affected individuals. Provider will not issue any public statement regarding a Security Incident that identifies Customer without Customer's prior written consent, except as required by Applicable Laws."

**Rationale**: Breach notification is a baseline expectation for any SaaS agreement handling business data. The 72-hour timeline aligns with GDPR requirements and reflects the time-sensitive nature of incident response. The cooperation and consent provisions ensure Customer retains control over its own notification and communications obligations.

**Priority**: Must-have

---

### Section 2.2 — Suspension Rights

**Current language**: "Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical. Provider will reinstate Customer's access to the Product only if Customer resolves the underlying issue."

**Proposed redline**: "Provider may temporarily suspend Customer's access to the Product, subject to the following:

(a) Except where immediate suspension is necessary to prevent imminent harm to the security or integrity of the Product, to prevent material harm to other customers, or to comply with a court order or Applicable Laws, Provider will give Customer at least 5 business days' prior written notice specifying the grounds for suspension and an opportunity to cure the underlying issue before suspension takes effect.

(b) Where Provider suspends access without prior notice under the exceptions in subsection (a), Provider will notify Customer in writing as soon as reasonably practicable and in any event within 24 hours after suspension.

(c) Suspension will be limited to the affected Users, features, or components of the Product where commercially feasible, rather than Customer's entire account.

(d) Provider will reinstate access within 2 business days after Customer resolves the underlying issue.

(e) If suspension continues for more than 10 consecutive business days, Customer may terminate the affected Order Form upon written notice and Provider will pay a prorated refund of any prepaid Fees for the remainder of the Subscription Period.

(f) Fees will not accrue for any period during which Customer's access to the Product is suspended for reasons other than Customer's payment default."

**Rationale**: For a platform supporting Customer's internal operations, unannounced suspension creates significant business continuity risk. The proposed language preserves Provider's ability to act quickly when genuine security or legal concerns require it, while providing notice, proportionality, and a reasonable exit mechanism for extended disruptions. The fee abatement provision during non-payment-related suspension ensures Customer is not paying for access it does not have.

**Priority**: Must-have

---

### Absence of Service Level Agreement (new Section 1.2A or Order Form addendum)

**Current language**: No uptime, availability, or performance commitments exist in the Standard Terms.

**Proposed redline** (new Section 1.2A):

"1.2A Service Levels. (a) Provider will use commercially reasonable efforts to maintain the Cloud Service with a Monthly Uptime Percentage of at least 99.5%. 'Monthly Uptime Percentage' means the total number of minutes in a calendar month minus the number of minutes of Downtime, divided by the total number of minutes in the calendar month. 'Downtime' means any period during which the Cloud Service is materially unavailable to Customer, excluding scheduled maintenance.

(b) Provider will provide Customer with at least 48 hours' advance notice of scheduled maintenance that may affect availability and will use commercially reasonable efforts to schedule such maintenance outside Customer's primary business hours.

(c) If the Monthly Uptime Percentage falls below 99.5% in any calendar month, Customer will receive a service credit equal to: (i) 5% of the monthly Fees for each full percentage point below 99.5%, up to a maximum credit of 30% of the applicable month's Fees. Service credits will be applied against the next invoice, or refunded if no further Fees are due. Customer must request service credits within 30 days of the end of the affected month.

(d) Service credits are Customer's sole and exclusive remedy for failure to meet the Monthly Uptime Percentage and do not limit any other rights Customer may have under this Agreement, including termination for material breach."

**Rationale**: A baseline availability commitment is standard for SaaS platforms at this investment level. The proposed 99.5% threshold and credit structure reflect common mid-market SaaS terms and give both parties a clear, measurable performance standard.

**Priority**: Should-have

**Fallback**: If Provider will not commit to specific uptime percentages and service credits in the Standard Terms, the minimum acceptable position is (a) a general commitment to commercially reasonable availability, (b) advance notice of scheduled maintenance, and (c) agreement that the SLA details will be specified in the Order Form. The Order Form should then set a specific uptime target and credit structure before execution.

---

### Section 5.5 — Post-Termination Data Handling

**Current language**: "(b) Upon Customer's request, Provider will delete Customer Content within 60 days."

**Proposed redline**: "(b) For a period of 30 days following the effective date of expiration or termination (the 'Export Period'), Provider will make Customer Content available for export in a standard, machine-readable format (such as CSV, JSON, or via API access). Provider will provide reasonable cooperation with Customer's data migration efforts; if Customer requires Provider's active assistance beyond making data available, Provider may charge its then-current professional services rates. Following the Export Period, Provider will delete all Customer Content within 30 days and, upon Customer's written request, will certify in writing that deletion has been completed. If Customer requests earlier deletion before the Export Period expires, Provider will comply within 30 days of the request."

**Rationale**: For a platform managing internal operational data, the ability to extract data in a usable format upon termination is essential for business continuity and vendor transition. Deletion without an export pathway creates vendor lock-in and operational risk that is inconsistent with standard market terms.

**Priority**: Must-have

---

## Negotiate Items

---

### Section 8.2 — Consequential Damages Waiver Including Direct Lost Profits

**Current language**: "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."

**Proposed redline**: "Neither party will be liable for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility. The foregoing will not apply to Increased Claims or breach of Section 10 (Confidentiality)."

**Rationale**: The mutual waiver of consequential damages is standard and accepted. However, the current formulation explicitly includes direct lost profits in the waiver, which is beyond the standard market position and effectively eliminates Customer's primary measure of recovery for service failures. Removing "lost profits or revenues (whether direct or indirect)" from the waiver restores Customer's ability to recover direct damages for service disruption, which is the standard position. The existing exceptions for Increased Claims and confidentiality breach are retained.

**Priority**: Must-have

**Fallback**: If Provider insists on retaining some lost profits limitation, a fallback is to exclude direct lost profits from the waiver but retain the waiver of indirect lost profits: "Neither party will be liable for indirect lost profits or revenues, or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."

---

### Section 8.1 — Liability Cap Structure (Cover Page Terms)

**Current language**: "Each party's total cumulative liability for all claims will not be more than the General Cap Amount." / "Each party's total cumulative liability for Increased Claims will not be more than the Increased Cap Amount." All amounts and claim categories are Cover Page variables.

**Proposed Cover Page terms**:

- **General Cap Amount**: The greater of (a) the total Fees paid and payable by Customer during the 12-month period immediately preceding the event giving rise to the claim, or (b) $150,000.
- **Increased Cap Amount**: Two times (2x) the General Cap Amount.
- **Increased Claims**: (a) Provider's indemnification obligations under Section 9.1; (b) Provider's breach of Section 3 (Privacy & Security), including any data breach or Security Incident; (c) breach of Section 10 (Confidentiality) by either party; (d) Customer's indemnification obligations under Section 9.2.
- **Unlimited Claims**: Either party's liability arising from (a) gross negligence or willful misconduct; (b) breach of Applicable Data Protection Laws resulting in unauthorized disclosure of Personal Data; or (c) infringement or misappropriation of the other party's intellectual property rights.

**Rationale**: These categories and values reflect standard mid-market SaaS positions and ensure that the liability framework is proportionate to the deal size and the nature of the risks involved. A 12-month fee floor ensures a meaningful recovery minimum. Elevating security, privacy, and indemnification claims to the increased tier reflects the heightened significance of these areas for a data-processing SaaS relationship.

**Priority**: Must-have

**Fallback**: If Provider will not accept unlimited liability for data protection breaches, a 3x General Cap Amount for all Increased Claims is acceptable. If Provider resists the intellectual property uncapping, that category can move to the Increased Claims tier instead.

---

### Section 12.12 — Force Majeure Payment Carveout

**Current language**: "Neither party liable for delays from Force Majeure Events, except Customer's payment obligations."

The full text of Section 5.4 provides context: "Either party may terminate an affected Order Form upon notice if a Force Majeure Event prevents the Product from materially operating for 30 or more consecutive days. Provider will pay to Customer a prorated refund of any prepaid Fees for the remainder of the Subscription Period."

**Proposed redline** (Section 12.12): "Neither party will be liable for delays or failures in performance resulting from Force Majeure Events, except that each party will continue to comply with its obligations under Section 10 (Confidentiality). If a Force Majeure Event prevents Provider from delivering the Cloud Service for more than 5 consecutive business days, Customer's payment obligations will be suspended for the duration of the non-delivery. Customer's obligation to pay Fees will resume when Provider restores the Cloud Service to material operability."

**Rationale**: Requiring payment for service that is not being delivered due to events outside either party's control creates an inequitable allocation of force majeure risk. The proposed language preserves the mutual force majeure defense for performance delays while ensuring that payment obligations correspond to actual service delivery.

**Priority**: Should-have

**Fallback**: If Provider insists on retaining the payment carveout, a fallback is to provide service credits for force majeure downtime: "If a Force Majeure Event prevents the Product from materially operating for more than 5 consecutive business days, Customer will receive a service credit equal to the prorated Fees for the period of non-delivery, to be applied against the next invoice."

---

### Section 3.1 — GDPR-Only DPA Trigger

**Current language**: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider."

**Proposed redline**: "The parties will enter into a data processing agreement (the 'DPA') prior to the submission of any Personal Data to the Product. The DPA will govern the processing of Personal Data under all Applicable Data Protection Laws, including but not limited to GDPR, the California Consumer Privacy Act (CCPA, as amended by the CPRA), the UK GDPR, and any other data protection laws applicable to the processing. The terms of the DPA will control each party's rights and obligations as to Personal Data, and the terms of the DPA will control in the event of any conflict with this Agreement."

**Rationale**: A DPA triggered only by GDPR-governed data leaves Personal Data subject to other regulatory frameworks without a specified contractual protection mechanism. The proposed language ensures comprehensive data protection coverage regardless of the applicable regulatory regime and reflects the multi-jurisdictional reality of modern data processing.

**Priority**: Should-have

**Fallback**: If Provider prefers to maintain the GDPR-specific trigger, add a second sentence: "With respect to Personal Data governed by Applicable Data Protection Laws other than GDPR, Provider will process such Personal Data in accordance with the data protection obligations set forth in the DPA as if those obligations applied to all Personal Data submitted to the Product."

---

### Absence of Subprocessor Controls (new Section 3.4)

**Current language**: No subprocessor provisions exist in the Standard Terms.

**Proposed redline** (new Section 3.4):

"3.4 Subprocessors. (a) Provider will maintain a list of subprocessors that process Customer Content or Personal Data, including each subprocessor's name, location, and the nature of processing performed. Provider will make this list available to Customer upon written request.

(b) Provider will notify Customer at least 30 days before engaging any new subprocessor that will process Customer Content or Personal Data. Customer may object to a new subprocessor on reasonable grounds by providing written notice to Provider within 15 days of receiving Provider's notification. If Customer objects, the parties will work in good faith for 15 days to resolve Customer's concerns. If the parties are unable to resolve Customer's concerns, Customer may terminate the affected Order Form upon written notice and Provider will pay a prorated refund of any prepaid Fees for the remainder of the Subscription Period.

(c) Provider will require each subprocessor to be bound by data protection obligations no less protective than those in this Agreement and any applicable DPA. Provider remains liable for the acts and omissions of its subprocessors to the same extent as if Provider had performed the processing directly."

**Rationale**: Subprocessor transparency and governance are standard components of SaaS data protection frameworks. Customer requires visibility into who processes its data, advance notice of changes, and a mechanism to object where a new subprocessor raises legitimate concerns. Provider's continued liability for subprocessor conduct ensures accountability and is consistent with the principle that Provider selected and engaged the subprocessor.

**Priority**: Should-have

**Fallback**: If Provider will not accept the full objection and termination mechanism, the minimum acceptable position is (a) a maintained and available subprocessor list, (b) advance notification of new subprocessors, and (c) Provider's obligation to flow down equivalent data protection obligations. The fallback omits the objection right and termination trigger.

---

### Sections 4.1 / 5.3 — Refund on Provider Material Breach Termination

**Current language**: "Except for the prorated refund of prepaid Fees allowed with specific termination rights given in the Agreement, Fees are non-refundable." (Section 4.1)

Refund rights exist for warranty breach (Section 6.4) and force majeure (Section 5.4), but no refund right exists for termination due to Provider's material breach under Section 5.3.

**Proposed redline** (addition to Section 4.1): "Except for the prorated refund of prepaid Fees allowed with specific termination rights given in the Agreement, Fees are non-refundable. For clarity, if Customer terminates an Order Form pursuant to Section 5.3 due to Provider's uncured material breach, Provider will pay to Customer a prorated refund of any prepaid Fees for the remainder of the Subscription Period, calculated from the effective date of termination."

**Proposed redline** (addition to Section 5.3): Add at the end of Section 5.3: "If Customer terminates an Order Form pursuant to this Section 5.3 due to Provider's material breach, Provider will pay to Customer a prorated refund of any prepaid Fees for the remainder of the Subscription Period."

**Rationale**: Where Customer terminates because Provider has failed to cure a material breach, Customer should not bear the cost of the unused subscription period. This is a basic commercial fairness provision and is consistent with the refund treatment the agreement already provides for warranty breach and force majeure terminations.

**Priority**: Must-have

---

### Section 6.3 / 6.4 — Provider's Warranty and Remedy Timeline

**Current language**: "Provider represents and warrants to Customer that it will not materially reduce the general functionality of the Cloud Service during the Subscription Period." (Section 6.3)

"If Provider breaches the warranty in Section 6.3, Customer must give Provider notice within 45 days of discovering the issue. Within 45 days of receiving sufficient details, Provider will attempt to restore the general functionality. If Provider cannot resolve the issue, Customer may terminate the affected Order Form and Provider will pay a prorated refund." (Section 6.4)

**Proposed redline** (Section 6.3): "Provider represents and warrants to Customer that during the Subscription Period, the Cloud Service will perform materially in accordance with the Documentation."

**Proposed redline** (Section 6.4): "If Provider breaches the warranty in Section 6.3, Customer will give Provider written notice within 30 days of discovering the non-conformance, describing the issue in reasonable detail. Within 30 days of receiving such notice, Provider will use commercially reasonable efforts to correct the non-conformance so that the Cloud Service performs materially in accordance with the Documentation. If Provider does not correct the non-conformance within the 30-day cure period, Customer may terminate the affected Order Form upon written notice and Provider will pay a prorated refund of any prepaid Fees for the remainder of the Subscription Period."

**Rationale**: The standard SaaS warranty commits the provider to performance in accordance with its own published documentation — an affirmative performance standard tied to the provider's own specifications. The current warranty merely commits Provider not to make the service worse, which does not cover performance that falls short of documented capabilities from the outset. Shortening the remedy timeline from 90 combined days to 60 combined days reflects the operational impact of a non-conforming service on Customer's internal operations.

**Priority**: Should-have

**Fallback**: If Provider insists on the existing warranty formulation (no material reduction in general functionality), accept it but negotiate the remedy timeline to 30 days' notice plus 30 days to cure instead of 45 plus 45.

---

### Section 1.5 — Customer Content License "Related Offerings" Extension

**Current language**: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings."

**Proposed redline**: "Provider may copy, display, modify, and use Customer Content solely as necessary to provide and maintain the Cloud Service as subscribed to by Customer under the applicable Order Form."

**Rationale**: The current "related offerings" extension is undefined and could be read to authorize use of Customer Content across any of Provider's current or future products and services. The proposed language ties the content license to the specific service Customer has contracted for, which is the standard market position.

**Priority**: Should-have

**Fallback**: If Provider needs "related offerings" for legitimate operational purposes (such as integrated analytics or support tools), define the term: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and any features or tools that are integral to the delivery of the Cloud Service ('Related Offerings'). 'Related Offerings' does not include Provider's other products or services that are not part of the subscribed Cloud Service."

---

### Section 12.6 — Assignment Without Consent in Change of Control

**Current language**: "No assignment without consent, except in merger/acquisition/change of control."

**Proposed redline**: "Neither party may assign this Agreement without the other party's prior written consent, not to be unreasonably withheld or delayed, except in connection with a merger, acquisition, corporate reorganization, or change of control, provided that: (a) the assigning party notifies the other party in writing within 30 days after the closing of the transaction; and (b) if Provider is acquired by, or merged with, an entity that is a direct competitor of Customer, or an entity that is subject to regulatory restrictions that would materially affect the processing of Customer Content, Customer may terminate this Agreement upon 60 days' written notice given within 90 days after receiving notice of the change of control, and Provider will pay a prorated refund of any prepaid Fees for the remainder of the Subscription Period."

**Rationale**: Given that assignment transfers the ML training rights, Customer Content licenses, and all data rights in this agreement, Customer should have the option to exit the relationship if Provider's acquirer creates a material conflict or data risk. The 90-day election window gives Customer adequate time to evaluate the implications without creating indefinite uncertainty for Provider.

**Priority**: Should-have

**Fallback**: If Provider will not accept the termination right, the minimum acceptable position is the 30-day notification requirement in subsection (a), without the termination trigger. This at least ensures Customer has visibility into ownership changes.

---

### Section 9 — Indemnification Scope (Cover Page Terms)

**Current language**: Both "Provider Covered Claims" and "Customer Covered Claims" are Cover Page variables. The substantive scope of indemnification is entirely undefined in the Standard Terms.

**Proposed Cover Page terms**:

- **Provider Covered Claims**: (a) Any claim that the Cloud Service, as provided by Provider and used by Customer in accordance with this Agreement, infringes or misappropriates a third party's intellectual property rights; and (b) any claim arising from Provider's breach of Section 3 (Privacy & Security) or Applicable Data Protection Laws with respect to Customer Content or Personal Data.
- **Customer Covered Claims**: Any claim arising from (a) Customer Content, including any claim that Customer Content infringes a third party's rights; or (b) Customer's use of the Cloud Service in breach of Section 2.1 (Restrictions on Customer).

**Rationale**: IP indemnification from the provider is a baseline expectation in SaaS agreements — Customer should not bear the risk that the service it is paying for infringes third-party rights. Adding data protection indemnification reflects the heightened importance of data security in this agreement. The Customer indemnification scope is standard and appropriately limited to matters within Customer's control.

**Priority**: Must-have

**Fallback**: If Provider will not accept data protection indemnification, the minimum acceptable position is IP indemnification alone for Provider Covered Claims: "Any claim that the Cloud Service, as provided by Provider and used by Customer in accordance with this Agreement and Documentation, infringes or misappropriates a third party's patent, copyright, trademark, or trade secret."

---

### Section 5.1 — Auto-Renewal Non-Renewal Notice Date

**Current language**: "automatically renew for additional Subscription Periods unless one party gives notice of non-renewal to the other party before the Non-Renewal Notice Date"

The Non-Renewal Notice Date is a Cover Page variable with no default or maximum in the Standard Terms.

**Proposed redline**: "automatically renew for additional Subscription Periods unless one party gives written notice of non-renewal to the other party at least 60 days before the end of the then-current Subscription Period"

**Rationale**: Specifying the non-renewal notice period directly in the Standard Terms prevents the Cover Page from setting an unreasonably long notice requirement that could lock Customer into an unwanted renewal. Sixty days is standard for mid-market SaaS agreements and gives both parties adequate planning time.

**Priority**: Should-have

**Fallback**: If Provider wants to retain the Cover Page variable, add a cap in the Standard Terms: "The Non-Renewal Notice Date will not be earlier than 90 days before the end of the then-current Subscription Period."

---

### Section 12.8 — Logo and Marketing Rights

**Current language**: "Provider may use Customer's name and logo in marketing."

**Proposed redline**: "Provider may include Customer's name in a list of customers on Provider's website or in Provider's sales materials. Any other use of Customer's name, logo, or trademarks — including in case studies, press releases, advertising, or social media — requires Customer's prior written approval. Customer may revoke this permission upon 30 days' written notice to Provider."

**Rationale**: Customer is willing to be identified as a Provider customer, which supports Provider's commercial interests. However, broader use of Customer's brand should be subject to approval to ensure accurate and appropriate representation. The revocation right provides Customer with an exit mechanism if circumstances change.

**Priority**: Nice-to-have

**Fallback**: "Provider may use Customer's name and logo in marketing. Customer may revoke this permission upon 30 days' written notice to Provider."

---

### Section 11.1 — Customer IP Ownership "Subject to" Qualification

**Current language**: "Customer retains all rights in Customer Content, subject to Sections 1.5 and 1.6."

**Proposed redline**: "As between the parties, Customer retains all right, title, and interest in and to Customer Content. Nothing in this Agreement transfers ownership of Customer Content to Provider. The limited licenses granted to Provider under Sections 1.5 and 1.6 do not diminish or qualify Customer's ownership of Customer Content."

**Rationale**: The proposed language clarifies that Customer's ownership of its content is unqualified and that the licenses to Provider are separate, limited grants rather than qualifications on ownership. This is the standard market formulation and eliminates the drafting ambiguity in the "subject to" construction. This is a clarification rather than a change in substantive position and should be straightforward to agree.

**Priority**: Should-have

**Fallback**: Not needed — this is a clarification of drafting that does not change the substantive rights of either party and should be acceptable as proposed.

---

### Section 5.6 — Survival of ML Training and Usage Data Rights

**Current language**: "The following sections will survive expiration or termination of the Agreement: Section 1.4 (Feedback and Usage Data), Section 1.6 (Machine Learning)..."

**Proposed redline**: Remove "Section 1.6 (Machine Learning)" from the list of surviving sections entirely. Modify the reference to Section 1.4 as follows: "Section 1.4 (Feedback and Usage Data) solely with respect to (i) Feedback voluntarily provided by Customer during the Subscription Period and (ii) Usage Data that was aggregated and de-identified in accordance with Section 1.4 during the Subscription Period..."

**Rationale**: Provider's rights to derive value from Customer's data should end when the commercial relationship ends. Feedback rights reasonably survive because Customer voluntarily provided the input. Usage Data rights may reasonably survive where the data has already been properly aggregated and de-identified. But open-ended survival of ML training rights over Customer Content is inconsistent with the principle of a clean break at termination. This redline should be negotiated as a package with the Section 1.6 redline.

**Priority**: Must-have (linked to the Section 1.6 redline)

---

### Absence of Disaster Recovery / Business Continuity Commitments (new Section 3.5 or Order Form)

**Current language**: No disaster recovery or business continuity provisions exist in the Standard Terms.

**Proposed redline** (new Section 3.5 or Order Form addendum):

"3.5 Disaster Recovery. Provider will maintain commercially reasonable disaster recovery and business continuity procedures for the Cloud Service, including regular backup of Customer Content at a frequency of no less than once per day. Provider will test its disaster recovery procedures at least annually. Upon Customer's written request, Provider will provide a summary description of its disaster recovery capabilities."

**Rationale**: For a platform supporting internal operations, baseline disaster recovery commitments provide Customer with assurance that Provider can recover from service disruptions. The proposed language sets a reasonable minimum without dictating specific technical approaches.

**Priority**: Should-have

**Fallback**: If Provider will not commit to specific backup frequency, accept a general commitment: "Provider will maintain commercially reasonable disaster recovery and business continuity procedures for the Cloud Service and will provide a summary description of such procedures upon Customer's written request."

---

### Absence of Change Management / Notification of Changes (new Section 1.2B or addition to Section 6.3)

**Current language**: No change notification provisions exist in the Standard Terms.

**Proposed redline** (new Section 1.2B):

"1.2B Changes to the Cloud Service. Provider will give Customer at least 30 days' advance written notice before making any material change to the Cloud Service that may adversely affect Customer's use, including deprecation of features, material changes to APIs, and changes to data formats or integrations. For deprecation of APIs or integrations on which Customer relies, Provider will use commercially reasonable efforts to provide at least 90 days' notice and, where feasible, maintain backward compatibility or provide a migration path."

**Rationale**: For a platform integrated into Customer's internal operations, advance notice of material changes is important for operational planning and continuity. This is standard practice for established SaaS providers and aligns with widely-accepted change management expectations.

**Priority**: Nice-to-have

**Fallback**: If Provider will not commit to specific notice periods, accept: "Provider will use commercially reasonable efforts to notify Customer in advance of material changes to the Cloud Service that may adversely affect Customer's use."

---

### Absence of Insurance Requirements (new Section 12.X)

**Current language**: No insurance requirements exist in the Standard Terms.

**Proposed redline** (new section in General Terms):

"12.18 Insurance. Provider will maintain, at its own expense, the following insurance coverage during the term of this Agreement: (a) commercial general liability insurance with a minimum limit of $1,000,000 per occurrence; (b) technology errors and omissions / professional liability insurance with a minimum limit of $2,000,000 per claim; and (c) cyber liability insurance with a minimum limit of $2,000,000 per claim. Provider will provide Customer with certificates of insurance upon written request."

**Rationale**: Insurance requirements provide Customer with assurance that Provider can satisfy claims, particularly in the event of a data breach or prolonged service failure. The proposed minimum amounts are reasonable for a mid-market SaaS provider and reflect standard procurement requirements.

**Priority**: Nice-to-have

**Fallback**: If Provider objects to specified minimums, accept a general commitment: "Provider will maintain commercially reasonable insurance coverage, including technology errors and omissions and cyber liability insurance, and will provide certificates of insurance upon Customer's written request."

---

### Absence of Data Portability / Export (addressed in Section 5.5 redline)

*This deviation is addressed in the Section 5.5 — Post-Termination Data Handling redline above, which includes a data export mechanism with a 30-day export period and standard format requirements.*

---

## Summary of Priority Designations

### Must-Have
- Section 1.6 — ML/AI Training Rights (Escalate)
- Section 2.1(a)(v) — Security Testing (Escalate)
- Absence of Security Commitments — new Section 3.2 (Escalate)
- Absence of Breach Notification — new Section 3.3 (Escalate)
- Section 2.2 — Suspension Rights (Escalate)
- Section 5.5 — Post-Termination Data Handling / Data Export (Escalate)
- Section 8.2 — Consequential Damages Waiver / Direct Lost Profits (Negotiate)
- Section 8.1 — Liability Cap Structure / Cover Page Terms (Negotiate)
- Sections 4.1 / 5.3 — Refund on Material Breach Termination (Negotiate)
- Section 9 — Indemnification Scope / Cover Page Terms (Negotiate)
- Section 5.6 — Survival of ML and Usage Data Rights (Negotiate, linked to 1.6)

### Should-Have
- Absence of SLA — new Section 1.2A (Escalate)
- Section 12.12 — Force Majeure Payment Carveout (Negotiate)
- Section 3.1 — GDPR-Only DPA Trigger (Negotiate)
- Absence of Subprocessor Controls — new Section 3.4 (Negotiate)
- Section 6.3 / 6.4 — Warranty and Remedy (Negotiate)
- Section 1.5 — Customer Content "Related Offerings" (Negotiate)
- Section 12.6 — Assignment / Change of Control (Negotiate)
- Section 5.1 — Auto-Renewal Notice Period (Negotiate)
- Section 11.1 — IP Ownership Clarification (Negotiate)
- Absence of DR/BC — new Section 3.5 (Negotiate)

### Nice-to-Have
- Section 12.8 — Logo and Marketing Rights (Negotiate)
- Absence of Change Management — new Section 1.2B (Negotiate)
- Absence of Insurance — new Section 12.18 (Negotiate)
