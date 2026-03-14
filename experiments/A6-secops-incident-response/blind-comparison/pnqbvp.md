## Postmortem: Customer Data Exposed via Misconfigured API Endpoint
**Date:** 2026-03-10 | **Duration:** 4 hours 22 minutes (detection to resolution); 11 days total exposure | **Severity:** SEV1
**Authors:** Incident Response Team | **Status:** Draft

### Summary

A new API endpoint (`/api/v2/customers/export`) was deployed to production on March 1st with a `@Public` authorization annotation instead of `@AdminOnly`. This made 2,847 customer records (name, email, account tier) accessible without authentication for 11 days. The misconfiguration was not caught by the CI/CD pipeline, security scanning, or QA testing. It was discovered on March 10th through a responsible disclosure report from an external security researcher. The endpoint was secured within 30 minutes of incident declaration.

This incident matters not because of the severity of the data exposed — no passwords, financial data, or sensitive PII were included — but because it reveals multiple gaps in how the system verifies authorization on new endpoints. The fact that every existing safeguard passed while the endpoint was publicly accessible indicates a systemic blind spot, not a one-off mistake.

### Impact

- **2,847 customer records exposed**: name, email address, and account tier. No passwords, payment information, or government-issued identifiers were included.
- **11 days of exposure** (March 1, 15:00 UTC through March 10, 10:30 UTC).
- **23 requests from 4 unique IP addresses** during the exposure window. 19 returned customer data; 4 returned empty results.
- **2 IPs attributed** to the reporting security researcher. **2 IPs remain unattributed** — it is unknown whether these represent malicious actors or additional researchers.
- **Legal assessment**: notification threshold not met under applicable privacy laws. Voluntary customer notification was recommended and drafted.
- **Reputational risk**: a security researcher found the vulnerability before internal systems did, which means external parties were aware of the exposure before the organisation was.

### Timeline

| Time (UTC) | Event | What Was Known |
|------------|-------|---------------|
| Mar 1, 14:00 | Feature branch merged. New `/api/v2/customers/export` endpoint added with `@Public` annotation (should have been `@AdminOnly`). | Developer believed the annotation was correct — IDE autocomplete selected `@Public`. The merge diff was reviewed, but the annotation appeared intentional in context. |
| Mar 1, 14:30 | CI/CD pipeline completes. 247 unit tests pass. Integration tests pass. Snyk security scan passes. | All automated checks reported green. Snyk scans dependencies for known vulnerabilities, not authorization configuration. No test existed to verify endpoint authentication requirements. |
| Mar 1, 14:45 | Deployed to staging. QA tests export functionality successfully. | QA confirmed the endpoint worked correctly. Testing was performed from an authenticated session, so the missing authentication requirement was invisible — the endpoint returned correct data because the tester was already logged in. |
| Mar 1, 15:00 | Deployed to production. | All gates passed. No one had reason to believe the endpoint was misconfigured. |
| Mar 1–10 | Endpoint live and unauthenticated in production. 23 requests from 4 IPs logged. | No alerting existed for unauthenticated access to new endpoints. Server logs captured the requests, but no one was looking at them in this context. The requests would have appeared as normal API traffic. |
| Mar 10, 09:15 | Security researcher submits responsible disclosure via email to security@company.com. | First external signal that something is wrong. |
| Mar 10, 09:45 | On-call security engineer reads the email, verifies the vulnerability, pages the incident commander. | 30 minutes from receipt to verification. The vulnerability was straightforward to confirm — hitting the endpoint from an unauthenticated session returned data. |
| Mar 10, 10:00 | SEV1 declared. War room opened. Roles assigned. | The team understood the scope: an unauthenticated endpoint exposing customer data. The question shifted to containment and impact assessment. |
| Mar 10, 10:15 | Engineering identifies the `@Public` annotation and deploys hotfix changing it to `@AdminOnly`. | Root technical cause identified within 15 minutes. The fix was a one-line change. |
| Mar 10, 10:30 | Hotfix verified in production. Endpoint returns 401 for unauthenticated requests. | Immediate exposure stopped. Attention shifted to impact assessment. |
| Mar 10, 11:00 | Security team begins log analysis. 23 requests from 4 IPs identified. 2 IPs matched to the security researcher. 2 IPs unattributed. | The team now knew the scale of access but not who the unattributed actors were or what they did with the data. |
| Mar 10, 12:00 | Legal notified. 2,847 exposed records confirmed (name, email, account tier). | Scope fully understood. No sensitive personal data, financial data, or credentials in the exposed dataset. |
| Mar 10, 13:00 | Legal determines notification threshold not met. Recommends voluntary notification as best practice. | Decision made to notify customers proactively despite no legal requirement. |
| Mar 10, 14:22 | Incident resolved. Customer notification drafted. Internal comms sent. | Full incident lifecycle complete. |

