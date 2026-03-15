---
model: GPT-5.3-Codex (gpt-5.3-codex)
date: 2026-03-15
experiment: A6
tier: optimised
run: 1
---

## Postmortem: Customer Data Exposed via Misconfigured API Endpoint
**Date:** 2026-03-10 | **Duration:** 11-day exposure, 4h22m detection-to-resolution | **Severity:** SEV1  
**Authors:** Security Engineering, Platform Engineering, Incident Command | **Status:** Draft

### Summary
An internal export endpoint was deployed with `@Public` instead of `@AdminOnly`, exposing customer data to unauthenticated requests for 11 days. The issue was not detected by internal controls; it was discovered by external responsible disclosure. Once reported, verification, escalation, containment, and legal/comms steps were executed quickly. The incident reveals a control-design gap: confidence accumulated across checks without authorization coverage actually expanding.

### Impact
- 2,847 records exposed (name, email, account tier)
- Exposure window: Mar 1, 15:00 UTC to Mar 10, 10:30 UTC
- 23 total requests from 4 IP addresses; 19 returned customer data
- 2 IPs are attributable to the researcher; 2 remain unattributed
- No password/payment/sensitive financial fields exposed
- Mandatory legal notification threshold not met; voluntary notice recommended

### Timeline
| Time (UTC) | Event | What Was Known |
|---|---|---|
| Mar 1, 14:00 | Endpoint merged with `@Public` annotation | Team believed endpoint was configured correctly |
| Mar 1, 14:30 | CI + tests + Snyk all passed | Checks confirmed functionality/dependency hygiene; auth boundary remained untested |
| Mar 1, 14:45 | QA passed in staging from authenticated session | Correct behavior for authenticated users observed; unauthenticated behavior unknown |
| Mar 1, 15:00 | Production deploy | No indicators of misconfiguration |
| Mar 1–10 | Endpoint served unauthenticated traffic | Logs recorded requests, but no rule interpreted them as security signal |
| Mar 10, 09:15 | Researcher disclosure received | First explicit signal of exposure |
| Mar 10, 09:45 | Security on-call verified issue | Confirmed unauthenticated access to customer export |
| Mar 10, 10:00 | SEV1 declared, war room opened | Incident command structure activated |
| Mar 10, 10:15 | Hotfix deployed (`@AdminOnly`) | Proximate defect identified and patched quickly |
| Mar 10, 10:30 | Hotfix verified in production | Active exposure ended |
| Mar 10, 11:00–14:22 | Log analysis, legal review, comms drafting | Scope clarified; some uncertainty remained (2 unattributed IPs) |

### Root Cause Analysis
This incident is best modeled as **converging causal branches**, not a single line.

1. **Single-point authorization control**  
   Endpoint access policy was encoded in a single annotation. One selection error changed confidentiality behavior with no independent guardrail.

2. **Coverage gap across verification checkpoints**  
   Unit tests, integration tests, and QA validated “does feature work for allowed users?” but not “is access denied for unauthenticated users?”

3. **Security tooling scope mismatch**  
   Snyk pass result was valid for dependency risk, but unrelated to authorization correctness. “Security scan passed” carried broader confidence than the scan’s scope justified.

4. **No runtime confidentiality detection layer**  
   Request logs contained evidence of unauthorized exposure, but no detection logic translated those events into an alert.

5. **Human decision context was under-supported**  
   IDE autocomplete + permissive default + missing review constraints made a high-impact mis-selection plausible and hard to detect in normal workflow.

### Response Evaluation
**What worked**
- Fast escalation and containment once disclosure arrived
- Clear incident command operations
- Rapid legal engagement and practical comms planning

**What fell short**
- Detection was externally triggered, not internally assured
- No explicit handoff from “incident contained” to “extended uncertainty resolution”
- Two unattributed IPs remained unresolved at closure

### Action Items
| Action | Owner | Rationale |
|---|---|---|
| Add CI authorization boundary tests for all endpoints from unauthenticated context | Platform Engineering | Directly closes verification branch gap |
| Require mandatory security review + justification for every `@Public` endpoint | Security + Eng Leads | Reduces silent high-impact annotation risk |
| Implement alerting for unauthenticated 200 responses on sensitive endpoints | Security Engineering | Adds runtime confidentiality detection layer |
| Audit all existing endpoints for authorization-intent mismatch | AppSec | Checks whether this is isolated or systemic |
| Scope migration to secure-by-default endpoint policy | Platform Architecture | Converts likely human slips into safe failure mode |
| Continue attribution work on two unknown IPs with formal closure criteria | Security Operations | Resolves uncertainty that affects impact interpretation |

### Lessons Learned
The key failure was not response speed; it was **control architecture**. Multiple checkpoints passed, yet none measured the failed property (unauthenticated access). This incident also shows a recurrent pattern in security operations: controls can create confidence faster than they create coverage. Post-incident improvement should therefore prioritize breadth and complementarity of controls, not just the count of controls.
