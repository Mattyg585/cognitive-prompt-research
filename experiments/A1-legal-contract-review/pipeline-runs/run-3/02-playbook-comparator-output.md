# Playbook Comparator Output

**Important**: This analysis assists with legal workflows but does not constitute legal advice. All findings should be reviewed by qualified legal professionals.

**Notice**: No organizational playbook was provided. This review evaluates the contract against widely-accepted commercial standards for SaaS/Cloud Service Agreements from the Customer's perspective. These standards reflect common market positions in enterprise and mid-market SaaS procurement. Organizations with specific negotiation playbooks may have stricter or different requirements than the generic standards applied here.

**Contract type**: Cloud Service Agreement (SaaS) — Standard Terms (Common Paper v2.1)
**User's side**: Customer (buyer)

---

## Deviation Analysis

### Machine Learning / AI Training Rights (Section 1.6)

**Classification**: Escalate

**Contract provision**: Provider is authorized to use both Customer Content and Usage Data to "develop, train, or enhance artificial intelligence or machine learning models" across Provider's entire product line, including third-party components. Customer explicitly "authorizes Provider to process its Usage Data and Customer Content for such purposes." De-identification is an effort-based standard: "commercially reasonable efforts consistent with industry standard technology." These rights survive termination per Section 5.6.

**Commercial standard**: Customer Content should not be used for ML/AI training without a clear opt-out mechanism, or preferably should be opt-in. Where ML training is permitted, it should be limited to improving the specific subscribed service, not Provider's entire product portfolio or third-party models. De-identification should be outcome-based, not effort-based. ML training rights over Customer Content should not survive termination.

**Gap**: The contract grants a broad, perpetual ML training license over Customer Content with no opt-out, scope extending to third-party model components and Provider's full product line, effort-based rather than outcome-based de-identification, and survival beyond termination. Once Customer Content has been used for model training, the practical reversibility is limited regardless of contractual deletion rights. This is materially beyond what current commercial standards accept.

### Security Testing Prohibition (Section 2.1(a)(v))

**Classification**: Escalate

**Contract provision**: A blanket prohibition against conducting "security or vulnerability tests on" the Product. No carveout for coordinated penetration testing with advance notice, Customer's own security due diligence, or access to third-party audit reports.

**Commercial standard**: SaaS agreements commonly either (a) permit penetration testing and security assessments with advance coordination and Provider approval, (b) provide access to third-party security audit reports (SOC 2 Type II, ISO 27001), or (c) both. A blanket prohibition without any alternative assurance pathway is not accepted practice for enterprise SaaS.

**Gap**: Absolute prohibition with no alternative pathway for security assurance. This is compounded by the complete absence of security commitments, certifications, and breach notification in the Standard Terms, creating a structural gap where Customer can neither verify nor contractually require adequate security.

### Absence of Security Commitments (Standard Terms generally)

**Classification**: Escalate

**Contract provision**: The Standard Terms contain no security standards, certifications (SOC 2, ISO 27001), encryption requirements (at rest or in transit), audit rights, or obligation for Provider to maintain any particular security posture.

**Commercial standard**: Enterprise SaaS agreements routinely include references to specific security certifications, annual audit commitments, encryption standards, and Customer audit rights (either direct or through third-party reports). These are baseline expectations for any SaaS platform processing business data.

**Gap**: Complete absence of security commitments. This is not a deviation in degree but in kind — no security floor exists in the Standard Terms. Customer has no contractual basis to require or verify any security practice.

### Absence of Data Breach Notification (Standard Terms generally)

**Classification**: Escalate

**Contract provision**: No obligation for Provider to notify Customer of security breaches, data incidents, unauthorized access to Customer Content, or compromise of Customer credentials.

**Commercial standard**: Breach notification obligations are considered essential in SaaS agreements handling business data. Standard provisions include notification within a defined timeframe (commonly 24-72 hours), description of the nature and scope of the breach, steps taken to remediate, and cooperation with Customer's incident response.

