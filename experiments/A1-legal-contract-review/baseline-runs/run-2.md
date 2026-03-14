# Contract Review Output -- Baseline Run 2

**Model**: Claude Opus 4.6 (1M context)
**Timestamp**: 2026-03-14
**Prompt**: Original monolithic prompt (SKILL.md)
**Contract**: Common Paper Cloud Service Agreement v2.1

---

## Contract Review Summary

**Document**: Common Paper Cloud Service Agreement -- Standard Terms Version 2.1
**Parties**: Provider (unnamed SaaS vendor) and Customer (our organization)
**Your Side**: Customer (buyer)
**Deadline**: 2 weeks
**Review Basis**: Generic commercial standards (no organizational playbook configured)

> **Note**: No organizational playbook was found. This review uses widely-accepted commercial standards as the baseline. Positions and recommendations should be calibrated to your organization's specific risk tolerance and legal preferences.

> **Important**: This analysis assists with legal workflows but does not constitute legal advice. All findings should be reviewed by qualified legal professionals before being relied upon.

---

## Key Findings

1. **RED -- Machine Learning / AI Training on Customer Data (Section 1.6)**: Provider claims rights to use Customer Content and Usage Data for AI/ML training. Even with aggregation and de-identification qualifications, this is an unusual and expansive data use right that goes well beyond what is needed to deliver the service. This is a priority concern given the focus on data protection.

2. **RED -- No DPA Included; Customer Must Initiate (Section 3.1)**: The agreement requires Customer to affirmatively enter into a DPA *before* submitting Personal Data governed by GDPR, but no DPA is attached or referenced. For a $150K/year SaaS platform handling internal operations data, this is a significant gap.

3. **YELLOW -- Feedback Clause Grants Unrestricted Rights (Section 1.4)**: Provider may use all Feedback "freely without any restriction or obligation." This is a broad, perpetual, irrevocable grant with no limitations. While common in SaaS agreements, it warrants narrowing.

4. **YELLOW -- Liability Cap and Damages Waiver Defined by Undefined Variables (Section 8)**: The General Cap Amount, Increased Cap Amount, Increased Claims, and Unlimited Claims are all defined on the Cover Page / Order Form, which is not provided. The structure is reasonable, but the actual risk allocation is entirely dependent on those undefined variables.

5. **YELLOW -- Logo Rights Without Consent (Section 12.8)**: Provider may use Customer's name and logo in marketing materials without requiring prior consent. Standard customer position is to require prior written approval.

---

## Clause-by-Clause Analysis

### Service and Access (Section 1.1-1.3) -- GREEN

**Contract says**: Customer may access and use the Cloud Service during the Subscription Period for internal business purposes. Customer may copy included Software and Documentation as needed for access. Affiliate Order Forms create separate agreements. Provider will provide Technical Support per the Order Form. Customer is responsible for user accounts and credential security.

**Standard position**: Standard SaaS access grant for internal use. Affiliate separation is commercially reasonable. Support tied to Order Form is standard.

**Deviation**: None material. The access grant is appropriately scoped for internal business use.

**Business impact**: Low risk. The Affiliate provision actually protects Customer from cross-liability for Affiliate actions.

---

### Feedback and Usage Data (Section 1.4) -- YELLOW

**Contract says**: Customer gives Feedback "AS IS" and Provider may use all Feedback "freely without any restriction or obligation." Provider may collect and analyze Usage Data and use it freely to maintain, improve, enhance, and promote Provider's products and services. Usage Data disclosed to others must be aggregated and not identify Customer or Users.

**Standard position**: Feedback clauses are common but should be limited to feedback voluntarily provided and should not extend to Customer's proprietary methodologies or processes. Usage Data collection is standard but the grant should be limited to service improvement, not promotion or third-party products.

**Deviation**: The Feedback clause is overly broad -- "freely without any restriction or obligation" could encompass proprietary improvements suggested by Customer. The Usage Data grant extends to "promote Provider's products" which is broader than service improvement.

