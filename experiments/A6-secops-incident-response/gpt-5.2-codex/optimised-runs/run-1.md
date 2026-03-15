---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A6
tier: optimised
run: 1
---

## Postmortem: Customer data exposed via misconfigured API endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes | **Severity:** SEV1
**Authors:** Security & Platform Engineering | **Status:** Draft

### Summary
A newly added internal export endpoint was deployed with a public authorization annotation due to an IDE autocomplete mistake. The endpoint was accessible without authentication for ~11 days, exposing 2,847 customer records (name, email, account tier). The issue was reported by a security researcher and resolved within 4 hours 22 minutes of detection, with a hotfix that enforced admin-only access. Two unknown IPs accessed the endpoint; attribution remains unresolved.

### Impact
- **Users affected:** 2,847 customer records exposed (name, email, account tier)
- **Duration of impact:** ~11 days of exposure; 4h 22m from detection to resolution
- **Business impact:** Legal assessment determined regulatory notification threshold not met; voluntary customer notification prepared

### Timeline
| Time (UTC) | Event |
|------------|-------|
| Mar 1, 14:00 | Feature branch merged: new `/api/v2/customers/export` endpoint added; `@Public` used instead of `@AdminOnly`. |
| Mar 1, 14:30 | CI/CD pipeline runs; unit and integration tests pass; dependency-only security scan passes. |
| Mar 1, 14:45 | Deployed to staging; QA validates functionality while authenticated. |
| Mar 1, 15:00 | Deployed to production. |
| Mar 1–10 | Endpoint live and unauthenticated; 23 requests from 4 IPs; 19 returned data. |
| Mar 10, 09:15 | Security researcher emails responsible disclosure with evidence. |
| Mar 10, 09:45 | On-call security engineer verifies and pages incident commander. |
| Mar 10, 10:00 | Incident declared SEV1; war room opened; roles assigned. |
| Mar 10, 10:15 | Hotfix deployed; annotation changed to `@AdminOnly`. |
| Mar 10, 10:30 | Hotfix verified in production; endpoint secured. |
| Mar 10, 11:00 | Log analysis identifies 23 requests; 2 IPs match researcher, 2 unknown. |
| Mar 10, 12:00 | Legal notified; breach assessment begins. |
| Mar 10, 13:00 | Legal advises notification threshold not met; recommends voluntary notice. |
| Mar 10, 14:22 | Incident resolved; customer notification drafted; internal comms sent. |

### Root Cause & Contributing Factors
**Root cause:** An authorization annotation on a new endpoint was misapplied (`@Public` instead of `@AdminOnly`) due to IDE autocomplete, resulting in unauthenticated access in production.

**Contributing factors:**
- No automated checks for unauthenticated endpoints or public annotations
- QA validation performed while authenticated, masking missing authorization
- Security scan focused on dependencies, not authorization configuration
- Lack of WAF/API gateway policy to flag new public endpoints
- Missing runtime authorization monitoring; exposure went undetected for 11 days
- Unattributed access from two unknown IPs; no evidence of further exfiltration beyond logs, but uncertainty remains

**5 Whys (root cause analysis):**
1. **Why** were customer records exposed? → The export endpoint allowed unauthenticated access.
2. **Why** was it unauthenticated? → The endpoint was annotated `@Public` instead of `@AdminOnly`.
3. **Why** was the wrong annotation used? → IDE autocomplete led to a one-character mistake without verification.
4. **Why** wasn’t the mistake caught before release? → Tests and QA validated functionality while authenticated; no negative auth tests or annotation checks existed.
5. **Why** don’t such checks exist? → Authorization verification is not enforced by CI policy, gateway rules, or runtime monitoring.

### Detection & Response
The incident was detected via a responsible disclosure email. The on-call security engineer verified the issue and escalated to the incident commander. A hotfix was deployed within 30 minutes of declaration to enforce admin-only access. Log analysis and legal assessment followed, concluding that regulatory notification thresholds were not met while recommending voluntary notification.

### What Went Well
- Responsible disclosure handled within 30 minutes of receipt
- Hotfix deployed within 30 minutes of incident declaration
- Clear incident roles, war room coordination, and maintained timeline
- Legal engaged early and provided clear guidance

### What Went Poorly
- 11-day exposure window before detection
- Authorization relies on a single-character annotation without verification
- No automated checks for public endpoints or unauthenticated access
- QA testing from authenticated sessions did not detect missing auth
- No WAF or API gateway policy to flag new public endpoints
- Two unknown IPs accessed data; attribution unresolved

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| Add unauthenticated endpoint tests to CI for all APIs | QA Lead | P0 | 2026-04-05 |
| Implement CI check to flag `@Public` annotations for security review | AppSec Lead | P0 | 2026-03-29 |
| Add API gateway/WAF alert on new public endpoints and unauthenticated traffic | SRE Lead | P1 | 2026-04-12 |
| Change default endpoint access to `@AdminOnly` (secure by default) | Platform Eng Lead | P1 | 2026-04-19 |
| Add runtime authorization monitoring with alerts for sensitive endpoints | Security Ops Lead | P1 | 2026-04-26 |
| Update QA checklist to include unauthenticated access validation | QA Lead | P2 | 2026-03-29 |

### Lessons Learned (optional)
Small authorization configuration mistakes can create high-impact exposures. Functional tests alone are insufficient; negative authorization tests and policy checks must be enforced in CI and at the gateway. Detection should not rely on external reports; runtime monitoring is required to identify unauthorized access quickly.
