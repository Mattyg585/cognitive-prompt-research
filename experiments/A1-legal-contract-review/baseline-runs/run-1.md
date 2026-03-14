## Contract Review Summary

**Document**: Common Paper Cloud Service Agreement — Standard Terms Version 2.1
**Parties**: Provider (unnamed SaaS vendor) and Customer (our organization)
**Your Side**: Customer (buyer)
**Deadline**: 2 weeks
**Review Basis**: Generic Standards (no organizational playbook found)

> **Note**: No organizational playbook was found. This review uses widely-accepted commercial standards as the baseline for a mid-market SaaS procurement ($150K/year). All analysis should be reviewed by qualified legal professionals before being relied upon for legal decisions.

---

## Key Findings

1. **RED — Machine Learning / AI Training on Customer Data (Section 1.6)**: Provider claims the right to use Customer Content and Usage Data to train AI/ML models. Even with aggregation and de-identification requirements, this is a material data rights concern for a customer. This clause is unusual and goes well beyond what is necessary for service delivery.

2. **RED — Data Protection Is Inadequate (Section 3.1)**: The DPA is only required for GDPR-governed Personal Data, not for all Personal Data. There is no breach notification timeline, no sub-processor controls, no cross-border transfer mechanism, and no data security standards specified in the agreement itself. For a $150K operational platform, this is insufficient.

3. **YELLOW — Feedback Clause Is Overbroad (Section 1.4)**: Provider receives an unrestricted, perpetual right to use all Feedback "freely without any restriction or obligation." While feedback clauses are common, the lack of any limitation is broader than market standard.

4. **YELLOW — Limitation of Liability Depends on Undefined Cover Page Variables (Section 8)**: The General Cap Amount, Increased Cap Amount, Increased Claims, and Unlimited Claims are all defined by reference to the Cover Page / Order Form, which is not provided. The framework is sound but the actual protections are unknown until these are set. This requires careful attention during Order Form negotiation.

5. **YELLOW — Logo Rights Without Consent (Section 12.8)**: Provider may use Customer's name and logo in marketing materials without requiring prior consent. Standard practice is to require opt-in or at minimum prior written approval.

---

## Clause-by-Clause Analysis

### 1. Service & Access (Section 1.1–1.3) — GREEN

**Contract says**: Customer may access and use the Cloud Service for internal business purposes during the Subscription Period. Support is as described in the Order Form. Customer is responsible for user account security. Affiliate Orders create separate agreements.

**Standard position**: Standard SaaS access grant for internal use. Affiliate structure is reasonable.

**Deviation**: None material. The Affiliate separation clause is actually favorable to Customer — it limits cross-liability between Customer and its Affiliates.

**Business impact**: Acceptable. Ensure the Order Form adequately defines support levels (response times, availability SLA, escalation paths).

---

### 2. Feedback and Usage Data (Section 1.4) — YELLOW

**Contract says**: Customer gives Feedback "AS IS" and Provider may use all Feedback "freely without any restriction or obligation." Provider may collect and analyze Usage Data and use it freely to maintain, improve, enhance, and promote its products and services. Usage Data disclosed to third parties must be aggregated and non-identifying.

**Standard position**: Feedback clauses are common, but market standard typically includes some guardrails: Feedback should not include Customer Confidential Information, and the license grant should be limited to incorporating Feedback into Provider's products (not "any use without restriction"). Usage Data collection is standard but should be limited to service improvement purposes.

**Deviation**: The Feedback clause is broader than market standard. "Freely without any restriction or obligation" is essentially an unlimited, perpetual, irrevocable license with no boundaries. Usage Data provisions are mostly acceptable due to the aggregation requirement for third-party disclosure.

**Business impact**: Low-to-moderate risk. If Customer inadvertently shares proprietary methodology or business logic as "Feedback," Provider has unrestricted rights to use it. For a $150K operational platform, this is unlikely to be a deal-breaker but should be narrowed.

**Redline suggestion**:

