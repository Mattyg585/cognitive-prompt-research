## Action Items

**Incident**: Customer data exposed via misconfigured API endpoint

### Immediate Actions

#### Audit all existing endpoints for annotation-based authorization correctness

**What**: Run a one-time automated scan of every endpoint in the codebase that uses annotation-based access control. For each endpoint, make an unauthenticated request and verify the response matches the declared annotation. `@AdminOnly` and other restricted annotations should return 401. `@Public` endpoints should be confirmed as intentionally public. Produce a report of any mismatches.

**Addresses**: Evidence gap -- "It is not known whether other endpoints in the system have similar annotation errors." Also addresses Systemic Vulnerability -- "Authorization is a single-point-of-failure configuration property" -- by determining the current scope of exposure before systemic fixes are in place.

**Rationale**: The causal analysis identifies that the annotation mechanism's vulnerability is not specific to this endpoint -- it applies to every endpoint in the system. Before any systemic fix is designed and implemented, the organisation needs to know whether other endpoints are currently misconfigured. This is a scoping action: it determines the size of the problem. The systemic fix addresses the future; this audit addresses the present.

**Owner**: Security engineering team.

**Trade-offs**: This produces a point-in-time snapshot, not ongoing protection. Any endpoint deployed after the audit and before systemic controls are in place would not be covered. The audit also requires a working definition of "intentionally public" for each endpoint, which may require input from feature teams who own the endpoints.

---

#### Implement alerting on unauthenticated access to endpoints serving sensitive data

**What**: Configure log-based alerts for unauthenticated requests that receive successful (200) responses from endpoints that access customer data, PII, or other sensitive data sources. The server logs already capture the necessary signals -- the gap is that no rule consumes them. Start with a focused rule: any 200 response to an unauthenticated request on endpoints tagged as serving customer data should trigger a high-priority alert to the security on-call.

**Addresses**: Root Cause 3 -- "No runtime detection mechanism for unauthorized access to sensitive endpoints." Also addresses the detection assessment finding: "The data needed for detection existed... They are not being read."

**Rationale**: This is a targeted fix that directly closes the detection gap that allowed an 11-day exposure window. The causal analysis and response evaluation both emphasise that the logs existed and contained the evidence -- the gap was between data collection and data analysis. This intervention bridges that specific gap. It is a surface-level fix relative to the deeper detection architecture redesign (see Longer-Term Investments), but it is implementable immediately using existing log infrastructure and directly addresses the failure mode that materialised.

**Owner**: Security engineering team, with input from the infrastructure/platform team that manages logging and alerting infrastructure.

**Trade-offs**: This rule will only cover endpoints that are already identified as serving sensitive data. Endpoints that are misclassified or newly created without the appropriate tags will not be covered. There is also a tuning challenge: the rule needs to distinguish between endpoints that are legitimately public (and should serve 200 responses to unauthenticated requests) and endpoints that are supposed to be restricted. False positives during initial rollout are likely and will need refinement.

---

#### Continue investigation of the two unattributed IP addresses

**What**: Assign a security analyst to exhaust available attribution methods for the two unattributed IPs that accessed customer data during the exposure window. This includes reverse DNS, geolocation, threat intelligence feed lookups, correlation with any other access logs across the organisation's systems, and checking whether the IPs appear in known scanner/crawler databases. Document findings regardless of outcome -- including a determination of "unattributable" if that is the result.

**Addresses**: Response gap -- "Unattributed IP investigation was not resolved at incident close." Also addresses the response pattern: "Post-incident investigation was bounded by the incident window, not by the questions that remained open."

**Rationale**: The legal determination that mandatory notification was not required was made with this uncertainty unresolved. If the unattributed IPs represent malicious access, the risk profile may differ from the legal assessment's assumptions. More broadly, closing this investigation thread is necessary for honest accounting of the incident's impact. This is a bounded, concrete task with a clear end state (attributed or documented as unattributable).

**Owner**: Security operations / threat intelligence team.

**Trade-offs**: Attribution may prove impossible, in which case the effort produces only a documented conclusion rather than actionable intelligence. However, the documentation itself has value -- it establishes whether the organisation has done due diligence in assessing the scope of the exposure.

---

### Near-Term Actions

#### Add authorization boundary tests to the CI/CD pipeline

