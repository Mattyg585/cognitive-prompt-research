---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A6
tier: pipeline
run: 1
stage: incident-triage-recorder
---

### Incident Record (YAML)
```yaml
incident_id: Unknown
title: Customer data exposed via misconfigured API endpoint
status: Resolved
start_time: 2026-03-01 15:00 UTC
reported_by: Security researcher via security@company.com
impact: 2,847 customer records (name, email, account tier) were accessible via an unauthenticated API endpoint for ~11 days.
affected_systems:
  - /api/v2/customers/export endpoint
  - Admin dashboard backend/API service
affected_users:
  - Customers with exposed records (2,847)
severity: SEV1
severity_rationale: Unauthenticated access to customer data with confirmed exposure across thousands of records.
signals:
  - Responsible disclosure email with screenshot showing unauthenticated access
  - Server logs showing 23 requests from 4 IPs to the endpoint
  - Endpoint returned 200 OK with customer data to unauthenticated requests
timeline:
  - time: 2026-03-01 14:00 UTC
    event: Feature branch merged adding /api/v2/customers/export; @Public used instead of @AdminOnly.
  - time: 2026-03-01 14:30 UTC
    event: CI/CD pipeline and tests pass; security scan passes.
  - time: 2026-03-01 14:45 UTC
    event: Deployed to staging; QA validates functionality.
  - time: 2026-03-01 15:00 UTC
    event: Deployed to production; endpoint live.
  - time: 2026-03-01 to 2026-03-10
    event: Endpoint accessible without authentication; 23 requests from 4 IPs.
  - time: 2026-03-10 09:15 UTC
    event: Security researcher reports unauthenticated access via email.
  - time: 2026-03-10 09:45 UTC
    event: On-call security engineer verifies issue and pages incident commander.
  - time: 2026-03-10 10:00 UTC
    event: SEV1 incident declared; war room opened and roles assigned.
  - time: 2026-03-10 10:15 UTC
    event: Hotfix deployed changing @Public to @AdminOnly.
  - time: 2026-03-10 10:30 UTC
    event: Hotfix verified; endpoint secured.
  - time: 2026-03-10 11:00 UTC
    event: Log analysis begins; 23 requests from 4 IPs identified.
  - time: 2026-03-10 12:00 UTC
    event: Legal notified; breach assessment starts; 2,847 records confirmed exposed.
  - time: 2026-03-10 13:00 UTC
    event: Legal recommends voluntary notification to affected customers.
  - time: 2026-03-10 14:22 UTC
    event: Incident resolved.
actions_taken:
  - Verified vulnerability and declared SEV1 incident
  - Hotfix deployed to require @AdminOnly authentication
  - Verified unauthenticated requests return 401
  - Performed log analysis of endpoint access
  - Notified legal and initiated breach assessment
  - Drafted customer notification
roles:
  incident_commander: TBD
  comms: TBD
  responders:
    - TBD (on-call security engineer)
    - TBD (engineering team)
    - TBD (security team)
    - TBD (legal)
open_questions:
  - What is the incident ID for tracking and follow-up?
  - Which specific customers were impacted (final list)?
  - Were any of the two unknown IPs malicious, and was data exfiltrated beyond observed requests?
  - Are there any other endpoints with incorrect authorization annotations?
  - Who are the named incident commander and comms owner for records?
```

### Triage Summary (Markdown)
```markdown
## Triage Summary: Customer data exposed via misconfigured API endpoint
**Current status:** Resolved
**Impact (who/what):** 2,847 customer records (name, email, account tier) were accessible via an unauthenticated API endpoint for ~11 days.
**Affected systems/users:** /api/v2/customers/export endpoint; customers with exposed records (2,847)
**Signals observed:** Responsible disclosure email with screenshot; server logs showing unauthenticated access and 23 requests from 4 IPs
**Known timeline:**
- 2026-03-01 15:00 UTC Deployed to production; endpoint live
- 2026-03-10 09:15 UTC Researcher reports unauthenticated access
- 2026-03-10 10:15 UTC Hotfix deployed to require @AdminOnly
- 2026-03-10 10:30 UTC Hotfix verified; endpoint secured
- 2026-03-10 14:22 UTC Incident resolved

**Severity:** SEV1 — Unauthenticated access to customer data with confirmed exposure across thousands of records.

**Immediate actions:**
- Applied hotfix to enforce authentication
- Analyzed logs for access scope and IPs
- Notified legal and initiated breach assessment
- Drafted customer notification

**Open questions / info needed:**
- Final list of affected customers and confirmation of data exfiltration by unknown IPs
- Named incident commander and comms owner
- Whether other endpoints have incorrect authorization annotations
```