**Business impact**: Moderate. If Customer provides suggestions that reflect proprietary business processes, Provider could incorporate those into its platform and sell them to competitors. The Usage Data promotion right means Customer's usage patterns could inform Provider's marketing.

**Redline suggestion**:

**Clause**: Section 1.4 (Feedback and Usage Data)
**Current language**: "Provider may use all Feedback freely without any restriction or obligation."
**Proposed redline**: "Provider may use Feedback to improve, enhance, and develop the Product. Feedback does not include Customer's proprietary business processes, methodologies, or trade secrets."
**Rationale**: We support Provider's product development but need to ensure our proprietary processes are not inadvertently transferred through feedback.
**Priority**: Should-have
**Fallback**: Accept the existing Feedback language but add a carveout: "Feedback does not include information designated as Confidential Information by Customer."

---

### Customer Content (Section 1.5) -- GREEN

**Contract says**: Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings. Customer is responsible for accuracy.

**Standard position**: This is a well-scoped license -- limited to what is necessary to deliver the service. The "related offerings" language is slightly broader than ideal but commercially reasonable.

**Deviation**: Minor. "Related offerings" extends slightly beyond the core service but is common in SaaS agreements.

**Business impact**: Low. The scope limitation to "provide and maintain" is the key protection.

---

### Machine Learning / AI Training (Section 1.6) -- RED

**Contract says**: Usage Data and Customer Content may be used to develop, train, or enhance AI/ML models that are part of Provider's products, including third-party components. Customer authorizes Provider to process its data for such purposes. Data must be aggregated and Provider will use "commercially reasonable efforts consistent with industry standard technology" to de-identify data before use. AI-generated information may be incorrect.

**Standard position**: Customers should retain control over whether their data is used for AI/ML training. The market is moving toward opt-in (not opt-out) for AI training on customer data. Aggregation and de-identification are positive but insufficient protections alone. "Commercially reasonable efforts" is a weak standard for de-identification.

**Deviation**: This clause authorizes Provider to train AI models on Customer Content and Usage Data by default, with no opt-out mechanism. The de-identification standard ("commercially reasonable efforts consistent with industry standard technology") is subjective and unenforceable in practice. The clause also permits use of Customer data for training *third-party* AI components, which significantly expands the data sharing scope.

**Business impact**: High. Customer's internal operations data -- potentially including proprietary workflows, business metrics, and employee data -- could be used to train AI models that benefit Provider's entire customer base, including competitors. The third-party component language means data could flow to AI vendors outside the Provider relationship. De-identification of operational data is notoriously difficult and "commercially reasonable efforts" provides no meaningful assurance.

**Redline suggestion**:

**Clause**: Section 1.6 (Machine Learning)
**Current language**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes."
**Proposed redline**: "Provider will not use Customer Content to develop, train, or enhance artificial intelligence or machine learning models unless Customer provides prior written consent. Provider may use aggregated and de-identified Usage Data for such purposes, provided that (a) such Usage Data cannot reasonably be re-identified, (b) Usage Data is not shared with third parties for AI/ML training, and (c) Customer may opt out of Usage Data processing for AI/ML purposes upon written notice."
**Rationale**: While we support Provider's product innovation, training AI models on our operational data -- particularly sharing it with third-party AI providers -- goes beyond the scope of our service relationship and raises data protection and competitive concerns.
**Priority**: Must-have
**Fallback**: If Provider insists on retaining some AI/ML rights, require (1) opt-out right for Customer Content, (2) prohibition on sharing data with third-party AI components, and (3) replace "commercially reasonable efforts" with a defined de-identification standard (e.g., NIST or ISO anonymization standards).

---

### Restrictions on Customer (Section 2.1) -- GREEN

**Contract says**: Standard restrictions including no reverse engineering, no sublicensing, no competitive development, no security testing, no unauthorized access, compliance with Documentation and Use Limitations.

**Standard position**: These restrictions are standard for SaaS agreements.