**Clause**: Section 1.4 (Feedback and Usage Data)
**Current language**: "Provider may use all Feedback freely without any restriction or obligation."
**Proposed redline**: "Provider may use Feedback to develop, improve, and enhance Provider's products and services without restriction or obligation, provided that Provider shall not identify Customer as the source of any Feedback in any public-facing materials without Customer's prior written consent."
**Rationale**: Narrowing the Feedback license to product improvement purposes aligns with the intent of the clause while protecting against unintended broad grants.
**Priority**: Nice-to-have
**Fallback**: Accept the current language but add: "Feedback shall not include Customer's Confidential Information unless expressly designated as Feedback by Customer."

---

### 3. Customer Content (Section 1.5) — GREEN

**Contract says**: Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings. Customer is responsible for accuracy.

**Standard position**: This is well-scoped. The "as needed to provide and maintain" limitation is the market standard formulation.

**Deviation**: None. The phrase "and related offerings" is slightly broader than "the Product" alone, but this is reasonable for service delivery.

**Business impact**: Acceptable.

---

### 4. Machine Learning / AI Training (Section 1.6) — RED

**Contract says**: Usage Data and Customer Content may be used to develop, train, or enhance AI/ML models that are part of Provider's products, including third-party components. Customer authorizes this processing. Data must be aggregated before use, and Provider will use "commercially reasonable efforts consistent with industry standard technology" to de-identify it. Provider's obligations regarding Personal Data under Applicable Data Protection Laws are preserved.

**Standard position**: Using Customer Content to train AI/ML models is NOT market standard for enterprise SaaS. Most enterprise customers require explicit opt-out rights or do not permit this at all. Using Usage Data (metadata, telemetry) for product improvement is generally acceptable, but Customer Content (the actual data the customer puts into the system) is a different category entirely.

**Deviation**: This is a significant deviation from customer-protective standards. Key issues:
- Customer Content is explicitly included in AI/ML training data
- The de-identification standard is "commercially reasonable efforts" — not a guarantee
- Third-party components of the Product may also receive this data
- There is no opt-out mechanism
- The aggregation requirement provides some protection, but aggregated Customer Content may still contain proprietary business patterns or insights

**Business impact**: HIGH. For a $150K/year internal operations platform, Customer Content likely includes sensitive operational data. Allowing the vendor to train AI models (including third-party models) on this data, even in aggregated/de-identified form, creates risk of:
- Competitive intelligence leakage through model outputs
- Loss of control over proprietary data patterns
- Regulatory risk if de-identification proves inadequate
- Data flowing to unknown third parties through "third-party components"

**Redline suggestion**:

**Clause**: Section 1.6 (Machine Learning)
**Current language**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes."
**Proposed redline**: "Usage Data (but not Customer Content) may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, provided that such Usage Data is aggregated and de-identified before any such use. Customer Content shall not be used for any purpose other than providing the Cloud Service to Customer as described in Section 1.5. Provider shall not use Customer Content or Usage Data to train or enhance third-party artificial intelligence or machine learning models without Customer's prior written consent."
**Rationale**: Customer Content represents proprietary business data submitted to the platform for operational use. Permitting its use in AI/ML training, even in aggregated form, exceeds the scope of the service relationship and creates data governance risks that are inconsistent with Customer's compliance obligations.
**Priority**: Must-have
**Fallback**: If Provider insists on some ML rights: (a) Remove Customer Content entirely — limit to Usage Data only; (b) Require strict anonymization (not merely "commercially reasonable" de-identification); (c) Exclude third-party model training; (d) Add an opt-out mechanism Customer can exercise at any time.

**Recommended escalation path**: This should be reviewed by senior counsel or data governance. If the vendor will not remove Customer Content from ML training, consider whether the data governance risk is acceptable for this platform.

---

### 5. Restrictions on Customer (Section 2.1) — GREEN

**Contract says**: Standard restrictions: no reverse engineering, no sublicensing, no derivative works, no security testing, no competitive development, no High Risk Activities, no unauthorized access.

**Standard position**: These are standard SaaS use restrictions. The restriction on security/vulnerability testing (2.1(a)(v)) is common but may conflict with Customer's security assessment requirements.

