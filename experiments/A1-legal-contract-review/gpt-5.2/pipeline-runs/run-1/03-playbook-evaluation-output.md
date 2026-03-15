---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: pipeline
run: 1
stage: 03-playbook-evaluation
---

| Issue ID | Title | Severity | Negotiation priority | Playbook position source | Deviation summary | Business impact | Escalation trigger (yes/no + why) | Evidence refs (EX-…) | Open questions |
|---|---|---|---|---|---|---|---|---|---|
| I-001 | Provider use of Feedback and Usage Data | YELLOW | Should-have | GENERIC | Provider can use Feedback without restriction and use Usage Data broadly, with only an aggregation/non-identification condition for external disclosures. | Potential conflict with internal confidentiality/data-governance expectations; may allow product/marketing improvements derived from Customer telemetry. | No — materiality depends on how “Usage Data” and “aggregated” are defined/implemented. | EX-001 | Define “Usage Data”; confirm retention limits; confirm whether use includes marketing/promotion and whether opt-out exists. |
| I-002 | Machine learning training using Usage Data and Customer Content | RED | Escalate | GENERIC | Provider is authorized to use aggregated Usage Data and Customer Content to train/enhance AI/ML models (incl. third-party components), with de-identification efforts. | High sensitivity for IP/confidentiality and data protection; may violate Customer policy or regulatory constraints; third-party model involvement increases exposure. | Yes — many orgs prohibit training on customer content absent explicit opt-in/controls and third-party restrictions. | EX-003 | Is there an opt-out/opt-in for training? What does “aggregated” mean for Customer Content? Which third parties/subprocessors are involved and where is processing hosted? What retention applies to training datasets/derivatives? |
| I-003 | Scope of Provider rights to copy/display/modify Customer Content | YELLOW | Nice-to-have | GENERIC | Content license is limited to what’s needed to provide/maintain the Product, but “modify” and “related offerings” can be expansive without definition. | Ambiguity can affect expectations about derived data (indexes/embeddings), subcontractor access, and post-termination handling. | No — appears service-limited, but definitions/derived data treatment can change risk. | EX-002 | Clarify scope of “related offerings”; confirm treatment of derived data (e.g., embeddings/indexes/logs): Customer Content vs Usage Data; confirm subcontractor access limits. |
| I-004 | Restriction on customer security or vulnerability testing | YELLOW | Should-have | GENERIC | Blanket restriction on security/vulnerability testing absent an explicit carve-out process. | Can block required pen tests/third-party assessments; may impede compliance and security assurance. | No — typically resolvable with a pre-approval/testing process; escalates if Customer requires testing as a condition to use. | EX-004 | Is there a permitted testing process (pre-approval, scope/windows)? Any exceptions in Order Form/Documentation? |
| I-005 | Compliance with Documentation and Use Limitations | YELLOW | Should-have | GENERIC | Incorporates external “Documentation” and “Use Limitations” not provided; change-control/version-lock is unclear. | Hidden/variable obligations may restrict intended use and create compliance/operational risk during term. | No — escalates if Provider can change unilaterally or if limitations block core use cases. | EX-005 | Provide current Documentation/Use Limitations; confirm whether they are version-locked at signature; confirm change process and notice. |
| I-006 | Suspension rights include “with or without notice” | YELLOW | Should-have | GENERIC | Provider may suspend access with or without notice for payment delinquency, restrictions breach, or materially harmful use, with only “try to inform when practical.” | Business continuity risk; could disrupt operations and impede access to data/service. | No — standard in SaaS, but becomes escalation if no cure/notice for non-emergency cases or if suspension blocks data export. | EX-006 | Are there cure periods/escalation steps? Is read-only/data export available during suspension? |
| I-007 | GDPR personal data requires a DPA; DPA controls conflicts | YELLOW | Must-have | GENERIC | Agreement requires a DPA before submitting GDPR-governed Personal Data and makes DPA controlling on conflicts, but the DPA isn’t provided. | Cannot validate privacy/security, subprocessors, transfers, breach notice, and processing terms; may delay deployment. | Yes — if service will process Personal Data, execution/acceptability of DPA is a gating item. | EX-007 | Provide DPA (incl. SCCs if applicable) and subprocessors; clarify whether DPA is mandatory for any Personal Data (not just GDPR). |
| I-008 | Prohibited Data limitations depend on Order Form / Key Terms | YELLOW | Should-have | GENERIC | Prohibited Data is undefined here and may be expanded/limited via Order Form/Key Terms not provided. | May restrict intended data types (regulated/sensitive), requiring process/product changes or preventing use. | No — escalates if Prohibited Data definition blocks core workflows (e.g., Personal Data, PCI, PHI). | EX-008 | Provide definition of “Prohibited Data”; confirm any authorizations in Order Form/Key Terms for needed data categories. |
| I-009 | Fees are non-refundable except limited prorated refunds | YELLOW | Nice-to-have | GENERIC | Default is non-refundable fees with only limited prorated refunds tied to specific termination rights (not fully visible). | Limits commercial flexibility and recovery if service issues arise; may increase procurement friction. | No — common in SaaS; escalates only if Customer requires broader refund/credit protections. | EX-009 | Identify termination rights that permit prorated refunds; confirm any SLA/service credits or additional refund terms in Order Form. |
| I-010 | Auto-renewal depends on Non-Renewal Notice Date | YELLOW | Should-have | GENERIC | Auto-renew applies unless notice is given by a variable “Non-Renewal Notice Date” not provided. | Risk of unintended renewal and budget/procurement timing issues. | No — standard, but escalates if notice window is unusually early/short or unclear. | EX-010 | Confirm notice period/Non-Renewal Notice Date; confirm renewal term length and any renewal pricing mechanism. |
| I-011 | Deletion of Customer Content is on-request and within 60 days | YELLOW | Should-have | GENERIC | Deletion is triggered by Customer request and can take up to 60 days; retention in backups/record retention is permitted. | May not meet strict deletion timelines; uncertainty about scope (backups/logs/derived data) affects compliance and offboarding. | No — escalates if Customer has strict deletion obligations or if derived/training data is retained. | EX-011, EX-012 | Confirm deletion scope/exclusions (backups/logs/derived data), confirmation method, and any data export window/process. |
| I-012 | Provider warranty is limited to no material reduction of general functionality | YELLOW | Should-have | GENERIC | Narrow functionality warranty plus broad warranty disclaimers; operational assurances likely pushed to Order Form/SLA/DPA. | Reduced contractual recourse for performance/security/service quality absent SLA/support commitments. | No — common, but escalates if Customer requires SLA/support/security commitments in contract. | EX-014, EX-015 | Is there an SLA/support SLA/security addendum? Any explicit security commitments outside the DPA? |
| I-013 | Liability caps and exceptions are driven by variables and defined terms | RED | Escalate | GENERIC | Caps depend on Cover Page variables; exceptions rely on undefined “Increased Claims” and “Unlimited Claims,” and damages waiver scope interacts with confidentiality carve-outs. | Unknown recovery profile for outages, data incidents, and other claims; potential misalignment with risk tolerance and insurance expectations. | Yes — cap amounts/definitions are deal-critical and typically require legal/procurement escalation if unfavorable or unclear. | EX-016, EX-017, EX-018, EX-029 | Provide General/Increased Cap Amounts; define Increased Claims/Unlimited Claims; confirm whether security/privacy events are included in carve-outs. |
| I-014 | Indemnity scope depends on definition of Covered Claims; exclusive remedy | RED | Escalate | GENERIC | Provider indemnity exists but scope is unclear without definitions; “exclusive remedy” language may limit other remedies for Covered Claims. | If IP infringement or key third-party claim types aren’t covered, Customer may bear material litigation/defense cost risk; remedy limitation could reduce leverage. | Yes — indemnity scope and remedy limitation are typically escalation points if unclear or narrow. | EX-019, EX-020 | Provide definitions of Provider Covered Claims/Covered Claim; confirm IP infringement coverage; confirm any caps/procedures and whether exclusive remedy limits non-covered claims. |
| I-015 | Provider may use Customer name and logo in marketing | YELLOW | Nice-to-have | GENERIC | Marketing use of name/logo appears permitted without an explicit prior-consent condition. | Brand/PR control risk; may conflict with internal communications policy. | No — usually resolvable with a consent/approval requirement or opt-out. | EX-027 | Is prior written consent required for each use? Can Customer opt out and impose brand guidelines? |
| I-016 | Entire agreement clause rejects customer purchase order terms | YELLOW | Nice-to-have | GENERIC | Explicit rejection of PO terms signals procurement add-ons won’t apply unless separately incorporated. | If Customer relies on PO terms for security/data/audit, those protections must be captured elsewhere; risk of assumption mismatch. | No — escalates if procurement requires PO terms to apply and no alternative addendum is available. | EX-023 | Are any Customer procurement terms incorporated via Order Form/Key Terms/addenda? |
| I-017 | Governing law and exclusive jurisdiction depend on variables | YELLOW | Should-have | GENERIC | Governing law/forum are variable and not specified in provided text. | May violate internal legal policy or increase dispute costs depending on chosen venue. | No — escalates if chosen law/forum is unacceptable or outside approved jurisdictions. | EX-025, EX-029 | Confirm Governing Law and Chosen Courts selections on Cover Page/Order Form; confirm any venue flexibility. |
| I-018 | Assignment permitted in change of control | YELLOW | Nice-to-have | GENERIC | Assignment is restricted except for merger/acquisition/change of control; no explicit notice/termination rights shown. | Continuity risk if Provider assigns to an acquirer with different risk posture; may affect data handling expectations. | No — common; escalates if Customer requires consent/termination rights for assignment. | EX-026 | Is advance notice required? Any termination rights tied to assignment/change of control? |
| I-019 | Notices depend on Notice Address and delivery mechanics | GREEN | Nice-to-have | GENERIC | Standard written notice mechanics; key variables (Notice Addresses) are missing from provided materials. | Administrative risk if addresses are wrong; can impact renewals/termination effectiveness. | No — typically operational/clerical, not a material risk item. | EX-028 | Confirm Notice Addresses on Cover Page/Order Form; confirm whether email notices are permitted and for what types. |

