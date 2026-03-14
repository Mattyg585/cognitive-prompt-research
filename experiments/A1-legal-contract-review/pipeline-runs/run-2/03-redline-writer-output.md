# Redline Writer Output

**Important**: This analysis assists with legal workflows but does not constitute legal advice. All proposed language should be reviewed by qualified legal professionals before submission to the counterparty.

**Business context**: Customer side. $150K/year SaaS platform for internal operations. New vendor, not strategic but important. Standard procurement process. 2-week deadline. Data protection and IP ownership are priorities.

---

## Escalate Items

Escalate items are presented with proposed language representing the standard market position. However, each should be reviewed by senior counsel or the business sponsor before finalization. The counterparty may resist strongly on some of these, and the final position should reflect an organizational decision about acceptable risk.

---

### Machine Learning Training Rights Over Customer Content (Section 1.6)

**Current language**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes. However, (a) Usage Data and Customer Content must be aggregated before it can be used for these purposes, and (b) Provider will use commercially reasonable efforts consistent with industry standard technology to de-identify Usage Data and Customer Content before such use."

**Proposed redline**: "Provider may use Usage Data, in aggregated and de-identified form, to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services. Provider will not use Customer Content to develop, train, or enhance artificial intelligence or machine learning models. For purposes of this Section, 'de-identified' means that the data cannot reasonably be used to identify Customer, its Users, or any natural person. Provider will not make Usage Data or Customer Content available to third parties for the purpose of developing, training, or enhancing artificial intelligence or machine learning models. The rights granted under this Section 1.6 will terminate upon expiration or termination of this Agreement."

In addition, amend Section 5.6 (Survival) to remove the reference to Section 1.6:

**Current language in Section 5.6**: "The following sections will survive expiration or termination of the Agreement: Section 1.4 (Feedback and Usage Data), Section 1.6 (Machine Learning)..."

**Proposed redline for Section 5.6**: "The following sections will survive expiration or termination of the Agreement: Section 1.4 (Feedback and Usage Data), Section 2.1 (Restrictions on Customer)..." [removing Section 1.6 from the survival list]

**Rationale**: Customer Content should be used solely for delivering the contracted service. Provider's legitimate product improvement interests are preserved through access to aggregated, de-identified Usage Data. An outcome-based de-identification standard (rather than an effort-based one) provides meaningful protection. Restricting use to Provider's own models, rather than extending it to third-party components, keeps the data relationship within the contracted vendor. Terminating these rights at contract end is consistent with the principle that data use rights should track the commercial relationship.

**Priority**: Must-have

**Note**: This is an Escalate item. Senior counsel or the business sponsor should confirm the desired position before this redline is transmitted. Provider may view the ML training clause as commercially significant, and complete removal of Customer Content from ML use could be a material negotiation point. The proposed language is the standard market position but Provider's response will indicate whether a compromise (such as an opt-in mechanism with granular controls) is needed.

---

### Data Breach Notification (Absent — new provision)

**Current language**: No breach notification provision exists in the Standard Terms. Section 3 addresses only GDPR-governed Personal Data DPA requirements and Prohibited Data restrictions.

**Proposed redline** (new Section 3.3):

"**3.3 Security Incident Notification.** (a) Provider will notify Customer in writing without undue delay, and in any event within 72 hours of becoming aware, of any Security Incident. A 'Security Incident' means any unauthorized access to, acquisition of, use of, or disclosure of Customer Content or Personal Data processed under this Agreement, or any breach of Provider's security measures that compromises the confidentiality, integrity, or availability of Customer Content.

(b) Provider's notification will include, to the extent known at the time of notification: (i) the nature of the Security Incident, including the categories and approximate number of records affected; (ii) the likely consequences of the Security Incident; (iii) the measures taken or proposed to be taken to address the Security Incident, including measures to mitigate its effects; and (iv) a designated contact point for further information.

(c) Provider will cooperate with Customer's reasonable requests for additional information and will provide timely updates as additional facts become available. Provider will take commercially reasonable steps to contain, investigate, and remediate the Security Incident. Upon request, Provider will provide Customer with a root cause analysis and remediation report within 30 days of resolution of the Security Incident.

(d) Provider's notification obligations under this Section are not an acknowledgement of fault or liability."