**Deviation**: The security testing restriction in 2.1(a)(v) could be problematic if Customer needs to conduct its own security assessments. However, this is typically addressed in the Order Form or a separate security testing agreement.

**Business impact**: Low. The restriction on security testing should be addressed in the Order Form to ensure Customer's security team can conduct necessary assessments.

---

### Suspension (Section 2.2) -- YELLOW

**Contract says**: Provider may suspend access for unpaid balances over 30 days, breach of restrictions, or use that "materially and negatively impacts the Product or others." Suspension may be with or without notice. Provider will "try to inform Customer before suspending" when practical.

**Standard position**: Suspension rights are standard but should require prior written notice (except in emergencies) and an opportunity to cure. "Try to inform" is a weak commitment. The "materially and negatively impacts" standard is subjective.

**Deviation**: The notice provision is inadequate -- "try to inform" and "with or without notice" give Provider broad discretion to suspend without meaningful notice. For a $150K/year platform used for internal operations, unexpected suspension could disrupt business operations.

**Business impact**: Moderate. Unannounced suspension of a core internal operations platform could cause workflow disruptions, missed deadlines, and downstream operational impacts.

**Redline suggestion**:

**Clause**: Section 2.2 (Suspension)
**Current language**: "Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical."
**Proposed redline**: "Provider will provide Customer at least 5 business days' prior written notice before suspending access, except where immediate suspension is reasonably necessary to prevent imminent harm to the Product, its users, or third parties, in which case Provider will notify Customer as soon as practicable and in no event later than 24 hours after suspension."
**Rationale**: As a platform supporting internal operations, unannounced suspension could cause significant business disruption. Prior notice ensures we can address issues before access is affected.
**Priority**: Should-have
**Fallback**: Accept "with or without notice" but require Provider to notify Customer within 24 hours of any suspension and provide a cure period of 5 business days before suspension takes effect for payment-related issues.

---

### Privacy and Security (Section 3) -- RED

**Contract says**: Before submitting Personal Data governed by GDPR, Customer must enter into a DPA with Provider. If a DPA is in place, its terms control. Customer may not submit Prohibited Data unless authorized by the Order Form.

**Standard position**: For a SaaS platform handling internal operations, a DPA should be included as part of the agreement or attached as an exhibit. The agreement should address data security standards, breach notification timelines, sub-processor management, data location, cross-border transfer mechanisms, and audit rights. Section 3 is remarkably thin for a modern SaaS agreement.

**Deviation**: Critical gaps:
- No DPA is attached or referenced -- Customer must affirmatively negotiate one separately
- No data security standards or commitments (no SOC 2, ISO 27001, or equivalent)
- No breach notification timeline or procedure
- No sub-processor transparency or approval rights
- No data location requirements
- No cross-border transfer protections
- No audit rights for Customer
- No data return or deletion timeline beyond the 60-day post-termination provision in Section 5.5(b)
- The GDPR trigger is narrow -- other data protection laws (CCPA, state privacy laws, international regulations) are not addressed

**Business impact**: High. A $150K/year SaaS platform for internal operations will almost certainly process employee data (names, email addresses, usage patterns) and potentially customer or business partner data. The absence of a DPA, security commitments, and breach notification procedures exposes Customer to regulatory risk and potential data breaches with no contractual remedies.

**Redline suggestion**:

**Clause**: Section 3 (Privacy & Security)
**Current language**: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider."
**Proposed redline**: "Provider will execute a Data Processing Agreement substantially in the form attached as Exhibit [X] concurrently with this Agreement. The DPA will address, at minimum: (a) Provider's data security measures, including maintenance of SOC 2 Type II certification or equivalent; (b) breach notification within 48 hours of discovery; (c) sub-processor disclosure and approval rights; (d) data location and cross-border transfer mechanisms; (e) annual audit rights or third-party audit report availability; and (f) data return and deletion upon termination. Provider's obligations under the DPA will apply to all Personal Data processed under Applicable Data Protection Laws, not limited to GDPR."
**Rationale**: As a platform processing operational data, we require data protection commitments aligned with current regulatory requirements and industry standards. A DPA should be executed concurrently, not deferred.
**Priority**: Must-have
**Fallback**: At minimum, require (1) a DPA executed before the service start date, (2) breach notification within 72 hours, (3) annual SOC 2 report availability, and (4) data deletion within 30 days of termination.

