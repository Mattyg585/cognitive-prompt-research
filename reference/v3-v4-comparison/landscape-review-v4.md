# Landscape Review (V4 — Synthesis Only)

12 entries | Generated 2026-02-26 | `created_by: landscape-reviewer-v4`

---

## 1. Cross-Story: Three Naming Families Tell the History of This Estate

At least three different teams or eras built this policy estate, and none of them retired what came before.

Three naming conventions run through the entire tenant: CA0xx (numbered, role-based targeting, appears to be the most recent and technically strongest), ACME Cloud (user-group-based, app-team-driven, the largest family by count), and CORP_ (group-based, infrastructure-focused, often the earliest layer). A fourth pattern — bare descriptive names like "Block Legacy Authentication Protocols" and "Guest Users - Block Access All Apps" — may represent the original baseline or ad-hoc additions.

The families do not replace each other. They stack. Global MFA has three policies (one per family). Legacy auth blocking has three (one per family). Guest blocking has two (CA0xx and bare-name). Admin MFA has five policies across all three families. Salesforce has two (ACME and CA-). Each layer adds its own exclusion groups, its own targeting approach, and its own session configurations — creating an estate where the same security intent is expressed multiple times with slightly different implementations.

The families are visible in: Global MFA Baseline (CA001, ACME Cloud Apps, CA50), Privileged Access Protection (CA006-Pilot/Fallback, ACME Cloud Admin Portals, CORP_Admin_Require_MFA/CORP_Admin_Session_Timeout/CORP_Privileged_Access_Workstations), Legacy Protocol Management (CA002, Block Legacy Authentication Protocols, CA-Block-Legacy-Auth), and External Identity Management (CA007a/CA007b, Guest Users - Block Access All Apps). The ACME Cloud family dominates Application-Specific Access with 13 policies. CORP_ policies appear in Device Trust & Compliance and Privileged Access Protection.

---

## 2. Landscape: Of 55 Policies, Roughly 25 Do Unique Work

Roughly half of the policy estate duplicates intent that is already enforced elsewhere — the unique security value concentrates in about 25 policies.

The arithmetic breaks down into several overlapping patterns of redundancy:

**Baseline duplication** (~10 policies): Three global MFA policies do the same thing (Global MFA Baseline). Three legacy auth blocks do the same thing (Legacy Protocol Management). Two guest blocks do the same thing (External Identity Management). Each set could be one policy. That is 4 policies worth of work spread across 10.

**App-named policies that only add MFA** (~5 policies): Of the 13 policies in Application-Specific Access, 5 target All Apps for a specific user group and require only MFA with no session controls (Snowflake Data Warehouse - Allow MFA, Workday HR System - Require MFA, CORP_Slack_Collaboration_MFA with its 30-day session, and similarly Atlassian Suite and REQ-23456). Since the baseline already enforces MFA for all users on all apps, these add nothing. Another 4 do add session controls (Adobe at 1 day, ServiceNow at 4 hours, Salesforce at 8 hours, Tableau at 12 hours) — those provide differentiated value even though their MFA component is redundant.

**Report-only policies that have never enforced** (~5 policies): CA013, CA003, CA004, CA-Salesforce-Require-MFA, and Require password change for high-risk users are all report-only. Three of them have name-config mismatches (the controls do not match the name). These represent intended next steps that stalled. They contribute no active security value today.

**Broken policies** (2-3 policies): CORP_Admin_Session_Timeout_4Hours and ACME Cloud - Zoom Premium Allow Access both include and exclude the same group — they apply to nobody. CA012 applies restrictions to all users instead of just unmanaged devices because it is missing the device filter that CA011 has.

**Ticket policies doing unexpected work** (2-3 policies): TKT-76543 and REQ-99887 target All Users with device compliance requirements — they function as tenant-wide security policies despite their temporary-sounding names. TKT-88888 requires MFA despite being named "MFA Exemption."