**Rationale**: Customer may have its own notification obligations under data protection and industry regulations that depend on timely notice from its vendors. A 72-hour notification window aligns with GDPR's controller notification requirement and provides Customer with sufficient time to assess its own obligations. The specified notification content enables Customer to conduct its own impact assessment. The disclaimer that notification does not constitute admission of fault is standard and should reduce Provider's concern that prompt notification creates adverse legal exposure.

**Priority**: Must-have

**Note**: This is an Escalate item. The 72-hour timeline and scope of required disclosures should be confirmed by senior counsel. Depending on Customer's own regulatory obligations, a shorter or longer window may be appropriate. Provider may push for a longer notification window (e.g., "without undue delay" without a hard deadline) or narrower notification content.

---

### Service Level Agreement / Uptime Commitment (Absent — new provision)

**Current language**: No SLA exists in the Standard Terms. Section 1.2 states only: "During the Subscription Period, Provider will provide Technical Support as described in the Order Form." Section 6.3 provides that Provider "will not materially reduce the general functionality of the Cloud Service during the Subscription Period."

**Proposed redline** (new Section 1.2A, or as an Order Form schedule):

"**1.2A Service Levels.** (a) Provider will make the Cloud Service available at a rate of at least 99.5% measured on a monthly basis, excluding scheduled maintenance windows. 'Available' means the Cloud Service is accessible and performing materially in accordance with the Documentation.

(b) Provider will give Customer at least 48 hours' advance written notice of scheduled maintenance. Scheduled maintenance will be conducted outside Customer's primary business hours where commercially practicable.

(c) If availability falls below 99.5% in any calendar month, Customer will receive a service credit equal to 5% of the monthly Fees for each full percentage point below 99.5%, up to a maximum credit of 30% of the monthly Fees for that month. Service credits will be applied against the next invoice or, if no further invoices are due, refunded within 30 days. Service credits are Customer's sole and exclusive remedy for failure to meet the availability target in this Section 1.2A(a).

(d) If availability falls below 95% in any two of three consecutive calendar months, Customer may terminate the affected Order Form upon written notice and receive a prorated refund of prepaid Fees for the remainder of the Subscription Period.

(e) Provider will make availability reports available to Customer upon reasonable request, no more frequently than monthly."

**Rationale**: A SaaS platform used for internal business operations at this commitment level warrants defined availability standards with financial accountability. The 99.5% target is moderate and widely accepted for business SaaS. Service credits provide a proportionate financial remedy without requiring the escalation of a termination right for routine shortfalls. The termination trigger at sustained poor performance protects Customer against chronic underperformance.

**Priority**: Must-have

**Note**: This is an Escalate item. The specific uptime percentage, credit structure, and termination threshold should be reviewed by the business team and senior counsel. Provider may prefer to address SLA terms in the Order Form — this is acceptable provided the substantive commitments are secured. The goal is binding performance standards, not their specific document location.

---

### Audit Rights (Absent — new provision)

**Current language**: No audit provision exists. No mechanism for Customer to verify Provider's security, data handling, or compliance practices.

**Proposed redline** (new Section 3.4):

"**3.4 Audit and Compliance Verification.** (a) Provider will maintain industry-standard security certifications (SOC 2 Type II, ISO 27001, or equivalent) and will provide Customer with a copy of its most recent certification report upon request, no more frequently than annually.

(b) Upon Customer's reasonable request, no more than once per calendar year (or additionally where Customer has a reasonable basis to believe Provider has failed to comply with its obligations under this Agreement), Provider will make available information reasonably necessary to verify Provider's compliance with its security, data protection, and confidentiality obligations under this Agreement. At Customer's option, such verification may be conducted by a qualified independent third-party auditor, subject to reasonable confidentiality obligations and reasonable advance scheduling.

(c) Provider may satisfy its obligations under Section 3.4(b) by providing its most recent SOC 2 Type II audit report or equivalent independent assessment, provided such report is no more than 12 months old and covers the obligations in question.

(d) Each party will bear its own costs in connection with any audit or verification under this Section."

**Rationale**: For a platform handling internal operational data, Customer needs a contractual mechanism to verify Provider's security and compliance practices. The proposed language is balanced — it permits Provider to satisfy the obligation through independent certifications rather than on-site audits, limits frequency to avoid operational disruption, and allocates costs fairly.

**Priority**: Must-have

