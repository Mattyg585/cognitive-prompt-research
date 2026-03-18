# Contract Auditor — Stage 1 Output

## Contract Overview

**Type**: Cloud Service Agreement (SaaS subscription)
**Parties**: Provider (unnamed, the SaaS vendor) and Customer (the buyer)
**User's side**: Customer
**Commercial structure**: Customer purchases access to Provider's Cloud Service for internal business operations at $150K/year. Provider delivers access to the Cloud Service, related Software, and Documentation during a Subscription Period, with Technical Support as described in the Order Form. Fees are non-refundable except in specific termination scenarios. The agreement operates through a Framework Terms / Order Form structure, where each Order Form creates its own subscription period and can be independently terminated, but Framework Terms termination kills all Order Forms beneath it.
**Effective date / Term**: Governed by the Order Form. The Agreement starts on the Order Date, runs through the Subscription Period, and auto-renews unless a party gives notice before the Non-Renewal Notice Date (a variable defined on the Cover Page, not in the Standard Terms).

## The Deal's Commercial Logic

This is a standard-form cloud services agreement built on Common Paper's open template, structured to be vendor-friendly in its defaults while leaving key commercial terms to the Cover Page and Order Form. The architecture is deliberate: the Standard Terms establish a baseline that favours Provider on data rights, liability, and operational flexibility, while the variable mechanism lets the parties negotiate specific thresholds (caps, notice periods, carveouts) deal by deal without touching the boilerplate.

The commercial exchange is straightforward — access to a SaaS platform for internal operations in return for subscription fees — but the contract's treatment of the data layer is where the real balance of interests sits. Provider has secured broad rights not just to operate on Customer Content (Section 1.5) but to harvest Usage Data freely for product improvement and promotion (Section 1.4), and — notably — to use both Usage Data and Customer Content for AI/ML training purposes (Section 1.6). The contract positions Customer Content and Usage Data as inputs to Provider's product development cycle, not merely as material held in trust for the Customer. This is a meaningful asymmetry for a $150K/year operational platform: the Customer is paying for a service, but the data flowing through that service feeds Provider's broader product and AI strategy.

The risk architecture channels Customer's exposure into a few key areas. Liability is capped (at amounts defined on the Cover Page) with a tiered structure — General Cap, Increased Cap, and Unlimited Claims — but the definitions of what falls into each tier are Cover Page variables, meaning the actual exposure profile is invisible from the Standard Terms alone. The consequential damages waiver is mutual and broad, covering lost profits and revenues "whether direct or indirect," which notably constrains Customer's primary avenue of recovery in a service failure scenario. Provider's indemnification covers IP-related Covered Claims (again, defined on Cover Page), and the indemnification procedure gives sole control of defense and settlement to the Indemnifying Party.

Provider's warranty commitment is narrow: it warrants only that it "will not materially reduce the general functionality of the Cloud Service during the Subscription Period" (Section 6.3). This is not a warranty that the service will work, perform to specifications, or meet Customer's needs — only that Provider won't actively degrade it. Combined with the disclaimer of all implied warranties including fitness for purpose (Section 7.1), this leaves Customer with limited warranty-based recourse.

The termination architecture provides some balance. Either party can terminate for material breach with 30 days' cure, and force majeure termination triggers a prorated refund. But the post-termination data provisions are permissive rather than protective: Provider must delete Customer Content within 60 days only "upon Customer's request" (Section 5.5(b)), and Recipient may retain Confidential Information per standard backup and retention policies (Section 5.6(b)).

Overall, the contract reflects a Provider that has modeled itself as a platform operator with legitimate interests in the data flowing through its systems, not merely as a service bureau holding Customer's data temporarily. The Customer's interests are protected at the level of confidentiality and data protection law compliance, but the commercial use rights around data — particularly for AI/ML — are broad.

## Clause Observations

### Service Access and Use (Section 1)

**What the contract provides**: Customer gets access to the Cloud Service, with rights to copy and use Software and Documentation as needed for access, all limited to "internal business purposes." Affiliates can enter separate Order Forms, creating separate agreements where Customer bears no responsibility for Affiliate obligations.

