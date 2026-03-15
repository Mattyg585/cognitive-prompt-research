---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A6
tier: baseline
run: 1
---

## Postmortem: Customer data exposed via misconfigured API endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes | **Severity:** SEV1
**Authors:** Security & Platform Engineering | **Status:** Draft

### Summary
On 2026-03-10, we discovered that a new customer export endpoint was deployed without authentication due to an annotation mistake, exposing limited customer data. The endpoint was publicly accessible for 11 days and was accessed 23 times from 4 IPs. We secured the endpoint within 30 minutes of incident declaration and initiated breach assessment and customer notification planning.

### Impact
- 2,847 customer records (name, email, account tier) were accessible
- Exposure window: ~11 days (Mar 1–Mar 10)
- 23 requests from 4 IPs; 2 IPs unrecognized
- Potential reputational risk and customer trust impact; legal assessment concluded notification not legally required

### Timeline
| Time (UTC) | Event |
|------------|-------|
| Mar 1, 14:00 | Feature branch merged with new `/api/v2/customers/export` endpoint; `@Public` annotation used instead of `@AdminOnly`. |
| Mar 1, 14:30 | CI/CD pipeline passes unit, integration tests; dependency security scan passes. |
| Mar 1, 14:45 | Deployed to staging; QA validates functionality with authenticated test user. |
| Mar 1, 15:00 | Deployed to production. |
| Mar 1–10 | Endpoint live and unauthenticated; 23 requests from 4 IPs, 19 returned data. |
| Mar 10, 09:15 | Security researcher reports unauthenticated access via email. |
| Mar 10, 09:45 | On-call verifies issue and pages incident commander. |
| Mar 10, 10:00 | SEV1 declared; war room opened; roles assigned. |
| Mar 10, 10:15 | Hotfix deployed changing annotation to `@AdminOnly`. |
| Mar 10, 10:30 | Hotfix verified in production; endpoint secured. |
| Mar 10, 11:00 | Log analysis identifies 23 requests, 2 unknown IPs. |
| Mar 10, 12:00 | Legal notified; breach assessment begins. |
| Mar 10, 13:00 | Legal recommends voluntary customer notification. |
| Mar 10, 14:22 | Incident resolved; notifications drafted; internal comms sent. |

### Root Cause
A new admin export endpoint was deployed with a public access annotation due to an IDE autocomplete mistake. The system lacked guardrails to prevent or detect public exposure of sensitive endpoints: no unauthenticated tests, no CI checks for public annotations, and no gateway/WAF policy to flag new public endpoints. As a result, the misconfiguration reached production and remained undetected for 11 days.

### 5 Whys
1. Why were customer records exposed? → The export endpoint allowed unauthenticated access.
2. Why did it allow unauthenticated access? → It was annotated with `@Public` instead of `@AdminOnly`.
3. Why wasn’t the wrong annotation caught before release? → Tests and reviews didn’t verify unauthenticated access and there were no automated checks for public endpoints.
4. Why were those checks missing? → The pipeline focuses on functionality and dependency security, not authorization enforcement.
5. Why is authorization not enforced by default? → The framework requires explicit secure annotations and lacks secure-by-default defaults and policy enforcement.

### What Went Well
- Responsible disclosure was triaged within 30 minutes.
- Hotfix deployed within 30 minutes of SEV1 declaration.
- Incident roles and war room were established quickly.
- Legal engagement was prompt and decisive.

### What Went Poorly
- 11-day detection gap for a public data exposure.
- Single-character annotation mistake had no safeguards.
- QA validated functionality but not authorization.
- No WAF/API gateway rules to alert on new public endpoints.
- Two unknown IPs accessed data and remain unattributed.

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| Add unauthenticated access tests for all API endpoints | QA Lead | P0 | 2026-03-24 |
| Implement CI check to flag any `@Public` endpoint for security review | Security Engineering | P0 | 2026-03-24 |
| Change framework defaults to `@AdminOnly` unless explicitly overridden | API Platform Lead | P1 | 2026-04-07 |
| Add API gateway/WAF rule to alert on new unauthenticated endpoints | SRE Lead | P1 | 2026-04-07 |
| Implement runtime monitoring for anomalous access to admin endpoints | Security Engineering | P1 | 2026-04-14 |
| Review existing endpoints for auth annotation correctness | Platform Engineering | P2 | 2026-04-14 |
| Create guidance and checklist for auth verification in code reviews | Dev Enablement | P2 | 2026-04-21 |

### Lessons Learned
Secure-by-default controls and explicit authorization verification are necessary to prevent simple configuration mistakes from reaching production. Functionality-only testing can mask security gaps, and authorization checks must be automated and enforced. Faster detection requires runtime monitoring and perimeter policies that flag unexpected public access.
