# Contract Reader Output

**Important**: This analysis assists with legal workflows but does not constitute legal advice. All analysis should be reviewed by qualified legal professionals.

## Contract Overview

**Type**: Cloud Service Agreement (SaaS) — Standard Terms (Common Paper v2.1)
**Parties**: Provider (unnamed, the SaaS vendor) and Customer (unnamed, the buyer)
**User's side**: Customer (buying a SaaS product)
**Commercial structure**: Provider grants Customer access to a cloud service during a subscription period in exchange for Fees. The agreement uses a two-layer architecture: Standard Terms provide the legal framework, while one or more Order Forms set the commercial specifics (fees, subscription period, support terms, use limitations). A Cover Page sits between them, defining variables that the Standard Terms reference but do not populate — liability cap amounts, covered claims for indemnification, governing law, non-renewal notice dates, and others. The practical effect is that many of the contract's most consequential terms are not visible in the Standard Terms alone.
**Effective date / Term**: The Framework Terms start on the Effective Date and continue for the longer of one year or until all Order Forms have ended. Each Order Form starts on its Order Date, continues through the Subscription Period, and auto-renews for additional Subscription Periods unless a party gives notice before the Non-Renewal Notice Date. The Effective Date, Subscription Period, and Non-Renewal Notice Date are all Cover Page variables not specified in these Standard Terms.

## Clause Summaries

### Access, Use, and Scope of License (Section 1.1)

**What the contract provides**: Customer receives a right to access and use the Cloud Service, and to copy and use included Software and Documentation, limited to internal business purposes. Customer Affiliates that sign separate Order Forms create entirely separate agreements — Customer is explicitly not responsible for those affiliate agreements.

**Specific terms**: Use is limited to the Subscription Period and to "internal business purposes." The Affiliate provision makes each Affiliate agreement "individual and separate from Customer."

**Key language**: "Customer may (a) access and use the Cloud Service; and (b) copy and use the included Software and Documentation only as needed to access and use the Cloud Service, in each case, for its internal business purposes." / "Provider's responsibility to the Affiliate is individual and separate from Customer and Customer is not responsible for its Affiliates' agreement."

**Interactions**: The scope of this license is bounded by the Restrictions in Section 2.1, Use Limitations defined in the Order Form, and Documentation. The Affiliate separation provision means any group-wide deployment would require separate Order Forms per entity, with no umbrella coverage or volume aggregation built into the Standard Terms.

### Support (Section 1.2)

**What the contract provides**: Provider will provide Technical Support during the Subscription Period "as described in the Order Form."

**Specific terms**: No support levels, response times, escalation paths, or SLAs appear in the Standard Terms. The entire support obligation is deferred to the Order Form.

**Key language**: "Provider will provide Technical Support as described in the Order Form."

**Interactions**: Because support is entirely defined by the Order Form, the Standard Terms provide no fallback if the Order Form is silent or vague on support. There is no minimum baseline.

### User Accounts and Responsibility (Section 1.3)

**What the contract provides**: Customer bears responsibility for all actions on Users' accounts and for all Users' compliance with the Agreement. Customer and Users must protect password and credential confidentiality. Customer must promptly notify Provider if it suspects or knows of fraudulent activity or compromise.

**Specific terms**: Notification obligation is triggered when Customer "suspects or knows" of fraudulent activity or compromise — a broad trigger that includes suspicion, not just knowledge.

**Key language**: "Customer is responsible for all actions on Users' accounts and for all Users' compliance with this Agreement."

**Interactions**: This unqualified responsibility clause feeds into Section 2.1 — if any User violates any restriction, Customer bears that liability. It also connects to Section 2.2 suspension rights, where Provider can suspend based on User actions attributed to Customer.

### Feedback and Usage Data (Section 1.4)

**What the contract provides**: Two distinct grants operating under different rules. First, any Feedback Customer provides can be used by Provider "freely without any restriction or obligation." Second, Provider may collect and analyze Usage Data and use it "freely" to "maintain, improve, enhance, and promote Provider's products and services." Disclosure of Usage Data to third parties is permitted only in aggregated, non-identifying form.

