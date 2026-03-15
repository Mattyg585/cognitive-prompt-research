---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A6
tier: pipeline
run: 1
stage: 03-incident-postmortem
---

## Postmortem: Unauthenticated API Endpoint Data Exposure
**Date:** 2026-03-15 | **Duration:** 11 days (March 1 - March 10) | **Severity:** SEV1
**Status:** Draft | **Author:** Postmortem Analyst

### Executive Summary
An internal admin export endpoint (/api/v2/customers/export) was inadvertently deployed with a @Public annotation, exposing 2,847 customer records (names, emails) to unauthenticated access for 11 days. The vulnerability was identified via responsible disclosure by a security researcher and remediated within 30 minutes of verification. No sensitive financial data or PII beyond contact information was exposed.

### Timeline (UTC)
| Time | Event |
|------|-------|
| Mar 1, 14:00 | Feature branch merged with @Public annotation instead of @AdminOnly. |
| Mar 1, 14:30 | CI/CD pipeline passed (unit/integration tests, Snyk dependency scan). |
| Mar 1, 14:45 | QA verified functionality in staging (using authenticated admin session). |
| Mar 1, 15:00 | Deployed to production. Endpoint live and unauthenticated. |
| Mar 10, 09:15 | Security researcher reports vulnerability via email. |
| Mar 10, 09:45 | On-call security engineer verifies vulnerability and pages Incident Commander. |
| Mar 10, 10:00 | Incident declared SEV1. War room opened. |
| Mar 10, 10:15 | Hotfix deployed (annotation changed to @AdminOnly). |
| Mar 10, 10:30 | Hotfix verified. Endpoint secured. |
| Mar 10, 14:22 | Incident resolved. |

### Root Cause Analysis (5 Whys)
1. **Why did the endpoint expose customer data without authentication?**
   Because the endpoint was deployed with a @Public annotation instead of the required @AdminOnly annotation.

2. **Why was the endpoint annotated with @Public?**
   Because the developer selected the wrong annotation (likely via IDE autocomplete error) and this single-word mistake was not caught during code review.

3. **Why did the error persist through CI/CD and QA?**
   Because the automated test suite checks for functionality (happy path) but does not include negative tests to verify access denial for unauthenticated users, and the security scan only checks dependencies.

4. **Why was there no negative testing for authorization?**
   Because the current testing framework and QA process prioritize functional verification from an authenticated context, lacking a standard requirement to explicitly test unauthenticated access attempts.

5. **Why does the framework allow @Public so easily (or why is it not secure-by-default)?**
   Because the application framework relies on explicit opt-in/opt-out annotations for security, meaning a mistake (using a valid but incorrect annotation) defaults to the specified behavior rather than failing closed or requiring a stricter default.

### What Went Well
- **Response Speed:** The vulnerability was patched within 30 minutes of incident declaration.
- **Process:** Incident command structure was established quickly; roles were clearly assigned.
- **Legal Engagement:** Legal team provided rapid guidance on notification requirements, avoiding unnecessary delays.
- **Disclosure Handling:** The report from the security researcher was processed and verified promptly.

### What Went Poorly
- **Detection Time:** The vulnerability persisted for 11 days before detection.
- **Testing Gaps:** QA testing was performed solely with admin privileges, masking the lack of authentication.
- **Tooling Blind Spots:** Security scans and CI checks missed the incorrect annotation; no automated tools flagged the new public endpoint.
- **Monitoring:** No alerts were triggered by the unusual unauthenticated traffic to the new endpoint.

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| Implement automated "negative testing" suite to verify 401/403 responses for unauthenticated users on all endpoints | QA Engineering | P0 | 2026-03-20 |
| Add CI/CD linter rule to flag @Public annotations for mandatory manual security review | DevSecOps | P0 | 2026-03-17 |
| Configure WAF/Gateway to alert on any new endpoint receiving unauthenticated traffic | SRE Team | P1 | 2026-03-25 |
| Evaluate framework changes to enforce "secure by default" (deny all unless explicitly annotated) | Architecture Team | P2 | 2026-04-15 |