**Specific terms**: Access limited to Subscription Period; use restricted to internal business purposes.

**Key language**: "Customer may (a) access and use the Cloud Service; and (b) copy and use the included Software and Documentation only as needed to access and use the Cloud Service, in each case, for its internal business purposes."

**Interactions**: The Affiliate carveout (Section 1.1) means that if Customer's Affiliates use the service under their own Order Forms, those are entirely separate contractual relationships. Customer has no leverage over — and no liability for — those agreements. This cuts both ways: it insulates Customer from Affiliate risk, but it also means Provider's obligations to Affiliates are not Customer's to enforce.

### Feedback and Usage Data (Section 1.4)

**What the contract provides**: Customer may provide Feedback voluntarily; Provider can use it freely and without restriction. Provider may collect and analyze Usage Data and use it freely for product improvement and promotion. Disclosure to third parties requires aggregation and de-identification.

**Specific terms**: Feedback given "AS IS"; Usage Data may be used "without restriction or obligation"; third-party disclosure requires aggregation and non-identification of Customer or Users.

**Key language**: "Provider may collect and analyze Usage Data, and Provider may freely use Usage Data to maintain, improve, enhance, and promote Provider's products and services without restriction or obligation."

**Interactions**: This provision works in concert with Section 1.6 (Machine Learning) to create a broad data utilization framework. The Feedback provision survives termination (Section 5.6), meaning Provider's rights to use Feedback are perpetual.

### Customer Content Rights (Section 1.5)

**What the contract provides**: Provider may "copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings." Customer is responsible for accuracy and content.

**Specific terms**: Provider's use limited to "provide and maintain the Product and related offerings."

**Key language**: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings."

**Interactions**: The phrase "and related offerings" extends Provider's use rights beyond the specific Cloud Service Customer is paying for. This is broader than "provide the Cloud Service" — it could encompass other products in Provider's portfolio. This breadth interacts with Section 1.6 (Machine Learning) to create a layered set of rights over Customer Content. Section 11.1 confirms Customer "retains all rights in Customer Content, subject to Sections 1.5 and 1.6" — meaning the retained rights are qualified by both the operational use grant and the ML training grant.

### Machine Learning (Section 1.6)

**What the contract provides**: Provider may use Usage Data and Customer Content to develop, train, or enhance AI/ML models that are part of Provider's products and services, including third-party components. Customer "authorizes Provider to process its Usage Data and Customer Content for such purposes."

**Specific terms**: Data must be aggregated before ML use; Provider will use "commercially reasonable efforts consistent with industry standard technology" to de-identify before such use. Provider acknowledges AI-generated information "may be incorrect or inaccurate" and that AI/ML features "are not a substitute for human oversight."

**Key language**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes."

**Interactions**: This provision survives termination (Section 5.6), meaning the ML training rights persist after the relationship ends. The aggregation and de-identification requirements are the primary guardrails, but "commercially reasonable efforts consistent with industry standard technology" for de-identification is an effort-based standard, not a results-based one. The carveout preserving Personal Data obligations under Applicable Data Protection Laws provides a floor, but Customer Content that is commercially sensitive without being Personal Data has no equivalent protection. The interaction with Section 11.1 means Customer's retained rights in Customer Content are explicitly subject to this ML use grant.

### Restrictions and Suspension (Section 2)

**What the contract provides**: Standard restriction set including no reverse engineering, no competitive use, no security testing, no derivative works. Provider may suspend access for unpaid balances (over 30 days, undisputed), breach of restrictions, or use that "materially and negatively impacts the Product or others."

**Specific terms**: Suspension for unpaid balance requires 30+ days and the balance must be undisputed. Provider "will try to inform Customer before suspending" when practical. Reinstatement requires resolving the underlying issue.

**Key language**: "Provider may temporarily suspend Customer's access to the Product with or without notice." The commitment to try to inform Customer is aspirational: "Provider will try to inform Customer before suspending Customer's account when practical."

