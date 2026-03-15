---
model: GPT-5.2
date: 2026-03-15
experiment: A6
tier: optimised
run: 1
---

## Postmortem: Customer data exposed via misconfigured API endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes (detected to resolved)
**Severity:** SEV1 | **Status:** Draft
**Authors:** Security/Engineering (TBD)

### Summary
On 2026-03-10, a security researcher reported that the `/api/v2/customers/export` endpoint returned customer data without authentication. The endpoint was intended for an internal admin dashboard but was deployed with an incorrect authorization annotation (`@Public` instead of `@AdminOnly`). A hotfix changed the annotation to `@AdminOnly`, and the endpoint began returning 401 for unauthenticated requests.

The endpoint had been live for approximately 11 days before detection. Server logs later showed 23 requests from 4 unique IP addresses, with 19 successful (200 OK) responses containing customer data. Two IPs matched the researcher; two were not attributed.

### Impact
- **Who/what was affected:** 2,847 customer records with **name, email, and account tier**.
- **Duration/scale:** Endpoint accessible without authentication for ~11 days; incident response duration was **4h 22m** from detection to resolution.
- **Business/security impact (known):** Confidentiality exposure of limited customer data fields. No passwords, payment information, or additional PII beyond email were reported as exposed.
- **Notification/Legal:** Legal determined statutory notification threshold was not met under applicable privacy laws; voluntary customer notification was recommended.
- **Where uncertainty remains:** The two unknown IPs have not been attributed; whether data was copied/exfiltrated beyond observed requests is **Unknown**.

### Timeline (Facts)
| Time (UTC) | Event | What Was Known |
|---|---|---|
| Mar 1, 14:00 | Feature branch merged adding `/api/v2/customers/export`. Developer used `@Public` instead of `@AdminOnly` (autocomplete mistake). | A new export endpoint for internal admin dashboard was introduced. |
| Mar 1, 14:30 | CI/CD ran; unit tests (247) and integration tests passed. Snyk scan passed (dependency-focused). | Build/test pipeline did not surface authorization misconfiguration. |
| Mar 1, 14:45 | Deployed to staging; QA verified export function while authenticated. | Functionality worked; missing authentication requirement was not tested. |
| Mar 1, 15:00 | Deployed to production. | Endpoint in production. |
| Mar 1–10 | Endpoint remained unauthenticated; later log review found 23 requests from 4 IPs (19 returned data). | At the time, the exposure was not detected. |
| Mar 10, 09:15 | Researcher emailed responsible disclosure with evidence (screenshot). | Confirmed report of unauthenticated access to customer export data. |
| Mar 10, 09:45 | On-call security engineer verified and paged incident commander. | Issue validated; escalation initiated. |
| Mar 10, 10:00 | Incident declared SEV1; war room opened; roles assigned. | Active coordinated response underway. |
| Mar 10, 10:15 | Engineering identified `@Public` annotation and deployed hotfix to `@AdminOnly`. | Containment path identified and applied. |
| Mar 10, 10:30 | Hotfix verified in production; endpoint secured (401 unauthenticated). | Immediate vulnerability closed. |
| Mar 10, 11:00 | Security began log analysis; 23 requests/4 IPs; 2 matched researcher, 2 unknown. | Some access attributable to reporter; remaining access un-attributed. |
| Mar 10, 12:00 | Legal notified; breach assessment began; 2,847 records confirmed exposed. | Exposure scope (fields + record count) confirmed. |
| Mar 10, 13:00 | Legal determined notification threshold not met; recommended voluntary notification. | Compliance posture determined; comms drafting initiated. |
| Mar 10, 14:22 | Incident resolved; customer notification drafted; internal comms sent. | Response complete; follow-up actions to be defined. |

### Causal Analysis (Root cause + contributing factors)
- **Trigger(s):** A production deploy included an endpoint intended for admin use but marked `@Public`, making it accessible without authentication.
- **Contributing factors (parallel):**
  - **No automated authorization verification:** Unit/integration tests passed without asserting unauthenticated behavior for the new endpoint.
  - **QA test context masked the issue:** Testing occurred from an authenticated session, which cannot reveal missing authentication requirements.
  - **Tooling/UX risk:** `@Public` vs `@AdminOnly` differed by a small token, and IDE autocomplete contributed to the wrong selection.
  - **Scanning gap:** The security scan (Snyk) validated dependencies, not authorization annotations or endpoint exposure.
  - **Runtime detection gap:** There was no WAF/API gateway policy or alerting to flag a newly public endpoint serving customer data.
