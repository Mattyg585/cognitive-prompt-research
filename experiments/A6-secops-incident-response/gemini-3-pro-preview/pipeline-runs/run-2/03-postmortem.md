---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A6
tier: pipeline
run: 2
stage: 03-incident-postmortem
---

## Postmortem: Customer data exposed via misconfigured API endpoint
**Date:** March 15, 2026 | **Duration:** 4 hours 22 minutes (Response) / 10 days (Exposure) | **Severity:** SEV1
**Status:** Draft | **Author:** Postmortem Analyst

### Executive Summary
An API endpoint returning customer records was inadvertently exposed to the public internet for 10 days due to a misconfiguration in the code annotations. This exposure resulted in the potential compromise of 2,847 customer records. The issue was identified by a security researcher, rapidly patched, and verified within 4 hours of disclosure.

### Timeline (UTC)
| Time | Event |
|------|-------|
| **Mar 1, 14:00** | Code merged with `@Public` annotation instead of `@AdminOnly`. |
| **Mar 1, 15:00** | Deployment to production completes; endpoint becomes publicly accessible. |
| **Mar 1–10** | Endpoint is live. Logs show 23 requests from 4 unique IPs (2 unattributed). |
| **Mar 10, 09:15** | Security researcher discloses vulnerability via responsible disclosure program. |
| **Mar 10, 10:00** | SEV1 declared by Incident Commander. |
| **Mar 10, 10:15** | Hotfix deployed changing annotation to `@AdminOnly`. |
| **Mar 10, 10:30** | Hotfix verified; endpoint is secured. |
| **Mar 10, 14:22** | Incident resolved. |

### Root Cause Analysis (5 Whys)
1. **Why were 2,847 customer records exposed?**
   → Because an API endpoint was accessible to unauthenticated requests.
2. **Why was the endpoint accessible to unauthenticated requests?**
   → Because the controller method was decorated with `@Public` instead of the required `@AdminOnly`.
3. **Why was the wrong annotation used?**
   → Because the implementation contained a human error (likely copy-paste or misunderstanding) that was not caught during development.
4. **Why was this error not caught during Code Review or CI/CD?**
   → Because the CI/CD pipeline tests functionality (happy path) but does not enforce negative authorization tests, and the code reviewer missed the single-line annotation error.
5. **Why do the pipelines not enforce negative authorization tests?**
   → Because the testing framework currently prioritizes feature verification and lacks a mandatory security harness that validates access control policies by default.

### What Went Well
- **Response Time**: The team deployed and verified a hotfix within 30 minutes of SEV1 declaration.
- **External Reporting**: The responsible disclosure program worked as intended, alerting us to the issue before widespread exploitation.

### What Went Poorly
- **Detection**: The vulnerability existed in production for 10 days without internal detection.
- **Testing Gaps**: Neither automated tests nor manual QA caught the missing authentication check.
- **Code Review**: A critical security configuration was overlooked in the peer review process.

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| **Implement Static Analysis Rule**: Block `@Public` on any controller returning sensitive data types. | Security Engineering | P0 | Mar 17 |
| **Add Negative Auth Tests**: Require integration tests that verify 401/403 responses for all new endpoints. | QA / SDET | P0 | Mar 20 |
| **Audit Existing Endpoints**: Scan codebase for other instances of `@Public` usage. | Security Engineering | P1 | Mar 16 |
| **Update PR Template**: Add specific checkbox for "Verified Auth Levels" in code review checklist. | Engineering Productivity | P2 | Mar 18 |
