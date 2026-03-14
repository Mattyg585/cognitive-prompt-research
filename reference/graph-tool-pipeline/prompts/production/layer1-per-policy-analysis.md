# Layer 1: Per-Policy Analysis (Batch of 5) 

## Context

**Project**: Entra ID Conditional Access policy assessment tool
**Layer**: Layer 1 - Per-policy semantic analysis

This prompt auto-detects which policies haven't been analyzed yet. Execute repeatedly until all policies in the tenant are enriched with Layer 1 observations.

---

## Your Task

Analyze 5 policies with deep semantic understanding. Infer intent from policy names, check if implementation matches that intent, and detect patterns worth investigating. Avoid mechanical execution - trust your judgment about what's significant.

**Your role:**
1. Auto-detect which 5 policies haven't been analyzed yet
2. Analyze each policy deeply - one at a time, understanding intent and implementation
3. Write observations as you complete each policy
4. Verify observations are written to database correctly

**Architecture context:** This is Layer 1 (per-policy analysis). Layer 2 (aggregate analysis) will detect cross-policy patterns separately. Focus on understanding each policy deeply - don't compare across policies.

---

## Investigation Lenses

Use these lenses to detect patterns worth investigating:

- **Anomalies**: Unusual configs, broken references, naming inconsistency
  - Example: Policy references authentication strength that doesn't exist in tenant

- **Gaps**: Missing controls, coverage holes
  - Example: Policy named "Require MFA for Admins" but excludes admin groups

- **Misconfigurations**: Name vs implementation mismatch, orphaned GUIDs
  - Example: Policy named for specific app but targets all applications

- **Conflicts**: Overlapping policies with different controls
  - Example: Two policies target same users with contradictory session controls

- **Attack surfaces**: Exclusions + gaps creating bypass paths
  - Example: Testing group excluded from baseline MFA + compliance policies

These are detection lenses, not checklists - let policy complexity guide what you investigate.

---

## Observation Count - Natural Variation

Let policy complexity guide observation count naturally:

- If you spot 2 distinct issues, write 2 observations. If you spot 7, write 7.
- Don't aim for consistency across policies.
- Trust your judgment about what's significant.

---

## Observation Categories & Confidence

**Common categories** (use these or create your own if none fit):
`misconfiguration`, `attack_surface`, `coverage`, `security_posture`, `positive`, `hygiene`, `naming`

**Confidence**: Trust your judgment. Higher when verified via API, lower when interpreting ambiguous signals. Natural variation is expected.

---

## Quality: Semantic Analysis vs Data Restating

**Good - semantic understanding:**
"Policy named 'Require MFA for Finance Team' but actually targets All Users, causing 350 users to need MFA instead of the intended 12-person Finance team. This is a semantic mismatch because it is infered that the policy should be scoped to the 12-person finance team and not all users.  Further investigations would be to look at what other scoping or controls are in place that may help uncover what's caused this semantic missmatch, is the policy targeting a finance app, perhaps this means it's less of an issue because, whilst not ideal, the 'all users' scope is further refined at the application layer where only 'finance users' are allowed to SSO to the finance app.  This is still an observation and likely will require follow up, as a config change at the enterprise app layer could have larger unitended consequencies up stream (at the CA policy), but this level of detail will help to inform the consultants next steps or steer customer conversations."

**Bad - just data restating:**
"Policy targets All Users and has 2 exclusion groups."

Focus on understanding what the configuration *means*, not just what it *says*.

---

## Investigation Mindset

Be curious about each policy. Every configuration tells a story:

- What were they trying to achieve?
- Why might this exist as-is?
- What context would change our interpretation?
- Did they nearly get there?

Dig deeper when appropriate. Your observations should help steer customer conversations, not just list findings.

---

## Step 1: Find the Next 5 Unanalyzed Policies

First, identify the tenant and get unanalyzed policies:

```sql
-- Get tenant ID (use this for all subsequent queries)
SELECT DISTINCT tenant_id FROM policies LIMIT 1;

-- Find 5 unanalyzed policies
SELECT id, display_name
FROM policies
WHERE tenant_id = '<tenant-id-from-above>'
  AND id NOT IN (
    SELECT DISTINCT policy_id
    FROM observations
    WHERE created_by = 'policy-analyzer-layer1'
      AND policy_id IS NOT NULL
  )
ORDER BY display_name
LIMIT 5;
```

**Database schema reference:**
- `policies` table: `id`, `tenant_id`, `display_name`, `state`, `configuration` (JSONB with full policy), `created_datetime`, `modified_datetime`
- Policy config is in `configuration` column (not `conditions`) - contains `conditions`, `grantControls`, `sessionControls`, `_metadata`

Use the 5 policies returned as your analysis targets. This makes the prompt reusable - same query works every run until all policies are enriched.

---

## Step 2: Analyze Each Policy Sequentially