**Note**: This is an Escalate item. The audit right interacts with the security testing prohibition in Section 2.1(a)(v) and the absence of sub-processor controls. Senior counsel should consider whether these three gaps should be addressed as a coordinated package. Provider may resist any audit right; the independent certification alternative in subsection (c) provides a pragmatic fallback that most SaaS vendors can accommodate.

---

### Suspension Without Notice or Limitation (Section 2.2)

**Current language**: "If Customer (a) has an outstanding, undisputed balance on its account for more than 30 days; (b) breaches Section 2.1 (Restrictions on Customer); or (c) uses the Product in violation of the Agreement or in a way that materially and negatively impacts the Product or others, then Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical. Provider will reinstate Customer's access to the Product only if Customer resolves the underlying issue."

**Proposed redline**: "If Customer (a) has an outstanding, undisputed balance on its account for more than 30 days after written notice from Provider of such balance; (b) breaches Section 2.1 (Restrictions on Customer) in a manner that Provider reasonably determines poses an imminent risk to the security or integrity of the Product; or (c) uses the Product in a manner that Provider reasonably determines materially and negatively impacts the Product or other customers, then Provider may suspend Customer's access to the affected portion of the Product. Except where Provider reasonably determines that immediate suspension is necessary to prevent imminent harm to the security or integrity of the Product or to comply with Applicable Laws, Provider will provide Customer with at least 5 business days' prior written notice and an opportunity to cure before any suspension takes effect. Any suspension will be limited in scope to the affected portion of the Product or the affected Users where commercially practicable. Provider will promptly reinstate Customer's access upon Customer's cure of the underlying issue. If the underlying issue is not cured within 30 days of suspension, either party may terminate the affected Order Form upon written notice, and Provider will refund to Customer a prorated portion of prepaid Fees for the remainder of the Subscription Period following the date of suspension."

**Rationale**: The current language allows Provider to suspend access without notice, for an indefinite duration, with no proportionality requirement and no defined reinstatement process. For a platform integrated into Customer's internal operations, these procedural safeguards prevent suspension from functioning as an informal termination without the protections that the termination clause provides. The emergency exception preserves Provider's ability to act immediately on genuine security threats. The 30-day limit and termination right prevent indefinite suspension.

**Priority**: Must-have

**Note**: This is an Escalate item. The suspension clause creates an asymmetry with the termination provisions that warrants senior counsel review. Provider may resist the 5-business-day notice requirement. The proportionality principle (limiting suspension to affected portions) and the reinstatement deadline are the most commercially important elements.

---

## Negotiate Items

---

### Customer Content License to "Related Offerings" (Section 1.5)

**Current language**: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings."

**Proposed redline**: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Cloud Service as described in the applicable Order Form."

**Rationale**: Provider's license to Customer Content should be scoped to the specific service Customer has contracted for. The phrase "related offerings" is undefined and could extend Provider's license to products and services Customer has not purchased. Tying the license to the Cloud Service described in the Order Form provides a clear, bounded scope.

**Priority**: Must-have

**Fallback**: If Provider resists removing "related offerings" entirely, accept: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and any ancillary services identified in the applicable Order Form." This preserves scope limitation while allowing Provider to specify related services in a document Customer negotiates and signs.

---

### Termination for Convenience (Absent — new provision)

**Current language**: No termination for convenience exists for either party.

**Proposed redline** (new Section 5.3A):

"**5.3A Termination for Convenience.** Customer may terminate any Order Form for convenience upon 90 days' prior written notice to Provider. Upon termination for convenience, Provider will refund to Customer a prorated portion of any prepaid Fees corresponding to the remainder of the Subscription Period following the effective date of termination, less a termination fee equal to one month's Fees."

**Rationale**: For a new vendor relationship where platform fit has not been proven in Customer's environment, the ability to exit with reasonable notice mitigates the risk of being locked into a poor-fit vendor for the full subscription term. The 90-day notice period and one-month termination fee balance Customer's flexibility with Provider's revenue predictability.

**Priority**: Should-have

**Fallback**: If a general termination-for-convenience right is rejected, propose a one-time early termination right exercisable during the first 6 months of the initial Subscription Period, upon 60 days' written notice, with a prorated refund net of a termination fee equal to 2 months' Fees. This provides an early-exit window while limiting Provider's downside to a defined period.

---

### Data Return and Portability (Section 5.5)

