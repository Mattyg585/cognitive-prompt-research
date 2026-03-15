---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: pipeline
run: 3
stage: 02-contract-map-and-issue-spotting
---

contract_map:
  contract_type_guess: "Cloud Service Agreement (SaaS) standard terms + Order Form(s) framework"
  parties:
    customer: "Customer"
    provider: "Provider"
    customer_affiliate_note: "Customer Affiliate may enter a separate Order Form creating a separate agreement"
  structure:
    sections:
      - id: S-001
        heading: "SERVICE"
        section_ref: "Section 1"
      - id: S-002
        heading: "RESTRICTIONS & OBLIGATIONS"
        section_ref: "Section 2"
      - id: S-003
        heading: "PRIVACY & SECURITY"
        section_ref: "Section 3"
      - id: S-004
        heading: "PAYMENT & TAXES"
        section_ref: "Section 4"
      - id: S-005
        heading: "TERM & TERMINATION"
        section_ref: "Section 5"
      - id: S-006
        heading: "REPRESENTATIONS & WARRANTIES"
        section_ref: "Section 6"
      - id: S-007
        heading: "DISCLAIMER OF WARRANTIES"
        section_ref: "Section 7"
      - id: S-008
        heading: "LIMITATION OF LIABILITY"
        section_ref: "Section 8"
      - id: S-009
        heading: "INDEMNIFICATION"
        section_ref: "Section 9"
      - id: S-010
        heading: "CONFIDENTIALITY"
        section_ref: "Section 10"
      - id: S-011
        heading: "RESERVATION OF RIGHTS"
        section_ref: "Section 11"
      - id: S-012
        heading: "GENERAL TERMS"
        section_ref: "Section 12"
      - id: S-013
        heading: "DEFINITIONS"
        section_ref: "Section 13"
    exhibits_and_schedules:
      - id: X-001
        title: "Order Form"
        ref: "Referenced in multiple sections (e.g., 1.1, 1.2, 3.2, 4.1, 5.1)"
      - id: X-002
        title: "Cover Page"
        ref: "Referenced in 5.6(a) and 13.1 (variables)"
      - id: X-003
        title: "Key Terms"
        ref: "Referenced in 3.2"
      - id: X-004
        title: "Data Processing Agreement (DPA)"
        ref: "Referenced in 3.1"
      - id: X-005
        title: "Documentation and Use Limitations"
        ref: "Referenced in 2.1(b)"
      - id: X-006
        title: "Additional Warranties"
        ref: "Referenced in 6.1(d)"
  architecture_lenses:
    order_of_precedence: unclear
    incorporation_by_reference: present
    defined_terms_pressure_points:
      - "Usage Data"
      - "Customer Content"
      - "Personal Data"
      - "Applicable Data Protection Laws"
      - "Prohibited Data"
      - "Documentation"
      - "Use Limitations"
      - "Provider Covered Claims / Customer Covered Claims"
      - "General Cap Amount / Increased Cap Amount"
      - "Increased Claims / Unlimited Claims"
      - "Governing Law / Chosen Courts"
      - "Non-Renewal Notice Date / Notice Address"
      - "Additional Warranties"
      - "Variables (defined on Cover Page)"
    cross_clause_interactions:
      - note: "Section 1.6 states machine learning use of Usage Data/Customer Content and also notes it does not reduce obligations regarding Personal Data; Section 3.1 requires a DPA before submitting GDPR Personal Data and states the DPA controls conflicts."
        refs: [EX-005, EX-009]
      - note: "Customer retains rights in Customer Content, but that retention is stated to be subject to Sections 1.5 and 1.6."
        refs: [EX-004, EX-005, EX-020]
      - note: "Customer Content deletion is framed as being 'upon Customer's request' within 60 days; separately, Confidential Information may be retained under backup/record retention policies with continued application of Privacy & Security and Confidentiality."
        refs: [EX-013, EX-014]
      - note: "Liability limitations use cap variables and include exceptions/alternative categories (e.g., Increased Claims, Unlimited Claims; confidentiality breach carve-out)."
        refs: [EX-017, EX-025]