**Specific terms**: Feedback is provided "AS IS." Provider's freedom of use is described as "without restriction or obligation" for both Feedback and Usage Data. The disclosure limitation requiring aggregation and non-identification applies only to sharing with "others" — Provider's own internal use of granular, non-aggregated Usage Data is unrestricted.

**Key language**: "Provider may use all Feedback freely without any restriction or obligation." / "Provider may collect and analyze Usage Data, and Provider may freely use Usage Data to maintain, improve, enhance, and promote Provider's products and services without restriction or obligation. However, Provider may only disclose Usage Data to others if the Usage Data is aggregated and does not identify Customer or Users."

**Interactions**: This section survives termination (Section 5.6), meaning Provider retains perpetual rights to Feedback and Usage Data even after the relationship ends. The Usage Data rights here are further extended by Section 1.6 (Machine Learning), which adds ML training to the permitted uses. There is no mechanism for Customer to request deletion of Usage Data or to revoke the Feedback license.

### Customer Content (Section 1.5)

**What the contract provides**: Provider's rights to Customer Content are limited to what is "needed to provide and maintain the Product and related offerings." Customer bears responsibility for "the accuracy and content of Customer Content."

**Specific terms**: Provider may "copy, display, modify, and use" Customer Content — a broad set of verbs, but constrained by the "only as needed" qualifier. The phrase "and related offerings" extends Provider's use rights beyond the specific subscribed Product.

**Key language**: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings."

**Interactions**: This Customer Content license is narrower than the Usage Data and Feedback rights in Section 1.4, but it is materially expanded by Section 1.6 (Machine Learning), which permits use of Customer Content for AI/ML training under specified conditions. Section 11.1 confirms Customer retains ownership of Customer Content "subject to Sections 1.5 and 1.6" — the "subject to" qualifier subordinates ownership to both license grants.

### Machine Learning (Section 1.6)

**What the contract provides**: Provider may use both Usage Data and Customer Content to "develop, train, or enhance artificial intelligence or machine learning models" that are part of Provider's products and services, including third-party components. Customer explicitly "authorizes Provider to process its Usage Data and Customer Content for such purposes."

**Specific terms**: Two safeguards apply: (a) data "must be aggregated before it can be used for these purposes" and (b) Provider will use "commercially reasonable efforts consistent with industry standard technology to de-identify" the data before such use. The section explicitly states it does not "reduce or limit Provider's obligations regarding Personal Data" under Applicable Data Protection Laws. A disclaimer notes that AI/ML features "may be incorrect or inaccurate" and "are not a substitute for human oversight."

**Key language**: "Customer authorizes Provider to process its Usage Data and Customer Content for such purposes." / "Provider will use commercially reasonable efforts consistent with industry standard technology to de-identify Usage Data and Customer Content before such use." / "Nothing in this section will reduce or limit Provider's obligations regarding Personal Data that may be contained in Usage Data or Customer Content under Applicable Data Protection Laws."

**Interactions**: This section significantly extends the Customer Content license in Section 1.5 — from "only as needed to provide and maintain the Product" to training AI/ML models across Provider's entire product portfolio, including third-party components. It survives termination (Section 5.6), meaning Customer Content contributed during the subscription could continue to inform Provider's models indefinitely. The aggregation requirement provides some structural protection, but "commercially reasonable efforts" for de-identification is an effort-based standard, not an outcome guarantee. The carveout preserving data protection obligations interacts with Section 3.1 (Personal Data) but the mechanism for enforcement is unclear — once data is aggregated and used for training, extraction or deletion from trained models may be technically infeasible.

### Restrictions on Customer (Section 2.1)

**What the contract provides**: Ten prohibited activities, prefaced with "Customer will not (and will not allow anyone else to)," extending Customer's liability to actions by any third party using Customer's access. The restrictions cover reverse engineering, redistribution, removing proprietary notices, derivative works, security testing, unauthorized access, competitive development, high risk activities, unauthorized network access, and uploading content without proper rights.

**Specific terms**: The reverse engineering restriction includes a carveout for Applicable Laws that prohibit such restrictions. The security testing prohibition is a blanket ban: "conduct security or vulnerability tests on" the Product. The competitive development restriction prohibits using the Product "to develop a competing service or product." All use must comply with Documentation and Use Limitations (a Cover Page variable).

**Key language**: "conduct security or vulnerability tests on, interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product" / "use the Product to develop a competing service or product"

