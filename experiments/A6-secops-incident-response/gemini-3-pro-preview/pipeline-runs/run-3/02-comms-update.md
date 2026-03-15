---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A6
tier: pipeline
run: 3
stage: 02-incident-comms
---

## Incident Update: Customer data exposed via misconfigured API endpoint
**Severity:** SEV1 | **Status:** Resolved
**Impact:** 2,847 customer records (name, email, account tier) exposed via unauthenticated API endpoint
**Last Updated:** 2026-03-10 14:30

### Current Status
The incident is resolved. The unauthenticated API endpoint has been secured with a hotfix. We have confirmed that 2,847 records were potentially exposed over an 11-day period. Legal has recommended voluntary notification to affected customers.

### Actions Taken
- Identified the root cause as a `@Public` annotation error on the `/api/v2/customers/export` endpoint.
- Deployed a hotfix to enforce proper authentication (verified).
- Analyzed traffic logs to identify the scope of access (23 requests, 4 unique IPs).
- Completed legal assessment regarding notification obligations.

### Next Steps
- Postmortem analysis to be conducted by the team.
- Drafting and sending voluntary notifications to the 2,847 affected customers.

***

### Customer Communication (Draft)
> **Subject**: Security Update: Data Export Feature
>
> We have resolved a security issue affecting the customer data export feature. A configuration error temporarily allowed unauthenticated access to limited contact information (name, email, account tier). The issue has been identified and fixed.
>
> We are contacting the affected users directly to provide further details.
>
> **Next Update**: N/A - Incident Resolved