**Deviation**: Minor. The security testing restriction could be an issue if Customer's security team needs to conduct penetration testing or vulnerability assessments.

**Business impact**: Low. If Customer requires the right to conduct security assessments, this should be addressed in the Order Form. Otherwise, standard.

---

### 6. Suspension (Section 2.2) — YELLOW

**Contract says**: Provider may suspend access for unpaid balances (30+ days), breach of restrictions, or use that "materially and negatively impacts the Product or others." Provider will "try to inform" Customer before suspension "when practical." Reinstatement requires resolution of the underlying issue.

**Standard position**: Suspension rights are standard, but market practice requires: (a) written notice before suspension (except in emergencies); (b) a cure period before suspension takes effect; (c) a defined process for reinstatement. "Try to inform" and "when practical" are weak protections.

**Deviation**: The lack of a guaranteed notice period and cure opportunity before suspension is below standard. For a $150K operational platform, unannounced suspension could cause significant business disruption.

**Business impact**: Moderate. If this platform supports internal operations, even a brief unannounced suspension could disrupt workflows. The "materially and negatively impacts" trigger is also subjective — Provider has broad discretion.

**Redline suggestion**:

**Clause**: Section 2.2 (Suspension)
**Current language**: "Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical."
**Proposed redline**: "Provider will provide Customer at least 5 business days' prior written notice before suspending Customer's access to the Product, except where immediate suspension is reasonably necessary to prevent imminent harm to the Product, other customers, or third parties, in which case Provider will notify Customer as soon as practicable and in no event later than 24 hours after suspension."
**Rationale**: Advance notice of suspension protects operational continuity and gives Customer the opportunity to cure any issues before service disruption.
**Priority**: Should-have
**Fallback**: Accept "with or without notice" but require: (a) Provider must notify Customer within 24 hours of any suspension, (b) Provider must provide a clear description of the issue, and (c) Provider must reinstate access within 2 business days of Customer curing the issue.

---

### 7. Privacy & Security (Section 3) — RED

**Contract says**: Before submitting GDPR-governed Personal Data, Customer must enter into a DPA with Provider. If a DPA exists, it controls. Customer must not submit Prohibited Data unless the Order Form authorizes it.

**Standard position**: For a $150K/year operational SaaS platform, data protection provisions should include:
- A DPA requirement for all Personal Data, not just GDPR-governed data (CCPA, state privacy laws, and other jurisdictions also require contractual protections)
- Specified data breach notification timeline (e.g., 72 hours or without undue delay)
- Sub-processor notification and objection rights
- Cross-border data transfer mechanisms (SCCs, adequacy decisions)
- Data security standards (SOC 2, ISO 27001, or equivalent)
- Audit rights
- Data deletion/return obligations on termination (beyond the bare provision in 5.5(b))
- Purpose limitation for data processing

**Deviation**: Section 3 is materially thin compared to market standard for enterprise SaaS:
- The DPA is only required for GDPR-governed Personal Data — this leaves non-GDPR personal data (US state law, PIPEDA, etc.) without contractual data processing protections
- No data breach notification timeline is specified in the agreement itself
- No sub-processor transparency or objection rights
- No cross-border transfer mechanism
- No data security standards or certifications required
- No audit rights for Customer
- Data deletion on termination is 60 days upon request (Section 5.5(b)), which is reasonable but should be mandatory, not request-dependent
- No purpose limitation beyond "as needed to provide and maintain the Product" (Section 1.5)

**Business impact**: HIGH. As an internal operations platform, this system will likely process employee data, potentially customer data, and operational data. Without adequate contractual data protection:
- Customer may be unable to satisfy its own regulatory obligations (CCPA, state privacy laws)
- There is no contractual recourse if Provider has a data breach and delays notification
- Customer has no visibility into or control over sub-processors handling its data
- Data may be transferred to jurisdictions with inadequate protection without Customer's knowledge

**Redline suggestion**:

