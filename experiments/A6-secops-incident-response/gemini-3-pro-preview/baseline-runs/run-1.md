---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A6
tier: baseline
run: 1
---

## Postmortem: Customer data exposed via misconfigured API endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes | **Severity:** SEV1
**Authors:** Incident Commander, Security Lead | **Status:** Draft

### Summary
An internal administrative endpoint (`/api/v2/customers/export`) was inadvertently exposed to the public internet due to a misconfigured `@Public` annotation instead of `@AdminOnly`. This resulted in the potential exposure of 2,847 customer records (name, email, account tier) to unauthenticated requests for a period of 11 days. The issue was identified via responsible disclosure and remediated by correcting the annotation.

### Impact
- **Users affected:** 2,847 customer records potentially accessed (name, email, account tier).
- **Duration of impact:** 11 days (March 1 to March 10).
- **Business impact:** Potential reputational damage. Legal assessment confirmed no financial or sensitive PII (passwords/payment info) was exposed, and mandatory notification thresholds were not met, though voluntary notification is recommended.

### Timeline
| Time (UTC) | Event |
|------------|-------|
| Mar 1, 14:00 | Feature branch merged with `/api/v2/customers/export` endpoint using `@Public` instead of `@AdminOnly`. |
| Mar 1, 14:30 | CI/CD pipeline runs. Unit tests, integration tests, and Snyk security scan pass (scans checked dependencies, not auth logic). |
| Mar 1, 14:45 | Deployed to staging. QA verifies functionality as authenticated user; no negative testing for unauthenticated access performed. |
| Mar 1, 15:00 | Deployed to production. Endpoint becomes live and unauthenticated. |
| Mar 1–10 | Endpoint receives 23 requests from 4 unique IPs (19 successful, 4 empty). |
| Mar 10, 09:15 | Security researcher emails report of exposed endpoint to security team. |
| Mar 10, 09:45 | On-call security engineer verifies vulnerability and pages Incident Commander. |
| Mar 10, 10:00 | Incident declared SEV1. War room opened. |
| Mar 10, 10:15 | Engineering identifies `@Public` annotation error. Hotfix deployed changing it to `@AdminOnly`. |
| Mar 10, 10:30 | Hotfix verified. Endpoint returns 401 for unauthenticated requests. |
| Mar 10, 11:00 | Log analysis identifies 23 requests: 2 IPs match researcher, 2 IPs are unknown. |
| Mar 10, 12:00 | Legal notified. Breach assessment confirms 2,847 records exposed but no sensitive financial/PII data. |
| Mar 10, 13:00 | Legal advises notification threshold not met; recommends voluntary notification. |
| Mar 10, 14:22 | Incident resolved. Customer notification drafted. Internal comms sent. |

### Root Cause
The incident was caused by a developer error where the `@Public` annotation was used instead of `@AdminOnly` due to an IDE autocomplete mistake. This error propagated to production because the existing CI/CD pipeline, security scans, and QA processes lacked specific checks for authorization logic on new endpoints, and the application framework is not secure-by-default.

### 5 Whys
1. **Why was customer data exposed?**
   Because the `/api/v2/customers/export` endpoint was accessible to unauthenticated users.
2. **Why was the endpoint accessible to unauthenticated users?**
   Because it was deployed with the `@Public` annotation instead of `@AdminOnly`.
3. **Why was the wrong annotation used?**
   Because the developer selected the wrong autocomplete option in the IDE, and the difference is only one character/word.
4. **Why was this error not detected before production?**
   Because code review missed the annotation change, security scans only checked dependencies, and QA testing was performed by an authenticated user without negative testing (unauthenticated access).
5. **Why is it possible to accidentally expose an endpoint so easily?**
   Because the framework requires developers to explicitly add authorization annotations rather than defaulting to a secure state (deny-all) that requires explicit overrides.

### What Went Well
- **Response Time:** Security researcher's disclosure was handled within 30 minutes.
- **Remediation:** Hotfix was deployed and verified within 30 minutes of incident declaration.
- **Process:** Roles were clearly assigned, and the war room operated effectively.
- **Legal Support:** Legal team provided rapid assessment and guidance regarding notification obligations.

### What Went Poorly
- **Detection Latency:** The vulnerability persisted for 11 days before being reported by an external researcher.
- **Tooling Gaps:** Security scans and CI/CD checks failed to flag the dangerous `@Public` annotation.
- **Testing Gaps:** QA processes focused on functionality (happy path) rather than security controls (negative testing).
- **Unknown Access:** Two of the four IPs that accessed the data remain unidentified/unattributed.
- **Defense in Depth:** No WAF rules or API gateway policies were in place to flag or block new public endpoints.

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| Implement automated negative testing suite to verify all endpoints reject unauthenticated access unless whitelisted. | QA Lead | P0 | 2026-03-17 |
| Add CI/CD static analysis rule to flag or block PRs introducing `@Public` annotations for manual security review. | DevOps Lead | P0 | 2026-03-15 |
| Configure WAF to alert on traffic to newly detected public endpoints. | Security Engineer | P1 | 2026-03-20 |
| Conduct forensic analysis on the two unknown IPs to determine intent. | Security Team | P1 | 2026-03-12 |
| Evaluate framework changes to enforce "secure by default" (e.g., `@AdminOnly` as implicit default). | Architecture Lead | P2 | 2026-04-01 |

### Lessons Learned
- **Secure Defaults:** Relying on manual developer annotations for critical security controls is error-prone; systems should default to the most secure state.
- **Negative Testing:** Testing must include "unhappy paths," specifically checking that unauthorized users *cannot* access restricted resources.
- **Static Analysis:** Simple grep-like checks in CI (e.g., for `@Public`) can catch high-impact human errors that sophisticated security scanners might miss.
- **Runtime Monitoring:** We need better visibility into new public endpoints to detect exposure faster than 11 days.
