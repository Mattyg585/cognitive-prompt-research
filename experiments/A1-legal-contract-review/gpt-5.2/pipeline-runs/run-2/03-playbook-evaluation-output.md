---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: pipeline
run: 2
stage: 03-playbook-evaluation
---

## Artifact C — Evaluated findings (no drafting)

| Issue ID | Title | Severity | Negotiation priority | Playbook position source | Deviation summary | Business impact | Escalation trigger (yes/no + why) | Evidence refs (EX-…) | Open questions |
|---|---|---|---|---|---|---|---|---|---|
| I-001 | AI/ML training use of Usage Data and Customer Content (including third-party components) | RED | Must-have | GENERIC | Allows provider (and third-party components) to use aggregated/de-identified Usage Data + Customer Content to develop/train/enhance AI/ML; de-identification is “commercially reasonable efforts” and aggregation standard is unspecified. | Potential loss of control over sensitive business info, heightened privacy/compliance review, reputational risk, and harder internal approvals for using the service. | yes — use of Customer Content for model training (incl. third parties) is a high-sensitivity data governance issue requiring privacy/security approval. | EX-005, EX-006, EX-007 | What qualifies as “aggregated”, and is it done before any third-party processing?; What measures/standard are used to de-identify, and how is effectiveness assessed?; Is there an opt-out/setting to disable training on our data? |
| I-002 | Usage Data broad use rights; disclosure limited by aggregation/non-identification | YELLOW | Should-have | GENERIC | Provider may “freely use” Usage Data without restriction/obligation; external disclosure is limited to aggregated/non-identifying, but thresholds/controls are not specified. | Competitive/operational sensitivity (telemetry can reveal usage patterns); privacy risk depends on how Usage Data is defined and anonymized. | no — typically negotiable, but depends on sensitivity and definition/controls. | EX-002, EX-003 | How is “Usage Data” defined (does it include content-derived signals)?; What is the aggregation threshold and how is non-identification assessed? |
| I-003 | GDPR Personal Data requires a DPA; DPA controls in conflicts | YELLOW | Must-have | GENERIC | If GDPR personal data will be submitted, a DPA is a prerequisite; DPA controls in conflicts, so actual obligations/rights are outside the provided contract text. | Go-live blocker if personal data processing is required; material privacy/security terms may differ from expectations until DPA is reviewed and executed. | yes — any intended processing of GDPR personal data requires DPA review/signature before deployment. | EX-008 | Is a DPA template available and does it include transfer mechanisms (e.g., SCCs) if needed?; Are there subprocessors and how are updates/notices handled? |
| I-004 | Prohibited Data restriction depends on Order Form or Key Terms (not provided) | YELLOW | Must-have | GENERIC | Whether certain regulated/sensitive data can be used is outsourced to documents not provided (Order Form/Key Terms). | Could block intended use cases or create compliance gaps if teams assume data types are permitted when they are not. | yes — if any regulated/sensitive data use is in scope, compliance sign-off is needed once “Prohibited Data” is defined. | EX-009 | How is “Prohibited Data” defined (does it include payment/health/etc.)?; Do Order Form/Key Terms authorize any prohibited categories and under what safeguards? |
| I-005 | Incorporation of Documentation and Use Limitations (not provided) | YELLOW | Should-have | GENERIC | Contract incorporates external Documentation/Use Limitations that were not provided; operational obligations may be changeable outside the agreement text. | Ongoing compliance burden and potential scope creep; deployment constraints may change or be discovered late. | no — usually resolvable by obtaining/locking referenced docs and change controls. | EX-011 | Where are Documentation/Use Limitations located and are they versioned/locked for the term?; Can Provider change them unilaterally and what notice applies? |
| I-006 | Suspension rights “with or without notice” | YELLOW | Should-have | GENERIC | Provider may suspend access with or without notice for several triggers; only a best-efforts “when practical” notice qualifier is offered. | Business continuity and incident response uncertainty; risk of service interruption impacting operations. | no — escalate if the service is operationally critical or triggers are broad/ambiguous in practice. | EX-012 | Are there cure/escalation steps before suspension (beyond “when practical” notice)?; Is there an SLA/credits scheme in the Order Form for downtime not related to suspension? |
| I-007 | Restriction on security or vulnerability testing | YELLOW | Should-have | GENERIC | Prohibits customer security/vulnerability testing; may conflict with internal security assurance requirements. | Could prevent standard security due diligence/monitoring, delaying approvals or forcing reliance on vendor attestations. | no — common position, but needs a defined approved testing path or alternative assurances. | EX-010 | Is there an authorized testing process (written permission, scoped testing) outside this clause?; Are SOC 2/ISO reports available as substitutes? |
| I-008 | Customer Content deletion is upon request and within 60 days | YELLOW | Should-have | GENERIC | Deletion is not automatic; it occurs upon request and within 60 days, leaving operational detail (backups/logs) unspecified. | Offboarding burden on customer; potential retention beyond internal policy expectations; audit/records management complications. | no — negotiate based on data sensitivity and retention requirements. | EX-014 | Is deletion automatic absent a request, and what about backups/logs?; Is there a data export mechanism and timing before deletion? |
| I-009 | Liability caps and key commercial variables not provided | RED | Must-have | GENERIC | Cap amount and key carveout definitions are missing (Variables live on Cover Page); cannot assess real risk allocation or recovery economics. | Signing without cap values/categorization risks unacceptable exposure and inadequate remedies; procurement cannot price/approve risk. | yes — liability caps/carveouts are core risk terms; requires legal/procurement escalation before approval. | EX-015, EX-017, EX-020 | What are General Cap Amount / Increased cap parameters on the Cover Page?; How are “Increased Claims” and “Unlimited Claims” defined? |
| I-010 | Consequential and other damages waiver | GREEN | Nice-to-have | GENERIC | Mutual waiver of consequential/special/etc. damages appears standard; impact depends on any carveouts tied to specific claim types elsewhere. | Limits recoverability for downstream business losses; generally market-standard for SaaS if balanced with appropriate carveouts/caps. | no — review interaction with confidentiality/security carveouts once cap definitions are known. | EX-016 | Do any cap exceptions meaningfully change the impact of this waiver in likely claim scenarios (e.g., confidentiality / data incidents)? |
| I-011 | Indemnity scope depends on defined “Covered Claims” and exclusive remedy provision | RED | Must-have | GENERIC | Indemnities and “exclusive remedy” hinge on missing definitions of Covered Claims; could narrow protections and foreclose other remedies for those claim categories. | Risk of insufficient IP/legal protection; exclusive remedy could constrain recovery paths if claim falls within narrow “Covered Claims” definition. | yes — indemnity scope/exclusive remedy materially affect risk transfer; requires legal escalation once definitions are available. | EX-018, EX-019, EX-022 | How are Provider Covered Claims / Customer Covered Claims defined (IP infringement? data/regulatory?)?; Are there caps or procedural conditions in Cover Page/Order Form? |
| I-012 | Provider marketing use of Customer name and logo | YELLOW | Should-have | GENERIC | Grants marketing rights without clear approval/revocation mechanics in provided text. | Brand/comms risk; may violate internal comms/PR policy or create unwanted publicity. | no — route to brand/comms owner; usually fixable with approval requirement. | EX-021 | Is customer approval required for specific uses and can consent be revoked?; Are brand guidelines/limitations referenced in Key Terms? |
| I-013 | Governing law and forum are variables not shown | YELLOW | Should-have | GENERIC | Governing law/venue are unspecified in the provided text (variables on Cover Page); acceptability is unknown. | Dispute cost/complexity and enforcement risk if forum is unfavorable. | no — escalate if selected jurisdiction deviates from company standard or creates regulatory/compliance friction. | EX-024, EX-020 | What are the selected Governing Law and Chosen Courts on the Cover Page/Key Terms? |
| I-014 | Entire agreement + rejection of Customer purchase order terms | YELLOW | Should-have | GENERIC | Rejects customer PO terms; if procurement relies on PO for operational/legal terms, those will not apply unless negotiated into Order Form/Key Terms. | Procurement process friction; risk that internal policy terms aren’t incorporated into the deal. | no — coordinate with procurement on required terms and incorporate them into the contract package. | EX-023 | Does Customer intend to rely on any PO terms; if so, should they be incorporated into the Order Form or Key Terms instead? |