**Gap**: Total absence. No notification timeline, no notification obligation, no cooperation commitment. Even where statutory notification obligations apply independently, the contract provides no mechanism for contractual cooperation, timeline commitments, or remediation obligations.

### Suspension Rights (Section 2.2)

**Classification**: Escalate

**Contract provision**: Provider may suspend access "with or without notice." Provider will only "try to inform Customer before suspending Customer's account when practical." No maximum suspension duration, no obligation to state reasons, no timeline for reinstatement after the issue is resolved, no remedy for wrongful suspension, and no excusal of payment obligations during suspension.

**Commercial standard**: SaaS suspension provisions typically include: written notice before suspension (except for imminent security threats), stated reason for suspension, a cure period before suspension takes effect, defined maximum suspension duration, commitment to reinstate promptly upon resolution, proportional scope (affected user or component rather than entire account), and either fee credits or payment suspension during Provider-initiated suspension.

**Gap**: The contract deviates from commercial standards across every dimension of suspension governance. The cumulative effect is that Provider could suspend service indefinitely while Customer continues to pay, with Customer's only recourse being a material breach claim under Section 5.3, which itself requires 30 days' notice and a cure opportunity — during which Customer remains without access but still owes Fees.

### Absence of Service Level Agreement (Standard Terms generally)

**Classification**: Escalate

**Contract provision**: No uptime commitment, availability guarantee, performance standard, scheduled maintenance notification, or service credits. The sole warranty (Section 6.3) commits only to not materially reducing "general functionality" — a backward-looking degradation standard, not a forward-looking performance commitment.

**Commercial standard**: SaaS agreements for business applications include uptime commitments (commonly 99.5%-99.9%), defined measurement methodology, service credits for downtime, scheduled maintenance windows with advance notice, and performance metrics. SLAs may appear in an Order Form or addendum, but the Standard Terms should at minimum reference or require them.

**Gap**: Complete absence of any performance commitment. The negative warranty in Section 6.3 is categorically different from an SLA. It does not cover degraded performance, intermittent outages, latency issues, or any measurable service standard. If the Order Form is also silent, Customer has no contractual basis for availability expectations.

### Post-Termination Data Handling (Section 5.5)

**Classification**: Escalate

**Contract provision**: Deletion occurs only "upon Customer's request" and Provider has 60 days after the request. If Customer fails to request deletion, the contract imposes no affirmative obligation to delete. No data export or portability mechanism. No transition assistance. Surviving sections (1.4 and 1.6) permit continued use of Usage Data and aggregated Customer Content for ML training post-termination. Section 5.6(b) permits retention under backup or record retention policies.

**Commercial standard**: SaaS agreements should provide: a data export period prior to deletion (commonly 30-60 days) in standard, machine-readable formats; automatic deletion within a defined period after the export window (typically 30-90 days) with certification of destruction; transition assistance at reasonable rates; and clean termination of all data use rights upon agreement end.

**Gap**: Deletion is not automatic — Customer must affirmatively request it. No export mechanism exists. No transition assistance is available. Most critically, surviving ML training and Usage Data rights mean Provider retains perpetual rights to derive value from Customer's data even after nominal deletion. The commercial standard of a clean break at termination is not achieved. This warrants escalation because the compound effect of no export, request-only deletion, and surviving data use rights creates material lock-in and post-termination data risk.

### Consequential Damages Waiver Including Direct Lost Profits (Section 8.2)

**Classification**: Negotiate

**Contract provision**: Both parties waive consequential, special, indirect, exemplary, punitive, and incidental damages. The waiver explicitly captures lost profits "whether direct or indirect." Exceptions apply for Increased Claims (Cover Page variable) and breach of Section 10 (Confidentiality).

**Commercial standard**: Mutual consequential damages waivers are standard in SaaS agreements. However, the explicit inclusion of "direct" lost profits in the waiver goes beyond the standard formulation, which typically waives only indirect or consequential lost profits. Direct lost profits are often Customer's primary measure of damages for service failures and are generally recoverable under standard SaaS liability terms.

