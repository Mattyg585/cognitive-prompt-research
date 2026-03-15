---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A1
tier: pipeline
run: 1
stage: 01-contract-auditor
---

```json
[
  {
    "clause_type": "Data Usage & AI Training",
    "risk_level": "RED",
    "deviation_description": "Grant of rights to use Customer Content for training Vendor's AI/ML models is a major deviation from data protection and IP ownership priorities.",
    "current_text": "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services... Customer authorizes Provider to process its Usage Data and Customer Content for such purposes.",
    "standard_reference": "Customer/Buyer Priorities: Data protection and IP ownership"
  },
  {
    "clause_type": "Indemnity (Customer Liability)",
    "risk_level": "RED",
    "deviation_description": "Customer indemnity appears to be uncapped for IP infringement (if 'Unlimited Claims' includes IP), violating the standard to cap liability.",
    "current_text": "Section 8.1 [Liability Caps] does not apply to Unlimited Claims.",
    "standard_reference": "Indemnity: No IP infringement uncapped"
  },
  {
    "clause_type": "Limitation of Liability (Consequential Damages)",
    "risk_level": "YELLOW",
    "deviation_description": "Consequential damages waiver has an exception for Confidentiality breaches.",
    "current_text": "Section 8.2 [Damages Waiver] does not apply to ... breach of Section 10 (Confidentiality).",
    "standard_reference": "Limitation of Liability: No consequential damages"
  },
  {
    "clause_type": "Governing Law",
    "risk_level": "YELLOW",
    "deviation_description": "Governing law is defined by variable, not explicitly fixed to NY or DE in the Standard Terms.",
    "current_text": "The Governing Law applies... Chosen Courts have exclusive jurisdiction.",
    "standard_reference": "Governing Law: Must be New York or Delaware"
  },
  {
    "clause_type": "Term & Termination",
    "risk_level": "GREEN",
    "deviation_description": "Termination for cause provisions match the standard.",
    "current_text": "Either party may terminate ... if the other party fails to cure a material breach ... following 30 days notice",
    "standard_reference": "Term & Termination: Mutual termination for cause (30 days cure)"
  }
]
```
