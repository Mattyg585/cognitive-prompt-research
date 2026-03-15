---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: pipeline
run: 1
stage: 02-contract-map-and-issue-spotting
---

contract_map:
  contract_type_guess: "Cloud Service Agreement (SaaS) — standard terms"
  parties:
    customer: "Customer"
    provider: "Provider"
  structure:
    sections:
      - id: S-001
        heading: "SERVICE"
        section_ref: "1"
      - id: S-002
        heading: "RESTRICTIONS & OBLIGATIONS"
        section_ref: "2"
      - id: S-003
        heading: "PRIVACY & SECURITY"
        section_ref: "3"
      - id: S-004
        heading: "PAYMENT & TAXES"
        section_ref: "4"
      - id: S-005
        heading: "TERM & TERMINATION"
        section_ref: "5"
      - id: S-006
        heading: "REPRESENTATIONS & WARRANTIES"
        section_ref: "6"
      - id: S-007
        heading: "DISCLAIMER OF WARRANTIES"
        section_ref: "7"
      - id: S-008
        heading: "LIMITATION OF LIABILITY"
        section_ref: "8"
      - id: S-009
        heading: "INDEMNIFICATION"
        section_ref: "9"
      - id: S-010
        heading: "CONFIDENTIALITY"
        section_ref: "10"
      - id: S-011
        heading: "RESERVATION OF RIGHTS"
        section_ref: "11"
      - id: S-012
        heading: "GENERAL TERMS"
        section_ref: "12"
      - id: S-013
        heading: "DEFINITIONS"
        section_ref: "13"
    exhibits_and_schedules:
      - id: X-001
        title: "Order Form"
        ref: "Referenced in Sections 1.2, 5.1, 3.2, 4.1, 6.4"
      - id: X-002
        title: "Cover Page (Variables)"
        ref: "Referenced in Section 13.1; portions survive per Section 5.6(a)"
      - id: X-003
        title: "Key Terms"
        ref: "Referenced in Section 3.2; likely defines Prohibited Data and variables"
      - id: X-004
        title: "Data Processing Agreement (DPA)"
        ref: "Referenced in Section 3.1; controls in event of conflict"
      - id: X-005
        title: "Documentation / Use Limitations"
        ref: "Referenced in Section 2.1(b)"
  architecture_lenses:
    order_of_precedence: unclear
    incorporation_by_reference: present
    defined_terms_pressure_points:
      - "General Cap Amount"
      - "Increased Claims"
      - "Increased Cap Amount"
      - "Unlimited Claims"
      - "Provider Covered Claims"
      - "Customer Covered Claims"
      - "Customer Content"
      - "Usage Data"
      - "Prohibited Data"
      - "Applicable Data Protection Laws"
      - "Confidential Information"
      - "Order Form"
      - "Key Terms"
      - "Cover Page"
      - "Non-Renewal Notice Date"
      - "Payment Process"
      - "Additional Warranties"
      - "Documentation"
      - "Use Limitations"
      - "Governing Law"
      - "Chosen Courts"
      - "Notice Address"
    cross_clause_interactions:
      - note: "Survival clause explicitly keeps Feedback/Usage Data and Machine Learning rights in effect after expiration/termination."
        refs: [EX-001, EX-003, EX-013]
      - note: "Deletion obligation for Customer Content is on-request and time-bound, while retention of Confidential Information in backups/record retention is permitted; interplay may affect offboarding and data retention expectations."
        refs: [EX-011, EX-012]
      - note: "Liability exceptions reference 'Increased Claims' and 'Unlimited Claims' (not defined in text provided) and separately carve out damages waiver for confidentiality breaches; interplay with confidentiality clause depends on definitions/variables on Cover Page/Key Terms."
        refs: [EX-018, EX-021, EX-029]