evidence_index:
  - ex_id: EX-001
    section_ref: "1.1"
    heading: "Access and Use"
    quote_verbatim: |-
      **1.1 Access and Use.** During the Subscription Period and subject to the terms of this Agreement, Customer may (a) access and use the Cloud Service; and (b) copy and use the included Software and Documentation only as needed to access and use the Cloud Service, in each case, for its internal business purposes. If a Customer Affiliate enters a separate Order Form with Provider, the Customer's Affiliate creates a separate agreement between Provider and that Affiliate, where Provider's responsibility to the Affiliate is individual and separate from Customer and Customer is not responsible for its Affiliates' agreement.
    notes: "Defines internal-use scope and clarifies separate affiliate Order Forms."

  - ex_id: EX-002
    section_ref: "1.2"
    heading: "Support"
    quote_verbatim: |-
      **1.2 Support.** During the Subscription Period, Provider will provide Technical Support as described in the Order Form.

  - ex_id: EX-027
    section_ref: "1.3"
    heading: "User Accounts"
    quote_verbatim: |-
      **1.3 User Accounts.** Customer is responsible for all actions on Users' accounts and for all Users' compliance with this Agreement. Customer and Users must protect the confidentiality of their passwords and login credentials. Customer will promptly notify Provider if it suspects or knows of any fraudulent activity with its accounts, passwords, or credentials, or if they become compromised.

  - ex_id: EX-003
    section_ref: "1.4"
    heading: "Feedback and Usage Data"
    quote_verbatim: |-
      **1.4 Feedback and Usage Data.** Customer may, but is not required to, give Provider Feedback, in which case Customer gives Feedback "AS IS". Provider may use all Feedback freely without any restriction or obligation. In addition, Provider may collect and analyze Usage Data, and Provider may freely use Usage Data to maintain, improve, enhance, and promote Provider's products and services without restriction or obligation. However, Provider may only disclose Usage Data to others if the Usage Data is aggregated and does not identify Customer or Users.

  - ex_id: EX-004
    section_ref: "1.5"
    heading: "Customer Content"
    quote_verbatim: |-
      **1.5 Customer Content.** Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings. Customer is responsible for the accuracy and content of Customer Content.

  - ex_id: EX-005
    section_ref: "1.6"
    heading: "Machine Learning"
    quote_verbatim: |-
      **1.6 Machine Learning.** Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes. However, (a) Usage Data and Customer Content must be aggregated before it can be used for these purposes, and (b) Provider will use commercially reasonable efforts consistent with industry standard technology to de-identify Usage Data and Customer Content before such use. Nothing in this section will reduce or limit Provider's obligations regarding Personal Data that may be contained in Usage Data or Customer Content under Applicable Data Protection Laws. Due to the nature of artificial intelligence and machine learning, information generated by these features may be incorrect or inaccurate. Product features that include artificial intelligence or machine learning models are not human and are not a substitute for human oversight.

  - ex_id: EX-006
    section_ref: "2.1(a)(v)"
    heading: "Restrictions on Customer (security testing)"
    quote_verbatim: |-
      (a) Except as expressly permitted by this Agreement, Customer will not (and will not allow anyone else to):

      (v) conduct security or vulnerability tests on, interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product;

  - ex_id: EX-007
    section_ref: "2.1(b)"
    heading: "Documentation and Use Limitations"
    quote_verbatim: |-
      (b) Use of the Product must comply with all Documentation and Use Limitations.

  - ex_id: EX-008
    section_ref: "2.2"
    heading: "Suspension"
    quote_verbatim: |-
      **2.2 Suspension.** If Customer (a) has an outstanding, undisputed balance on its account for more than 30 days; (b) breaches Section 2.1 (Restrictions on Customer); or (c) uses the Product in violation of the Agreement or in a way that materially and negatively impacts the Product or others, then Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical. Provider will reinstate Customer's access to the Product only if Customer resolves the underlying issue.

  - ex_id: EX-009
    section_ref: "3.1"
    heading: "Personal Data / DPA"
    quote_verbatim: |-
      **3.1 Personal Data.** Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider. If the parties have a DPA, each party will comply with its obligations in the DPA, the terms of the DPA will control each party's rights and obligations as to Personal Data, and the terms of the DPA will control in the event of any conflict with this Agreement.

  - ex_id: EX-010
    section_ref: "3.2"
    heading: "Prohibited Data"
    quote_verbatim: |-
      **3.2 Prohibited Data.** Customer will not (and will not allow anyone else to) submit Prohibited Data to the Product unless authorized by the Order Form or Key Terms.

  - ex_id: EX-011
    section_ref: "4.1"
    heading: "Fees / non-refundable"
    quote_verbatim: |-
      **4.1 Fees.** Unless the Order Form specifies a different currency, all Fees are in U.S. Dollars and are exclusive of taxes. Except for the prorated refund of prepaid Fees allowed with specific termination rights given in the Agreement, Fees are non-refundable.

  - ex_id: EX-012
    section_ref: "5.1"
    heading: "Auto-renewal"
    quote_verbatim: |-
      **5.1 Order Form and Agreement.** For each Order Form, the Agreement will start on the Order Date, continue through the Subscription Period, and automatically renew for additional Subscription Periods unless one party gives notice of non-renewal to the other party before the Non-Renewal Notice Date.

  - ex_id: EX-026
    section_ref: "5.4"
    heading: "Force Majeure termination and refund"
    quote_verbatim: |-
      **5.4 Force Majeure.** Either party may terminate an affected Order Form upon notice if a Force Majeure Event prevents the Product from materially operating for 30 or more consecutive days. Provider will pay to Customer a prorated refund of any prepaid Fees for the remainder of the Subscription Period. A Force Majeure Event does not excuse Customer's obligation to pay Fees accrued prior to termination.

  - ex_id: EX-013
    section_ref: "5.5"
    heading: "Effect of Termination (use rights; deletion)"
    quote_verbatim: |-
      **5.5 Effect of Termination.** Termination of the Framework Terms will automatically terminate all Order Forms governed by the Framework Terms. Upon any expiration or termination:

      (a) Customer will no longer have any right to use the Product.

      (b) Upon Customer's request, Provider will delete Customer Content within 60 days.

  - ex_id: EX-014
    section_ref: "5.6"
    heading: "Survival / retained Confidential Information"
    quote_verbatim: |-
      **5.6 Survival.** (a) The following sections will survive expiration or termination of the Agreement: Section 1.4 (Feedback and Usage Data), Section 1.6 (Machine Learning), Section 2.1 (Restrictions on Customer), Section 4 (Payment & Taxes) for Fees accrued or payable before expiration or termination, Section 5.5 (Effect of Termination), Section 5.6 (Survival), Section 6 (Representations & Warranties), Section 7 (Disclaimer of Warranties), Section 8 (Limitation of Liability), Section 9 (Indemnification), Section 10 (Confidentiality), Section 11 (Reservation of Rights), Section 12 (General Terms), Section 13 (Definitions), and the portions of a Cover Page referenced by these sections.

      (b) Each Recipient may retain Discloser's Confidential Information in accordance with its standard backup or record retention policies maintained in the ordinary course of business or as required by Applicable Laws, in which case Section 3 (Privacy & Security) and Section 10 (Confidentiality) will continue to apply to retained Confidential Information.

  - ex_id: EX-015
    section_ref: "6.3–6.4"
    heading: "Provider warranty (functionality) and remedy"
    quote_verbatim: |-
      **6.3 From Provider.** Provider represents and warrants to Customer that it will not materially reduce the general functionality of the Cloud Service during the Subscription Period.

      **6.4 Provider Warranty Remedy.** If Provider breaches the warranty in Section 6.3, Customer must give Provider notice within 45 days of discovering the issue. Within 45 days of receiving sufficient details, Provider will attempt to restore the general functionality. If Provider cannot resolve the issue, Customer may terminate the affected Order Form and Provider will pay a prorated refund.

  - ex_id: EX-016
    section_ref: "7.1"
    heading: "Disclaimer of warranties"
    quote_verbatim: |-
      **7.1** Provider makes no guarantees that the Product will always be safe, secure, or error-free, or that it will function without disruptions, delays, or imperfections. Except for the warranties in Section 6, Provider and Customer each disclaim all other warranties and conditions, whether express or implied, including merchantability, fitness for a particular purpose, title, and non-infringement.

  - ex_id: EX-017
    section_ref: "8.1–8.4"
    heading: "Liability caps, damages waiver, exceptions"
    quote_verbatim: |-
      **8.1 Liability Caps.** (a) Each party's total cumulative liability for all claims will not be more than the General Cap Amount. (b) If there are Increased Claims, each party's total cumulative liability for Increased Claims will not be more than the Increased Cap Amount.

      **8.2 Damages Waiver.** Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility.

      **8.4 Exceptions.** The liability cap in 8.1(a) does not apply to Increased Claims. Section 8.1 does not apply to Unlimited Claims. Section 8.2 does not apply to Increased Claims or breach of Section 10 (Confidentiality).

  - ex_id: EX-018
    section_ref: "9.1–9.6"
    heading: "Indemnification (scope, procedure, exclusive remedy)"
    quote_verbatim: |-
      **9.1 Protection by Provider.** Provider will indemnify, defend, and hold harmless Customer from Provider Covered Claims and all resulting damages, costs, and expenses including reasonable attorneys' fees.

      **9.3 Procedure.** The Indemnifying Party's obligations require the Protected Party to: (a) promptly notify; (b) provide reasonable assistance; and (c) give sole control over defense and settlement. The Indemnifying Party may not agree to settlements containing admissions of fault without consent.

      **9.5 Exclusions.** Provider's obligations don't apply to claims from unauthorized modifications, unauthorized use, combination with non-Provider items, or use of old versions. Customer's obligations don't apply to unauthorized use of Customer Content.

      **9.6 Exclusive Remedy.** Section 9, together with termination rights, describes exclusive remedies for Covered Claims.

  - ex_id: EX-019
    section_ref: "10.1, 10.4"
    heading: "Confidentiality (non-use/non-disclosure; permitted disclosures)"
    quote_verbatim: |-
      **10.1 Non-Use and Non-Disclosure.** Recipient will not use or disclose Discloser's Confidential Information except as authorized or needed under the Agreement.

      **10.4 Permitted Disclosures.** Recipient may disclose to employees, advisors, contractors with need-to-know, bound by equivalent confidentiality obligations.

  - ex_id: EX-020
    section_ref: "11.1"
    heading: "Reservation of rights"
    quote_verbatim: |-
      **11.1** Provider retains all rights in the Product. Customer retains all rights in Customer Content, subject to Sections 1.5 and 1.6.

  - ex_id: EX-021
    section_ref: "12.1"
    heading: "Entire agreement; purchase order terms"
    quote_verbatim: |-
      **12.1 Entire Agreement.** This Agreement supersedes all prior statements. Provider rejects terms in Customer's purchase orders.

  - ex_id: EX-022
    section_ref: "12.3"
    heading: "Governing law; chosen courts"
    quote_verbatim: |-
      **12.3 Governing Law.** The Governing Law applies without regard to conflict of laws. Chosen Courts have exclusive jurisdiction.

  - ex_id: EX-023
    section_ref: "12.6"
    heading: "Assignment"
    quote_verbatim: |-
      **12.6 Assignment.** No assignment without consent, except in merger/acquisition/change of control.

  - ex_id: EX-024
    section_ref: "12.8"
    heading: "Logo rights"
    quote_verbatim: |-
      **12.8 Logo Rights.** Provider may use Customer's name and logo in marketing.

  - ex_id: EX-025
    section_ref: "13.1"
    heading: "Variables on Cover Page"
    quote_verbatim: |-
      **13.1** Variables have meanings given on the Cover Page; undefined variables mean "none" or "not applicable."

