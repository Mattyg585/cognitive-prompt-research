# Policy Plan

## Purpose

Compare a proposed policy against current Entra state and produce a diff showing what will change. This is the "terraform plan" equivalent for Conditional Access policies.

**Used by**: Policy Lifecycle Orchestrator (before creating PR)
**Output**: Structured diff for PR body

---

## Input

You will receive:
1. **Proposed policy JSON** - The policy to be deployed
2. **Context** - Whether this is a new policy or modification of existing

---

## Your Task

### Step 1: Identify the Policy

Check if this policy already exists in Entra:

```
# Search by displayName
GET /identity/conditionalAccess/policies?$filter=displayName eq '{displayName}'
```

If found, note the policy ID. If not found, this is a CREATE operation.

### Step 2: Get Current State (if exists)

If the policy exists, retrieve its current configuration:

```
GET /identity/conditionalAccess/policies/{id}
```

### Step 3: Compare and Generate Diff

**For CREATE (new policy)**:
```
## What Will Change

**CREATE** new Conditional Access policy: `{displayName}`

| Setting | Value |
|---------|-------|
| State | {state} |
| Target Apps | {applications} |
| Target Users | {users} |
| Exclusions | {exclusions} |
| Grant Controls | {grantControls} |
| Session Controls | {sessionControls if any} |
```

**For MODIFY (existing policy)**:
```
## What Will Change

**MODIFY** existing policy: `{displayName}` (ID: {id})

| Field | Current | Proposed |
|-------|---------|----------|
| {field1} | {currentValue} | {proposedValue} |
| {field2} | {currentValue} | {proposedValue} |
| ... | ... | ... |

### Unchanged
- {list of fields that aren't changing}
```

**For NO CHANGE**:
```
## What Will Change

**NO CHANGES** - Proposed policy matches current Entra state.

Policy: `{displayName}` (ID: {id})
```

---

## Comparison Rules

### Fields to Compare

Compare these top-level fields:
- `state`
- `conditions.applications`
- `conditions.users`
- `conditions.platforms`
- `conditions.locations`
- `conditions.clientAppTypes`
- `conditions.devices`
- `conditions.signInRiskLevels`
- `conditions.userRiskLevels`
- `grantControls`
- `sessionControls`

### Ignore These Fields
- `id` (auto-generated)
- `createdDateTime`
- `modifiedDateTime`
- `_metadata` (our tracking field, stripped on deploy)

### Array Comparison
For arrays (like `includeApplications`, `excludeGroups`):
- Show items added: `+ {item}`
- Show items removed: `- {item}`
- Show items unchanged: `{item}`

### Nested Object Comparison
For nested objects, show the specific field that changed:
```
conditions.users.excludeGroups | [] | ["group-id-1", "group-id-2"]
```

---

## Example Output

### Example 1: New Policy
```markdown
## What Will Change

**CREATE** new Conditional Access policy: `CA-Salesforce-Require-MFA`

| Setting | Value |
|---------|-------|
| State | Report-only (`enabledForReportingButNotEnforced`) |
| Target Apps | Salesforce (`0023a5fa-a1ad-481c-ad63-19626dfd5460`) |
| Target Users | All users |
| Exclusions | Break-Glass Accounts (`ca-exclusion-breakglass`) |
| Grant Controls | Require MFA (authentication strength) |
```

### Example 2: Modify Existing
```markdown
## What Will Change

**MODIFY** existing policy: `CA-Salesforce-Require-MFA` (ID: `902a9045-e088-4975-89bd-09fe1dfbd276`)

| Field | Current | Proposed |
|-------|---------|----------|
| conditions.users.excludeGroups | *none* | `CA-Exclusion-BreakGlass`, `CA-Exclude-Testing-Admins` |

### Unchanged
- state: enabledForReportingButNotEnforced
- conditions.applications: Salesforce
- conditions.users.includeUsers: All
- grantControls: MFA (authentication strength)
```

### Example 3: No Changes
```markdown
## What Will Change

**NO CHANGES** - Proposed policy matches current Entra state.

Policy: `CA-Salesforce-Require-MFA` (ID: `902a9045-e088-4975-89bd-09fe1dfbd276`)
```

---

## Tools Available

### Lokka MCP (Graph API)
```
mcp__Lokka-Microsoft__Lokka-Microsoft
- apiType: "graph"
- method: "get"
- path: "/identity/conditionalAccess/policies"
```

---

## Integration with Orchestrator

The Policy Lifecycle Orchestrator should:

1. Generate the policy JSON
2. **Call this Plan prompt** to get the diff
3. Include the diff output in the PR body under "## What Will Change"
4. Create the PR

This ensures every PR shows exactly what will change before deployment.

---

## Reuse for Drift Detection

This same comparison logic powers Drift Detection, just in reverse:
- **Plan**: Compare proposed (repo) → current (Entra) = "what WILL change"
- **Drift**: Compare current (Entra) → baseline (repo) = "what HAS changed"

The diff format is the same, just the direction and context differ.
