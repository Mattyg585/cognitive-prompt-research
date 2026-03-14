## Incident Timeline

**Incident**: Customer data exposed via misconfigured API endpoint
**Period covered**: 2026-03-01 14:00 UTC (feature branch merge) to 2026-03-10 14:22 UTC (incident resolved)
**Severity**: SEV1
**Total exposure window**: Approximately 11 days (Mar 1 15:00 to Mar 10 10:30)
**Detection-to-resolution**: 4 hours 22 minutes (Mar 10 09:15 to Mar 10 14:22, measured from external report receipt)

### Pre-Incident Context

A new `/api/v2/customers/export` endpoint was being developed for an internal admin dashboard. This endpoint was designed to export customer data and was intended to be restricted to admin users only. The codebase uses annotation-based access control, where `@AdminOnly` restricts an endpoint to authenticated admin sessions and `@Public` makes it accessible without authentication. These two annotations are the mechanism by which authorization is declared at the endpoint level.

The CI/CD pipeline included 247 unit tests, integration tests, and a Snyk security scan. The Snyk scan was configured to check dependency vulnerabilities, not application-level authorization configuration. No automated test existed that verified endpoints from an unauthenticated session. No CI-level check existed to flag endpoints carrying the `@Public` annotation for review.

QA testing processes tested endpoint functionality from authenticated sessions. There is no evidence in the record of a QA procedure that included testing authorization boundaries (i.e., verifying that endpoints reject unauthenticated requests).

### Chronological Timeline

**2026-03-01, 14:00 UTC**
- **Event**: Feature branch merged containing the new `/api/v2/customers/export` endpoint. The endpoint carried a `@Public` annotation instead of the intended `@AdminOnly` annotation.
- **Known at this point**: The developer was working on an admin-only feature for the internal dashboard. The IDE's autocomplete offered `@Public` and `@AdminOnly` as options. The merge was treated as routine.
- **Not known**: That the annotation was incorrect. The developer's intent was `@AdminOnly`; the committed code read `@Public`. There is no indication anyone reviewed the annotation specifically during code review, though the record does not document whether a code review occurred or what it covered.
- **Decision**: Merge the feature branch.
- **Decision context**: The feature was complete and functionally correct. The annotation difference is a single-character autocomplete selection in the IDE. The developer believed the endpoint was appropriately secured.

**2026-03-01, 14:30 UTC**
- **Event**: CI/CD pipeline ran. All 247 unit tests passed. Integration tests passed. Snyk security scan passed.
- **Known at this point**: All automated checks returned green. The pipeline reported the build as ready for deployment.
- **Not known**: The Snyk scan checked dependency vulnerabilities only, not authorization annotations. No test in the suite verified whether the endpoint required authentication. The passing pipeline provided confidence that was accurate for what it tested but did not cover the specific failure mode present.

**2026-03-01, 14:45 UTC**
- **Event**: Application deployed to staging environment. QA tested the export functionality. The endpoint worked as expected functionally -- it returned customer data correctly.
- **Known at this point**: The feature worked. QA's test user was already authenticated, so the export returned data as expected.
- **Not known**: The test was being conducted from an authenticated session. From that vantage point, the endpoint's behavior was identical whether it carried `@Public` or `@AdminOnly` -- both would return data to an authenticated admin user. The authorization misconfiguration was invisible to this testing approach.
- **Decision**: QA approved the deployment for production.
- **Decision context**: The feature performed correctly in staging. All automated tests had passed. QA's testing approach confirmed functionality. There was no step in the QA process that tested from an unauthenticated session.

**2026-03-01, 15:00 UTC**
- **Event**: Application deployed to production. The `/api/v2/customers/export` endpoint was now live and accessible without authentication on the public internet.
- **Known at this point**: The team believed a fully functional, properly secured admin endpoint had been deployed.
- **Not known**: The endpoint was accessible to anyone. No monitoring, WAF rule, or API gateway policy existed to detect or alert on a new endpoint receiving unauthenticated traffic.

**2026-03-01 to 2026-03-10 (9-day exposure period)**
- **Event**: The endpoint remained live and unauthenticated. Server logs recorded 23 requests to the endpoint from 4 unique IP addresses over this period. 19 of the 23 requests returned 200 OK with customer data. 4 requests returned empty results (queries against date ranges containing no customers).
- **Known at this point**: The team had no awareness of unauthorized access. No alert triggered. No anomaly was flagged. The 23 requests were logged in server logs but were not surfaced to any team.
- **Not known**: That the endpoint was being accessed externally. That customer data was being returned to unauthenticated requesters. The server logs contained the evidence, but no process or monitoring consumed those logs for this type of event.
- **Gap in the record**: The distribution of the 23 requests across the 9-day period is not documented. It is not known when the first external request occurred, whether the requests were clustered or spread out, or what the pattern of access looked like over time. The 4 unique IP addresses are documented but their access patterns (which IP made how many requests, when) are not detailed in the available record.