**Gap**: The "whether direct or indirect" formulation for lost profits effectively eliminates Customer's primary damages measure for service failures. Whether this gap is fully mitigated depends on the Cover Page definition of Increased Claims — if service failures qualify as Increased Claims, the exception restores lost profit recovery. Without the Cover Page, this is a meaningful narrowing of Customer's remedies.

### Liability Cap Structure — Cover Page Dependency (Section 8)

**Classification**: Negotiate

**Contract provision**: General Cap Amount, Increased Cap Amount, Increased Claims, and Unlimited Claims are all Cover Page variables. The Standard Terms establish a tiered structure but contain no amounts, no defaults, and no category assignments.

**Commercial standard**: While liability caps are often specified in order forms, the base agreement commonly establishes defaults or minimums — typically 12 months of fees paid or payable as a General Cap. IP indemnification and data breach are commonly designated as Increased Claims with a 2x-3x multiplier. Gross negligence, willful misconduct, and breach of data protection obligations are commonly uncapped.

**Gap**: Complete deferral of all liability parameters to the Cover Page with no minimum floor. If the Cover Page sets low cap amounts or fails to designate critical claims (IP infringement, data breach) as Increased or Unlimited, Customer's recovery for any breach could be severely constrained. The Standard Terms provide no backstop.

### Force Majeure Payment Carveout (Section 12.12)

**Classification**: Negotiate

**Contract provision**: Force Majeure excuses performance delays for both parties, "except Customer's payment obligations." Customer must continue paying even when Provider cannot deliver service due to force majeure. Section 5.4 provides a termination right after 30 consecutive days of material inoperability with a prorated refund, but does not address the first 30 days.

**Commercial standard**: The more balanced commercial position either suspends payment obligations during force majeure or provides service credits for periods of non-delivery. While one-sided force majeure payment carveouts exist in SaaS agreements, they are not the widely-accepted standard.

**Gap**: Customer pays for service it cannot receive during force majeure. The 30-day termination trigger provides some relief, but Customer still pays for up to 30 days of non-delivery, and the prorated refund covers only the remainder of the Subscription Period — not the period during which no service was delivered.

### GDPR-Only DPA Trigger (Section 3.1)

**Classification**: Negotiate

**Contract provision**: DPA requirement triggered only by "Personal Data governed by GDPR." No specified DPA mechanism for Personal Data under CCPA, UK GDPR, LGPD, POPIA, or other data protection regimes.

**Commercial standard**: Modern SaaS agreements increasingly address multiple privacy regimes or require a DPA for any Personal Data processing, regardless of regulatory framework. Many vendors now include a single DPA covering all applicable data protection laws.

**Gap**: The GDPR-only trigger leaves Personal Data governed by non-GDPR regimes without a specified contractual data protection framework. For a Customer operating across multiple jurisdictions, this creates compliance gaps the contract does not address.

### Absence of Subprocessor Controls (Standard Terms generally)

**Classification**: Negotiate

**Contract provision**: No restrictions on Provider's use of subprocessors or subcontractors. No notification requirements for subprocessor changes. No obligation to flow down data protection or confidentiality obligations. No right for Customer to object.

**Commercial standard**: SaaS agreements handling business data typically include: a list of current subprocessors, advance notification (commonly 30 days) of new subprocessors, Customer's right to object to new subprocessors, requirement to flow down equivalent contractual obligations, and Provider remaining liable for subprocessor actions.

**Gap**: Complete absence of subprocessor governance. Customer has no visibility into who processes its data, no advance notice of changes, no objection right, and no assurance that subprocessors are bound by equivalent obligations. This is particularly material given the ML training rights in Section 1.6 extending to "third-party components."

### Refund on Provider Material Breach Termination (Sections 4.1 / 5.3)

**Classification**: Negotiate

**Contract provision**: Fees are generally "non-refundable." Prorated refunds are explicitly provided only for warranty breach termination (Section 6.4) and force majeure termination (Section 5.4). No refund provision exists for termination due to Provider's material breach under Section 5.3.

**Commercial standard**: When Customer terminates for Provider's uncured material breach, Customer should receive a prorated refund of prepaid fees for the unused portion of the subscription period. This is a basic commercial fairness principle.

