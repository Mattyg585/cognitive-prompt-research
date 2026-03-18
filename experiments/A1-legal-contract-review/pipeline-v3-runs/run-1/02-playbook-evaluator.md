# Playbook Evaluator — Stage 2 Output

**Review basis**: Generic widely-accepted commercial standards for a $150K/year SaaS subscription agreement. No organizational playbook was provided. All "standard positions" referenced below reflect market norms for mid-market SaaS procurement by a Customer, not any specific organization's negotiation playbook.

**Business context**:
- **User's side**: Customer
- **Deal size**: $150K/year SaaS subscription
- **Deadline**: 2 weeks
- **Strategic importance**: Standard operational tool
- **Relationship**: New vendor relationship

---

## Deviation Analysis

### 1. Machine Learning / AI Training Rights over Customer Content (Section 1.6)

**Classification**: Escalate

**Contract provision**: Provider may use both Usage Data and Customer Content to develop, train, or enhance AI/ML models that are part of Provider's products and services, including third-party components. Customer "authorizes Provider to process its Usage Data and Customer Content for such purposes." The provision survives termination. De-identification is on a "commercially reasonable efforts" standard, not a results-based guarantee. Third-party model training is included.

**Standard market position**: For a $150K/year operational SaaS agreement, the standard market position is that Customer Content is used solely to provide the contracted service. Usage Data (metadata, telemetry) may be used for product improvement in aggregated, de-identified form. Training AI/ML models on Customer Content — particularly for third-party components and surviving termination — is not a standard grant at this deal size. Where ML training rights exist, they are typically limited to Usage Data only, require opt-in consent, or include a meaningful opt-out mechanism.

**Gap**: The contract grants ML training rights over Customer Content (not just Usage Data), extends those rights to third-party components, and makes the grant survive termination with no opt-out. The de-identification standard is effort-based, not outcome-based. This is a material departure from standard market positions for an operational SaaS tool. The Auditor's analysis of the interaction with Section 11.1 ("Customer retains all rights in Customer Content, subject to Sections 1.5 and 1.6") confirms this grant directly qualifies Customer's ownership rights.

**Redline**:
  - **Current language**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes."
  - **Proposed redline**: "Provider may use Usage Data, in aggregated and de-identified form, to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services. Provider shall not use Customer Content for the development, training, or enhancement of any AI or ML models. For clarity, this restriction includes third-party components of the Product. Provider's use of Usage Data for AI/ML purposes shall not survive expiration or termination of this Agreement."
  - **Rationale**: Customer Content processed through an operational SaaS platform may include commercially sensitive business data. Granting perpetual, broad ML training rights over that content — including to third-party model providers — is not commensurate with a standard subscription for an operational tool. Usage Data for product improvement is appropriate; Customer Content for model training is not.
  - **Priority**: Must-have
  - **Fallback**: Not appropriate for a must-have. If Provider insists on some ML use of Customer Content, escalate to senior business and legal stakeholders for a risk decision — this is not a term the negotiation team should concede at their level of authority.

---

### 2. Customer Content Use for "Related Offerings" (Section 1.5)

**Classification**: Negotiate

**Contract provision**: Provider may "copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings."

**Standard market position**: Provider's right to use Customer Content should be limited to providing and maintaining the specific contracted Cloud Service. The phrase "related offerings" is undefined and could extend Provider's use rights to other products in its portfolio or future products.

**Gap**: The inclusion of "and related offerings" extends Provider's use rights beyond the contracted service. Standard market language limits this to "provide and maintain the Cloud Service" or "provide the Product" without the "related offerings" extension.

**Redline**:
  - **Current language**: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings."
  - **Proposed redline**: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Cloud Service as described in the applicable Order Form."
  - **Rationale**: Customer Content rights should be scoped to the service Customer is paying for. Extending those rights to undefined "related offerings" creates ambiguity about the scope of Provider's use.
  - **Priority**: Should-have
  - **Fallback**: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product. For clarity, 'Product' does not include other products or services offered by Provider that are not part of Customer's subscription."

---

### 3. Service Level Agreement — Absence

**Classification**: Escalate

**Contract provision**: No SLA, no uptime commitment, no performance standards, no service credit mechanism anywhere in the Standard Terms. The only warranty is that Provider will "not materially reduce the general functionality of the Cloud Service" (Section 6.3).