**Interactions**: Breach of Section 2.1 is one of three triggers for Provider's suspension right under Section 2.2. The security testing prohibition (2.1(a)(v)) prevents Customer from conducting its own security assessments — this interacts with the absence of any security commitments from Provider in the Standard Terms. The competitive development restriction (2.1(a)(vii)) survives termination per Section 5.6, though its practical impact post-termination is limited since Customer would no longer have Product access.

### Suspension (Section 2.2)

**What the contract provides**: Provider may temporarily suspend Customer's access under three circumstances: outstanding undisputed balance over 30 days, breach of Section 2.1, or use that "materially and negatively impacts the Product or others." Provider will "try to inform Customer before suspending Customer's account when practical," but notice is not required. Reinstatement is conditioned on Customer resolving "the underlying issue."

**Specific terms**: The 30-day payment threshold applies only to "undisputed" balances. There is no time limit on how long suspension can last. There is no obligation for Provider to specify the reason for suspension. There is no timeline for reinstatement once the issue is resolved. There is no remedy for Customer if suspension is wrongful.

**Key language**: "Provider may temporarily suspend Customer's access to the Product with or without notice." / "However, Provider will try to inform Customer before suspending Customer's account when practical." / "Provider will reinstate Customer's access to the Product only if Customer resolves the underlying issue."

**Interactions**: Suspension is distinct from termination — Customer's payment obligations presumably continue during suspension, as no provision excuses them. The phrase "materially and negatively impacts the Product or others" gives Provider broad discretion to determine what constitutes a negative impact. The only recourse for wrongful suspension would be a material breach claim under Section 5.3, which requires 30 days' notice and cure.

### Personal Data (Section 3.1)

**What the contract provides**: Before submitting GDPR-governed Personal Data, Customer must enter into a separate data processing agreement (DPA) with Provider. If a DPA exists, its terms control on data protection matters, including in any conflict with the Agreement.

**Specific terms**: The DPA requirement is triggered specifically by "Personal Data governed by GDPR." The DPA terms prevail over the Agreement in case of conflict. The DPA itself is not included in or appended to the Standard Terms.

**Key language**: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider." / "the terms of the DPA will control in the event of any conflict with this Agreement."

**Interactions**: The GDPR-specific trigger means Personal Data governed by other data protection laws (CCPA, LGPD, POPIA, UK GDPR, etc.) does not trigger a DPA requirement under this provision. Section 1.6 preserves data protection obligations for Personal Data in the ML context, but the mechanism for non-GDPR Personal Data is unspecified. The conditional framing — "Before submitting" and "If the parties have a DPA" — means there is no default data protection framework in the Standard Terms themselves.

### Prohibited Data (Section 3.2)

**What the contract provides**: Customer may not submit Prohibited Data to the Product unless specifically authorized by the Order Form or Key Terms. The obligation extends to anyone acting through Customer.

**Specific terms**: "Prohibited Data" is defined on the Cover Page. Without the Cover Page, the scope of this restriction is unknown.

**Key language**: "Customer will not (and will not allow anyone else to) submit Prohibited Data to the Product unless authorized by the Order Form or Key Terms."

**Interactions**: Submission of unauthorized Prohibited Data would likely constitute a breach interacting with Customer's warranty in Section 6.2 that it has "all rights necessary to submit or make available Customer Content."

### Payment and Taxes (Section 4)

**What the contract provides**: A comprehensive payment framework. Fees default to U.S. Dollars, are exclusive of taxes, and are non-refundable except for specific prorated refund rights granted elsewhere. Two payment mechanisms are supported: invoicing (usage-based in arrears, other fees in advance) and automatic payment. Customer bears responsibility for all taxes that Provider itemizes on invoices, except Provider's income taxes.

**Specific terms**: Customer is responsible for "all duties, taxes, and levies that apply to Fees, including sales, use, VAT, GST, or withholding" that Provider itemizes and includes in an invoice. A payment dispute mechanism requires Customer to notify Provider before payment is due (or within 30 days of an automatic payment), pay all undisputed amounts on time, and work toward resolution within 15 days.

**Key language**: "Except for the prorated refund of prepaid Fees allowed with specific termination rights given in the Agreement, Fees are non-refundable." / "Customer must notify Provider about the dispute before payment is due, or within 30 days of an automatic payment, and must pay all undisputed amounts on time."

