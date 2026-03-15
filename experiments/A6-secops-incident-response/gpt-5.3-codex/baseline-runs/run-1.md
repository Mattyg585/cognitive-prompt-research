---
model: GPT-5.3-Codex (gpt-5.3-codex)
date: 2026-03-15
experiment: A6
tier: baseline
run: 1
---

## Postmortem: Customer Data Exposed via Misconfigured API Endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes | **Severity:** SEV1  
**Authors:** Security Engineering, Platform Engineering | **Status:** Draft

### Summary
On March 1, a new endpoint (`/api/v2/customers/export`) was deployed with `@Public` instead of `@AdminOnly`, allowing unauthenticated access to customer export data. The issue remained in production for 11 days and was discovered by a security researcher on March 10. The team declared SEV1, deployed a hotfix in 30 minutes, and completed legal and communication steps the same day.

### Impact
- 2,847 customer records were exposed (name, email, account tier)
- No passwords, payment data, or sensitive financial data were exposed
- Endpoint was publicly accessible for approximately 11 days
- 23 requests from 4 IPs were observed; 19 returned customer data
- 2 IPs were attributed to the security researcher, 2 remain unattributed

### Timeline
| Time (UTC) | Event |
|---|---|
| Mar 1, 14:00 | Feature merged with `@Public` instead of `@AdminOnly` |
| Mar 1, 14:30 | CI/CD passed (247 unit tests, integration tests, Snyk dependency scan) |
| Mar 1, 14:45 | Staging QA passed from authenticated session |
| Mar 1, 15:00 | Production deploy |
| Mar 1–10 | Endpoint remained unauthenticated and publicly accessible |
| Mar 10, 09:15 | Security researcher disclosed issue by email |
| Mar 10, 09:45 | On-call engineer verified and paged incident commander |
| Mar 10, 10:00 | SEV1 declared; war room opened |
| Mar 10, 10:15 | Hotfix deployed (`@AdminOnly`) |
| Mar 10, 10:30 | Hotfix verified in production |
| Mar 10, 11:00 | Log analysis started; 23 requests from 4 IPs confirmed |
| Mar 10, 12:00 | Legal notified; exposure details confirmed |
| Mar 10, 13:00 | Legal advised mandatory notice not required; voluntary notice recommended |
| Mar 10, 14:22 | Incident resolved |

### Root Cause
The endpoint authorization was controlled by an annotation and was incorrectly set to `@Public` due to a one-character autocomplete mistake. Existing controls did not catch this:

- No CI check for authorization annotations
- No unauthenticated endpoint test coverage
- Security scan focused on dependencies, not authorization
- QA tested from authenticated context only
- No runtime alerting for new unauthenticated endpoint traffic

### 5 Whys
1. Why was customer data accessible without authentication?  
   Because `/api/v2/customers/export` was annotated with `@Public`.
2. Why was `@Public` used?  
   Because the developer selected it via IDE autocomplete instead of `@AdminOnly`.
3. Why wasn’t this caught in testing?  
   Because tests verified functionality but not unauthenticated access behavior.
4. Why wasn’t it caught in CI/security scanning?  
   Because CI and Snyk checks did not validate endpoint authorization configuration.
5. Why could one annotation error expose data for days?  
   Because authorization relied on permissive defaults and lacked defense-in-depth controls.

### What Went Well
- Responsible disclosure was reviewed quickly
- Vulnerability was verified and escalated within 30 minutes
- Hotfix was deployed and validated rapidly
- Incident command process and role assignment worked well
- Legal was engaged early with clear guidance

### What Went Poorly
- Exposure existed for 11 days before detection
- Internal controls did not detect unauthenticated data access
- Authorization misconfiguration had no compile-time/test-time guardrail
- QA process did not include unauthorized-access test cases
- Two accessing IP addresses remain unattributed

### Action Items
| Action | Owner | Priority | Due Date |
|---|---|---|---|
| Add unauthenticated endpoint authorization test suite in CI | Platform Engineering | P0 | 2026-03-24 |
| Add CI gate for any `@Public` annotation requiring manual review | Platform Engineering | P0 | 2026-03-24 |
| Design secure-by-default endpoint authorization model | Platform Architecture | P1 | 2026-04-07 |
| Add WAF/API gateway alerting for unauthenticated access to sensitive endpoints | Security Engineering | P1 | 2026-04-07 |
| Investigate two unattributed IP addresses | Security Operations | P0 | 2026-03-17 |
| Add code review checklist item for endpoint authorization intent | Engineering Management | P2 | 2026-03-21 |

### Lessons Learned
This incident showed that existing safeguards were strong for functional correctness but weak for authorization assurance. Once detected, response execution was fast and coordinated. The largest gap was prevention and detection: a single annotation error could reach production and remain undetected for days.