**Standard market position**: A $150K/year SaaS subscription for an operational tool should include a measurable uptime commitment (typically 99.5% or higher), defined measurement methodology, and a service credit mechanism for failures to meet the SLA. This is standard at this price point and widely available from SaaS providers.

**Gap**: Complete absence. The combination of no SLA, no service credits, non-refundable fees, and the ability to suspend without credits means Customer has no measurable service commitment and no financial remedy short of termination for service quality issues.

**Redline**:
  - **Current language**: [No language — this is an absence]
  - **Proposed redline**: Add as a schedule or Order Form attachment:

    "**Service Level Agreement.** Provider shall make the Cloud Service Available (as measured by Provider's monitoring systems) at least 99.5% of the time during each calendar month, excluding scheduled maintenance windows for which Provider has given at least 48 hours' prior notice ('Uptime Commitment').

    If Provider fails to meet the Uptime Commitment in any calendar month, Customer shall receive a service credit equal to the following percentage of the monthly Fees for the affected Cloud Service:

    - Below 99.5% but at or above 99.0%: 5% credit
    - Below 99.0% but at or above 95.0%: 10% credit
    - Below 95.0%: 20% credit

    Service credits shall be applied against future invoices and shall not be refunded as cash. Service credits are Customer's sole financial remedy for failure to meet the Uptime Commitment and do not limit Customer's termination rights under the Agreement.

    If Provider fails to meet the Uptime Commitment for three or more months in any twelve-month period, Customer may terminate the affected Order Form upon 30 days' written notice and receive a prorated refund of prepaid Fees for the remainder of the Subscription Period."

  - **Rationale**: An operational SaaS tool at this price point requires measurable availability commitments. Without an SLA, Customer has no baseline for service expectations and no graduated remedy before the termination threshold.
  - **Priority**: Must-have
  - **Fallback**: Not appropriate for a must-have at this deal size and use case. If Provider refuses a formal SLA, escalate — proceeding without any uptime commitment for an operational tool at $150K/year is a business-level risk decision.

---

### 4. Suspension Without Notice or Credit (Section 2.2)

**Classification**: Negotiate

**Contract provision**: Provider may suspend access "with or without notice." The commitment to try to inform Customer is aspirational: "Provider will try to inform Customer before suspending Customer's account when practical." No provision for fee credits during suspension. No mechanism for Customer to dispute a suspension.

**Standard market position**: Suspension powers are standard but should include: (a) prior written notice except in genuine emergencies, (b) a clear and limited set of suspension grounds, (c) fee credits for any suspension not caused by Customer, and (d) a mechanism for Customer to cure and reinstate.

**Gap**: The contract allows suspension without notice, provides no fee credits, and has no dispute mechanism. The "materially and negatively impacts the Product or others" ground is subjective and Provider-determined with no objective standard.

**Redline**:
  - **Current language**: "Provider may temporarily suspend Customer's access to the Product with or without notice."
  - **Proposed redline**: "Provider may temporarily suspend Customer's access to the Product upon written notice to Customer, except where Provider reasonably determines that immediate suspension is necessary to prevent imminent harm to the security or integrity of the Cloud Service or to comply with applicable law. In the event of suspension not caused by Customer's breach of this Agreement or Customer's misuse of the Cloud Service, Customer's Fee obligations shall be reduced on a pro-rata basis for the period of suspension. Provider shall use commercially reasonable efforts to restore access promptly after the condition giving rise to the suspension has been resolved."
  - **Rationale**: Suspension without notice or credit shifts operational and financial risk entirely to Customer. A notice requirement with a narrow emergency exception, combined with fee relief for Provider-initiated suspensions, is standard market practice.
  - **Priority**: Should-have
  - **Fallback**: Accept Provider's suspension right as drafted but add: "In the event of any suspension lasting more than 5 consecutive business days that is not caused by Customer's breach, Customer may terminate the affected Order Form upon written notice and receive a prorated refund of prepaid Fees for the remainder of the Subscription Period."

---

### 5. Provider Warranty — Non-Degradation Only (Section 6.3)

**Classification**: Negotiate