evidence_index:
  - ex_id: EX-001
    section_ref: "1.4"
    heading: "Feedback and Usage Data"
    quote_verbatim: |-
      **1.4 Feedback and Usage Data.** Customer may, but is not required to, give Provider Feedback, in which case Customer gives Feedback "AS IS". Provider may use all Feedback freely without any restriction or obligation. In addition, Provider may collect and analyze Usage Data, and Provider may freely use Usage Data to maintain, improve, enhance, and promote Provider's products and services without restriction or obligation. However, Provider may only disclose Usage Data to others if the Usage Data is aggregated and does not identify Customer or Users.
    notes: "Covers Provider use of Feedback and Usage Data; includes a disclosure condition for Usage Data." 

  - ex_id: EX-002
    section_ref: "1.5"
    heading: "Customer Content"
    quote_verbatim: |-
      **1.5 Customer Content.** Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings. Customer is responsible for the accuracy and content of Customer Content.

  - ex_id: EX-003
    section_ref: "1.6"
    heading: "Machine Learning"
    quote_verbatim: |-
      **1.6 Machine Learning.** Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes. However, (a) Usage Data and Customer Content must be aggregated before it can be used for these purposes, and (b) Provider will use commercially reasonable efforts consistent with industry standard technology to de-identify Usage Data and Customer Content before such use. Nothing in this section will reduce or limit Provider's obligations regarding Personal Data that may be contained in Usage Data or Customer Content under Applicable Data Protection Laws. Due to the nature of artificial intelligence and machine learning, information generated by these features may be incorrect or inaccurate. Product features that include artificial intelligence or machine learning models are not human and are not a substitute for human oversight.

  - ex_id: EX-004
    section_ref: "2.1(a)(v)"
    heading: "Restrictions on Customer — security/vulnerability tests"
    quote_verbatim: |-
      (v) conduct security or vulnerability tests on, interfere with the operation of, cause performance degradation of, or circumvent access restrictions of the Product;

  - ex_id: EX-005
    section_ref: "2.1(b)"
    heading: "Documentation / Use Limitations"
    quote_verbatim: |-
      (b) Use of the Product must comply with all Documentation and Use Limitations.

  - ex_id: EX-006
    section_ref: "2.2"
    heading: "Suspension"
    quote_verbatim: |-
      **2.2 Suspension.** If Customer (a) has an outstanding, undisputed balance on its account for more than 30 days; (b) breaches Section 2.1 (Restrictions on Customer); or (c) uses the Product in violation of the Agreement or in a way that materially and negatively impacts the Product or others, then Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical. Provider will reinstate Customer's access to the Product only if Customer resolves the underlying issue.

  - ex_id: EX-007
    section_ref: "3.1"
    heading: "Personal Data / DPA"
    quote_verbatim: |-
      **3.1 Personal Data.** Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider. If the parties have a DPA, each party will comply with its obligations in the DPA, the terms of the DPA will control each party's rights and obligations as to Personal Data, and the terms of the DPA will control in the event of any conflict with this Agreement.

  - ex_id: EX-008
    section_ref: "3.2"
    heading: "Prohibited Data"
    quote_verbatim: |-
      **3.2 Prohibited Data.** Customer will not (and will not allow anyone else to) submit Prohibited Data to the Product unless authorized by the Order Form or Key Terms.

  - ex_id: EX-009
    section_ref: "4.1"
    heading: "Fees non-refundable"
    quote_verbatim: |-
      **4.1 Fees.** Unless the Order Form specifies a different currency, all Fees are in U.S. Dollars and are exclusive of taxes. Except for the prorated refund of prepaid Fees allowed with specific termination rights given in the Agreement, Fees are non-refundable.

  - ex_id: EX-010
    section_ref: "5.1"
    heading: "Auto-renewal / non-renewal notice"
    quote_verbatim: |-
      **5.1 Order Form and Agreement.** For each Order Form, the Agreement will start on the Order Date, continue through the Subscription Period, and automatically renew for additional Subscription Periods unless one party gives notice of non-renewal to the other party before the Non-Renewal Notice Date.

  - ex_id: EX-011
    section_ref: "5.5(b)"
    heading: "Deletion of Customer Content"
    quote_verbatim: |-
      (b) Upon Customer's request, Provider will delete Customer Content within 60 days.

  - ex_id: EX-012
    section_ref: "5.6(b)"
    heading: "Retention in backups/record retention"
    quote_verbatim: |-
      (b) Each Recipient may retain Discloser's Confidential Information in accordance with its standard backup or record retention policies maintained in the ordinary course of business or as required by Applicable Laws, in which case Section 3 (Privacy & Security) and Section 10 (Confidentiality) will continue to apply to retained Confidential Information.

  - ex_id: EX-013
    section_ref: "5.6(a)"
    heading: "Survival (incl. ML and usage rights)"
    quote_verbatim: |-
      **5.6 Survival.** (a) The following sections will survive expiration or termination of the Agreement: Section 1.4 (Feedback and Usage Data), Section 1.6 (Machine Learning), Section 2.1 (Restrictions on Customer), Section 4 (Payment & Taxes) for Fees accrued or payable before expiration or termination, Section 5.5 (Effect of Termination), Section 5.6 (Survival), Section 6 (Representations & Warranties), Section 7 (Disclaimer of Warranties), Section 8 (Limitation of Liability), Section 9 (Indemnification), Section 10 (Confidentiality), Section 11 (Reservation of Rights), Section 12 (General Terms), Section 13 (Definitions), and the portions of a Cover Page referenced by these sections.

  - ex_id: EX-014
    section_ref: "6.3"
    heading: "Provider warranty"
    quote_verbatim: |-
      **6.3 From Provider.** Provider represents and warrants to Customer that it will not materially reduce the general functionality of the Cloud Service during the Subscription Period.

  - ex_id: EX-015
    section_ref: "7.1"
    heading: "Disclaimer of warranties"
    quote_verbatim: |-
      **7.1** Provider makes no guarantees that the Product will always be safe, secure, or error-free, or that it will function without disruptions, delays, or imperfections. Except for the warranties in Section 6, Provider and Customer each disclaim all other warranties and conditions, whether express or implied, including merchantability, fitness for a particular purpose, title, and non-infringement.

  - ex_id: EX-016
    section_ref: "8.1"
    heading: "Liability caps (variables)"
    quote_verbatim: |-
      **8.1 Liability Caps.** (a) Each party's total cumulative liability for all claims will not be more than the General Cap Amount. (b) If there are Increased Claims, each party's total cumulative liability for Increased Claims will not be more than the Increased Cap Amount.

  - ex_id: EX-017
    section_ref: "8.2"
    heading: "Damages waiver"
    quote_verbatim: |-
      **8.2 Damages Waiver.** Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility.

  - ex_id: EX-018
    section_ref: "8.4"
    heading: "Liability exceptions (defined-term dependent)"
    quote_verbatim: |-
      **8.4 Exceptions.** The liability cap in 8.1(a) does not apply to Increased Claims. Section 8.1 does not apply to Unlimited Claims. Section 8.2 does not apply to Increased Claims or breach of Section 10 (Confidentiality).

  - ex_id: EX-019
    section_ref: "9.1"
    heading: "Provider indemnity"
    quote_verbatim: |-
      **9.1 Protection by Provider.** Provider will indemnify, defend, and hold harmless Customer from Provider Covered Claims and all resulting damages, costs, and expenses including reasonable attorneys' fees.

  - ex_id: EX-020
    section_ref: "9.6"
    heading: "Exclusive remedy for covered claims"
    quote_verbatim: |-
      **9.6 Exclusive Remedy.** Section 9, together with termination rights, describes exclusive remedies for Covered Claims.

  - ex_id: EX-021
    section_ref: "10.1"
    heading: "Confidentiality (baseline obligation)"
    quote_verbatim: |-
      **10.1 Non-Use and Non-Disclosure.** Recipient will not use or disclose Discloser's Confidential Information except as authorized or needed under the Agreement.

  - ex_id: EX-022
    section_ref: "11.1"
    heading: "Reservation of rights"
    quote_verbatim: |-
      **11.1** Provider retains all rights in the Product. Customer retains all rights in Customer Content, subject to Sections 1.5 and 1.6.

  - ex_id: EX-023
    section_ref: "12.1"
    heading: "Entire agreement / rejection of PO terms"
    quote_verbatim: |-
      **12.1 Entire Agreement.** This Agreement supersedes all prior statements. Provider rejects terms in Customer's purchase orders.

  - ex_id: EX-024
    section_ref: "12.2"
    heading: "Modifications in signed writing"
    quote_verbatim: |-
      **12.2 Modifications.** Changes require writing signed by each party.

  - ex_id: EX-025
    section_ref: "12.3"
    heading: "Governing law / forum (variables)"
    quote_verbatim: |-
      **12.3 Governing Law.** The Governing Law applies without regard to conflict of laws. Chosen Courts have exclusive jurisdiction.

  - ex_id: EX-026
    section_ref: "12.6"
    heading: "Assignment"
    quote_verbatim: |-
      **12.6 Assignment.** No assignment without consent, except in merger/acquisition/change of control.

  - ex_id: EX-027
    section_ref: "12.8"
    heading: "Logo rights"
    quote_verbatim: |-
      **12.8 Logo Rights.** Provider may use Customer's name and logo in marketing.

  - ex_id: EX-028
    section_ref: "12.9"
    heading: "Notices"
    quote_verbatim: |-
      **12.9 Notices.** Written notices to the Notice Address. Deemed given on confirmed delivery or two days after mailing.

  - ex_id: EX-029
    section_ref: "13.1"
    heading: "Variables on Cover Page"
    quote_verbatim: |-
      **13.1** Variables have meanings given on the Cover Page; undefined variables mean "none" or "not applicable."

