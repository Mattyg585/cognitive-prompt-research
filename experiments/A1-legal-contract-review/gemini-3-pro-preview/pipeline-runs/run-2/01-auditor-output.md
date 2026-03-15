---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A1
tier: pipeline
run: 2
stage: 01-contract-auditor
---

```json
[
  {
    "clause_type": "Data Privacy / AI Usage",
    "risk_level": "RED",
    "deviation_description": "Clause explicitly allows Provider to use Customer Content to train AI/ML models. This contradicts the Data Protection priority.",
    "current_text": "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models that are part of Provider's products and services... and Customer authorizes Provider to process its Usage Data and Customer Content for such purposes.",
    "standard_reference": "Strong Data Protection: No use of Customer Content for AI training/product improvement without explicit consent."
  },
  {
    "clause_type": "IP Ownership",
    "risk_level": "RED",
    "deviation_description": "Customer's ownership of their content is qualified by the broad AI training license in Section 1.6.",
    "current_text": "Customer retains all rights in Customer Content, subject to Sections 1.5 and 1.6.",
    "standard_reference": "Customer IP Ownership: Customer should own their data and content without broad encumbrances for Provider's benefit."
  },
  {
    "clause_type": "Limitation of Liability",
    "risk_level": "YELLOW",
    "deviation_description": "Liability cap is defined as a variable ('General Cap Amount') rather than a fixed value. Needs verification against Cover Page to ensure it meets the 12-month standard.",
    "current_text": "Each party's total cumulative liability for all claims will not be more than the General Cap Amount.",
    "standard_reference": "Cap at 12 months fees."
  },
  {
    "clause_type": "Governing Law",
    "risk_level": "YELLOW",
    "deviation_description": "Governing Law is defined as a variable. Needs verification against Cover Page.",
    "current_text": "The Governing Law applies without regard to conflict of laws.",
    "standard_reference": "New York or Delaware."
  },
  {
    "clause_type": "Payment Terms",
    "risk_level": "YELLOW",
    "deviation_description": "Payment terms are defined as a variable ('Payment Process'). Needs verification against Cover Page.",
    "current_text": "Customer will pay Provider Fees... according to the Payment Process.",
    "standard_reference": "Net 30 or Net 45."
  },
  {
    "clause_type": "Term & Termination",
    "risk_level": "GREEN",
    "deviation_description": "Termination for cause matches standard (30 days cure).",
    "current_text": "if the other party fails to cure a material breach of the Framework Terms or an Order Form following 30 days notice",
    "standard_reference": "Mutual termination for cause (30 days cure)."
  }
]
```