**Gap**: If Customer terminates because Provider materially breaches the agreement, Customer has no explicit right to recover prepaid fees for the remaining subscription period. Customer pays for service that Provider failed to deliver, with no contractual refund mechanism.

### Provider's Warranty (Section 6.3 / 6.4)

**Classification**: Negotiate

**Contract provision**: Provider warrants only that it "will not materially reduce the general functionality of the Cloud Service." The remedy requires Customer to notify within 45 days of discovery, then Provider has 45 days to attempt restoration. If unresolved, Customer may terminate with a prorated refund.

**Commercial standard**: Provider should warrant that the Cloud Service will perform materially in accordance with its published documentation or specifications. This is an affirmative performance standard, not merely a commitment to avoid degradation. Remedy timelines are shorter — commonly 30 days' notice with 30 days to cure.

**Gap**: The warranty is a floor (do not make it worse) rather than a standard (it will work as described). It does not cover performance degradation, intermittent issues, or failures to meet documented specifications — only "material" reductions in "general functionality." The 90-day combined remedy window (45 to notify + 45 to cure) is longer than standard and leaves Customer using a degraded service without an exit right during that period.

### Logo and Marketing Rights (Section 12.8)

**Classification**: Negotiate

**Contract provision**: "Provider may use Customer's name and logo in marketing." No consent requirement, no approval right over usage context, no usage guidelines, and no mechanism to opt out.

**Commercial standard**: Where logo rights are granted, they typically include prior written approval of specific uses, limitation to customer lists or case studies, usage guidelines, and a right to revoke. An unqualified, unconditional marketing use right is more permissive than standard.

**Gap**: Customer has no control over how its brand is used by Provider. No approval, no context limitations, no withdrawal mechanism.

### Customer Content License — "Related Offerings" Extension (Section 1.5)

**Classification**: Negotiate

**Contract provision**: Provider may "copy, display, modify, and use Customer Content only as needed to provide and maintain the Product and related offerings." The phrase "and related offerings" extends usage rights beyond the specific subscribed Product.

**Commercial standard**: The standard position limits Provider's license to Customer Content to what is necessary to provide the contracted service. The license should be tied to "the Product" or "the Cloud Service" without extension to undefined related offerings.

**Gap**: "Related offerings" is undefined and could encompass any of Provider's current or future products and services. The standard formulation would omit "and related offerings" or define the term narrowly.

### Assignment Without Consent in Change of Control (Section 12.6)

**Classification**: Negotiate

**Contract provision**: Either party may assign the agreement in merger, acquisition, or change of control without the other party's consent. All data rights — including ML training authorizations and Customer Content licenses — transfer to the acquirer.

**Commercial standard**: While mutual assignment in change of control is not uncommon, many enterprise SaaS agreements include: advance notification of the assignment, a termination right for Customer if the acquirer is a competitor, or consent requirements for assignment to certain categories of entities.

**Gap**: No notification requirement and no termination right for Customer if Provider is acquired by a competitor or by an entity with materially different data practices. This is particularly significant given the breadth of ML training rights and Customer Content licenses that transfer with the agreement.

### Indemnification Scope — Cover Page Dependency (Section 9)

**Classification**: Negotiate

**Contract provision**: Both "Provider Covered Claims" and "Customer Covered Claims" are Cover Page variables. The procedural framework exists in the Standard Terms but the substantive scope of indemnification is entirely undefined without the Cover Page.

**Commercial standard**: IP infringement indemnification from Provider is a baseline expectation in SaaS agreements, typically specified in the base terms. Provider should indemnify Customer against claims that the service infringes third-party intellectual property rights.

**Gap**: Without the Cover Page, whether Provider indemnifies Customer for IP infringement claims is unknown. The complete deferral of indemnification scope creates the possibility that IP indemnification is absent or narrowly scoped.

### Absence of Data Portability / Export (Section 5.5)

**Classification**: Negotiate

**Contract provision**: Beyond the 60-day deletion right (upon request), no provision for data export in standard or usable formats, no API for data retrieval, and no transition assistance upon termination.