**Interactions**: Payment obligations survive termination (Section 5.6 for accrued Fees). The dispute mechanism interacts with the 30-day suspension trigger in Section 2.2 — if Customer disputes and provides proper notice, the balance should be considered "disputed" and not trigger suspension, though the timing could be close. Customer's payment obligations are explicitly not excused by Force Majeure (Sections 5.4 and 12.12). Prorated refunds are available only for warranty breach termination (Section 6.4) and force majeure termination (Section 5.4) — there is no explicit refund provision for termination due to Provider's material breach under Section 5.3.

### Term, Renewal, and Termination (Section 5)

**What the contract provides**: A layered term structure. The Framework Terms persist for the longer of one year or until all Order Forms end. Each Order Form auto-renews for additional Subscription Periods unless a party gives notice before the Non-Renewal Notice Date (a Cover Page variable). Termination for cause is available for: (a) material breach with 30 days' written notice and opportunity to cure; (b) incurable material breach, dissolution, cessation of business, or insolvency proceedings continuing more than 60 days — each permitting immediate termination upon notice. Either party may terminate an affected Order Form if a Force Majeure Event prevents the Product from materially operating for 30 or more consecutive days.

**Specific terms**: 30-day cure period for curable material breach. 60-day grace period for bankruptcy/insolvency proceedings. 30 consecutive days of material inoperability for force majeure termination. Non-Renewal Notice Date is a Cover Page variable with no default.

**Key language**: "automatically renew for additional Subscription Periods unless one party gives notice of non-renewal to the other party before the Non-Renewal Notice Date" / "if the other party fails to cure a material breach of the Framework Terms or an Order Form following 30 days notice"

**Interactions**: The Non-Renewal Notice Date being a Cover Page variable means the auto-renewal lock-in period is entirely controlled by what's negotiated. If set far in advance, Customer could be locked into renewal before it has information needed to make a renewal decision. Termination of the Framework Terms automatically terminates all Order Forms (Section 5.5). Force Majeure termination includes a prorated refund of prepaid Fees (Section 5.4), but Customer must still pay accrued Fees.

### Effect of Termination (Section 5.5)

**What the contract provides**: Upon expiration or termination, Customer loses all rights to use the Product. Provider will delete Customer Content within 60 days but only upon Customer's request. Each party returns or destroys the other's Confidential Information. Provider submits a final bill for accrued Fees.

**Specific terms**: 60-day deletion window. Deletion is upon request only — not automatic. No data export or portability obligation. No transition assistance.

**Key language**: "Upon Customer's request, Provider will delete Customer Content within 60 days."

**Interactions**: The survival clause (Section 5.6) is extensive. Sections 1.4 (Feedback and Usage Data) and 1.6 (Machine Learning) both survive, meaning Provider's rights to use Usage Data and aggregated Customer Content for ML training persist even after Customer Content is nominally deleted. Section 5.6(b) permits retention of Confidential Information under standard backup or record retention policies, with confidentiality obligations continuing to apply.

### Survival (Section 5.6)

**What the contract provides**: A broad list of sections that survive termination: Feedback and Usage Data (1.4), Machine Learning (1.6), Restrictions on Customer (2.1), Payment (for accrued fees), Effect of Termination (5.5), Survival (5.6), Representations & Warranties (6), Disclaimer (7), Limitation of Liability (8), Indemnification (9), Confidentiality (10), Reservation of Rights (11), General Terms (12), Definitions (13), and related Cover Page portions.

**Key language**: The full enumeration of surviving sections in 5.6(a). Also: "Each Recipient may retain Discloser's Confidential Information in accordance with its standard backup or record retention policies maintained in the ordinary course of business or as required by Applicable Laws."

**Interactions**: The survival of Sections 1.4 and 1.6 is particularly consequential — it means Provider's rights over Feedback, Usage Data, and the ML training authorization continue indefinitely. Combined with Section 5.6(b)'s retention carveout, significant amounts of Customer data may persist with Provider post-termination under legitimate contractual authority.

### Representations and Warranties (Section 6)