**What**: For every endpoint that uses annotation-based access control, add an automated test that makes an unauthenticated request and asserts the expected response code. Endpoints annotated `@AdminOnly` must return 401 to unauthenticated requests. Endpoints annotated `@Public` must return 200 (or appropriate success code). These tests run in CI on every pull request and block merge on failure. The tests should be generated from or validated against the endpoint annotations to prevent drift.

**Addresses**: Root Cause 2 -- "No checkpoint in the development-to-production path tests authorization boundaries." Also addresses Contributing Factor -- "Authenticated-session testing created a structural blind spot in QA."

**Rationale**: The causal analysis identifies that the testing suite was substantial (247 tests) but entirely scoped to functional correctness and dependency vulnerabilities. The property that failed -- "does this endpoint enforce authentication?" -- is trivially testable (make an unauthenticated request, assert 401) but was never tested. This intervention directly closes that gap. It matches the cause depth: the cause was a systematic absence of authorization-boundary testing across the pipeline, and the fix introduces systematic authorization-boundary testing across the pipeline.

**Owner**: Engineering team that owns the CI/CD pipeline, with security engineering providing the test patterns and reviewing coverage.

**Trade-offs**: This adds test execution time to every PR. The tests also need to be maintained as endpoints are added, removed, or reclassified. If the tests are generated from annotations, they test that the annotation is enforced but not that the annotation is correct -- that is a separate problem (see the longer-term investment in authorization model redesign). A test that asserts `@Public` returns 200 will pass even if `@Public` was the wrong annotation for that endpoint.

---

#### Add QA procedure for authorization boundary testing in staging

**What**: Add a step to the QA checklist for any feature involving access-controlled endpoints: test the endpoint from an unauthenticated session and from sessions with insufficient privileges, verifying that access is correctly denied. Document this as a required step in the QA process for any feature that creates or modifies endpoints.

**Addresses**: Contributing Factor -- "Authenticated-session testing created a structural blind spot in QA." Also addresses the human factors finding: "QA followed the procedure, and the procedure did not include the test that would have caught this."

**Rationale**: The causal analysis is explicit that QA did not fail -- QA followed a process that did not include authorization boundary testing. The fix is to the process, not to QA's judgment. This is appropriately scoped: it changes what QA tests, not how QA operates. The automated CI tests (above) provide a safety net, but manual QA verification from an unauthenticated context adds a human checkpoint that catches cases the automated tests might miss (e.g., endpoints not yet covered by automated test generation).

**Owner**: QA team lead, with security engineering providing guidance on test scenarios.

**Trade-offs**: Adds time to the QA cycle for any feature involving endpoints. The effectiveness depends on the QA team understanding what "authorization boundary testing" means in practice, which may require a brief training session. There is also a risk that this becomes a checkbox exercise over time -- the team should consider periodic review of whether the procedure is being followed meaningfully.

---

#### Establish a formal handoff process between incident response and post-incident investigation

**What**: When an incident is closed, the incident commander produces a "handoff memo" listing open questions, unresolved investigation threads, and follow-up actions that were deferred during the incident. This memo is assigned to a specific owner (typically the security team lead or engineering manager) with a due date for either completing the follow-up or documenting why it was closed without resolution.

**Addresses**: Response pattern -- "Post-incident investigation was bounded by the incident window, not by the questions that remained open." Specifically addresses the unattributed IPs, the absence of an other-endpoints review, and the undetermined monitoring gap -- all of which were open at incident close.

**Rationale**: The response evaluation identifies a structural gap: the incident response was effective at answering "what happened and is it fixed?" but did not systematically hand off "what else should we check?" The fix matches the cause: it is a process intervention for a process gap. The memo format is lightweight -- it does not add bureaucracy to incident response, it adds a single structured output at the end.

**Owner**: Incident response process owner (whoever maintains the incident response playbook).

**Trade-offs**: This adds one deliverable to incident closure, which in high-frequency incident environments could become burdensome. The memo is only valuable if follow-up is actually tracked and completed -- without accountability mechanisms, it becomes documentation that is written and ignored.

---

#### Evaluate and scope the Snyk configuration relative to actual security testing needs

**What**: Review the current Snyk configuration and its position in the CI/CD pipeline. Clarify in pipeline documentation what the Snyk scan does and does not cover. Evaluate whether Snyk or another tool can be configured to perform application-level security checks (e.g., endpoint authorization verification) in addition to dependency vulnerability scanning. If it can, configure it. If it cannot, document the gap explicitly so the team knows what the "security scan" step actually provides.

**Addresses**: Contributing Factor -- "The Snyk security scan provided a false sense of security coverage."