**Contract provision**: Provider warrants only that it "will not materially reduce the general functionality of the Cloud Service during the Subscription Period." The warranty remedy requires Customer notice within 45 days of discovery, then Provider gets 45 days to cure. If unresolved, Customer may terminate for a prorated refund.

**Standard market position**: SaaS providers at this price point typically warrant that the Cloud Service will perform materially in accordance with the Documentation or published specifications. This is an affirmative performance commitment, not merely a promise not to degrade. The warranty remedy should include the option to terminate with a prorated refund, but the notice and cure windows (45 days each, totaling 90 days) are longer than market standard.

**Gap**: The warranty is a non-degradation commitment, not a performance commitment. Customer has no warranty-based recourse if the service simply does not work as documented from day one or if performance is poor but stable. The 90-day total notice-and-cure window is longer than the 30-day cure period for material breach.

**Redline**:
  - **Current language**: "Provider represents and warrants to Customer that it will not materially reduce the general functionality of the Cloud Service during the Subscription Period."
  - **Proposed redline**: "Provider represents and warrants to Customer that the Cloud Service will perform materially in accordance with the Documentation during the Subscription Period. Provider further warrants that it will not materially reduce the general functionality of the Cloud Service during the Subscription Period."
  - **Rationale**: A warranty tied to Documentation provides an objective, measurable standard. The non-degradation warranty addresses a different risk (Provider removing features) and should be retained alongside an affirmative performance warranty.
  - **Priority**: Should-have
  - **Fallback**: Accept the non-degradation warranty but reduce the remedy timeline: "Customer shall notify Provider within 45 days of discovery. Provider shall have 30 days from receipt of notice to restore conformance. If Provider fails to do so, Customer may terminate the affected Order Form and receive a prorated refund of prepaid Fees."

---

### 6. Security Obligations — Absence

**Classification**: Escalate

**Contract provision**: No security standards, no breach notification obligation (beyond what data protection law may require), no audit or assessment rights, no description of security practices.

**Standard market position**: A SaaS vendor handling operational data at $150K/year should commit to maintaining industry-standard security practices (typically SOC 2 Type II or equivalent), provide breach notification within a specified timeframe (24-72 hours is standard), and make audit reports or certifications available to Customer upon request.

**Gap**: Complete absence. Customer has no contractual assurance regarding how Provider protects Customer Content, no right to verify security practices, and no guaranteed breach notification timeline.

**Redline**:
  - **Current language**: [No language — this is an absence]
  - **Proposed redline**: Add as a new section or schedule:

    "**Security.** Provider shall maintain administrative, technical, and physical safeguards designed to protect Customer Content against unauthorized access, use, or disclosure, in accordance with industry-standard practices, including maintaining SOC 2 Type II certification (or equivalent) covering the Cloud Service.

    Provider shall make its most recent SOC 2 Type II report (or equivalent) available to Customer upon request, no more than once per twelve-month period, subject to Provider's reasonable confidentiality requirements.

    In the event Provider becomes aware of any unauthorized access to or acquisition of Customer Content ('Security Incident'), Provider shall: (a) notify Customer in writing within 72 hours of confirming the Security Incident; (b) investigate and take reasonable steps to mitigate the Security Incident; and (c) provide Customer with reasonable information regarding the nature and scope of the Security Incident as it becomes available."

  - **Rationale**: For an operational SaaS platform processing business data, contractual security commitments are a baseline expectation. The absence of any security obligations, breach notification, or audit rights is a material gap at this deal size.
  - **Priority**: Must-have
  - **Fallback**: Not appropriate for a must-have. If Provider cannot commit to specific certifications, at minimum require: (a) commercially reasonable security measures, (b) breach notification within 72 hours, and (c) annual provision of a security questionnaire or summary of practices. Escalate if Provider refuses all security commitments.

---

### 7. Consequential Damages Waiver Including Direct Lost Profits (Section 8.2)

**Classification**: Negotiate

**Contract provision**: "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages." The "whether direct or indirect" qualifier forecloses the argument that lost profits are direct damages.

**Standard market position**: A mutual consequential damages waiver is standard. However, explicitly waiving direct lost profits is more aggressive than typical. Many agreements waive "indirect, consequential, special, incidental, and punitive damages" and let direct damages (including direct lost profits) remain recoverable up to the liability cap.

