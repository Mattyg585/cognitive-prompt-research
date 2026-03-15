---
model: GPT-5.2
date: 2026-03-15
experiment: A6
tier: baseline
run: 1
---

## Postmortem: Customer data exposed via misconfigured API endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes (detected → resolved) | **Severity:** SEV1
**Authors:** Security (On-call), Platform Eng, Incident Commander | **Status:** Draft

### Summary
On Mar 10, 2026 we confirmed that a customer export API endpoint (`/api/v2/customers/export`) could be accessed without authentication due to an authorization annotation misconfiguration introduced on Mar 1. The endpoint exposed limited customer data (name, email, account tier) and was reachable for ~11 days before responsible disclosure. We mitigated by deploying a hotfix to enforce admin-only access and initiated breach assessment and customer communications.

### Impact
- **Users affected:** 2,847 customer records were accessible via an unauthenticated API endpoint
- **Duration of impact:** ~11 days of exposure window (Mar 1–Mar 10); 4h 22m from detection to mitigation/incident resolution activities
- **Business impact:** Security incident requiring SEV1 response, legal review, and customer notification drafting; potential reputational risk. No passwords, payment information, or sensitive personal data were exposed.

### Timeline
| Time (UTC) | Event |
|------------|-------|
| Mar 1, 14:00 | Feature branch merged adding new `/api/v2/customers/export` endpoint for internal admin dashboard. Authorization annotation set to `@Public` instead of `@AdminOnly` due to IDE autocomplete error. |
| Mar 1, 14:30 | CI/CD runs: 247 unit tests pass; integration tests pass. Snyk dependency scan passes (does not evaluate endpoint authorization). |
| Mar 1, 14:45 | Deployed to staging. QA validates export functionality while authenticated; authorization requirement not explicitly tested. |
| Mar 1, 15:00 | Deployed to production. |
| Mar 1–Mar 10 | Endpoint remains unauthenticated. Logs later show 23 requests from 4 unique IPs; 19 returned 200 OK with customer data; 4 returned empty results. |
| Mar 10, 09:15 | Security researcher emails security@company.com with responsible disclosure and evidence of unauthenticated access. |
| Mar 10, 09:45 | On-call security engineer verifies the issue and pages the incident commander. |
| Mar 10, 10:00 | Incident declared SEV1; Slack war room opened; roles assigned; timeline tracking begins. |
| Mar 10, 10:15 | Engineering identifies incorrect `@Public` annotation. Hotfix prepared and deployed changing to `@AdminOnly`. |
| Mar 10, 10:30 | Hotfix verified in production; unauthenticated requests now receive 401; endpoint secured. |
| Mar 10, 11:00 | Security begins log analysis; 23 requests from 4 IPs identified. 2 IPs match the researcher; 2 IPs remain unknown/unattributed. |
| Mar 10, 12:00 | Legal notified; breach assessment initiated. 2,847 records confirmed exposed (name, email, account tier only). |
| Mar 10, 13:00 | Legal determines statutory notification threshold not met (no sensitive/financial data). Recommends voluntary customer notification as best practice. |
| Mar 10, 14:22 | Incident declared resolved; customer notification drafted; internal communications sent. |

### Root Cause
A new internal admin export endpoint was deployed to production with an explicit `@Public` authorization annotation instead of `@AdminOnly`. The authorization model relied on developer-specified annotations with a minimal, easily-confused difference and lacked automated verification (compile-time checks, CI tests, or runtime monitoring) to detect unintended public exposure. QA validated functionality in authenticated contexts but did not test unauthenticated access, allowing the misconfiguration to ship and persist until external discovery.

### 5 Whys
1. Why were customer records accessible without authentication? → Because `/api/v2/customers/export` was marked `@Public`, allowing unauthenticated requests to receive data.
2. Why was the endpoint marked `@Public`? → Because the developer selected `@Public` via IDE autocomplete instead of `@AdminOnly` (a one-character difference).
3. Why wasn’t this caught before deployment? → Because existing unit/integration tests validated functional behavior with authenticated users and did not include unauthenticated authorization checks for endpoints.
4. Why didn’t tooling or CI flag a public admin export endpoint? → Because security scanning focused on dependency vulnerabilities and there was no policy/linter/check to require review or explicit justification for `@Public` endpoints.
5. Why did the system allow an insecure-by-default configuration to reach production and remain undetected? → Because authorization defaults and guardrails were insufficient (annotation-driven access control without fail-closed defaults, coverage gaps in QA/security testing, and limited monitoring/alerting for unauthenticated access to sensitive routes).

### What Went Well
- Responsible disclosure intake was handled quickly (verified and escalated within ~30 minutes).
- Hotfix was deployed rapidly (~30 minutes from incident declaration) and verified in production.
- Incident response process was effective: war room established, roles assigned, and timeline maintained.
- Legal was engaged early and provided clear guidance on notification requirements and best-practice communication.

### What Went Poorly
- The endpoint was exposed for ~11 days before detection; internal monitoring did not surface the issue.
- Authorization control depended on a fragile annotation choice with no automated verification.
- QA testing in authenticated sessions did not catch missing authentication/authorization.
- No WAF/API gateway controls or alerts existed to flag new public endpoints or unusual unauthenticated access to data-export routes.
- Two unknown IPs accessed the endpoint; attribution is incomplete and we cannot conclusively determine malicious exfiltration beyond observed log entries.

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| Implement an automated unauthenticated-access test suite for all API routes (including “must return 401/403” assertions) and require it in CI. | Platform Eng Lead | P0 | 2026-03-24 |
| Add a CI policy check that fails builds when `@Public` is used on routes under `/api/v2/` unless an approved allowlist/justification exists. | Security Engineering | P0 | 2026-03-20 |
| Change authorization defaults to fail-closed (e.g., endpoints are non-public unless explicitly declared with reviewed policy) and make admin endpoints require explicit `@AdminOnly` or equivalent role policy. | Application Architecture | P0 | 2026-04-15 |
| Add API gateway/WAF rules and alerts for unauthenticated access to export/administrative endpoints, including detection of new public routes and anomalous request patterns. | SecOps | P1 | 2026-04-01 |
| Add static analysis/lint rule to detect suspicious combinations (e.g., `export` endpoints annotated `@Public`) and surface as PR checks. | Developer Experience (DevEx) | P1 | 2026-04-08 |
| Update QA test plans to include explicit authorization verification for new endpoints (authenticated vs unauthenticated, least-privilege roles). | QA Manager | P1 | 2026-03-31 |
| Improve log retention, queryability, and alerting for sensitive endpoints (including dashboards for 401/200 rates by endpoint and source IP). | Observability Team | P2 | 2026-04-22 |
| Complete follow-up investigation on the two unknown IPs (ISP lookups, correlation with other logs, evaluate need for additional voluntary notification language). | Security (On-call Rotation) | P1 | 2026-03-22 |

### Lessons Learned
- “Secure by default” must be enforced by platform guardrails, not left to individual annotation choices.
- AuthZ testing needs explicit negative tests (unauthenticated and least-privileged role scenarios), not only happy-path functional coverage.
- Dependency scanning is necessary but not sufficient; policy-as-code for access control and runtime monitoring are required to reduce exposure windows.
- Fast mitigation and clear incident roles materially reduce harm, but prevention and early detection are the priority for data exposure scenarios.
