---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: pipeline
run: 3
stage: 03-playbook-evaluation
---

| Issue ID | Title | Severity | Negotiation priority | Playbook position source | Deviation summary | Business impact | Escalation trigger (yes/no + why) | Evidence refs (EX-…) | Open questions |
|---|---|---|---|---|---|---|---|---|---|
| I-001 | AI/ML training and enhancement using Usage Data and Customer Content | RED | Must-have | GENERIC | Provider is authorized to use aggregated/de-identified Usage Data **and Customer Content** to develop/train/enhance AI/ML models (including third‑party components), which goes beyond “provide the service” usage expectations for many customers. | Potential confidentiality/competitive sensitivity risk; potential IP/data governance concerns; heightened stakeholder scrutiny given focus on data protection and IP ownership. | yes — expands data use beyond core service delivery; may conflict with internal policies on model training / third‑party processing. | EX-005 | What is the definition of “Usage Data” and does it include content-derived features/outputs?; Are there opt‑outs or customer-specific boundaries on training?; What third‑party components/subprocessors are involved?; Retention for training data and whether model weights are treated as containing Customer data? |
| I-002 | Broad rights to use Feedback and Usage Data (including for promotion) | YELLOW | Should-have | GENERIC | Provider may use Feedback “freely” and may “freely use” Usage Data to improve/enhance/**promote** products; disclosure to others limited to aggregated non-identifying Usage Data. | Risk that “Usage Data” could still reveal sensitive operational patterns; marketing/benchmarking concerns depending on what qualifies as “aggregated.” | no — bounded by aggregation/non-identification for external disclosure, but still worth tightening depending on definitions. | EX-003 | How is “Usage Data” defined and what is “aggregated”?; Can Customer restrict use for promotion/marketing? |
| I-003 | Scope of Provider license to Customer Content; deletion on request; retention via backups | YELLOW | Should-have | GENERIC | License allows Provider to copy/display/modify/use Customer Content to provide and maintain the Product and “related offerings”; deletion is only **upon Customer request** within 60 days; backups/record retention allow continued retention of Confidential Information. | Data governance friction: Customer must operationalize deletion requests; ambiguity in “related offerings” could broaden use; backup retention may impede full deletion expectations. | no — manageable if operationalized, but may be policy-sensitive for regulated/sensitive data. | EX-004, EX-013, EX-014 | What are “related offerings”?; Is deletion automatic or request-only and how requested?; Provider backup/retention periods and deletion timelines for backups? |
| I-004 | DPA required for GDPR Personal Data; DPA controls conflicts | RED | Escalate | GENERIC | Agreement requires a DPA **before** submitting GDPR Personal Data and states DPA controls conflicts; the DPA is not provided, leaving core privacy/security terms unknown. | Material compliance and go-live gating risk if GDPR Personal Data will be processed; unknown subprocessors/transfer/security obligations until DPA reviewed/executed. | yes — missing DPA terms are a compliance gating item if any GDPR Personal Data will be processed. | EX-009 | Is a standard DPA available and what are security measures, subprocessors, transfers?; Does Provider process non‑GDPR personal data and what governs it? |
| I-005 | Prohibited Data restrictions depend on Order Form or Key Terms not provided | YELLOW | Must-have | GENERIC | Customer is prohibited from submitting “Prohibited Data” unless authorized by Order Form/Key Terms, but those definitions/permissions are not provided. | Risk of unintended noncompliance or blocked use-cases if Customer’s intended datasets fall into “Prohibited Data.” | no — primarily a scope/fit issue, but could become escalatory if intended use requires regulated data. | EX-010 | How is “Prohibited Data” defined?; Does the Order Form authorize any categories for this deal? |
| I-006 | Restriction on security or vulnerability testing | YELLOW | Should-have | GENERIC | Blanket restriction on security/vulnerability testing could prevent routine scanning/pen testing without an exception process. | May conflict with Customer security assurance requirements; could slow incident response and vendor risk management approvals. | no — unless Customer policy requires testing rights; then becomes escalation. | EX-006 | Is there an approval-based security testing process (scope/notice) elsewhere (Order Form/policy)? |
| I-007 | Documentation and Use Limitations incorporated by reference | YELLOW | Must-have | GENERIC | Compliance obligation extends to “Documentation and Use Limitations,” which are not included; potential for unilateral updates depending on external docs. | Hidden/variable obligations; risk of future restrictions impacting operations, compliance, or pricing/usage. | yes — incorporated documents not provided can materially change risk/obligations; should be reviewed/locked for the deal. | EX-007 | What specific docs/use limits apply and where located?; Can they be updated unilaterally and what notice applies? |
| I-008 | Provider suspension rights “with or without notice” | YELLOW | Should-have | GENERIC | Provider may suspend with or without notice for certain triggers; only “try to inform” when practical; reinstatement conditioned on curing. | Availability/continuity risk; potential operational disruption if suspension occurs without advance notice, especially for disputed allegations or automated triggers. | no — common in SaaS for abuse/security, but should be bounded (notice, cure, partial suspension) where possible. | EX-008 | Cure periods/escalation paths in SLA/Order Form?; Is suspension scoped to tenant vs users/workloads? |
| I-009 | Auto-renewal mechanics depend on Non-Renewal Notice Date | YELLOW | Should-have | GENERIC | Renewal is automatic unless notice given before a “Non‑Renewal Notice Date,” but the date is a variable not provided. | Procurement calendaring risk (missed notice leads to unwanted renewal/fees). | no — administrative, but important to confirm in Order Form/Cover Page. | EX-012 | What is the notice window/date (e.g., 30/60/90 days)?; What is the Notice Address for non-renewal? |
| I-010 | Non-refundable fees with limited prorated refund pathways | YELLOW | Nice-to-have | GENERIC | Fees are non-refundable except for prorated refunds tied to specific termination rights; broader commercial flexibility is limited. | Financial risk if early termination or dissatisfaction; dependence on termination triggers for recovery. | no — commercial issue; escalate only if business requires refund/exit flexibility. | EX-011, EX-026, EX-015 | Which termination rights provide prorated refunds beyond those explicit?; SLA credits/additional refund terms in Order Form? |
| I-011 | Provider warranty scope and remedy (functionality; notice window) | YELLOW | Should-have | GENERIC | Warranty is limited to not materially reducing general functionality; remedy is restore-or-terminate with prorated refund; notice must be given within 45 days of discovery. | May be insufficient for security/privacy or performance expectations; notice window and limited remedies may reduce leverage. | no — typical baseline; escalation if business relies on stronger uptime/security commitments. | EX-015 | What “Additional Warranties” exist (6.1(d)) and do they cover security/privacy? |
| I-012 | Disclaimer of warranties includes safe/secure/error-free statements | YELLOW | Should-have | GENERIC | Provider disclaims that Product will always be safe/secure/error‑free, and disclaims other warranties except Section 6. | Reinforces need for explicit SLA/security commitments elsewhere; may undercut reliance on implied assurances. | no — common disclaimer, but should be balanced by affirmative security/SLA commitments if required. | EX-016 | Are there security commitments/audit reports/uptime terms in Order Form or separate security docs? |
| I-013 | Liability caps depend on Cover Page variables; category-based exceptions | RED | Escalate | GENERIC | Liability caps (General/Increased) and categories (Increased/Unlimited Claims) depend on Cover Page/Definitions not provided; undefined variables default to “none/not applicable,” creating risk of unexpectedly low caps or broad carve-outs. | Material allocation-of-risk unknown; could materially limit Customer recovery and/or expand exposure depending on how categories are defined. | yes — liability cap terms/definitions missing are a core risk item; requires legal escalation before acceptance. | EX-017, EX-025 | What are the cap amounts on the Cover Page?; How are “Increased Claims” and “Unlimited Claims” defined? |
| I-014 | Indemnification scope depends on defined terms; exclusive remedy language | RED | Escalate | GENERIC | Indemnity applies to “Provider Covered Claims,” but the defined scope is not provided; exclusive-remedy framing may limit other remedies; exclusions could be broad. | If IP infringement and key third-party claims aren’t clearly covered, Customer bears major risk; exclusive remedy could reduce flexibility. | yes — indemnity scope/definitions are core risk allocation and require escalation if not clearly acceptable. | EX-018 | Definition of “Provider Covered Claims” (incl. IP infringement?) ; Any limits on counsel choice/settlement/cooperation costs beyond stated? |
| I-015 | Governing law and exclusive jurisdiction variables | YELLOW | Nice-to-have | GENERIC | Governing law and chosen courts are variables not provided; could be set to an unfavorable forum. | Increased dispute cost/complexity depending on forum; may affect enforceability and internal policy compliance. | no — unless forum selection violates internal policy or creates regulatory constraints. | EX-022 | What are the selected Governing Law and Chosen Courts on Cover Page/Key Terms? |
| I-016 | Provider marketing use of Customer name and logo | YELLOW | Should-have | GENERIC | Provider may use Customer name/logo for marketing without stated consent/approval mechanics in the excerpt. | Brand/communications control risk; may conflict with internal PR/brand policies. | no — often negotiable to require approval/limits; escalate only if strict policy. | EX-024 | Are there limitations/approval requirements in Order Form/Cover Page? |
| I-017 | Entire agreement clause rejects Customer purchase order terms | YELLOW | Nice-to-have | GENERIC | Provider rejects Customer PO terms and states agreement supersedes prior statements, limiting incorporation of procurement boilerplate. | Customer must ensure required supplier terms (security, compliance, etc.) are in Order Form/DPA rather than relying on PO. | no — typical clause; operational reminder rather than a material legal blocker. | EX-021 | Are any Customer procurement terms intended to apply, and if so where are they incorporated? |
| I-018 | Assignment restrictions with M&A/change-of-control exception | YELLOW | Nice-to-have | GENERIC | Assignment generally requires consent with an exception for merger/acquisition/change of control; details may affect corporate flexibility. | Potential friction for reorganizations or transfers; may affect affiliate deals. | no — usually manageable; escalate if impending corporate restructuring requires assignment flexibility. | EX-023 | Does consent requirement apply to assignment by operation of law outside the stated exception? |
| I-019 | Customer responsibility for user actions and credential security | GREEN | Nice-to-have | GENERIC | Customer is responsible for user actions and credential security; standard operational allocation in SaaS terms. | Drives internal IAM/credential controls and incident notification process; generally consistent with baseline expectations. | no — standard. | EX-027 | What auth/security controls are available (SSO/MFA) and are they included in the subscription/Order Form? |

```yaml
findings:
  - issue_id: I-001
    title: "AI/ML training and enhancement using Usage Data and Customer Content"
    severity: RED
    negotiation_priority: Must-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Provider is authorized to use aggregated/de-identified Usage Data and Customer Content to develop/train/enhance AI/ML models (incl. third-party components), which exceeds many customers’ baseline expectations for Customer Content use."
    business_impact: "Potential confidentiality/competitive sensitivity and data governance/IP concerns; heightened scrutiny given data_protection and ip_ownership focus."
    escalation_trigger:
      triggered: true
      reason: "Authorizes broader data use (model training) beyond core service delivery; may conflict with internal policy requirements and third-party processing constraints."
    evidence_refs: [EX-005]
    open_questions:
      - "What is the definition of 'Usage Data' and does it include event logs, metadata, content-derived features, or outputs?"
      - "Are there opt-outs, customer-specific model boundaries, or contractual limits on using Customer Content for model training?"
      - "What third-party components/subprocessors are involved in these AI/ML features?"
      - "What are the retention periods for data used in AI/ML training, and are trained model weights treated as containing Customer data?"

  - issue_id: I-002
    title: "Broad rights to use Feedback and Usage Data (including for promotion)"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Provider may use Feedback freely and may freely use Usage Data to improve/enhance/promote products; external disclosure limited to aggregated non-identifying Usage Data."
    business_impact: "Potential for sensitive operational insights to be inferred depending on how 'Usage Data' and 'aggregated' are defined; marketing/benchmarking concerns."
    escalation_trigger:
      triggered: false
      reason: "External disclosure constrained to aggregated/non-identifying, but definitions should be confirmed."
    evidence_refs: [EX-003]
    open_questions:
      - "How does the contract define 'Usage Data' and 'aggregated' in this context?"
      - "Is Customer permitted to restrict use of Usage Data for promotion/marketing?"

  - issue_id: I-003
    title: "Scope of Provider license to Customer Content; deletion on request; retention via backups"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Customer Content use includes 'related offerings'; deletion occurs within 60 days only upon Customer request; backup/record-retention allows retention of Confidential Information."
    business_impact: "Operational burden to request deletion; ambiguity may broaden use; backup retention may not meet strict deletion expectations."
    escalation_trigger:
      triggered: false
      reason: "Typically manageable with process controls, but may be policy-sensitive depending on data types."
    evidence_refs: [EX-004, EX-013, EX-014]
    open_questions:
      - "What are 'related offerings' and do they include optional modules, add-ons, or separate products?"
      - "Is Customer Content deleted automatically on termination, or only if Customer requests it (and how is that request made)?"
      - "What are Provider's standard backup/retention periods and deletion timelines for backups?"

  - issue_id: I-004
    title: "DPA required for GDPR Personal Data; DPA controls conflicts"
    severity: RED
    negotiation_priority: Escalate
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Agreement requires executing a DPA before submitting GDPR Personal Data and states DPA controls conflicts; DPA terms are not provided."
    business_impact: "Potential compliance and launch gating risk; security/subprocessor/transfer obligations unknown until DPA is reviewed/executed."
    escalation_trigger:
      triggered: true
      reason: "If any GDPR Personal Data will be processed, missing DPA terms are a compliance gating item requiring legal/privacy escalation."
    evidence_refs: [EX-009]
    open_questions:
      - "Is there a standard DPA available, and what are the security measures, subprocessors, and cross-border transfer terms?"
      - "Does Provider process any Personal Data outside GDPR scope (and what governs those terms if not in a DPA)?"

  - issue_id: I-005
    title: "Prohibited Data restrictions depend on Order Form or Key Terms not provided"
    severity: YELLOW
    negotiation_priority: Must-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Customer cannot submit 'Prohibited Data' unless authorized by Order Form/Key Terms, but those definitions/permissions are not provided."
    business_impact: "Risk intended datasets/use-cases are disallowed; potential compliance exposure if definitions are broader than expected."
    escalation_trigger:
      triggered: false
      reason: "Primarily a scope/fit issue until intended data types are confirmed."
    evidence_refs: [EX-010]
    open_questions:
      - "How is 'Prohibited Data' defined in the Key Terms/Definitions, and does it include regulated data types relevant to Customer?"
      - "Does the Order Form authorize any categories of Prohibited Data for this deal?"

  - issue_id: I-006
    title: "Restriction on security or vulnerability testing"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Customer is prohibited from conducting security/vulnerability tests on the Product (and related interference/circumvention activities)."
    business_impact: "May conflict with vendor risk management requirements and routine assurance activities; could delay approvals or incident response."
    escalation_trigger:
      triggered: false
      reason: "Becomes escalatory if Customer policy requires pentest/scanning rights."
    evidence_refs: [EX-006]
    open_questions:
      - "Is there a permitted security testing process (e.g., written approval, scope limits) in the Order Form or separate policy?"

  - issue_id: I-007
    title: "Documentation and Use Limitations incorporated by reference"
    severity: YELLOW
    negotiation_priority: Must-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Agreement incorporates external Documentation/Use Limitations not provided, creating potentially material obligations outside the Standard Terms excerpt."
    business_impact: "Hidden and potentially changeable constraints could affect operations, compliance, and commercial usage over time."
    escalation_trigger:
      triggered: true
      reason: "Incorporated documents not provided can materially change obligations; should be reviewed and anchored for the deal."
    evidence_refs: [EX-007]
    open_questions:
      - "What specific Documentation and Use Limitations apply to the Product for this deal, and where are they located?"
      - "Can Documentation/Use Limitations be updated unilaterally, and if so, what notice applies?"

  - issue_id: I-008
    title: "Provider suspension rights 'with or without notice'"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Provider may suspend access with or without notice for specified triggers; only attempts to inform Customer when practical; reinstatement depends on resolving underlying issue."
    business_impact: "Service continuity risk and potential operational disruption; may require internal runbooks for rapid remediation and communication."
    escalation_trigger:
      triggered: false
      reason: "Common for abuse/security contexts; negotiate bounds/notice where possible."
    evidence_refs: [EX-008]
    open_questions:
      - "Are there cure periods, escalation paths, or minimum notice commitments in the Order Form/SLA?"
      - "Does suspension apply to the whole tenant/account or only specific users/workloads?"

  - issue_id: I-009
    title: "Auto-renewal mechanics depend on Non-Renewal Notice Date"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Order Forms auto-renew unless notice is given before the Non-Renewal Notice Date, which is a variable not provided in the excerpt."
    business_impact: "Risk of inadvertent renewal and unexpected spend if notice timing/addresses are not operationalized."
    escalation_trigger:
      triggered: false
      reason: "Administrative control item; confirm notice window and address in deal documents."
    evidence_refs: [EX-012]
    open_questions:
      - "What is the Non-Renewal Notice Date for the Order Form (e.g., 30/60/90 days)?"
      - "What is the Notice Address for sending non-renewal notices?"

  - issue_id: I-010
    title: "Non-refundable fees with limited prorated refund pathways"
    severity: YELLOW
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Fees are non-refundable except for prorated refunds tied to specific termination rights; broader refund/exit flexibility is limited."
    business_impact: "Commercial risk if Customer needs to exit early; recovery depends on narrow termination scenarios and any SLA credits."
    escalation_trigger:
      triggered: false
      reason: "Primarily commercial; escalate only if business requires stronger termination/refund options."
    evidence_refs: [EX-011, EX-026, EX-015]
    open_questions:
      - "Which termination rights are intended to provide prorated refunds for this deal (beyond those explicitly stated)?"
      - "Are there SLA credits or additional refund terms in the Order Form?"

  - issue_id: I-011
    title: "Provider warranty scope and remedy (functionality; notice window)"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Warranty limited to no material reduction of general functionality; remedy is restore-or-terminate with prorated refund; Customer must notify within 45 days of discovery."
    business_impact: "Limited protection for performance/security needs; notice timing may reduce ability to claim remedies if missed."
    escalation_trigger:
      triggered: false
      reason: "Typical baseline; evaluate against business-critical reliability/security requirements."
    evidence_refs: [EX-015]
    open_questions:
      - "What are the 'Additional Warranties' referenced in 6.1(d), and do any apply to security/privacy?"

  - issue_id: I-012
    title: "Disclaimer of warranties includes safe/secure/error-free statements"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Provider disclaims guarantees of being safe/secure/error-free and disclaims other warranties/conditions except those in Section 6."
    business_impact: "Reinforces need for explicit SLA/security commitments via Order Form/DPA/security addendum."
    escalation_trigger:
      triggered: false
      reason: "Common disclaimer; negotiate affirmative commitments elsewhere if required."
    evidence_refs: [EX-016]
    open_questions:
      - "Are there security commitments, audit reports, or uptime/SLA terms in the Order Form or separate security documentation?"

  - issue_id: I-013
    title: "Liability caps depend on Cover Page variables; category-based exceptions"
    severity: RED
    negotiation_priority: Escalate
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Liability caps and exception categories depend on undefined Cover Page variables and Definitions not provided; undefined variables default to 'none'/'not applicable,' creating uncertainty and potential adverse outcomes."
    business_impact: "Core risk allocation unknown; could materially limit Customer recovery and/or expand exposure depending on cap amounts and category definitions."
    escalation_trigger:
      triggered: true
      reason: "Missing cap amounts and definitions for Increased/Unlimited Claims are material and require legal escalation before acceptance."
    evidence_refs: [EX-017, EX-025]
    open_questions:
      - "What are the General Cap Amount and Increased Cap Amount in the Cover Page for this deal?"
      - "How are 'Increased Claims' and 'Unlimited Claims' defined in the Definitions/Key Terms?"

  - issue_id: I-014
    title: "Indemnification scope depends on defined terms; exclusive remedy language"
    severity: RED
    negotiation_priority: Escalate
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Provider indemnity applies to 'Provider Covered Claims' but scope is definition-dependent (not provided); Section 9 plus termination rights described as exclusive remedies for Covered Claims; exclusions may narrow coverage."
    business_impact: "If key third-party claims (e.g., IP infringement) are not clearly covered, Customer bears material risk; exclusive remedy framing may limit relief."
    escalation_trigger:
      triggered: true
      reason: "Indemnity scope and definitions are central risk allocation; escalate to confirm IP/critical coverage and remedy landscape."
    evidence_refs: [EX-018]
    open_questions:
      - "What is the definition/scope of 'Provider Covered Claims' and does it include intellectual property infringement claims?"
      - "Are there limitations on defense counsel choice, settlement authority, or cooperation costs beyond what is stated here?"

  - issue_id: I-015
    title: "Governing law and exclusive jurisdiction variables"
    severity: YELLOW
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Governing law and chosen courts are variables not included in the excerpt; forum could be unfavorable."
    business_impact: "Potential increased dispute cost/complexity and policy compliance issues depending on selected law/forum."
    escalation_trigger:
      triggered: false
      reason: "Escalate only if selected forum violates policy or creates material cost/regulatory constraints."
    evidence_refs: [EX-022]
    open_questions:
      - "What are the Governing Law and Chosen Courts specified on the Cover Page/Key Terms?"

  - issue_id: I-016
    title: "Provider marketing use of Customer name and logo"
    severity: YELLOW
    negotiation_priority: Should-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Provider may use Customer name and logo in marketing without an explicit approval/consent process in the excerpt."
    business_impact: "Brand/communications control risk; may require internal approvals and coordinated external communications."
    escalation_trigger:
      triggered: false
      reason: "Typically negotiable to add approval/limits; escalate if strict brand policy."
    evidence_refs: [EX-024]
    open_questions:
      - "Are there limitations (e.g., prior written approval, timing, press release coordination) in the Order Form or Cover Page?"

  - issue_id: I-017
    title: "Entire agreement clause rejects Customer purchase order terms"
    severity: YELLOW
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Agreement supersedes prior statements and rejects Customer purchase order terms, limiting incorporation of procurement boilerplate."
    business_impact: "Operationally, required Customer terms (security/compliance) must be placed in Order Form/DPA/addenda rather than relying on PO flowdown."
    escalation_trigger:
      triggered: false
      reason: "Common clause; manage by ensuring required terms are explicitly incorporated elsewhere."
    evidence_refs: [EX-021]
    open_questions:
      - "Are any Customer procurement terms intended to apply (e.g., supplier code, security addendum), and if so where are they incorporated?"

  - issue_id: I-018
    title: "Assignment restrictions with M&A/change-of-control exception"
    severity: YELLOW
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Assignment generally requires consent, except for merger/acquisition/change of control."
    business_impact: "May create friction for reorganizations, affiliate transfers, or divestitures; could impact future flexibility."
    escalation_trigger:
      triggered: false
      reason: "Typically manageable unless corporate changes are anticipated."
    evidence_refs: [EX-023]
    open_questions:
      - "Does the consent requirement apply to assignment by operation of law outside the stated exception?"

  - issue_id: I-019
    title: "Customer responsibility for user actions and credential security"
    severity: GREEN
    negotiation_priority: Nice-to-have
    playbook_position_source: GENERIC
    playbook_position: "GENERIC"
    deviation_summary: "Customer is responsible for Users' actions and must protect credentials and notify Provider of suspected compromise—standard SaaS allocation."
    business_impact: "Requires internal IAM controls and incident notification processes; generally aligns with baseline expectations."
    escalation_trigger:
      triggered: false
      reason: "Standard provision."
    evidence_refs: [EX-027]
    open_questions:
      - "What authentication/security controls are available (e.g., SSO/MFA) and are they included in the subscription/Order Form?"
```