**Gap**: The explicit inclusion of "lost profits or revenues (whether direct or indirect)" goes beyond the standard consequential damages waiver. For an operational tool, if Provider's failure causes Customer to lose revenue directly (e.g., the tool is down and Customer cannot process orders), that direct lost profit would be unrecoverable.

**Redline**:
  - **Current language**: "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."
  - **Proposed redline**: "Neither party will be liable for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility. The foregoing shall not limit either party's liability for direct damages, including direct lost profits, which shall remain subject to the applicable liability cap."
  - **Rationale**: A blanket waiver of all lost profits — including direct lost profits — leaves Customer with an unreasonably narrow recovery path for service failures affecting an operational tool. Direct lost profits should remain recoverable within the liability cap.
  - **Priority**: Should-have
  - **Fallback**: Accept the current waiver but add carveouts: "The limitations in this Section 8.2 shall not apply to: (a) Provider's breach of Section 10 (Confidentiality); (b) Provider's breach of its security obligations; or (c) Provider's indemnification obligations under Section 9."

---

### 8. Post-Termination Data Deletion (Section 5.5(b))

**Classification**: Negotiate

**Contract provision**: Provider must delete Customer Content within 60 days only "upon Customer's request." Section 5.6(b) permits retention per standard backup and retention policies. The ML training rights (Section 1.6) survive termination entirely.

**Standard market position**: Post-termination, Provider should return or delete Customer Content within 30 days, with an automatic deletion default (not requiring Customer to affirmatively request). Backup retention should have a defined maximum period (typically 90 days). A reasonable data export/portability period should precede deletion.

**Gap**: Deletion is request-dependent, not automatic. The 60-day window is longer than market standard. Backup retention is open-ended. There is no data export or portability provision. The ML training survival compounds the concern — even after deletion, Provider retains the benefit of models trained on Customer Content.

**Redline**:
  - **Current language**: "Upon Customer's request, Provider will delete Customer Content within 60 days."
  - **Proposed redline**: "Upon expiration or termination of the Agreement, Provider shall: (a) make Customer Content available for export in a standard, machine-readable format for a period of 30 days following the effective date of termination ('Export Period'); and (b) delete all Customer Content, including copies in backup systems, within 30 days following the end of the Export Period. Provider shall certify such deletion in writing upon Customer's request. Notwithstanding the foregoing, Provider may retain Customer Content as required by applicable law, provided that such retained data remains subject to the confidentiality obligations of this Agreement."
  - **Rationale**: An operational platform will accumulate substantial Customer Content. Automatic deletion with a preceding export window is the market standard approach. Request-dependent deletion with open-ended backup retention creates risk that Customer Content persists indefinitely.
  - **Priority**: Should-have
  - **Fallback**: Accept the 60-day deletion window but require: (a) deletion to be automatic (not request-dependent), (b) backup copies to be deleted within 90 days, and (c) a 30-day export period before deletion begins.

---

### 9. Non-Renewal Notice Date as Cover Page Variable (Section 5.1)

**Classification**: Negotiate

**Contract provision**: Auto-renewal unless notice is given before the Non-Renewal Notice Date, which is a Cover Page variable. Per Section 13.1, if not specified, it defaults to "none" or "not applicable."

**Standard market position**: A non-renewal notice period of 30-60 days before the end of the then-current term is standard. The notice period should be explicit in the agreement, not dependent on a Cover Page variable that could be left blank.

**Gap**: If the Cover Page does not populate this field, the agreement may auto-renew with no mechanism for non-renewal, effectively creating an evergreen contract. Even if the Cover Page is populated, the risk is that it is set at an unreasonably long notice period.

**Redline**:
  - **Current language**: [Cover Page variable — Non-Renewal Notice Date]
  - **Proposed redline**: Ensure the Cover Page specifies: "Non-Renewal Notice Date: 60 days prior to the end of the then-current Subscription Period." Additionally, add to Standard Terms: "If the Non-Renewal Notice Date is not specified on the Cover Page, either party may elect not to renew by providing written notice at least 60 days prior to the end of the then-current Subscription Period."
  - **Rationale**: A default non-renewal mechanism prevents accidental lock-in if the Cover Page is incomplete. Sixty days provides reasonable notice to both parties.
  - **Priority**: Should-have
  - **Fallback**: Accept Provider's structure but ensure the Cover Page is populated with no more than 90 days' notice. Flag for the business team to calendar the non-renewal date.

