---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: optimised
run: 1
---

## Basis & Context
- Document: Common Paper Cloud Service Agreement — Standard Terms Version 2.1 (released Nov 5, 2024). Only the Standard Terms + scenario were provided; referenced Cover Page / Key Terms / Order Form(s) were not included.
- Your side: Customer / buyer (SaaS subscription), per scenario.
- Review basis: **Generic Commercial Baseline** (no playbook found in provided materials).
- Assumptions / missing info:
  - Missing: Cover Page (variables like liability cap amounts, governing law / chosen courts, “Key Terms”), Key Terms, Order Form(s) (pricing, subscription period, support/SLA, use limitations), Payment Process details, Documentation and Use Limitations, any DPA, security exhibits, and any incorporated policies (e.g., AUP, support policy).
  - Impact: Several key risk allocations (liability caps, data/security commitments, scope definitions) cannot be confirmed and should be treated as unresolved until the missing documents are reviewed.

## Phase 1 — Contract Map (no ratings)
### Document architecture
- Structure provided: “Standard Terms” that contemplate a **Cover Page** (variables), **Framework Terms**, and one or more **Order Form(s)**.
- Incorporation by reference (mentioned but not provided):
  - Order Form: Technical Support (Section 1.2); may authorize Prohibited Data (Section 3.2); defines Subscription Period (Section 5.1); may set Payment Process (Section 4.2–4.3); may include Use Limitations (Section 2.1(b)).
  - Documentation / Use Limitations: compliance required (Section 2.1(b)).
- Order of precedence: not stated in the provided text.

### Key terms snapshot
- Scope of use: Customer may “access and use the Cloud Service” and “copy and use the included Software and Documentation only as needed… for its internal business purposes.” (Section 1.1)
- Support: “Provider will provide Technical Support as described in the Order Form.” (Section 1.2)
- Customer accounts: Customer responsible for user actions; must protect credentials; must notify on suspected fraud/compromise. (Section 1.3)
- Data / content:
  - Usage Data: Provider may “collect and analyze Usage Data” and “freely use Usage Data to maintain, improve, enhance, and promote” offerings; may disclose only if “aggregated and does not identify Customer or Users.” (Section 1.4)
  - Customer Content license: Provider may “copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings.” (Section 1.5)
  - ML/AI: “Usage Data and Customer Content may be used to develop, train, or enhance” AI/ML models (including third-party components), subject to aggregation + de-identification commitments; clause notes AI may be inaccurate and requires human oversight. (Section 1.6)
- Restrictions: broad limits including no reverse engineering, no redistribution, no derivative works, **no security/vulnerability tests**, no competing service, etc. (Section 2.1)
- Suspension: Provider may suspend for (a) >30 day undisputed nonpayment; (b) breach of Section 2.1; or (c) use that violates the agreement or materially negatively impacts product/others — “with or without notice” (but will try to inform when practical). (Section 2.2)
- Privacy: GDPR personal data requires a DPA; DPA controls if conflict. (Section 3.1)
- Prohibited data: Customer must not submit Prohibited Data unless authorized by Order Form or Key Terms. (Section 3.2)
- Fees/taxes: Fees non-refundable except limited prorated refund tied to specified termination rights; dispute process requires timely notice and payment of undisputed amounts. (Section 4)
- Term/termination:
  - Auto-renewal unless non-renewal notice before “Non-Renewal Notice Date” (not provided). (Section 5.1)
  - Termination for material breach (30-day cure) and certain insolvency/uncurable-breach scenarios. (Section 5.3)
  - Force majeure: if product prevented from materially operating for 30+ consecutive days, termination + prorated refund of prepaid fees for remaining term. (Section 5.4)
  - Post-termination: stop use; deletion of Customer Content within 60 days **upon Customer request**; return/destroy confidential info; final billing. (Section 5.5)
  - Survival includes Sections 1.4 and 1.6 (Usage Data / ML), LoL, indemnification, confidentiality, etc. (Section 5.6)
- Warranties / disclaimers:
  - Provider warranty: will not “materially reduce the general functionality” during subscription period. (Section 6.3)
  - Remedy: provider attempts restore; if cannot, termination + prorated refund. (Section 6.4)
  - Broad disclaimer: product may not be safe/secure/error-free; disclaims implied warranties including non-infringement. (Section 7.1)
