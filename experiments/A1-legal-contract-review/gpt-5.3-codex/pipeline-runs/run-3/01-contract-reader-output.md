---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A1
tier: pipeline
run: 3
stage: 01-contract-reader
---

## Contract Overview
- Type: SaaS cloud service agreement (Common Paper v2.1 framework + cover-page variables)
- User side: Customer/buyer
- Commercial structure: subscription access + support; obligations distributed through Standard Terms + Order Forms

## Material Clause Summaries

### Data rights stack
- Section 1.5 grants service-operation rights over Customer Content.
- Section 1.6 separately authorizes ML training on Usage Data and Customer Content, including third-party components, with aggregation/de-identification qualifiers.
- Section 5.6 lists 1.6 as surviving termination.

### Privacy/security layer
- Section 3.1 requires DPA before submitting GDPR-governed personal data.
- Standard terms do not independently set breach-notice timeline, audit channel, or processor-change mechanics.

### Service continuity layer
- Section 2.2 allows suspension for payment/restriction breaches or material impact on product/others.
- Notice is discretionary ("try to inform"), and reinstatement timing is not specific.

### Liability/remedy layer
- Section 8 uses General Cap / Increased Cap / Unlimited Claims architecture.
- Actual cap values and claim mapping are cover-page variables not present in this text.

### Exit and transfer layer
- Section 5.5(b): deletion within 60 days upon customer request.
- Section 12.6: assignment allowed with consent exceptions for merger/acquisition/change of control.

## Unusual or Non-Standard Provisions
- Explicit ML training authorization over Customer Content.
- Survival of data-use-heavy provisions post-termination.
- Strongly variable economic/risk posture via undefined cover-page terms.

## Notable Absences
- No explicit uptime/service-credit commitment in the provided terms.
- No detailed provider-side security baseline in the provided terms.

## Material Interactions
- 1.6 + 5.6: model-training rights can persist after contract end.
- 1.6 + 12.6: assignment flexibility may change who ultimately benefits from trained models.
- 2.2 + payment obligations: suspension and billing may continue in parallel.

## Reader Observation
Assignment flexibility plus surviving data-use rights creates transfer-of-control risk.