### Root Cause Analysis

This incident has a branching causal structure. There was a single proximate cause (the wrong annotation), but multiple independent system gaps had to coexist for the exposure to persist for 11 days undetected. Fixing only the proximate cause would leave the system vulnerable to the next similar mistake.

**The proximate cause: a wrong annotation.**

The developer used `@Public` instead of `@AdminOnly` on the new endpoint. This was an IDE autocomplete error — both annotations appear in the autocomplete list, and `@Public` was selected instead of `@AdminOnly`. This is a human error of the kind that will recur. People make selection errors in autocomplete menus routinely. The question is not "how do we prevent developers from picking the wrong autocomplete suggestion" but "why did this particular error propagate through every subsequent check without being caught?"

**Branch 1: The annotation system itself is fragile.**

The authorization model uses opt-in annotation — endpoints are public by default unless explicitly annotated with a restrictive decorator. This means any new endpoint starts in the most permissive state, and security depends on the developer remembering (and correctly applying) the right annotation. In a secure-by-default model, a missing or wrong annotation would result in *more* restrictive behaviour, not less. The `@Public` annotation would be the one requiring explicit, deliberate application — and would be the natural candidate for a CI gate requiring justification or review.

This is an architectural decision, likely made early in the framework's life when the API surface was smaller and the team was smaller. It made development faster at the cost of security, a tradeoff that becomes more dangerous as the API surface grows.

**Branch 2: No test verifies authorization from the outside.**

The integration test suite and QA process both test endpoints from an authenticated context. This means they verify that *authorized users can access the endpoint* — but never verify that *unauthorized users cannot*. This is a classic gap: testing the positive case but not the negative case for security-critical behaviour.

The QA tester was already logged in. The endpoint worked. The test passed. From the tester's perspective, everything was correct. The information that would have revealed the problem — "does this endpoint work without authentication?" — was never generated because the test methodology couldn't produce it.

**Branch 3: The security scanning tools have a scope mismatch.**

Snyk scans for known vulnerabilities in dependencies. It does not examine application-level authorization configuration. This is not a failing of Snyk — it's doing what it's designed to do. But there is an implicit assumption in the pipeline that "security scan passes" means "the application is secure," when in reality it means "the dependencies don't have known CVEs." No tool in the pipeline checks whether endpoints have appropriate authorization annotations.

**Branch 4: No runtime detection of anomalous access patterns.**

Even after the endpoint was deployed with the wrong annotation, runtime detection could have caught the exposure. There was no WAF rule flagging new endpoints receiving unauthenticated traffic. There was no API gateway policy alerting when a previously-nonexistent endpoint starts receiving external requests. The 23 requests over 11 days were logged but never surfaced — they looked like normal traffic because nothing was looking for "unauthenticated access to an endpoint that should require authentication."

This represents a missing layer of defence in depth. The organisation relied on pre-deployment checks (which all failed to catch this) without a runtime safety net.

**Branch 5: Code review did not catch the annotation.**

The merge diff was reviewed, but the `@Public` annotation did not trigger a question. This is understandable — in a diff with meaningful functional changes, a single annotation that *looks* intentional is easy to pass over. The reviewer had no way to know the developer intended `@AdminOnly` unless they independently reasoned about what authorization the endpoint should have. Without a convention like "all new endpoints require a justification comment for their authorization level," the annotation appeared to be a deliberate choice.

**Where the branches converge:**

Each of these gaps is individually understandable. Taken together, they reveal a system where authorization correctness depends entirely on a single point — the developer choosing the right annotation — with no verification layer anywhere downstream. The CI/CD pipeline, the security scan, QA testing, code review, and runtime monitoring all passed or were absent. The system had no redundancy for authorization correctness.

### Response Evaluation

**What worked well:**

- **Rapid response once detected (09:15 to 10:30, 75 minutes from email to verified fix).** The incident response process functioned as designed. Roles were assigned quickly, the war room was effective, and the hotfix was straightforward.
- **The security researcher's email was acted on within 30 minutes.** The on-call engineer read the disclosure, verified it, and escalated promptly. This reflects a healthy responsible disclosure handling process.
- **Legal was engaged early (12:00) and provided clear, actionable guidance by 13:00.** This prevented ambiguity about notification obligations.
- **The technical fix was simple and deployed quickly (10:00 to 10:30).** Because the root cause was a single annotation, the hotfix was low-risk and fast.

**What did not work well:**