**Commercial standard**: SaaS agreements increasingly include data export rights — either a defined export period prior to deletion, API access for data retrieval, or export in standard formats (CSV, JSON, etc.). Transition assistance, even at additional cost, is a common provision.

**Gap**: No export mechanism exists. Customer's data is held in Provider's systems with no contractual right to extract it in any usable format. Upon termination, Customer loses access to the service and its data simultaneously, with no export window. This creates vendor lock-in and operational risk.

### Auto-Renewal and Non-Renewal Notice Date (Section 5.1)

**Classification**: Negotiate

**Contract provision**: Order Forms auto-renew for additional Subscription Periods unless notice is given before the Non-Renewal Notice Date, which is a Cover Page variable with no default or maximum in the Standard Terms.

**Commercial standard**: Auto-renewal is standard. Notice periods are typically 30-90 days before the end of the then-current term. The Standard Terms should establish a default or maximum notice period.

**Gap**: Without a default or cap, the Cover Page could specify an aggressively long Non-Renewal Notice Date, effectively locking Customer into renewal before it has the information needed to make a renewal decision. The Standard Terms provide no protection against unreasonable notice periods.

### Absence of Disaster Recovery / Business Continuity Commitments

**Classification**: Negotiate

**Contract provision**: No commitments regarding data backup frequency, backup testing, disaster recovery capabilities, recovery time objectives (RTO), or recovery point objectives (RPO).

**Commercial standard**: Enterprise SaaS agreements typically address at minimum: regular data backup with defined frequency, documented disaster recovery procedures, RTO and RPO commitments, and periodic testing.

**Gap**: Complete absence. Customer has no contractual assurance that Provider maintains any disaster recovery capability.

### Absence of Change Management / Notification of Changes

**Classification**: Negotiate

**Contract provision**: No obligation for Provider to notify Customer of changes to the service, feature deprecation, API changes, integration changes, or data format changes.

**Commercial standard**: SaaS agreements commonly include advance notice for material service changes, particularly API deprecation (commonly 90-180 days notice), integration changes, and changes that may affect Customer's use.

**Gap**: Complete absence of change notification obligations. The warranty in Section 6.3 provides some implicit protection against material degradation, but only retroactively and only for changes that cross the "material" threshold.

### Absence of Insurance Requirements

**Classification**: Negotiate

**Contract provision**: No requirement for Provider to maintain professional liability, cyber liability, errors and omissions, or any other insurance coverage.

**Commercial standard**: Enterprise SaaS agreements often require minimum insurance coverage — commonly professional liability / E&O, cyber / technology liability, and commercial general liability — with specified minimum amounts and certificate of insurance upon request.

**Gap**: Complete absence. Customer has no assurance that Provider can satisfy claims, particularly in the event of a data breach or prolonged service failure.

### Customer IP Ownership — "Subject to" Qualification (Section 11.1)

**Classification**: Negotiate

**Contract provision**: "Customer retains all rights in Customer Content, subject to Sections 1.5 and 1.6." The "subject to" language subordinates Customer's ownership to Provider's content licenses and ML training rights.

**Commercial standard**: Customer should retain unqualified ownership of Customer Content. Licenses to Provider should be framed as separate, limited grants — not as qualifications on ownership. The standard formulation is "Customer retains all rights, title, and interest in Customer Content. Customer hereby grants Provider a limited license to..." — separating ownership from license.

**Gap**: The "subject to" formulation technically qualifies Customer's ownership rights rather than granting a separate license. While the practical effect may be similar, the drafting subordinates ownership to usage rights rather than the reverse. This is relevant if disputes arise about the scope of Provider's rights.

---

## Provisions Aligned with Commercial Standards