candidate_issues:
  - issue_id: I-001
    title: "Provider use of Feedback and Usage Data"
    description: "The agreement permits Provider to use Feedback without restriction, and to collect/analyze and freely use Usage Data for product maintenance, improvement, enhancement, and promotion, with a limitation that disclosures to others must be aggregated and not identify Customer or Users."
    why_it_matters: "Usage Data programs can implicate confidentiality expectations, privacy expectations, and internal data-governance requirements. The scope of what counts as Usage Data and what 'aggregated' means can affect whether Customer data signals or metadata may be used outside delivering the service."
    evidence_refs: [EX-001]
    missing_info_questions:
      - "How is 'Usage Data' defined on the Cover Page/Key Terms?"
      - "Is there any opt-out, limits on use for marketing/promotion, or limits on retention?"
      - "Does Usage Data include content-derived signals or only telemetry/metrics?"

  - issue_id: I-002
    title: "Machine learning training using Usage Data and Customer Content"
    description: "The agreement authorizes Provider to use aggregated Usage Data and Customer Content to develop, train, or enhance AI/ML models (including third-party components), with de-identification using commercially reasonable efforts and an aggregation requirement before such use."
    why_it_matters: "Customers may have policy or regulatory constraints on using their content to train models, especially where third-party components are involved. Definitions of aggregation/de-identification and the operational implementation can affect confidentiality and IP expectations and may affect whether customer data can be reconstructed or used to generate outputs resembling Customer Content."
    evidence_refs: [EX-003]
    missing_info_questions:
      - "Is there an opt-out from ML/model training for Customer Content and/or Usage Data?"
      - "What does 'aggregated' mean operationally for Customer Content?"
      - "Which third-party AI/ML components are used, and where are they hosted/processed?"
      - "What retention periods apply to data used for training?"

  - issue_id: I-003
    title: "Scope of Provider rights to copy/display/modify Customer Content"
    description: "Provider may copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings."
    why_it_matters: "Customer may want clarity on what modifications are made (format conversions, indexing, backups), what derivative/processed forms are created, and how those are treated on termination and deletion."
    evidence_refs: [EX-002]
    missing_info_questions:
      - "Does 'related offerings' include analytics, support tooling, or subcontractor services?"
      - "Are derived data/embeddings/indexes treated as Customer Content, Usage Data, or something else?"

  - issue_id: I-004
    title: "Restriction on customer security or vulnerability testing"
    description: "Customer is restricted from conducting security or vulnerability tests on the Product, among other prohibited activities."
    why_it_matters: "Customers often have security programs requiring penetration testing, vulnerability scanning, or third-party assessments. A blanket restriction can create operational friction and may conflict with security compliance obligations."
    evidence_refs: [EX-004]
    missing_info_questions:
      - "Does Provider offer a permitted process for security testing (e.g., pre-approval, scopes, windows)?"
      - "Does the Order Form/Documentation provide any exceptions for agreed testing?"

  - issue_id: I-005
    title: "Compliance with Documentation and Use Limitations"
    description: "Use of the Product must comply with all Documentation and Use Limitations (not provided in the text)."
    why_it_matters: "Incorporation of external documents can introduce obligations or restrictions that are not visible in the main agreement text, affecting permitted use, compliance requirements, and operational feasibility."
    evidence_refs: [EX-005]
    missing_info_questions:
      - "What are the current Documentation and Use Limitations documents, and are they version-locked at signature?"
      - "Can Provider change Documentation/Use Limitations unilaterally during the term?"

  - issue_id: I-006
    title: "Suspension rights include 'with or without notice'"
    description: "Provider may temporarily suspend access with or without notice for certain triggers including payment delinquency over 30 days, breach of restrictions, or usage that materially and negatively impacts the Product or others."
    why_it_matters: "Suspension provisions can affect business continuity. Notice, cure process, and scope of suspension (full vs partial) can be important operationally for internal operations that rely on the service."
    evidence_refs: [EX-006]
    missing_info_questions:
      - "Are there cure periods or escalation steps before suspension (other than 'try to inform when practical')?"
      - "Can Customer obtain temporary read-only access or data export during suspension?"

  - issue_id: I-007
    title: "GDPR personal data requires a DPA; DPA controls conflicts"
    description: "Before submitting GDPR-governed Personal Data, Customer must enter into a DPA; if present, the DPA controls each party's rights/obligations for Personal Data and controls in the event of conflict with the Agreement."
    why_it_matters: "Key security, processing, subprocessor, transfer, and breach-notification terms are typically in the DPA. Without the DPA text, it is unclear what commitments apply and whether they align with Customer requirements."
    evidence_refs: [EX-007]
    missing_info_questions:
      - "Provide the DPA (including SCCs if applicable) and list of subprocessors."
      - "Is the DPA mandatory regardless of whether Customer intends to process GDPR personal data?"

  - issue_id: I-008
    title: "Prohibited Data limitations depend on Order Form / Key Terms"
    description: "Customer may not submit Prohibited Data unless authorized by the Order Form or Key Terms; those materials are not included in the text provided."
    why_it_matters: "Restrictions on data types can limit intended use cases (e.g., regulated or sensitive data). If Customer's workflows involve any restricted data, this clause may require changes in business processes or product configuration."
    evidence_refs: [EX-008]
    missing_info_questions:
      - "How is 'Prohibited Data' defined, and does it include Personal Data, PCI, PHI, or other regulated data?"
      - "Do the Order Form/Key Terms authorize any otherwise-prohibited categories?"

  - issue_id: I-009
    title: "Fees are non-refundable except limited prorated refunds"
    description: "Fees are stated to be non-refundable except for prorated refunds of prepaid fees allowed with specific termination rights in the Agreement."
    why_it_matters: "Refund structure impacts commercial flexibility if Customer terminates early, experiences service issues, or has changes in business needs. The operative termination rights and refund mechanics depend on other referenced terms."
    evidence_refs: [EX-009]
    missing_info_questions:
      - "Which termination rights in the Agreement or Order Form permit prorated refunds (beyond those explicitly stated)?"
      - "Are any service credits, SLA credits, or additional refunds specified in the Order Form?"

  - issue_id: I-010
    title: "Auto-renewal depends on Non-Renewal Notice Date"
    description: "The agreement renews automatically unless a party gives notice of non-renewal before the Non-Renewal Notice Date (not provided)."
    why_it_matters: "Renewal timing can affect procurement planning and budgeting. If the notice window is short or unclear, Customer may miss the opportunity to avoid renewal."
    evidence_refs: [EX-010]
    missing_info_questions:
      - "What is the Non-Renewal Notice Date / notice period in the Order Form/Cover Page?"
      - "What are the renewal term lengths and any renewal price adjustments?"

  - issue_id: I-011
    title: "Deletion of Customer Content is on-request and within 60 days"
    description: "Upon Customer request, Provider will delete Customer Content within 60 days after expiration or termination."
    why_it_matters: "Customers may need clearer offboarding obligations (timelines, scope of deletion, confirmation, and exclusions for backups). Deletion scope interacts with any permitted retention and with Customer's compliance requirements."
    evidence_refs: [EX-011, EX-012]
    missing_info_questions:
      - "What deletion method and confirmation is provided, and what is excluded (e.g., backups, logs, derived data)?"
      - "Is there a data export window/process prior to deletion?"

  - issue_id: I-012
    title: "Provider warranty is limited to no material reduction of general functionality"
    description: "Provider warrants only that it will not materially reduce the general functionality of the Cloud Service during the Subscription Period; remedies and other warranties are limited/waived elsewhere."
    why_it_matters: "Customers often look for commitments on uptime, performance, security controls, and support response times. A narrow functionality warranty may leave those topics dependent on the Order Form, SLA, or other referenced materials."
    evidence_refs: [EX-014, EX-015]
    missing_info_questions:
      - "Is there an SLA, security addendum, or support SLA in the Order Form?"
      - "Are there any explicit security commitments outside the DPA?"

  - issue_id: I-013
    title: "Liability caps and exceptions are driven by variables and defined terms"
    description: "Total cumulative liability is capped by the General Cap Amount (and Increased Cap Amount for Increased Claims). Exceptions reference Increased Claims and Unlimited Claims; damages waiver is broadly stated with certain exceptions."
    why_it_matters: "Customer's potential recovery for outages, data incidents, or other claims may be limited depending on cap amounts and how Increased/Unlimited Claims are defined. Without the Cover Page/Key Terms, the practical allocation is unclear."
    evidence_refs: [EX-016, EX-017, EX-018, EX-029]
    missing_info_questions:
      - "What are the General Cap Amount and Increased Cap Amount on the Cover Page?"
      - "How are 'Increased Claims' and 'Unlimited Claims' defined, and do they include data protection/security events?"

  - issue_id: I-014
    title: "Indemnity scope depends on definition of Covered Claims; exclusive remedy"
    description: "Provider will indemnify Customer for Provider Covered Claims, and Section 9 (with termination rights) is described as the exclusive remedy for Covered Claims."
    why_it_matters: "Customers often rely on provider indemnity for IP infringement and certain third-party claims. The scope, exclusions, and whether other remedies are limited depend on how Covered Claims are defined and any related Key Terms."
    evidence_refs: [EX-019, EX-020]
    missing_info_questions:
      - "Provide definitions of Provider Covered Claims / Covered Claim, and confirm whether IP infringement is included."
      - "Are there caps, carve-outs, or special procedures in the Cover Page/Key Terms for indemnity claims?"

  - issue_id: I-015
    title: "Provider may use Customer name and logo in marketing"
    description: "Provider may use Customer's name and logo in marketing."
    why_it_matters: "Customer may require prior written consent, brand guidelines compliance, or limitations on public announcements, especially for mid-market procurement and confidentiality expectations."
    evidence_refs: [EX-027]
    missing_info_questions:
      - "Is customer approval required for each use, and can Customer opt out?"

  - issue_id: I-016
    title: "Entire agreement clause rejects customer purchase order terms"
    description: "The agreement states it supersedes prior statements and that Provider rejects terms in Customer's purchase orders."
    why_it_matters: "If Customer procurement relies on PO terms (e.g., security, data handling, audit rights), this clause indicates those terms will not apply, and needed protections must be included in the Agreement/Order Form/DPA."
    evidence_refs: [EX-023]
    missing_info_questions:
      - "Are any Customer standard procurement terms incorporated elsewhere (Order Form, Key Terms, addenda)?"

  - issue_id: I-017
    title: "Governing law and exclusive jurisdiction depend on variables"
    description: "The contract provides that the Governing Law applies and that Chosen Courts have exclusive jurisdiction, without specifying the jurisdiction in the text provided."
    why_it_matters: "Forum and governing law can affect dispute resolution costs, enforceability, and internal policy requirements, and may be material to procurement approval workflows."
    evidence_refs: [EX-025, EX-029]
    missing_info_questions:
      - "What are the Governing Law and Chosen Courts selections on the Cover Page/Order Form?"

  - issue_id: I-018
    title: "Assignment permitted in change of control"
    description: "Assignment is prohibited without consent except in merger/acquisition/change of control."
    why_it_matters: "If Provider can assign in a transaction, Customer may want to understand continuity of obligations, especially where data protection and confidentiality are priorities."
    evidence_refs: [EX-026]
    missing_info_questions:
      - "Does Customer receive notice of assignment/change of control, and are there termination rights tied to assignment?"

  - issue_id: I-019
    title: "Notices depend on Notice Address and delivery mechanics"
    description: "Notices must be written and sent to the Notice Address; deemed given on confirmed delivery or two days after mailing."
    why_it_matters: "Operationally, correct notice addresses and delivery methods matter for renewal, termination, and dispute notices. Missing or incorrect notice details can create administrative risk."
    evidence_refs: [EX-028]
    missing_info_questions:
      - "What are the parties' Notice Addresses on the Cover Page/Order Form?"
      - "Are email notices permitted (and if so, where specified)?"