---

### Payment and Taxes (Section 4) -- GREEN

**Contract says**: Fees in USD unless Order Form specifies otherwise; non-refundable except for specific termination refund rights. Invoicing in arrears for usage-based and in advance for other fees. Customer responsible for taxes except Provider's income taxes. Payment dispute process with 15-day resolution period.

**Standard position**: Payment terms are standard. The dispute resolution process is reasonable. Non-refundable fees are standard with the exception for termination-related refunds.

**Deviation**: None material. The payment dispute mechanism in Section 4.6 is actually customer-friendly, requiring Provider to work with Customer to resolve disputes within 15 days.

**Business impact**: Low. Standard commercial terms.

---

### Term and Termination (Section 5) -- YELLOW

**Contract says**: Agreement runs for the Subscription Period with automatic renewal unless notice of non-renewal is given before the Non-Renewal Notice Date (defined on Cover Page). Either party may terminate for material breach with 30 days to cure, or immediately for incurable breach, dissolution, or insolvency. Force majeure termination after 30 consecutive days of non-operation, with prorated refund.

**Standard position**: The structure is reasonable but several key terms are undefined (Subscription Period, Non-Renewal Notice Date) -- they are set on the Cover Page. There is no termination for convenience right. The 60-day deletion period for Customer Content is long. No transition assistance is provided.

**Deviation**:
- No termination for convenience: Customer is locked in for the full Subscription Period with no early exit
- Data deletion timeline of 60 days post-termination is long; 30 days is more standard
- No transition assistance provisions (data export, migration support, continued access during wind-down)
- Non-Renewal Notice Date is undefined here and set on the Cover Page -- needs to be reviewed to ensure adequate notice window

**Business impact**: Moderate. Without termination for convenience, Customer is locked into the full contract term even if the platform underperforms, the business need changes, or a better alternative becomes available. For a $150K/year commitment with a new vendor, this is a meaningful restriction. The lack of transition assistance could make migration costly and disruptive.

**Redline suggestion**:

**Clause**: Section 5.3 (Termination)
**Current language**: [No termination for convenience provision exists]
**Proposed redline**: Add new Section 5.3(c): "Customer may terminate any Order Form for convenience upon 90 days' prior written notice, subject to payment of Fees for the 90-day notice period. Provider will provide reasonable transition assistance during the notice period, including data export in a standard machine-readable format."
**Rationale**: As this is a new vendor relationship for an important operational platform, we need flexibility to exit if the service does not meet expectations or our business needs change.
**Priority**: Should-have
**Fallback**: If full termination for convenience is rejected, negotiate (1) termination for convenience after the initial 12-month period with 90 days' notice, and (2) a data export right in a standard format at any time during the term.

**Clause**: Section 5.5(b) (Effect of Termination -- Data Deletion)
**Current language**: "Upon Customer's request, Provider will delete Customer Content within 60 days."
**Proposed redline**: "Upon Customer's request, Provider will (a) provide Customer with a complete export of Customer Content in a standard, machine-readable format within 15 days, and (b) delete all Customer Content within 30 days after export or, if no export is requested, within 30 days of termination."
**Rationale**: A 60-day deletion window is longer than industry standard and extends the period during which our data remains in Provider's systems post-termination.
**Priority**: Should-have
**Fallback**: Accept 60-day deletion but require data export capability within 15 days.

---

### Representations and Warranties (Section 6) -- GREEN

**Contract says**: Mutual reps on authority, organization, and legal compliance. Customer warrants rights to Customer Content. Provider warrants it will not materially reduce Cloud Service functionality during the Subscription Period. If Provider breaches the functionality warranty, Customer has 45 days to report, Provider has 45 days to fix, and if unfixed, Customer may terminate with prorated refund.