The policies doing genuinely unique work include: the baseline MFA (1 of the 3), the legacy auth block (1 of the 3), the guest default-deny plus allow-list (CA007a + CA007b or their equivalents), risk-based blocking (CA008a + CA008b), geo-blocking (CA005), MFA registration protection (CA009), device compliance (CORP_Require_Compliant_Device_Windows), mobile app protection (CA18), admin MFA (CA006-Fallback or equivalent), admin workstations (CORP_Privileged_Access_Workstations), the location-restricted populations (VPN Block, Finance Users), unmanaged device session controls (CA011), and the app-team policies that add session timeouts. That comes to roughly 20-25 policies carrying the estate's actual security posture.

---

## 3. Cross-Story: Policy Names That Overstate What the Controls Actually Do

Six policies across four stories have names that claim stronger security controls than their configurations actually deliver — and three of these are the intended next maturity step for the estate.

The pattern appears in two forms. First, policies where the name describes an aspiration that was never configured:

- "CA013 - Require Phishing-Resistant MFA - Admin Portals" requires standard MFA, not phishing-resistant (Privileged Access Protection)
- "CA003 - Require Compliant or Hybrid-Joined Devices" requires only MFA, no device controls (Device Trust & Compliance)
- "CA004 - Require App Protection - Mobile BYOD" requires only MFA, no app protection (Device Trust & Compliance)

All three are also report-only, so they enforce nothing regardless. But their names in the policy list create an impression of coverage that does not exist. Someone scanning the policy list would see phishing-resistant MFA for admins, device compliance for all users, and app protection for BYOD — none of which is actually in place.

Second, policies where the name contradicts the actual behavior:

- "TKT-76543 - Temporary Full Access" requires MFA AND compliant device — one of the strictest policies in the estate, not "full access" (Ticket/Temporary Access)
- "TKT-88888 - Temp MFA Exemption" requires MFA — the opposite of an exemption (Ticket/Temporary Access)
- "REQ-99887 - Service Accounts Allow Access" requires compliant or domain-joined device for all users except service accounts — the name describes the exemption, not the enforcement (Ticket/Temporary Access)

The first group matters for maturity planning: these are the estate's intended next steps (phishing-resistant auth, device compliance, app protection), and each needs both a configuration fix and a state change before it delivers what the name promises. The second group matters for operational clarity: anyone troubleshooting access issues or auditing the estate will be misled by these names.

---

## 4. Cross-Story: Three Enabled Policies Silently Apply to Nobody

Three enabled policies evaluate to an empty target population because they include and exclude the same group — they consume management attention without providing security value.

The pattern is identical in each case: a group appears in both includeGroups and excludeGroups, and because Conditional Access excludes override includes, the effective population is zero.

- "CORP_Admin_Session_Timeout_4Hours" includes and excludes CA-Include-Admin-Session-Timeout (Privileged Access Protection). This one has well-designed session controls (4-hour sign-in frequency, no persistent browser) that no administrator currently receives.
- "ACME Cloud - Zoom Premium Allow Access" includes and excludes CA-Include-Zoom-Premium-Users (Application-Specific Access). Unlike most app-named policies, this one actually targets a specific application (Zoom Premium), making it architecturally correct — except that it applies to nobody.
- "CA012 - App Restrictions - Office 365 Unmanaged Devices" is a different variant: it does not have the include/exclude conflict, but it is missing the device filter that its companion policy CA011 has (Device Trust & Compliance). Without the filter, it applies applicationEnforcedRestrictions to ALL users on Office 365, not just unmanaged devices — restricting managed device users unnecessarily.

The first two are safe to fix (add group to include-only and verify membership). CA012 needs the device filter from CA011 added to its configuration. None of these carry security dependencies that make them risky to touch — they are either doing nothing or doing the wrong thing.

---

## 5. Cross-Story: The Stalled Rollout — Five Report-Only Policies Are the Next Maturity Step

Five report-only policies form a coherent set of intended improvements that would move the estate from Initial toward Advanced maturity — but all five appear to have stalled at the same stage.

The five policies and what they would deliver if enforced (with configuration fixes where needed):

