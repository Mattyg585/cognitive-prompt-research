# Handoff Specification: Marketing Content Pipeline

This document defines the structured information passed between agents in the pipeline.

## 1. Strategist -> Writer (The Creative Brief)

**Goal:** Establish the strategic direction before writing begins.
**Format:** Structured Markdown.

### Content Structure
```markdown
# Creative Brief

## Target Audience
- **Persona:** [Specific role/demographic]
- **Pain Point:** [What keeps them up at night?]
- **Desired Outcome:** [What do they want to achieve?]

## Core Strategy
- **Unique Selling Proposition:** [Why is this solution different?]
- **Key Insight:** [The one thing they need to understand]
- **Call to Action:** [What specifically should they do next?]

## Content Outline
- **Working Title:** [Provisional headline]
- **Introduction Hook:** [How we grab attention]
- **Key Point 1:** [Argument + Evidence]
- **Key Point 2:** [Argument + Evidence]
- **Key Point 3:** [Argument + Evidence]
- **Conclusion:** [How we wrap up]

## Tone & Voice
- **Style:** [e.g., Authoritative but friendly]
- **Avoid:** [e.g., Jargon, passive voice]
```

**Why Separate:**
The Strategist defines *what* to say. The Writer focuses on *how* to say it.

## 2. Writer -> Editor (The First Draft)

**Goal:** Deliver a compelling narrative flow without worrying about character counts or SEO constraints.
**Format:** Raw Markdown text.

### Content Structure
```markdown
# [Draft Headline]

[Introduction paragraph(s) focused on the hook]

## [Section 1 Header]
[Content focused on Key Point 1. Flow and persuasion are prioritized over brevity.]

## [Section 2 Header]
[Content focused on Key Point 2.]

...

## Conclusion
[Final thoughts and Call to Action]
```

**Why Separate:**
Writing for flow requires ignoring length constraints. The Writer produces "too much good content," and the Editor cuts it down.

## 3. Editor -> Final Output (The Polished Asset)

**Goal:** Ensure the content meets all technical requirements (SEO, formatting) while preserving the narrative flow.
**Format:** Final formatted content (Markdown/HTML as requested).

### Content Structure
*   **Headline:** Optimized for SEO/Clicks (under 60 chars if required).
*   **Body:** Formatted with H2/H3, bullet points, and short paragraphs.
*   **SEO:** Keywords naturally integrated.
*   **Meta Description:** Added if requested.