- Liability:
  - Caps reference “General Cap Amount” and “Increased Cap Amount” (not provided). (Section 8.1)
  - Consequential damages waived. (Section 8.2)
  - Exceptions reference “Increased Claims” and “Unlimited Claims” (not defined in provided excerpt). (Section 8.4)
- Indemnity:
  - Provider indemnifies Customer for “Provider Covered Claims” (undefined here). (Section 9.1)
  - Customer indemnifies Provider for “Customer Covered Claims” (undefined here). (Section 9.2)
  - Exclusions include unauthorized modifications/use, combination, old versions, etc. (Section 9.5)
- Confidentiality: basic non-use/non-disclosure + exclusions and permitted disclosures; injunctive relief for breach. (Section 10; Section 12.4)
- IP reservation: Provider retains all rights in Product; Customer retains all rights in Customer Content, “subject to Sections 1.5 and 1.6.” (Section 11.1)
- Publicity: Provider may use Customer’s name and logo in marketing. (Section 12.8)
- Assignment: no assignment without consent except in merger/acquisition/change of control. (Section 12.6)

### Issue candidates (not yet evaluated)
- AI/ML training on Customer Content (and potentially sensitive data) (Section 1.6).
- Broad Usage Data rights including “promote” products/services (Section 1.4).
- Publicity / logo use without approval (Section 12.8).
- No explicit security controls, audit rights, breach notification timeline, subprocessors, or security exhibit in provided text (Section 3 is mostly DPA gating).
- Deletion only “upon Customer’s request” and within 60 days; backup retention allowed (Sections 5.5(b), 5.6(b)).
- Suspension “with or without notice” and broad triggers; especially for alleged “materially and negatively impacts” (Section 2.2).
- Prohibition on security/vulnerability testing (Section 2.1(a)(v)).
- Liability caps and key definitions missing (Cover Page / Key Terms), preventing evaluation of risk allocation (Section 8).
- Indemnity scope unclear (Covered Claims undefined; relationship to LoL unclear without definitions) (Section 9).
- Governing law / chosen courts are referenced but not provided (Section 12.3).
- Auto-renewal mechanics depend on missing “Non-Renewal Notice Date” (Section 5.1).

## Phase 2 — Evaluated Findings (GREEN/YELLOW/RED)
### 1) Data/AI — Provider use of Customer Content for AI/ML training
- Topic: Data; IP; AI/ML
- Evidence: “Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models…” (Section 1.6)
- Baseline: Generic baseline — customer content should be used to provide the service; any model training on customer content is typically **opt-in** (or excluded), with strong restrictions for confidentiality/personal data.
- Deviation: Express authorization for model training/enhancement on Customer Content (even if aggregated + de-identified).
- Business impact / exposure: Potential confidentiality, competitive, and regulatory risk (e.g., inadvertent learning/leakage concerns; internal stakeholder resistance; DPAs may not cover training use). Could be a deal-breaker given data protection priority.
- Decision needed: Whether vendor is allowed to use Customer Content for training at all; if yes, under what constraints (opt-in, scope, exclusions).
- Disposition: **RED** (escalate to counsel + security/privacy; align with internal policy).

### 2) Data — Usage Data rights include “promote” products/services
- Topic: Data; privacy
- Evidence: Provider may “freely use Usage Data to maintain, improve, enhance, and promote Provider’s products and services” and may disclose only if “aggregated and does not identify Customer or Users.” (Section 1.4)
- Baseline: Generic baseline — allow service improvement/analytics; promotional use is often limited or requires stronger aggregation/non-identification assurances and marketing restrictions.
- Deviation: Promotional use explicitly permitted.
- Business impact / exposure: Reputational/competitive concerns (e.g., implied customer metrics used in marketing). Risk of re-identification claims if aggregation is weak.
- Decision needed: Whether marketing/promo use is acceptable; what de-identification/aggregation standard and controls apply.
- Disposition: **YELLOW** (negotiate).

### 3) Publicity — Provider may use Customer name/logo in marketing
- Topic: Publicity
- Evidence: “Provider may use Customer’s name and logo in marketing.” (Section 12.8)
- Baseline: Generic baseline — customer approval required for publicity (often written consent), at least for name/logo.
- Deviation: Unconditional publicity right.
- Business impact / exposure: Internal comms/brand control; potential compliance concerns (e.g., procurement policy).
- Decision needed: Whether any publicity is allowed, and if so under what approval process.
- Disposition: **YELLOW** (negotiate).