**What the contract provides**: Mutual representations covering legal authority, good standing, compliance with Applicable Laws, and compliance with Additional Warranties (a Cover Page variable). Customer specifically warrants that it and its Users have all rights necessary to submit Customer Content and to allow its use as described in the Agreement. Provider's sole product warranty is that it "will not materially reduce the general functionality of the Cloud Service during the Subscription Period."

**Specific terms**: Provider's warranty is framed as a negative commitment (will not reduce) rather than an affirmative quality commitment. The warranty remedy (Section 6.4) requires Customer to notify within 45 days of discovering the issue. Provider then has 45 days from receiving "sufficient details" to attempt restoration. If Provider cannot resolve, Customer may terminate and receive a prorated refund.

**Key language**: "Provider represents and warrants to Customer that it will not materially reduce the general functionality of the Cloud Service during the Subscription Period." / "If Provider breaches the warranty in Section 6.3, Customer must give Provider notice within 45 days of discovering the issue."

**Interactions**: The warranty in 6.3 is narrow — it covers only "general functionality" and only "material" reductions. It does not cover performance degradation, intermittent outages, specific feature changes, uptime, data integrity, or security incidents. The 45-day discovery-to-notice deadline in 6.4 could forfeit the remedy if Customer does not detect or report functionality reductions promptly. The total potential timeline before Customer can terminate is up to 90 days (45 to notify + 45 to cure). The warranty remedy in 6.4 is the only path to a prorated refund other than force majeure termination, given the general non-refundability of Fees in Section 4.1.

### Disclaimer of Warranties (Section 7)

**What the contract provides**: Provider makes no guarantees regarding safety, security, error-free operation, or uninterrupted service. Both parties disclaim all warranties beyond those in Section 6, including merchantability, fitness for a particular purpose, title, and non-infringement.

**Key language**: "Provider makes no guarantees that the Product will always be safe, secure, or error-free, or that it will function without disruptions, delays, or imperfections."

**Interactions**: This broad disclaimer eliminates implied warranties that might otherwise supplement the narrow express warranty in Section 6.3. Combined with that narrow warranty, Customer's contractual protection against service quality problems is limited to demonstrating a "material reduction in general functionality."

### Limitation of Liability (Section 8)

**What the contract provides**: A tiered liability structure with three levels: (1) a General Cap Amount for general claims, (2) an Increased Cap Amount for Increased Claims, and (3) no cap for Unlimited Claims. Both parties waive consequential, special, indirect, exemplary, punitive, and incidental damages, including lost profits and revenues "whether direct or indirect." The waiver has two exceptions: it does not apply to Increased Claims, and it does not apply to breach of Section 10 (Confidentiality).

**Specific terms**: The General Cap Amount, Increased Cap Amount, Increased Claims, and Unlimited Claims are all Cover Page variables — the Standard Terms establish the tiered structure but not the dollar amounts or which claims fall into which tier. The damages waiver explicitly captures lost profits "whether direct or indirect," which means even direct lost-profit claims are waived.

**Key language**: "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility." / "Section 8.2 does not apply to Increased Claims or breach of Section 10 (Confidentiality)."

**Interactions**: The practical risk allocation depends entirely on the Cover Page values. If the General Cap is low and few claims are designated as Increased or Unlimited, Customer's recovery for any breach is severely constrained. The waiver of direct lost profits could eliminate Customer's primary measure of damages for service failures. The confidentiality breach exception (Section 8.4) provides stronger protection for data mishandling — this is the one area where consequential damages remain available without needing Increased Claims designation.

### Indemnification (Section 9)

**What the contract provides**: A mutual indemnification structure where Provider indemnifies Customer from "Provider Covered Claims" and Customer indemnifies Provider from "Customer Covered Claims." Both Covered Claims definitions are Cover Page variables. Procedural requirements include prompt notice, reasonable assistance, and sole control of defense by the Indemnifying Party. The Indemnifying Party may not agree to settlements containing "admissions of fault" without the Protected Party's consent.

**Specific terms**: Provider's exclusions apply to claims arising from: unauthorized modifications, unauthorized use, combination with non-Provider items, or continued use of old versions when a newer version would avoid the claim. Customer's exclusion: unauthorized use of Customer Content. Indemnification plus termination rights constitutes the "exclusive remedy" for Covered Claims (Section 9.6). In response to claims, Provider may modify the Product, obtain continued use rights, or terminate and refund (Section 9.4).