- **Latent/systemic conditions:**
  - Authorization was not “secure by default”; correctness depended on developers selecting the right annotation.
  - The delivery pipeline lacked a dedicated control point for endpoint exposure review (CI policy/test gate/manual review).
- **Where evidence runs out:**
  - Whether the two unknown IPs were benign, malicious, or related; whether data was further redistributed is **Unknown**.

#### 5 Whys (requested)
1) **Why** was customer data accessible without authentication?  
   Because `/api/v2/customers/export` was deployed with a `@Public` annotation.

2) **Why** was it annotated `@Public`?  
   A developer selected `@Public` instead of `@AdminOnly` due to a one-character autocomplete mistake.

3) **Why** didn’t CI/tests catch the incorrect authorization?  
   The test suite validated functionality but did not include unauthenticated/authorization assertions for each endpoint.

4) **Why** didn’t QA catch it in staging?  
   QA tested as an already-authenticated user and did not explicitly verify that unauthenticated requests are rejected.

5) **Why** was there no additional guardrail at deploy/runtime?  
   There was no CI policy to flag `@Public` endpoints for review, and no WAF/API gateway monitoring to alert on new unauthenticated access patterns.

### Response Evaluation (Evidence-linked)
- **What worked:**
  - Responsible disclosure intake was fast: the report was acted on within ~30 minutes of receipt (09:15 → 09:45 verification/escalation).
  - Containment was rapid: hotfix deployed and verified within 30 minutes of incident declaration (10:00 → 10:30).
  - Process execution was strong: war room opened, roles assigned, timeline maintained, and legal engaged early (12:00 onwards).
- **What didn’t:**
  - Detection was slow: the issue existed for ~11 days without internal detection.
  - Evidence/attribution limits remained: two unknown IPs accessed the endpoint; attribution and downstream data handling are unresolved.
- **Detection/observability notes:**
  - Existing security tooling did not cover endpoint authorization posture.
  - No automated signal existed to highlight a new public endpoint serving customer exports.

### Action Items (Tied to findings)
| Action | Owner | Due | Rationale |
|---|---|---:|---|
| Add automated unauthenticated access tests for all HTTP endpoints (or a required allowlist) in CI | Backend Eng / QA (TBD) | TBD | Prevents regressions where endpoints become unintentionally public (contributing factors: missing auth tests, QA context). |
| Add a CI policy that flags any use of `@Public` (or new public routes) for explicit review/approval | Platform Eng / Security Eng (TBD) | TBD | Creates a deliberate control point for risky exposure changes. |
| Make authorization “secure by default” (e.g., require explicit auth annotation; reduce reliance on `@Public` being chosen correctly) | Backend Architecture (TBD) | TBD | Reduces single-token human error risk and shifts to safer defaults. |
| Add WAF/API gateway rule or alerting for new unauthenticated endpoints returning customer data / export-sized responses | Security Eng / Infra (TBD) | TBD | Improves time-to-detect for public exposure and suspicious access patterns. |
| Improve audit logging & alerting specifically for unauthenticated access to sensitive customer export endpoints | Observability / Security (TBD) | TBD | Strengthens forensic capability and detection; helps with attribution gaps. |
| Create/extend a checklist for feature QA that includes explicit authorization verification (authenticated + unauthenticated) | QA (TBD) | TBD | Addresses the “tested while authenticated” blind spot. |

### Lessons Learned
- Authorization failures can be “functionally invisible” when tested only through authenticated flows; every endpoint needs an explicit unauthenticated expectation.
- Security scanning that focuses on dependencies is not sufficient to prevent exposure-by-misconfiguration; policy and tests must cover exposure controls.
- Small UX/tooling hazards (annotation names, autocomplete) can create high-severity outcomes without additional guardrails.
- Fast response is valuable, but it does not compensate for long detection windows; runtime monitoring for exposure changes is critical.