- **Detection took 11 days and came from an external party.** The organisation's own monitoring, logging, and security processes did not detect the exposure. Every request to the unauthenticated endpoint was logged, but no process examined those logs for this type of anomaly. The incident was found because a security researcher happened to discover the endpoint — not because any internal system flagged it.
- **The unattributed IPs remain a gap.** Two of the four IPs that accessed the endpoint have not been identified. Without attribution, the organisation cannot determine whether customer data was exfiltrated by a malicious actor. This limits the accuracy of the impact assessment and may affect notification decisions if new information surfaces.
- **No pre-deployment gate caught the issue.** The entire CI/CD pipeline — unit tests, integration tests, security scan, QA, code review — is designed to catch bugs, not authorization misconfigurations. The incident passed through every gate because no gate was designed to check what went wrong.

### Action Items

| Action | Owner | Rationale |
|--------|-------|-----------|
| Implement an unauthenticated endpoint test suite that hits every API endpoint from an unauthenticated session and verifies the expected authorization response (401/403 for protected endpoints, 200 only for intentionally public ones). Run this in CI on every deploy. | Engineering / QA Lead | Addresses Branch 2 (no negative-case authorization testing). This is the highest-leverage fix — it would have caught this exact incident at the CI stage. |
| Add a CI gate that flags any endpoint annotated with `@Public` for mandatory review, requiring an explicit justification comment and approval from a security-aware reviewer. | Engineering Lead | Addresses Branch 1 (annotation fragility) and Branch 5 (code review gap). Makes `@Public` a deliberate, reviewed choice rather than an easy autocomplete mistake. |
| Evaluate and implement a secure-by-default authorization model where endpoints require authentication unless explicitly marked public. This is a larger architectural change — scope it, assess migration risk, and timeline it. | Engineering Lead / Architect | Addresses Branch 1 at the architectural level. Inverts the failure mode so that mistakes result in over-restriction, not exposure. |
| Deploy a WAF rule or API gateway policy that alerts when new endpoints receive unauthenticated traffic, and when previously unseen endpoints appear in traffic logs. | Security Engineering | Addresses Branch 4 (no runtime detection). Provides a defence-in-depth layer that catches issues the pre-deployment pipeline misses. |
| Add an authorization configuration check to the CI security scanning step — either extend the existing tooling or add a dedicated scanner that verifies endpoint annotations against an expected-authorization manifest. | Security Engineering | Addresses Branch 3 (security scan scope mismatch). Closes the gap between "dependencies are safe" and "authorization is correct." |
| Investigate the two unattributed IP addresses. Determine if further forensic analysis is warranted. Document findings regardless of outcome. | Security Team | Addresses the open question from the incident — whether data was accessed by a malicious party. Necessary for accurate impact assessment. |
| Establish a convention in code review that new or modified endpoint authorization annotations require an explicit comment explaining the intended access level and why. | Engineering Lead | Addresses Branch 5 (code review gap). Makes authorization intent visible in the diff, giving reviewers the context to question unexpected annotations. |

### Lessons Learned

**Authorization correctness had zero redundancy.** The system treated authorization as a single decision point — the developer's annotation — with no downstream verification. Every other aspect of code quality has multiple checkpoints (tests, review, QA, monitoring). Authorization had one, and it was the most error-prone: a human making a selection in an autocomplete menu. This incident revealed that the organisation's testing and monitoring infrastructure was comprehensive for *functionality* but had a blind spot for *authorization*.

**Testing from an authenticated session cannot verify authentication requirements.** This seems obvious in retrospect, but the QA process was designed to verify "does the feature work?" not "is the feature correctly restricted?" The authenticated testing methodology has a structural inability to detect missing authentication — the test environment inherently masks the problem. This is a general principle: security testing requires adversarial conditions, not just functional conditions.

**The gap between "security scan passes" and "the application is secure" is larger than assumed.** The presence of Snyk in the pipeline creates a reasonable confidence that security is being checked. But Snyk's scope (dependency vulnerabilities) does not overlap at all with this incident's cause (application-level authorization). The label "security scan" is doing work that the tool itself isn't — it creates an illusion of coverage. Naming matters: if the pipeline step were called "dependency vulnerability scan" instead of "security scan," the gap in authorization checking might have been more visible.

**Detection time, not response time, was the real failure.** The response once detected was excellent — 75 minutes from email to verified fix. But detection took 11 days and required an external party. If the organisation's security posture is measured by response time, this incident looks like a success. If measured by detection time, it reveals a significant gap. The 11-day window is the metric that matters — it represents the actual risk exposure, and it was limited only by the chance that a security researcher found the endpoint before (or alongside) any malicious actor.

**IDE autocomplete errors will recur.** The proximate cause — a developer selecting `@Public` instead of `@AdminOnly` from an autocomplete menu — is not a mistake that training or attention can reliably prevent. It is a category of human error that is inherent to the tooling. The correct response is not "be more careful" but "build systems where this class of error is caught automatically." The action items above are designed to add those catching mechanisms at multiple points in the pipeline.