- **Mutual confidentiality obligations (Section 10)**: Standard bilateral framework with accepted exclusions, compelled disclosure provisions, and permitted sharing with personnel under equivalent obligations. Confidentiality breach is carved out from the consequential damages waiver, providing enhanced protection. Consistent with commercial standards.
- **Termination for material breach (Section 5.3)**: 30-day notice and cure period is within the standard range. Immediate termination for insolvency, dissolution, or cessation of business is standard. 60-day grace period for insolvency proceedings is reasonable.
- **Mutual representations and warranties (Section 6.1, 6.2)**: Standard representations of authority, good standing, and legal compliance for both parties. Customer's warranty regarding rights in Customer Content is standard.
- **Payment dispute mechanism (Section 4.3)**: Standard framework requiring notice, payment of undisputed amounts, and good faith resolution within 15 days. The tie-in to the suspension trigger (undisputed balance) provides reasonable protection against suspension during legitimate disputes.
- **No unilateral modification (Section 12.2)**: Requirement of written agreement signed by each party is a strong and standard protection.
- **Injunctive relief for IP and confidentiality breach (Section 12.4)**: Standard provision permitting injunctive relief without bond.
- **Feedback license (Section 1.4)**: Broad feedback licenses are standard for SaaS agreements. Provider's unrestricted right to use Feedback for product improvement is commercially reasonable and widely accepted.
- **Indemnification procedures (Section 9.3)**: Standard procedural requirements — prompt notice, reasonable assistance, sole control of defense and settlement, consent required for admissions of fault. Aligned with market practice.
- **Force majeure termination right (Section 5.4)**: Termination right after 30 consecutive days of material inoperability with prorated refund is a reasonable provision.

---

## Provisions Outside Standard Evaluation Categories

### Heavy Deferral of Material Terms to Cover Page Variables

The Standard Terms defer an unusually large number of consequential provisions to the Cover Page: General Cap Amount, Increased Cap Amount, Increased Claims, Unlimited Claims, Provider Covered Claims, Customer Covered Claims, Non-Renewal Notice Date, Prohibited Data, Confidential Information definition, Additional Warranties, Use Limitations, and Governing Law. While Cover Pages and Order Forms commonly set commercial terms, the scope of deferral here extends beyond commercial terms into core risk allocation. The Standard Terms establish structural plumbing but the actual protections — liability limits, indemnification scope, renewal lock-in, and data handling boundaries — are opaque without the Cover Page. Several classifications in this analysis (particularly Limitation of Liability, Indemnification, and Auto-Renewal) carry caveats because the Cover Page values could either resolve or deepen the identified gaps. Any review should be conditioned on concurrent review of the Cover Page before execution.

### Interaction Between ML Training Rights and Change of Control

Sections 1.6 and 12.6 interact to create a compound risk that no single evaluation category captures. Provider may use Customer Content for ML training across its product line including third-party components (1.6). Provider may be acquired without Customer consent (12.6). The ML training rights survive termination (5.6). The combined effect is that Customer's data could be used by an unknown future acquirer for AI/ML training purposes across products unknown to Customer at the time of signing, with no mechanism to object, withdraw consent, or exit without liability. This interaction warrants attention as a systemic risk that transcends individual clause assessment.

### Cumulative Security Assurance Gap

Three provisions — the security testing prohibition (Section 2.1(a)(v)), the absence of security commitments, and the absence of breach notification — interact to create a compound gap greater than the sum of its parts. Customer cannot test security, cannot require security, and will not be told if security fails. No single deviation category adequately captures this. It represents a structural absence of security assurance rather than a deviation from a specific standard provision.

### Payment Obligation Asymmetry Across Multiple Provisions

Across force majeure (Section 12.12), suspension (Section 2.2), and the absence of SLA credits, Customer's payment obligation is effectively unconditional. Customer pays during force majeure when no service is delivered, pays during suspension when access is removed, and earns no credits for downtime or service degradation. This persistent one-sided payment obligation is a structural feature of the agreement rather than an individual clause deviation.

### Competing Service Restriction Surviving Termination

Section 2.1(a)(vii) prohibits using the Product "to develop a competing service or product," and Section 5.6 causes this restriction to survive termination. While the practical scope may be limited post-termination (Customer no longer has Product access), the technical survival of this restriction could create ambiguity about residual obligations and exposure. This does not map cleanly to standard evaluation categories.