**Rationale**: The causal analysis identifies that the presence of a "security scan" in the pipeline likely contributed to confidence that security properties were being verified, when in fact the scan only covered dependency vulnerabilities. The intervention is to close the gap between what the scan provides and what the team believes it provides. This can be done either by expanding the scan's scope or by making the scope explicit. Either way, the false confidence is addressed.

**Owner**: Security engineering team, with the platform/DevOps team that manages CI/CD configuration.

**Trade-offs**: Expanding the scan scope may increase CI execution time and introduce new false positives. If the evaluation determines that Snyk cannot cover application-level authorization, the "fix" is documentation -- which addresses false confidence but does not add new detection capability.

---

### Longer-Term Investments

#### Redesign authorization to include defense in depth

**What**: Move from a single-annotation authorization model to a layered model where authorization is enforced at multiple levels. Options include: an API gateway that independently enforces authentication requirements based on endpoint classification, a data-layer authorization check that verifies the requesting context before returning PII, or a network-level segmentation that routes sensitive-data endpoints through a separate authentication-required path. The goal is that no single configuration error -- at any layer -- results in unauthenticated access to customer data.

**Addresses**: Systemic Vulnerability -- "Authorization is a single-point-of-failure configuration property." Also addresses Root Cause 1 at its deepest identified level: "The deeper issue is the complete absence of a verification layer."

**Rationale**: This is the systemic intervention for the deepest systemic cause. The annotation mechanism itself is not the problem -- annotations are a reasonable access control pattern. The problem is that the annotation is the only barrier. Any system where a single human error directly exposes customer data has a design problem, regardless of how many tests or alerts are layered on top. The tests and alerts (see Near-Term Actions) reduce the probability of the error reaching production or persisting undetected, but they do not eliminate the single-point-of-failure architecture. This intervention does. It is a significant engineering investment, which is appropriate given that the cause it addresses is architectural.

**Owner**: Architecture / platform engineering team, with security engineering providing requirements and threat modeling.

**Trade-offs**: Defense-in-depth authorization adds complexity to the system. Multiple enforcement layers mean multiple places where authorization logic must be maintained and kept consistent. If layers disagree (e.g., the gateway allows but the data layer denies), debugging becomes harder. The implementation needs to be designed so the layers reinforce each other without creating a maintenance burden that leads to one layer being abandoned or allowed to drift. There is also a performance consideration if authentication checks are added at multiple layers.

---

#### Build a detection architecture oriented toward confidentiality, not just availability

**What**: Design and implement a monitoring strategy that covers confidentiality events, not just availability and performance. This includes: alerting on access pattern anomalies for sensitive endpoints (new IPs, unusual volumes, unauthenticated access), periodic automated verification that endpoint authentication configurations match their intended state, and log analysis rules that surface authorization-relevant events. This goes beyond the immediate alerting fix (see Immediate Actions) by building a systematic detection capability rather than a point rule.

**Addresses**: Systemic Vulnerability -- "Detection architecture is oriented toward availability, not confidentiality." Also addresses the detection assessment: "The detection gap is not specific to this endpoint... The detection gap is systemic, not incident-specific."

**Rationale**: The immediate alerting rule (see Immediate Actions) closes the specific gap that materialised in this incident. This longer-term investment addresses the broader pattern: the organisation can detect when things go down but not when things leak. The causal analysis identifies this as a systemic vulnerability that extends beyond this endpoint to any data exposure that does not cause a functional symptom. A comprehensive confidentiality-oriented detection capability addresses the category, not just the instance. This matches the cause depth: the cause is architectural (the monitoring system was designed for availability), and the fix is architectural (redesign the monitoring strategy to include confidentiality).

**Owner**: Security engineering team, with infrastructure/platform team providing the monitoring and alerting platform capabilities.

**Trade-offs**: Confidentiality-oriented monitoring generates a different alert profile than availability monitoring. Availability alerts tend to be high-signal (something is obviously down). Confidentiality alerts are often lower-signal and require investigation (is this access pattern suspicious, or is it a new legitimate integration?). The team will need to invest in alert triage capability and accept a higher investigation-to-incident ratio. Without this investment, the alerts will be ignored, which recreates the detection gap at a different level.

---

#### Address the systemic testing blind spot around security-as-configuration

