## Contract Review Summary

**Document**: Common Paper Cloud Service Agreement — Standard Terms Version 2.1
**Parties**: Provider (unnamed SaaS vendor) and Customer (our organization)
**Your Side**: Customer (buyer)
**Deadline**: 2 weeks
**Review Basis**: Generic review using widely-accepted commercial standards (no organizational playbook available)

> **Note**: No organizational playbook was found. This review uses widely-accepted commercial standards for SaaS procurement as the baseline. All analysis should be reviewed by qualified legal counsel before being relied upon for legal decisions.

---

## Working Theory of the Contract

This is a framework-plus-order-form SaaS agreement built on the Common Paper standard. Its commercial structure is straightforward: Provider hosts a cloud service, Customer pays subscription fees for access, and the parties layer deal-specific terms through individual Order Forms governed by overarching Framework Terms.

Risk flows predominantly toward the Customer once you look beyond the symmetrical surface. The contract is facially balanced — mutual reps, mutual indemnification structure, mutual liability caps — but the substance tilts Provider-ward in several important ways. Provider retains broad rights over Customer Content (Sections 1.5, 1.6), can use Customer data to train AI/ML models including third-party ones, collects and uses Usage Data with minimal constraints, and can suspend access unilaterally. Meanwhile, the data protection provisions are a placeholder — Section 3 punts the real obligations to a DPA that doesn't yet exist and only addresses GDPR, ignoring other privacy regimes. The liability framework (Section 8) defers the most important numbers — cap amounts and claim classification — to Cover Page variables that aren't part of these Standard Terms.

The most structurally significant feature is the interplay between Sections 1.4, 1.5, 1.6, and 11. Together, these create a one-way flow: Customer Content goes in, Provider retains broad processing and ML training rights, and Customer's ownership is "subject to" those grants. For a $150K/year internal operations platform, this architecture means the Customer is potentially feeding proprietary operational data into the Provider's AI training pipeline, with only "commercially reasonable" de-identification standing between its data and Provider's broader product ecosystem.

The contract is also notably silent on several things a customer should expect in a mid-market SaaS deal: no SLA, no uptime commitment in the Standard Terms, no data portability format, no transition assistance, and no audit rights.

---

## Key Findings

**1. AI/ML Training Rights on Customer Data (Section 1.6) — RED.** This is the contract's most consequential provision. Provider claims the right to use both Usage Data and Customer Content to "develop, train, or enhance artificial intelligence or machine learning models," including "third-party components of the Product." The safeguards — aggregation and "commercially reasonable efforts consistent with industry standard technology" for de-identification — are procedurally vague and legally unenforceable in any meaningful way. "Commercially reasonable efforts" is not a standard; it is an escape hatch. For a platform processing internal operations data, this clause creates material risk that proprietary workflows, business logic, and potentially sensitive employee or customer data are ingested into models that serve competitors. The savings clause for Personal Data under "Applicable Data Protection Laws" is necessary but insufficient — it only addresses regulated personal data, not proprietary business data. This provision must be struck or fundamentally restructured before execution.

**2. Data Protection Is a Shell (Section 3) — RED.** The data protection section contains two provisions: one requiring a DPA before submitting GDPR-governed Personal Data, and one prohibiting submission of Prohibited Data. There is no embedded DPA, no breach notification timeline, no security standards, no audit rights, no sub-processor restrictions, no cross-border transfer mechanisms, and no data retention or deletion schedule. The DPA obligation is triggered only by GDPR-governed data, leaving data subject to CCPA, LGPD, POPIA, and other privacy regimes entirely unaddressed. For a SaaS platform handling internal operations — which will almost certainly process employee PII and potentially customer PII — the absence of an operative data protection framework is a dealbreaker. A DPA conforming to current regulatory expectations must be a condition precedent to execution.

**3. Damages Waiver Excludes Direct Lost Profits (Section 8.2) — RED.** The consequential damages waiver excludes "lost profits or revenues (whether direct or indirect)." The parenthetical "whether direct or indirect" is aggressive and atypical. Market standard excludes indirect or consequential lost profits but preserves claims for direct lost profits — which are the most likely form of actual damages if Provider's platform fails and disrupts Customer's operations. This language could leave Customer without a meaningful remedy for the exact scenario that matters most: Provider's service goes down, Customer's operations are disrupted, and Customer loses revenue as a direct result. This must be narrowed.

