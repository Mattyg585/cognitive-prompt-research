## Postmortem: Customer Data Exposed via Misconfigured API Endpoint
**Date**: 2026-03-10 | **Duration**: 11 days exposure, 4 hours 22 minutes detection-to-resolution | **Severity**: SEV1
**Authors**: Security Engineering, Incident Response Team | **Status**: Draft

### Summary

On March 1, a new API endpoint intended for admin-only access was deployed to production with a `@Public` annotation instead of `@AdminOnly`, making customer data accessible to anyone on the internet without authentication. The misconfiguration passed through every internal checkpoint -- code merge, 247 automated tests, a Snyk security scan, and QA testing in staging -- because none of these checkpoints tested whether the endpoint enforced authentication. The endpoint remained open for 11 days, during which 19 successful requests from 4 IP addresses returned data on 2,847 customers (names, email addresses, account tiers). No internal system detected the exposure. It was discovered only when a security researcher filed a responsible disclosure report on March 10.

Once notified, the team responded effectively: the vulnerability was verified within 30 minutes, a SEV1 was declared, and a hotfix was deployed within 30 minutes of declaration, stopping the exposure. Log analysis, legal assessment, and customer notification followed in a structured sequence. Legal determined mandatory breach notification was not required, but voluntary notification was recommended and accepted.

The root causes are architectural, not individual. Authorization depends on a single annotation with no defense in depth. The testing strategy verifies what the system does but not what it prevents. The monitoring architecture detects when things go down but not when things leak. Immediate actions include auditing all existing endpoints for similar misconfigurations and implementing alerting on unauthenticated access to sensitive data endpoints. Longer-term, the organisation is investing in defense-in-depth authorization, confidentiality-oriented detection, and a systematic review of security properties that are declared through configuration but never tested.

### Impact

**Data exposed**: 2,847 customer records containing name, email address, and account tier. The exposed data did not include passwords, payment information, or sensitive personal data beyond email addresses.

**Exposure window**: Approximately 11 days (March 1, 15:00 UTC to March 10, 10:30 UTC).

**External access**: 23 requests from 4 unique IP addresses during the exposure window. 19 requests returned customer data; 4 returned empty results. Two IP addresses were attributed to the security researcher who filed the disclosure. Two remain unattributed at incident close.

**Legal determination**: Mandatory notification thresholds under applicable privacy laws were not met. Voluntary notification to affected customers was recommended by legal and accepted by the team.

**Unknown impact**: The identity and intent of the two unattributed IP addresses remain unknown. Whether data returned to those addresses has been stored, shared, or used cannot be determined from the available evidence. The distribution of the 23 requests across the 11-day window is not documented, so the pattern of access -- whether it was targeted or opportunistic -- is not characterised.

### Timeline

**March 1, 14:00 UTC** -- Feature branch merged containing a new `/api/v2/customers/export` endpoint. The endpoint was intended for admin-only access as part of an internal dashboard. The developer selected `@Public` instead of `@AdminOnly` via IDE autocomplete. The developer believed the endpoint was correctly secured.

**March 1, 14:30 UTC** -- CI/CD pipeline ran. All 247 unit tests passed. Integration tests passed. Snyk security scan passed. The Snyk scan was configured for dependency vulnerability checking only -- it did not assess application-level authorization. No test in the pipeline verified whether the endpoint required authentication.

**March 1, 14:45 UTC** -- Application deployed to staging. QA tested the export functionality from an authenticated admin session. The endpoint returned customer data correctly. From an authenticated session, the endpoint behaves identically whether annotated `@Public` or `@AdminOnly`. QA approved the deployment.

**March 1, 15:00 UTC** -- Application deployed to production. The endpoint was live on the public internet, accessible without authentication. No monitoring, WAF rule, or API gateway policy existed to detect unauthenticated traffic to the endpoint.

**March 1 to March 10** -- The endpoint remained open. Server logs recorded 23 requests from 4 unique IP addresses. 19 returned customer data. No alert fired. No team had awareness of the unauthorized access. The logs contained the evidence, but no process consumed them for this type of event.

**March 10, 09:15 UTC** -- A security researcher emailed security@company.com with a responsible disclosure report, including a screenshot demonstrating unauthenticated access to customer data. This was the first time anyone inside the organisation became aware of the exposure.

**March 10, 09:45 UTC** -- On-call security engineer read the email, independently verified the vulnerability, and paged the incident commander.

