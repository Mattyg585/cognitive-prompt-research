---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A6
tier: pipeline
run: 3
stage: 01-incident-commander
---

**Status**: Resolved
**Severity**: SEV1
**Impact**: 2,847 customer records exposed via unauthenticated API endpoint
**Current Action**: Incident resolved; initiating postmortem process

# Incident Commander Handoff

The incident is now resolved. I am handing off to **incident-postmortem** to conduct the root cause analysis and generate the final report.

## Incident Summary
- **Title**: Customer data exposed via misconfigured API endpoint
- **Severity**: SEV1
- **Duration**: 4 hours 22 minutes (detected to resolved)
- **Date**: 2026-03-10
- **Impact**: 2,847 customer records (name, email, account tier) accessible via unauthenticated API endpoint for approximately 11 days before detection.

## Timeline
- **Mar 1, 14:00**: Feature branch merged with `/api/v2/customers/export` endpoint using `@Public` instead of `@AdminOnly`.
- **Mar 1, 14:30**: CI/CD passed (tests and security scan did not catch missing auth).
- **Mar 1, 15:00**: Deployed to production.
- **Mar 1–10**: Endpoint live. Logs show 23 requests from 4 unique IP addresses (19 returned data).
- **Mar 10, 09:15**: Security researcher reports vulnerability via email.
- **Mar 10, 09:45**: On-call security engineer verifies and pages IC.
- **Mar 10, 10:00**: **Incident Declared SEV1**. War room opened.
- **Mar 10, 10:15**: Engineering identifies `@Public` annotation error. Hotfix deployed.
- **Mar 10, 10:30**: **Hotfix verified**. Endpoint secured (returns 401).
- **Mar 10, 11:00**: Log analysis links 2 IPs to researcher, 2 IPs unknown.
- **Mar 10, 12:00**: Legal assessment begins. 2,847 records confirmed exposed.
- **Mar 10, 13:00**: Legal determines no mandatory notification threshold met; recommends voluntary notification.
- **Mar 10, 14:22**: **Incident Resolved**.

## Response Notes
- **Successes**: Rapid handling of disclosure (30m), fast hotfix deployment (30m), effective legal engagement.
- **Failures**: 11-day exposure window, lack of automated auth checks, incomplete QA (tested functionality only), attribution gap for 2 unknown IPs.
- **Discussion Points**: Need for unauthenticated endpoint testing, CI checks for `@Public`, WAF rules for new endpoints, "secure by default" code changes.

@incident-postmortem: Please proceed with the Root Cause Analysis (5 Whys) and generate the full blameless postmortem.