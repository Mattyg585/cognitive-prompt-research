---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A6
tier: optimised
run: 1
---

## Postmortem: Customer data exposed via misconfigured API endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes (detected to resolved) | **Severity:** SEV1
**Authors:** Incident Commander, Security Engineer | **Status:** Draft

### Summary
A misconfigured API endpoint (`/api/v2/customers/export`) exposed 2,847 customer records (name, email, account tier) to unauthenticated access for 11 days. The issue was identified via a responsible disclosure report and remediated within 30 minutes of verification by changing the `@Public` annotation to `@AdminOnly`.

### Impact
- **Users affected**: 2,847 customer records accessible (name, email, account tier).
- **Duration of impact**: 11 days (March 1 - March 10).
- **Business impact**: Potential reputational damage. Legal assessment confirmed no mandatory notification threshold met (no financial/PII beyond email), but voluntary notification recommended.

### Timeline
| Time (UTC) | Event |
|------------|-------|
| Mar 1, 14:00 | Feature branch merged with `@Public` annotation instead of `@AdminOnly` due to IDE autocomplete error. |
| Mar 1, 14:30 | CI/CD pipeline passes (unit, integration, Snyk security scan). No authorization checks performed. |
| Mar 1, 14:45 | Deployed to staging. QA verifies functionality as authenticated user; no unauthenticated access tests performed. |
| Mar 1, 15:00 | Deployed to production. Endpoint becomes live and unauthenticated. |
| Mar 1–10 | Endpoint exposed. 23 requests from 4 IPs recorded (19 returned data, 4 empty). |
| Mar 10, 09:15 | Security researcher reports vulnerability to `security@company.com`. |
| Mar 10, 09:45 | Security engineer verifies vulnerability and pages Incident Commander. |
| Mar 10, 10:00 | Incident declared SEV1. War room opened. |
| Mar 10, 10:15 | Hotfix deployed (annotation changed to `@AdminOnly`). Endpoint returns 401. |
| Mar 10, 10:30 | Hotfix verified. Endpoint secured. |
| Mar 10, 11:00 | Log analysis identifies 4 IPs (2 attributed to researcher, 2 unknown). |
| Mar 10, 12:00 | Legal assessment confirms 2,847 records exposed. |
| Mar 10, 13:00 | Legal advises voluntary notification. |
| Mar 10, 14:22 | Incident resolved. Internal comms sent. |

### Root Cause Analysis (Drill Down)
*   **Proximal Cause**: Developer selected `@Public` instead of `@AdminOnly` due to an IDE autocomplete error.
*   **Systemic Cause**: The application framework uses an "opt-in security" model where endpoints are public unless explicitly secured, rather than "secure by default."
*   **Process Cause**: CI/CD pipelines and QA processes tested for functionality (presence of feature) but not for security constraints (absence of access for unauthenticated users).

### 5 Whys (Depth Check)
1.  **Why was customer data exposed?**
    Because the `/api/v2/customers/export` endpoint was accessible without authentication.
2.  **Why was it accessible without authentication?**
    Because the code was annotated with `@Public` instead of `@AdminOnly`.
3.  **Why was the incorrect annotation used?**
    Because the developer made a one-character autocomplete mistake in the IDE, and the framework allows `@Public` without additional validation.
4.  **Why was the error not caught in review or testing?**
    Because unit tests, integration tests, and QA manual tests were all performed as authenticated users to verify the feature worked. No negative tests existed to verify that unauthenticated users *could not* access it.
5.  **Why is there no automated check for unauthenticated access?**
    Because our security scanning (Snyk) checks dependencies, not application logic, and we lack a comprehensive suite of negative authorization tests in our CI pipeline.

### What Went Well
- Security researcher's responsible disclosure was handled within 30 minutes.
- Hotfix deployed in 30 minutes from incident declaration.
- Clean incident response process — roles assigned, war room functional, timeline maintained.
- Legal engaged early and provided clear guidance on notification requirements.

### What Went Poorly
- 11-day exposure window — nobody noticed for over a week.
- Authorization annotation is a single-character difference (`@Public` vs `@AdminOnly`) with no compile-time or test-time verification.
- No automated check for unauthenticated endpoints — the security scan checks dependencies only.
- QA tested functionality but not authorization — testing from an authenticated session can't catch missing auth.
- No WAF rule or API gateway policy that flags new public endpoints.
- Two unknown IPs accessed data and have not been attributed.

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| Add authorization test suite that specifically tests each endpoint from an unauthenticated session (negative testing). | QA Lead | P0 | 2026-03-20 |
| Add CI check (linter/static analysis) that flags any endpoint with `@Public` annotation for mandatory manual security review. | DevEx Lead | P1 | 2026-03-17 |
| Implement WAF rule to alert on new endpoints receiving unauthenticated traffic to detect exposure windows earlier. | SecOps Lead | P1 | 2026-03-25 |
| Evaluate refactoring framework to `@AdminOnly` by default (Secure by Default) to prevent opt-in security errors. | Platform Architect | P2 | 2026-04-15 |

### Lessons Learned
- **Test for the negative:** Functionality testing proves it works; security testing must prove it *doesn't* work for the wrong people.
- **Secure by default is critical:** Relying on developers to remember to add security annotations is a single point of failure.
- **Runtime observability:** We cannot rely solely on pre-deployment checks; we need to know when a new public endpoint appears in production traffic.