---

### 10. Indemnification Exclusion for "Combination with Non-Provider Items" (Section 9.5)

**Classification**: Negotiate

**Contract provision**: Provider's indemnification does not apply to claims arising from "combination with non-Provider items" or unauthorized modifications, unauthorized use, or use of outdated versions.

**Standard market position**: IP indemnification exclusions are standard, but the "combination with non-Provider items" exclusion should be limited to situations where the claim would not have arisen but for the combination. A blanket exclusion for any claim involving integrated products effectively guts the indemnification for any real-world deployment.

**Gap**: The exclusion as written could apply to virtually any IP claim in a production environment, since SaaS products are almost always used in combination with other systems. The standard market formulation limits this to claims that would not have arisen but for the combination.

**Redline**:
  - **Current language**: [Exclusion for claims arising from "combination with non-Provider items"]
  - **Proposed redline**: "Provider's obligations under Section 9 shall not apply to the extent a Covered Claim arises solely from: (a) modification of the Product by anyone other than Provider without Provider's written authorization; (b) Customer's use of the Product in breach of this Agreement; (c) Customer's continued use of a version of the Product after Provider has made available a non-infringing update at no additional cost; or (d) the combination of the Product with non-Provider items, but only to the extent the Covered Claim would not have arisen but for such combination."
  - **Rationale**: The "but for" standard is the market-standard formulation. It preserves Provider's protection against claims genuinely caused by third-party combinations while ensuring Provider's indemnification covers its own product's infringement.
  - **Priority**: Should-have
  - **Fallback**: Accept the current exclusion language but add: "For clarity, the exclusion in Section 9.5 for combination with non-Provider items shall not apply where the Covered Claim is based on the Product alone, without reference to its combination with other items."

---

### 11. Assignment in Change of Control Without Consent (Section 12.6)

**Classification**: Negotiate

**Contract provision**: Either party may assign the agreement in a merger, acquisition, or change of control without the other party's consent.

**Standard market position**: Assignment restrictions with a change-of-control exception are common, but for Customer, the risk is that Provider is acquired by a competitor or an entity Customer would not have contracted with — and the acquirer inherits all data rights, including ML training rights over Customer Content (per Sections 1.5 and 1.6). Market-standard protections include a Customer termination right upon Provider change of control, or at minimum, a notification requirement.

**Gap**: Customer has no consent right, no notification right, and no termination right triggered by Provider's change of control. Given the broad data rights in Sections 1.5 and 1.6, an acquirer could inherit rights to use Customer Content for ML training of the acquirer's products.

**Redline**:
  - **Current language**: [Assignment permitted in change of control without consent]
  - **Proposed redline**: "Either party may assign this Agreement in connection with a merger, acquisition, or sale of all or substantially all of its assets, provided that the assigning party gives the other party written notice at least 30 days prior to the effective date of such assignment. If Provider assigns this Agreement pursuant to this Section, Customer may terminate this Agreement upon 60 days' written notice given within 90 days following receipt of Provider's assignment notice, and Provider shall refund any prepaid Fees for the remainder of the Subscription Period on a prorated basis."
  - **Rationale**: A Customer termination right upon Provider change of control is a standard protection when the agreement includes broad data rights. Customer should have the option to exit the relationship rather than have its data rights transferred to an unknown acquirer.
  - **Priority**: Nice-to-have
  - **Fallback**: Accept no termination right but require: "Provider shall give Customer written notice within 30 days following any change of control. Upon Provider's change of control, the provisions of Sections 1.5 and 1.6 shall not extend to any products or services of the acquiring entity that are not the Cloud Service as it existed prior to the change of control."

---

### 12. Logo / Marketing Rights (Section 12.8)

**Classification**: Negotiate

**Contract provision**: "Provider may use Customer's name and logo in marketing." Unilateral right with no opt-out, no consent mechanism, no approval right over materials.

**Standard market position**: Logo rights are a common vendor request but should include Customer's prior written consent, or at minimum, a right to opt out upon written notice.

