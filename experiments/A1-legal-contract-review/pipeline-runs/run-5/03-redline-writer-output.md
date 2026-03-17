**Important: This document assists with legal workflows but does not constitute legal advice. All proposed redlines should be reviewed by qualified legal professionals before submission.**

# Redline Proposals

This is a $150K/year SaaS platform from a new vendor going through standard procurement. The relationship is commercial, not strategic — the vendor is important but not a long-term partner where concessions buy relationship capital. Data protection and IP ownership are the stated priorities. The two-week deadline means the redline package needs to be tight and defensible, not aspirational. The proposals below are calibrated accordingly: firm on data and liability substance, straightforward on operational terms, and realistic about what a new vendor will accept in a standard procurement cycle.

---

## Escalate Items

*These require senior review before finalizing the redline position. The proposed language below represents a commercially reasonable starting point, but the appropriate position may differ based on internal risk tolerance and strategic considerations.*

### Section 1.6 — Machine Learning Training Rights

**Current language**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes. However, (a) Usage Data and Customer Content must be aggregated before it can be used for these purposes, and (b) Provider will use commercially reasonable efforts consistent with industry standard technology to de-identify Usage Data and Customer Content before such use."

**Proposed redline**: "Usage Data (but not Customer Content) may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services. Customer Content may not be used for such purposes unless Customer provides prior written opt-in consent on the applicable Order Form. For any permitted use under this Section, Provider must de-identify the data such that it cannot reasonably be used to identify Customer, Users, or any individual, and Provider will certify upon Customer's request that de-identification has been completed. The rights granted under this Section do not extend to third-party components of the Product unless the third party is bound by data protection obligations no less protective than those in this Agreement. The authorisations granted under this Section terminate upon expiration or termination of the Agreement; Provider may retain models trained prior to termination but may not use Customer Content or Usage Data for new training after the Agreement ends."

**Rationale**: The current provision grants broad rights over Customer Content for ML training purposes with an effort-based de-identification standard. Industry practice increasingly limits ML training to usage telemetry, requires outcome-based de-identification, and provides customers with opt-in controls. The proposed language preserves Provider's ability to improve its products using Usage Data while giving Customer meaningful control over how its substantive content is used. The post-termination limitation ensures the authorisation does not outlive the commercial relationship indefinitely.

**Priority**: Must-have

### Sections 7–8 — Liability Framework

**Current language**: "Each party's total cumulative liability for all claims will not be more than the General Cap Amount." / "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."

**Proposed redline**: Add the following as Section 8.1(c): "Unless otherwise specified on the Cover Page, the General Cap Amount will be the total Fees paid or payable by Customer during the twelve (12) months preceding the event giving rise to the claim. The Increased Cap Amount will be two (2) times the General Cap Amount. Provider's breach of Section 3 (Privacy & Security), Section 10 (Confidentiality), and Provider's indemnification obligations under Section 9 will be designated as Increased Claims."

Revise Section 8.2 to read: "Neither party will be liable for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility. This Section 8.2 does not apply to direct lost profits or revenues arising from Provider's breach of this Agreement."

**Rationale**: The Standard Terms establish a liability architecture where all material amounts are Cover Page variables. Setting default values in the Standard Terms ensures the Customer has a defined liability floor regardless of how the Cover Page is completed, and designating data and confidentiality breaches as Increased Claims reflects the allocation appropriate for a data-handling platform. Preserving direct lost profits is consistent with standard enterprise practice — most agreements waive only indirect or consequential lost profits.

**Priority**: Must-have

### Section 2.2 — Suspension Rights

**Current language**: "Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical. Provider will reinstate Customer's access to the Product only if Customer resolves the underlying issue."

**Proposed redline**: "Provider may temporarily suspend Customer's access to the Product only after providing Customer with five (5) business days' prior written notice and an opportunity to cure, except where Provider reasonably determines that immediate suspension is necessary to prevent imminent harm to the Product, other customers, or third parties, or to comply with Applicable Laws. In the case of immediate suspension, Provider will notify Customer in writing within twenty-four (24) hours of the suspension, including a description of the basis for suspension and the steps required for reinstatement. Provider will reinstate Customer's access within two (2) business days after Customer resolves the underlying issue. If suspension continues for more than fifteen (15) consecutive business days, Customer may terminate the affected Order Form and receive a prorated refund of prepaid Fees for the remainder of the Subscription Period."

**Rationale**: The current language permits suspension without notice or cure period, which for an operational SaaS platform creates business continuity risk disproportionate to the underlying triggers. The proposed language preserves Provider's ability to act immediately in genuine emergencies while ensuring that routine disputes (billing, usage disagreements) follow a notice-and-cure process consistent with enterprise SaaS standards. The reinstatement timeline and extended-suspension termination right prevent suspension from becoming a de facto termination without the refund and data-return protections that termination requires.

