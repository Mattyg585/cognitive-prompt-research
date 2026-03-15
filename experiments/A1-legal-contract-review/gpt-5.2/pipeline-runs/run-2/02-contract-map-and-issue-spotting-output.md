---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: pipeline
run: 2
stage: 02-contract-map-and-issue-spotting
---

contract_map:
  contract_type_guess: "Cloud Service Agreement / SaaS subscription terms (Common Paper CSA v2.1 standard terms)"
  parties:
    customer: "Customer (buyer; unnamed in provided text)"
    provider: "Provider (cloud service provider; unnamed in provided text)"
  structure:
    sections:
      - { id: S-001, heading: "SERVICE", section_ref: "§1" }
      - { id: S-002, heading: "RESTRICTIONS & OBLIGATIONS", section_ref: "§2" }
      - { id: S-003, heading: "PRIVACY & SECURITY", section_ref: "§3" }
      - { id: S-004, heading: "PAYMENT & TAXES", section_ref: "§4" }
      - { id: S-005, heading: "TERM & TERMINATION", section_ref: "§5" }
      - { id: S-006, heading: "REPRESENTATIONS & WARRANTIES", section_ref: "§6" }
      - { id: S-007, heading: "DISCLAIMER OF WARRANTIES", section_ref: "§7" }
      - { id: S-008, heading: "LIMITATION OF LIABILITY", section_ref: "§8" }
      - { id: S-009, heading: "INDEMNIFICATION", section_ref: "§9" }
      - { id: S-010, heading: "CONFIDENTIALITY", section_ref: "§10" }
      - { id: S-011, heading: "RESERVATION OF RIGHTS", section_ref: "§11" }
      - { id: S-012, heading: "GENERAL TERMS", section_ref: "§12" }
      - { id: S-013, heading: "DEFINITIONS", section_ref: "§13" }
    exhibits_and_schedules:
      - { id: X-001, title: "Order Form", ref: "Referenced throughout (e.g., §§1.2, 5.1; definitions §13.1)" }
      - { id: X-002, title: "Cover Page", ref: "Referenced in §§5.6(a), 13.1" }
      - { id: X-003, title: "Key Terms", ref: "Referenced in §3.2" }
      - { id: X-004, title: "Data Processing Agreement (DPA)", ref: "Referenced in §3.1" }
      - { id: X-005, title: "Documentation", ref: "Referenced in §2.1(b)" }
      - { id: X-006, title: "Use Limitations", ref: "Referenced in §2.1(b)" }
      - { id: X-007, title: "Additional Warranties", ref: "Referenced in §6.1(d)" }
  architecture_lenses:
    order_of_precedence: unclear
    incorporation_by_reference: present
    defined_terms_pressure_points:
      - term: "Variables"
        refs: [EX-020]
        note: "Core commercial/legal fields appear as 'Variables' defined on the Cover Page; if not defined, they default to 'none'/'not applicable'."
      - term: "Usage Data"
        refs: [EX-002, EX-003]
        note: "Usage Data is collected/analyzed and may be used broadly; disclosure limitation is tied to aggregation/non-identification."
      - term: "Customer Content"
        refs: [EX-004, EX-005, EX-006]
        note: "Customer Content is licensed for service delivery/maintenance and may be used (aggregated/de-identified) for AI/ML development/training."
      - term: "Personal Data (GDPR)"
        refs: [EX-008]
        note: "GDPR processing is tied to entering a DPA; DPA terms control if present and in conflict."
      - term: "Prohibited Data"
        refs: [EX-009]
        note: "Submission restrictions depend on Order Form or Key Terms (not provided)."
      - term: "General Cap Amount / Increased Cap Amount / Increased Claims / Unlimited Claims"
        refs: [EX-015, EX-017]
        note: "Liability caps and carveouts depend on defined terms/variables not included in provided text."
      - term: "Provider Covered Claims / Customer Covered Claims"
        refs: [EX-018, EX-019]
        note: "Indemnity scope depends on defined terms not included in provided text."
      - term: "Governing Law / Chosen Courts"
        refs: [EX-024]
        note: "Jurisdictional terms are variables (not provided)."
    cross_clause_interactions:
      - note: "If the parties have a DPA, the DPA controls rights/obligations for Personal Data and controls in the event of conflict with this Agreement."
        refs: [EX-008]
      - note: "Survival section explicitly keeps Sections 1.4 and 1.6 (Feedback/Usage Data; Machine Learning) in force after termination/expiration."
        refs: [EX-013]
      - note: "Limitation-of-liability carveouts reference 'breach of Section 10 (Confidentiality)' and categories of 'Increased Claims'/'Unlimited Claims'."
        refs: [EX-017]
      - note: "Indemnification is stated as the exclusive remedy for Covered Claims, together with termination rights."
        refs: [EX-022]