**Key language**: "Provider will indemnify, defend, and hold harmless Customer from Provider Covered Claims and all resulting damages, costs, and expenses including reasonable attorneys' fees." / "The Indemnifying Party may not agree to settlements containing admissions of fault without consent."

**Interactions**: Because both Covered Claims categories are Cover Page variables, the scope of indemnification protection depends entirely on what is negotiated there. The "exclusive remedy" designation in Section 9.6 channels all Covered Claims into the indemnification framework, which could limit Customer's options. Section 9.4 gives Provider a terminate-and-refund option that could leave Customer without a working product in the event of IP claims.

### Confidentiality (Section 10)

**What the contract provides**: Mutual confidentiality obligations. Recipient may not use or disclose Discloser's Confidential Information except as authorized or needed under the Agreement. Standard exclusions apply: previously known, publicly available, independently developed, or received from authorized third parties. Compelled disclosure is permitted with reasonable advance notice. Permitted disclosure to employees, advisors, and contractors with need-to-know, bound by equivalent confidentiality obligations.

**Specific terms**: "Confidential Information" is defined on the Cover Page. Retained copies under standard backup or record retention policies remain subject to confidentiality obligations (Section 5.6(b)).

**Key language**: "Recipient will not use or disclose Discloser's Confidential Information except as authorized or needed under the Agreement."

**Interactions**: Breach of confidentiality is carved out from the consequential damages waiver (Section 8.4), making it one of the higher-exposure areas in the contract. Section 12.4 provides for injunctive relief without bond for confidentiality or IP breaches. The survival provision ensures confidentiality obligations outlast the agreement.

### Reservation of Rights (Section 11)

**What the contract provides**: Provider retains all rights in the Product. Customer retains all rights in Customer Content, but expressly "subject to Sections 1.5 and 1.6."

**Key language**: "Customer retains all rights in Customer Content, subject to Sections 1.5 and 1.6."

**Interactions**: The "subject to" qualifier is significant. It means Customer's formal ownership is encumbered by two broad licenses: Section 1.5 (copy, display, modify, use for providing the Product and "related offerings") and Section 1.6 (ML training across Provider's product line, including third-party components). Both survive termination. Customer owns the content but has granted extensive usage rights that persist independently of the commercial relationship.

### General Terms (Section 12) — Selected Provisions

**Assignment (12.6)**: No assignment without consent, except in merger, acquisition, or change of control. This applies to both parties, meaning Provider could be acquired and the agreement — including all data rights — could transfer to a new entity without Customer's consent.

**Logo Rights (12.8)**: "Provider may use Customer's name and logo in marketing." No consent requirement, no approval right over usage context, no usage guidelines, and no mechanism to withdraw or opt out.

**Modifications (12.2)**: Changes require "writing signed by each party." No unilateral modification right.

**Entire Agreement (12.1)**: The Agreement supersedes all prior statements. "Provider rejects terms in Customer's purchase orders."

**Force Majeure (12.12)**: Neither party liable for delays from Force Majeure Events, "except Customer's payment obligations." This is a one-sided carveout — Customer must keep paying even during force majeure, while Provider's service obligations are excused.

**Governing Law (12.3)**: Cover Page variable. Chosen Courts have exclusive jurisdiction.

**Beta Products (12.7)**: Provided "AS IS" with no warranty, indemnity, or support.

## Unusual or Non-Standard Provisions

**Machine Learning clause (Section 1.6)**: An explicit grant authorizing Provider to use Customer Content for AI/ML training across Provider's entire product line, including third-party components of the Product. While ML clauses are becoming more common, several features of this one stand out: the scope encompasses third-party model components, the safeguards are effort-based rather than outcome-based ("commercially reasonable efforts" for de-identification), the authorization is active ("Customer authorizes Provider to process"), and the rights survive termination. Once Customer Content has been used for training, the practical reversibility is limited regardless of contractual deletion rights.

**Security testing prohibition without exception (Section 2.1(a)(v))**: A blanket prohibition against conducting "security or vulnerability tests" on the Product, with no carveout for Customer's own security due diligence, authorized penetration testing with advance notice, or review of third-party audit reports. Many SaaS agreements either permit testing with coordination or provide third-party assessment results as an alternative.