**Interactions**: The suspension power is broad and does not require notice. The "materially and negatively impacts the Product or others" ground (Section 2.2(c)) is subjective and Provider-determined. There is no provision for Customer to dispute a suspension or to receive a credit for downtime caused by suspension. This interacts with Section 4.1, where Fees are non-refundable — meaning Customer could be paying for a suspended service.

### Privacy and Security (Section 3)

**What the contract provides**: Customer must enter a DPA before submitting GDPR-governed Personal Data. DPA terms control over the Agreement in event of conflict. Customer may not submit Prohibited Data unless authorized by the Order Form.

**Specific terms**: DPA is a prerequisite for GDPR-governed Personal Data; DPA controls over Agreement in conflicts; Prohibited Data submission requires Order Form authorization.

**Key language**: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider."

**Interactions**: The DPA requirement is narrowly scoped to GDPR. Personal Data governed by other privacy regimes (CCPA, LGPD, PIPEDA, etc.) has no equivalent DPA requirement in the Standard Terms. The Prohibited Data restriction puts the compliance burden on Customer to ensure it does not submit data that the Product is not authorized to handle. There is no corresponding obligation on Provider to detect or reject Prohibited Data, or to notify Customer if it encounters it.

### Payment and Taxes (Section 4)

**What the contract provides**: Fees in USD unless specified otherwise, non-refundable except for specific termination-related prorated refunds. Invoicing in arrears for usage-based, in advance for other Fees. Customer responsible for all taxes except Provider's income taxes.

**Specific terms**: Fees are non-refundable with limited exceptions; payment disputes require notice before payment is due or within 30 days of automatic payment; parties will work to resolve disputes within 15 days.

**Key language**: "Except for the prorated refund of prepaid Fees allowed with specific termination rights given in the Agreement, Fees are non-refundable."

**Interactions**: The non-refundable Fees principle interacts with the suspension power (Section 2.2) — Customer continues to owe Fees during suspension. The payment dispute mechanism (Section 4.6) is reasonable but note the asymmetry: Customer must pay "all undisputed amounts on time" while disputing, but Provider has no obligation to continue service during a dispute beyond not suspending for "undisputed" balances.

### Term and Termination (Section 5)

**What the contract provides**: Auto-renewal unless notice given before Non-Renewal Notice Date (a Cover Page variable). Either party may terminate for material breach with 30 days' cure period, or immediately for incurable breach, dissolution, or insolvency (bankruptcy must continue 60+ days). Force majeure termination available if the Product is materially non-operational for 30+ consecutive days.

**Specific terms**: 30-day cure period for material breach; 60-day threshold for bankruptcy proceedings; 30 consecutive days of force majeure impact required; post-termination data deletion within 60 days upon Customer request; force majeure termination triggers prorated refund.

**Key language**: "Upon Customer's request, Provider will delete Customer Content within 60 days." Note: deletion is upon request only, not automatic.

**Interactions**: The Non-Renewal Notice Date is a Cover Page variable — if not specified, it defaults to "none" or "not applicable" per Section 13.1, which could mean the agreement auto-renews with no mechanism for non-renewal. This is a significant gap if the Cover Page is not carefully completed. The 60-day deletion window is generous to Provider and only begins when Customer makes a request. Combined with Section 5.6(b) allowing retention per standard backup policies, practical data deletion could extend well beyond 60 days.

### Representations and Warranties (Section 6)

**What the contract provides**: Mutual reps on authority, organization, legal compliance, and Additional Warranties (a Cover Page variable). Customer warrants rights to all submitted Customer Content. Provider warrants only that it "will not materially reduce the general functionality of the Cloud Service during the Subscription Period."

**Specific terms**: Provider warranty remedy requires Customer notice within 45 days of discovering an issue; Provider gets 45 days to attempt restoration; if Provider cannot resolve, Customer may terminate for a prorated refund.

**Key language**: "Provider represents and warrants to Customer that it will not materially reduce the general functionality of the Cloud Service during the Subscription Period."