### 4) Security & privacy — DPA is a prerequisite for GDPR personal data, but no security/breach terms are stated here
- Topic: Data protection; security
- Evidence: “Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement with Provider.” (Section 3.1)
- Baseline: Generic baseline — for SaaS with personal data, expect: DPA available, documented security controls, breach notification timeline, subprocessors transparency, and (often) audit reports (SOC 2/ISO 27001).
- Deviation: Standard Terms do not provide the substantive privacy/security commitments; they push to a DPA (not provided) and do not clarify whether Provider will process personal data before a DPA is in place.
- Business impact / exposure: High for this deal (data protection priority). Without DPA/security exhibit, risk can’t be assessed; procurement timelines at 2 weeks likely require immediate DPA + security package.
- Decision needed: Confirm whether personal data will be processed; obtain DPA + security addendum; confirm compliance posture.
- Disposition: **RED** (missing critical documents; cannot approve without them).

### 5) Data retention — deletion only upon request; long window; backup retention
- Topic: Data lifecycle
- Evidence:
  - “Upon Customer’s request, Provider will delete Customer Content within 60 days.” (Section 5.5(b))
  - Recipient may retain confidential info in backups/record retention; Section 3 and 10 continue to apply. (Section 5.6(b))
- Baseline: Generic baseline — deletion/return within a shorter period and/or automatic deletion obligation on termination; backup retention should be time-limited and subject to access restrictions.
- Deviation: Deletion is not automatic and is relatively slow; backups can retain.
- Business impact / exposure: Data minimization and offboarding risk; could complicate regulatory obligations and internal policies.
- Decision needed: Offboarding requirements; whether 60 days + request is acceptable.
- Disposition: **YELLOW** (negotiate).

### 6) Suspension — broad right, potentially without notice
- Topic: Operational continuity
- Evidence: Provider may suspend access if Customer has outstanding undisputed balance >30 days, breaches restrictions, or uses product in violation / materially negatively impacts product/others; may suspend “with or without notice” (will try to inform when practical). (Section 2.2)
- Baseline: Generic baseline — suspension should have notice + opportunity to cure except emergencies; avoid suspension for good-faith disputes.
- Deviation: “With or without notice” + broad “materially and negatively impacts” trigger.
- Business impact / exposure: Business disruption risk (internal ops SaaS); could be unacceptable.
- Decision needed: Required notice/cure standards; emergency suspension carveout.
- Disposition: **YELLOW** (negotiate).

### 7) Security testing — prohibition on vulnerability testing
- Topic: Security assurance
- Evidence: Customer must not “conduct security or vulnerability tests on… or circumvent access restrictions” (Section 2.1(a)(v))
- Baseline: Generic baseline — customers often need some right to security assessment (e.g., review audit reports; limited pen test with notice; third-party assessments), especially for mid-market procurement.
- Deviation: Blanket prohibition.
- Business impact / exposure: Procurement/security may block without audit evidence or an agreed testing pathway.
- Decision needed: Substitute assurances (SOC 2 Type II, ISO 27001, pen-test reports) and/or controlled testing permission.
- Disposition: **YELLOW** (negotiate).

### 8) IP — Customer content ownership preserved, but subject to broad ML clause
- Topic: IP; data
- Evidence: “Customer retains all rights in Customer Content, subject to Sections 1.5 and 1.6.” (Section 11.1)
- Baseline: Generic baseline — customer retains content; provider gets limited license to provide service; ML training typically excluded/opt-in.
- Deviation: Ownership preserved, but subject to 1.6’s training authorization.
- Business impact / exposure: Ownership language may not mitigate training risk.
- Decision needed: Align 1.6 with IP expectations.
- Disposition: **YELLOW** (negotiate via 1.6).

### 9) Limitation of liability — cap amounts and key definitions missing
- Topic: Limitation of liability
- Evidence: “Each party’s total cumulative liability… will not be more than the General Cap Amount… Increased Cap Amount.” (Section 8.1). Exceptions reference “Increased Claims” and “Unlimited Claims.” (Section 8.4)
- Baseline: Generic baseline — for SaaS, expect clear caps (often 12 months fees) and carefully scoped carveouts; customer wants adequate remedies for data/security and IP issues.
- Deviation: Cannot evaluate without Cover Page variables and definition of Increased/Unlimited Claims.
- Business impact / exposure: Potentially severe under-remedy (e.g., if caps are low) or unexpected uncapped exposures.
- Decision needed: Obtain Cover Page/Key Terms and confirm cap amounts + definitions + carveouts.
- Disposition: **RED** (escalate; blocking until confirmed).

