---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A6
tier: pipeline
run: 3
stage: 03-incident-postmortem
---

## Postmortem: Customer data exposed via misconfigured API endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes | **Severity:** SEV1
**Status:** Draft | **Author:** Postmortem Analyst

### Executive Summary
On March 10, 2026, a security researcher reported that the `/api/v2/customers/export` endpoint was accessible without authentication, exposing 2,847 customer records (names, emails, account tiers). The incident was caused by a misconfigured `@Public` annotation on a new endpoint deployed 11 days prior. The issue was resolved via a hotfix within 30 minutes of verification.

### Timeline (UTC)
| Time | Event |
|------|-------|
| **Mar 1, 14:00** | Feature branch merged with `/api/v2/customers/export` endpoint using `@Public` annotation. |
| **Mar 1, 14:30** | CI/CD pipeline passed; tests and security scans did not flag the missing auth check. |
| **Mar 1, 15:00** | Endpoint deployed to production. Exposure window begins. |
| **Mar 10, 09:15** | Security researcher reports vulnerability via email. |
| **Mar 10, 09:45** | On-call security engineer verifies the report and pages Incident Commander. |
| **Mar 10, 10:00** | **Incident Declared SEV1**. War room established. |
| **Mar 10, 10:15** | Engineering identifies `@Public` annotation error. Hotfix deployed. |
| **Mar 10, 10:30** | **Hotfix verified**. Endpoint secured (returns 401). Exposure window ends. |
| **Mar 10, 11:00** | Log analysis links 2 IPs to researcher, 2 IPs unknown. |
| **Mar 10, 14:22** | **Incident Resolved** following legal assessment. |

### Root Cause Analysis (5 Whys)
1. **Why were 2,847 customer records exposed?**
   Because the `/api/v2/customers/export` endpoint returned sensitive data to unauthenticated requests.

2. **Why did the endpoint return data to unauthenticated requests?**
   Because the endpoint controller was annotated with `@Public` instead of `@AdminOnly` in the code.

3. **Why was the endpoint annotated with `@Public`?**
   The implementation used an insecure default or template during development, and the specific authorization requirement was missed during implementation.

4. **Why was this error not caught during Code Review or CI/CD?**
   The automated test suite focused on functionality (happy path) rather than security constraints (negative testing), and the static analysis tools were not configured to flag `@Public` usage on sensitive data routes.

5. **Why were there no automated checks for sensitive data routes?**
   **Root Cause:** The engineering pipeline lacks "secure by default" guardrails, specifically automated linting for authorization annotations and mandatory negative security tests for new API endpoints.

### What Went Well
- **Response Time**: The time from verification to fix deployment was approximately 30 minutes.
- **External Reporting**: The security researcher disclosure process functioned correctly, alerting the team to an issue that internal monitoring missed.
- **Legal Assessment**: Rapid legal review clarified notification obligations within hours of the incident.

### What Went Poorly
- **Detection**: The vulnerability persisted in production for 11 days without internal detection.
- **Testing Coverage**: CI/CD passed despite a critical authorization flaw; lack of negative testing.
- **Access Logs**: Attribution for 2 of the 4 unique IPs remains unknown, leaving a gap in impact assessment.

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| **Audit all existing `@Public` endpoints** to ensure no other sensitive data is exposed. | Security Team | P0 | 2026-03-11 |
| **Implement linting rule** to block `@Public` on controllers returning sensitive data types (User, Export, etc.). | DevOps | P1 | 2026-03-15 |
| **Require negative security tests** (401/403 checks) for all new API endpoints in CI/CD. | Engineering Lead | P1 | 2026-03-20 |
| **Investigate the 2 unknown IPs** further to determine if malicious scraping occurred. | SecOps | P2 | 2026-03-13 |
| **Update WAF rules** to automatically flag/block anomalous unauthenticated traffic to `/api/v2/*`. | SRE | P2 | 2026-03-25 |
