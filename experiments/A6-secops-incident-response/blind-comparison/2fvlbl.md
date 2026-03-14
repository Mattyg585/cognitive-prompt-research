## Postmortem: Customer Data Exposed via Misconfigured API Endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes | **Severity:** SEV1
**Authors:** Security Engineering, Platform Engineering | **Status:** Draft

### Summary
A new API endpoint (`/api/v2/customers/export`) was deployed to production on March 1 with an incorrect authorization annotation (`@Public` instead of `@AdminOnly`), making it accessible without authentication. The endpoint remained publicly accessible for 11 days, during which 2,847 customer records (name, email, account tier) were exposed. The issue was discovered on March 10 via a responsible disclosure report from a security researcher, and a hotfix was deployed within 30 minutes of incident declaration.

### Impact
- 2,847 customer records exposed (name, email, account tier — no passwords, payment data, or sensitive PII beyond email)
- 11 days of exposure (March 1 to March 10), with 23 requests from 4 unique IP addresses hitting the endpoint; 19 returned customer data
- 2 of the 4 IPs remain unattributed — potential data exfiltration by unknown actors cannot be ruled out
- Legal determined mandatory notification threshold not met, but voluntary customer notification was sent as best practice

### Timeline
| Time (UTC) | Event |
|------------|-------|
| Mar 1, 14:00 | Feature branch merged — `/api/v2/customers/export` endpoint added with `@Public` annotation (should have been `@AdminOnly`) |
| Mar 1, 14:30 | CI/CD pipeline completes — 247 unit tests pass, integration tests pass, Snyk security scan passes |
| Mar 1, 14:45 | Deployed to staging — QA verifies export functionality works (tested from authenticated session) |
| Mar 1, 15:00 | Deployed to production |
| Mar 1–10 | Endpoint live and unauthenticated — 23 requests from 4 unique IPs, 19 returning customer data |
| Mar 10, 09:15 | Security researcher sends responsible disclosure email to security@company.com |
| Mar 10, 09:45 | On-call security engineer verifies vulnerability, pages incident commander |
| Mar 10, 10:00 | SEV1 declared — war room opened, roles assigned |
| Mar 10, 10:15 | Hotfix deployed — annotation changed to `@AdminOnly`, endpoint returns 401 for unauthenticated requests |
| Mar 10, 10:30 | Hotfix verified in production |
| Mar 10, 11:00 | Log analysis begins — 23 requests from 4 IPs identified, 2 matched to security researcher |
| Mar 10, 12:00 | Legal notified — 2,847 exposed records confirmed |
| Mar 10, 13:00 | Legal determines mandatory notification threshold not met; recommends voluntary notification |
| Mar 10, 14:22 | Incident resolved — customer notification drafted, internal comms sent |

### Root Cause
A developer adding a new internal admin endpoint (`/api/v2/customers/export`) used the `@Public` annotation instead of `@AdminOnly` due to an IDE autocomplete error. The two annotations are a single-character difference, making the mistake easy to make and hard to spot in code review. The existing CI/CD pipeline, security scanning, and QA testing processes all failed to catch the misconfiguration: the security scanner (Snyk) only checks dependencies, not authorization annotations; the QA team tested functionality from an already-authenticated session, which cannot detect missing authentication requirements; and there was no automated check to flag new public-facing endpoints or verify authorization requirements on API routes.

### 5 Whys
1. Why was customer data accessible without authentication? → Because the `/api/v2/customers/export` endpoint was annotated with `@Public` instead of `@AdminOnly`, allowing unauthenticated access.
2. Why was the wrong annotation applied? → Because the developer's IDE autocompleted `@Public` instead of `@AdminOnly`, and the two annotations are a single-character difference that was missed during code review.
3. Why didn't code review or testing catch the incorrect annotation? → Because there is no automated authorization test suite that tests endpoints from an unauthenticated session, and QA tested only from an authenticated session where the endpoint worked as expected.
4. Why is there no automated check for authorization on new endpoints? → Because the existing security scanning (Snyk) focuses on dependency vulnerabilities, not application-level authorization logic, and no CI pipeline check exists to flag endpoints with `@Public` annotations for manual review.
5. Why does the framework default to allowing public access rather than requiring explicit authorization? → Because the framework was designed with a permissive default where developers must opt into security restrictions rather than a secure-by-default model where all endpoints require authentication unless explicitly marked public.

### What Went Well
- Security researcher's responsible disclosure was handled within 30 minutes of email receipt
- Hotfix deployed in 30 minutes from incident declaration to endpoint secured
- Clean incident response process — roles assigned quickly, war room functional, timeline maintained throughout
- Legal engaged early and provided clear, actionable guidance
- Exposure limited to non-sensitive data (no passwords, payment info, or sensitive PII beyond email)

### What Went Poorly
- 11-day exposure window before detection — no monitoring or alerting caught the unauthenticated endpoint
- Authorization annotation is a single-character difference (`@Public` vs `@AdminOnly`) with no compile-time or test-time safety net
- No automated check for unauthenticated endpoints in the CI/CD pipeline — security scan only covers dependencies
- QA tested functionality but not authorization — testing from an authenticated session fundamentally cannot catch missing auth
- No WAF rule or API gateway policy to flag new endpoints receiving unauthenticated traffic
- Two unknown IPs accessed customer data and remain unattributed — potential data exfiltration cannot be confirmed or ruled out

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| Build authorization test suite that tests every endpoint from an unauthenticated session | Platform Engineering | P0 | 2026-03-24 |
| Add CI pipeline check that flags any endpoint with `@Public` annotation for mandatory security review | Platform Engineering | P0 | 2026-03-24 |
| Change framework default to `@AdminOnly` (secure by default) — require explicit `@Public` annotation with justification | Platform Engineering | P1 | 2026-04-07 |
| Add WAF/API gateway rule to alert on new endpoints receiving unauthenticated traffic | Security Engineering | P1 | 2026-04-07 |
| Implement runtime authorization monitoring to detect endpoints accessible without authentication | Security Engineering | P1 | 2026-04-14 |
| Investigate the 2 unattributed IPs — engage threat intelligence to determine if data was exfiltrated | Security Engineering | P0 | 2026-03-17 |
| Send voluntary notification to 2,847 affected customers with details and recommended actions | Legal / Customer Success | P0 | 2026-03-14 |
| Add code review checklist item for authorization annotations on all new endpoints | Engineering Management | P2 | 2026-03-21 |

### Lessons Learned
Our existing security testing has a critical blind spot: it validates dependencies and functionality but does not validate authorization. A single annotation — one autocomplete away from the correct value — was the only thing standing between customer data and the public internet, and nothing in our pipeline was designed to catch it. The fix is defense in depth: secure-by-default framework settings so the wrong annotation is the restrictive one, automated authorization testing so every endpoint is verified from an unauthenticated session, CI checks to flag any use of `@Public` for human review, and runtime monitoring so that if all of those layers fail, we detect unauthenticated access in hours rather than days. The 30-minute response time once the incident was detected shows our incident response process works well — the gap is in detection and prevention, not response.