**Clause**: Section 3.1 (Personal Data)
**Current language**: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider."
**Proposed redline**: "The parties shall enter into Provider's Data Processing Addendum ('DPA'), which is incorporated by reference. The DPA shall address, at minimum: (a) processing of all Personal Data (not limited to GDPR-governed data) in accordance with Applicable Data Protection Laws; (b) data breach notification to Customer without undue delay and in no event later than 72 hours after discovery; (c) a current list of sub-processors with advance notice and objection rights for changes; (d) appropriate cross-border data transfer mechanisms; (e) Provider's maintenance of industry-standard security certifications (SOC 2 Type II or equivalent); and (f) Customer's right to audit Provider's compliance with the DPA no more than once per year."
**Rationale**: The current data protection provisions do not address the full scope of Applicable Data Protection Laws (including US state privacy laws) and lack the operational data protection terms necessary for an enterprise SaaS platform processing personal and sensitive operational data.
**Priority**: Must-have
**Fallback**: At minimum, require: (a) DPA for all Personal Data, not just GDPR; (b) 72-hour breach notification; (c) sub-processor list with notification of changes.

**Recommended escalation path**: Request Provider's existing DPA for review. If Provider does not have a DPA, this is a significant vendor maturity concern. Escalate to information security and privacy teams for assessment.

---

### 8. Payment & Taxes (Section 4) — GREEN