**Standard position**: The mutual reps are standard. The Provider warranty on functionality is a reasonable minimum commitment. The warranty remedy process is fair but the 45+45 day timeline (90 days total) is long.

**Deviation**: Minor. Provider's warranty is limited to not *materially reducing* functionality -- it does not warrant that the service will perform as described, meet specifications, or achieve any particular availability level. There is no SLA or uptime commitment in the standard terms.

**Business impact**: Low-to-moderate. The absence of an SLA is notable for a $150K/year platform but is typically addressed in the Order Form. If no SLA is in the Order Form, this should be escalated.

---

### Disclaimer of Warranties (Section 7) -- GREEN

**Contract says**: Provider disclaims all warranties except those in Section 6, including merchantability, fitness for purpose, title, and non-infringement. Provider makes no guarantees on safety, security, or error-free operation.

**Standard position**: Standard warranty disclaimer for SaaS agreements. The carveout for Section 6 warranties is appropriate.

**Deviation**: None material. This is a standard mutual disclaimer.

**Business impact**: Low. The key protection is the Section 6 warranty on functionality, which is preserved.

---

### Limitation of Liability (Section 8) -- YELLOW

**Contract says**: Each party's total liability capped at the General Cap Amount (defined on Cover Page). Increased Claims have a higher cap (Increased Cap Amount). Mutual waiver of consequential, indirect, special, exemplary, punitive, and incidental damages, plus lost profits/revenues. Exceptions: liability cap does not apply to Increased Claims (which have their own cap) or Unlimited Claims. Damages waiver does not apply to Increased Claims or breach of confidentiality.

**Standard position**: The structure is well-designed -- three tiers (General Cap, Increased Cap, Unlimited) is best practice. The mutual damages waiver with carveouts for Increased Claims and confidentiality breaches is customer-friendly. However, all the critical variables (General Cap Amount, Increased Cap Amount, what constitutes Increased Claims and Unlimited Claims) are on the Cover Page.

**Deviation**: Cannot fully assess without the Cover Page. Key concerns:
- If General Cap Amount is set at a fraction of annual fees (e.g., 3 months), this is insufficient for a $150K/year contract
- If IP infringement and data breach are not listed as Increased or Unlimited Claims, the cap may be too low for the most significant risks
- The damages waiver includes direct lost profits, which is aggressive -- most customer-favorable positions only waive indirect lost profits

**Business impact**: Potentially high, depending on Cover Page values. The waiver of direct lost profits is notable -- if Provider's service failure causes Customer to lose revenue, Customer cannot recover lost profits even as direct damages.

**Redline suggestion**:

**Clause**: Section 8.2 (Damages Waiver)
**Current language**: "Neither party will be liable for lost profits or revenues (whether direct or indirect)..."
**Proposed redline**: "Neither party will be liable for indirect lost profits or revenues, or for consequential, special, indirect, exemplary, punitive, or incidental damages..."
**Rationale**: Direct lost profits resulting from service failures should remain recoverable as they are a foreseeable consequence of service disruption.
**Priority**: Should-have
**Fallback**: Accept the lost profits waiver but ensure the Cover Page sets the General Cap Amount at no less than 12 months of fees and that data breach and IP infringement are classified as Increased Claims or Unlimited Claims.

**Note for Order Form / Cover Page review**: Ensure the following variables are set to acceptable levels:
- General Cap Amount: At least 12 months of fees ($150K minimum)
- Increased Cap Amount: At least 2x annual fees ($300K minimum)
- Increased Claims should include: IP indemnification, data breach, breach of data protection obligations
- Unlimited Claims should include: willful misconduct, fraud, IP infringement indemnity (if possible)

---

### Indemnification (Section 9) -- YELLOW

**Contract says**: Mutual indemnification -- Provider indemnifies Customer from "Provider Covered Claims" and Customer indemnifies Provider from "Customer Covered Claims." Standard procedure with notice, assistance, and sole control of defense. Provider may modify, replace, or terminate if required by settlement or court order. Exclusions for unauthorized modifications, unauthorized use, and combination with non-Provider items. Indemnification is the exclusive remedy for Covered Claims.