### 10) Indemnification — scope unclear without “Covered Claims” definition
- Topic: Indemnity; IP infringement
- Evidence: “Provider will indemnify… from Provider Covered Claims…” (Section 9.1); “Customer will indemnify… from Customer Covered Claims…” (Section 9.2). Definitions list includes “Covered Claim” but does not define it here. (Section 13)
- Baseline: Generic baseline — provider should indemnify for third-party IP infringement claims regarding the product; customer indemnity should be limited to customer content and misuse.
- Deviation: Missing definition prevents confirming IP indemnity scope.
- Business impact / exposure: If IP indemnity is narrow or absent, customer bears risk of infringement claims.
- Decision needed: Confirm Covered Claim definition and ensure provider IP indemnity is included.
- Disposition: **RED** (blocking until confirmed).

### 11) Confidentiality — baseline provisions present
- Topic: Confidentiality
- Evidence: Recipient “will not use or disclose” except as authorized/needed; standard exclusions/permitted disclosures (Section 10).
- Baseline: Generic baseline — mutual confidentiality with need-to-know disclosures and legal compelled disclosure.
- Deviation: None apparent in provided excerpt (term length not specified here).
- Business impact / exposure: Acceptable pending confirmation of any term/duration in missing docs.
- Decision needed: Confirm confidentiality term/duration (if any) in Key Terms/Cover Page.
- Disposition: **GREEN** (note; verify missing pieces).

### 12) Fees — non-refundable, limited proration
- Topic: Commercial
- Evidence: “Fees are non-refundable” except for prorated refund of prepaid fees allowed with specific termination rights. (Section 4.1)
- Baseline: Generic baseline — common for SaaS; ensure proration on termination for provider breach and force majeure is present.
- Deviation: Not unusual, but could be tough if early termination flexibility is desired.
- Business impact / exposure: Low/medium; primarily commercial.
- Decision needed: Confirm termination rights tied to proration are sufficient.
- Disposition: **GREEN/YELLOW** (generally acceptable; negotiate only if business needs more flexibility).

### 13) Auto-renewal — dependent on missing “Non-Renewal Notice Date”
- Topic: Term/renewal
- Evidence: Auto-renewal unless notice before “Non-Renewal Notice Date.” (Section 5.1)
- Baseline: Generic baseline — acceptable with reasonable notice window and clear dates.
- Deviation: Notice date not provided.
- Business impact / exposure: Operational risk if notice window is short.
- Decision needed: Confirm notice window/dates in Order Form/Cover Page.
- Disposition: **YELLOW** (negotiate if window is unfavorable).

### 14) Governing law / venue — missing
- Topic: Disputes
- Evidence: “The Governing Law applies…” and “Chosen Courts have exclusive jurisdiction.” (Section 12.3)
- Baseline: Generic baseline — acceptable if aligned with customer preference/risk profile.
- Deviation: Not assessable without the missing Cover Page variables.
- Business impact / exposure: Medium; affects litigation cost and leverage.
- Decision needed: Obtain Cover Page.
- Disposition: **RED** (missing key term).

## Phase 3 — Redlines (YELLOW/RED only)
> Note: Proposed language is drafted to be insert-ready but may require alignment with the missing Cover Page/Key Terms/Order Form.

### Redline 1 — Restrict AI/ML training on Customer Content (Section 1.6)
- Clause: Section 1.6 (Machine Learning)
- Current language: “Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models…”
- Proposed redline (option A — preferred):
  - Replace the first sentence of Section 1.6 with:
  > “Provider may use Usage Data to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider’s products and services **provided that such Usage Data is aggregated and de-identified and does not identify Customer or any User**. **Provider will not use Customer Content or Personal Data to develop, train, or enhance any artificial intelligence or machine learning models, except to the extent strictly necessary to provide the Cloud Service to Customer (e.g., to operate Customer-facing features for Customer’s account).**”
