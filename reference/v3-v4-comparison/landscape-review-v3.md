# Landscape Review (V3)

8 entries | Generated 2026-02-20 | `created_by: landscape-reviewer`

---

## 1. Cross-Story: Three Naming Families Reveal How This Estate Grew

At least three distinct authorship eras left their fingerprints across this estate — and the naming conventions tell the story of each one.

The CA0xx family (CA001, CA002, CA003, etc.) follows a numbered scheme suggesting a planned rollout, possibly from a consulting engagement or Microsoft reference architecture. The ACME Cloud family (ACME Cloud Apps, ACME Cloud - Salesforce, etc.) appears to be an organization-branded layer added later, often covering the same scenarios with minor variations. The CORP_ family (CORP_Admin_Require_MFA, CORP_Require_Compliant_Device_Windows) uses a corporate prefix suggesting an internal IT team convention. A handful of bare-name policies (Block Legacy Authentication Protocols, Guest Users - Block Access All Apps) predate all three.

These families create systematic duplication across the estate: three enabled global MFA policies (Global MFA Baseline), three legacy auth blocks (Legacy Protocol Management), two guest default-deny policies with diverging exclusion lists (External Identity Management), five admin MFA layers (Privileged Access Protection), and two Salesforce policies with fundamentally different architectures (Application-Specific Access).

Each family brought its own exclusion group conventions — CA-Exclusion-Standard vs CA-Exclusion-Emergency, role-based admin targeting vs group-based. The current redundancy provides accidental safety: removing any single policy still leaves coverage from another family. But the exclusion group divergence means consolidation requires careful reconciliation of who is excluded from what, not just deleting duplicates.

> **Assumed:** The three naming families represent different implementation eras or authorship teams, not a deliberate parallel structure. The ACME Cloud family may represent a rebrand or organizational change. Bare-name policies likely predate all three conventions.

> **Not checked:** Did not verify policy creation dates or audit logs to confirm the chronological sequence of naming families. Did not check whether the naming conventions correlate with specific administrator accounts.

---

## 2. Landscape: Roughly Half the Estate Duplicates the Baseline

Of 55 unique policies, roughly 25–30 are doing genuinely distinct security work — the rest duplicate baseline controls or duplicate each other.

The redundancy falls into three patterns:

Baseline duplication (~12 policies): The estate has 3 global MFA policies, 3 legacy auth blocks, 2 guest blocks, and ~4 app-team MFA policies that add no controls beyond what the baseline already enforces (Snowflake Data Warehouse - Allow MFA, Workday HR System - Require MFA, REQ-23456 - Finance Apps Allow Access, and Atlassian Suite - Require Managed Device all require MFA for specific user groups, but baseline MFA already covers All Users on All Apps). These policies are operationally invisible — removing them changes nothing about what users experience. The risk is in the exclusion groups: each duplicate carries slightly different exclusion lists, and those differences may or may not be intentional.

Era duplication (~5 policies): Newer policies were created to replace older ones but the originals were never removed. CA-Salesforce-Require-MFA was built to replace ACME Cloud - Salesforce Require MFA with better architecture (app-specific targeting, authentication strength) but stalled in report-only. CA-Block-Legacy-Auth was built to replace the older legacy auth blocks with a cleaner design (no exclusions) but also stalled in report-only. These represent migrations that stopped mid-flight.

Aspirational policies (~5 policies): Report-only policies with name-config mismatches that were never completed: CA003 (device compliance), CA004 (app protection), CA013 (phishing-resistant MFA), Require password change for high-risk users, Block High Risk Sign-Ins - REPORT ONLY. These were the next maturity step — they represent the gap between where the tenant is and where someone intended it to be.

The policies doing genuinely distinct work include: the enforced baseline MFA (1 needed of 3), legacy auth block (1 needed of 3), guest default-deny with selective allow (CA007a + CA007b), risk-based blocking (CA008a + CA008b), device compliance (CORP_Require_Compliant_Device_Windows, CA18, CA011, CA012), geo-blocking (CA005), MFA registration protection (CA009), admin session controls (CORP_Privileged_Access_Workstations), location-based restrictions (Location Restricted Finance Users, ACME Cloud - VPN Block Untrusted Locations), app-specific session controls (ServiceNow 4hr, Salesforce 8hr, Tableau 12hr), user-segment policies (CA03 - Remote Workers, CORP_Mobile_Only_Users_Access), and the ticket policies that have accidentally become tenant-wide controls.

---

## 3. Cross-Story: Policy Names That Overstate Actual Security Controls

At least six policies across the estate have names that promise security controls their configurations don't deliver — creating a gap between the stated posture and the actual one.