candidate_issues:
  - issue_id: I-001
    title: "AI/ML training and enhancement using Usage Data and Customer Content"
    description: "The agreement authorizes Provider to process Usage Data and Customer Content to 'develop, train, or enhance' AI/ML models that are part of Provider's products and services, including third-party components, subject to aggregation and de-identification language."
    why_it_matters: "This may affect Customer expectations about how Customer Content and related data are used beyond delivering the core service, including downstream use in model development and use by third-party components."
    evidence_refs: [EX-005]
    missing_info_questions:
      - "What is the definition of 'Usage Data' and does it include event logs, metadata, content-derived features, or outputs?"
      - "Are there opt-outs, customer-specific model boundaries, or contractual limits on using Customer Content for model training?"
      - "What third-party components/subprocessors are involved in these AI/ML features?"
      - "What are the retention periods for data used in AI/ML training, and are trained model weights treated as containing Customer data?"

  - issue_id: I-002
    title: "Broad rights to use Feedback and Usage Data (including for promotion)"
    description: "Provider may use Feedback 'freely without any restriction or obligation' and may collect/analyze and 'freely use' Usage Data to maintain, improve, enhance, and promote Provider's products and services; disclosure to others is limited to aggregated, non-identifying Usage Data."
    why_it_matters: "This may affect confidentiality and competitive sensitivity if Usage Data could reveal operational patterns even when aggregated, and it sets expectations for product analytics and marketing uses."
    evidence_refs: [EX-003]
    missing_info_questions:
      - "How does the contract define 'Usage Data' and 'aggregated' in this context?"
      - "Is Customer permitted to restrict use of Usage Data for promotion/marketing?"

  - issue_id: I-003
    title: "Scope of Provider license to Customer Content; deletion on request; retention via backups"
    description: "Provider may 'copy, display, modify, and use' Customer Content as needed to provide and maintain the Product and 'related offerings.' Upon expiration/termination, Provider will delete Customer Content within 60 days upon Customer's request. The contract also allows retention of Confidential Information in backups/record retention policies with continued confidentiality and privacy obligations."
    why_it_matters: "This affects data governance expectations (use scope, retention, and deletion mechanics) and may require operational processes to request deletion and understand what may be retained in backups."
    evidence_refs: [EX-004, EX-013, EX-014]
    missing_info_questions:
      - "What are 'related offerings' and do they include optional modules, add-ons, or separate products?"
      - "Is Customer Content deleted automatically on termination, or only if Customer requests it (and how is that request made)?"
      - "What are Provider's standard backup/retention periods and deletion timelines for backups?"

  - issue_id: I-004
    title: "DPA required for GDPR Personal Data; DPA controls conflicts"
    description: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement (DPA) with Provider, and if the parties have a DPA, the DPA controls rights/obligations as to Personal Data and controls in the event of a conflict with the Agreement."
    why_it_matters: "This creates a dependency on a separate document for GDPR processing terms and may affect launch timing and compliance responsibilities."
    evidence_refs: [EX-009]
    missing_info_questions:
      - "Is there a standard DPA available, and what are the security measures, subprocessors, and cross-border transfer terms?"
      - "Does Provider process any Personal Data outside GDPR scope (and what governs those terms if not in a DPA)?"

  - issue_id: I-005
    title: "Prohibited Data restrictions depend on Order Form or Key Terms not provided"
    description: "Customer is prohibited from submitting 'Prohibited Data' unless authorized by the Order Form or Key Terms."
    why_it_matters: "Whether Customer can use the service for intended datasets depends on how 'Prohibited Data' is defined and what the Order Form/Key Terms permit."
    evidence_refs: [EX-010]
    missing_info_questions:
      - "How is 'Prohibited Data' defined in the Key Terms/Definitions, and does it include regulated data types relevant to Customer?"
      - "Does the Order Form authorize any categories of Prohibited Data for this deal?"

  - issue_id: I-006
    title: "Restriction on security or vulnerability testing"
    description: "Customer may not 'conduct security or vulnerability tests on' the Product, among other prohibited activities."
    why_it_matters: "This may affect Customer security assurance activities (e.g., penetration testing, scanning) and how Customer validates security requirements."
    evidence_refs: [EX-006]
    missing_info_questions:
      - "Is there a permitted security testing process (e.g., written approval, scope limits) in the Order Form or separate policy?"

  - issue_id: I-007
    title: "Documentation and Use Limitations incorporated by reference"
    description: "Use of the Product must comply with all Documentation and Use Limitations."
    why_it_matters: "This can create additional obligations and restrictions outside the provided Standard Terms, depending on what the Documentation and Use Limitations say and how they change over time."
    evidence_refs: [EX-007]
    missing_info_questions:
      - "What specific Documentation and Use Limitations apply to the Product for this deal, and where are they located?"
      - "Can Documentation/Use Limitations be updated unilaterally, and if so, what notice applies?"

  - issue_id: I-008
    title: "Provider suspension rights 'with or without notice'"
    description: "Provider may temporarily suspend access for specified triggers (including nonpayment and certain violations) and may do so 'with or without notice,' with an intent to inform Customer 'when practical' and reinstatement conditioned on resolving the issue."
    why_it_matters: "This can affect service continuity and incident response planning, including how quickly Customer can remediate and restore access."
    evidence_refs: [EX-008]
    missing_info_questions:
      - "Are there cure periods, escalation paths, or minimum notice commitments in the Order Form/SLA?"
      - "Does suspension apply to the whole tenant/account or only specific users/workloads?"

  - issue_id: I-009
    title: "Auto-renewal mechanics depend on Non-Renewal Notice Date"
    description: "Each Order Form automatically renews unless a party gives notice of non-renewal before the Non-Renewal Notice Date."
    why_it_matters: "Renewal timing and notice deadlines depend on variables not included in the provided Standard Terms and can affect procurement calendaring."
    evidence_refs: [EX-012]
    missing_info_questions:
      - "What is the Non-Renewal Notice Date for the Order Form (e.g., 30/60/90 days)?"
      - "What is the Notice Address for sending non-renewal notices?"

  - issue_id: I-010
    title: "Non-refundable fees with limited prorated refund pathways"
    description: "Fees are non-refundable except for prorated refund of prepaid Fees allowed with specific termination rights in the Agreement; separate sections describe prorated refunds in certain termination scenarios."
    why_it_matters: "This affects financial flexibility if Customer needs to terminate early or if service availability issues lead to termination."
    evidence_refs: [EX-011, EX-026, EX-015]
    missing_info_questions:
      - "Which termination rights are intended to provide prorated refunds for this deal (beyond those explicitly stated)?"
      - "Are there SLA credits or additional refund terms in the Order Form?"

  - issue_id: I-011
    title: "Provider warranty scope and remedy (functionality; notice window)"
    description: "Provider warrants it will not materially reduce the general functionality during the Subscription Period; if breached, Customer must give notice within 45 days of discovering the issue, Provider attempts to restore, and if not resolved Customer may terminate and receive a prorated refund."
    why_it_matters: "This sets the baseline service warranty and prescribes timelines and remedies that may influence how Customer tracks issues and pursues relief."
    evidence_refs: [EX-015]
    missing_info_questions:
      - "What are the 'Additional Warranties' referenced in 6.1(d), and do any apply to security/privacy?"

  - issue_id: I-012
    title: "Disclaimer of warranties includes safe/secure/error-free statements"
    description: "Provider makes no guarantees that the Product will always be safe, secure, or error-free, and disclaims other warranties/conditions except those in Section 6."
    why_it_matters: "This shapes expectations around reliability and security assurances and interacts with any security requirements that may need to be captured in the Order Form, DPA, or security addendum."
    evidence_refs: [EX-016]
    missing_info_questions:
      - "Are there security commitments, audit reports, or uptime/SLA terms in the Order Form or separate security documentation?"

  - issue_id: I-013
    title: "Liability caps depend on Cover Page variables; category-based exceptions"
    description: "Total cumulative liability is capped by the General Cap Amount (and Increased Cap Amount for Increased Claims), with additional exceptions and categories including Unlimited Claims and a confidentiality-breach carve-out from the damages waiver/certain limitations. Variables are defined on the Cover Page and may be 'none' or 'not applicable' if undefined."
    why_it_matters: "Customer's potential recovery and exposure depend on how caps and claim categories are defined and populated in the Cover Page and Definitions, which are not included in the provided text."
    evidence_refs: [EX-017, EX-025]
    missing_info_questions:
      - "What are the General Cap Amount and Increased Cap Amount in the Cover Page for this deal?"
      - "How are 'Increased Claims' and 'Unlimited Claims' defined in the Definitions/Key Terms?"

  - issue_id: I-014
    title: "Indemnification scope depends on defined terms; exclusive remedy language"
    description: "Provider indemnifies Customer for 'Provider Covered Claims' with defense/hold harmless obligations, subject to procedure requirements and exclusions; Section 9 plus termination rights is described as the exclusive remedies for Covered Claims."
    why_it_matters: "Whether indemnity covers key scenarios (e.g., third-party IP claims) depends on how 'Provider Covered Claims' is defined and how exclusions apply; the exclusive remedy framing may affect other remedies."
    evidence_refs: [EX-018]
    missing_info_questions:
      - "What is the definition/scope of 'Provider Covered Claims' and does it include intellectual property infringement claims?"
      - "Are there limitations on defense counsel choice, settlement authority, or cooperation costs beyond what is stated here?"

  - issue_id: I-015
    title: "Governing law and exclusive jurisdiction variables"
    description: "The Governing Law applies and Chosen Courts have exclusive jurisdiction."
    why_it_matters: "The selected law and forum can affect dispute handling and enforcement considerations; the specific selections are not provided in the Standard Terms excerpt."
    evidence_refs: [EX-022]
    missing_info_questions:
      - "What are the Governing Law and Chosen Courts specified on the Cover Page/Key Terms?"

  - issue_id: I-016
    title: "Provider marketing use of Customer name and logo"
    description: "Provider may use Customer's name and logo in marketing."
    why_it_matters: "This affects brand/communications controls and may require internal approvals or limitations on public references."
    evidence_refs: [EX-024]
    missing_info_questions:
      - "Are there limitations (e.g., prior written approval, timing, press release coordination) in the Order Form or Cover Page?"

  - issue_id: I-017
    title: "Entire agreement clause rejects Customer purchase order terms"
    description: "The Agreement supersedes prior statements and Provider rejects terms in Customer's purchase orders."
    why_it_matters: "This can limit reliance on procurement terms typically included in POs and may require ensuring any required terms are included directly in the Order Form/Cover Page/DPA."
    evidence_refs: [EX-021]
    missing_info_questions:
      - "Are any Customer procurement terms intended to apply (e.g., supplier code, security addendum), and if so where are they incorporated?"

  - issue_id: I-018
    title: "Assignment restrictions with M&A/change-of-control exception"
    description: "Assignments require consent, except in merger/acquisition/change of control."
    why_it_matters: "This can affect corporate restructuring, affiliate rollups, or transfers of an Order Form/Agreement rights and obligations."
    evidence_refs: [EX-023]
    missing_info_questions:
      - "Does the consent requirement apply to assignment by operation of law outside the stated exception?"

  - issue_id: I-019
    title: "Customer responsibility for user actions and credential security"
    description: "Customer is responsible for actions on Users' accounts and must protect credential confidentiality and notify Provider of suspected/known fraudulent activity or compromise."
    why_it_matters: "This frames operational responsibilities for account governance and incident communications, and may interact with internal security policies and access management practices."
    evidence_refs: [EX-027]
    missing_info_questions:
      - "What authentication/security controls are available (e.g., SSO/MFA) and are they included in the subscription/Order Form?"