**March 10, 10:00 UTC** -- SEV1 declared. War room opened. Incident commander assigned roles. Severity was assessed on the nature of the exposure (customer data, public endpoint) without waiting to quantify scope.

**March 10, 10:15 UTC** -- Engineering identified the `@Public` annotation as the cause and deployed a hotfix changing it to `@AdminOnly`. The fix was deployed directly rather than through the full deployment pipeline, given the endpoint was actively exposing data.

**March 10, 10:30 UTC** -- Hotfix verified in production. Endpoint confirmed returning 401 for unauthenticated requests. Exposure stopped.

**March 10, 11:00 UTC** -- Security team began log analysis. Identified 23 requests from 4 unique IPs. Two IPs matched the security researcher. Two were unknown and unattributed.

**March 10, 12:00 UTC** -- Legal notified. Exposed dataset confirmed as 2,847 records containing name, email address, and account tier. No passwords, payment data, or sensitive PII beyond email.

**March 10, 13:00 UTC** -- Legal completed assessment. Mandatory notification threshold not met. Voluntary notification recommended.

**March 10, 14:22 UTC** -- Incident resolved. Customer notification drafted. Internal communications sent.

**Gaps in the timeline record**: The code review process for the feature branch is undocumented -- it is unknown whether a review occurred, or what it covered if it did. The distribution of the 23 requests across the 11-day exposure window is not detailed. The hotfix deployment process (whether it went through an abbreviated pipeline or was deployed directly) is not documented. No review of other endpoints for similar misconfigurations was conducted during the incident.

### Root Cause Analysis

The causal structure of this incident is converging, not linear. Multiple independent factors had to co-exist for this outcome. Removing any one of several factors would have either prevented the misconfiguration from reaching production or reduced the exposure window from 11 days to minutes or hours.

#### Root Cause 1: Authorization is a single-point-of-failure configuration property with no verification layer

The entire access control decision for the endpoint rested on a single annotation. `@Public` and `@AdminOnly` are two options in an IDE autocomplete menu -- the difference is a single selection. There is no compile-time check, no static analysis rule, no integration test, and no deployment gate that verifies the authorization state of an endpoint matches its intended access level.

The annotation mechanism itself is reasonable -- annotation-based access control is a common and valid pattern. The deeper issue is the complete absence of any verification layer. The annotation is the only barrier between the public internet and customer data. There is no API gateway enforcing authentication independently, no network segmentation routing sensitive endpoints differently, no data-layer check verifying the requesting context before returning PII. A single human error at a single moment -- with no second check at any subsequent stage -- directly exposed customer data.

This vulnerability is not specific to this endpoint. It applies to every endpoint in the system that relies solely on annotation-based access control.

#### Root Cause 2: No checkpoint in the development-to-production path tests authorization boundaries

The path from code to production included multiple checkpoints: code merge, 247 automated tests, integration tests, a Snyk security scan, and QA testing in staging. None tested whether the endpoint enforced authentication from an unauthenticated context.

Each checkpoint operated correctly within its scope:
- CI/CD tested functional behavior -- the endpoint returned correct data
- Snyk tested dependency vulnerabilities -- no known CVEs in dependencies
- QA tested feature behavior from an authenticated session -- the export worked

All checkpoints passed. The results were accurate for what was tested but collectively provided false confidence about authorization. The testing suite was substantial in volume but uniform in coverage -- every checkpoint tested a different facet of functional correctness while none tested the security property that failed. Confidence accumulated across checkpoints without coverage expanding.

#### Root Cause 3: No runtime detection mechanism for unauthorized access to sensitive endpoints

Once the misconfigured endpoint was live, no monitoring, alerting, or analysis existed to detect unauthenticated access to an endpoint serving customer data. The endpoint served 19 successful data-returning requests over approximately 9 days with zero internal alerts.

The server logs captured all 23 requests. The data needed for detection was being collected in real time. The gap was not in data collection but in data analysis -- no alerting rule, no log review process, no anomaly detection consumed the logs for authorization-relevant signals. The monitoring architecture appears oriented toward availability and performance. The system can detect when an endpoint goes down. It cannot detect when an endpoint is accessed by someone who should not have access.

This detection gap is systemic, not incident-specific. Any endpoint with a similar misconfiguration -- now or in the future -- would have the same extended exposure window, bounded only by whether an external party happened to notice.