```yaml
findings:
  - issue_id: I-001
    title: "Provider use of Feedback and Usage Data"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Feedback is usable without restriction; Usage Data may be used broadly, with aggregation/non-identification required only for disclosures to others."
    business_impact: "May conflict with confidentiality/data-governance expectations and enable broad internal use of telemetry for product/marketing."
    escalation_trigger:
      triggered: false
      reason: "Typically negotiable; severity depends on how 'Usage Data' and 'aggregated' are defined and operationalized."
    evidence_refs: [EX-001]
    open_questions:
      - "How is 'Usage Data' defined on the Cover Page/Key Terms?"
      - "Are there retention limits or an opt-out for marketing/promotion use?"
      - "What does 'aggregated' mean for disclosures?"

  - issue_id: I-002
    title: "Machine learning training using Usage Data and Customer Content"
    severity: RED
    negotiation_priority: Escalate
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Authorizes AI/ML training using aggregated Usage Data and Customer Content (including third-party components), subject to aggregation and de-identification efforts."
    business_impact: "High IP/confidentiality and data-protection sensitivity; may be prohibited by Customer policy; third-party involvement increases exposure."
    escalation_trigger:
      triggered: true
      reason: "Training on customer content is commonly a hard stop without explicit opt-in/strict controls and third-party limitations."
    evidence_refs: [EX-003]
    open_questions:
      - "Is there an opt-out/opt-in for model training on Customer Content and/or Usage Data?"
      - "Operational meaning of 'aggregated' for Customer Content?"
      - "Which third-party AI/ML components/subprocessors are used and where is processing hosted?"
      - "What retention and deletion controls apply to training datasets and derivatives?"

  - issue_id: I-003
    title: "Scope of Provider rights to copy/display/modify Customer Content"
    severity: YELLOW
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Service-limited content license, but 'modify' and 'related offerings' are not defined and could expand scope."
    business_impact: "Ambiguity can affect derived data handling, subcontractor access, and post-termination expectations."
    escalation_trigger:
      triggered: false
      reason: "Appears limited to service delivery; risk turns on definitions and derived-data treatment."
    evidence_refs: [EX-002]
    open_questions:
      - "Does 'related offerings' include analytics/support tooling/subcontractor services?"
      - "How are derived artifacts (indexes/embeddings/logs) classified and treated?"

  - issue_id: I-004
    title: "Restriction on customer security or vulnerability testing"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Restricts customer security/vulnerability testing without an explicit exception mechanism in the provided text."
    business_impact: "May prevent required security assessments and create compliance friction."
    escalation_trigger:
      triggered: false
      reason: "Often addressed via a permitted-testing process; escalates only if Customer requires testing as a gating condition."
    evidence_refs: [EX-004]
    open_questions:
      - "Is there a pre-approval process for pen tests/scans (scope/windows)?"
      - "Are there exceptions in the Order Form/Documentation?"

  - issue_id: I-005
    title: "Compliance with Documentation and Use Limitations"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "External Documentation/Use Limitations are incorporated but not provided; change control is unclear."
    business_impact: "Hidden or changing obligations can restrict intended use and increase compliance risk."
    escalation_trigger:
      triggered: false
      reason: "Negotiable via version-lock/change notice; escalates if unilateral changes are allowed."
    evidence_refs: [EX-005]
    open_questions:
      - "Provide current Documentation and Use Limitations."
      - "Are they version-locked at signature, and how can they be changed during term?"

  - issue_id: I-006
    title: "Suspension rights include 'with or without notice'"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Provider may suspend access with or without notice for specified triggers; notice is only 'when practical.'"
    business_impact: "Business continuity and data access risk if suspension is abrupt or broad."
    escalation_trigger:
      triggered: false
      reason: "Common clause; key is cure/notice for non-emergencies and ability to export data."
    evidence_refs: [EX-006]
    open_questions:
      - "Are there cure periods/escalation steps before suspension?"
      - "Is read-only/data export access available during suspension?"

  - issue_id: I-007
    title: "GDPR personal data requires a DPA; DPA controls conflicts"
    severity: YELLOW
    negotiation_priority: Must-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Requires a DPA before submitting GDPR-governed Personal Data and makes the DPA controlling on conflicts; DPA text not provided."
    business_impact: "Cannot validate processing, transfers, subprocessors, and breach/security commitments without the DPA; may block go-live."
    escalation_trigger:
      triggered: true
      reason: "If the service will process Personal Data, an acceptable executed DPA is a gating requirement."
    evidence_refs: [EX-007]
    open_questions:
      - "Provide the DPA (including SCCs if applicable) and subprocessor list."
      - "Is the DPA required for all Personal Data or only GDPR-governed Personal Data?"

  - issue_id: I-008
    title: "Prohibited Data limitations depend on Order Form / Key Terms"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Prohibited Data is restricted unless authorized by Order Form/Key Terms, which are not provided."
    business_impact: "May restrict key use cases involving regulated/sensitive data categories."
    escalation_trigger:
      triggered: false
      reason: "Materiality depends on how Prohibited Data is defined and whether Customer's intended data falls within it."
    evidence_refs: [EX-008]
    open_questions:
      - "Provide definition of 'Prohibited Data' in Key Terms/Cover Page."
      - "Confirm any authorizations for needed data categories."

  - issue_id: I-009
    title: "Fees are non-refundable except limited prorated refunds"
    severity: YELLOW
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Fees are non-refundable by default, with limited prorated refund tied to certain termination rights."
    business_impact: "Reduced commercial flexibility and potential procurement objections if service performance is inadequate."
    escalation_trigger:
      triggered: false
      reason: "Common SaaS position; escalates only if Customer requires broader refund/credit protections."
    evidence_refs: [EX-009]
    open_questions:
      - "Which termination rights permit prorated refunds?"
      - "Are there SLA/service credits or additional refunds in the Order Form?"

  - issue_id: I-010
    title: "Auto-renewal depends on Non-Renewal Notice Date"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Auto-renews unless notice is provided by a variable Non-Renewal Notice Date not included in provided text."
    business_impact: "Risk of inadvertent renewal and budget/procurement misalignment."
    escalation_trigger:
      triggered: false
      reason: "Typically negotiable via notice period and renewal mechanics in Order Form."
    evidence_refs: [EX-010]
    open_questions:
      - "Confirm the notice window / Non-Renewal Notice Date."
      - "Confirm renewal term length and renewal pricing adjustments, if any."

  - issue_id: I-011
    title: "Deletion of Customer Content is on-request and within 60 days"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Deletion is on Customer request and within 60 days; retention in backups/record retention is permitted."
    business_impact: "May not satisfy strict deletion/compliance needs; unclear handling of backups/logs/derived data."
    escalation_trigger:
      triggered: false
      reason: "Often acceptable with clarification and DPA alignment; escalates if strict deletion timelines or derived data retention conflicts exist."
    evidence_refs: [EX-011, EX-012]
    open_questions:
      - "Confirm deletion scope and exclusions (backups/logs/derived data) and confirmation method."
      - "Confirm data export process prior to deletion."

  - issue_id: I-012
    title: "Provider warranty is limited to no material reduction of general functionality"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Narrow functionality warranty combined with broad disclaimer; other assurances likely outside the provided text."
    business_impact: "Limits recourse for uptime/performance/security issues absent SLA/support commitments."
    escalation_trigger:
      triggered: false
      reason: "Common; mitigated by SLA/support/security commitments in Order Form/DPA."
    evidence_refs: [EX-014, EX-015]
    open_questions:
      - "Is there an SLA/support SLA or security addendum?"
      - "Are any security controls/commitments provided outside the DPA?"

  - issue_id: I-013
    title: "Liability caps and exceptions are driven by variables and defined terms"
    severity: RED
    negotiation_priority: Escalate
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Liability caps and carve-outs depend on Cover Page variables and undefined Increased/Unlimited Claims; damages waiver interplay may further limit recovery."
    business_impact: "Could materially limit Customer recovery for outages, data incidents, and other claims; deal approval may depend on cap alignment with spend/risk."
    escalation_trigger:
      triggered: true
      reason: "Cap amounts and claim definitions are deal-critical and currently unknown in the provided materials."
    evidence_refs: [EX-016, EX-017, EX-018, EX-029]
    open_questions:
      - "What are the General Cap Amount and Increased Cap Amount on the Cover Page?"
      - "Define Increased Claims and Unlimited Claims (and whether security/privacy claims are included)."

  - issue_id: I-014
    title: "Indemnity scope depends on definition of Covered Claims; exclusive remedy"
    severity: RED
    negotiation_priority: Escalate
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Indemnity exists but Covered Claims scope is undefined in provided text; exclusive-remedy language may limit remedies for those claims."
    business_impact: "If IP infringement or key third-party claims are not covered, Customer may bear significant defense/liability costs; remedy limitations reduce leverage."
    escalation_trigger:
      triggered: true
      reason: "Indemnity scope and remedy limitations are commonly escalation points when unclear or potentially narrow."
    evidence_refs: [EX-019, EX-020]
    open_questions:
      - "Provide definitions of Provider Covered Claims / Covered Claim."
      - "Confirm whether IP infringement is covered and any caps/procedures applicable to indemnity."

  - issue_id: I-015
    title: "Provider may use Customer name and logo in marketing"
    severity: YELLOW
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Permits Provider to use Customer name/logo in marketing without an explicit prior-consent requirement in provided text."
    business_impact: "Brand/PR control risk; may conflict with internal policies."
    escalation_trigger:
      triggered: false
      reason: "Usually resolved by adding a consent/approval requirement or opt-out."
    evidence_refs: [EX-027]
    open_questions:
      - "Is prior written consent required for each use?"
      - "Can Customer opt out and require brand guideline compliance?"

  - issue_id: I-016
    title: "Entire agreement clause rejects customer purchase order terms"
    severity: YELLOW
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Rejects Customer purchase order terms; protections must be in the Agreement/Order Form/DPA."
    business_impact: "Procurement assumptions may fail if PO terms are relied upon for data/security/audit requirements."
    escalation_trigger:
      triggered: false
      reason: "Common clause; escalates if procurement requires PO terms and no alternative addendum is available."
    evidence_refs: [EX-023]
    open_questions:
      - "Are any Customer standard terms incorporated via Order Form/Key Terms/addenda?"

  - issue_id: I-017
    title: "Governing law and exclusive jurisdiction depend on variables"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Governing law and exclusive jurisdiction are variable and not specified in provided text."
    business_impact: "May impact dispute cost/enforceability and internal policy compliance."
    escalation_trigger:
      triggered: false
      reason: "Escalates only if chosen law/forum is unacceptable to Customer policy."
    evidence_refs: [EX-025, EX-029]
    open_questions:
      - "What are the Governing Law and Chosen Courts selections on the Cover Page/Order Form?"

  - issue_id: I-018
    title: "Assignment permitted in change of control"
    severity: YELLOW
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Allows assignment in merger/acquisition/change of control; notice/termination rights not shown in provided text."
    business_impact: "Continuity and data-handling concerns if Provider is acquired or obligations move to a new entity."
    escalation_trigger:
      triggered: false
      reason: "Standard; escalates if Customer requires consent/termination rights for assignment."
    evidence_refs: [EX-026]
    open_questions:
      - "Is Customer entitled to advance notice of assignment/change of control?"
      - "Are there termination rights tied to assignment?"

  - issue_id: I-019
    title: "Notices depend on Notice Address and delivery mechanics"
    severity: GREEN
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Standard notice mechanics; Notice Address variables are not included in provided materials."
    business_impact: "Primarily administrative—incorrect addresses can undermine renewal/termination effectiveness."
    escalation_trigger:
      triggered: false
      reason: "Typically operational/clerical; ensure addresses are correct in Order Form/Cover Page."
    evidence_refs: [EX-028]
    open_questions:
      - "What are the parties' Notice Addresses on the Cover Page/Order Form?"
      - "Are email notices permitted (and if so, for which notice types)?"
```