**Current language**: "Upon Customer's request, Provider will delete Customer Content within 60 days."

**Proposed redline**: Replace Section 5.5(b) with:

"(b) For a period of 30 days following expiration or termination of an Order Form (the 'Retrieval Period'), Provider will, upon Customer's request, make Customer Content available for export in a standard, machine-readable format (such as CSV, JSON, or via API access). Provider will complete any such export within 15 business days of Customer's request.

(c) Following the expiration of the Retrieval Period, or upon Customer's earlier written request, Provider will delete all Customer Content in its possession or control, including copies maintained in backup systems, within 60 days and will certify such deletion in writing upon Customer's request.

(d) During the Retrieval Period, Provider will provide reasonable cooperation with Customer's data migration efforts at Provider's then-current professional services rates."

**Rationale**: For a platform used in internal business operations, the ability to retrieve data in a usable format at the end of the relationship is operationally essential. The current provision offers only deletion, which means Customer loses access to data it generated and owns. The proposed sequence — retrieval window, then deletion with certification — provides an orderly transition. Transition assistance at standard rates does not impose uncompensated burden on Provider.

**Priority**: Must-have

**Fallback**: If the transition assistance provision (subsection (d)) is rejected, the data export right and certified deletion are the essential elements. Accept removal of the transition cooperation clause to secure the export and deletion provisions.

---

### Security Testing Prohibition (Section 2.1(a)(v))

**Current language**: "conduct security or vulnerability tests on, interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product"

**Proposed redline**: "conduct security or vulnerability tests on the Product without Provider's prior written consent (such consent not to be unreasonably withheld or delayed for assessments conducted by a qualified third-party assessor using industry-standard methodologies and with reasonable advance notice to Provider), interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product. Upon Customer's reasonable request, no more than once per year, Provider will provide Customer with a summary of Provider's most recent independent penetration test results or equivalent security assessment."

**Rationale**: An absolute prohibition on security testing, combined with the absence of audit rights, leaves Customer with no mechanism to assess Provider's security posture. The proposed language permits coordinated testing with Provider's consent and requires Provider to share independent assessment results. Both mechanisms are standard in mid-market SaaS procurement.

**Priority**: Should-have

**Fallback**: If the right to conduct testing (even with consent) is rejected, the provision of independent security assessment results is the minimum acceptable alternative. This can be bundled with the audit rights provision as a single security assurance package.

---

### Provider Warranty Scope and Remedy (Sections 6.3 and 6.4)

**Current language (Section 6.3)**: "Provider represents and warrants to Customer that it will not materially reduce the general functionality of the Cloud Service during the Subscription Period."

**Current language (Section 6.4)**: "If Provider breaches the warranty in Section 6.3, Customer must give Provider notice within 45 days of discovering the issue. Within 45 days of receiving sufficient details, Provider will attempt to restore the general functionality. If Provider cannot resolve the issue, Customer may terminate the affected Order Form and Provider will pay a prorated refund."

**Proposed redline (Section 6.3)**: "Provider represents and warrants to Customer that the Cloud Service will perform materially in accordance with the Documentation during the Subscription Period."

**Proposed redline (Section 6.4)**: "If Provider breaches the warranty in Section 6.3, Customer must give Provider notice within 45 days of discovering the issue. Within 30 days of receiving Customer's notice with sufficient details to identify the nonconformity, Provider will use commercially reasonable efforts to correct the nonconformity. If Provider does not resolve the issue within such 30-day period, Customer may terminate the affected Order Form and Provider will pay a prorated refund of any prepaid Fees for the remainder of the Subscription Period."

**Rationale**: Performance against published documentation is the standard warranty for SaaS products and provides an objective, verifiable standard. The current warranty — a commitment not to reduce existing functionality — sets no affirmative performance obligation and provides no recourse for a service that simply fails to work as described. Reducing the cure period from 45 to 30 days brings the total resolution timeline (45 days notice + 30 days cure = 75 days) to a more commercially reasonable window.

**Priority**: Should-have

**Fallback**: If "materially in accordance with the Documentation" is rejected, propose "materially in accordance with the service description in the applicable Order Form." The goal is an objective, verifiable performance standard, not the specific reference document. Retain the 30-day cure period as a separate ask from the warranty standard.

---

### Direct Lost Profits Exclusion (Section 8.2)

**Current language**: "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."