**Standard position**: The mutual structure is appropriate. However, the actual scope depends entirely on how "Provider Covered Claims" and "Customer Covered Claims" are defined on the Cover Page. Typically, Provider should indemnify for IP infringement and data breaches; Customer should indemnify for Customer Content and misuse.

**Deviation**:
- Scope is undefined in the standard terms -- depends on Cover Page definitions
- The exclusion for "combination with non-Provider items" could be very broad, potentially excluding claims arising from standard integrations
- Provider's right to terminate and refund as a remedy (Section 9.4(c)) means Provider can walk away from an infringement claim by simply ending the service
- Exclusive remedy clause (Section 9.6) means Customer cannot pursue other remedies for Covered Claims

**Business impact**: Moderate. The "combination with non-Provider items" exclusion is concerning for a SaaS platform that will likely integrate with other systems. If an IP claim arises from an integration, Provider could disclaim indemnification responsibility.

**Redline suggestion**:

**Clause**: Section 9.5 (Exclusions)
**Current language**: "Provider's obligations don't apply to claims from... combination with non-Provider items..."
**Proposed redline**: "Provider's obligations do not apply to claims arising from combination with non-Provider items, unless such combination is (a) contemplated by the Documentation, (b) made through Provider's published APIs, or (c) consistent with the Product's intended use."
**Rationale**: Standard integrations through documented APIs and intended use cases should remain within the scope of Provider's indemnification. Excluding all combinations could leave us unprotected for foreseeable use.
**Priority**: Should-have
**Fallback**: Accept the exclusion but add a carveout for integrations that are "documented, recommended, or provided by Provider."

---

### Confidentiality (Section 10) -- GREEN

**Contract says**: Standard mutual confidentiality with non-use and non-disclosure obligations. Standard exclusions (prior knowledge, public information, independent development, authorized third-party receipt). Required disclosures permitted with reasonable advance notice. Permitted disclosures to employees, advisors, and contractors with need-to-know under equivalent obligations.

**Standard position**: Standard confidentiality provisions. No defined term for confidentiality obligations (survival is addressed in Section 5.6). The exclusions and permitted disclosures are appropriately scoped.

**Deviation**: None material. The confidentiality provisions are well-constructed and mutual.

**Business impact**: Low. Standard protections.

---

### Reservation of Rights (Section 11) -- YELLOW

**Contract says**: Provider retains all rights in the Product. Customer retains all rights in Customer Content, *subject to Sections 1.5 and 1.6*.

**Standard position**: Each party should retain its pre-existing IP without qualification. Customer's rights in Customer Content should not be subject to the broad AI/ML training rights in Section 1.6.

**Deviation**: The "subject to Sections 1.5 and 1.6" qualification means Customer's ownership of its own content is subordinated to Provider's rights to use it for service delivery (1.5, reasonable) and AI/ML training (1.6, problematic). This creates an internal tension -- Customer "retains all rights" but has granted Provider broad rights to use that content for AI training.

**Business impact**: Moderate to high, particularly in conjunction with the Section 1.6 concerns. Customer's IP in its operational data and content is effectively licensed to Provider for AI/ML purposes.

**Redline suggestion**: Address through the Section 1.6 redline above. If Section 1.6 is appropriately narrowed, the "subject to" qualification in Section 11.1 becomes acceptable.

---

### Assignment (Section 12.6) -- GREEN

**Contract says**: No assignment without consent, except in merger, acquisition, or change of control.

**Standard position**: Standard assignment clause. The change-of-control exception is mutual, which is appropriate.

**Deviation**: None material. This is a balanced provision.

**Business impact**: Low. Customer retains the right to assign in M&A transactions, which is important for corporate flexibility.

---

### Logo Rights (Section 12.8) -- YELLOW

**Contract says**: Provider may use Customer's name and logo in marketing.