Three are aspirational (report-only, never completed):
- "CA013 - Require Phishing-Resistant MFA - Admin Portals" — requires standard MFA, not phishing-resistant (Privileged Access Protection)
- "CA003 - Require Compliant or Hybrid-Joined Devices" — requires MFA, not device compliance (Device Trust & Compliance)
- "CA004 - Require App Protection - Mobile BYOD" — requires MFA, not app protection (Device Trust & Compliance, User Type Segmentation)

Three are enabled and actively misleading:
- "ACME Cloud - BYOD Users Allow Any Device" — has no device controls at all; it's a baseline MFA duplicate for a BYOD user group (User Type Segmentation)
- "TKT-76543 - Temporary Full Access" — one of the strictest policies in the tenant (MFA AND compliant device for All Users); "Full Access" suggests permissiveness, not restriction (Ticket/Temporary Access)
- "TKT-88888 - Temp MFA Exemption" — requires MFA; the only user actually exempted is one individual in the excludeUsers list (Ticket/Temporary Access)

The risk is not technical — these policies enforce what they enforce regardless of their names. The risk is operational: anyone reading the policy list builds a mental model based on names. That mental model will overstate phishing-resistant MFA coverage, device compliance breadth, and app protection for mobile — and will understate the actual security controls on ticket policies.

---

## 4. Cross-Story: Two Enabled Policies Silently Apply to Nobody

Two policies include and exclude the same group, making them evaluate to an empty target population despite being in the enabled state.

CORP_Admin_Session_Timeout_4Hours (Privileged Access Protection): Includes and excludes CA-Include-Admin-Session-Timeout. Designed to enforce 4-hour session timeouts and no persistent browser for administrators. These session controls are not provided by any other policy — the only other admin session timeouts are the sign-in frequency on CA006-Fallback and CA006-Pilot, which lack the persistentBrowser: never control. Fixing this policy would restore a genuinely missing admin session control.

ACME Cloud - Zoom Premium Allow Access (Application-Specific Access): Includes and excludes CA-Include-Zoom-Premium-Users. This is one of only two policies in the estate that target a specific application ID (the other being CA-Salesforce-Require-MFA, which is report-only). Since it applies to nobody, Zoom Premium users currently fall through to whatever baseline policies match them.

Both are likely copy-paste errors where the target group was accidentally added to the exclusion list. Both have been in this state undetected — neither generates sign-in log entries because neither evaluates for any user. These are quick fixes: remove the group from excludeGroups on each policy.

---

## 5. Landscape: Ticket Policies Are Accidentally Load-Bearing for Device Compliance

Two ticket-prefixed policies targeting All Users have become accidental pillars of the tenant's device compliance posture — removing them during a "temporary policy cleanup" would silently drop device requirements for most users.

TKT-76543 - Temporary Full Access requires MFA AND compliantDevice for All Users on All Apps. This is one of only two AND-operator grant policies in the estate. Its CA-Exclude-Temp-Full-Access group has 0 members, meaning nobody is exempted. It functions as a tenant-wide device compliance requirement despite its name suggesting temporary scope.

REQ-99887 - Service Accounts Allow Access requires compliantDevice OR domainJoinedDevice for All Users on All Apps. Despite naming that describes service account exemptions, it enforces device compliance for the entire tenant (excluding service accounts via three overlapping mechanisms).

The other device compliance policies have narrower scope: CORP_Require_Compliant_Device_Windows covers only Windows/macOS platforms, Atlassian Suite covers one user group, CORP_SAP_Managed_Device_Required covers SAP users only. CA003 — the policy that was intended to be the broad device compliance requirement — is report-only with wrong grant controls.

The safe retirement order: fix CA003's configuration and enable it (or create a clean replacement device compliance policy) before touching either ticket policy. If someone retires the ticket policies first — a natural target during cleanup — the broad device compliance requirement disappears with them.

> **Assumed:** TKT-76543 and REQ-99887 were not intentionally designed as the primary device compliance policies. They acquired this role accidentally because CA003 was never completed and no other policy enforces device compliance at All Users scope.

> **Not checked:** Did not verify whether TKT-76543's AND operator (requiring both MFA and compliant device) causes issues for users without managed devices — unlike REQ-99887's OR operator (compliant or domain-joined), the AND operator is strict and offers no fallback. Did not check whether Intune enrollment rates support tenant-wide compliant device enforcement.

---

## 6. Landscape: Orphaned Directory References Signal a Deprovisioning Gap

Deleted users and groups persist as exclusion references across the estate, indicating that directory object lifecycle changes are not propagated to Conditional Access policy configurations.

Two deleted user accounts (GUIDs 7cd133ac, 3acbac59) appear in the excludeUsers list of nearly every policy in the tenant — spanning all 10 stories. Three orphaned group GUIDs appear in Guest Users - Block Access All Apps (External Identity Management). Two orphaned group GUIDs appear in CA-Salesforce-Require-MFA (Application-Specific Access). One orphaned group appears in TKT-88888 (Ticket/Temporary Access). REQ-99887 lists a user GUID in its excludeGroups field — an invalid reference type that Entra ID may silently ignore or may cause evaluation issues.