**Proposed redline**: "Neither party will be liable for consequential, special, indirect, exemplary, punitive, or incidental damages, including indirect lost profits or revenues, even if informed of the possibility."

**Rationale**: The standard market formulation of a consequential damages waiver excludes indirect and consequential damages. The explicit inclusion of "whether direct or indirect" for lost profits goes beyond market standard by eliminating direct, foreseeable, and calculable revenue losses that would ordinarily be recoverable in a breach of contract claim. Removing the parenthetical restores the standard position while preserving the mutual waiver of consequential damages.

**Priority**: Should-have

**Fallback**: If Provider resists removing direct lost profits from the exclusion across the board, propose a carve-out for losses arising from Provider's breach of data protection obligations (including any DPA) or confidentiality obligations. This preserves a damages pathway for Customer's stated priority areas while maintaining the mutual exclusion for other categories.

---

### Logo and Marketing Rights (Section 12.8)

**Current language**: "Provider may use Customer's name and logo in marketing."

**Proposed redline**: "Provider may include Customer's name in Provider's customer list. Any other use of Customer's name, logo, or trademarks in marketing or promotional materials requires Customer's prior written consent."

**Rationale**: Customer should control the use of its brand in Provider's marketing. Inclusion in a customer list is standard and supports Provider's sales efforts without risk of unwanted brand association.

**Priority**: Nice-to-have

**Fallback**: Accept an opt-out mechanism: "Provider may use Customer's name and logo in marketing. Customer may opt out of such use at any time upon written notice to Provider, and Provider will cease such use within 30 days of receiving notice."

---

### Sub-processor / Subcontractor Governance (Absent — new provision)

**Current language**: No provision addresses sub-processors or subcontractors.

**Proposed redline** (new Section 3.5):

"**3.5 Subprocessors.** (a) Provider will maintain a list of subprocessors that process Customer Content or Personal Data under this Agreement and will make such list available to Customer upon request.

(b) Provider will notify Customer at least 30 days in advance of engaging any new subprocessor that will process Customer Content or Personal Data. If Customer objects to a new subprocessor on reasonable grounds within 15 days of receiving such notice, the parties will discuss Customer's concerns in good faith. If the parties cannot resolve the objection within 30 days, Customer may terminate the affected Order Form upon written notice and receive a prorated refund of prepaid Fees for the remainder of the Subscription Period.

(c) Provider will ensure that each subprocessor is bound by written obligations no less protective than those applicable to Provider under this Agreement with respect to Customer Content, Personal Data, and Confidential Information. Provider remains responsible for the acts and omissions of its subprocessors."

**Rationale**: Customer should know who processes its data and have a mechanism to raise concerns about changes to the processing chain. The advance notification and objection right are standard in SaaS agreements, particularly where data protection regulations require the controller to maintain oversight of its processing chain. Provider remains the accountable party, which is consistent with the bilateral commercial relationship.

**Priority**: Should-have

**Fallback**: If the objection and termination mechanism is rejected, the minimum acceptable position is transparency and contractual flow-down: (a) Provider maintains and shares a subprocessor list, (b) Provider provides advance notice of changes, and (c) subprocessors are bound by equivalent confidentiality and data protection obligations. Drop the objection right if necessary to secure these three elements.

---

### Data Processing Coverage Beyond GDPR (Section 3.1)

**Current language**: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider."

**Proposed redline**: "Before submitting Personal Data governed by Applicable Data Protection Laws, Customer and Provider will enter into a data processing agreement that addresses the requirements of all Applicable Data Protection Laws governing the processing of Personal Data under this Agreement, including (as applicable) GDPR, the California Consumer Privacy Act and California Privacy Rights Act, and other applicable data protection legislation. The terms of such data processing agreement are incorporated by reference into this Agreement."

**Rationale**: Data processing obligations should cover all applicable privacy regimes, not only GDPR. Customer may process data subject to CCPA/CPRA, state privacy laws, or other jurisdictional requirements that mandate specific contractual mechanisms. Incorporation by reference ensures the DPA has full contractual force within the Agreement.

**Priority**: Should-have

**Fallback**: If Provider resists a single comprehensive DPA, accept a structure where the existing GDPR DPA is supplemented by jurisdiction-specific addenda (e.g., a CCPA Service Provider Addendum). The key requirement is contractual coverage for all applicable privacy laws, not the document structure.

