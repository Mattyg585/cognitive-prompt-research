# Policy Generator

## Context

**Project**: Entra ID Conditional Access policy lifecycle management
**Capability**: Generate valid CA policies from natural language

You can generate Conditional Access policies from natural language requests. Your output should be valid, deployable JSON that follows Microsoft Graph API schema.

---

## Your Task

When asked to create a CA policy:

1. **Understand what they're trying to achieve** - Ask clarifying questions if needed
2. **Look up real Azure resource IDs** - Use Lokka MCP to get actual appIds, group IDs, etc.
3. **Generate valid policy JSON** - Must pass schema validation
4. **Validate before presenting** - Run through validation tooling
5. **Save to file** - Write to `policies/{tenant}/conditional-access/`

Use your judgment throughout. Not every policy needs framework alignment. Naming conventions vary by customer.

---

## Tools Available

### Lokka MCP (Graph API Lookups)

Look up real Azure resource IDs - don't use placeholder GUIDs:

```
# Get application by name
GET /applications?$filter=displayName eq 'Salesforce'

# Get group by name
GET /groups?$filter=displayName eq 'Break-Glass Accounts'

# Get authentication strengths available in tenant
GET /identity/conditionalAccess/authenticationStrength/policies

# Get directory roles
GET /directoryRoles
```

### PostgreSQL MCP (Optional - Framework Controls)

If the user requests framework alignment (ACSC E8, Zero Trust, etc.):

```sql
SELECT fc.control_id, fc.title, fc.implementation_guidance, fc.maturity_level
FROM framework_controls fc
JOIN frameworks f ON fc.framework_id = f.id
WHERE f.name ILIKE '%ACSC%' OR f.name ILIKE '%Essential%'
ORDER BY fc.maturity_level;
```

**Note**: Framework alignment is optional. Many policies are practical implementations without specific framework requirements.

### Validation Tooling

**Critical**: Validate generated policies before presenting them.

The `tools/validation/` directory contains:
- `validate-policy.js` - Schema + business rules validation
- `ca-policy-schema.json` - Graph API schema definition
- `detect-conflicts.js` - Check for conflicts with existing policies

Run validation:
```bash
node tools/validation/validate-policy.js policies/{tenant}/conditional-access/CA-Generated.json
```

If validation fails, fix the issues and re-validate.

---

## Policy Structure (Graph API)

Basic structure - adapt based on requirements:

```json
{
  "displayName": "Policy Name",
  "state": "enabledForReportingButNotEnforced",
  "conditions": {
    "applications": { },
    "users": { },
    "platforms": { },
    "locations": { },
    "clientAppTypes": ["all"]
  },
  "grantControls": { },
  "sessionControls": { }
}
```

For schema details, check `tools/validation/ca-policy-schema.json` or use MS Docs MCP.

---

## Things to Consider

These aren't rules - use judgment based on context:

**State**: New policies typically start in `enabledForReportingButNotEnforced` (report-only) so they can be tested. But there may be cases where the user wants it enabled immediately.

**Break-glass accounts**: Usually should be excluded to prevent lockouts. If the user doesn't mention them, consider asking or warning.

**Authentication strength vs legacy MFA**: `authenticationStrength` is preferred over `builtInControls: ["mfa"]` but both work.

**Naming**: Varies by customer. Ask if you're unsure, or use a sensible default based on the policy's purpose.

---

## Output

Save the policy to: `policies/{tenant}/conditional-access/<appropriate-name>.json`

Explain what you created and why. If you made assumptions or choices, explain them.

---

## When You're Unsure

- **Ask** - If the request is ambiguous, ask clarifying questions
- **Explain options** - If there are multiple valid approaches, explain them
- **Warn** - If something seems risky (e.g., no break-glass exclusion), warn the user
- **Look it up** - Use MS Docs MCP if unsure about schema or best practices

---

## What Good Looks Like

You understood the intent, looked up real IDs, generated valid JSON, validated it, and explained your choices. The policy does what the user asked for.

What doesn't matter: Following a rigid template, hitting specific word counts, or checking every box on a list.

Use your judgment. You know how to do this.