**GDPR-only DPA trigger (Section 3.1)**: The DPA requirement is triggered only by "Personal Data governed by GDPR," which is narrower than the approach taken in many modern SaaS agreements that address multiple privacy regimes or require a DPA for any Personal Data processing. Personal Data governed by CCPA, LGPD, POPIA, UK GDPR, or other regimes has no specified DPA mechanism in the Standard Terms.

**Customer Content deletion only upon request (Section 5.5(b))**: Post-termination deletion occurs only "upon Customer's request" and Provider has 60 days after the request. If Customer fails to make the request, the contract imposes no affirmative obligation for Provider to delete. Combined with the retention carveout in Section 5.6(b) and the surviving ML training rights, Customer Content could persist with Provider indefinitely.

**Suspension without notice or time limit (Section 2.2)**: Provider may suspend "with or without notice," need only "try to inform" Customer "when practical," and faces no maximum suspension duration, no obligation to state the reason, and no timeline for reinstatement once the issue is resolved. There is no express remedy for wrongful suspension.

**Logo rights without qualification (Section 12.8)**: A marketing use right over Customer's name and logo with no approval mechanism, no context limitations, no usage guidelines, and no opt-out.

**Force Majeure payment carveout (Section 12.12)**: Force Majeure excuses performance delays for both parties, "except Customer's payment obligations." This means Customer must continue paying even when Provider's service delivery is prevented by force majeure — a one-sided treatment that is sometimes but not always present in SaaS agreements.

**Heavy reliance on Cover Page variables for material terms**: An unusually large number of consequential terms are Cover Page variables: General Cap Amount, Increased Cap Amount, Increased Claims, Unlimited Claims, Provider Covered Claims, Customer Covered Claims, Non-Renewal Notice Date, Prohibited Data, Confidential Information, Additional Warranties, Use Limitations, and Governing Law. The Standard Terms establish the structure but the actual risk allocation for liability, indemnification, renewal lock-in, and other critical areas is opaque without the Cover Page.

## Notable Absences

**Service Level Agreement (SLA)**: No uptime commitment, availability guarantee, performance standard, or scheduled maintenance notification. The sole warranty (Section 6.3) commits only to not materially reducing "general functionality" — a substantially lower bar than a service level commitment.

**Security commitments**: No security standards, no certifications (SOC 2, ISO 27001), no encryption requirements, no audit rights, and no obligation for Provider to maintain any particular security posture. The security testing prohibition in Section 2.1(a)(v) compounds this — Customer cannot verify security independently and has no contractual security baseline to enforce.

**Data breach notification**: No obligation for Provider to notify Customer of security breaches, data incidents, unauthorized access to Customer Content, or compromise of Customer credentials. This is material for a SaaS platform handling internal business operations.

**Data portability or export**: Beyond the 60-day deletion right (upon request), there is no provision for data export in standard or usable formats, no API for data retrieval, and no transition assistance upon termination.

**Transition assistance**: No obligation for Provider to assist Customer with migration to an alternative service, provide knowledge transfer, or maintain access during a transition period.

**Subprocessor or subcontractor controls**: No restrictions on Provider's use of subprocessors or subcontractors. No notification requirements for changes in subprocessors. No obligation to flow down equivalent data protection or confidentiality obligations. No right for Customer to object.

**Disaster recovery and business continuity**: No commitments regarding data backup frequency, backup testing, disaster recovery capabilities, recovery time objectives, or recovery point objectives.

**Insurance requirements**: No requirement for Provider to maintain professional liability, cyber liability, errors and omissions, or any other insurance coverage.

**Change management or notification of changes**: No obligation for Provider to notify Customer of changes to the service, deprecation of features, API changes, integration changes, or data format changes. The warranty against material reduction of general functionality (Section 6.3) provides some protection, but only after the change has already occurred and only for changes that rise to "material."

**Refund on material breach termination**: Prorated refunds are provided for warranty breach termination (Section 6.4) and force majeure termination (Section 5.4), but there is no explicit refund provision when Customer terminates for Provider's uncured material breach under Section 5.3.

**Non-GDPR data protection framework**: No mechanism for addressing Personal Data under CCPA, LGPD, UK GDPR, POPIA, or other data protection regimes. The DPA trigger is limited to GDPR.