**Gap**: The provision is unilateral with no Customer control. Standard practice is to require consent or at least provide an opt-out.

**Redline**:
  - **Current language**: "Provider may use Customer's name and logo in marketing."
  - **Proposed redline**: "Provider may use Customer's name and logo in its customer lists and marketing materials, subject to Customer's prior written approval (not to be unreasonably withheld). Customer may revoke this permission at any time upon written notice to Provider."
  - **Rationale**: Customer should retain control over how its brand is used in third-party marketing. A consent requirement with a reasonableness standard is the standard market approach.
  - **Priority**: Nice-to-have
  - **Fallback**: "Provider may use Customer's name in text-only customer lists. Use of Customer's logo in any marketing materials requires Customer's prior written consent."

---

### 13. Data Processing for Non-GDPR Regimes (Section 3)

**Classification**: Negotiate

**Contract provision**: A DPA is required only before submitting "Personal Data governed by GDPR" (Section 3.1). No equivalent requirement for CCPA, LGPD, PIPEDA, or other data protection regimes.

**Standard market position**: A DPA covering all applicable data protection laws should be in place before any Personal Data is processed. Limiting the DPA requirement to GDPR creates compliance gaps for data subject to other regimes.

**Gap**: Personal Data governed by non-GDPR regimes has no DPA requirement in the Standard Terms. For a US-based Customer or one with global operations, CCPA and other state/national privacy laws may apply and are not addressed.

**Redline**:
  - **Current language**: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider."
  - **Proposed redline**: "Before submitting Personal Data governed by any Applicable Data Protection Law (including but not limited to GDPR, CCPA/CPRA, LGPD, and PIPEDA), Customer and Provider shall enter into a data processing agreement that addresses the requirements of all applicable data protection regimes."
  - **Rationale**: Data protection obligations are not limited to GDPR. The DPA requirement should cover all applicable privacy laws to avoid compliance gaps.
  - **Priority**: Should-have
  - **Fallback**: Accept the GDPR-only trigger in the Standard Terms but negotiate a standalone DPA as an Order Form attachment that covers all applicable data protection regimes.

---

### 14. Liability Cap Amounts — Cover Page Dependency (Sections 8.1, 8.3)

**Classification**: Negotiate

**Contract provision**: General Cap Amount, Increased Cap Amount, and the categories of Increased Claims and Unlimited Claims are all Cover Page variables. If not populated, all liability falls under the General Cap with no enhanced protection for critical categories.

**Standard market position**: For a $150K/year SaaS agreement, the General Cap is typically 12 months of fees paid or payable ($150K). Increased Cap for data breach and confidentiality violations is typically 2-3x the General Cap ($300K-$450K). IP indemnification is typically uncapped or at the Increased Cap level.

**Gap**: The Standard Terms provide the structure but no defaults. The Cover Page must be carefully populated. If General Cap is set below 12 months of fees, or if IP indemnification and data breach are not elevated to Increased or Unlimited Claims, Customer's protection is inadequate.

**Redline**:
  - **Current language**: [Cover Page variables]
  - **Proposed redline**: Ensure the Cover Page specifies:
    - General Cap Amount: "The greater of (a) the total Fees paid and payable by Customer during the 12-month period immediately preceding the event giving rise to the claim, or (b) $150,000."
    - Increased Cap Amount: "Three times (3x) the General Cap Amount."
    - Increased Claims: "Claims arising from (a) breach of Section 10 (Confidentiality); (b) breach of data protection obligations; (c) Provider's indemnification obligations under Section 9."
    - Unlimited Claims: "Claims arising from (a) either party's infringement or misappropriation of the other party's intellectual property rights; (b) either party's willful misconduct or fraud."
  - **Rationale**: The liability cap structure only protects Customer if the categories and amounts are properly calibrated. These amounts and categories reflect standard market positions for a deal of this size.
  - **Priority**: Must-have
  - **Fallback**: Accept a 2x Increased Cap and negotiate which claim categories qualify. The minimum acceptable position is that data breach and confidentiality breach are Increased Claims and IP indemnification is at least at the Increased Cap level.

---

## Provisions Aligned with Standard Market Position

The following provisions are consistent with or within acceptable range of standard market positions for a $150K/year SaaS agreement:

