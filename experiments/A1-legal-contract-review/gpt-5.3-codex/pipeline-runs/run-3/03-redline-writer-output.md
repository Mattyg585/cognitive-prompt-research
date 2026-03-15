---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A1
tier: pipeline
run: 3
stage: 03-redline-writer
---

## Redline Package

### Section 1.6 (Machine Learning)
**Current language**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models... including third-party components..."

**Proposed redline**: "Provider may use aggregated and de-identified Usage Data to improve the Product. Provider will not use Customer Content to train or enhance machine learning or AI models unless Customer provides prior written opt-in consent, which Customer may revoke on thirty (30) days' notice. Provider will not use Customer Content or Usage Data to train third-party AI/ML models without Customer's prior written consent."

**Rationale**: Preserves product-improvement telemetry while restoring customer control over content-derived model training.
**Priority**: Must-have
**Fallback**: Usage Data only (no Customer Content), no third-party model training.

### Section 3.1 / new security clause
**Current language**: DPA required before GDPR-governed personal data submission.

**Proposed redline**: "The parties will execute a DPA at signing and include breach-notice timing, sub-processor notice, and security-assurance reporting obligations."

**Rationale**: Converts high-level privacy reference into enforceable operating commitments.
**Priority**: Must-have
**Fallback**: DPA execution at signature + breach-notice SLA + annual assurance report sharing.

### Section 2.2 (Suspension)
**Current language**: Provider may suspend with or without notice; will try to inform when practical.

**Proposed redline**: "Provider will provide prior written notice and cure opportunity before suspension, except in immediate security emergencies. For emergency suspension, Provider will notify Customer within 24 hours and restore service promptly after cure."

**Rationale**: Protects operational continuity while preserving emergency response rights.
**Priority**: Should-have
**Fallback**: Emergency-only immediate suspension + mandatory prompt notice.

### Section 8 / Cover Page variables
**Current language**: Liability cap tiers exist but values are unresolved in provided text.

**Proposed redline**: "Set General Cap at not less than twelve (12) months of fees; map confidentiality/privacy/security incidents to enhanced-cap tier."

**Rationale**: Makes remedy economics explicit before execution.
**Priority**: Should-have
**Fallback**: Lower cap floor acceptable only if enhanced claims remain robust.

### Section 5.5 (Data return/deletion)
**Current language**: Delete on request within 60 days.

**Proposed redline**: "On termination, Provider will make Customer Content available in a machine-readable export format and then certify deletion within an agreed timeline."

**Rationale**: Supports migration and controlled data offboarding.
**Priority**: Should-have
**Fallback**: Keep 60-day window but require export + deletion certification.