## Material Clause Interactions

**Customer Content ownership encumbered by perpetual licenses**: Section 11.1 states Customer "retains all rights in Customer Content," but qualifies this with "subject to Sections 1.5 and 1.6." Section 1.5 licenses Provider to copy, display, modify, and use Customer Content for providing and maintaining the Product "and related offerings." Section 1.6 authorizes Provider to use Customer Content for ML training across Provider's product line, including third-party components, with aggregation and commercially reasonable de-identification. Both Sections 1.4 and 1.6 survive termination (Section 5.6). The combined effect is that Customer retains formal ownership but Provider holds broad, perpetual, surviving licenses to derive value from the content — licenses that persist after the commercial relationship ends and potentially after Customer Content is nominally deleted.

**Narrow warranty + broad disclaimer + Cover Page liability caps = uncertain protection**: Section 6.3 warrants only against "material reduction of general functionality." Section 7.1 disclaims all other warranties including safety, security, error-free operation, and uninterrupted service. Section 8 caps liability to Cover Page amounts and waives consequential damages, including direct lost profits. Together, these create a structure where: service degradation short of material functionality reduction produces no warranty breach; even a clear breach may yield only limited recovery depending on cap amounts; and Customer's primary measure of damages (lost profits from service failures) is waived regardless.

**Suspension without notice + continued payment obligation + no wrongful suspension remedy**: Section 2.2 allows suspension "with or without notice" for broadly defined triggers. No provision excuses payment during suspension. There is no maximum suspension duration, no timeline for reinstatement, and no remedy for wrongful suspension. Customer's only apparent recourse for wrongful suspension would be to claim material breach under Section 5.3, which requires 30 days' written notice and a cure opportunity — during which time Customer remains without service access but still owes Fees.

**Non-refundable Fees + auto-renewal + Cover Page notice period**: Section 4.1 provides Fees are non-refundable except for specific prorated refund rights. Section 5.1 auto-renews unless notice is given before the Non-Renewal Notice Date. The Non-Renewal Notice Date is a Cover Page variable. If the notice period is lengthy and Customer misses the deadline, Customer is locked into a full renewal period with non-refundable Fees and no early exit short of a material breach claim.

**Security testing prohibition + absence of security commitments + no breach notification**: Section 2.1(a)(v) prohibits Customer from conducting security or vulnerability tests. The Standard Terms contain no security standards, certifications, audit rights, or breach notification obligations. These three elements — a prohibition on testing, no affirmative commitments, and no incident notification — compound to create a structural gap in security assurance. Customer can neither verify security independently nor rely on contractual obligations to ensure it.

**Assignment without consent in change of control + ML training rights + no subprocessor controls**: Section 12.6 permits assignment in merger, acquisition, or change of control without consent. Combined with the ML training rights in Section 1.6 and the absence of any subprocessor restrictions, Customer's data and content could transfer to an acquiring entity that uses it for ML training, with third-party model components, through subprocessors unknown to Customer — with no mechanism for Customer to object, withdraw consent, or exit without liability.

**Post-termination data lifecycle gap**: Section 5.5(b) requires deletion only "upon Customer's request" within 60 days. Section 5.6(b) permits retention under standard backup or record retention policies. Sections 1.4 and 1.6 (both surviving termination) permit continued use of Usage Data and aggregated Customer Content for ML training and product improvement. There is no data export right and no transition assistance. The combined effect is that after termination, Customer loses access to the Product and its data immediately, must affirmatively request deletion, may wait up to 60 days for deletion, and even then, Provider may retain data under backup policies and continue using aggregated/de-identified versions under the surviving ML and Usage Data licenses — with no mechanism for Customer to verify compliance.

**Payment obligation asymmetry around force majeure**: Sections 5.4 and 12.12 both specify that force majeure does not excuse Customer's payment obligations. If a Force Majeure Event prevents Provider from delivering service, Customer must continue paying until either the event resolves or 30 consecutive days pass (triggering the termination right in Section 5.4). Customer pays for service it cannot receive, with the only exit being termination after 30 days of non-delivery, at which point Customer receives only a prorated refund of prepaid Fees for the remainder of the Subscription Period — not a refund covering the period of non-delivery.