```yaml
findings:
  - issue_id: I-001
    title: "AI/ML training use of Usage Data and Customer Content (including third-party components)"
    severity: RED
    negotiation_priority: Must-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Permits provider (incl. third-party components) to use aggregated/de-identified Usage Data + Customer Content for AI/ML training; aggregation/de-identification standards and opt-out controls are unspecified."
    business_impact: "High-sensitivity data governance and privacy/compliance risk; may block internal approvals and create reputational exposure."
    escalation_trigger:
      triggered: true
      reason: "Customer Content authorized for AI/ML training (including third-party components) creates material governance/privacy risk."
    evidence_refs: [EX-005, EX-006, EX-007]
    open_questions:
      - "What qualifies as 'aggregated' for these purposes, and is aggregation performed before any third-party processing?"
      - "What technical and organizational measures are used to de-identify, and is there any standard or testing method referenced?"
      - "Do any product settings allow Customer to disable AI/ML training on its data?"

  - issue_id: I-002
    title: "Usage Data broad use rights; disclosure limited by aggregation/non-identification"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Provider may freely use Usage Data without restriction/obligation; disclosure limitation relies on undefined aggregation/non-identification controls."
    business_impact: "Potential privacy and competitive sensitivity depending on Usage Data definition and anonymization practices."
    escalation_trigger:
      triggered: false
      reason: "Typically negotiable; escalation depends on sensitivity of telemetry and internal privacy posture."
    evidence_refs: [EX-002, EX-003]
    open_questions:
      - "How is 'Usage Data' defined (scope, fields, and whether it includes content-derived signals)?"
      - "What is the aggregation threshold and how is non-identification assessed?"

  - issue_id: I-003
    title: "GDPR Personal Data requires a DPA; DPA controls in conflicts"
    severity: YELLOW
    negotiation_priority: Must-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "DPA is required before submitting GDPR Personal Data; DPA controls rights/obligations and conflicts, but DPA text is not provided."
    business_impact: "Potential go-live blocker; material privacy/security obligations remain unknown until DPA is reviewed and executed."
    escalation_trigger:
      triggered: true
      reason: "Any GDPR Personal Data processing requires DPA review/signature before deployment."
    evidence_refs: [EX-008]
    open_questions:
      - "Is a DPA template available and does it include cross-border transfer terms (e.g., SCCs) if needed?"
      - "Does the service involve sub-processors and, if so, where are they listed and how are changes notified?"

  - issue_id: I-004
    title: "Prohibited Data restriction depends on Order Form or Key Terms (not provided)"
    severity: YELLOW
    negotiation_priority: Must-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Permitted/forbidden data categories depend on external documents not provided (Order Form/Key Terms)."
    business_impact: "May block intended use cases or create compliance gaps if prohibited/regulated data is in scope."
    escalation_trigger:
      triggered: true
      reason: "If regulated/sensitive data is planned, compliance approval depends on the missing definition/authorization."
    evidence_refs: [EX-009]
    open_questions:
      - "How is 'Prohibited Data' defined, and does it include regulated data types relevant to Customer (e.g., payment/health data)?"
      - "Do the Order Form or Key Terms authorize any Prohibited Data categories, and under what safeguards?"

  - issue_id: I-005
    title: "Incorporation of Documentation and Use Limitations (not provided)"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Contract incorporates Documentation/Use Limitations that are not provided; change control/version lock is unknown."
    business_impact: "Operational compliance burden and potential shifting obligations affecting deployment and approvals."
    escalation_trigger:
      triggered: false
      reason: "Usually addressed by obtaining referenced docs and negotiating versioning/change notice."
    evidence_refs: [EX-011]
    open_questions:
      - "Where are the Documentation and Use Limitations located, and are they versioned/locked for the subscription term?"
      - "Can Provider change Documentation/Use Limitations unilaterally, and if so, what notice applies?"

  - issue_id: I-006
    title: "Suspension rights 'with or without notice'"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Provider may suspend access with or without notice; only a practical/when-possible notice qualifier is offered."
    business_impact: "Reduced operational predictability and higher interruption risk; impacts business continuity planning."
    escalation_trigger:
      triggered: false
      reason: "Escalate if service is critical or if suspension triggers are broad in practice."
    evidence_refs: [EX-012]
    open_questions:
      - "Are there any cure or escalation steps before suspension (other than the 'when practical' notice)?"
      - "Is there an SLA/credit scheme in the Order Form that addresses downtime unrelated to suspension?"

  - issue_id: I-007
    title: "Restriction on security or vulnerability testing"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Prohibits customer security/vulnerability testing; may conflict with internal security assurance requirements."
    business_impact: "Could delay security approval or force reliance on vendor attestations instead of internal testing."
    escalation_trigger:
      triggered: false
      reason: "Common SaaS position; seek approved testing pathway or substitute assurances (SOC 2/ISO)."
    evidence_refs: [EX-010]
    open_questions:
      - "Is there an authorized testing process (e.g., written permission, scope limits) outside this clause?"
      - "Are third-party security assessments (SOC 2/ISO) available as substitutes?"

  - issue_id: I-008
    title: "Customer Content deletion is upon request and within 60 days"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Deletion occurs upon customer request and within 60 days; treatment of backups/logs and default deletion behavior is unspecified."
    business_impact: "Retention may exceed policy expectations; customer must operationalize offboarding deletion requests and audit trail."
    escalation_trigger:
      triggered: false
      reason: "Escalate if data sensitivity/retention obligations require tighter deletion commitments."
    evidence_refs: [EX-014]
    open_questions:
      - "Does Provider delete Customer Content automatically absent a request, and what happens to backups/logs?"
      - "Is there a data export mechanism and time window before deletion?"

  - issue_id: I-009
    title: "Liability caps and key commercial variables not provided"
    severity: RED
    negotiation_priority: Must-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Key cap amounts and carveout categories are undefined in the provided text (Variables are on the Cover Page), preventing assessment of practical exposure and remedies."
    business_impact: "Core risk allocation is unknown; could result in unacceptable exposure or inadequate recovery economics."
    escalation_trigger:
      triggered: true
      reason: "Liability caps/carveouts are fundamental approval terms and require legal/procurement escalation."
    evidence_refs: [EX-015, EX-017, EX-020]
    open_questions:
      - "What are the General Cap Amount and any Increased/Unlimited claim parameters on the Cover Page?"
      - "How are 'Increased Claims' and 'Unlimited Claims' defined in the Cover Page/Key Terms?"

  - issue_id: I-010
    title: "Consequential and other damages waiver"
    severity: GREEN
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Mutual waiver of consequential/special/etc. damages is market-standard; practical impact depends on how carveouts/cap exceptions are defined elsewhere."
    business_impact: "Limits recovery for downstream losses; generally acceptable if caps and carveouts align with risk profile."
    escalation_trigger:
      triggered: false
      reason: "Re-evaluate once liability cap carveouts/definitions are known."
    evidence_refs: [EX-016]
    open_questions:
      - "Do the cap exceptions (e.g., for confidentiality breaches) meaningfully change the impact of this waiver in likely claim scenarios?"

  - issue_id: I-011
    title: "Indemnity scope depends on defined 'Covered Claims' and exclusive remedy provision"
    severity: RED
    negotiation_priority: Must-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Indemnity scope and the exclusive-remedy limitation hinge on missing 'Covered Claims' definitions and any related conditions/caps."
    business_impact: "Could leave customer under-protected for key risks (e.g., IP), and exclusive remedy could limit recovery routes."
    escalation_trigger:
      triggered: true
      reason: "Indemnity/exclusive remedy materially affect risk transfer and require legal evaluation once definitions are available."
    evidence_refs: [EX-018, EX-019, EX-022]
    open_questions:
      - "How are Provider Covered Claims and Customer Covered Claims defined, and do they include IP infringement, data-related claims, or regulatory claims?"
      - "Are there monetary caps or process conditions tied to indemnification in the Cover Page/Order Form?"

  - issue_id: I-012
    title: "Provider marketing use of Customer name and logo"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Marketing right granted without explicit approval/revocation mechanics in provided text."
    business_impact: "Brand/comms risk and internal approval burden; potential for undesired publicity."
    escalation_trigger:
      triggered: false
      reason: "Typically resolved by requiring written approval and allowing revocation."
    evidence_refs: [EX-021]
    open_questions:
      - "Is Customer approval required for specific uses, and can Customer revoke consent?"
      - "Are there brand guidelines or limitations referenced elsewhere (e.g., Key Terms)?"

  - issue_id: I-013
    title: "Governing law and forum are variables not shown"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Governing law/venue are defined as variables on the Cover Page and are not included in the provided text."
    business_impact: "Could increase dispute cost/complexity if forum is unfavorable or inconsistent with company standards."
    escalation_trigger:
      triggered: false
      reason: "Escalate only if selected jurisdiction materially deviates from standard or introduces regulatory constraints."
    evidence_refs: [EX-024, EX-020]
    open_questions:
      - "What are the selected Governing Law and Chosen Courts on the Cover Page/Key Terms?"

  - issue_id: I-014
    title: "Entire agreement + rejection of Customer purchase order terms"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Rejects customer PO terms; any required procurement/legal terms must be incorporated into the contract package instead."
    business_impact: "Procurement workflow friction and risk that internal policy terms are not incorporated unless negotiated explicitly."
    escalation_trigger:
      triggered: false
      reason: "Coordinate with procurement to identify required terms and ensure they are included in Order Form/Key Terms."
    evidence_refs: [EX-023]
    open_questions:
      - "Does Customer intend to rely on any PO terms; if so, should they be incorporated into the Order Form or Key Terms instead?"
```