- "CA013 - Require Phishing-Resistant MFA - Admin Portals" — phishing-resistant authentication for administrators. Needs config fix: currently requires standard MFA, not phishing-resistant. (Privileged Access Protection)
- "CA003 - Require Compliant or Hybrid-Joined Devices" — universal device compliance. Needs config fix: currently requires only MFA. (Device Trust & Compliance)
- "CA004 - Require App Protection - Mobile BYOD" — app protection for mobile BYOD. Needs config fix: currently requires only MFA. (Device Trust & Compliance)
- "CA-Salesforce-Require-MFA" — per-application authentication strength targeting. Config is correct (uses authenticationStrength, targets specific app). Has orphaned exclusion groups. (Application-Specific Access)
- "Require password change for high-risk users" — automated risk remediation. Config appears correct. (Risk-Based Access)

The pattern suggests a coordinated improvement initiative that got partway through: policies were created, named for the intended controls, but the configurations were either never completed (CA013, CA003, CA004) or never switched from report-only to enforced (CA-Salesforce, password change). The three with config mismatches all share the same characteristic — MFA was configured as a starting point, with the intent to add the real controls later.

These five represent the clearest path to maturity improvement. Three need configuration fixes before enforcement. Two could potentially be enforced now. All five need impact assessment from report-only logs before any state change.

---

## 6. Landscape: Ticket Policies Accidentally Carry Tenant-Wide Device Compliance

Two policies from Ticket/Temporary Access are among the most consequential in the tenant — they enforce device compliance for all users, but their names suggest they are temporary accommodations.

"TKT-76543 - Temporary Full Access" requires MFA AND compliant device for all users on all apps. The AND operator makes this one of the strictest grant controls in the estate — only "CORP_Privileged_Access_Workstations" uses the same pattern. If this policy were disabled as part of ticket cleanup, every user in the tenant would lose the compliant device requirement it provides (unless another policy covers them).

"REQ-99887 - Service Accounts Allow Access" requires compliant OR domain-joined device for all users on all apps (excluding service accounts). This is the other tenant-wide device compliance policy — it catches users on any platform where TKT-76543 catches them on all platforms with the additional MFA requirement.

These two policies interact with "CORP_Require_Compliant_Device_Windows" (which only targets Windows/macOS) and the report-only "CA003" (which targets Windows/macOS but is not enforced and has the wrong controls anyway). The actual device compliance posture of the estate depends on ticket policies that nobody would naturally associate with that function.

Retirement sequencing matters here. Neither TKT-76543 nor REQ-99887 can be safely removed or renamed without first verifying that a properly named, intentional device compliance policy covers the same population. CORP_Require_Compliant_Device_Windows covers Windows/macOS but not other platforms. CA003 is report-only with wrong controls. The gap is real.

> **Assumed:** This is a cross-story inference: no single story investigation identified both ticket policies and the device compliance story together. The retirement dependency between Ticket/Temporary Access and Device Trust & Compliance only becomes visible at landscape altitude.

---

## 7. Cross-Story: Orphaned Directory Objects Across the Estate Signal Missing Lifecycle Governance

Orphaned user GUIDs, deleted group references, and empty exclusion groups appear across every story — the deprovisioning process does not include policy cleanup.

The scope: two deleted user GUIDs (7cd133ac, 3acbac59) appear in the excludeUsers list of approximately 20 policies across all 10 stories. Three orphaned group GUIDs appear in "Guest Users - Block Access All Apps" (External Identity Management). Two orphaned group GUIDs appear in "CA-Salesforce-Require-MFA" (Application-Specific Access). One orphaned group GUID appears in "TKT-88888 - Temp MFA Exemption" (Ticket/Temporary Access). And "REQ-99887 - Service Accounts Allow Access" lists a user GUID in excludeGroups — a type mismatch that may cause evaluation errors.

The orphaned user exclusions are harmless — excluding a non-existent user has no effect. But the orphaned group exclusions in the guest block policy are potentially consequential: those groups may once have contained guest populations that were allowed through the block. When the groups were deleted, those guest exceptions silently disappeared.