#### Contributing factors

**Authenticated-session QA testing created a structural blind spot.** QA tested the endpoint from an authenticated admin session, following its established process. From that vantage point, the endpoint behaved identically whether annotated `@Public` or `@AdminOnly`. QA did not fail to follow its process -- it followed a process that did not include the test that would have caught this misconfiguration.

**The Snyk security scan provided a false sense of security coverage.** The presence of a "security scan" in the CI/CD pipeline likely contributed to confidence that security properties were being verified. The scan was doing legitimate work (dependency vulnerability checking), but its presence may have masked the absence of application-level security testing. A pipeline with a security scan feels more secure than one without, even when the scan's scope does not cover the failure mode in question.

**The misconfiguration caused zero functional symptoms.** The wrong annotation did not break anything. No errors, no degradation, no user complaints. The system behaved exactly as it would have with the correct annotation from the perspective of legitimate users. Security misconfigurations that cause functional symptoms get caught quickly. This one was silent, and the silence was interpreted as health.

#### Systemic vulnerabilities

The causal analysis identifies four systemic vulnerabilities that extend beyond this incident:

1. **Authorization is a single point of failure** -- any annotation error on any endpoint directly exposes whatever data that endpoint serves, with no independent enforcement layer.

2. **The testing philosophy verifies what the system does but not what it prevents** -- the 247-test suite thoroughly covers functional behavior while security-relevant configuration is untested. This gap likely extends to other configuration-declared security properties: rate limiting, CORS policies, data retention settings.

3. **The detection architecture is oriented toward availability, not confidentiality** -- the organisation can detect outages but not data leaks. Any exposure that does not cause a functional symptom would go undetected until externally reported.

4. **Confidence accumulates across checkpoints without coverage expanding** -- multiple passing checkpoints create compound confidence even when their coverage overlaps rather than complements. The quantity of positive signals substitutes for breadth of signal coverage.

#### Human factors

The developer's annotation error was shaped by tooling that makes the error easy and provides no feedback. Two options in an autocomplete menu, a single selection, no compile-time warning that a public annotation is applied to an endpoint accessing customer data. In this information environment, the error is predictable -- a reasonable developer working at normal speed would make this error at some non-trivial rate.

QA's testing approach was shaped by a process that did not include authorization boundary testing. QA followed procedure correctly; the procedure did not cover this failure mode. The gap was in process design, not in QA's judgment.

The on-call engineer, incident commander, and response team operated with appropriate speed given the information available. The 30-minute verification window was reasonable for an email-based disclosure channel. The 30-minute declaration-to-fix window was fast for a production change. The systemic failure was not in response speed but in the 11-day gap before anyone learned there was a problem.

### Response Evaluation

#### What worked well

**Rapid escalation and correct severity classification.** Once the security researcher's report arrived, the on-call engineer verified, escalated, and the incident was declared SEV1 within 45 minutes. The team correctly treated "confirmed customer data accessible without authentication" as sufficient for SEV1 without waiting to quantify scope. This meant the full incident response apparatus was available from the start.

**Fast and appropriate technical remediation.** The root cause was identified and a hotfix deployed within 15 minutes of incident declaration. The team made the correct trade-off: deploying a one-line annotation change directly rather than routing through the full deployment pipeline while the endpoint was actively leaking. The fix was verified in production rather than assumed.

**Methodical post-containment investigation.** After the endpoint was secured, the team maintained structure through containment, quantification (log analysis, IP attribution), legal assessment, and communication planning. Each step informed the next. Legal was engaged after the scope was defined but before any external communication, giving legal a concrete problem to assess.

#### What fell short

**Detection depended entirely on an external party.** The incident was detected because a security researcher chose to email the company. This was not delayed detection -- it was outsourced detection. If the researcher had not been scanning, had not reported, or had reported through a different channel, the exposure window would have been longer. Responsible disclosure is not a detection strategy.

**Pre-deployment checkpoints provided accumulated false confidence.** Every gate gave a green signal. No gate tested the property that failed. The team believed a properly secured endpoint had been deployed because their entire verification chain told them so. This is a response-relevant finding because it made internal detection impossible: no one had reason to look for a problem.

**Unattributed IP investigation was not resolved at incident close.** Two of the four accessing IP addresses remained unidentified when the incident was closed. The record does not indicate whether further investigation was planned. The legal determination was made with this uncertainty unresolved.