**Priority**: Must-have

### Privacy & Security — Security Commitments (new provision)

**Current language**: No security obligations appear in the Standard Terms.

**Proposed redline**: Add as Section 3.3: "Provider will maintain administrative, technical, and physical safeguards designed to protect Customer Content and Usage Data against unauthorized access, destruction, loss, alteration, or disclosure. These safeguards will be consistent with industry standards and will include, at a minimum: (a) maintenance of SOC 2 Type II certification (or a substantially equivalent third-party audit) covering the systems used to process Customer Content; (b) encryption of Customer Content in transit and at rest using industry-standard protocols; (c) access controls limiting Provider personnel access to Customer Content to those with a business need; and (d) annual third-party penetration testing. Provider will make its most recent SOC 2 Type II report and penetration test executive summary available to Customer upon request, subject to Provider's reasonable confidentiality requirements."

**Rationale**: An enterprise cloud platform processing customer data at this price point is reasonably expected to maintain and demonstrate baseline security standards. SOC 2 Type II is the accepted baseline for SaaS providers. The proposed language establishes a contractual security floor without imposing prescriptive technical requirements that may not align with Provider's architecture.

**Priority**: Must-have

### Privacy & Security — Breach Notification (new provision)

**Current language**: No breach notification obligations exist in the Standard Terms.

**Proposed redline**: Add as Section 3.4: "Provider will notify Customer in writing without undue delay, and in any event within seventy-two (72) hours, after becoming aware of any Security Incident affecting Customer Content or Customer's Usage Data. 'Security Incident' means any unauthorized access to, acquisition of, or disclosure of Customer Content or Usage Data. The notification will include: (a) a description of the nature of the Security Incident, including the categories and approximate volume of data affected; (b) the likely consequences of the Security Incident; (c) the measures taken or proposed to address the Security Incident and mitigate its effects; and (d) a designated contact for further information. Provider will cooperate with Customer's reasonable investigation of any Security Incident and will provide updates as material new information becomes available."

**Rationale**: Breach notification is a baseline expectation in enterprise SaaS agreements. The 72-hour timeline aligns with GDPR requirements and is widely adopted as an industry standard regardless of whether Personal Data is involved. The proposed language ensures the Customer is notified of incidents affecting any data entrusted to the platform, not just data that qualifies as Personal Data under applicable privacy law.

**Priority**: Must-have

### Service Levels — SLA Framework (new provision or Order Form reference)

**Current language**: No SLA, uptime commitment, or performance standards appear in the Standard Terms.

**Proposed redline**: Add as Section 1.7: "Provider will use commercially reasonable efforts to make the Cloud Service available at least 99.9% of the time during each calendar month, excluding scheduled maintenance windows of which Provider gives Customer at least forty-eight (48) hours' advance notice. If the Cloud Service falls below the availability commitment in any calendar month, Customer will be entitled to a service credit equal to the following percentage of the monthly Fees for the affected month: (a) 10% for availability between 99.0% and 99.9%; (b) 25% for availability between 95.0% and 99.0%; (c) 50% for availability below 95.0%. Service credits will be applied against the next invoice. Service credits are Customer's sole remedy for failure to meet the availability commitment and do not limit any other rights under this Agreement, including termination for material breach."

**Rationale**: A $150K/year operational SaaS platform requires a defined availability commitment. The 99.9% target with tiered service credits is standard for enterprise SaaS. The proposed language establishes a measurable standard with meaningful but proportionate financial consequences for downtime, while preserving the Customer's other contractual remedies for persistent or severe service failures.

**Priority**: Must-have

---

## Negotiate Items

### Sections 6.3–6.4 — Warranty Remedy Timeline

**Current language**: "Customer must give Provider notice within 45 days of discovering the issue. Within 45 days of receiving sufficient details, Provider will attempt to restore the general functionality."

**Proposed redline**: Replace Section 6.4 with: "If Provider breaches the warranty in Section 6.3, Customer must give Provider notice within thirty (30) days of discovering the issue. Within thirty (30) days of receiving sufficient details from Customer, Provider will restore the general functionality of the Cloud Service. During the cure period, if the breach materially impairs Customer's use of the Cloud Service, Fees for the affected Cloud Service will be abated proportionally to the impairment. If Provider does not resolve the issue within the thirty (30) day cure period, Customer may terminate the affected Order Form upon notice and Provider will pay a prorated refund of any prepaid Fees for the remainder of the Subscription Period."