The CA-Exclude-Legacy-Auth group (in "Block Legacy Authentication Protocols") exists but has 0 members — an empty exclusion placeholder. CA-Exclude-Temp-Full-Access (in TKT-76543) also has 0 members. These are not broken, but they suggest exclusion groups were created proactively and never populated, or were populated and later emptied.

The pattern is consistent: accounts and groups get deleted from the directory, but their references in Conditional Access policies are never cleaned up. This is a governance finding about the change management process, not a technical vulnerability.

> **Not checked:** Whether the three orphaned groups in "Guest Users - Block Access All Apps" contained guest exceptions that are now silently blocked. Whether the orphaned group in TKT-88888 previously exempted a population from MFA. Whether the user GUID in REQ-99887's excludeGroups causes silent evaluation errors or is ignored by Entra ID.

---

## 8. Landscape: Guest Access May Be Broken by Design — Two Block Policies With Incompatible Exclusion Logic

The guest access model relies on two overlapping block policies whose exclusion lists serve different purposes, and the interaction between them may prevent guest access that the estate intends to allow.

The intended design appears to be: block all guests by default, then allow specific guest populations through for specific apps (SharePoint, Teams) with MFA. Two policies implement the block: "CA007a - Block Guest Users - Default Deny" and "Guest Users - Block Access All Apps." Two policies implement the allow: "CA007b - Allow Guest Access - SharePoint/Teams with MFA" and "ACME Cloud - Guest SharePoint Allow."

The problem is in how exclusions are distributed. "Guest Users - Block Access All Apps" excludes CA-Include-Guest-SharePoint-Allow and CA-Include-Contractors-2024 — so guests in those groups bypass this block. But "CA007a - Block Guest Users - Default Deny" only excludes CA-Exclusion-Standard (1 internal user) and CA-Exclusion-BreakGlass (2 internal accounts). Guest accounts would not be in these internal emergency groups. Since Conditional Access evaluates all matching policies and block always wins, CA007a would still block guests even if they are excluded from the other block policy.

This means the guest allow-list may not actually work. A guest in CA-Include-Guest-SharePoint-Allow bypasses one block but not the other. CA007b grants access with MFA for SharePoint/Teams, but the CA007a block would override the grant.

This is the thread most worth validating with a test guest account. The External Identity Management story has the detail on the specific group memberships and policy configurations.

> **Assumed:** The interaction between two block policies and two grant policies for guest access is a cross-story inference that required seeing both the External Identity Management investigation and the CA evaluation model together. The "block always wins" principle comes from Microsoft documentation, not from testing against this specific tenant.

---

## 9. Landscape: Exclusion Groups Are the Real Attack Surface — Same Groups Recur Everywhere

The exclusion groups that bypass security controls are more consistent than the policies themselves — and their membership is the single biggest unknown in the estate.

A small set of exclusion groups appears across nearly every story: CA-Exclusion-Standard (1 member), CA-Exclusion-Emergency (1 member), CA-Exclusion-BreakGlass (2 members), and the two orphaned individual user GUIDs. These are the emergency bypass groups, and their recurrence across MFA, legacy auth blocking, guest blocking, device compliance, risk-based access, and admin controls means their members bypass virtually every security control in the estate.

Break-glass accounts should bypass everything — that is their purpose. But the investigation was unable to resolve the exclusion group memberships in detail. It is not confirmed whether the members of these groups are actual break-glass accounts with appropriate monitoring (sign-in alerts, usage auditing), or whether the groups have accumulated additional members over time. The 2 members in CA-Exclusion-BreakGlass and the single member in each of the other two groups are small numbers, which is a good sign. But for accounts that bypass every control in the tenant, even one inappropriate member is a significant exposure.

Beyond the emergency groups, several policies have their own exclusion groups: CA-Exclude-Legacy-Auth (0 members), CA-Exclude-Temp-Full-Access (0 members), the individually excluded service accounts in REQ-99887, and the individually excluded temp-mfa-exempt user in TKT-88888. These are smaller in scope but still represent bypass paths that need periodic review.