**Post-incident investigation was bounded by the incident window, not by the open questions.** The incident was closed with several threads unresolved: the unattributed IPs, no review of other endpoints for similar issues, and no determination of whether the monitoring gap was a known accepted risk or an unconsidered one. The response answered "what happened and is it fixed?" but did not systematically hand off "what else should we check?" to a follow-up process.

### Action Items

#### Immediate

| Action | Addresses | Owner |
|--------|-----------|-------|
| **Audit all existing endpoints for annotation-based authorization correctness.** Run an automated scan making unauthenticated requests to every annotated endpoint; verify responses match declared access level. | Determines whether other endpoints are currently misconfigured -- scoping the present while systemic fixes address the future. | Security Engineering |
| **Implement alerting on unauthenticated access to endpoints serving sensitive data.** Configure log-based alerts for unauthenticated requests receiving 200 responses from endpoints accessing customer data. The logs already capture the signal; this bridges the gap between collection and analysis. | Directly closes the detection gap that allowed an 11-day exposure window. | Security Engineering + Infrastructure |
| **Continue investigation of the two unattributed IP addresses.** Exhaust available attribution methods (reverse DNS, geolocation, threat intelligence feeds, cross-system log correlation). Document findings including a determination of "unattributable" if that is the result. | Resolves the open investigative thread and determines whether the risk profile differs from the legal assessment's assumptions. | Security Operations |

#### Near-term

| Action | Addresses | Owner |
|--------|-----------|-------|
| **Add authorization boundary tests to the CI/CD pipeline.** For every annotated endpoint, add a test that makes an unauthenticated request and asserts the expected response code. Block merge on failure. | Closes the systematic absence of authorization-boundary testing across the deployment path. | Engineering (CI/CD) + Security Engineering |
| **Add QA procedure for authorization boundary testing in staging.** For any feature involving access-controlled endpoints, test from unauthenticated and insufficient-privilege sessions. | Changes the process that shaped QA's blind spot -- fixes the procedure, not QA's judgment. | QA Team Lead + Security Engineering |
| **Establish a formal handoff process between incident response and post-incident investigation.** Incident commander produces a handoff memo at closure listing open questions and unresolved threads, assigned to a specific owner with a due date. | Addresses the pattern of closing incidents before resolving investigative loose ends. | Incident Response Process Owner |
| **Evaluate and scope the Snyk configuration.** Clarify what the scan covers in pipeline documentation. Evaluate whether it can perform application-level security checks; if not, document the gap explicitly. | Closes the gap between what the security scan provides and what the team believes it provides. | Security Engineering + DevOps |

#### Longer-term

| Action | Addresses | Owner |
|--------|-----------|-------|
| **Redesign authorization to include defense in depth.** Move from single-annotation access control to a layered model (API gateway enforcement, data-layer authorization, or network segmentation) so that no single configuration error exposes customer data. | Addresses the architectural single point of failure -- the deepest systemic cause. | Architecture / Platform Engineering |
| **Build a detection architecture oriented toward confidentiality, not just availability.** Design monitoring that covers access-pattern anomalies, periodic authorization-state verification, and log analysis for authorization-relevant events -- beyond the immediate point rule. | Addresses the systemic detection gap: the organisation can detect outages but not leaks. | Security Engineering + Infrastructure |
| **Conduct a systematic review of security-as-configuration properties.** Identify all security properties declared through configuration (rate limiting, CORS, encryption-at-rest, etc.) and determine whether each is tested from an adversarial perspective. Add tests where gaps exist. | Addresses the broader testing blind spot -- the pattern of testing what the system does but not what it prevents. | Engineering Leadership + Security Engineering |

#### Findings not yet addressed by action items

- **Code review process**: Whether a review occurred and what it covered is unknown. The appropriate intervention (security-focused review requirements vs. merge gate enforcement) depends on which scenario is true. This requires follow-up investigation before an action item can be designed.
- **Access pattern characterisation**: The distribution of the 23 requests over the exposure window has not been analysed. Understanding whether access was targeted or opportunistic would inform severity assessment but cannot produce an action item until the analysis is done.
- **How the authorization testing gap formed**: The near-term and longer-term actions close the gap and address the pattern. But neither addresses the organisational question of why a 247-test suite never included this trivially testable property. Understanding whether this was a conscious deprioritisation or a conceptual blind spot has implications for how the organisation manages risk awareness.