**4. Post-Termination Data Handling Is Inadequate (Section 5.5) — YELLOW.** Customer Content deletion occurs only "upon Customer's request" and Provider has 60 days to comply. There is no obligation to return data in a usable format, no transition assistance, no certification of deletion, and no automatic deletion default. For an operations platform, data portability and transition planning should be contractually specified, not left to post-termination negotiation when Customer has no leverage.

**5. Feedback Grant Is Overbroad (Section 1.4) — YELLOW.** The "without any restriction or obligation" language on Feedback use is unnecessarily sweeping. Combined with the undefined scope of "Feedback" (a Cover Page variable), this could capture substantive product suggestions containing Customer's proprietary operational methodologies, granting Provider unrestricted rights to commercialize them.

**6. Liability Caps Are Undefined (Section 8.1) — YELLOW.** The three-tier liability structure (General Cap, Increased Cap, Unlimited Claims) is well-designed but the actual dollar amounts and claim classifications are Cover Page variables. These are among the most important commercial terms in the agreement and must be negotiated explicitly. For a $150K/year deal, the General Cap should be no less than 12 months of fees paid, and the Increased Cap should be at least 2x that amount.

---

## Clause-by-Clause Analysis

### Service & Access (Sections 1.1–1.3) — GREEN

Standard SaaS access grant limited to internal business purposes. The Affiliate structure is clean — separate Order Forms create separate obligations, avoiding unintended joint liability. User account responsibilities are reasonable. Support is scoped to the Order Form, which is typical but means the actual support commitment must be verified in the Order Form itself.

### Feedback and Usage Data (Section 1.4) — YELLOW

**What the contract says**: Feedback is given "AS IS" and Provider may use it "freely without any restriction or obligation." Usage Data may be collected, analyzed, and used to maintain, improve, enhance, and promote Provider's products "without restriction or obligation," though external disclosure must be aggregated and non-identifying.

**Deviation**: The "without any restriction or obligation" formulation is broader than market standard, which typically grants a royalty-free license for product improvement purposes rather than an unrestricted release of all obligations. The Usage Data provisions are closer to standard but the "promote" use case extends beyond product improvement into marketing, which is atypical.

**Redline**:

> **Current**: "Provider may use all Feedback freely without any restriction or obligation."
>
> **Proposed**: "Provider may use Feedback for the purpose of improving, developing, and enhancing Provider's products and services, provided that Provider will not disclose Feedback in a manner that identifies Customer or its confidential business processes without Customer's prior written consent."
>
> **Rationale**: Preserves Provider's legitimate interest in product improvement while protecting Customer's proprietary context.
>
> **Priority**: Should-have
>
> **Fallback**: Accept the existing language but add: "For clarity, Provider's use of Feedback remains subject to Section 10 (Confidentiality)."

### Customer Content (Section 1.5) — GREEN

Provider's right to copy, display, modify, and use Customer Content is appropriately scoped to providing and maintaining the Product. This is standard and necessary for SaaS delivery.

### Machine Learning / AI Training (Section 1.6) — RED

**What the contract says**: Usage Data and Customer Content may be used to develop, train, or enhance AI/ML models in Provider's products, including third-party components. Safeguards: (a) data must be aggregated before use, and (b) Provider will use "commercially reasonable efforts consistent with industry standard technology" to de-identify data. A savings clause preserves obligations under Applicable Data Protection Laws for Personal Data.

**Deviation**: This clause is far outside market standard for a $150K/year operational SaaS platform. Most enterprise SaaS agreements either (a) prohibit use of customer data for ML training entirely, (b) make it opt-in rather than opt-out, or (c) at minimum exclude Customer Content and limit ML use to anonymized Usage Data only. The inclusion of Customer Content — the customer's actual business data — is the core problem. The "commercially reasonable efforts" de-identification standard is unenforceable and unmeasurable. The third-party component language means Customer's data could flow to entities with whom Customer has no contractual relationship.