**2026-03-10, 09:15 UTC**
- **Event**: A security researcher emailed security@company.com with a responsible disclosure report. The report included a screenshot demonstrating that the endpoint returned customer data without authentication.
- **Known at this point**: For the first time, an external party communicated that the endpoint was open. The disclosure report provided specific evidence: a screenshot of the unauthenticated response containing customer data.
- **Not known**: The scope of exposure (how many records, how many external requesters). Whether any of the access was malicious. How long the endpoint had been exposed.

**2026-03-10, 09:45 UTC (T+30 min from disclosure)**
- **Event**: On-call security engineer read the email and verified the vulnerability. Paged the incident commander.
- **Known at this point**: The vulnerability was confirmed as real. The endpoint was open and returning customer data without authentication.
- **Not known**: The scope and duration of exposure. Whether the issue affected other endpoints.
- **Decision**: Page the incident commander.
- **Decision context**: The security engineer had verified that an unauthenticated endpoint was returning customer data in production. This met the threshold for incident escalation.

**2026-03-10, 10:00 UTC (T+45 min from disclosure)**
- **Event**: Incident declared SEV1. War room opened in Slack. Incident commander assigned roles to responders.
- **Known at this point**: Confirmed data exposure via unauthenticated endpoint. The security researcher's report was the sole source of information. The team knew the endpoint was open but did not yet know why or for how long.
- **Decision**: Declare SEV1 and open war room.
- **Decision context**: Customer data accessible without authentication on a production endpoint. The nature of the exposure (customer records via public endpoint) warranted the highest severity level.

**2026-03-10, 10:15 UTC (T+1 hr from disclosure, T+15 min from incident declaration)**
- **Event**: Engineering team identified the `@Public` annotation on the endpoint as the source of the exposure. Deployed a hotfix changing the annotation to `@AdminOnly`. The endpoint began returning 401 for unauthenticated requests.
- **Known at this point**: The specific technical cause was identified -- the wrong annotation on the endpoint. The fix was straightforward: change the annotation. The team now knew this was a configuration issue on a single endpoint.
- **Not known**: The full scope of exposure. How many records had been accessed. Who had accessed them. How long the endpoint had been misconfigured.
- **Decision**: Deploy the annotation change as a hotfix directly, without going through the full deployment pipeline.
- **Decision context**: The fix was a one-line annotation change. The endpoint was actively exposing customer data. Speed of remediation was the priority.

**2026-03-10, 10:30 UTC (T+1 hr 15 min from disclosure)**
- **Event**: Hotfix verified in production. The endpoint was confirmed to return 401 for unauthenticated requests. The exposure was stopped.
- **Known at this point**: The endpoint was secured. The immediate risk was addressed. The team could now shift from containment to assessment.

**2026-03-10, 11:00 UTC (T+1 hr 45 min from disclosure)**
- **Event**: Security team began log analysis. Identified 23 requests from 4 unique IP addresses to the endpoint. Cross-referenced the IPs against known security researcher IPs. Two IPs matched the security researcher who filed the disclosure. Two IPs were unknown and unattributed.
- **Known at this point**: The scale of access was quantified at 23 requests from 4 IPs. The security researcher accounted for 2 of the 4 IPs. 19 requests had returned customer data; 4 had returned empty results.
- **Not known**: The identity or intent of the 2 unknown IP addresses. Whether those requests represented malicious exfiltration, automated scanning, or something else. Whether the data returned in those requests had been stored, shared, or used.

**2026-03-10, 12:00 UTC (T+2 hr 45 min from disclosure)**
- **Event**: Legal team notified. Data breach assessment began. The exposed dataset was confirmed as 2,847 customer records containing name, email address, and account tier. The assessment confirmed the exposed data did not include passwords, payment information, or PII beyond email addresses.
- **Known at this point**: The full scope of the data exposure was defined: 2,847 records, three fields per record (name, email, account tier). The data classification was established -- contact information and account metadata, not credentials or financial data.
- **Decision**: Notify legal and begin formal breach assessment.
- **Decision context**: Customer data had been confirmed as exposed to unknown external parties. Legal assessment was required to determine notification obligations.

