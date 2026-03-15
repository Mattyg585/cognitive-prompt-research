---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A1
tier: pipeline
run: 3
stage: playbook-evaluator
---

## Deviations & Risk Classification
- [1.6] Machine Learning — RED
  - Playbook position: Customer Content not used to train provider/third-party models; usage data only if de-identified and with clear opt-out/consent.
  - Deviation: Provider may use aggregated/de-identified Usage Data and Customer Content to train AI/ML models, including third-party components.
  - Impact: Loss of control of customer data/IP; privacy/regulatory exposure; competitive risk.
  - Escalation trigger: Any training on Customer Content or Personal Data; third-party training use.
  - Reference: Section 1.6 excerpt.
- [12.8] Logo Rights — YELLOW
  - Playbook position: Marketing use of name/logo requires prior written approval and scope limits.
  - Deviation: Provider may use Customer’s name and logo in marketing without approval.
  - Impact: Brand/PR risk and implied endorsement.
  - Escalation trigger: Public marketing use without approval or scope limits.
  - Reference: Section 12.8 excerpt.
- [2.2] Suspension — YELLOW
  - Playbook position: Suspension only for material breach or security threat, with notice and cure except emergencies; no suspension for disputed invoices.
  - Deviation: Provider may suspend for overdue undisputed balances, restriction breaches, or harmful use, with notice only when practical.
  - Impact: Service disruption risk; leverage in payment disputes.
  - Escalation trigger: Suspension for payment without cure period or for alleged breach without notice.
  - Reference: Section 2.2 excerpt.
- [5.1] Auto-Renewal — YELLOW
  - Playbook position: No auto-renewal or clear advance notice and mutual agreement on renewal terms.
  - Deviation: Auto-renews unless timely non-renewal notice; notice window not specified here.
  - Impact: Unintended renewals and pricing lock-in risk.
  - Escalation trigger: Short/undefined notice period or unilateral renewal pricing changes.
  - Reference: Section 5.1 excerpt.
- [4.1] Fees Non-Refundable — YELLOW
  - Playbook position: Prorated refunds for provider breach or early termination; refunds for unused prepaid fees if service fails.
  - Deviation: Fees are non-refundable except limited prorated termination rights.
  - Impact: Financial exposure if service underperforms or terminates.
  - Escalation trigger: No refund rights tied to provider breach or suspension.
  - Reference: Section 4.1 excerpt.
- [6.3–6.4] Provider Warranty/Remedy — YELLOW
  - Playbook position: Performance/availability warranties with reasonable cure and service credits.
  - Deviation: Only warranty is no material reduction in general functionality; notice within 45 days; remedy limited to restore or terminate/refund.
  - Impact: Limited recourse for performance defects and downtime.
  - Escalation trigger: No SLA/service credits in Order Form or narrow remedy for chronic issues.
  - Reference: Sections 6.3–6.4 excerpts.
- [8.1–8.4] Liability Limits — YELLOW
  - Playbook position: Higher/uncapped liability for IP infringement, confidentiality, and data protection; damages waiver not applied to those.
  - Deviation: General and increased caps unspecified here; damages waiver applies except Increased Claims/confidentiality breaches.
  - Impact: Potentially inadequate recovery for high-impact losses.
  - Escalation trigger: Low cap (e.g., fees paid) or missing carve-outs for data/privacy/IP.
  - Reference: Sections 8.1–8.4 excerpts.
- [5.5] Data Deletion/Return — YELLOW
  - Playbook position: Data return in usable format with transition assistance and defined deletion timelines without request.
  - Deviation: Deletion within 60 days only upon request; no portability/assistance commitments.
  - Impact: Exit friction and data portability risk.
  - Escalation trigger: No data export assistance or format commitments.
  - Reference: Section 5.5 excerpt.
- Missing: Security Controls & Breach Notification — RED
  - Playbook position: Specific security standards, audit/compliance reporting, and defined incident notification timelines.
  - Deviation: No explicit security controls or breach notification timelines beyond DPA placeholder.
  - Impact: Elevated security/compliance risk and unclear incident response duties.
  - Escalation trigger: Absence of concrete security and notification commitments.
  - Reference: Missing clause noted in clause map.
- Missing: SLA/Service Credits — YELLOW
  - Playbook position: Uptime SLA with credits and defined remedies.
  - Deviation: No SLA/service credits in base terms; support only in Order Form.
  - Impact: Limited availability remedies.
  - Escalation trigger: No SLA or credits in Order Form.
  - Reference: Missing clause noted in clause map.
- Missing: Audit/Compliance Rights — YELLOW
  - Playbook position: Audit rights or third‑party compliance reports (e.g., SOC 2/ISO) and data protection reporting.
  - Deviation: No audit/reporting commitments.
  - Impact: Vendor risk management gaps.
  - Escalation trigger: No compliance reports or audit rights available.
  - Reference: Missing clause noted in clause map.
- Missing: Price Increase/Renewal Controls — YELLOW
  - Playbook position: Limits on renewal price increases or mutual agreement.
  - Deviation: No limits on renewal pricing mechanics.
  - Impact: Budget risk on renewal.
  - Escalation trigger: Unilateral price increases at renewal.
  - Reference: Missing clause noted in clause map.
- [9.1] Provider Indemnification Scope — YELLOW
  - Playbook position: Explicit IP infringement indemnity for the service and data.
  - Deviation: Indemnity scope depends on “Provider Covered Claims” (definition not provided here); IP scope unclear.
  - Impact: Uncertain protection for IP infringement or third‑party claims.
  - Escalation trigger: Indemnity excludes IP or data claims.
  - Reference: Section 9.1 excerpt (definition missing).

## Most Material Issues (ordered)
- Customer Content used for AI/ML training (Section 1.6).
- Missing security controls and breach notification timelines.
- Liability cap adequacy and carve-outs for data/privacy/IP (Sections 8.1–8.4).
- Absence of SLA/service credits and performance remedies.
- Suspension rights without clear notice/cure (Section 2.2).

## Assumptions / Open Questions
- Playbook positions were not provided; classifications reflect standard customer‑side SaaS positions.
- Order Form/Key Terms define caps, Non‑Renewal Notice Date, support/SLA, and security addenda.
- DPA exists and contains incident notification timelines and security obligations.
- Definitions of “Provider Covered Claims,” “Increased Claims,” and cap amounts are needed to confirm liability/indemnity scope.

You assist with legal workflows but do not provide legal advice. All analysis should be reviewed by qualified legal professionals before being relied upon.