For each of the 5 policies, analyze deeply then write observations before moving to the next policy.

**Your approach for each policy:**

Understand this policy deeply. Apply the investigation mindset - be curious about what they were trying to achieve, why it exists as-is, and what context matters. Detect patterns worth investigating, calculate impact via Lokka MCP, and write observations for each significant finding.

Let the policy's complexity guide how many observations you write - simple policy might yield 2-3, complex policy 6-8+. Trust your judgment.

**Key investigation angles:**
- **Intent vs implementation**: What story does this policy tell?
- **Exclusions**: Do they undermine the intent? Use Lokka MCP for group member counts
- **Policy state**: Enabled, report-only, disabled? How long in current state?
- **Patterns**: Apply the investigation lenses (anomalies, gaps, misconfigurations, conflicts, attack surfaces)
- **Affected scope**: Calculate user impact, percentage of tenant affected
- **_metadata field**: Check `configuration._metadata` for context:
  - `modAdminExcluded: true` = MOD Admin was intentionally excluded during policy transformation
  - `sourceFile` = Original policy source (helps understand provenance)
  - Use this context to inform your analysis (e.g., don't flag MOD Admin exclusion as unexpected if metadata shows it was intentional)

**Important notes:**
- This is per-policy analysis (Layer 1) - focus on understanding each policy deeply
- Cross-policy patterns will be detected separately (Layer 2) - don't compare across policies
- Set `related_observations` to empty array: `ARRAY[]::integer[]`

### Database Write Format

Use psql via Bash for writing observations:

**Load credentials from .env file:**
```bash
# Source credentials from .env file
source /home/matt/repos/personal/graphTool/.env

PGPASSWORD="$DB_PASSWORD" psql \
  -h "$DB_HOST" \
  -U "$DB_USER" \
  -d "$DB_NAME" \
  -c "INSERT INTO observations (
    tenant_id,
    policy_id,
    observation_type,
    category,
    layer,
    title,
    description,
    evidence,
    related_observations,
    ai_confidence,
    ai_reasoning,
    affected_scope,
    created_by,
    status
  ) VALUES (
    '<tenant-id>',
    '<policy-uuid>',
    'intent_analysis',
    'misconfiguration',
    1,
    'Short title of observation',
    'Detailed description',
    '{
      \"evidence_paths\": [\"conditions.clientAppTypes[0]\", \"conditions.clientAppTypes[2]\"],
      \"fields_referenced\": [\"conditions.clientAppTypes\"],
      \"key_values\": {\"conditions.clientAppTypes\": [\"exchangeActiveSync\", \"browser\", \"other\"]},
      \"summary\": \"Legacy auth enabled via exchangeActiveSync in clientAppTypes\"
    }'::jsonb,
    ARRAY[]::integer[],
    0.85,
    'Reasoning for this observation',
    '{\"excluded_groups\": 2, \"group_member_counts\": {\"Group-A\": 12}, \"estimated_impact\": \"~150 users\"}'::jsonb,
    'policy-analyzer-layer1',
    'pending'
  );"
```

**Alternative**: If writing multiple observations for a policy, consider using a Python script with psycopg2 to batch insert them.

### Verify After Each Policy

After completing each policy, query to verify observations were written:

```sql
SELECT id, title, category, ai_confidence,
       evidence->>'summary' as evidence_summary,
       jsonb_array_length(evidence->'evidence_paths') as path_count,
       created_at
FROM observations
WHERE policy_id = '<the-policy-uuid>'
ORDER BY created_at DESC;
```

**Check evidence_paths are populated** - `path_count` should be > 0 for each observation.

---

## Tools Available

### postgres MCP (Read-Only)
- Read policy data: `SELECT * FROM policies WHERE id = '...'`
- Read existing observations: `SELECT * FROM observations WHERE tenant_id = '...'`
- Query schema: Check table structures

### psql via Bash (For Database Writes)
**Load credentials from .env file:**
```bash
# Source credentials from .env file
source /home/matt/repos/personal/graphTool/.env

PGPASSWORD="$DB_PASSWORD" psql \
  -h "$DB_HOST" \
  -U "$DB_USER" \
  -d "$DB_NAME" \
  -c "INSERT INTO observations (...) VALUES (...);"
```

Database credentials: `/home/matt/repos/personal/graphTool/.env`

### Lokka MCP (Validation & Enrichment)
- Validate GUIDs: Check if user/group/app/location GUIDs exist
- Get group member counts: Retrieve member count for groups
- Enrich context: Get display names for UUIDs
- Retrieve details: Get named location properties, auth strength details

**GUID Resolution Protocol:**
When validating GUIDs in `excludeUsers` or `includeUsers`, check multiple object types:

1. Try `/users/{id}` first
2. If 404, try `/servicePrincipals/{id}` - automation accounts are commonly excluded
3. If still 404, try `/directoryObjects/{id}` as catch-all

**Important:** Service Principal exclusions are typically intentional. CI/CD pipelines, automation accounts, and app registrations cannot complete interactive MFA. Only flag as concerning if:
- The SPN name suggests it shouldn't be excluded (e.g., user-facing app)
- The exclusion creates an unexpected bypass path

**Common Valid Exclusion Patterns:**
- **Service Principals**: CI/CD pipelines, sync services, automation - cannot do interactive MFA
- **Break-glass groups**: Emergency access accounts - should have compensating controls (PIM, monitoring)
- **Sync accounts**: Azure AD Connect, SCIM provisioning services

**Note:** If parallel Lokka API calls fail (sibling errors), retry the failed calls individually.

### MS Docs MCP (Domain Knowledge)
- "What protocols does legacy authentication include?"
- "What does ACSC E8 ML2 require for admin MFA?"
- "What is phishing-resistant MFA?"

### WebSearch (External Research)
- Research unfamiliar protocols or settings
- Look up compliance framework requirements

---

## Evidence Structure (Critical for Traceability)

Every observation must include **evidence_paths** - the specific JSON paths in the policy that support the finding. This enables:
- One-click highlighting in the web app ("show me exactly where")
- Deterministic verification (paths exist or they don't)
- Demo-ability on calls ("here's the evidence")

**Evidence JSONB structure:**
```json
{
  "evidence_paths": [
    "conditions.clientAppTypes[0]",
    "conditions.clientAppTypes[2]",
    "conditions.users.excludeGroups[0]"
  ],
  "fields_referenced": [
    "conditions.clientAppTypes",
    "conditions.users.excludeGroups"
  ],
  "key_values": {
    "conditions.clientAppTypes": ["exchangeActiveSync", "browser", "other"],
    "conditions.users.excludeGroups": ["group-guid-here"]
  },
  "summary": "Legacy auth enabled via exchangeActiveSync and other in clientAppTypes"
}
```

**Field descriptions:**
- `evidence_paths`: Exact JSON paths (with array indices) - for highlighting
- `fields_referenced`: Parent field names - for quick reference
- `key_values`: The actual values at those paths - for inline display
- `summary`: One-line summary of what the evidence shows

**Path format:** Use dot notation with array indices: `conditions.users.excludeGroups[0]`

---

## Affected Scope Tracking

Calculate impact metrics for observations:

**For group exclusions:**
1. Identify excluded group GUIDs from policy configuration
2. Query Lokka MCP to get member count for each group
3. Calculate percentage of tenant users affected
4. Add to `affected_scope` JSONB field

**Example affected_scope structure:**
```json
{
  "excluded_groups": 2,
  "group_member_counts": {
    "CA-Bypass-All-Admins": 12,
    "Testing-Admins": 35
  },
  "total_excluded_users": 47,
  "tenant_user_count": 350,
  "percentage_affected": "13.4%",
  "scope_description": "47 users (13.4% of tenant) bypass this control"
}
```

---

## Success Criteria

- All 5 policies analyzed successfully
- Observations show natural variation in count based on policy complexity
- Observations have valid structure with `affected_scope` field populated
- **Evidence includes `evidence_paths` array** - specific JSON paths that support the finding
- **Evidence includes `key_values`** - actual values at those paths for verification
- Group member counts retrieved via Lokka MCP and included in `affected_scope`
- Semantic understanding maintained (not just data restating)
- GUIDs validated correctly (check service principals if user lookup fails)
- Categories used appropriately (common categories or justified alternatives)
- No database write conflicts or failures
- `related_observations[]` stays empty (cross-policy linking is Layer 2 work)
- Batch summary provided at end

---

## Key Principles

- Trust your autonomy - minimal prescription yields better insights
- Semantic understanding > data retrieval (understand intent, not just config)
- Track affected_scope for prioritization (use Lokka MCP to get group member counts)
- Natural variation in observation count is healthy (trust your judgment)
- Validate GUIDs via Lokka MCP - but remember to check service principals, not just users

---

## Step 3: Batch Summary

After analyzing all 5 policies, provide a brief summary:

```sql
-- Count observations from this batch
SELECT COUNT(*) as total_observations, COUNT(DISTINCT policy_id) as policies_analyzed
FROM observations
WHERE created_by = 'policy-analyzer-layer1'
  AND created_at > NOW() - INTERVAL '1 hour';

-- Count remaining
SELECT COUNT(*) as remaining_policies
FROM policies
WHERE tenant_id = '<tenant-id>'
  AND id NOT IN (
    SELECT DISTINCT policy_id FROM observations
    WHERE created_by = 'policy-analyzer-layer1' AND policy_id IS NOT NULL
  );
```

**Summary format:**
- Policies analyzed: X of Y
- Observations written: N
- Remaining policies: Z
- Key patterns noticed (brief, 2-3 bullets)

This helps track progress across multiple batch runs.
