---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A1
tier: baseline
run: 1
---

## Contract Review Summary

**Document**: Common Paper Cloud Service Agreement — Standard Terms Version 2.1
**Parties**: Provider (Vendor) and Customer (You)
**Your Side**: Customer/Buyer
**Deadline**: 2 weeks
**Review Basis**: Generic Commercial Standards (Buyer-friendly, Mid-market SaaS)

## Key Findings

1.  **CRITICAL IP/PRIVACY RISK (AI Training)**: Section 1.6 grants the Provider broad rights to use your Confidential Information and Usage Data to train their AI models. For a $150k/year deal, this is a major leak of intellectual property and potentially sensitive data. **(RED)**
2.  **DATA PROTECTION GAP**: Section 3.1 only requires a Data Processing Agreement (DPA) for GDPR data. As a US-based or global company, you likely need coverage for CCPA/CPRA and other laws. The DPA should be signed now, not "before submitting." **(RED)**
3.  **LIABILITY CAP UNCERTAINTY**: The contract structure relies on a "Cover Page" to define liability caps. Without a "Super Cap" for data breaches (usually 2-3x fees or higher fixed amount) and uncapped IP indemnification, you are exposed. **(YELLOW)**

## Clause-by-Clause Analysis

### IP Ownership & AI Training -- RED
**Contract says**: "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence... Customer authorizes Provider to process..." (Sec 1.6)
**Playbook position**: Customer owns all Customer Content. Vendor can only use it to provide the service, not to train models for other customers.
**Deviation**: Explicit grant of rights to train AI on your data.
**Business impact**: Your proprietary data could improve the product for competitors or leak into the model.
**Redline suggestion**: Strike the training rights or limit strictly to "aggregated, de-identified Usage Data only (excluding Customer Content)."

### Data Protection -- RED
**Contract says**: "Before submitting Personal Data governed by GDPR, Customer must enter into a data processing agreement..." (Sec 3.1)
**Playbook position**: DPA must be executed for *all* personal data (CCPA, etc.) and incorporated immediately.
**Deviation**: Limits DPA trigger to GDPR only.
**Business impact**: Regulatory non-compliance risk if you process non-EU data.
**Redline suggestion**: "The parties will execute Provider's standard DPA, which is incorporated by reference here. Provider represents that it complies with all Applicable Data Protection Laws."

### Indemnification -- YELLOW
**Contract says**: Provider indemnifies "Provider Covered Claims" (Sec 9.1).
**Playbook position**: Vendor must indemnify for IP infringement, unmodified.
**Deviation**: "Provider Covered Claims" is a defined term (likely in Cover Page/Definitions) not visible here. Standard Common Paper usually covers IP, but we must verify.
**Business impact**: If "Provider Covered Claims" is defined narrowly, you may be liable for using their tool.
**Redline suggestion**: Ensure "Provider Covered Claims" expressly includes "claims that the Cloud Service infringes any third party intellectual property right."

### Limitation of Liability -- YELLOW
**Contract says**: Caps liability at "General Cap Amount" and "Increased Cap Amount" for "Increased Claims" (Sec 8.1).
**Playbook position**: General Cap = 12 months' fees. Super Cap (Data Breach) = 3x fees. IP Indemnification = Uncapped.
**Deviation**: Structure is good, but amounts are hidden in variables.
**Business impact**: Low caps mean you cannot recover damages if they cause a massive breach.
**Redline suggestion**: Define General Cap as "12 months' fees paid/payable" and Increased Cap (for Data Breach) as "3x General Cap." Clarify that IP Indemnification is an "Unlimited Claim."

### Term & Termination -- YELLOW
**Contract says**: Auto-renewal unless notice given. Termination for cause only (Sec 5).
**Playbook position**: Termination for Convenience (TfC) preferred for buyers.
**Deviation**: No TfC.
**Business impact**: Locked into $150k/year even if the tool is shelfware.
**Redline suggestion**: Add: "Customer may terminate an Order Form for convenience upon 30 days' prior written notice." (Likely a trade-off point).

## Negotiation Strategy

1.  **Lead with Tier 1 (Must-Haves)**:
    *   **Strike Section 1.6 (AI Training)** on Customer Content. This is non-negotiable for IP safety.
    *   **Expand Section 3.1 (Data)** to include a DPA for *all* data, not just GDPR.

2.  **Trade Tier 2 (Should-Haves)**:
    *   Push for **Termination for Convenience**. If they refuse, trade it for a **Data Breach Super Cap** (3x fees).
    *   Accept the **Logo Rights** (Sec 12.8) only if they agree to the **IP Training** fix.

3.  **Next Steps**:
    *   Request the "Cover Page" to see the actual Cap Amounts and Definitions.
    *   Send the redline for Section 1.6 immediately.