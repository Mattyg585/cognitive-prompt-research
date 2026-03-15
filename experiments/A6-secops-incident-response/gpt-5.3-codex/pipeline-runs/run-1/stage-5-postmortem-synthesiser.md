---
model: GPT-5.3-Codex (gpt-5.3-codex)
date: 2026-03-15
experiment: A6
tier: pipeline
run: 1
stage: stage-5-postmortem-synthesiser
---

## Postmortem: Customer Data Exposed via Misconfigured API Endpoint
**Date:** 2026-03-10 | **Duration:** 4h22m (detection to resolution), ~11 days total exposure | **Severity:** SEV1  
**Authors:** Security Engineering, Platform Engineering, Incident Command | **Status:** Draft

### Summary
An API endpoint intended for internal admin use was deployed with `@Public` rather than `@AdminOnly`, exposing 2,847 customer records (name, email, account tier) to unauthenticated requests for ~11 days. The incident was detected externally via responsible disclosure, not internal controls. Once detected, escalation and containment were fast and coordinated. The deeper issue is structural: multiple controls passed, but none verified the failed security property (unauthenticated access denial).

### Impact
- 2,847 records exposed (name, email, account tier)
- No passwords/payment data reported in exposed set
- 23 requests from 4 IPs; 19 successful data-returning requests
- 2 IPs attributed to researcher; 2 unattributed at closure
- Legal: mandatory breach-notification threshold not met; voluntary notification recommended

### Timeline
| Time (UTC) | Event | What Was Known |
|---|---|---|
| Mar 1, 14:00 | Endpoint merged with `@Public` | Endpoint intended for internal use; misannotation not recognized |
| Mar 1, 14:30 | CI/tests/security scan passed | Functional/dependency checks green; auth boundary untested |
| Mar 1, 14:45 | QA validated from authenticated session | Feature behavior looked correct for logged-in user |
| Mar 1, 15:00 | Production deployment | No internal signal of exposure |
| Mar 1–10 | Unauthenticated access occurred | Access events logged but not alerted |
| Mar 10, 09:15 | External disclosure received | First explicit signal of breach |
| Mar 10, 09:45 | Security verified issue | Unauthenticated data access confirmed |
| Mar 10, 10:00 | SEV1 declared | Incident command formalized |
| Mar 10, 10:15 | Annotation hotfix deployed | Proximate defect corrected |
| Mar 10, 10:30 | Fix verified | Active exposure ended |
| Mar 10, 11:00–14:22 | Scoping, legal, comms | Scope clarified, some uncertainty persisted |

### Root Cause Analysis
This incident followed a converging-cause pattern:

1. **Single-point authorization fragility**: a single annotation controlled confidentiality outcome.
2. **Verification blind spot**: no mandatory unauthorized-access tests in CI/QA path.
3. **Detection blind spot**: runtime monitoring lacked confidentiality-focused alerting.

Contributing factors included scope mismatch in “security scan” confidence and minimal review friction around high-impact annotation choices. Human actions were process-conformant for available context; system design failed to provide robust error-catching layers.

### Response Evaluation
**Worked well**
- Fast verification, escalation, and containment once signal existed.
- Effective war-room coordination and legal/comms sequencing.

**Fell short**
- Detection depended on external actor.
- Incident closed with unresolved attribution uncertainty.
- No immediate documented sweep for similar endpoint misconfigurations.

### Action Items
| Action | Owner | Rationale |
|---|---|---|
| Platform-wide unauthenticated probe of customer-data endpoints | AppSec + Platform Eng | Establish whether exposure class is broader than this endpoint |
| Emergency alert on unauthenticated 200 responses for sensitive export routes | Security Engineering | Add immediate confidentiality detection signal |
| Complete formal investigation of unattributed IPs with closure criteria | Security Operations | Resolve material uncertainty in impact interpretation |
| Enforce CI authorization boundary tests for all API endpoints | Platform Engineering | Convert auth-policy violations into build failures |
| Require security approval + justification for `@Public` endpoints | Security + Eng Mgmt | Increase control at high-impact permission choice |
| Add incident “open uncertainty handoff” gate before final closure | Incident Management | Prevent silent loss of unresolved risk threads |
| Move toward secure-by-default endpoint authorization architecture | Platform Architecture | Make common implementation errors fail safe |
| Build confidentiality-focused monitoring program | Security Architecture | Correct availability-heavy observability bias |
| Institute quarterly confidence-vs-coverage control review | Security Governance | Detect overlap-heavy controls that inflate confidence |

### Lessons Learned
**Incident-report facts:** a misannotation exposed data; external disclosure triggered response; containment was rapid once initiated.

**Organizational-learning insights:** this was not primarily a “developer mistake” event. It was a control-system design event where confidence grew as checks passed, yet coverage did not include authorization boundaries. The key pattern is that overlapping controls can produce assurance theater if they test adjacent properties rather than complementary ones.

This postmortem therefore functions as an **organizational-learning artifact**, not only an incident report: it identifies a reusable failure mode (confidence without coverage) and defines structural interventions to reduce recurrence across the platform.

### Remaining Uncertainty
- Attribution and intent for two unknown IPs remain unresolved at time of incident closure.
- Unknown whether additional endpoints currently share similar authorization-risk profile prior to platform-wide sweep completion.