**Redline**:

> **Current**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services, including third-party components of the Product, and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes."
>
> **Proposed**: "Provider may use Usage Data, in aggregated and de-identified form, to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services. Provider will not use Customer Content for any machine learning, artificial intelligence, or model training purpose. For the avoidance of doubt, neither Usage Data nor Customer Content will be shared with or made available to third parties for machine learning or model training purposes without Customer's prior written consent."
>
> **Rationale**: Customer Content represents proprietary business data entrusted to the platform for operational purposes, not for model training. Restricting ML training to aggregated, de-identified Usage Data preserves Provider's product improvement interests while protecting the Customer's proprietary information.
>
> **Priority**: Must-have
>
> **Fallback**: If Provider insists on ML training rights over Customer Content, require: (i) explicit opt-in consent (not default authorization), (ii) a defined and auditable de-identification standard (not "commercially reasonable efforts"), (iii) exclusion of all third-party model training, and (iv) a right to opt out at any time with prospective effect.

### Restrictions on Customer (Section 2.1) — GREEN

Standard restrictions. The reverse engineering exception for Applicable Laws (likely referencing EU decompilation rights) is a good sign of a considered template. The prohibition on competitive development (2.1(a)(vii)) is typical for SaaS.

### Suspension (Section 2.2) — YELLOW

**What the contract says**: Provider may suspend access for unpaid balances over 30 days, breach of restrictions, or use that "materially and negatively impacts the Product or others," with or without notice. Provider will "try to inform Customer" before suspension "when practical."

**Deviation**: The "try to inform" and "when practical" qualifiers are weaker than market standard, which typically requires reasonable prior written notice except in emergencies. The "materially and negatively impacts... others" trigger is vague and could be invoked for resource consumption that affects other tenants, without any objective threshold.

**Redline**:

> **Current**: "Provider may temporarily suspend Customer's access to the Product with or without notice. However, Provider will try to inform Customer before suspending Customer's account when practical."
>
> **Proposed**: "Provider will provide Customer with at least 5 business days' prior written notice before suspending access, except where immediate suspension is reasonably necessary to prevent imminent harm to the Product, other customers, or third parties, in which case Provider will notify Customer as soon as reasonably practicable after suspension and will work with Customer to resolve the issue and restore access promptly."
>
> **Rationale**: For an operations platform, unannounced suspension could cause significant business disruption. Prior notice allows Customer to cure issues before access is lost.
>
> **Priority**: Should-have
>
> **Fallback**: Accept "with or without notice" but add a requirement that Provider provide written notice within 24 hours of any suspension, stating the reason and the steps needed to restore access.

### Privacy & Security (Section 3) — RED

**What the contract says**: Customer must enter a DPA before submitting GDPR-governed Personal Data. Customer must not submit Prohibited Data unless authorized.

**Deviation**: This is not a data protection framework; it is a placeholder. For a mid-market SaaS platform handling internal operations, the absence of operative data protection terms is a material gap. Market standard for this deal size includes: an executed DPA as a schedule to the agreement, breach notification timelines (72 hours for GDPR, reasonable promptness otherwise), defined security standards or certifications (SOC 2, ISO 27001), audit rights, sub-processor notification and objection rights, data localization or transfer mechanisms, and data retention/deletion schedules.

**Redline**:

> **Proposed**: Add as a condition to execution: "The parties will execute a Data Processing Addendum substantially in the form of Provider's standard DPA prior to the Effective Date. The DPA will address, at minimum: (a) data processing scope and purpose limitations; (b) security measures and certifications; (c) breach notification within 72 hours of discovery; (d) sub-processor notification and objection rights; (e) data subject rights assistance; (f) cross-border transfer mechanisms; (g) audit rights; and (h) data deletion and return obligations on termination. The DPA will cover all Personal Data processed under this Agreement, regardless of governing jurisdiction."
>
> **Rationale**: A DPA should be a condition of execution, not a deferred obligation triggered only by GDPR-scoped data. The Provider almost certainly has a standard DPA — this ask is about ensuring it is in place from day one and covers all applicable privacy regimes.
>
> **Priority**: Must-have
>
> **Fallback**: If Provider resists pre-execution DPA, require execution within 30 days of the Effective Date and prohibit processing of any Personal Data until the DPA is in place.

