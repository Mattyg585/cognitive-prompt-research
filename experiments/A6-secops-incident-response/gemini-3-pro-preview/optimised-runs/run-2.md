---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A6
tier: optimised
run: 2
---

## Postmortem: Customer Data Exposure via Misconfigured API Endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes (response), 11 days (exposure) | **Severity:** SEV1
**Authors:** Incident Response Team | **Status:** Draft

### Summary
An internal admin export endpoint (`/api/v2/customers/export`) was inadvertently deployed with a `@Public` annotation instead of `@AdminOnly`, exposing 2,847 customer records to unauthenticated access. The vulnerability persisted for 11 days before a responsible disclosure by a security researcher led to a hotfix. While no sensitive PII (passwords/payment) was exposed, 23 unauthorized requests were logged, including 2 from unidentified sources.

### Impact
- **Users affected:** 2,847 customer records (Name, Email, Account Tier) were accessible.
- **Duration of impact:** 11 days (March 1 to March 10).
- **Business impact:** Potential reputational damage; legal assessment confirmed no mandatory notification threshold was met, but voluntary notification was recommended and drafted.

### Timeline
| Time (UTC) | Event |
|------------|-------|
| Mar 1, 14:00 | Feature branch merged with `@Public` annotation error on new endpoint. |
| Mar 1, 14:30 | CI/CD passes; automated tests verified functionality but not access restrictions. |
| Mar 1, 14:45 | Staging deployment; QA verified functionality using authenticated accounts. |
| Mar 1, 15:00 | Production deployment; endpoint becomes live and unauthenticated. |
| Mar 1–10 | Endpoint is active. Logs show 23 requests (19 successful) from 4 IPs. |
| Mar 10, 09:15 | Security researcher reports vulnerability via email. |
| Mar 10, 09:45 | Security engineer verifies issue and pages Incident Commander. |
| Mar 10, 10:00 | SEV1 declared. War room opened. |
| Mar 10, 10:15 | Hotfix deployed (annotation changed to `@AdminOnly`). |
| Mar 10, 10:30 | Hotfix verified; endpoint secured. |
| Mar 10, 11:00 | Log analysis identifies 2 unknown IPs accessed data. |
| Mar 10, 14:22 | Incident resolved. |

### Root Cause Analysis (Drill Down)
*   **Proximal Cause:** The developer applied the `@Public` annotation instead of `@AdminOnly` due to an autocomplete error.
*   **Systemic Cause:** The application framework treats annotations as "secure by configuration" rather than "secure by default"—a single keyword slip defaults to open access.
*   **Process Cause:** The testing strategy focused exclusively on "happy path" functionality (authenticated users succeeding) and lacked negative testing (unauthenticated users failing).

### 5 Whys (Depth Check)
1.  **Why was customer data exposed?** Because the API endpoint allowed unauthenticated access.
2.  **Why did the endpoint allow unauthenticated access?** Because it was annotated with `@Public`.
3.  **Why was it annotated with `@Public`?** Because the developer selected the wrong autocomplete option, and peer review missed the single-word error.
4.  **Why was the error not caught in CI/CD or QA?** Because the test suite only checked if the endpoint returned data for authorized users, not if it blocked unauthorized ones.
5.  **Why were there no negative tests for unauthorized access?** Because the engineering process does not mandate specific security integration tests for new endpoints, relying instead on a dependency scanner (Snyk) that cannot detect logical misconfigurations.

### What Went Well
- **Response Time:** 30 minutes from verification to fix deployment.
- **Process:** Roles were assigned quickly, and the war room was effective.
- **Legal Support:** Legal provided rapid assessment of notification obligations.

### What Went Poorly
- **Detection:** 11-day lag time; reliance on external researcher rather than internal monitoring.
- **Tooling:** Security scans passed despite the vulnerability.
- **Attribution:** Inability to identify 2 of the 4 IPs that accessed the data.

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| Implement mandatory "negative testing" (verify 401/403) for all new endpoints in CI | QA Lead | P0 | 2026-03-15 |
| Create linter rule to flag `@Public` usage for manual security review | DevExp Lead | P1 | 2026-03-17 |
| Evaluate "Secure by Default" framework (fail closed if no annotation present) | Platform Arch | P1 | 2026-04-01 |
| Configure WAF to alert on traffic to new unauthenticated endpoints | SecOps | P2 | 2026-03-20 |

### Lessons Learned
- **Tests must prove failure:** It is as important to prove that unauthorized users *cannot* access data as it is to prove that authorized users *can*.
- **Defaults matter:** Security should not rely on a developer typing the correct word; it should rely on the absence of the correct word resulting in a secure state.
- **Scanners are not enough:** Static analysis of dependencies (Snyk) does not replace logical security testing of application code.