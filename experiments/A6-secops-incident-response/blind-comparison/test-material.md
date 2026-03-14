# Test Material: Production Incident

## Mode: Postmortem

Write a blameless postmortem for the following resolved incident.

## Incident Summary

- **Title**: Customer data exposed via misconfigured API endpoint
- **Severity**: SEV1
- **Duration**: 4 hours 22 minutes (detected to resolved)
- **Date**: 2026-03-10
- **Impact**: 2,847 customer records (name, email, account tier) accessible via unauthenticated API endpoint for approximately 11 days before detection

## Timeline

| Time (UTC) | Event |
|------------|-------|
| Mar 1, 14:00 | Feature branch merged: new `/api/v2/customers/export` endpoint added for internal admin dashboard. Developer used `@Public` annotation instead of `@AdminOnly` — a one-character autocomplete mistake in the IDE. |
| Mar 1, 14:30 | CI/CD pipeline runs. All 247 unit tests pass. Integration tests pass. Security scan (Snyk) passes — it checks dependencies, not authorization annotations. |
| Mar 1, 14:45 | Deployed to staging. QA tests the export functionality — it works. Nobody tests whether the endpoint requires authentication because the test user is already authenticated. |
| Mar 1, 15:00 | Deployed to production. |
| Mar 1–10 | Endpoint live and unauthenticated. Server logs show 23 requests to the endpoint from 4 unique IP addresses. 19 of the 23 requests returned 200 OK with customer data. 4 returned empty results (date range with no customers). |
| Mar 10, 09:15 | Security researcher emails security@company.com with a responsible disclosure report. Includes screenshot showing the endpoint returns customer data without authentication. |
| Mar 10, 09:45 | On-call security engineer reads the email, verifies the vulnerability. Pages the incident commander. |
| Mar 10, 10:00 | Incident declared SEV1. War room opened in Slack. Incident commander assigns roles. |
| Mar 10, 10:15 | Engineering team identifies the `@Public` annotation. Deploys hotfix — changes annotation to `@AdminOnly`. Endpoint now returns 401 for unauthenticated requests. |
| Mar 10, 10:30 | Hotfix verified in production. Endpoint secured. |
| Mar 10, 11:00 | Security team begins log analysis. Identifies 23 requests from 4 IPs. Cross-references against known security researcher IPs — 2 IPs match the researcher. 2 IPs are unknown. |
| Mar 10, 12:00 | Legal notified. Data breach assessment begins. 2,847 records confirmed exposed (name, email, account tier — no passwords, payment info, or PII beyond email). |
| Mar 10, 13:00 | Legal determines notification threshold not met under applicable privacy laws (no sensitive personal data, no financial data). Recommends voluntary notification to affected customers as best practice. |
| Mar 10, 14:22 | Incident resolved. Customer notification drafted. Internal comms sent. |

## What Went Well
- Security researcher's responsible disclosure was handled within 30 minutes of email receipt
- Hotfix deployed in 30 minutes from incident declaration
- Clean incident response process — roles assigned, war room functional, timeline maintained
- Legal engaged early and provided clear guidance

## What Went Poorly
- 11-day exposure window — nobody noticed for over a week
- Authorization annotation is a single-character difference (`@Public` vs `@AdminOnly`) with no compile-time or test-time verification
- No automated check for unauthenticated endpoints — the security scan checks dependencies only
- QA tested functionality but not authorization — testing from an authenticated session can't catch missing auth
- No WAF rule or API gateway policy that flags new public endpoints
- The two unknown IPs that accessed customer data have not been attributed — we don't know if data was exfiltrated by a malicious actor

## What the Team Discussed
- Adding an authorization test suite that specifically tests each endpoint from an unauthenticated session
- Adding a CI check that flags any endpoint with `@Public` annotation for manual review
- WAF rule to alert on new endpoints receiving unauthenticated traffic
- Whether the default should be `@AdminOnly` (secure by default) rather than requiring developers to explicitly add authorization
- Whether 11 days is acceptable detection time or whether we need runtime authorization monitoring

## The Task

Write the full postmortem using the `/incident-response postmortem` template from the prompt. Include the 5 Whys root cause analysis and specific, owned action items.