### Payment & Taxes (Section 4) — GREEN

Standard payment terms. Fees are non-refundable except where specific termination rights apply, which is typical. The payment dispute mechanism (Section 4.6) is reasonable — good-faith notice, pay undisputed amounts, 15-day resolution window. Tax responsibility allocation is standard (Customer pays itemized taxes, not Provider's income tax).

### Term & Termination (Section 5.1–5.4) — GREEN

The framework is standard: Order Form governs subscription period, auto-renewal with notice of non-renewal, termination for material breach with 30-day cure, and termination for insolvency. Force majeure termination with prorated refund after 30 days is reasonable. One note: the Non-Renewal Notice Date is a Cover Page variable and must be reviewed — overly short notice periods can create unwanted auto-renewals.

### Effect of Termination (Section 5.5) — YELLOW

**What the contract says**: On termination, Customer's rights end, Customer Content is deleted within 60 days on request, Confidential Information is returned or destroyed, and Provider submits a final invoice.

**Deviation**: The 60-day deletion window is at the outer edge of market standard (30 days is more typical). More importantly, there is no data return obligation, no specified format, no transition assistance, and no certification of deletion. For an operations platform, losing access to your data without a structured transition is a significant business risk.

**Redline**:

> **Current**: "Upon Customer's request, Provider will delete Customer Content within 60 days."
>
> **Proposed**: "Upon Customer's request made within 30 days of termination or expiration, Provider will (a) make Customer Content available for export in a standard, machine-readable format (such as CSV, JSON, or via API) within 30 days, and (b) following successful export or upon Customer's written confirmation, delete all Customer Content within 30 days and certify such deletion in writing. If Customer does not request export within 30 days of termination, Provider will delete Customer Content within 60 days of termination."
>
> **Rationale**: Data portability is essential for operational continuity. Customer should not be locked into a vendor relationship because extracting its own data is impractical.
>
> **Priority**: Should-have
>
> **Fallback**: Accept the 60-day deletion window but add a data export right in a machine-readable format and a written certification of deletion.

### Survival (Section 5.6) — YELLOW

**What the contract says**: Sections 1.4 (Feedback), 1.6 (Machine Learning), and several others survive termination.

**Deviation**: The survival of Section 1.6 (Machine Learning) post-termination is problematic. If the ML training clause is not revised, its survival means Provider retains the right to continue using Customer Content already ingested into ML models indefinitely after the relationship ends. This is an unusual and aggressive survival provision. Combined with Section 5.6(b), which allows retention of Confidential Information per standard backup policies, the practical effect is that Customer's data may persist in Provider's ML models permanently with no obligation to purge.

This issue is resolved if the Section 1.6 redline is accepted. If not, the survival clause for Section 1.6 must be separately addressed.

### Representations & Warranties (Section 6) — GREEN

Mutual representations are standard. Provider's warranty of non-reduction of general functionality is a reasonable minimum. The warranty remedy process (45-day notice, 45-day cure, then termination with prorated refund) is measured and workable.

### Disclaimer of Warranties (Section 7) — GREEN

Standard mutual disclaimer of implied warranties, subject to the express warranties in Section 6. The "safe, secure, or error-free" disclaimer is typical for cloud services.

### Limitation of Liability (Section 8) — RED (Section 8.2) / YELLOW (Section 8.1)

**Section 8.1 (Caps)**: The three-tier structure — General Cap, Increased Cap, and Unlimited Claims — is well-designed. However, the actual amounts and claim classifications are Cover Page variables that must be negotiated. For a $150K/year deal:
- General Cap: Should be at least 12 months of fees paid (i.e., $150K minimum)
- Increased Cap: Should be at least 24 months of fees paid ($300K)
- Unlimited Claims should include: willful misconduct, breach of Section 3 (data protection), indemnification obligations, and breach of Section 1.6 (ML training rights)

**Section 8.2 (Damages Waiver)**: The exclusion of "lost profits or revenues (whether direct or indirect)" is the significant issue. The parenthetical "whether direct or indirect" extends the exclusion beyond the standard consequential damages waiver to cover direct lost profits, which are a foreseeable and primary category of damages if a SaaS operations platform fails.

**Redline for Section 8.2**:

> **Current**: "Neither party will be liable for lost profits or revenues (whether direct or indirect), or for consequential, special, indirect, exemplary, punitive, or incidental damages, even if informed of the possibility."
>
> **Proposed**: "Neither party will be liable for consequential, special, indirect, exemplary, punitive, or incidental damages, including indirect lost profits or revenues, even if informed of the possibility. For the avoidance of doubt, this exclusion does not apply to direct damages, including direct lost profits or revenues."
>
> **Rationale**: Direct lost profits are the primary measure of damages when an operations platform fails. Excluding them leaves Customer without meaningful recourse for the most foreseeable harm.
>
> **Priority**: Must-have
>
> **Fallback**: Accept the exclusion of lost profits but carve out damages arising from Provider's breach of Section 3 (Privacy & Security), Section 10 (Confidentiality), and willful misconduct.

**Section 8.4 (Exceptions)**: The exception structure is sound — Increased Claims escape the General Cap, Unlimited Claims escape all caps, and confidentiality breach escapes the damages waiver. The specific claims in each category are Cover Page variables that need to be negotiated per the recommendations above.

### Indemnification (Section 9) — YELLOW

**What the contract says**: Mutual indemnification for "Covered Claims" (a Cover Page variable). Standard procedural requirements: prompt notice, reasonable assistance, sole control of defense, no settlement with admission of fault without consent.

**Deviation**: The structure is sound, but the substance depends entirely on Cover Page variables. "Provider Covered Claims" and "Customer Covered Claims" are not defined in the Standard Terms. At minimum, Provider Covered Claims should include: (a) IP infringement claims arising from Customer's authorized use of the Product, and (b) claims arising from Provider's breach of data protection obligations. Customer Covered Claims should include claims arising from Customer Content or Customer's breach of the agreement.

Section 9.5's exclusions are standard and reasonable. The exclusive remedy provision (Section 9.6) is typical.

**Action**: Ensure Cover Page defines appropriate Covered Claims. No redline to Standard Terms needed, but the Cover Page negotiation is critical.

**Priority**: Must-have (in Cover Page negotiation)

### Confidentiality (Section 10) — GREEN

Standard mutual confidentiality provisions. Exclusions for publicly available, independently developed, and lawfully received information are standard. Required disclosure with reasonable advance notice is appropriate. Permitted disclosure to need-to-know personnel bound by equivalent obligations is market standard.

### Reservation of Rights (Section 11) — YELLOW

**What the contract says**: Provider retains all rights in the Product. Customer retains all rights in Customer Content, "subject to Sections 1.5 and 1.6."

**Deviation**: The "subject to" qualification is the issue. Customer's ownership of its own content is made expressly subordinate to Provider's processing rights (Section 1.5) and ML training rights (Section 1.6). While Section 1.5 is reasonable and necessary for service delivery, the subordination to Section 1.6 means Customer's ownership of its content is hollow if Provider can train ML models on it indefinitely. This issue is resolved if the Section 1.6 redline is accepted.

### General Terms (Section 12) — Mostly GREEN

**Assignment (Section 12.6)** — GREEN. Mutual consent requirement with an exception for merger/acquisition/change of control is market standard.

**Logo Rights (Section 12.8)** — YELLOW. Provider may use Customer's name and logo in marketing. This is common but should require prior written consent, or at minimum allow Customer to opt out.

> **Proposed**: Add: "Provider will obtain Customer's prior written consent before using Customer's name or logo in marketing materials. Customer may revoke consent at any time upon written notice."
>
> **Priority**: Nice-to-have

**Force Majeure (Section 12.12)** — GREEN. Standard with the appropriate carveout for Customer's payment obligations.

**Governing Law (Section 12.3)** — YELLOW. The governing law and chosen courts are Cover Page variables. For a $150K mid-market deal, Customer should seek its home jurisdiction or a neutral jurisdiction. This is a Cover Page negotiation point, not a Standard Terms issue.

Confidentiality, Force Majeure, Assignment, Export Controls, Anti-Bribery, Government Rights, and the remaining general terms are standard and acceptable.

---

## Negotiation Strategy

The counterparty here is a SaaS provider using the Common Paper standard, which signals a company that values efficient contracting and is accustomed to negotiating against this template. This is useful — they have seen these asks before, and the framework's Cover Page / Standard Terms split is designed to accommodate customer-specific negotiation without rewriting the base agreement. The Provider is likely a mid-market or growth-stage SaaS company; the Common Paper standard is most popular with companies in that bracket.

Provider's likely priorities: (1) preserving ML/AI training rights, which are increasingly central to SaaS product strategy and valuation narratives; (2) limiting data protection obligations that create operational burden; (3) maintaining broad liability protections. Provider's BATNA is walking away from a $150K deal — material but not transformative for a mid-market SaaS company. This means Provider has some room to negotiate but won't accept terms that create precedent problems for their broader customer base.

Customer's leverage is moderate. $150K/year is a solid mid-market deal. The two-week deadline creates some time pressure, but Common Paper agreements are designed for relatively fast negotiation, so this is manageable if redlines are focused.

**Sequencing**: Lead with the data protection ask. Requiring a DPA prior to execution is the most defensible, least controversial must-have — it is regulatory hygiene, not aggressive lawyering, and Provider almost certainly has a standard DPA ready to attach. Getting early agreement on this establishes a collaborative tone and creates momentum.

Next, address the ML training clause. This will be the hardest negotiation point because it touches Provider's product strategy. Frame it around Customer Content specifically — conceding aggregated, de-identified Usage Data for ML purposes is reasonable and gives Provider something. The ask is: keep your hands off our actual business data. If Provider pushes back, the opt-in / auditable de-identification / no third-party training fallback gives room to land in a workable middle ground.

Third, raise the damages waiver. The "whether direct or indirect" lost profits exclusion is objectively atypical, and pointing to market comparables should be effective. If Provider resists, the carve-out fallback (data breach, confidentiality breach, willful misconduct) still captures the scenarios that matter most.

Hold the data portability, logo rights, and suspension notice asks for the concession phase. These are commercially reasonable asks that Provider should be willing to grant, and they can be offered as trades against concessions on the ML or liability points. If negotiations get tight, logo rights is the first thing to drop.

The Cover Page negotiation is where several of these issues will actually be resolved — liability cap amounts, claim classification (Increased vs. Unlimited), Covered Claims definitions, governing law, and non-renewal notice periods. Prepare a Cover Page markup alongside the Standard Terms redlines and present them as a package.

---

## Next Steps

1. **Immediate**: Request Provider's standard DPA and any Cover Page template or existing term sheet for this deal size.
2. **Within 3 business days**: Prepare and deliver a consolidated redline covering:
   - Standard Terms: Sections 1.4, 1.6, 2.2, 3.1, 5.5, 8.2, and 12.8
   - Cover Page: liability cap amounts, claim classifications (Increased and Unlimited), Covered Claims definitions, governing law, venue, and non-renewal notice period
   - DPA: review Provider's standard DPA against current regulatory expectations (GDPR, CCPA at minimum)
3. **Internal alignment**: Brief the business stakeholder on the ML training issue — this is likely the point where Provider pushes back hardest, and the business team should understand the risk of accepting vs. the risk of deal friction.
4. **Escalation planning**: If Provider refuses to modify Section 1.6 materially, escalate to senior counsel for a risk acceptance decision. The combination of ML training rights on Customer Content, survival post-termination, and vague de-identification standards creates a risk that should not be accepted at the procurement level.
5. **Target completion**: Aim to exchange first redlines within 5 business days, leaving one week for negotiation within the two-week deadline.

> **Disclaimer**: This analysis is based on general commercial standards and does not constitute legal advice. All findings and recommendations should be reviewed by qualified legal counsel before being relied upon for legal decisions.