**Standard position**: Customer should have the right to approve use of its name and logo in marketing materials. Blanket grants without consent are not standard for mid-market deals.

**Deviation**: No consent requirement. Provider has a blanket right to use Customer's brand in marketing.

**Business impact**: Low-to-moderate. Reputational risk if Provider uses Customer's brand in marketing materials that Customer would not endorse.

**Redline suggestion**:

**Clause**: Section 12.8 (Logo Rights)
**Current language**: "Provider may use Customer's name and logo in marketing."
**Proposed redline**: "Provider may use Customer's name and logo in marketing materials only with Customer's prior written consent, not to be unreasonably withheld."
**Rationale**: We require approval over use of our brand in third-party marketing materials.
**Priority**: Nice-to-have
**Fallback**: Accept logo use in customer lists and on Provider's website, but require prior written consent for case studies, press releases, and featured marketing content.

---

### Force Majeure (Section 5.4, 12.12) -- GREEN

**Contract says**: Neither party liable for delays from Force Majeure Events, except Customer's payment obligations. Either party may terminate an affected Order Form if Force Majeure prevents material operation for 30+ consecutive days, with prorated refund.

**Standard position**: Standard force majeure with a reasonable 30-day threshold for termination. The preservation of Customer's payment obligation is standard. The prorated refund on termination is customer-friendly.

**Deviation**: None material.

**Business impact**: Low. The 30-day threshold and termination right with refund are balanced.

---

### Governing Law and Dispute Resolution (Section 12.3) -- YELLOW

**Contract says**: Governing Law applies without regard to conflict of laws. Chosen Courts have exclusive jurisdiction. (Both defined on Cover Page.)

**Standard position**: Cannot assess without knowing the Governing Law and Chosen Courts from the Cover Page. The structure is standard.

**Deviation**: Depends entirely on Cover Page values. If Governing Law is a well-established commercial jurisdiction (Delaware, New York, California, England) and Chosen Courts are convenient, this is GREEN. If the jurisdiction is unusual or remote, this escalates.

**Business impact**: Variable. Must review Cover Page values.

**Note for Order Form / Cover Page review**: Ensure Governing Law is an established commercial jurisdiction and Chosen Courts are reasonably accessible.

---

### Insurance -- NOT ADDRESSED

**Contract says**: No insurance provisions in the standard terms.

**Standard position**: For a $150K/year SaaS vendor, Customer should require evidence of commercial general liability, professional liability / E&O, and cyber liability insurance at appropriate minimums.

**Deviation**: Complete absence. No insurance requirements.

**Business impact**: Moderate. If Provider suffers a data breach or operational failure, inadequate insurance could mean Provider cannot fund its indemnification or liability obligations.

**Redline suggestion**:

**Clause**: [New -- Insurance]
**Current language**: [None]
**Proposed redline**: Add new section: "Provider will maintain throughout the term: (a) commercial general liability insurance of at least $1,000,000 per occurrence; (b) professional liability / errors and omissions insurance of at least $2,000,000; and (c) cyber liability insurance of at least $5,000,000. Provider will provide certificates of insurance upon request."
**Rationale**: Insurance requirements ensure Provider can meet its contractual obligations in the event of a claim.
**Priority**: Should-have
**Fallback**: Require cyber liability insurance only, at a minimum of $2,000,000, with certificate of insurance upon request.

---

### SLA / Uptime -- NOT ADDRESSED

**Contract says**: No service level agreement or uptime commitment in the standard terms. Provider warrants only that it will not "materially reduce the general functionality" (Section 6.3).

**Standard position**: A $150K/year SaaS platform for internal operations should include an SLA with defined uptime commitment (99.9% is standard), measurement methodology, and service credits for downtime.

**Deviation**: Complete absence. The only performance commitment is the negative warranty against functionality reduction.

**Business impact**: Moderate to high. Without an SLA, Customer has no contractual remedy for poor performance or downtime short of the material breach threshold. For an internal operations platform, reliability is critical.

**Note for Order Form review**: Ensure the Order Form includes an SLA with uptime commitment, measurement methodology, exclusions, and service credit schedule.