**2026-03-10, 13:00 UTC (T+3 hr 45 min from disclosure)**
- **Event**: Legal completed their assessment. Determined that the notification threshold under applicable privacy laws was not met, as the exposed data did not include sensitive personal data or financial data. Legal recommended voluntary notification to affected customers as best practice.
- **Known at this point**: The legal obligations were defined. Mandatory notification was not required. Voluntary notification was recommended.
- **Decision**: Accept legal's recommendation to proceed with voluntary customer notification.
- **Decision context**: Legal provided a clear assessment distinguishing mandatory obligation (not triggered) from best-practice recommendation (voluntary notification). The team chose to notify voluntarily.

**2026-03-10, 14:22 UTC (T+5 hr 7 min from disclosure, T+4 hr 22 min from incident declaration)**
- **Event**: Incident resolved. Customer notification drafted. Internal communications sent.
- **Known at this point**: The endpoint was secured. The scope was defined. Legal guidance was established. Notification was in progress.

### Concurrent Activity

**Security researcher communication thread**: The security researcher who filed the responsible disclosure at 09:15 was a parallel actor throughout the incident. Their report triggered detection. Two of the four accessing IP addresses were attributed to them. The timing and nature of their testing (how many of the 23 requests were theirs, when they conducted their testing) is not fully detailed in the record.

**Normal business operations**: The 11-day exposure period (Mar 1-10) overlapped with normal business operations. The endpoint was serving customer data to unauthenticated requesters during this period without any team's awareness. Production systems otherwise operated normally -- the misconfiguration did not cause any functional degradation or alerts.

**The two unattributed IPs**: During the exposure period, two IP addresses that have not been identified accessed the endpoint. Their activity ran in parallel to the security researcher's activity. The nature, timing, and intent of their access remains unknown at the time of incident resolution.

### Gaps in the Record

**Code review process**: The record does not document whether the feature branch received a code review before merge, or if it did, what the review covered. It is not known whether a reviewer saw the `@Public` annotation and approved it, missed it, or whether the merge bypassed review.

**Request distribution over the exposure period**: The 23 requests from 4 IPs are quantified as a total, but the record does not detail when they occurred within the Mar 1-10 window, how they were distributed across the 4 IPs, or what specific data each request returned. The granularity needed to understand the access pattern is absent.

**Unattributed IP investigation**: At the time of incident resolution, the two unknown IPs had not been attributed. The record does not indicate whether further investigation was planned, in progress, or considered unnecessary. Whether data was exfiltrated by a potentially malicious actor remains an open question in the factual record.

**Hotfix deployment process**: The record notes the hotfix was deployed in 15 minutes (10:00 to 10:15), but does not detail whether it went through an abbreviated CI/CD pipeline, was deployed directly, or what verification steps occurred before the 10:30 production verification.

**Other endpoints**: The record does not document whether any review was conducted of other endpoints for similar annotation issues during or after the incident. Whether this misconfiguration was isolated or part of a broader pattern is not addressed in the available evidence.

**Server log monitoring**: The record states server logs captured the 23 requests. It does not document what monitoring or alerting was configured on those logs, why the requests did not trigger any alert, or whether the logs were routinely reviewed.

### Key Observations

There was a 30-minute interval between the security researcher's email (09:15) and the on-call engineer's verification and escalation (09:45). There was then a 15-minute interval between incident declaration (10:00) and the deployed hotfix (10:15).

The exposure window (approximately 11 days) was substantially longer than the detection-to-resolution window (4 hours 22 minutes). Detection was triggered by an external party, not by internal monitoring.

All internal checkpoints -- code merge, CI/CD pipeline, security scan, QA in staging -- passed without detecting the authorization misconfiguration. Each checkpoint tested a different aspect (functional correctness, dependency vulnerabilities, feature behavior) but none tested the specific property that failed (endpoint authorization from an unauthenticated context).

The QA test that verified the endpoint in staging was conducted from an authenticated session. From that session, the endpoint behaved identically whether configured as `@Public` or `@AdminOnly`, making the misconfiguration invisible to that test.

Of the 4 IP addresses that accessed the endpoint, 2 have been attributed (to the security researcher) and 2 remain unattributed at incident close.

The period between incident resolution (14:22) and the legal determination (13:00) included approximately 1 hour 22 minutes of activity (notification drafting, internal comms) that is not broken down further in the record.