**Interactions**: Provider's warranty is remarkably narrow — it promises not to actively degrade the service, not that the service will perform at any particular level. There is no uptime warranty, no performance SLA in the Standard Terms, and no warranty of fitness. The remedy is also constrained: Customer must discover the issue and notify within 45 days, then Provider gets another 45 days to fix it, and if it cannot, the remedy is termination with a prorated refund — not damages. Combined with the Section 7 disclaimer and the Section 8.2 consequential damages waiver, Customer's financial recovery for service degradation is limited to prorated Fees.

### Disclaimer and Limitation of Liability (Sections 7–8)

**What the contract provides**: All implied warranties disclaimed. Three-tier liability structure: General Cap, Increased Cap, and Unlimited Claims. Broad consequential damages waiver covering lost profits and revenues "whether direct or indirect." The consequential damages waiver does not apply to Increased Claims or breach of Confidentiality (Section 10).

**Specific terms**: General Cap Amount, Increased Cap Amount, and the categories for Increased Claims and Unlimited Claims are all Cover Page variables. The consequential damages waiver exception for Confidentiality breach and Increased Claims is specified in Section 8.4.

**Key language**: "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."

**Interactions**: The three-tier structure is architecturally sound but its substance depends entirely on Cover Page definitions. If Increased Claims and Unlimited Claims are not populated, all liability falls under the General Cap, including indemnification obligations. The "whether direct or indirect" qualifier on lost profits is notable — it forecloses the argument that lost profits are direct damages recoverable under the cap. The consequential damages waiver exception for Confidentiality breach (Section 8.4) provides an important carveout, particularly given the ML training provisions in Section 1.6, but its practical value depends on proving a Confidentiality breach rather than a breach of the data use limitations.

### Indemnification (Section 9)

**What the contract provides**: Mutual indemnification for respective Covered Claims (defined on Cover Page). Standard procedure requiring prompt notice, reasonable assistance, and sole control over defense/settlement to the Indemnifying Party. Settlement admissions of fault require consent. Provider may modify or replace infringing components, or terminate and refund. Indemnification is the exclusive remedy for Covered Claims.

**Specific terms**: Provider Covered Claims and Customer Covered Claims are Cover Page variables. Exclusions include unauthorized modifications, unauthorized use, combination with non-Provider items, and use of outdated versions.

**Key language**: "Section 9, together with termination rights, describes exclusive remedies for Covered Claims."

**Interactions**: The exclusive remedy provision (Section 9.6) is significant — it forecloses other contract claims for matters that qualify as Covered Claims. The breadth of exclusions (Section 9.5) could limit Provider's indemnification in practice: "combination with non-Provider items" could exclude claims arising from the integration context in which most SaaS products operate. The interaction with the liability cap depends on whether indemnification is classified as an Increased Claim or Unlimited Claim on the Cover Page.

### Confidentiality (Section 10)

**What the contract provides**: Standard mutual confidentiality with standard exclusions (prior knowledge, public availability, independent development, authorized third-party receipt). Permitted disclosure to employees, advisors, and contractors with need-to-know and equivalent confidentiality obligations. Required disclosures permitted with reasonable advance notice.

**Specific terms**: Confidential Information definition is in the Cover Page/definitions. Survival per Section 5.6.

**Interactions**: The confidentiality obligations interact with the data use provisions in two important ways. First, Section 1.4 and 1.6 grant Provider use rights that operate independently of — and potentially in tension with — confidentiality obligations. Provider's right to use Usage Data and Customer Content for ML training is framed as an authorized use under the Agreement, meaning confidentiality would not constrain it. Second, the consequential damages waiver exception for Confidentiality breach (Section 8.4) creates a path for uncapped consequential damages if Provider mishandles Confidential Information outside the authorized use grants — but distinguishing authorized ML use from unauthorized Confidential Information use could be practically difficult.

### Reservation of Rights (Section 11)

**What the contract provides**: Provider retains all rights in the Product. Customer retains all rights in Customer Content, "subject to Sections 1.5 and 1.6."