evidence_index:
  - ex_id: EX-001
    section_ref: "§1.1"
    heading: "Access and Use"
    quote_verbatim: |-
      "During the Subscription Period and subject to the terms of this Agreement, Customer may (a) access and use the Cloud Service; and (b) copy and use the included Software and Documentation only as needed to access and use the Cloud Service, in each case, for its internal business purposes."
    notes: "Scope of permitted use; ties to Subscription Period."

  - ex_id: EX-002
    section_ref: "§1.4"
    heading: "Feedback and Usage Data"
    quote_verbatim: |-
      "Provider may collect and analyze Usage Data, and Provider may freely use Usage Data to maintain, improve, enhance, and promote Provider's products and services without restriction or obligation."
    notes: "Broad use right for Usage Data."

  - ex_id: EX-003
    section_ref: "§1.4"
    heading: "Feedback and Usage Data"
    quote_verbatim: |-
      "However, Provider may only disclose Usage Data to others if the Usage Data is aggregated and does not identify Customer or Users."
    notes: "Disclosure condition tied to aggregation/non-identification."

  - ex_id: EX-004
    section_ref: "§1.5"
    heading: "Customer Content"
    quote_verbatim: |-
      "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings."
    notes: "License to Customer Content framed as 'as needed' for provision/maintenance."

  - ex_id: EX-005
    section_ref: "§1.6"
    heading: "Machine Learning"
    quote_verbatim: |-
      "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes."
    notes: "AI/ML training/enhancement authorization; includes third-party components."

  - ex_id: EX-006
    section_ref: "§1.6"
    heading: "Machine Learning"
    quote_verbatim: |-
      "However, (a) Usage Data and Customer Content must be aggregated before it can be used for these purposes, and (b) Provider will use commercially reasonable efforts consistent with industry standard technology to de-identify Usage Data and Customer Content before such use."
    notes: "Conditions for AI/ML use (aggregation; de-identification)."

  - ex_id: EX-007
    section_ref: "§1.6"
    heading: "Machine Learning"
    quote_verbatim: |-
      "Nothing in this section will reduce or limit Provider's obligations regarding Personal Data that may be contained in Usage Data or Customer Content under Applicable Data Protection Laws."
    notes: "Preserves (unspecified) obligations under data protection laws."

  - ex_id: EX-008
    section_ref: "§3.1"
    heading: "Personal Data"
    quote_verbatim: |-
      "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider. If the parties have a DPA, each party will comply with its obligations in the DPA, the terms of the DPA will control each party's rights and obligations as to Personal Data, and the terms of the DPA will control in the event of any conflict with this Agreement."
    notes: "DPA prerequisite for GDPR Personal Data; DPA precedence for Personal Data."

  - ex_id: EX-009
    section_ref: "§3.2"
    heading: "Prohibited Data"
    quote_verbatim: |-
      "Customer will not (and will not allow anyone else to) submit Prohibited Data to the Product unless authorized by the Order Form or Key Terms."
    notes: "Prohibited Data carveout depends on Order Form/Key Terms."

  - ex_id: EX-010
    section_ref: "§2.1(a)(v)"
    heading: "Restrictions on Customer"
    quote_verbatim: |-
      "conduct security or vulnerability tests on, interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product;"
    notes: "Explicit restriction on security/vulnerability testing."

  - ex_id: EX-011
    section_ref: "§2.1(b)"
    heading: "Restrictions on Customer"
    quote_verbatim: |-
      "Use of the Product must comply with all Documentation and Use Limitations."
    notes: "Operational constraints incorporate Documentation/Use Limitations (not provided)."

  - ex_id: EX-012
    section_ref: "§2.2"
    heading: "Suspension"
    quote_verbatim: |-
      "If Customer (a) has an outstanding, undisputed balance on its account for more than 30 days; (b) breaches Section 2.1 (Restrictions on Customer); or (c) uses the Product in violation of the Agreement or in a way that materially and negatively impacts the Product or others, then Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical."
    notes: "Suspension triggers and notice qualifier ('with or without notice')."

  - ex_id: EX-013
    section_ref: "§5.6(a)"
    heading: "Survival"
    quote_verbatim: |-
      "The following sections will survive expiration or termination of the Agreement: Section 1.4 (Feedback and Usage Data), Section 1.6 (Machine Learning), Section 2.1 (Restrictions on Customer), Section 4 (Payment & Taxes) for Fees accrued or payable before expiration or termination, Section 5.5 (Effect of Termination), Section 5.6 (Survival), Section 6 (Representations & Warranties), Section 7 (Disclaimer of Warranties), Section 8 (Limitation of Liability), Section 9 (Indemnification), Section 10 (Confidentiality), Section 11 (Reservation of Rights), Section 12 (General Terms), Section 13 (Definitions), and the portions of a Cover Page referenced by these sections."
    notes: "Enumerated survival; explicitly includes 1.4 and 1.6."

  - ex_id: EX-014
    section_ref: "§5.5(b)"
    heading: "Effect of Termination"
    quote_verbatim: |-
      "Upon Customer's request, Provider will delete Customer Content within 60 days."
    notes: "Deletion obligation is upon request; timing is 60 days."

  - ex_id: EX-015
    section_ref: "§8.1"
    heading: "Liability Caps"
    quote_verbatim: |-
      "Each party's total cumulative liability for all claims will not be more than the General Cap Amount."
    notes: "Cap amount is a variable not included in provided text."

  - ex_id: EX-016
    section_ref: "§8.2"
    heading: "Damages Waiver"
    quote_verbatim: |-
      "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."
    notes: "Categories of damages waived."

  - ex_id: EX-017
    section_ref: "§8.4"
    heading: "Exceptions"
    quote_verbatim: |-
      "Section 8.2 does not apply to Increased Claims or breach of Section 10 (Confidentiality)."
    notes: "Carveout ties limitation to defined terms and confidentiality breaches."

  - ex_id: EX-018
    section_ref: "§9.1"
    heading: "Protection by Provider"
    quote_verbatim: |-
      "Provider will indemnify, defend, and hold harmless Customer from Provider Covered Claims and all resulting damages, costs, and expenses including reasonable attorneys' fees."
    notes: "Provider indemnity exists but depends on definition of Provider Covered Claims."

  - ex_id: EX-019
    section_ref: "§9.2"
    heading: "Protection by Customer"
    quote_verbatim: |-
      "Customer will indemnify, defend, and hold harmless Provider from Customer Covered Claims and all resulting damages, costs, and expenses."
    notes: "Customer indemnity exists but depends on definition of Customer Covered Claims."

  - ex_id: EX-020
    section_ref: "§13.1"
    heading: "Definitions (Variables)"
    quote_verbatim: |-
      "Variables have meanings given on the Cover Page; undefined variables mean \"none\" or \"not applicable.\""
    notes: "Variables framework affects multiple business/legal terms referenced elsewhere."

  - ex_id: EX-021
    section_ref: "§12.8"
    heading: "Logo Rights"
    quote_verbatim: |-
      "Provider may use Customer's name and logo in marketing."
    notes: "Marketing permission stated at a high level; details not specified here."

  - ex_id: EX-022
    section_ref: "§9.6"
    heading: "Exclusive Remedy"
    quote_verbatim: |-
      "Section 9, together with termination rights, describes exclusive remedies for Covered Claims."
    notes: "Exclusive-remedy linkage to indemnification/termination."

  - ex_id: EX-023
    section_ref: "§12.1"
    heading: "Entire Agreement"
    quote_verbatim: |-
      "This Agreement supersedes all prior statements. Provider rejects terms in Customer's purchase orders."
    notes: "PO terms rejected; entire agreement language."

  - ex_id: EX-024
    section_ref: "§12.3"
    heading: "Governing Law"
    quote_verbatim: |-
      "The Governing Law applies without regard to conflict of laws. Chosen Courts have exclusive jurisdiction."
    notes: "Governing law / forum are variables not shown in provided text."

