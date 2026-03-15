---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A1
tier: pipeline
run: 3
stage: 01-contract-auditor
---
```json
[
  {
    "clause_type": "Intellectual Property / AI Training",
    "risk_level": "RED",
    "deviation_description": "Contract allows Provider to use Customer Content to train AI/ML models. This creates a risk of IP leakage and confidentiality breach, directly conflicting with the priority of IP ownership and data protection.",
    "current_text": "Usage Data and Customer Content may be used to develop, train, or enhance artificial intelligence or machine learning models... Customer authorizes Provider to process its Usage Data and Customer Content for such purposes.",
    "standard_reference": "Customer Data should only be used to provide the Service. No rights to train models on Customer Content."
  },
  {
    "clause_type": "Warranty Remedy",
    "risk_level": "RED",
    "deviation_description": "Cure period for material functionality reduction is 45 days. This is excessive for a $150k/year contract and could leave the business without a working tool for 1.5 months before termination rights trigger.",
    "current_text": "Within 45 days of receiving sufficient details, Provider will attempt to restore the general functionality.",
    "standard_reference": "Standard cure period for material breach is 30 days; critical functionality issues usually require faster resolution (e.g., 7-10 days)."
  },
  {
    "clause_type": "Governing Law",
    "risk_level": "YELLOW",
    "deviation_description": "Governing Law is defined as a variable in the Cover Page (not provided), rather than explicitly stated as NY or DE.",
    "current_text": "The Governing Law applies without regard to conflict of laws.",
    "standard_reference": "Must be New York or Delaware."
  },
  {
    "clause_type": "Limitation of Liability",
    "risk_level": "YELLOW",
    "deviation_description": "Liability cap amount is defined as a variable ('General Cap Amount') in the Cover Page (not provided). Cannot verify if it meets the 12-month fee standard.",
    "current_text": "Each party's total cumulative liability for all claims will not be more than the General Cap Amount.",
    "standard_reference": "Cap at 12 months fees."
  },
  {
    "clause_type": "Indemnification",
    "risk_level": "GREEN",
    "deviation_description": "Indemnification is mutual, matching the standard structure.",
    "current_text": "Provider will indemnify... Customer from Provider Covered Claims... Customer will indemnify... Provider from Customer Covered Claims",
    "standard_reference": "Must be mutual."
  },
  {
    "clause_type": "Term & Termination",
    "risk_level": "GREEN",
    "deviation_description": "Termination for cause includes a 30-day cure period, matching the standard.",
    "current_text": "if the other party fails to cure a material breach of the Framework Terms or an Order Form following 30 days notice",
    "standard_reference": "Mutual termination for cause (30 days cure)."
  },
  {
    "clause_type": "Consequential Damages",
    "risk_level": "GREEN",
    "deviation_description": "Waiver of consequential damages is mutual and present.",
    "current_text": "Neither party will be liable for lost profits or revenues... or for consequential, special, indirect... damages",
    "standard_reference": "No consequential damages."
  }
]
```
