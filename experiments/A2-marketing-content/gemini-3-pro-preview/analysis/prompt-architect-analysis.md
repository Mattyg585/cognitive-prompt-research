# Prompt Architect Analysis: Marketing Content Skill

**Analyzer:** Prompt Architect Agent
**Target:** `experiments/A2-marketing-content/original/SKILL.md`
**Date:** 2026-03-15

## 1. Cognitive Map

This prompt functions as a **Structural Scaffolding** engine. It does not ask the model to *think* about marketing strategy; it asks the model to *conform* to marketing conventions.

*   **Primary Mode:** **Constraint Satisfaction**. The prompt is dominated by specific limits (character counts, section counts, component checklists).
*   **Secondary Mode:** **Pattern Matching**. It provides rigid templates (Blog, Social, Email) and expects the model to map user input into these shapes.
*   **Missing Mode:** **Strategic Reasoning (System 2)**. There is no instruction to analyze the target audience, determine the unique selling proposition, or construct a logical argument *before* writing.

The prompt assumes the user provides a high-quality "Seed" (the core idea) and the model merely applies the "Lens" (formatting). If the user provides a weak seed (e.g., "write about coffee"), the model will produce a structurally perfect but intellectually empty artifact ("The Ultimate Guide to Coffee: 3 Reasons Why...").

## 2. Mode Interference

### A. The "Compliance vs. Creativity" Conflict
The prompt is saturated with numeric anchors and formatting constraints that trigger the model's "Checklist" mode, suppressing its "Storytelling" mode.

> **Quote:** *"Headline — clear, benefit-driven, includes primary keyword (aim for 60 characters or less for SEO)"*

**Mechanism:** When an LLM is given a hard constraint ("60 characters") and a semantic goal ("benefit-driven"), it prioritizes the hard constraint because it is easily verifiable. This often results in truncated, awkward, or generic headlines that fit the box but fail to compel.

### B. The "Template Trap" (Schema Overfitting)
The rigid structures force content into buckets even when it doesn't fit.

> **Quote:** *"Body sections (3-5 sections) — each with a descriptive subheading (H2). Use H3 for subsections. One core idea per section..."*

**Mechanism:** This induces **Schema Overfitting**. The model will fabricate "3-5 sections" even if the topic only warrants two, or requires a continuous narrative. It encourages "fluff" generation to fill the pre-defined slots.

### C. Context Vacuum (Missing Stance)
The prompt describes *what* a blog post looks like, but not *who* is writing it or *who* is reading it.

> **Quote:** *"Write at an 8th-grade reading level for broad audiences; adjust up for technical audiences"*

**Mechanism:** This is a superficial style instruction, not a cognitive stance. Without a "Strategist" stance (e.g., "You are a direct-response copywriter focused on conversion"), the model defaults to its training average: bland, corporate-safe marketing speak.

## 3. Diagnostic Signals (What to look for in output)

*   **The "Three-Point" Hallucination:** Content that arbitrarily divides every topic into exactly 3 or 5 points, regardless of logic.
*   **Hollow Hooks:** Introductions that use the "Question/Stat" formula but feel disconnected from the actual value proposition (e.g., "Did you know 50% of people like X? That's why X is important.").
*   **Keyword Stuffing:** Primary keywords inserted awkwardly in the first sentence to satisfy the "include primary keyword" constraint, damaging flow.
*   **Generic "Benefit" Language:** phrases like "unlock your potential," "streamline your workflow," or "take it to the next level" appearing repeatedly because the model is simulating a "generic marketer" rather than a specific brand voice.
*   **Orphaned CTAs:** Calls to action that are technically present (satisfying the checklist) but psychologically unearned.

## 4. Intervention Strategy

### Tier 1: Prompt-Level Fixes (Low Cost)
*   **Add a "Pre-flight" Step:** Instruct the model to *think* before writing.
    *   *Add:* "Before writing, output a <strategy> block: Define the Target Audience, the One Key Insight, and the Reader's Pain Point."
*   **Softening Constraints:** Change hard limits to targets.
    *   *Change:* "Aim for 60 chars" -> "Prioritize impact; aim for short headlines where possible."
*   **Inject Voice:** Add a persona instruction.
    *   *Add:* "Write not as a content farm, but as a subject matter expert having a conversation over coffee. Avoid corporate jargon."

### Tier 2: Pipeline-Level Interventions (High Value)
*   **The "Strategist-Writer-Editor" Chain:**
    1.  **Agent A (Strategist):** Receives the topic. Outputs a Creative Brief (Audience, Angle, Outline, Key Arguments).
    2.  **Agent B (Writer):** Receives the Brief. Writes the draft *ignoring* character counts and focusing on flow/persuasion.
    3.  **Agent C (Editor):** Receives the Draft and the Original Skill Rules (SEO, formatting). Edits the draft to fit the constraints without killing the soul.

**Recommendation:** The current prompt is a "Reference Sheet" masquerading as a "Skill". It needs to be reframed to guide the *process* of writing, not just the *structure* of the output. I recommend a Tier 2 approach for high-stakes content, but a Tier 1 fix is sufficient for a general-purpose utility.