---

### Change of Control / Assignment to Competitor (Section 12.6)

**Current language**: "No assignment without consent, except in merger/acquisition/change of control."

**Proposed redline**: "Neither party may assign this Agreement without the other party's prior written consent, not to be unreasonably withheld. Notwithstanding the foregoing, either party may assign this Agreement without consent in connection with a merger, acquisition, corporate reorganization, or sale of all or substantially all of its assets, provided that the assigning party gives written notice to the other party within 30 days of the assignment. If the Agreement is assigned to a direct competitor of the non-assigning party, the non-assigning party may terminate this Agreement upon 60 days' written notice given within 90 days of receiving notice of the assignment, and Provider will refund to Customer a prorated portion of prepaid Fees for the remainder of the Subscription Period."

**Rationale**: An acquisition by a competitor raises concerns about operational data being accessible to a market rival. The termination right provides Customer with an exit path without requiring consent to the transaction itself. The 90-day exercise window gives Customer time to evaluate the change before committing to a decision.

**Priority**: Nice-to-have

**Fallback**: If the termination right is rejected, accept a notification requirement: the assigning party must notify the other party within 30 days of any assignment. Awareness of a change of control allows Customer to make operational decisions even without a contractual exit mechanism.

---

### Force Majeure Payment Asymmetry (Section 12.12)

**Current language**: "Neither party liable for delays from Force Majeure Events, except Customer's payment obligations."

The full contract text in Section 5.4 provides: "A Force Majeure Event does not excuse Customer's obligation to pay Fees accrued prior to termination."

**Proposed redline for Section 12.12**: "Neither party will be liable for delays or failures in performance resulting from Force Majeure Events. If a Force Majeure Event prevents Provider from delivering the Cloud Service for more than 5 consecutive business days, Customer's payment obligations will be suspended proportionally for the duration of the service interruption. For the avoidance of doubt, Customer remains obligated to pay Fees accrued prior to the commencement of the Force Majeure Event."

**Rationale**: Requiring Customer to pay full fees during a period when Provider cannot deliver the service due to force majeure creates a one-sided allocation of risk. Proportional fee suspension during extended outages is fair to both parties — Provider is not penalized for brief interruptions, but Customer is not required to pay indefinitely for a service that is not being delivered.

**Priority**: Nice-to-have

**Fallback**: If proportional fee suspension is rejected, accept a service credit mechanism: Customer receives service credits for any day during a Force Majeure Event on which the Cloud Service is unavailable, applied against future invoices. This is less favorable than suspension but still provides some financial recognition that service was not delivered.

---

### Price Protection on Renewal (Absent — new provision)

**Current language**: No provisions address pricing upon renewal. No caps, no advance notice, no protections against price increases.

**Proposed redline** (add to Section 5.1 or as an Order Form term):

"Provider will provide Customer with written notice of any change to Fees at least 60 days before the Non-Renewal Notice Date for the applicable renewal Subscription Period. Fee increases for renewal Subscription Periods will not exceed the greater of (a) 5% of the prior Subscription Period's Fees or (b) the percentage increase in the Consumer Price Index (All Urban Consumers) published by the U.S. Bureau of Labor Statistics for the 12-month period ending closest to 60 days before the renewal date. If the proposed Fee increase exceeds these limits, Customer may terminate the applicable Order Form by giving notice of non-renewal within 30 days of receiving the pricing notice."

**Rationale**: Pricing predictability is important for budgeting, and advance notice of changes before the non-renewal deadline ensures Customer can make an informed renewal decision. The cap provides protection against arbitrary increases while allowing Provider to adjust pricing with inflation or reasonable business growth.

**Priority**: Nice-to-have

**Fallback**: If a price cap is rejected, the advance pricing notice requirement is the essential element. Accept: "Provider will provide Customer with written notice of Fees for any renewal Subscription Period at least 60 days before the applicable Non-Renewal Notice Date." This ensures Customer always knows the renewal price before the window to decline renewal closes.

---

### User Account Liability (Section 1.3)

**Current language**: "Customer is responsible for all actions on Users' accounts and for all Users' compliance with this Agreement."

**Proposed redline**: "Customer is responsible for (a) maintaining reasonable access controls for Users' accounts, including requiring strong passwords and promptly deactivating accounts of Users who no longer require access, and (b) actions taken by Users that Customer has authorized to access the Product through Customer's account. Customer will not be responsible for unauthorized actions on Users' accounts resulting from a compromise of Provider's systems or a Security Incident as defined in Section 3.3."

