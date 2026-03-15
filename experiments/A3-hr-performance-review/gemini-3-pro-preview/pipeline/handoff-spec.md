# Pipeline Handoff Specification: HR Performance Review

## Overview
This pipeline transforms raw employee activity data into a structured, unbiased performance review. It separates the cognitive modes of **Search** (comprehensive recall), **Analysis** (impact evaluation), and **Construction** (formatting).

## Flow
`1-activity-logger` -> `2-impact-analyst` -> `3-review-writer`

---

## Handoff 1: Activity Log
**From:** `1-activity-logger`
**To:** `2-impact-analyst`

### Content
A comprehensive, unfiltered chronological list of all work items found in the source data.
*   **Format:** JSON List or Markdown Table.
*   **Fields:**
    *   `Date`: YYYY-MM-DD
    *   `Source`: (e.g., Jira, Slack, Email)
    *   `Activity`: Brief description of task/event.
    *   `Status`: Completed, In Progress, Blocked.
    *   `Context`: Any relevant details (collaborators, blockers).

### Constraints
*   **NO Filtering:** Do not omit "minor" tasks.
*   **NO Evaluation:** Do not label as "good" or "bad".
*   **completeness:** Must cover the entire review period.

---

## Handoff 2: Impact Assessment
**From:** `2-impact-analyst`
**To:** `3-review-writer`

### Content
A selected set of key accomplishments and development areas, justified by business impact.
*   **Format:** Structured Markdown.
*   **Sections:**
    1.  **Top 3-5 Accomplishments:**
        *   `Headline`: Punchy summary.
        *   `Evidence`: Specific tasks/dates from the log.
        *   `Impact`: Why it mattered (revenue, efficiency, team health).
    2.  **Key Challenges/Misses:**
        *   `Issue`: What went wrong.
        *   `Cause`: Context from log (not blame).
        *   `Pattern`: Is this isolated or recurring?
    3.  **Recommended Rating:** Based on evidence (Exceeds/Meets/Below).

### Constraints
*   **Selection Logic:** Must be based on *impact*, not *recency*.
*   **Balance:** Must include both wins and misses if present.
*   **Evidence-Based:** Every claim must reference a specific item from the Activity Log.

---

## Final Output
**From:** `3-review-writer`
**To:** User

### Content
The final, polished performance review in the required company format.
*   **Format:** Official Markdown Template.
*   **Tone:** Professional, constructive, objective.