---

## Negotiation Strategy

### Tier 1 -- Must-Haves (Deal Breakers)

1. **Revise Section 1.6 (Machine Learning)**: Remove or substantially limit Provider's right to use Customer Content for AI/ML training. At minimum, require opt-in consent and prohibit sharing with third-party AI components. This is the single most important issue given the data protection focus.

2. **Require a DPA (Section 3)**: A DPA must be executed concurrently with the agreement, not deferred. It must include breach notification timelines, sub-processor controls, data security standards, and audit rights. For a platform processing internal operations data, this is non-negotiable.

### Tier 2 -- Should-Haves (Strong Preferences)

3. **Liability cap adequacy (Section 8 / Cover Page)**: Ensure General Cap is at least 12 months of fees. Ensure IP infringement and data breach are Increased Claims. Remove the direct lost profits waiver or reclassify as indirect only.

4. **Termination for convenience (Section 5)**: Add a termination for convenience right with reasonable notice period and transition assistance, given that this is a new vendor.

5. **Suspension notice (Section 2.2)**: Require prior written notice before suspension, with emergency exception.

6. **Indemnification scope (Section 9 / Cover Page)**: Ensure Provider Covered Claims include IP infringement and data breach. Narrow the "combination" exclusion for documented integrations.

7. **Data export and deletion (Section 5.5)**: Reduce deletion timeline to 30 days. Add data export in machine-readable format.

8. **Insurance**: Add cyber liability and professional liability requirements.

### Tier 3 -- Nice-to-Haves (Concession Candidates)

9. **Feedback clause (Section 1.4)**: Narrow the feedback grant. Concession candidate if Section 1.6 is resolved.

10. **Logo rights (Section 12.8)**: Require prior written consent. Can concede to "customer list" use without consent.

11. **Reservation of rights qualification (Section 11.1)**: Addressed by resolving Section 1.6.

### Recommended Approach

**Lead with Sections 1.6 and 3** -- the AI/ML training rights and DPA gap are both principled positions that are well-supported by market trends and regulatory requirements. These are defensible asks that most reasonable vendors will accommodate.

**Package Tier 2 items together** -- present the liability, termination, and suspension asks as a standard customer-protection package. Offer to accept the Feedback clause and Logo rights as-is (Tier 3 concessions) in exchange for movement on termination for convenience and suspension notice.

**Preserve Cover Page / Order Form negotiations** -- many critical variables (liability caps, Increased Claims, Unlimited Claims, SLA, Non-Renewal Notice Date, Governing Law) are defined outside the standard terms. Conduct a parallel review of the Cover Page and Order Form to ensure these values are acceptable.

### Timeline Considerations

- **2-week deadline** is tight but workable for a standard terms negotiation
- Priority the must-haves (Sections 1.6 and 3) in the first round of redlines
- Package Tier 2 items for the second round if needed
- The DPA negotiation may require its own timeline -- start this immediately
- Request the Cover Page / Order Form early to review the undefined variables

---

## Next Steps

1. **Immediate**: Request the Cover Page / Order Form from the vendor to review all undefined variables (liability caps, SLA, governing law, subscription period, non-renewal notice date, Covered Claims definitions)
2. **Immediate**: Request Provider's standard DPA for review; if none exists, prepare a DPA based on your standard form
3. **Day 1-2**: Send initial redlines focusing on Section 1.6 (ML/AI), Section 3 (Privacy), and the Cover Page variables
4. **Day 3-5**: Review vendor response and negotiate Tier 2 items
5. **Day 5-7**: Finalize DPA in parallel
6. **Day 7-10**: Resolve remaining items and finalize agreement
7. **Day 10-14**: Internal review, signature, and execution
8. **Throughout**: Ensure qualified legal counsel reviews all redlines and the final agreement before execution

---

*This analysis is based on widely-accepted commercial standards and is not legal advice. All findings should be reviewed by qualified legal professionals before being relied upon for legal decisions.*