- Rationale (external-facing): We need to ensure our data is not used to improve models for other customers or third parties; training use creates confidentiality and regulatory risk.
- Priority: Must-have
- Fallback (option B — controlled opt-in):
  > “Provider may use Customer Content to train/enhance models **only if Customer provides prior written consent** (which may be granted per Order Form) and only for the expressly approved scope; Customer may revoke consent prospectively at any time.”
- Notes: Align with DPA (if any) and define whether “Customer Content” may include personal/sensitive data.

### Redline 2 — Tighten Usage Data “promote” usage (Section 1.4)
- Clause: Section 1.4 (Feedback and Usage Data)
- Current language: “Provider may freely use Usage Data to maintain, improve, enhance, and promote Provider’s products and services…”
- Proposed redline:
  > “Provider may use Usage Data to maintain, improve, and enhance Provider’s products and services. Provider may use Usage Data for external marketing or promotional purposes only if such Usage Data is aggregated and de-identified using commercially reasonable measures and **cannot reasonably be used to identify Customer, any User, or Customer’s usage patterns**, and Provider will not publish Customer-specific benchmarks or case studies without Customer’s prior written consent.”
- Rationale (external-facing): We’re comfortable with analytics and product improvement; we need to avoid any customer-identifiable marketing use.
- Priority: Should-have
- Fallback: Permit marketing use limited to high-level aggregated stats with prior notice.
- Notes: Consider adding a definition/standard for “aggregated” and “does not identify.”

### Redline 3 — Publicity requires consent (Section 12.8)
- Clause: Section 12.8 (Logo Rights)
- Current language: “Provider may use Customer’s name and logo in marketing.”
- Proposed redline:
  > “Provider may use Customer’s name and logo in marketing **only with Customer’s prior written consent** in each instance, and Customer may withhold consent in its sole discretion.”
- Rationale (external-facing): We have internal brand and procurement controls over any public references.
- Priority: Should-have
- Fallback: Consent not unreasonably withheld for mutually approved case study after go-live.
- Notes: If vendor insists, allow listing Customer name only (no logo) on a private customer list shown under NDA.

### Redline 4 — Add security + breach notification commitments (insert into Section 3)
- Clause: Section 3 (Privacy & Security)
- Current language: Section 3.1 requires a DPA for GDPR personal data; no other security terms provided here.
- Proposed redline (insert new Section 3.3):
  > “**3.3 Security; Breach Notice.** Provider will implement and maintain commercially reasonable administrative, physical, and technical safeguards designed to protect Customer Content and Personal Data against unauthorized access, use, alteration, and disclosure. Provider will notify Customer without undue delay after becoming aware of a Security Incident involving Customer Content or Personal Data and will provide timely information reasonably requested by Customer to support Customer’s incident response and legal compliance obligations.”
- Rationale (external-facing): We need baseline security and breach notice commitments in the agreement for procurement and compliance.
- Priority: Must-have
- Fallback: Put these commitments into the DPA / security addendum if executed concurrently and incorporated by reference with precedence.
- Notes: Consider adding specific timelines (e.g., 72 hours) if required by internal policy; ensure definitions (Security Incident) are added in Key Terms.

### Redline 5 — Improve deletion/offboarding (Section 5.5(b) and backups)
- Clause: Section 5.5(b) (Effect of Termination) + Section 5.6(b)
- Current language: “Upon Customer’s request, Provider will delete Customer Content within 60 days.” and backups retention allowed.
- Proposed redline:
  > “Upon expiration or termination, Provider will, at Customer’s election, (a) return Customer Content in a reasonably usable format and/or (b) delete Customer Content, in each case within **30 days**. Provider may retain Customer Content solely in encrypted backups in accordance with its standard backup policies for a limited period, provided such retained data is not accessed except as required by law and is deleted/overwritten in the ordinary course.”
- Rationale (external-facing): We need a predictable offboarding timeline and a clear deletion obligation.
- Priority: Should-have
- Fallback: Keep 60 days but make deletion automatic (no request) and provide export right.
- Notes: If the product supports it, request self-service export tools and a deletion certificate.

### Redline 6 — Suspension notice and cure (Section 2.2)
- Clause: Section 2.2 (Suspension)
- Current language: “…Provider may temporarily suspend… with or without notice. However, Provider will try to inform Customer before suspending… when practical.”
- Proposed redline:
  > “Provider may suspend Customer’s access only after providing written notice and a reasonable opportunity to cure, except where Provider reasonably determines suspension is necessary to prevent imminent harm to the Product or other customers. Provider will not suspend access for amounts subject to a good-faith payment dispute under Section 4.6 provided Customer pays undisputed amounts on time.”
