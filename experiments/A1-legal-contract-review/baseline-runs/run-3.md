# Contract Review Output

**Important**: This analysis assists with legal workflows but does not constitute legal advice. All findings should be reviewed by qualified legal professionals before being relied upon for legal decisions.

## Contract Review Summary

**Document**: Common Paper Cloud Service Agreement -- Standard Terms Version 2.1
**Parties**: Provider (unnamed SaaS vendor) and Customer (buyer)
**Your Side**: Customer (buyer)
**Deadline**: 2 weeks
**Review Basis**: Generic review using widely-accepted commercial standards (no organizational playbook found)

**Note**: No organizational playbook was located. This review is based on general commercial standards and market norms for mid-market SaaS agreements from the customer's perspective.

---

## Key Findings

1. **RED -- Machine Learning / AI Training on Customer Data (Section 1.6)**: Provider claims broad rights to use Customer Content and Usage Data for AI/ML training. Even with aggregation and de-identification requirements, this is a significant data rights issue for a customer, particularly one prioritizing data protection.

2. **RED -- Data Protection is Dangerously Thin (Section 3)**: The agreement mentions a DPA only in the context of GDPR-governed Personal Data and places the burden on the Customer to initiate it. There are no data security standards, no breach notification timelines, no sub-processor controls, and no data localization provisions in the base agreement.

3. **YELLOW -- Feedback Clause Grants Unrestricted Rights (Section 1.4)**: Provider receives a perpetual, unrestricted, obligation-free license to all Feedback. Combined with a broad definition of Feedback, this could capture valuable Customer IP.

4. **YELLOW -- Liability and Indemnification Terms Depend Entirely on Undefined Cover Page Variables**: The General Cap Amount, Increased Cap Amount, Unlimited Claims, Provider Covered Claims, and Customer Covered Claims are all defined on the Cover Page, which is not provided. The framework is sound but the actual risk allocation is unknowable without these values.

5. **YELLOW -- Logo Rights Without Consent (Section 12.8)**: Provider may use Customer's name and logo in marketing materials without requiring prior approval.

---

## Clause-by-Clause Analysis

### 1. Service & Access (Section 1.1-1.3) -- GREEN

**Contract says**: Customer may access and use the Cloud Service during the Subscription Period for internal business purposes. Customer Affiliates may enter separate Order Forms creating separate agreements. Provider will provide Technical Support as described in the Order Form. Customer is responsible for user accounts and credential security.

**Standard position**: These are standard SaaS access and use provisions. Internal business purpose limitation is typical. Affiliate structuring is reasonable.

**Deviation**: None material. The Affiliate carve-out (creating a separate agreement per Affiliate) is common in Common Paper templates. The support terms depend on the Order Form, which is standard.

**Business impact**: Low risk. These are well-drafted, balanced provisions.

---

### 2. Feedback and Usage Data (Section 1.4) -- YELLOW

**Contract says**: Customer gives Feedback "AS IS" and Provider may use all Feedback freely without restriction or obligation. Provider may collect and analyze Usage Data and use it freely to maintain, improve, enhance, and promote its products and services. Usage Data disclosed to third parties must be aggregated and not identify Customer.

**Standard position**: Feedback clauses are common, but best practice for customers is to ensure the clause does not inadvertently capture suggestions that constitute Customer IP (e.g., proprietary methodologies, workflows, or business logic). Usage data collection is standard but should have clearer boundaries.

