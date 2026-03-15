---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A1
tier: optimised
run: 2
---

# Contract Review: Common Paper Cloud Service Agreement v2.1

**Context**: Customer/Buyer | SaaS Agreement ($150K/yr) | Standard Used: Generic Commercial + Priorities (Data Protection, IP)

## Phase 1: Diagnosis & Risk Assessment

| Clause | Status | Gap Analysis (Current vs Standard) | Business Impact |
| :--- | :--- | :--- | :--- |
| **1.6 Machine Learning** | 🔴 RED | Current: Provider uses Customer Content to train AI models. Standard: No use of Customer Data for product improvement without opt-in. | Loss of IP control; data privacy risk; aids competitors. |
| **8. Liability Caps** | 🟡 YELLOW | Current: Caps defined in "Cover Page" (missing). Structure exists for "Increased Claims". Standard: 12mo fees (General), 3x/Uncapped (Data/IP). | Potential exposure if "Increased Cap" is low or excludes Data Breach. |
| **2.2 Suspension** | 🟡 YELLOW | Current: Notice "when practical". Standard: Prior notice required (except emergencies). | Risk of sudden operational disruption. |
| **12.8 Logo Rights** | 🟡 YELLOW | Current: Unilateral right to use logo. Standard: Requires Customer consent. | Reputational control. |
| **9. Indemnification** | 🟢 GREEN | Current: Mutual structure (Provider covers "Provider Covered Claims"). Standard: Mutual IP indemnity. | Appears standard, pending "Covered Claims" definition. |

*(Note: "Cover Page" definitions were not provided, so Liability analysis assumes standard Common Paper structure but flags the specific values/inclusions needed.)*

## Phase 2: Recommended Redlines & Strategy

### High Priority Issues (Red/Yellow)

**1. Machine Learning & Data Use (Section 1.6)**
*   **Current Text**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models..."
*   **Redline**: "Usage Data and Customer Content may **NOT** be used to develop, train, or enhance artificial intelligence or machine learning models..." (Or delete section 1.6 entirely and rely on 2.1(a)(x) regarding rights).
*   **Rationale (External)**: "Due to internal data governance and IP policies, we cannot grant rights for our data to train public or shared models."
*   **Fallback**: Limit to *Usage Data* only (exclude Customer Content), and strictly aggregated/anonymized.

**2. Limitation of Liability (Section 8)**
*   **Current Text**: [Refers to General/Increased Caps]
*   **Redline**: [Add to Cover Page or Amendment]: "General Cap Amount: 12 months' Fees. Increased Cap Amount: 3x General Cap Amount (covering Data Breach, Confidentiality, IP)."
*   **Rationale (External)**: "Standard market position for a deal of this size and data sensitivity."
*   **Fallback**: 24 months for Data Breach; Super-cap only for *direct* damages.

**3. Suspension (Section 2.2)**
*   **Current Text**: "Provider will try to inform Customer before suspending Customer's account when practical."
*   **Redline**: "Provider will provide Customer with at least five (5) business days' prior written notice before suspending... except in cases of emergency security threats."
*   **Rationale (External)**: "We need time to cure inadvertent issues before business interruption."
*   **Fallback**: Notice "concurrent with suspension."

**4. Marketing (Section 12.8)**
*   **Current Text**: "Provider may use Customer's name and logo in marketing."
*   **Redline**: "Subject to Customer's prior written consent, Provider may use..."
*   **Rationale (External)**: "Corporate policy requires brand team approval."
*   **Fallback**: Permitted for "customer list" only, not press releases.

### Negotiation Strategy
*   **Must-Haves**: 
    1.  **Section 1.6 (AI Training)**: Absolute restriction on using *Customer Content* for training. (Top Priority: Data/IP).
    2.  **Liability Caps**: Confirming Data Breach fits into "Increased Claims" with adequate multiplier.
*   **Trade-Offs**: 
    *   Can concede on **Audit Rights** (not listed, but if requested).
    *   Can concede on **General Cap** amount (12mo vs 6mo) if Data Breach super-cap is secured.
    *   Can accept **Suspension** terms if "Emergency" is strictly defined.
*   **Next Steps**: Request the "Cover Page" to verify Cap amounts and definitions of "Covered Claims". Submit redline on Section 1.6 immediately.