- Rationale (external-facing): We need continuity for internal operations and protection during good-faith disputes.
- Priority: Should-have
- Fallback: Emergency suspension allowed, but require notice and reinstatement process within a defined time.
- Notes: Align with incident response and customer communications obligations.

### Redline 7 — Allow controlled security assessments (Section 2.1(a)(v))
- Clause: Section 2.1(a)(v) (Restrictions on Customer)
- Current language: Customer will not “conduct security or vulnerability tests…”
- Proposed redline:
  > “Notwithstanding Section 2.1(a)(v), Customer (or its designated third-party assessor) may conduct reasonable security assessments of the Product, including vulnerability scanning and penetration testing, **subject to Provider’s prior written approval (not to be unreasonably withheld) and reasonable rules of engagement** designed to avoid service disruption.”
- Rationale (external-facing): Our security program requires the ability to validate controls (or a viable substitute).
- Priority: Nice-to-have / Should-have (depending on security requirements)
- Fallback: Provider provides current SOC 2 Type II / ISO 27001 report and recent pen-test summary under NDA; no customer testing.
- Notes: Choose either audit reports or testing—don’t insist on both if time is tight.

### Redline 8 — Resolve liability/indemnity missing definitions via Cover Page/Key Terms (Sections 8–9)
- Clause: Sections 8 (Limitation of Liability) and 9 (Indemnification)
- Current language: Caps and Covered Claims depend on missing variables/definitions.
- Proposed redline (Cover Page / Key Terms additions — required):
  - Add to Cover Page variables:
    - “General Cap Amount: fees paid or payable by Customer under the applicable Order Form in the 12 months preceding the event giving rise to the claim.”
    - “Increased Cap Amount: [higher multiple/amount to be agreed], applicable to data protection/security incidents, confidentiality breaches, and indemnity obligations.”
  - Ensure “Provider Covered Claims” includes third-party IP infringement claims alleging the Product infringes/misappropriates IP rights.
- Rationale (external-facing): We need clear, commercially reasonable caps and a standard IP indemnity for vendor-provided SaaS.
- Priority: Must-have
- Fallback: If vendor won’t increase caps, seek: stronger security obligations + service credits + termination rights, and narrow any uncapped exposures for Customer.
- Notes: This item is blocked until the actual Cover Page/Key Terms are provided.

## Phase 4 — Negotiation Strategy & Next Steps
### Prioritized asks
- Must-have:
  - Remove/opt-in AI/ML training on **Customer Content** (Section 1.6).
  - Obtain and incorporate DPA + security addendum; add security/breach notice commitments if not already in DPA (Section 3).
  - Confirm/renegotiate **liability cap amounts and carveouts** (Section 8; missing Cover Page/Key Terms).
  - Confirm provider IP indemnity scope via “Covered Claims” definition (Section 9; missing).
- Should-have:
  - Publicity/name/logo requires written consent (Section 12.8).
  - Improve deletion/offboarding commitments (Section 5.5) and clarify backup retention limits.
  - Suspension requires notice/cure and protects good-faith disputes (Section 2.2).
- Nice-to-have (or substitute assurance):
  - Controlled security assessment rights or strong third-party audit evidence (Section 2.1).

### Proposed tradeoffs
- If vendor resists training restrictions, offer a narrow opt-in for specific anonymized datasets with explicit approval per Order Form, and/or allow training on aggregated Usage Data only.
- If vendor resists higher liability caps, trade for stronger security commitments, faster breach notice, and clear termination/refund rights for security failures.

### Escalations
- Escalate to privacy/security counsel and procurement stakeholders:
  - AI/ML training on Customer Content (Section 1.6).
  - Missing DPA/security package.
  - Missing liability cap variables and indemnity definitions.

### Next steps
- Request immediately (timebox to meet 2-week deadline):
  - The **Cover Page** (variables: Governing Law, Chosen Courts, cap amounts, Key Terms).
  - The **Order Form(s)** (Subscription Period, fees, support/SLA, use limitations, Payment Process).
  - The **DPA** and any security exhibit (SOC 2/ISO, subprocessors, breach terms).
- Once received: re-run Phase 2 focusing on the now-specified caps, definitions, and data/security obligations; then finalize redlines.

This is not legal advice; counsel should review before use.