**Rationale**: The current 90-day combined timeline (45 days to notify plus 45 days to cure) is approximately double the standard enterprise cure period for service degradation. Reducing each window to 30 days and adding fee abatement during the cure period ensures the Customer is not paying full price for a service acknowledged to be materially degraded. The total 60-day window remains generous relative to market practice.

**Priority**: Should-have

**Fallback**: Accept 30-day notice period with a 45-day cure period (75 days total instead of 90), and add fee abatement during the cure period even if the cure window is not shortened. The fee abatement is the more important protection — it creates an incentive for Provider to resolve issues promptly.

### Sections 5.5, 5.6 — Post-Termination Data Handling

**Current language**: "Upon Customer's request, Provider will delete Customer Content within 60 days." / "Each Recipient may retain Discloser's Confidential Information in accordance with its standard backup or record retention policies maintained in the ordinary course of business."

**Proposed redline**: Replace Section 5.5(b) with: "Provider will, at Customer's election, return Customer Content in a standard, machine-readable format or delete Customer Content, in either case within thirty (30) days of expiration or termination. If Customer does not make an election within fifteen (15) days of expiration or termination, Provider will delete Customer Content within thirty (30) days thereafter. Provider will certify in writing upon Customer's request that deletion has been completed."

Replace Section 5.6(b) with: "Each Recipient may retain Discloser's Confidential Information as required by Applicable Laws or applicable regulatory requirements, in which case Section 3 (Privacy & Security) and Section 10 (Confidentiality) will continue to apply to retained Confidential Information. Provider will delete such retained Confidential Information when the legal or regulatory requirement for retention has expired."

**Rationale**: Automatic deletion with an option to request return is the standard enterprise approach — it ensures data does not persist indefinitely due to an administrative oversight. Limiting the retention carve-out to legal and regulatory requirements (rather than open-ended "standard backup policies") prevents Provider from retaining data under internal policies that may not align with Customer's data governance requirements. The written certification of deletion provides verifiable assurance.

**Priority**: Should-have

**Fallback**: Accept the 60-day deletion timeline if Provider agrees to automatic deletion (without requiring Customer request) and limits the retention carve-out to data required by Applicable Laws. The certification of deletion is a standard ask and should not be conceded.

### Section 1.2 — Support Commitments

**Current language**: "Provider will provide Technical Support as described in the Order Form."

**Proposed redline**: Replace Section 1.2 with: "During the Subscription Period, Provider will provide Technical Support as described in the Order Form. At a minimum, Provider will provide: (a) business-hours support (Monday through Friday, 8:00 AM to 6:00 PM in Provider's primary time zone, excluding Provider's published holidays) via email and a web-based ticketing system; (b) initial response within four (4) business hours for issues that render the Cloud Service materially unusable (Severity 1), and within one (1) business day for all other issues; and (c) reasonable ongoing communication regarding the status and resolution of reported issues."

**Rationale**: While detailed support terms are commonly specified in the Order Form, establishing a minimum floor in the Standard Terms ensures the Customer has a baseline support commitment even if the Order Form is thin on support specifics. The proposed minimums are intentionally modest — they set a floor, not a ceiling.

**Priority**: Should-have

**Fallback**: Remove the minimum support terms from the Standard Terms, but require the following language: "Provider will provide Technical Support as described in the Order Form. The Order Form will specify, at minimum, support hours, initial response times by severity level, and available support channels." This ensures the Order Form negotiation addresses support even if the Standard Terms do not contain substantive minimums.

### Section 4 — Payment Terms and Non-Refundable Fees

**Current language**: "Except for the prorated refund of prepaid Fees allowed with specific termination rights given in the Agreement, Fees are non-refundable." / "Customer must notify Provider about the dispute before payment is due."

**Proposed redline**: Revise Section 4.1 to read: "...Fees are non-refundable except (a) as expressly provided in this Agreement, or (b) in the event of a material failure of the Cloud Service to perform in substantial conformity with the Documentation for a period of five (5) or more consecutive business days, in which case Customer will be entitled to a prorated credit for the period of non-conformity."

Revise Section 4.6 to read: "If Customer has a good-faith disagreement about the Fees charged or invoiced, Customer must notify Provider about the dispute within thirty (30) days of the invoice date or automatic charge, and must pay all undisputed amounts on time."

**Rationale**: The non-refundability provision, in the absence of an SLA with service credits, leaves the Customer without fee-based recourse for service failures short of termination. Adding a credit mechanism for documented outages provides an intermediate remedy. The dispute timeline revision to 30 days post-invoice aligns with standard commercial practice and gives the Customer adequate time to review charges.

**Priority**: Should-have