### Lessons Learned

**The system's safety architecture was designed around functional failure, not security failure, and these are fundamentally different failure modes.** Every internal safeguard -- tests, security scans, QA, monitoring -- was designed to catch things that break. A wrong annotation does not break anything. The endpoint worked perfectly. Production operated normally for 11 days. The entire safety architecture assumes that bad states produce symptoms, and that monitoring for symptoms is equivalent to monitoring for bad states. Security misconfigurations violate this assumption. They are bad states with no symptoms. This incident reveals that the organisation's safety model has an implicit axiom -- "if nothing is broken, nothing is wrong" -- that is false for an entire class of failures. The action items add authorization tests and confidentiality monitoring, but the deeper lesson is that the safety architecture needs to be re-examined for every place it assumes that bad states are symptomatic.

**The annotation system's real failure is not that it allows errors -- it's that it provides no cognitive friction at the point where the security decision is made.** The developer selected an autocomplete suggestion. That selection was the entire security decision for an endpoint serving customer data. There was no moment of deliberation, no confirmation, no second step. The IDE offered two options; one was selected; the choice was final and invisible. Compare this to a system where deploying a public endpoint requires a separate declaration file, or where endpoints accessing PII trigger a review gate. These add friction, and friction is cost. But the lesson is that security decisions should be made in contexts that match their consequences. A decision that controls whether customer data is public should not be made in the same cognitive mode as selecting a variable name from autocomplete. The action items add verification after the fact; the lesson is about the moment of decision itself.

**Multiple independent checkpoints can produce less safety than a single well-scoped one when their coverage overlaps rather than complements.** The deployment path had four checkpoints: CI tests, security scan, QA, deployment. Each gave a green signal. The cumulative effect was high confidence. But the coverage was not additive -- each checkpoint tested a different view of functional correctness, and none tested authorization boundaries. Four overlapping checks produce more confidence than one check while providing no more coverage. This is worse than having one check and knowing it is limited, because the accumulated confidence actively suppresses the vigilance that might catch the gap. The lesson extends beyond this incident: any safety system should be evaluated not by how many checks it has but by whether the checks' coverage is complementary. If adding a checkpoint increases confidence more than it increases coverage, it has made the system less safe by masking the gap.

**The 11-day exposure window was not a detection failure -- it was a structural inevitability.** Given the system as it was configured, there was no mechanism by which this exposure could have been detected internally. Not "the monitoring missed it" -- there was nothing to miss it. Not "the team should have noticed" -- there was nothing to notice. The exposure window was not caused by slow detection; it was caused by the absence of any detection capability for this failure class. The lesson is that detection coverage, like test coverage, has an explicit scope -- and what falls outside that scope is not "unlikely to be detected" but "guaranteed to be undetected." The organisation should identify other failure classes that fall outside the current detection scope and make an explicit decision about each: build detection, accept the risk, or mitigate through prevention. The current state -- where the scope gap was not known and therefore not decided -- is the least safe configuration.

**The incident reveals a category error in how the organisation thinks about its security scan.** The CI/CD pipeline includes a "security scan" (Snyk). The team likely thinks of this as "we have security testing in our pipeline." Snyk checks whether known vulnerabilities exist in third-party dependencies. It does not assess anything about the application's own security configuration. This is like having a building inspector who checks whether the bricks meet code but does not check whether the doors lock. Both are valuable; neither substitutes for the other. The category error is treating "security" as a single domain that a single tool can cover. The lesson is that security testing has multiple, independent domains -- dependency vulnerabilities, authorization configuration, network exposure, data handling -- and coverage in one domain provides zero coverage in another. Naming a tool "security scan" when it covers one domain creates a false sense of coverage across all domains.

**The gap between "incident resolved" and "questions answered" reveals a missing organisational muscle.** The incident was closed at 14:22 with two IPs unattributed, no review of other endpoints, and no understanding of whether the monitoring gap was known or unconsidered. The incident response process is designed to answer "what happened and is it fixed?" -- and it answered that well. But no process existed to carry forward "what else should we check?" The handoff between incident response (acute, time-bounded) and post-incident investigation (methodical, completeness-oriented) is a different organisational capability from either one. The action items add a handoff memo, but the lesson is broader: the organisation's incident process is optimised for containment and resolution. Learning and systemic investigation are not structurally supported. They happen if individuals choose to pursue them, not because the process requires it.