**Key language**: "Customer retains all rights in Customer Content, subject to Sections 1.5 and 1.6."

**Interactions**: The "subject to" qualifier is the operative phrase. Customer's retained rights are not absolute — they are qualified by both the operational use grant (Section 1.5, limited to providing the Product and "related offerings") and the ML training grant (Section 1.6, broader and surviving termination). This is a meaningful qualification for an operational SaaS platform that will process substantial Customer Content.

### General Terms (Section 12)

**What the contract provides**: Standard boilerplate including entire agreement, modification requires writing, governing law per Cover Page, exclusive jurisdiction in Chosen Courts, assignment restrictions with change-of-control exception, Beta Products provided "AS IS," Provider logo rights over Customer's name, force majeure (excluding payment obligations), export compliance by Customer.

**Specific terms**: Governing Law and Chosen Courts are Cover Page variables. Assignment permitted in merger/acquisition/change of control without consent.

**Key language**: "Provider may use Customer's name and logo in marketing." This is a unilateral right with no apparent opt-out in the Standard Terms.

**Interactions**: The assignment provision (Section 12.6) allows either party to assign in a change of control without consent. For Customer, this means Provider could be acquired and the contract — including the ML training rights over Customer Content — would transfer to the acquirer. The logo rights provision (Section 12.8) is unilateral to Provider with no reciprocal right or opt-out mechanism.

## Unusual or Non-Standard Provisions

**Machine Learning training rights on Customer Content (Section 1.6)**: While increasingly common, the explicit grant allowing Provider to use Customer Content — not just Usage Data — for AI/ML model training, including "third-party components of the Product," is notable. The survival of this provision post-termination means Customer's data can continue to influence models after the relationship ends, with only aggregation and "commercially reasonable" de-identification as constraints. The inclusion of third-party model training is a further extension beyond Provider's own products.

**"Related offerings" in Customer Content use (Section 1.5)**: The phrase "provide and maintain the Product and related offerings" extends Provider's use rights beyond the contracted service. "Related offerings" is not defined and could encompass other products in Provider's portfolio, future products, or third-party integrations.

**Logo rights without opt-out (Section 12.8)**: Provider gets a unilateral right to use Customer's name and logo in marketing. There is no consent mechanism, no approval right over materials, and no opt-out. For a $150K/year deal, this is a standard vendor request, but its inclusion in the non-negotiable Standard Terms without any Customer control is atypical of balanced agreements.

**Provider warranty as a non-degradation commitment only (Section 6.3)**: The warranty that Provider "will not materially reduce the general functionality" is unusual in that it only commits Provider not to make things worse. It makes no affirmative commitment about uptime, performance, or fitness. This is narrower than most SaaS warranties, which typically warrant conformance with documentation or specifications.

**Suspension without notice or credit (Section 2.2)**: Provider may suspend "with or without notice" and there is no provision for fee credits during suspension. The only mitigation is that Provider "will try to inform Customer before suspending" — an effort commitment, not an obligation.

## Notable Absences

**Service Level Agreement**: There is no uptime commitment, performance SLA, or service credit mechanism in the Standard Terms. For a $150K/year operational platform, the absence of any measurable service commitment is significant. The Order Form or a separate SLA document would need to address this.

**Data processing beyond GDPR**: The DPA requirement is scoped only to "Personal Data governed by GDPR" (Section 3.1). There is no equivalent requirement for personal data governed by CCPA, LGPD, PIPEDA, or other data protection regimes. For a platform handling internal operations data, this gap may require a separately negotiated DPA or addendum.

**Security obligations**: There is no description of Provider's security practices, no security standards commitment (SOC 2, ISO 27001, etc.), no breach notification obligation beyond what Applicable Data Protection Laws may require, and no audit or assessment rights for Customer.

**Insurance requirements**: No provision requiring Provider to maintain errors and omissions, cyber liability, or other insurance coverage.

**Data location**: No restriction on where Customer Content or Personal Data may be stored or processed. No data residency commitments.

