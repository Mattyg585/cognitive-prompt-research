---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A6
tier: optimised
run: 3
---

## Postmortem: Customer data exposed via misconfigured API endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes | **Severity:** SEV1
**Authors:** Incident Commander, Security Lead | **Status:** Draft

### Summary
A misconfigured API endpoint (`/api/v2/customers/export`) was deployed to production with a `@Public` annotation instead of `@AdminOnly`, exposing 2,847 customer records for 11 days. The issue was identified via a responsible disclosure report and remediated via hotfix within 30 minutes.

### Impact
- **Users affected:** 2,847 customer records (name, email, account tier) were exposed to unauthenticated public access.
- **Duration of impact:** 11 days (March 1, 15:00 UTC to March 10, 10:15 UTC).
- **Business impact:** Potential reputational damage. Legal review determined notification threshold was not met, but voluntary notification is recommended. 2 unauthorized IPs remain unattributed.

### Timeline
| Time (UTC) | Event |
|------------|-------|
| **Mar 1, 14:00** | Feature branch merged with `@Public` annotation error. |
| **Mar 1, 14:30** | CI/CD passes (tests only cover functionality, security scan only covers dependencies). |
| **Mar 1, 15:00** | Deployed to production. Endpoint is live and unauthenticated. |
| **Mar 10, 09:15** | Security researcher reports vulnerability to security@company.com. |
| **Mar 10, 09:45** | Security engineer verifies vulnerability; pages Incident Commander. |
| **Mar 10, 10:00** | Incident declared SEV1. War room established. |
| **Mar 10, 10:15** | Hotfix deployed (annotation changed to `@AdminOnly`). Endpoint secured. |
| **Mar 10, 11:00** | Log analysis reveals 23 requests from 4 IPs (2 researcher, 2 unknown). |
| **Mar 10, 12:00** | Legal assessment confirms 2,847 records exposed; no financial/PII beyond email. |
| **Mar 10, 14:22** | Incident resolved. |

### Root Cause Analysis (Drill Down)
*   **Proximal Cause:** Developer selected `@Public` annotation instead of `@AdminOnly` due to an IDE autocomplete error.
*   **Systemic Cause:** The application framework defaults to open access unless explicitly restricted (insecure by default), and the CI/CD pipeline lacks negative testing for authorization.
*   **Process Cause:** QA testing protocols focused exclusively on authenticated functionality ("does it work for admin?") rather than unauthenticated restrictions ("does it fail for public?").

### 5 Whys (Depth Check)
1.  **Why was customer data exposed?**
    Because the `/api/v2/customers/export` endpoint accepted requests without authentication.
2.  **Why did the endpoint accept unauthenticated requests?**
    Because the controller method was annotated with `@Public` instead of `@AdminOnly`.
3.  **Why was the wrong annotation used?**
    The developer made a selection error during autocomplete, and the code review and testing process did not catch it.
4.  **Why did testing not catch the error?**
    The automated test suite runs as an authenticated user to verify functionality, and there are no "negative tests" to verify that unauthenticated users are blocked.
5.  **Why does the system allow a single annotation error to expose data?**
    Because the security model relies on explicit opt-in for protection (developers must add `@AdminOnly`) rather than explicit opt-out (secure by default), and no static analysis exists to flag `@Public` usage.

### What Went Well
- **Response Speed:** Hotfix was deployed 30 minutes after incident declaration.
- **External Handling:** Responsible disclosure from the researcher was triaged immediately (30 mins from email to paging).
- **Process:** Roles were clearly assigned, and Legal was engaged early for accurate risk assessment.

### What Went Poorly
- **Detection Time:** The vulnerability persisted for 11 days before detection.
- **Tooling Gaps:** Security scans (Snyk) checked dependencies but missed application logic flaws; CI/CD passed despite the vulnerability.
- **Testing Blind Spot:** QA and automated tests only verified the "happy path" (authorized access), completely missing the "sad path" (unauthorized access).
- **Unattributed Access:** Two unknown IPs accessed the data, meaning we cannot rule out malicious exfiltration.

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| **Implement "Secure by Default"**<br>Refactor framework so endpoints are private/admin-only by default, requiring explicit `@Public` annotation to open them. | Platform Engineering | P0 | 2026-04-01 |
| **Add Negative Authorization Tests**<br>Create a test suite that attempts to access all endpoints as an unauthenticated user and asserts 401/403 response. | QA Lead | P0 | 2026-03-20 |
| **Add Static Analysis for `@Public`**<br>Add a CI linter rule that flags any new usage of `@Public` for manual security review. | DevSecOps | P1 | 2026-03-25 |
| **Implement WAF Alerting**<br>Configure WAF to alert on new endpoints receiving unauthenticated traffic. | SRE Team | P1 | 2026-03-30 |
| **Runtime Authorization Monitoring**<br>Investigate tools to monitor for anomalies in authorization patterns (e.g., admin endpoints accessed without tokens). | Security Team | P2 | 2026-04-15 |

### Lessons Learned
- **Tests must verify failure modes:** It is as important to test that the system fails when it should (unauthorized access) as it is to test that it succeeds when allowed.
- **Annotations are brittle:** A single-character difference in code should not result in a SEV1 data breach. Security controls should be deeper in the stack (gateway/middleware) or secure by default.
- **Dependency scanning is not enough:** Scanning `package.json` gives a false sense of security; we need analysis of our own code logic.
