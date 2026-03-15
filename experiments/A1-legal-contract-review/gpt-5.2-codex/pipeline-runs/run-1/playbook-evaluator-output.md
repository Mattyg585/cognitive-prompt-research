---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A1
tier: pipeline
run: 1
stage: playbook-evaluator
---

## Deviations & Risk Classification
- 1.6 Machine Learning — RED
  - Playbook position: No use of Customer Content for model training/feature development without explicit opt-in; usage data only aggregated/de-identified with strict limits.
  - Deviation: Provider may use aggregated, de-identified Customer Content and Usage Data to develop, train, or enhance AI/ML features.
  - Impact: Potential IP/confidentiality leakage, regulatory exposure, and loss of control over data-derived models.
  - Escalation trigger: Any regulated/sensitive data, or internal policy prohibiting training on customer data.
  - Reference: Section 1.6

- 1.4 Feedback and Usage Data — YELLOW
  - Playbook position: Provider may use usage data internally for service improvement; sharing limited and no re-identification.
  - Deviation: Broad rights to use Feedback and Usage Data, with only aggregation/non-identification limits on disclosure.
  - Impact: Competitive and privacy risk from expansive data-use rights.
  - Escalation trigger: Data sensitivity or concern about secondary use beyond service improvement.
  - Reference: Section 1.4

- 2.2 Suspension — YELLOW
  - Playbook position: Suspension only for material breach or security risk, with notice and opportunity to cure when feasible.
  - Deviation: Provider may suspend access with or without notice for nonpayment, restriction breaches, or harmful use.
  - Impact: Service interruption risk without advance notice.
  - Escalation trigger: Service is business-critical or short notice is unacceptable.
  - Reference: Section 2.2

- 4.1 Fees (Non-Refundable) — YELLOW
  - Playbook position: Prorated refunds for termination for cause and clearer refund rights when service fails.
  - Deviation: Fees are non-refundable except limited prorated refunds tied to specific termination rights.
  - Impact: Financial exposure if service underperforms or terminates early.
  - Escalation trigger: Large prepaid amounts or high reliance on service performance.
  - Reference: Section 4.1

- 6.3–6.4 Provider Warranty/Remedy — YELLOW
  - Playbook position: Performance warranty with meaningful remedies and reasonable notice periods.
  - Deviation: Warranty limited to no material reduction of general functionality; 45-day notice window; restore-or-terminate remedy.
  - Impact: Narrow remedy and short notice window may limit recourse.
  - Escalation trigger: High availability or performance commitments required.
  - Reference: Sections 6.3–6.4

- 8.1–8.4 Liability Limits — YELLOW
  - Playbook position: Cap tied to meaningful multiple of fees; carve-outs for data breach, confidentiality, and IP infringement.
  - Deviation: Cap amounts and Increased Claims are in the Cover Page; damages waiver broadly applies except Increased Claims and confidentiality.
  - Impact: Potentially low cap and missing data-breach carve-out could leave Customer under-protected.
  - Escalation trigger: Low cap values or no carve-out for data security/privacy violations.
  - Reference: Sections 8.1–8.4

- 9.6 Exclusive Remedy — YELLOW
  - Playbook position: Preserve broader remedies for material breaches (especially data/privacy and IP).
  - Deviation: Indemnity and termination rights are exclusive remedies for Covered Claims.
  - Impact: Limits recovery options if indemnity scope is narrow.
  - Escalation trigger: Covered Claim definitions are narrow or exclude data/privacy issues.
  - Reference: Section 9.6

- 12.8 Logo Rights — YELLOW
  - Playbook position: Marketing use of name/logo only with prior written consent (opt-in).
  - Deviation: Provider may use Customer name and logo in marketing.
  - Impact: Uncontrolled publicity and brand risk.
  - Escalation trigger: Strict brand controls or confidentiality around vendor relationships.
  - Reference: Section 12.8

- Missing: Security standards/audit rights — RED
  - Playbook position: Explicit security controls, audit/attestation rights, and minimum standards.
  - Deviation: No specific security controls or audit rights beyond DPA requirement.
  - Impact: Insufficient assurance for data protection obligations.
  - Escalation trigger: Regulated data or internal security compliance requirements.
  - Reference: Missing clause

- Missing: Data breach notification/incident response — RED
  - Playbook position: Defined breach notification timelines and cooperation obligations.
  - Deviation: No breach notification timeline or incident response commitments.
  - Impact: Compliance and operational risk if an incident occurs.
  - Escalation trigger: Any personal data processing or regulatory obligations.
  - Reference: Missing clause

- Missing: Service levels/uptime credits — YELLOW
  - Playbook position: SLA with measurable uptime and service credits.
  - Deviation: No SLA or service credit commitments.
  - Impact: Limited recourse for downtime.
  - Escalation trigger: Mission-critical service reliance.
  - Reference: Missing clause

- Missing: Data residency/subprocessor transparency — YELLOW
  - Playbook position: Disclosure of data locations and subprocessors; approval/notice rights.
  - Deviation: No data residency or subprocessor transparency commitments.
  - Impact: Cross-border transfer and compliance risk.
  - Escalation trigger: Data localization requirements or strict vendor risk policies.
  - Reference: Missing clause

- Missing: Data export/transition assistance — YELLOW
  - Playbook position: Clear data export format and transition support at termination.
  - Deviation: No portability or transition assistance commitments.
  - Impact: Risk of vendor lock-in and operational disruption at exit.
  - Escalation trigger: Short transition windows or complex data migrations.
  - Reference: Missing clause

- Missing: Termination for convenience/price increase controls — YELLOW
  - Playbook position: Termination for convenience or renewal price protections.
  - Deviation: No convenience termination or price increase protections identified.
  - Impact: Commercial flexibility risk.
  - Escalation trigger: Budget sensitivity or volatile pricing.
  - Reference: Missing clause

- Missing: Insurance requirements — YELLOW
  - Playbook position: Vendor maintains adequate cyber/tech E&O insurance.
  - Deviation: No insurance obligations stated.
  - Impact: Limited financial backstop for losses.
  - Escalation trigger: High risk profile or enterprise procurement requirements.
  - Reference: Missing clause

## Most Material Issues (ordered)
- Use of Customer Content/Usage Data for AI/ML training (Section 1.6).
- Missing security standards/audit rights and breach notification commitments.
- Suspension without notice (Section 2.2).
- Liability cap values/absence of data-breach carve-out (Sections 8.1–8.4; Cover Page).
- No SLA/service credits.
- Broad marketing use of Customer name/logo (Section 12.8).

## Assumptions / Open Questions
- Cover Page variables (General Cap Amount, Increased Cap Amount, Governing Law, Chosen Courts, Notice Address, Use Limitations, Key Terms) are unknown.
- Order Form details (Subscription Period, Support terms, Payment Process, Fees/currency) are unknown.
- Whether a DPA is executed and what security/breach terms it contains is unknown.
- Data sensitivity/regulatory profile and whether Customer permits any model training on Customer Content.
