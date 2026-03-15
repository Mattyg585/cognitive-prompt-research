# Pipeline Handoff Specifications

## 1. Investigator → Diagnostician

### What Crosses
*   **Facts**: Raw error messages, stack traces, log excerpts.
*   **Context**: Relevant file paths, recent commit SHAs, PR descriptions.
*   **Reproduction**: Steps taken to verify the issue, environment details.
*   **Observations**: Confirmed behaviors (what works vs what fails).

### What Gets Dropped
*   **Hypotheses**: Guesses about *why* it's happening (unless explicitly confirmed).
*   **Fix Ideas**: Suggestions for code changes.
*   **Speculation**: Unverified theories.

### Format: Investigation Report (Markdown)
```markdown
# Investigation Report

## Validated Behavior
- **Expected**: [Behavior]
- **Actual**: [Behavior]
- **Reproduction**: [Steps verified]

## Context Gathered
- **Files Involved**: [List of paths]
- **Recent Changes**: [Relevant commits/PRs]
- **Logs/Errors**: [Exact text]

## Observations
- [Fact 1]
- [Fact 2]
```

---

## 2. Diagnostician → Resolver

### What Crosses
*   **Root Cause**: The definitive "why" backed by evidence.
*   **Mechanism**: Explanation of the failure chain.
*   **Scope**: Specific files and lines to modify.
*   **Requirements**: Constraints for the fix (e.g., performance, side effects).

### What Gets Dropped
*   **Investigation History**: Dead ends and failed reproduction attempts.
*   **Alternative Theories**: Discarded hypotheses.

### Format: Diagnosis Report (Markdown)
```markdown
# Diagnosis Report

## Root Cause
[Definitive explanation]

## Mechanism
1. [Step 1 of failure]
2. [Step 2 of failure]

## Requirements for Fix
- **Target Files**: [Paths]
- **Constraints**: [Performance, compatibility, etc.]
- **Verification**: [Test case to add]
```