**Contract says**: Fees are in USD, non-refundable (except for specific termination refund rights), exclusive of taxes. Invoicing in arrears for usage-based and in advance for other fees. Customer responsible for taxes (except Provider's income taxes). Payment disputes must be raised before due date or within 30 days of auto-payment, with a 15-day resolution window.

**Standard position**: These are standard commercial payment terms. The payment dispute process is reasonable and well-defined.

**Deviation**: None material. The non-refundable fee structure is standard for SaaS. The dispute mechanism provides adequate protection.

**Business impact**: Acceptable. Ensure the Order Form specifies payment terms (Net 30 or Net 45 is standard for mid-market).

---

### 9. Term & Termination (Section 5) — YELLOW

**Contract says**: Agreement runs for the Subscription Period and auto-renews unless non-renewal notice is given before the Non-Renewal Notice Date (defined in Order Form). Either party can terminate for material breach with 30 days' cure. Either party can terminate for incurable breach, dissolution, or insolvency. Force majeure termination after 30 days with prorated refund. On termination: Customer loses access, Provider deletes Customer Content within 60 days upon request, Confidential Information returned/destroyed.

**Standard position**: Generally reasonable structure. Key concerns:
- No termination for convenience — Customer is locked in for the full Subscription Period
- The Non-Renewal Notice Date is undefined (on Cover Page) — if it's set at 90+ days, Customer could miss the window and be auto-renewed
- Data deletion is only "upon Customer's request" — it should be mandatory
- No transition assistance provisions
- Survival of Section 1.6 (Machine Learning) means the ML training rights on aggregated data survive termination

**Deviation**: The lack of termination for convenience is below standard for a non-strategic $150K/year deal where Customer is the buyer. Market practice for mid-market SaaS increasingly includes termination for convenience with 30-90 days' notice (though sometimes with early termination fees). The survival of ML rights post-termination is concerning.

**Business impact**: Moderate. If the platform underperforms or Customer's needs change, Customer is locked in until the Subscription Period ends. For a new, non-strategic vendor, this reduces Customer's leverage.

**Redline suggestion**:

**Clause**: Section 5.3 (Termination)
**Current language**: [No termination for convenience provision exists]
**Proposed redline**: Add new Section 5.3(c): "Customer may terminate an Order Form for convenience upon 90 days' prior written notice. In such event, Provider will pay to Customer a prorated refund of any prepaid Fees for the remainder of the Subscription Period following the effective date of termination."
**Rationale**: Termination for convenience provides necessary flexibility for a non-strategic vendor relationship and is increasingly standard in mid-market SaaS procurement.
**Priority**: Should-have
**Fallback**: If Provider rejects termination for convenience: (a) negotiate a shorter initial Subscription Period (e.g., 12 months instead of multi-year); (b) ensure the Non-Renewal Notice Date provides at least 60 days; (c) add a "termination for convenience" right that triggers only after the initial Subscription Period.

**Clause**: Section 5.5(b) (Effect of Termination — Data Deletion)
**Current language**: "Upon Customer's request, Provider will delete Customer Content within 60 days."
**Proposed redline**: "Provider will, within 60 days of expiration or termination, delete all Customer Content and certify such deletion in writing. Upon Customer's request made within 30 days of expiration or termination, Provider will first export and make available to Customer all Customer Content in a standard, machine-readable format before deletion."
**Rationale**: Data return and deletion should be mandatory post-termination, not contingent on Customer's request. Customer should also have the right to export its data before deletion.
**Priority**: Should-have
**Fallback**: At minimum, require: (a) Provider notifies Customer before deleting Customer Content and provides a 30-day window for Customer to request export; (b) deletion is mandatory after the export window closes.

**Clause**: Section 5.6 (Survival)
**Current language**: "The following sections will survive expiration or termination of the Agreement: Section 1.4 (Feedback and Usage Data), Section 1.6 (Machine Learning)..."
**Proposed redline**: Remove Section 1.6 (Machine Learning) from the survival clause. If ML rights are retained at all, they should not survive termination of the agreement.
**Rationale**: Provider's right to use Customer data for ML training purposes should end when the service relationship ends.
**Priority**: Must-have (if Section 1.6 is not fully revised per the RED flag above)
**Fallback**: If Provider insists Section 1.6 survives: limit survival to Usage Data that was aggregated and de-identified prior to termination, and exclude Customer Content entirely.

---

### 10. Representations & Warranties (Section 6) — GREEN

**Contract says**: Mutual representations of authority, valid existence, and legal compliance. Customer warrants rights to Customer Content. Provider warrants it will not materially reduce Cloud Service functionality during the Subscription Period. Warranty remedy: 45 days to notify, 45 days to cure, termination with prorated refund if not cured.

**Standard position**: These are standard but minimal. The Provider warranty is limited to not "materially reducing" functionality — it does not warrant that the service will perform as described, meet specifications, or conform to documentation.

**Deviation**: The Provider warranty is weaker than market standard. Most enterprise SaaS agreements include a warranty that the service will perform materially in accordance with the Documentation. The 45-day notice window and 45-day cure period are generous to Provider.

**Business impact**: Low-to-moderate. The narrow warranty means Customer's remedy for service deficiencies is limited. However, this is partially offset by the practical reality that if the service does not perform, Customer can choose not to renew.

---

### 11. Disclaimer of Warranties (Section 7) — GREEN

**Contract says**: No guarantees of safety, security, or error-free operation. Both parties disclaim all warranties except those in Section 6, including merchantability, fitness for a particular purpose, title, and non-infringement.

**Standard position**: Standard commercial disclaimer. The mutual nature is balanced.

**Deviation**: None material.

**Business impact**: Acceptable. Standard SaaS practice.

---

### 12. Limitation of Liability (Section 8) — YELLOW

**Contract says**: Each party's total liability capped at the General Cap Amount (defined on Cover Page). Increased Claims have a separate, higher cap (Increased Cap Amount). Both parties waive consequential, special, indirect, exemplary, punitive, and incidental damages, plus lost profits/revenues. Exceptions: Increased Claims are not subject to the General Cap. Unlimited Claims are not subject to any cap. The consequential damages waiver does not apply to Increased Claims or breach of confidentiality.

**Standard position**: The framework is well-structured (three tiers: General Cap, Increased Cap, Unlimited). This is actually a sophisticated limitation of liability structure that provides flexibility. However, the actual cap amounts are undefined (on the Cover Page), which makes it impossible to assess whether the caps are adequate.

**Deviation**: The structure is acceptable but:
- Cannot assess adequacy without knowing the General Cap Amount and Increased Cap Amount
- The damages waiver includes direct lost profits, which is unusual — most waivers cover only indirect/consequential lost profits. Direct lost profits (e.g., Provider's breach directly causes Customer to lose a client) should arguably be recoverable.
- The consequential damages waiver does not carve out data breach or IP infringement by default — these are only addressed if they are classified as Increased Claims on the Cover Page

**Business impact**: Moderate. The practical impact depends entirely on the Cover Page values. Key points for Order Form negotiation:
- General Cap Amount should be at least 12 months of fees ($150K minimum)
- Increased Claims should include data breach and IP infringement
- Increased Cap Amount should be at least 2x the General Cap Amount
- Unlimited Claims should include fraud, willful misconduct, and breach of confidentiality involving Customer Content

**Redline suggestion**:

**Clause**: Section 8.2 (Damages Waiver)
**Current language**: "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."
**Proposed redline**: "Neither party will be liable for indirect lost profits or revenues, or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility. This waiver does not apply to (a) Provider's breach of Section 3 (Privacy & Security) or Section 10 (Confidentiality) with respect to Customer Content or Personal Data, or (b) either party's Unlimited Claims."
**Rationale**: Direct lost profits resulting from Provider's breach should remain recoverable, and data-related breaches should not be subject to the consequential damages waiver given the operational nature of the platform.
**Priority**: Should-have
**Fallback**: Accept the current waiver but ensure that data breach and IP infringement are classified as Increased Claims on the Cover Page, which would exempt them from the 8.2 waiver per Section 8.4.

---

### 13. Indemnification (Section 9) — GREEN

**Contract says**: Mutual indemnification structure. Provider indemnifies for Provider Covered Claims; Customer indemnifies for Customer Covered Claims (both defined on Cover Page). Standard procedure: prompt notice, reasonable assistance, sole control of defense. Provider may obtain continued use rights, replace/modify, or terminate and refund for IP claims. Exclusions for unauthorized modifications, unauthorized use, combination with non-Provider items, or old versions.

**Standard position**: The structure is sound and balanced. The specific Covered Claims are defined on the Cover Page, so the adequacy depends on those definitions. Standard exclusions are reasonable.

**Deviation**: Cannot fully assess without the Cover Page definitions. For a customer-side review:
- Provider Covered Claims should include at minimum: third-party IP infringement claims arising from Customer's authorized use of the Product
- Customer Covered Claims should be limited to: claims arising from Customer Content and Customer's breach of the Agreement
- The indemnity should be subject to the Increased Cap, not the General Cap

**Business impact**: Low, assuming Cover Page definitions are appropriate. The IP remediation options in 9.4 (obtain rights, replace/modify, or terminate and refund) are standard and reasonable.

---

### 14. Confidentiality (Section 10) — GREEN

**Contract says**: Standard non-use and non-disclosure obligations. Standard exclusions (prior knowledge, public information, independent development, authorized third-party receipt). Required disclosures permitted with reasonable advance notice. Permitted disclosures to employees, advisors, and contractors with need-to-know and equivalent confidentiality obligations.

**Standard position**: These are standard confidentiality provisions.

**Deviation**: None material. The confidentiality term is not specified (no expiration). Section 5.6(b) allows retention per standard backup/retention policies, with continued confidentiality obligations — this is reasonable.

**Business impact**: Acceptable.

---

### 15. Reservation of Rights (Section 11) — GREEN

**Contract says**: Provider retains all rights in the Product. Customer retains all rights in Customer Content, subject to Sections 1.5 (Customer Content use for service delivery) and 1.6 (Machine Learning).

**Standard position**: The IP ownership allocation is clear and standard — each party retains its own IP. However, the "subject to Section 1.6" qualification is concerning because it subordinates Customer's ownership of Customer Content to the ML training rights.

**Deviation**: The reservation itself is standard. The concern here is with Section 1.6 (addressed above as RED).

**Business impact**: See Section 1.6 analysis. If Section 1.6 is revised, this section becomes fully acceptable.

---

### 16. Assignment (Section 12.6) — GREEN

**Contract says**: No assignment without consent, except in merger, acquisition, or change of control.

**Standard position**: Standard. The change-of-control exception is mutual and market-standard.

**Deviation**: None.

**Business impact**: Acceptable. Note that this means if Provider is acquired by a competitor or an entity Customer would prefer not to do business with, the agreement transfers to the acquirer. Customer may want to negotiate a termination right upon Provider change of control, but this is a nice-to-have.

---

### 17. Logo Rights (Section 12.8) — YELLOW

**Contract says**: Provider may use Customer's name and logo in marketing.

**Standard position**: Many vendors request logo rights, but market standard requires prior written consent or at minimum an opt-out right. A blanket grant without consent is below standard.

**Deviation**: No consent requirement. Provider can use Customer's name and logo freely.

**Business impact**: Low. Reputational risk is minimal for most organizations, but some companies have strict brand guidelines or prefer not to be publicly associated with specific vendors.

**Redline suggestion**:

**Clause**: Section 12.8 (Logo Rights)
**Current language**: "Provider may use Customer's name and logo in marketing."
**Proposed redline**: "Provider may use Customer's name and logo in marketing materials, including Customer lists and case studies, only with Customer's prior written consent, which shall not be unreasonably withheld."
**Rationale**: Customer's brand assets should be used only with Customer's approval, consistent with Customer's brand guidelines and communications policies.
**Priority**: Nice-to-have
**Fallback**: Add: "Customer may revoke this right at any time upon written notice to Provider."

---

### 18. Force Majeure (Section 5.4, 12.12) — GREEN

**Contract says**: Neither party liable for delays from Force Majeure Events, except Customer's payment obligations. Either party may terminate an affected Order Form if a Force Majeure Event prevents material operation for 30+ consecutive days. Provider pays prorated refund.

**Standard position**: Standard. The 30-day trigger for termination is reasonable. The carveout for Customer's payment obligations is standard. The prorated refund is customer-protective.

**Deviation**: None material.

**Business impact**: Acceptable.

---

### 19. Governing Law & Dispute Resolution (Section 12.3) — YELLOW

**Contract says**: Governing Law applies without regard to conflict of laws. Chosen Courts have exclusive jurisdiction. (Both defined on Cover Page.)

**Standard position**: The framework is fine, but the actual governing law and jurisdiction are defined on the Cover Page and not provided for review. These terms are material.

**Deviation**: Cannot assess without Cover Page. For a mid-market US deal, Customer should ensure:
- Governing law is a well-established commercial jurisdiction (Delaware, New York, or Customer's home state)
- Chosen Courts are reasonably convenient for Customer
- Consider whether arbitration or litigation is preferred

**Business impact**: Depends entirely on Cover Page. Flag for Order Form review.

---

### 20. Insurance — NOT ADDRESSED

**Contract says**: No insurance provisions in the Standard Terms.

**Standard position**: For a $150K/year operational SaaS platform, Customer should require Provider to maintain at minimum: (a) Commercial General Liability ($1M per occurrence / $2M aggregate); (b) Professional Liability / E&O ($2M); (c) Cyber Liability / Data Breach ($2M); (d) Workers' Compensation (statutory limits).

**Deviation**: Complete absence of insurance requirements.

**Business impact**: Moderate. Without insurance requirements, Provider's financial ability to satisfy indemnification or liability obligations is unknown. This is particularly concerning given the data protection gaps identified above.

**Redline suggestion**:

**Clause**: [New Section — Insurance]
**Current language**: [None]
**Proposed redline**: Add new section: "Provider shall maintain, at its own expense, the following insurance coverage during the term of this Agreement: (a) Commercial General Liability with limits of not less than $1,000,000 per occurrence and $2,000,000 in the aggregate; (b) Professional Liability / Errors & Omissions with limits of not less than $2,000,000 per claim; (c) Cyber Liability / Technology Errors & Omissions with limits of not less than $2,000,000 per claim; and (d) Workers' Compensation as required by applicable law. Provider shall provide certificates of insurance upon Customer's request."
**Rationale**: Insurance requirements ensure Provider has the financial resources to back its contractual obligations, particularly indemnification and data breach response.
**Priority**: Should-have
**Fallback**: At minimum, require Provider to confirm it maintains commercially reasonable insurance coverage and provide a certificate upon request.

---

## Negotiation Strategy

### Tier 1 — Must-Haves (Deal Breakers)

1. **Revise Section 1.6 (Machine Learning)**: Remove Customer Content from ML training scope entirely. This is the single most important issue. If Provider will not agree, escalate to senior counsel and data governance for a risk-acceptance decision.

2. **Strengthen Section 3 (Data Protection)**: Require a comprehensive DPA covering all Personal Data, with breach notification timelines, sub-processor controls, and cross-border transfer mechanisms. Request Provider's existing DPA for review immediately.

3. **Remove Section 1.6 from survival clause (Section 5.6)**: ML training rights should not survive termination.

### Tier 2 — Should-Haves (Strong Preferences)

4. **Add termination for convenience (Section 5.3)**: With 90 days' notice and prorated refund.

5. **Strengthen suspension protections (Section 2.2)**: Require advance notice except in emergencies.

6. **Revise data deletion to be mandatory (Section 5.5(b))**: With data export rights and written certification.

7. **Narrow the consequential damages waiver (Section 8.2)**: Carve out data breach and direct lost profits.

8. **Add insurance requirements**: At minimum cyber liability and E&O.

9. **Negotiate adequate Cover Page values**: General Cap at 12 months of fees minimum; data breach and IP infringement as Increased Claims.

### Tier 3 — Nice-to-Haves (Concession Candidates)

10. **Narrow Feedback clause (Section 1.4)**: Limit to product improvement purposes.

11. **Require consent for logo use (Section 12.8)**: Prior written approval.

12. **Add Provider change-of-control termination right**: Customer right to terminate if Provider is acquired.

### Recommended Approach

**Lead with items 1-3.** These are non-negotiable from a data governance perspective. Frame the conversation around regulatory compliance and data protection — these are increasingly well-understood requirements that most mature SaaS vendors expect.

**Trade items 10-12 to secure items 4-9.** The Feedback clause, logo rights, and change-of-control termination right are reasonable concessions that signal good faith while protecting the positions that matter.

**Request the Provider's DPA and Cover Page / Order Form template immediately.** Many of the issues identified in this review (liability caps, governing law, Covered Claims definitions) depend on Cover Page values that are not included in the Standard Terms. The negotiation cannot be fully scoped until these are reviewed.

### Timeline Considerations

With a 2-week deadline:
- **Week 1**: Send initial redline with all Tier 1 and Tier 2 items. Request the DPA and Cover Page simultaneously. Begin internal review of DPA when received.
- **Week 2**: Negotiate responses. Focus remaining time on Tier 1 items. Concede Tier 3 items as needed to close.
- **Escalation**: If Tier 1 items are not resolved by end of Week 1, escalate to senior counsel and consider whether the timeline needs to extend.

---

## Next Steps

1. **Immediately request Provider's DPA and Order Form / Cover Page template.** These documents are essential to complete the review.
2. **Send initial redline** incorporating all Tier 1 and Tier 2 items above.
3. **Engage information security / privacy team** to review the ML training clause (Section 1.6) and assess data governance risk.
4. **Review Provider's security posture**: Request SOC 2 Type II report, security questionnaire responses, and sub-processor list.
5. **Negotiate Cover Page values** with the following minimums:
   - General Cap Amount: 12 months of fees ($150,000)
   - Increased Claims: Data breach, IP infringement, breach of confidentiality
   - Increased Cap Amount: 2x annual fees ($300,000)
   - Unlimited Claims: Fraud, willful misconduct, indemnification obligations
   - Non-Renewal Notice Date: At least 60 days before end of Subscription Period
   - Governing Law: Customer's preferred jurisdiction
6. **Calendar the Non-Renewal Notice Date** once the Order Form is signed to avoid inadvertent auto-renewal.

---

> **Disclaimer**: This analysis is based on widely-accepted commercial standards for mid-market SaaS procurement and should be reviewed by qualified legal counsel before being relied upon for legal decisions. No organizational playbook was applied.