The orphaned user exclusions are harmless (excluding a deleted user has no effect). The orphaned group exclusions in Guest Users - Block Access All Apps are potentially significant — those groups may have contained guest populations that were allowed through the block. When the groups were deleted, those guests lost their exemption and are now blocked without anyone necessarily knowing. This is the reverse of accidental load-bearing: removing a directory object silently changed a policy's effective scope.

The pattern points to a gap in the deprovisioning process — when users or groups are deleted from the directory, nobody reviews or updates the Conditional Access policies that reference them.

---

## 7. Conversation: How to Walk the Customer Through This Landscape

This estate tells a clear story of organic growth — start there, then move to quick wins, then strategic decisions.

Open with the naming families (builds trust, no judgment). Show the customer their own history: "We can see at least three phases of policy creation across your environment. Here's what each phase brought." This positions the conversation as collaborative forensics, not an audit. The customer likely knows they have legacy policies — acknowledging the history without criticizing it builds rapport.

Quick wins second (low-risk, high-visibility). Two policies apply to nobody and can be fixed immediately: CORP_Admin_Session_Timeout_4Hours and ACME Cloud - Zoom Premium Allow Access (remove the target group from exclusions). Three legacy auth policies can consolidate to one. The name-config mismatches on report-only policies (CA003, CA004, CA013) are safe to fix because they're not enforced — fix the configuration, then decide on enforcement separately.

Strategic thread: consolidation with caution. The baseline duplication (~12 policies doing the same work) is the obvious cleanup target, but the different exclusion families need reconciliation first. Walk through the exclusion groups: who's in CA-Exclusion-Standard vs CA-Exclusion-Emergency? Are they the same people? This conversation reveals the customer's break-glass and exception governance process — valuable context for recommendations.

High-value investigation: guest access and ticket policies. The guest default-deny model with the potential block-vs-grant conflict (External Identity Management) needs validation with a test guest account before making changes. The ticket policies that have become tenant-wide device compliance controls (Ticket/Temporary Access) need careful handling — explain the accidental load-bearing pattern before suggesting any changes.

Park for later: report-only rollout decisions. The report-only policies represent the customer's own roadmap — phishing-resistant MFA, device compliance, app protection. These are their decisions about security investment, not findings to fix. Frame as: "These policies show where someone intended to go next. Are these still priorities?"

---

## 8. Handover: Landscape Summary

This is a 55-policy Entra ID Conditional Access estate built organically over at least three authorship eras, each leaving its own naming convention and exclusion group patterns.

The result is an environment where roughly half the policies duplicate baseline controls — three global MFA policies, three legacy auth blocks, two guest-deny policies, five admin MFA layers — all enforced, all slightly different in their exclusion lists. The redundancy provides accidental safety (no single point of failure for any control) but makes the estate hard to reason about and harder to maintain.

The most significant cross-estate theme is the gap between stated and actual posture. Six policies have names that promise security controls their configurations don't deliver — phishing-resistant MFA that's actually standard MFA, device compliance that's actually MFA, app protection that's actually MFA. Two enabled policies apply to nobody due to include/exclude conflicts on the same group. Together, these mean the policy list as documentation overstates what's actually enforced. Anyone making security decisions based on policy names alone would miscalculate their coverage.

The CISA Zero Trust Maturity Model assessment places this tenant at Initial maturity overall, with Identity as the strongest pillar reaching toward Advanced. Five report-only policies represent the intended path from Initial to Advanced — phishing-resistant MFA for admins, broad device compliance, mobile app protection, risk-based password remediation — but none have been enforced. These are stalled rollouts, not abandoned experiments.

The finding that warrants the most care is buried in the Ticket/Temporary Access story: two ticket-prefixed policies (TKT-76543 and REQ-99887) have accidentally become the primary device compliance enforcement for the entire tenant. If a cleanup effort retires "temporary" policies first — a natural instinct — it would silently remove device compliance requirements for all users. The safe order is to fix and enable CA003 (the intended device compliance policy, currently report-only with wrong grant controls) before touching either ticket policy.

The guest default-deny model in External Identity Management also warrants validation before changes — CA007a may block guests that CA007b intends to allow, because Conditional Access block always wins when both match. A test guest account would confirm whether the designed intent and actual behavior align.

Start the customer conversation with the naming families — it's the non-threatening entry point that explains everything else. Then quick wins: fix the two broken policies, consolidate legacy auth to one policy, correct the report-only config mismatches. Then the strategic conversations: exclusion group reconciliation across naming families, guest access validation, and whether the stalled report-only policies are still on the roadmap. The ticket policies and their accidental load-bearing role should come last — by then the customer understands the organic growth pattern that explains how this happened.