> **Not checked:** Membership of CA-Exclusion-Standard, CA-Exclusion-Emergency, and CA-Exclusion-BreakGlass beyond what L1 observed (member count only). Whether break-glass accounts have monitoring and alerting configured. Whether any exclusion group has accumulated non-break-glass members over time.

---

## 10. Landscape: Retirement Sequencing — What Can Be Safely Removed and What Cannot

Not every redundant policy can be removed in any order — some are accidentally load-bearing, and the safe retirement sequence depends on what gets built to replace them.

**Safe to remove now** (no security dependencies):
The redundant baseline MFA and legacy auth policies can be consolidated one at a time. Removing "CA50 - Global MFA Requirement" or "ACME Cloud Apps - MFA Required All Users" while keeping "CA001 - Require MFA - All Users" would reduce redundancy without affecting coverage — but exclusion groups need reconciliation first (CA001 uses CA-Exclusion-Standard, the others use CA-Exclusion-Emergency). Similarly, one of the two enforced legacy auth blocks can be removed while the other stays. The five app-named policies that only add MFA with no session controls (Snowflake, Workday, Slack with its 30-day timeout, and the others identified in Application-Specific Access) can be removed without any security loss — the baseline already covers their MFA requirement.

**Safe to fix now** (broken, no downstream dependencies):
"CORP_Admin_Session_Timeout_4Hours" (remove group from excludeGroups), "ACME Cloud - Zoom Premium Allow Access" (remove group from excludeGroups), and "CA012 - App Restrictions - Office 365 Unmanaged Devices" (add device filter matching CA011). These are either doing nothing or doing the wrong thing.

**Needs replacement first** (accidentally load-bearing):
"TKT-76543 - Temporary Full Access" and "REQ-99887 - Service Accounts Allow Access" provide tenant-wide device compliance. Before removing or renaming them, a properly named device compliance policy needs to cover the same population. "CA003 - Require Compliant or Hybrid-Joined Devices" was intended for this role but needs its configuration fixed (add actual device controls) and state changed (report-only to enforced) before the ticket policies can be retired.

**Needs investigation first** (unknown dependencies):
The guest block interaction (CA007a vs Guest Users - Block Access All Apps) needs testing before either policy is modified. The report-only policies (CA013, CA003, CA004, CA-Salesforce, password change) need report-only log review before enforcement. The two orphaned user GUIDs should be identified before cleanup to confirm they were not service accounts with a specific exclusion purpose.

---

## 11. Conversation: Walking the Customer Through This Landscape

How to structure the customer conversation to build trust, deliver quick wins, and then go deep on the strategic work.

**Open with what works well.** This estate has a working security foundation: universal MFA is enforced, legacy auth is blocked, high-risk sign-ins are blocked, geo-blocking is in place, guest access defaults to deny, and admin accounts have layered MFA. The redundancy that makes this estate larger than it needs to be also means coverage gaps are rare — overlapping policies create safety nets. Start here to establish credibility and avoid triggering defensiveness.

**Then name the size of the opportunity.** Of 55 policies, roughly 25 are doing unique work. The rest are duplicates from different eras, report-only policies that never progressed, or broken configurations. The estate can be made smaller, clearer, and easier to manage without reducing security — in fact, consolidation would make the actual posture more visible and auditable. Frame this as simplification, not criticism. The people who built this were solving real problems; the issue is that nobody went back to retire the old solutions.

**Quick wins that build momentum.** Three categories of immediate value: (1) Fix the three policies that silently apply to nobody — CORP_Admin_Session_Timeout_4Hours and the Zoom policy just need a group removed from excludeGroups, and CA012 needs a device filter added. These are low-risk fixes that restore intended security controls. (2) Remove the pure-duplicate app-named MFA policies that add nothing beyond baseline. (3) Clean up orphaned user and group references across the estate — harmless individually, but they signal a governance gap and clutter the configuration.