**Subprocessor controls**: No disclosure obligation for subprocessors, no notification of subprocessor changes, and no Customer right to object to new subprocessors. These would typically appear in a DPA, but the DPA is not part of the Standard Terms and is only required for GDPR-governed data.

**Transition assistance**: No obligation for Provider to assist with data migration or transition at end of term. The only post-termination data obligation is deletion within 60 days upon request.

**Scheduled downtime / maintenance windows**: No commitment to provide notice of scheduled maintenance or to schedule maintenance during off-peak hours.

## Material Clause Interactions

**Data rights cascade (Sections 1.4, 1.5, 1.6, 5.6, 11.1)**: These provisions create a layered data rights architecture that is more extensive than any single clause suggests. Section 1.5 grants operational use rights over Customer Content for the Product "and related offerings." Section 1.6 extends to ML training, surviving termination. Section 1.4 makes Usage Data freely usable without restriction. Section 11.1 subordinates Customer's retained rights to both 1.5 and 1.6. Section 5.6 makes the Feedback and ML provisions survive termination. Read together, Provider acquires broad, perpetual, surviving rights over the data flowing through its platform, constrained only by aggregation requirements, commercially reasonable de-identification, and data protection law compliance. Each provision read alone appears bounded; read together, they create a comprehensive data utilization framework that favours Provider.

**Liability cap + consequential damages waiver + narrow warranty (Sections 6.3, 7.1, 8.1, 8.2, 8.4)**: Provider's warranty is limited to non-degradation of general functionality. All implied warranties are disclaimed. Lost profits and revenues are waived "whether direct or indirect." The liability cap is set at Cover Page amounts. Together, these provisions mean that if the Cloud Service fails, performs poorly, or does not meet Customer's needs, Customer's maximum recovery is a prorated refund of prepaid Fees (via the warranty remedy in Section 6.4) and direct damages up to the General Cap — but with lost profits excluded from direct damages and consequential damages waived, the recoverable direct damages for a service failure may be limited to the Fees themselves. For a $150K/year platform that supports internal operations, the actual business impact of a service failure could substantially exceed the available recovery.

**Suspension + non-refundable Fees + no SLA (Sections 2.2, 4.1, no SLA)**: Provider can suspend access without notice and without a credit mechanism. Fees are non-refundable. There is no SLA providing service credits for downtime. This combination means Customer has no financial remedy for Provider-initiated service interruptions short of termination for material breach, which requires a 30-day cure period (Section 5.3(a)). A suspension lasting 29 days followed by reinstatement could leave Customer without access and without remedy.

**Post-termination data retention + ML survival (Sections 1.6, 5.5, 5.6)**: Customer Content deletion requires Customer's affirmative request and Provider gets 60 days. But Section 5.6(b) permits retention per standard backup and retention policies, and Section 1.6 (ML training rights) survives termination entirely. This means that even after termination and a deletion request, Provider may (a) retain data in backups indefinitely per its retention policies, and (b) continue to benefit from ML models trained on Customer Content during the relationship. The aggregation and de-identification requirements apply, but once data has been used to train a model, it has influenced the model's parameters — the practical effect of "deletion" on trained models is unclear and the contract does not address it.

**Assignment + data rights in change of control (Sections 12.6, 1.5, 1.6)**: Either party may assign in a change of control without consent. If Provider is acquired, the acquirer inherits Provider's rights under Sections 1.5 and 1.6 — including the right to use Customer Content for ML training of the acquirer's products and services (since Section 1.6 covers "Provider's products and services" and the acquirer steps into Provider's shoes). Customer has no consent right and no termination right triggered by change of control. This could result in Customer's operational data being available for ML training by a competitor or an entity Customer would not have contracted with.

**Indemnification exclusions + integration reality (Section 9.5)**: Provider's indemnification obligations do not apply to claims arising from "combination with non-Provider items." In practice, SaaS products are almost always integrated with other systems — identity providers, data warehouses, APIs, complementary tools. This exclusion could effectively hollow out Provider's IP indemnification obligation for any claim arising in the context of Customer's actual use, since nearly any deployment involves combination with non-Provider items.