candidate_issues:
  - issue_id: I-001
    title: "AI/ML training use of Usage Data and Customer Content (including third-party components)"
    description: "The agreement authorizes Provider to process and use Usage Data and Customer Content to develop, train, or enhance AI/ML models that are part of Provider's products and services, including third-party components, subject to aggregation and de-identification conditions."
    why_it_matters: "This can affect data governance expectations, internal approvals, and downstream use/disclosure considerations, especially if Customer Content contains sensitive business information or if third parties are involved in model components."
    evidence_refs: [EX-005, EX-006, EX-007]
    missing_info_questions:
      - "What qualifies as 'aggregated' for these purposes, and is aggregation performed before any third-party processing?"
      - "What technical and organizational measures are used to de-identify, and is there any standard or testing method referenced?"
      - "Do any product settings allow Customer to disable AI/ML training on its data?"

  - issue_id: I-002
    title: "Usage Data broad use rights; disclosure limited by aggregation/non-identification"
    description: "Provider may collect and analyze Usage Data and may freely use it to maintain, improve, enhance, and promote products/services without restriction or obligation; Provider may disclose Usage Data only if aggregated and does not identify Customer or Users."
    why_it_matters: "Usage Data handling can implicate privacy, competitive sensitivity, and compliance obligations; definitions and implementation details determine how much information can be derived from Usage Data and how it is shared externally."
    evidence_refs: [EX-002, EX-003]
    missing_info_questions:
      - "How is 'Usage Data' defined (scope, fields, and whether it includes content-derived signals)?"
      - "What is the aggregation threshold and how is non-identification assessed?"

  - issue_id: I-003
    title: "GDPR Personal Data requires a DPA; DPA controls in conflicts"
    description: "Before submitting GDPR-governed Personal Data, Customer must enter into a data processing agreement with Provider; if the parties have a DPA, the DPA controls rights/obligations for Personal Data and controls in the event of conflict with the Agreement."
    why_it_matters: "Operational deployment may require finalizing a DPA before go-live for certain data; the DPA can materially alter privacy/security obligations and allocation of responsibilities."
    evidence_refs: [EX-008]
    missing_info_questions:
      - "Is a DPA template available and does it include cross-border transfer terms (e.g., SCCs) if needed?"
      - "Does the service involve sub-processors and, if so, where are they listed and how are changes notified?"

  - issue_id: I-004
    title: "Prohibited Data restriction depends on Order Form or Key Terms (not provided)"
    description: "Customer may not submit Prohibited Data unless authorized by the Order Form or Key Terms."
    why_it_matters: "Whether the product can be used for certain categories of data depends on external documents; misalignment can block intended use cases or create compliance/process obligations for data classification and controls."
    evidence_refs: [EX-009]
    missing_info_questions:
      - "How is 'Prohibited Data' defined, and does it include regulated data types relevant to Customer (e.g., payment/health data)?"
      - "Do the Order Form or Key Terms authorize any Prohibited Data categories, and under what safeguards?"

  - issue_id: I-005
    title: "Incorporation of Documentation and Use Limitations (not provided)"
    description: "Use of the Product must comply with all Documentation and Use Limitations."
    why_it_matters: "External documentation and use limitations can create ongoing operational obligations (usage restrictions, technical requirements, security requirements) that affect compliance, procurement approvals, and intended deployment."
    evidence_refs: [EX-011]
    missing_info_questions:
      - "Where are the Documentation and Use Limitations located, and are they versioned/locked for the subscription term?"
      - "Can Provider change Documentation/Use Limitations unilaterally, and if so, what notice applies?"

  - issue_id: I-006
    title: "Suspension rights 'with or without notice'"
    description: "Provider may temporarily suspend access for certain triggers (including breach of restrictions and certain use impacts) and may do so with or without notice, with a stated intent to try to inform Customer when practical."
    why_it_matters: "Service interruption procedures and notice expectations affect business continuity planning and incident response; suspension criteria and notice mechanics shape operational predictability."
    evidence_refs: [EX-012]
    missing_info_questions:
      - "Are there any cure or escalation steps before suspension (other than the 'when practical' notice)?"
      - "Is there an SLA/credit scheme in the Order Form that addresses downtime unrelated to suspension?"

  - issue_id: I-007
    title: "Restriction on security or vulnerability testing"
    description: "Customer is restricted from conducting security or vulnerability tests on the Product."
    why_it_matters: "Security review programs may require testing or scanning; restrictions can affect how Customer completes security due diligence or ongoing monitoring."
    evidence_refs: [EX-010]
    missing_info_questions:
      - "Is there an authorized testing process (e.g., written permission, scope limits) outside this clause?"
      - "Are third-party security assessments (SOC 2/ISO) available as substitutes?"

  - issue_id: I-008
    title: "Customer Content deletion is upon request and within 60 days"
    description: "Upon expiration or termination, and upon Customer's request, Provider will delete Customer Content within 60 days."
    why_it_matters: "Data lifecycle management may require specific deletion timelines and automatic deletion expectations; the 'upon request' condition affects internal offboarding processes and recordkeeping."
    evidence_refs: [EX-014]
    missing_info_questions:
      - "Does Provider delete Customer Content automatically absent a request, and what happens to backups/logs?"
      - "Is there a data export mechanism and time window before deletion?"

  - issue_id: I-009
    title: "Liability caps and key commercial variables not provided"
    description: "The agreement limits each party's total cumulative liability to a 'General Cap Amount' and references additional cap constructs (e.g., Increased Cap Amount) and categories (Increased Claims, Unlimited Claims) that are not specified in the provided text."
    why_it_matters: "Liability allocation depends on the cap amounts and carveouts; missing cap values prevent assessing the practical exposure and recovery expectations for claims."
    evidence_refs: [EX-015, EX-017, EX-020]
    missing_info_questions:
      - "What are the General Cap Amount and any Increased/Unlimited claim parameters on the Cover Page?"
      - "How are 'Increased Claims' and 'Unlimited Claims' defined in the Cover Page/Key Terms?"

  - issue_id: I-010
    title: "Consequential and other damages waiver"
    description: "The agreement waives liability for lost profits/revenues and various categories of consequential, special, indirect, exemplary, punitive, or incidental damages."
    why_it_matters: "Remedy limitations can affect recovery for business interruption, data incidents, or other downstream impacts; internal stakeholders may need to align expectations with the contract's damages framework."
    evidence_refs: [EX-016]
    missing_info_questions:
      - "Do the cap exceptions (e.g., for confidentiality breaches) meaningfully change the impact of this waiver in likely claim scenarios?"

  - issue_id: I-011
    title: "Indemnity scope depends on defined 'Covered Claims' and exclusive remedy provision"
    description: "Provider and Customer each provide indemnification for their respective 'Covered Claims', and the agreement states indemnification (together with termination rights) is the exclusive remedy for Covered Claims."
    why_it_matters: "The practical protection depends on how Covered Claims are defined and any exclusions; the exclusive-remedy framing can limit other routes to recovery for claim categories that fall within Covered Claims."
    evidence_refs: [EX-018, EX-019, EX-022]
    missing_info_questions:
      - "How are Provider Covered Claims and Customer Covered Claims defined, and do they include IP infringement, data-related claims, or regulatory claims?"
      - "Are there monetary caps or process conditions tied to indemnification in the Cover Page/Order Form?"

  - issue_id: I-012
    title: "Provider marketing use of Customer name and logo"
    description: "Provider may use Customer's name and logo in marketing."
    why_it_matters: "Brand use can require internal approvals and may be inconsistent with procurement or comms policies; scope and approval mechanics affect how this is implemented."
    evidence_refs: [EX-021]
    missing_info_questions:
      - "Is Customer approval required for specific uses, and can Customer revoke consent?"
      - "Are there brand guidelines or limitations referenced elsewhere (e.g., Key Terms)?"

  - issue_id: I-013
    title: "Governing law and forum are variables not shown"
    description: "The agreement states the 'Governing Law' applies and 'Chosen Courts have exclusive jurisdiction' but does not specify them in the provided text."
    why_it_matters: "Forum and governing law influence dispute handling, cost, and enforcement; missing values prevent confirming whether the venue aligns with Customer's legal and operational constraints."
    evidence_refs: [EX-024, EX-020]
    missing_info_questions:
      - "What are the selected Governing Law and Chosen Courts on the Cover Page/Key Terms?"

  - issue_id: I-014
    title: "Entire agreement + rejection of Customer purchase order terms"
    description: "The agreement states it supersedes prior statements and rejects terms in Customer's purchase orders."
    why_it_matters: "If Customer procurement processes rely on PO terms (e.g., for ordering, invoicing, or policy clauses), this clause can affect how those terms apply and what must be negotiated into the agreement documents."
    evidence_refs: [EX-023]
    missing_info_questions:
      - "Does Customer intend to rely on any PO terms; if so, should they be incorporated into the Order Form or Key Terms instead?"