**What**: Conduct a broader review of the testing philosophy to identify other properties that are declared through configuration but never tested from the perspective of an adversary or unauthorized user. Authorization annotations are one instance, but the pattern may extend to: rate limiting configuration, CORS policies, data retention settings, encryption-at-rest configuration, and other security properties that are set through configuration rather than enforced through code logic. For each identified property, determine whether a test exists that verifies the property from the outside (i.e., from the perspective of someone who should be denied), and add tests where gaps are found.

**Addresses**: Systemic Vulnerability -- "The test architecture has a systematic gap around security-as-configuration." Also addresses the causal analysis observation: "the team may be testing what the system does but not testing what the system prevents."

**Rationale**: The near-term CI test addition (see Near-Term Actions) addresses authorization boundary testing specifically. This longer-term investment addresses the broader pattern the causal analysis identified: the testing philosophy is oriented toward functional correctness, not toward verifying security properties. The causal analysis notes that this gap "likely extends beyond this endpoint to any security property that is declared through configuration rather than enforced through code logic." Fixing only the authorization testing gap leaves the broader blind spot intact. This intervention matches the systemic depth of the finding.

**Owner**: Engineering leadership, with security engineering providing the security-properties inventory and test requirements.

**Trade-offs**: This is a large scoping exercise that could expand indefinitely. It needs to be bounded -- start with properties that protect customer data and expand from there. There is also a cultural dimension: shifting a team's testing philosophy from "test what it does" to "also test what it prevents" requires changing mental models, not just adding tests. The tests themselves are often simple, but identifying which properties to test requires a different way of thinking about the system.

---

### Findings Not Addressed

#### Code review process gap

The causal analysis identifies an evidence gap: "The record does not document whether a code review occurred before the feature branch was merged." It is unknown whether a reviewer saw the `@Public` annotation and approved it, missed it, or whether no review occurred. The causal analysis notes these have different systemic implications -- a missed annotation suggests review processes are insufficient for catching security-relevant configuration; no review suggests the merge process lacks a required gate. **No action item is generated because the appropriate intervention depends on which of these is true.** Before designing a fix (e.g., requiring security-focused review for changes to access control annotations, or adding a merge gate that requires review), the organisation should first determine what actually happened. This is a follow-up investigation item, not an action item.

#### Request access pattern characterization during the exposure window

The causal analysis notes that the distribution of the 23 requests over the 9-day exposure period is unknown -- whether access was concentrated (suggesting targeted activity) or spread out (suggesting scanning). The IP attribution follow-up (see Immediate Actions) partially addresses this, but the full access pattern characterization is not addressed by any action item. **This is an investigative gap, not an intervention gap.** The characterization would inform severity assessment and potentially change the risk profile, but the action it would produce (if any) cannot be determined until the analysis is done.

#### Why no authorization testing existed

The causal analysis identifies the deepest unanswered causal question: why was authorization boundary testing never implemented despite a comprehensive test suite? Was it a conscious decision, a deprioritization, or a conceptual blind spot? **The near-term action item (add authorization boundary tests) addresses the gap itself. The systemic testing review (see Longer-Term Investments) addresses the pattern. But neither addresses the organisational question of how the gap formed.** Understanding this would inform whether the organisation has a prioritization problem, a risk-awareness problem, or a cultural blind spot around security testing. This is a retrospective learning question rather than an actionable intervention, and it may be addressed during the postmortem discussion itself rather than through a formal action item.

#### Monitoring architecture -- known gap vs. unconsidered gap

The causal analysis notes uncertainty about whether the monitoring gap was known and accepted or simply never considered. **The immediate alerting fix and the longer-term detection architecture redesign address the gap regardless of how it formed.** However, understanding whether this was a conscious risk acceptance or an oversight has implications for how the organisation manages risk decisions. If it was a known, accepted risk, then the risk acceptance process may need review (was the risk accurately assessed?). If it was never considered, then the organisation may need a systematic process for identifying monitoring gaps. This distinction is important but cannot be resolved without further investigation into the monitoring team's history of decisions.

#### Disclosure channel speed

The response evaluation notes that the 30-minute verification window is reasonable for an email-based disclosure channel, and that a dedicated reporting portal or bug bounty platform could compress this. **No action item is generated because the detection gap (11 days) dwarfs the disclosure-to-verification gap (30 minutes).** Improving the disclosure channel would save minutes; improving detection would save days. The detection improvements (see Immediate Actions and Longer-Term Investments) are higher-leverage. A dedicated vulnerability disclosure program may be worth considering independently, but it does not address any root cause or significant response gap from this incident.