**Then the strategic conversation.** Two threads worth going deep on: First, the stalled rollout — five report-only policies represent the next maturity step (phishing-resistant MFA, device compliance, app protection, per-app auth strength, risk remediation). Three need configuration fixes before enforcement. All need impact assessment. This is the path from Initial to Advanced maturity. Second, the ticket policies that accidentally carry device compliance — TKT-76543 and REQ-99887 need to be replaced with intentional device compliance policies before they can be retired. This connects directly to getting CA003 fixed and enforced.

**Save the guest access question for a focused session.** The interaction between CA007a and Guest Users - Block Access All Apps is the most technically complex thread and the one most likely to reveal broken access. It needs testing with a guest account before making changes. Raise it, scope it, and book follow-up time rather than trying to resolve it in the initial conversation.

**Close with the narrative.** This estate grew organically over at least three implementation phases. Each phase solved real problems but did not retire what came before. The result is an estate that is twice the size it needs to be, with some policies accidentally carrying weight that their names do not reveal. The remediation path is clear: consolidate the duplicates, fix the broken policies, complete the stalled rollout, and then re-baseline. None of this requires new products or licenses — it is configuration work against existing capabilities.

---

## 12. Handover: Landscape Summary

This is a 55-policy Conditional Access estate that grew organically over at least three implementation phases, each adding its own layer without retiring what came before. The result is an environment with a solid security foundation — universal MFA, legacy auth blocking, risk-based access, geo-fencing, and a guest default-deny model — buried under enough redundancy and configuration drift that the actual posture is harder to read than it should be.

The dominant theme is layered redundancy. Three naming families (CA0xx, ACME Cloud, CORP_) run through the entire estate, and each family brought its own version of the same controls: three global MFA policies, three legacy auth blocks, two guest blocks, five admin MFA policies, two Salesforce policies. Each layer uses different exclusion groups, different targeting approaches, and slightly different configurations. The security intent is sound in every case — the problem is not what was built, but that nobody went back to consolidate. Roughly 25 of the 55 policies carry the estate's actual security value; the rest are duplicates, stalled rollouts, or broken configurations.

The second theme is a stalled rollout toward Advanced maturity. Five report-only policies represent a coherent set of improvements — phishing-resistant MFA for admins, device compliance for all users, app protection for BYOD, per-application authentication strength, and automated risk remediation. Three of these have name-config mismatches where the grant controls were never updated to match the policy name. These five are the clearest path forward, and they connect directly to the framework assessment's finding of an estate at Initial maturity with Advanced-tier ambitions.

The third theme is accidental dependencies. Two ticket-prefixed policies (TKT-76543 and REQ-99887) provide tenant-wide device compliance — a function their names completely obscure. Removing them during ticket cleanup would silently drop device requirements for every user. The guest access model has a similar hidden dependency: two overlapping block policies with incompatible exclusion lists may prevent guest access that the allow-list policies intend to permit. These are the threads that need the most care.

The framework assessment places the estate at Initial maturity on the CISA Zero Trust Maturity Model across most pillars, with Identity as the strongest (reaching toward Advanced) and Data as the weakest (minimal CA visibility — Purview and DLP would need separate assessment). The Networks and Applications pillars have limited CA visibility by nature. The key observation is that the gap from Initial to Advanced is not about missing capability — the report-only policies already contain the intended controls. It is about completing configurations, validating impact, and switching from report-only to enforced.

Start with the conversation framework entry for the recommended walkthrough order. The quick wins are the broken policies that apply to nobody (easy fixes, immediate value), the pure-duplicate app-named MFA policies (safe to remove), and the orphaned directory references (governance hygiene). The strategic work is completing the stalled rollout and replacing the accidentally load-bearing ticket policies with intentional device compliance. The guest access interaction needs its own focused session with test validation.

This estate was built by people who were solving real problems in real time. The redundancy is not negligence — it is the natural result of iterative improvement without dedicated policy lifecycle management. The remediation path is configuration work against existing capabilities. No new products, no new licenses, no architectural changes. Just completion of work that was started and consolidation of work that accumulated.