- **Service access and use scope** (Section 1): Standard grant limited to internal business purposes with appropriate restrictions. The Affiliate carveout is commercially reasonable.
- **Usage Data for product improvement** (Section 1.4): Aggregated, de-identified Usage Data for product improvement is standard. (The ML training extension in Section 1.6 is addressed separately above.)
- **Payment and Fees structure** (Section 4): Non-refundable fees with specified exceptions, invoicing mechanics, and tax allocation are within market norms.
- **Term and termination for breach** (Section 5): 30-day cure period for material breach, immediate termination for insolvency/dissolution, and force majeure termination with prorated refund are standard.
- **Mutual confidentiality obligations** (Section 10): Standard mutual confidentiality with standard exclusions and permitted disclosures.
- **Mutual indemnification structure** (Section 9): Mutual framework with standard procedural requirements is appropriate. (The exclusion scope is addressed separately above.)
- **Restrictions on use** (Section 2.1): Standard restriction set including no reverse engineering, no competitive use, no security testing.
- **Governing law and jurisdiction** (Section 12): Cover Page variables — standard structure. Ensure these are populated with acceptable jurisdictions.
- **Force majeure** (Section 12): Standard with appropriate carveout excluding payment obligations.

---

## Provisions Outside Standard Framework Categories

The following items from the Auditor's analysis do not map to standard playbook categories but warrant attention:

### Post-Termination ML Model Persistence

The Auditor identified a concern that is not addressed by standard contract review categories: even after Customer Content is deleted post-termination, ML models trained on that content retain its influence in their parameters. The contract requires deletion of Customer Content but does not address what happens to models that were trained on it. This is an emerging issue without settled market positions. The distinction between "data" (deletable) and "model weights influenced by data" (not practically deletable) is real, and the contract does not acknowledge it. This should be flagged to legal counsel as a novel risk area. If the ML training provision is removed per the redline above, this issue is mooted. If any ML rights over Customer Content are retained, counsel should consider whether additional language addressing model artifacts is warranted.

### Interaction Between Data Rights and Confidentiality

The Auditor flagged a structural tension: Sections 1.4 and 1.6 grant Provider data use rights that operate as authorized uses under the Agreement, potentially outside the Confidentiality protections. The consequential damages exception for Confidentiality breach (Section 8.4) creates a recovery path only for unauthorized use — but the authorized use grants are broad enough that distinguishing authorized ML training from unauthorized Confidential Information misuse could be difficult in practice. This interaction does not have a single redline fix; it is a structural feature of the contract that counsel should understand when assessing the aggregate data rights position.

### Cover Page Architecture as Risk Vector

Multiple critical terms — liability caps, Covered Claims definitions, non-renewal notice period, governing law, Increased/Unlimited Claims categories — are Cover Page variables. The Standard Terms are designed to be vendor-friendly defaults that the Cover Page can moderate. If the Cover Page is not carefully negotiated and populated, the defaults produce a materially one-sided agreement. This is not a single clause deviation but a structural observation: the negotiation of the Cover Page is at least as important as the negotiation of the Standard Terms. Ensure the Cover Page is reviewed with the same rigor as the Standard Terms themselves.

### Absence of Transition Assistance

The Auditor noted the absence of any transition or migration assistance obligation. For a $150K/year operational tool, if Customer terminates or decides not to renew, there is no obligation for Provider to assist with data migration to a successor platform. The proposed data export redline (item 8 above) addresses the data portability aspect, but operational transition assistance (knowledge transfer, integration support, parallel running) is not addressed. For a standard operational tool, this may be acceptable if the export provision is adequate, but if the tool involves complex data structures or integrations, transition assistance should be considered.

### Absence of Insurance Requirements

No requirement for Provider to maintain professional liability, cyber liability, or other insurance. For a new vendor relationship at $150K/year, the absence of insurance requirements means there is no independent assurance that Provider can satisfy indemnification or liability obligations. This is a standard procurement requirement that should be addressed, particularly given the data handling involved. Consider adding a requirement for Provider to maintain at least: (a) commercial general liability, (b) professional liability / errors and omissions, and (c) cyber liability / technology errors and omissions coverage, with minimum limits commensurate with the deal size and data exposure.