**Deviation**: The Feedback clause is broadly worded -- "Provider may use all Feedback freely without any restriction or obligation" is one-sided. While voluntary, the lack of any limitation on how Feedback is used (including incorporating it into products sold to Customer's competitors) is a concern. Usage Data provisions are reasonable with the aggregation/anonymization requirement for third-party disclosure.

**Business impact**: If Customer provides substantive suggestions about product functionality or shares workflow insights, Provider gains unrestricted rights to commercialize those ideas. For a $150K/year operational platform, the risk is moderate -- Customer should implement internal policies about what constitutes Feedback versus Customer Confidential Information.

**Redline suggestion**:

**Clause**: Section 1.4 (Feedback and Usage Data)
**Current language**: "Provider may use all Feedback freely without any restriction or obligation."
**Proposed redline**: "Provider may use Feedback freely without restriction or obligation, provided that Feedback does not include Customer's Confidential Information, proprietary business processes, or trade secrets. Customer retains all rights in any materials shared with Provider that are not expressly designated as Feedback."
**Rationale**: Clarifies the boundary between voluntary product feedback and proprietary business information to protect Customer's intellectual property.
**Priority**: Should-have
**Fallback**: Add a sentence clarifying that Feedback is limited to suggestions regarding Provider's product functionality and does not include Customer's business methodologies or proprietary data.

---

### 3. Customer Content (Section 1.5) -- GREEN

**Contract says**: Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings. Customer is responsible for accuracy.

**Standard position**: This is a well-scoped license -- limited to what is necessary to deliver the service. "Related offerings" is slightly broader than ideal but commercially reasonable.

**Deviation**: Minor. "Related offerings" could be tightened but is unlikely to be problematic in practice.

**Business impact**: Low risk.

---

### 4. Machine Learning / AI Training (Section 1.6) -- RED

**Contract says**: Usage Data and Customer Content may be used to develop, train, or enhance AI/ML models that are part of Provider's products and services, including third-party components. Customer authorizes such processing. Data must be aggregated before use and Provider will use "commercially reasonable efforts consistent with industry standard technology" to de-identify. Provider acknowledges that AI outputs may be inaccurate.

**Standard position**: Customer-side best practice is to prohibit the use of Customer Content for AI/ML training entirely, or at minimum to require explicit opt-in consent and provide an opt-out mechanism. The use of customer data to train AI models that benefit the Provider's other customers (including competitors) is increasingly scrutinized. Many enterprise SaaS agreements now include an explicit AI/ML carve-out protecting customer data.

**Deviation**: This is a significant departure from customer-favorable standards. Key concerns:
- Customer Content (not just Usage Data) can be used for AI/ML training
- The authorization is blanket -- no opt-out mechanism
- "Commercially reasonable efforts" for de-identification is a weak standard; it is not a guarantee
- Third-party AI components are included, meaning Customer data could flow to unknown third parties for training purposes
- The aggregation requirement provides some protection but does not address the competitive concern of training models that benefit competitors

**Business impact**: For a $150K/year operational platform, Customer Content likely includes sensitive internal business data. Training Provider's AI models on this data effectively subsidizes Provider's product development and benefits all Provider customers, including Customer's competitors. The "commercially reasonable efforts" de-identification standard means there is no guarantee of anonymization. This is a material data rights issue.

**Redline suggestion**:

**Clause**: Section 1.6 (Machine Learning)
**Current language**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes."
**Proposed redline**: "Usage Data (but not Customer Content) may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services. Provider will not use Customer Content to train, develop, or enhance any AI or ML models. Customer authorizes Provider to process Usage Data (but not Customer Content) for such purposes, provided that Provider maintains a current list of third-party AI/ML components that process Usage Data and makes it available to Customer upon request."
**Rationale**: Customer Content contains proprietary business information that should not be used to train AI models benefiting Provider's broader customer base. This aligns with emerging enterprise SaaS market standards for AI data governance.
**Priority**: Must-have
**Fallback**: If Provider insists on using Customer Content for AI/ML, require: (a) explicit opt-in rather than default authorization; (b) a clear opt-out mechanism; (c) deletion of Customer Content from training data upon termination; and (d) "best efforts" rather than "commercially reasonable efforts" for de-identification.

---

### 5. Restrictions on Customer (Section 2.1) -- GREEN

**Contract says**: Standard restrictions including no reverse engineering, no sublicensing, no security testing, no competitive development, no use with High Risk Activities, and compliance with Documentation and Use Limitations.

**Standard position**: These are standard SaaS restrictions. The reverse engineering carve-out for applicable law is appropriate. The competitive use restriction is common.

**Deviation**: The prohibition on security/vulnerability testing (Section 2.1(a)(v)) is worth noting. Customer may want the right to conduct security assessments, particularly for a platform handling internal operations data.

**Business impact**: Low to moderate. If Customer has a security program that requires vendor penetration testing, this restriction could be an issue. Otherwise standard.

---

### 6. Suspension (Section 2.2) -- YELLOW

**Contract says**: Provider may suspend access for unpaid balances (30+ days), breach of restrictions, or use that negatively impacts the Product or others. Provider "will try to inform Customer before suspending" but is not required to provide advance notice. Reinstatement requires resolution of the underlying issue.

**Standard position**: Suspension rights are standard, but best practice requires prior written notice (except in emergencies) and a cure period before suspension. The language "will try to inform" is weak -- it should be "will provide reasonable advance notice except in cases of imminent harm."

**Deviation**: The notice provision is weaker than market standard. "Will try to inform" imposes no real obligation. Suspension without notice for a $150K/year platform could cause significant operational disruption.

**Business impact**: Moderate. An unexpected suspension of an operational SaaS platform could disrupt internal operations. The 30-day payment trigger is reasonable, but the broad "negatively impacts the Product or others" language gives Provider wide discretion.

**Redline suggestion**:

**Clause**: Section 2.2 (Suspension)
**Current language**: "Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical."
**Proposed redline**: "Provider will provide Customer at least 5 business days' prior written notice before suspending access, except where immediate suspension is reasonably necessary to prevent imminent harm to the Product, other customers, or third parties. In the case of immediate suspension, Provider will notify Customer as soon as reasonably practicable and will work with Customer to resolve the issue promptly."
**Rationale**: A $150K/year operational platform requires reasonable notice before suspension to allow Customer to address issues and mitigate operational disruption.
**Priority**: Should-have
**Fallback**: Accept "with or without notice" but add a requirement that Provider must notify Customer within 24 hours of any suspension and provide a specific description of the issue to be cured.

---

### 7. Privacy & Security (Section 3) -- RED

**Contract says**: Before submitting Personal Data governed by GDPR, Customer must enter into a DPA with Provider. If a DPA exists, it controls. Customer must not submit Prohibited Data unless authorized by the Order Form.

**Standard position**: For a $150K/year SaaS platform processing internal operations data, the data protection provisions are dangerously inadequate. Market standard requires:
- A DPA as an exhibit to the agreement (not as a separate future agreement)
- Coverage for all data protection laws, not just GDPR
- Data security commitments (SOC 2, ISO 27001, or equivalent)
- Breach notification timelines (typically 48-72 hours)
- Sub-processor disclosure and approval rights
- Data localization or transfer mechanism commitments
- Data return and deletion provisions with specific timelines
- Audit rights or third-party audit report access

**Deviation**: Critical gaps:
- The DPA is not included or referenced as an exhibit -- it depends on Customer initiating it before submitting Personal Data
- Only GDPR is mentioned; other data protection regimes (CCPA/CPRA, PIPEDA, state privacy laws) are not addressed
- No data security standards or certifications are required
- No breach notification timeline
- No sub-processor transparency
- No data localization provisions
- No audit rights
- Data deletion upon termination is addressed in Section 5.5(b) but on a 60-day timeline and only upon Customer request

**Business impact**: This is the most significant gap in the agreement for a customer prioritizing data protection. An internal operations platform will almost certainly process personal data (employee data, customer records, etc.). Without a DPA, security commitments, and breach notification provisions baked into the agreement, Customer is exposed to regulatory risk and has limited recourse if a data incident occurs.

**Redline suggestion**:

**Clause**: Section 3 (Privacy & Security)
**Current language**: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider."
**Proposed redline**: "The parties will execute Provider's Data Processing Agreement (DPA), attached as Exhibit [X], which will govern all processing of Personal Data under this Agreement. The DPA will comply with all Applicable Data Protection Laws, including but not limited to GDPR, CCPA/CPRA, and other applicable privacy laws. Provider will: (a) maintain industry-standard security measures, including SOC 2 Type II certification or equivalent; (b) notify Customer of any Security Incident involving Customer data within 48 hours of discovery; (c) maintain a current list of sub-processors and provide Customer with at least 30 days' advance notice before engaging a new sub-processor; (d) upon termination, return or delete all Customer data within 30 days at Customer's election; and (e) upon request, provide Customer with copies of relevant third-party audit reports (e.g., SOC 2) or permit Customer to conduct reasonable security assessments."
**Rationale**: An operational SaaS platform will process personal data and business-sensitive information. Industry-standard data protection commitments are necessary to satisfy Customer's regulatory obligations and security requirements.
**Priority**: Must-have
**Fallback**: At minimum, require: (a) a DPA attached as an exhibit covering all applicable data protection laws; (b) breach notification within 72 hours; and (c) annual SOC 2 Type II report sharing. The sub-processor and audit provisions can be addressed in the DPA itself.

---

### 8. Payment & Taxes (Section 4) -- GREEN

**Contract says**: Fees in USD, exclusive of taxes, non-refundable except where termination rights allow prorated refunds. Invoicing or automatic payment per the Payment Process. Customer responsible for applicable taxes (not Provider's income taxes). Payment disputes require notice before due date or within 30 days of automatic payment; parties will resolve within 15 days.

**Standard position**: These are standard payment provisions. The dispute resolution process is reasonable. The tax allocation is standard.

**Deviation**: None material. The 15-day dispute resolution window is tight but not unusual.

**Business impact**: Low risk. Standard commercial terms.

---

### 9. Term & Termination (Section 5) -- YELLOW

**Contract says**: Auto-renewal unless notice given before the Non-Renewal Notice Date (defined on Cover Page). Termination for material breach with 30-day cure period. Immediate termination for incurable breach, dissolution, or insolvency. Force Majeure termination after 30 consecutive days with prorated refund. Upon termination: Customer loses access; Provider deletes Customer Content within 60 days upon request; Confidential Information returned or destroyed; final invoice submitted.

**Standard position**: The framework is reasonable. Key concerns:
- No termination for convenience. Customer is locked in for the full Subscription Period.
- The Non-Renewal Notice Date is undefined (Cover Page variable) -- this could be 30 days, 90 days, or more
- Customer Content deletion is 60 days (market standard is 30 days) and only upon request (should be automatic with an option to request return)
- No transition assistance provisions

**Deviation**:
- Absence of termination for convenience is common but unfavorable for a customer in a new vendor relationship. For a $150K/year commitment with an unproven vendor, this is a meaningful gap.
- 60-day deletion timeline is longer than the 30-day market standard
- No transition assistance or data export provisions

**Business impact**: Customer is committed for the full Subscription Period with no exit other than material breach. If the platform underperforms or business needs change, Customer has no contractual exit. This is particularly concerning for a new vendor relationship. The 60-day data deletion window is also long -- Customer's data sits on Provider's systems for up to two months post-termination.

**Redline suggestion**:

**Clause**: Section 5.3 (Termination)
**Current language**: [No termination for convenience provision exists]
**Proposed redline**: Add new Section 5.3(c): "Customer may terminate an Order Form for convenience upon 90 days' prior written notice. In such event, Provider will refund to Customer a prorated portion of any prepaid Fees for the remainder of the Subscription Period following the effective date of termination."
**Rationale**: For a new vendor relationship, termination for convenience provides appropriate flexibility if the platform does not meet operational needs. A 90-day notice period balances Customer's flexibility with Provider's revenue predictability.
**Priority**: Should-have
**Fallback**: If Provider rejects termination for convenience, request: (a) an initial Subscription Period of no more than 12 months with the right to not renew on 60 days' notice; and (b) a performance-based termination right tied to SLA failures.

**Clause**: Section 5.5(b) (Effect of Termination -- Data Deletion)
**Current language**: "Upon Customer's request, Provider will delete Customer Content within 60 days."
**Proposed redline**: "Upon expiration or termination, Provider will, at Customer's election, return (in a standard, machine-readable format) or delete all Customer Content within 30 days. If Customer does not make an election within 30 days of termination, Provider will delete all Customer Content within an additional 30 days and certify deletion in writing."
**Rationale**: 30-day timelines for data return or deletion are market standard. Data portability in a usable format is essential to avoid vendor lock-in.
**Priority**: Should-have
**Fallback**: Accept 45-day timeline but require the data return option in a machine-readable format and written certification of deletion.

---

### 10. Representations & Warranties (Section 6) -- GREEN

**Contract says**: Mutual representations of authority, good standing, and legal compliance. Customer warrants rights to Customer Content. Provider warrants it will not materially reduce Cloud Service functionality during the Subscription Period, with a 45-day notice/45-day cure warranty remedy process.

**Standard position**: The mutual representations are standard. Provider's functionality warranty is a helpful commitment. The warranty remedy process is reasonable.

**Deviation**: The Provider warranty is limited to not "materially reducing" functionality. There is no affirmative warranty of performance, uptime, or fitness for purpose (though fitness for purpose is disclaimed in Section 7). An SLA with uptime commitments would typically be in the Order Form.

**Business impact**: Low to moderate. The warranty is a floor, not a ceiling. Customer should ensure the Order Form includes meaningful SLAs with service credits.

---

### 11. Disclaimer of Warranties (Section 7) -- GREEN

**Contract says**: Provider disclaims warranties of merchantability, fitness for a particular purpose, title, and non-infringement, except for the express warranties in Section 6.

**Standard position**: Standard disclaimer language. The carve-out for Section 6 express warranties is appropriate.

**Deviation**: None. This is boilerplate.

**Business impact**: Low risk.

---

### 12. Limitation of Liability (Section 8) -- YELLOW

**Contract says**: Each party's total liability capped at the General Cap Amount. Increased Claims subject to a higher Increased Cap Amount. Damages waiver covers lost profits (direct or indirect), consequential, special, indirect, exemplary, punitive, and incidental damages. Limitations apply to all liability theories. Exceptions: Increased Claims are not subject to the general cap; Unlimited Claims are not subject to any cap; Increased Claims and confidentiality breaches are not subject to the damages waiver.

**Standard position**: The framework is well-structured with three tiers (general cap, increased cap, unlimited). However, the actual dollar amounts (General Cap Amount, Increased Cap Amount) and the definitions of which claims fall into each tier (Increased Claims, Unlimited Claims) are all Cover Page variables that are not provided.

**Deviation**: Cannot fully assess without the Cover Page values. Key concerns from the framework:
- The damages waiver includes direct lost profits, which is more aggressive than standard. Most damages waivers exclude only indirect lost profits.
- The carve-out from the damages waiver for confidentiality breaches is customer-favorable
- Whether Provider's data breaches, IP infringement, or indemnification obligations are Increased or Unlimited Claims depends entirely on the Cover Page

**Business impact**: The framework is commercially reasonable, but the actual risk allocation depends entirely on values not present in this document. For a $150K/year deal, a general cap of 12 months' fees ($150K) is market standard. The direct lost profits waiver is concerning -- if Provider's platform failure causes Customer to lose revenue, Customer cannot recover those losses.

**Redline suggestion**:

**Clause**: Section 8.2 (Damages Waiver)
**Current language**: "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."
**Proposed redline**: "Neither party will be liable for indirect lost profits or revenues, or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."
**Rationale**: Direct lost profits are a foreseeable consequence of a breach and should remain recoverable, subject to the liability cap. Excluding direct lost profits removes a key remedy for platform failures that cause business disruption.
**Priority**: Should-have
**Fallback**: Accept the current language but ensure that data breach-related damages and IP infringement are classified as Increased Claims or Unlimited Claims on the Cover Page, where the damages waiver does not apply.

---

### 13. Indemnification (Section 9) -- YELLOW

**Contract says**: Mutual indemnification structure. Provider indemnifies Customer for Provider Covered Claims; Customer indemnifies Provider for Customer Covered Claims. Standard procedure (prompt notice, reasonable assistance, sole control of defense). Provider can obtain substitute rights, modify, or terminate/refund if required by settlement. Standard exclusions for unauthorized modifications, unauthorized use, combination with non-Provider items, or use of old versions.

**Standard position**: The framework is sound. However, the substance depends entirely on the definitions of Provider Covered Claims and Customer Covered Claims on the Cover Page. Typically:
- Provider should cover: IP infringement claims, data breach claims
- Customer should cover: claims arising from Customer Content, Customer's breach of law

**Deviation**: Cannot fully assess without Cover Page definitions. Key concerns:
- Whether IP infringement indemnification is included (standard and critical for SaaS)
- Whether data breach indemnification is included (critical given data protection priority)
- Whether indemnification obligations are subject to the liability cap or are Increased/Unlimited Claims
- The exclusion for "combination with non-Provider items" could be read broadly -- if Customer integrates the platform with its other systems (which is typical for an internal operations platform), this exclusion could gut the IP indemnity

**Business impact**: Moderate to high, depending on Cover Page definitions. The combination exclusion is a particular concern for an operational platform that will necessarily be integrated with other systems.

**Redline suggestion**:

**Clause**: Section 9.5 (Exclusions)
**Current language**: "Provider's obligations don't apply to claims from unauthorized modifications, unauthorized use, combination with non-Provider items, or use of old versions."
**Proposed redline**: "Provider's obligations don't apply to claims arising solely from (a) Customer's unauthorized modifications to the Product; (b) Customer's use of the Product in violation of this Agreement or the Documentation; (c) Customer's combination of the Product with non-Provider items, but only to the extent the claim would not have arisen absent such combination; or (d) Customer's continued use of a version of the Product after Provider has made available a non-infringing update at no additional cost."
**Rationale**: The exclusions should be narrowly scoped. The combination exclusion in particular should apply only where the combination itself caused the infringement, not where the Product independently infringes. The "old versions" exclusion should require Provider to make an updated version available.
**Priority**: Should-have
**Fallback**: Accept current language but ensure the Cover Page defines Provider Covered Claims to explicitly include third-party IP infringement and data breach claims, and classify them as Increased Claims or Unlimited Claims.

---

### 14. Confidentiality (Section 10) -- GREEN

**Contract says**: Standard mutual confidentiality provisions. Non-use and non-disclosure except as needed under the Agreement. Standard exclusions (prior knowledge, public information, independent development, authorized third-party receipt). Required disclosure permitted with reasonable advance notice. Permitted disclosure to employees, advisors, and contractors with need-to-know under equivalent confidentiality obligations.

**Standard position**: These are well-drafted, balanced confidentiality provisions. Standard carve-outs and permitted disclosures are appropriate.

**Deviation**: None material. The confidentiality term is not specified in the Standard Terms (likely a Cover Page variable). Customer should ensure a reasonable survival period (2-3 years post-termination for general confidential information; indefinite for trade secrets).

**Business impact**: Low risk. Standard provisions.

---

### 15. Reservation of Rights / IP Ownership (Section 11) -- YELLOW

**Contract says**: Provider retains all rights in the Product. Customer retains all rights in Customer Content, subject to Sections 1.5 (Customer Content license) and 1.6 (Machine Learning).

**Standard position**: The ownership allocation is clear and standard at a high level. However, the "subject to" qualifier for Sections 1.5 and 1.6 is significant. Section 1.5 grants a reasonable operational license, but Section 1.6 (as analyzed above) grants broad AI/ML training rights over Customer Content. Together, the Customer's retention of rights in Customer Content is materially qualified.

**Deviation**: The IP ownership structure itself is standard. The concern is the breadth of rights granted under Section 1.6, which effectively allows Provider to derive commercial value from Customer Content through AI/ML training. For a customer prioritizing IP ownership, this combination is problematic.

**Business impact**: Moderate to high when read together with Section 1.6. Customer retains nominal ownership but has granted significant derivative rights. See Section 1.6 analysis above for redline.

---

### 16. Assignment (Section 12.6) -- GREEN

**Contract says**: No assignment without consent, except in merger/acquisition/change of control.

**Standard position**: Standard assignment provision. The change-of-control exception is mutual and market standard.

**Deviation**: None. This is balanced.

**Business impact**: Low risk.

---

### 17. Logo Rights (Section 12.8) -- YELLOW

**Contract says**: Provider may use Customer's name and logo in marketing.

**Standard position**: Many customers require prior written approval before their name or logo is used in marketing materials. This is a standard customer-side ask.

**Deviation**: No consent requirement. Provider can use Customer's name and logo freely for marketing purposes.

**Business impact**: Low, but reputational. Customer may not want to be publicly associated with the vendor, particularly as a new relationship. This is typically an easy concession to obtain.

**Redline suggestion**:

**Clause**: Section 12.8 (Logo Rights)
**Current language**: "Provider may use Customer's name and logo in marketing."
**Proposed redline**: "Provider may use Customer's name and logo in marketing materials only with Customer's prior written consent, which will not be unreasonably withheld."
**Rationale**: Customer should control the use of its brand in third-party marketing materials.
**Priority**: Nice-to-have
**Fallback**: Permit use in customer lists and general marketing but require prior approval for case studies, press releases, and featured references.

---

### 18. Governing Law & Dispute Resolution (Section 12.3) -- YELLOW

**Contract says**: Governing Law applies without regard to conflict of laws. Chosen Courts have exclusive jurisdiction.

**Standard position**: The actual governing law and chosen courts are Cover Page variables. The framework (exclusive jurisdiction, no conflict of laws) is standard. Customer should ensure the Cover Page specifies a favorable or neutral jurisdiction.

**Deviation**: Cannot assess without Cover Page values. If Provider selects a jurisdiction far from Customer's operations or an unusual venue, this should be negotiated.

**Business impact**: Depends on Cover Page values. For a $150K/year mid-market deal, this is unlikely to be a deal-breaker but should be reviewed when the Cover Page is populated.

---

### 19. Force Majeure (Section 5.4, 12.12) -- GREEN

**Contract says**: Neither party liable for delays from Force Majeure Events, except Customer's payment obligations. Either party may terminate an affected Order Form if Force Majeure prevents the Product from materially operating for 30+ consecutive days, with prorated refund.

**Standard position**: Standard force majeure provisions. The 30-day termination trigger is reasonable. The carve-out for Customer's payment obligations is market standard. The prorated refund upon force majeure termination is customer-favorable.

**Deviation**: None material.

**Business impact**: Low risk.

---

### 20. Insurance -- NOT PRESENT

**Contract says**: No insurance provisions in the Standard Terms.

**Standard position**: For a $150K/year SaaS platform handling internal operations data, Customer should require Provider to maintain minimum insurance coverage, including: commercial general liability, professional liability (E&O), cyber liability/privacy insurance, and workers' compensation.

**Deviation**: Complete absence. Insurance requirements would typically be on the Cover Page or in the Order Form, but the Standard Terms do not even reference them.

**Business impact**: Moderate. Without insurance requirements, Customer has no assurance that Provider can satisfy indemnification obligations or cover losses from a data breach or service failure.

**Redline suggestion**:

**Clause**: Insurance (new provision)
**Current language**: [None]
**Proposed redline**: Add a new section or Order Form provision: "Provider will maintain throughout the term of this Agreement: (a) Commercial General Liability insurance with limits of not less than $2,000,000 per occurrence; (b) Professional Liability (Errors & Omissions) insurance with limits of not less than $2,000,000 per occurrence; (c) Cyber Liability insurance with limits of not less than $5,000,000 per occurrence, covering data breaches, network security failures, and privacy violations; and (d) Workers' Compensation insurance as required by applicable law. Provider will provide certificates of insurance upon Customer's request."
**Rationale**: Insurance requirements ensure Provider has financial backing for its indemnification and liability obligations, which is particularly important for a vendor handling sensitive operational data.
**Priority**: Should-have
**Fallback**: Accept lower limits appropriate for the deal size (e.g., $1M general liability, $2M cyber liability) and require certificate of insurance at signing and annually thereafter.

---

### 21. Survival (Section 5.6) -- GREEN

**Contract says**: Extensive list of surviving sections including Feedback/Usage Data, Machine Learning, Restrictions, Payment, Termination effects, Warranties, Disclaimer, Limitation of Liability, Indemnification, Confidentiality, Reservation of Rights, General Terms, and Definitions.

**Standard position**: Survival clauses are standard. The list is comprehensive and appropriate.

**Deviation**: The survival of Section 1.4 (Feedback) and Section 1.6 (Machine Learning) means Provider's rights to use Feedback and to train AI/ML models on previously collected data survive termination. This is consistent with the grants but worth noting given the concerns about those sections.

**Business impact**: If the Section 1.6 concerns are addressed (by excluding Customer Content from AI/ML training), the survival provision is standard. If not, the survival of Section 1.6 means Provider can continue to use Customer Content collected during the term for AI/ML training even after termination, in perpetuity.

---

## Negotiation Strategy

### Tier 1 -- Must-Haves (Deal Breakers)

1. **Remove Customer Content from AI/ML training (Section 1.6)**: This is the single most important issue. Provider should not be training its AI models on Customer's operational data. Limit AI/ML training to Usage Data only, with appropriate aggregation and de-identification.

2. **Strengthen Data Protection (Section 3)**: Require a DPA as an exhibit, covering all applicable data protection laws. Include breach notification timelines, sub-processor controls, security standards, and audit rights. This is non-negotiable for a platform processing internal operations data.

### Tier 2 -- Should-Haves (Strong Preferences)

3. **Termination for convenience (Section 5.3)**: For a new vendor, Customer needs an exit option. A 90-day notice period with prorated refund is a reasonable ask.

4. **Narrow the indemnification exclusions (Section 9.5)**: The combination exclusion must be scoped to apply only where the combination itself caused the claim.

5. **Fix the damages waiver (Section 8.2)**: Remove "direct" from the lost profits exclusion so that direct lost profits remain recoverable.

6. **Improve suspension notice (Section 2.2)**: Require advance written notice before suspension except in emergencies.

7. **Reduce data deletion timeline (Section 5.5(b))**: 30 days instead of 60, with a data return option in machine-readable format.

8. **Add insurance requirements**: Cyber liability insurance is particularly important.

### Tier 3 -- Nice-to-Haves (Concession Candidates)

9. **Logo rights consent (Section 12.8)**: Require prior approval for marketing use.

10. **Feedback clause boundaries (Section 1.4)**: Clarify that Feedback does not include Confidential Information.

11. **Security testing rights (Section 2.1(a)(v))**: Right to conduct security assessments with prior notice.

### Recommended Approach

Lead with the two must-haves (AI/ML data rights and data protection). These are strong market-standard positions and should be non-controversial for a responsible vendor. Frame them as regulatory compliance requirements rather than purely commercial asks.

Package the Tier 2 items as a group -- present them together with the Tier 1 items to show a comprehensive but reasonable markup. Be prepared to trade Tier 3 items (logo rights, feedback boundaries) to secure Tier 2 wins (termination for convenience, indemnification scope).

Keep in mind that this is a Common Paper standard form, which is designed to be balanced. Provider may resist modifications to the Standard Terms and prefer to address issues on the Cover Page/Order Form. Use this to Customer's advantage: many of the critical variables (liability caps, covered claims, governing law) are Cover Page items where negotiation is expected.

### Timeline Considerations

With a 2-week deadline:
- **Week 1**: Send the redline with all Tier 1 and Tier 2 items. Identify a primary negotiation contact. Request Provider's DPA and security documentation (SOC 2 report, security whitepaper).
- **Week 2**: Negotiate remaining open items. Finalize Cover Page values. Concede Tier 3 items strategically to close on Tier 1 and Tier 2.
- The 2-week timeline is tight but feasible for a mid-market deal. Do not let time pressure force acceptance of the AI/ML or data protection issues without resolution.

---

## Next Steps

1. **Request Provider's DPA**: Ask Provider for their standard Data Processing Agreement immediately. Review it against the requirements identified above.
2. **Request SOC 2 Report**: Ask Provider for their most recent SOC 2 Type II report or equivalent security certification.
3. **Prepare the redline**: Incorporate the redline suggestions above into a marked-up version of the agreement, prioritizing Tier 1 and Tier 2 items.
4. **Review Cover Page / Order Form**: When available, review the Cover Page to assess the actual values for liability caps, covered claims, governing law, and other critical variables. Many issues flagged as YELLOW in this review may be resolved or escalated based on Cover Page values.
5. **Legal counsel review**: Have qualified legal counsel review the marked-up agreement, particularly the AI/ML and data protection provisions, before sending to Provider.
6. **Internal stakeholder alignment**: Confirm with internal stakeholders (IT security, procurement, data privacy) that the proposed positions align with organizational requirements.

---

*This review is based on general commercial standards for mid-market SaaS agreements from the customer perspective. No organizational playbook was available. All findings should be reviewed by qualified legal counsel before being relied upon for legal decisions.*