**Rationale**: Unqualified liability for all user actions, regardless of Customer's knowledge or control, is broader than market standard. Customer should be responsible for exercising reasonable oversight, but should not bear liability for actions resulting from security failures on Provider's side. This qualified approach incentivizes both parties to maintain appropriate security measures.

**Priority**: Nice-to-have

**Fallback**: If Provider resists the qualified responsibility framework, accept a narrower revision: "Customer is responsible for all authorized actions on Users' accounts and for all Users' compliance with this Agreement. Customer will use reasonable security measures to protect the confidentiality of User credentials." This preserves Customer's general responsibility while adding the qualifier "authorized" to exclude compromised-account scenarios.

---

### Entire Agreement / Purchase Order Rejection (Section 12.1)

**Current language**: "Provider rejects terms in Customer's purchase orders."

**Proposed redline**: "This Agreement, including all Order Forms and any DPA, constitutes the entire agreement between the parties regarding its subject matter and supersedes all prior or contemporaneous agreements, representations, or understandings. To the extent Customer's purchase order includes terms addressing data protection, security standards, audit rights, or insurance requirements that are not addressed in this Agreement, such terms will be deemed incorporated into the applicable Order Form unless they directly conflict with the Standard Terms."

**Rationale**: A blanket rejection of purchase order terms removes a mechanism that often fills gaps in the vendor's standard terms. Given the absences identified in this review (breach notification, audit rights, sub-processor controls), Customer's standard procurement terms may provide protections that the Standard Terms do not. The proposed language preserves the entire agreement principle while allowing purchase order terms to supplement — not override — the Agreement on specific topics.

**Priority**: Nice-to-have

**Fallback**: If Provider insists on the blanket purchase order rejection, this becomes a lower-priority item provided the substantive gaps (breach notification, audit rights, sub-processor controls, security assurance) are addressed through the specific redlines proposed above. If those gaps are filled, the purchase order rejection is less consequential. If they are not filled, this provision becomes more important as a fallback mechanism.

---

## Summary of Redline Priorities

### Must-have (5 items)
1. Machine Learning Training Rights (Section 1.6) — remove Customer Content from ML training, end-date the rights, require outcome-based de-identification
2. Data Breach Notification (new Section 3.3) — 72-hour notification, defined disclosure content, cooperation and remediation obligations
3. Service Level Agreement (new Section 1.2A) — 99.5% availability target, service credits, termination right for sustained underperformance
4. Audit Rights (new Section 3.4) — annual verification right, satisfiable through SOC 2 Type II or equivalent
5. Suspension Safeguards (Section 2.2) — advance notice, proportionality, defined reinstatement, 30-day cap
6. Customer Content License Scope (Section 1.5) — remove "related offerings," scope to contracted Cloud Service
7. Data Return and Portability (Section 5.5) — export in machine-readable format before deletion, certified deletion

### Should-have (7 items)
1. Termination for Convenience (new Section 5.3A) — 90-day notice, prorated refund less one-month fee
2. Security Testing (Section 2.1(a)(v)) — consent-based testing right, annual security assessment reports
3. Provider Warranty (Sections 6.3/6.4) — performance against Documentation, 30-day cure period
4. Direct Lost Profits (Section 8.2) — remove "whether direct or indirect" parenthetical
5. Sub-processor Governance (new Section 3.5) — list, advance notice, objection right, contractual flow-down
6. Data Processing Beyond GDPR (Section 3.1) — extend DPA to all Applicable Data Protection Laws
7. Liability Caps (Cover Page terms) — 12-month fee-based caps, 2x for Increased Claims, defined categories

### Nice-to-have (6 items)
1. Logo and Marketing Rights (Section 12.8) — consent for use beyond customer list
2. Change of Control (Section 12.6) — termination right on assignment to competitor
3. Force Majeure Payment (Section 12.12) — proportional fee suspension during extended outages
4. Price Protection on Renewal (new Order Form term) — advance pricing notice and increase cap
5. User Account Liability (Section 1.3) — qualified responsibility for authorized actions
6. Entire Agreement / Purchase Orders (Section 12.1) — allow supplemental purchase order terms on unaddressed topics