**Fallback**: If the SLA with service credits (proposed above) is accepted, the fee credit provision in Section 4.1 becomes less critical — the SLA service credits serve a similar function. In that case, accept the non-refundability provision as-is but insist on the 30-day dispute timeline revision.

### Section 5.1 — Auto-Renewal and Non-Renewal Notice

**Current language**: "...automatically renew for additional Subscription Periods unless one party gives notice of non-renewal to the other party before the Non-Renewal Notice Date."

**Proposed redline**: "...automatically renew for additional Subscription Periods of equal length unless one party gives written notice of non-renewal to the other party at least sixty (60) days before the end of the then-current Subscription Period."

**Rationale**: Defining the non-renewal notice period in the Standard Terms rather than leaving it as a Cover Page variable eliminates the risk of an unexpectedly long notice requirement. Sixty days is standard for enterprise SaaS agreements and gives both parties adequate planning time without locking the Customer into decisions six or more months in advance.

**Priority**: Nice-to-have

**Fallback**: Accept the Cover Page variable approach, but confirm in the Cover Page that the Non-Renewal Notice Date is no more than 90 days before the end of the Subscription Period.

### Section 12.8 — Logo Rights

**Current language**: "Provider may use Customer's name and logo in marketing."

**Proposed redline**: "Provider may use Customer's name and logo in marketing materials, including Customer lists and case studies, only with Customer's prior written consent. Customer may withdraw consent at any time upon thirty (30) days' written notice."

**Rationale**: Brand and trademark usage by third parties is a standard area of customer control. Prior consent with a withdrawal mechanism is the accepted enterprise practice and is a routine ask.

**Priority**: Nice-to-have

**Fallback**: "Provider may use Customer's name and logo in Customer lists and on Provider's website. Use of Customer's name or logo in case studies, press releases, or other promotional materials requires Customer's prior written consent." This permits basic customer-list usage (which most vendors expect) while preserving consent requirements for substantive marketing use.

### Section 12.6 — Assignment and Change of Control

**Current language**: "No assignment without consent, except in merger/acquisition/change of control."

**Proposed redline**: Replace Section 12.6 with: "Neither party may assign or transfer this Agreement without the other party's prior written consent, not to be unreasonably withheld. Notwithstanding the foregoing, either party may assign this Agreement in connection with a merger, acquisition, corporate reorganization, or sale of all or substantially all of its assets, provided that (a) the assignee assumes all obligations under this Agreement, and (b) Customer may terminate this Agreement upon sixty (60) days' written notice if Provider is acquired by, merged with, or otherwise comes under the control of an entity that is a direct competitor of Customer or that Customer reasonably determines presents a material data security or reputational concern. In the event of such termination, Provider will pay a prorated refund of any prepaid Fees for the remainder of the Subscription Period."

**Rationale**: Symmetric change-of-control assignment without consent is standard in vendor templates but presents a specific risk for the Customer: the Customer's data (including any ML training authorisations) would transfer to an acquirer that may be a competitor or may have different data practices. A termination right on Provider change of control is a standard enterprise negotiation ask and is particularly relevant given the data rights provisions in this Agreement.

**Priority**: Should-have

**Fallback**: Rather than a broad termination right, narrow the trigger to acquisition by a Customer competitor: "Customer may terminate this Agreement upon sixty (60) days' written notice if Provider is acquired by or merged with an entity that directly competes with Customer's primary line of business." This is a narrower, more defensible ask that addresses the most concrete risk.

### Section 2.1(a)(v) — Security Testing Prohibition

**Current language**: "conduct security or vulnerability tests on, interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product"

**Proposed redline**: Replace Section 2.1(a)(v) with: "(v) interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product. Notwithstanding the foregoing, Customer may conduct security or vulnerability assessments of the Product upon providing Provider with at least fifteen (15) business days' advance written notice and coordinating the scope and timing with Provider. Alternatively, Provider will, upon Customer's request and no more than once per twelve-month period, make available a summary of its most recent third-party penetration test results, subject to Provider's reasonable confidentiality requirements."

**Rationale**: The blanket prohibition on security testing, combined with the absence of security commitments or audit rights, prevents the Customer from verifying the security of a platform that holds its data. Permitting coordinated testing or providing third-party test results is standard enterprise practice and is consistent with the security commitments proposed above. The coordination requirement protects Provider from disruptive testing while giving Customer a meaningful verification path.

**Priority**: Should-have

**Fallback**: If Provider will not agree to customer-initiated testing, accept the penetration test summary alternative alone — but make it mandatory rather than optional: "Provider will, upon Customer's request and no more than once per twelve-month period, provide a summary of its most recent third-party penetration test results covering the systems used to process Customer Content."
