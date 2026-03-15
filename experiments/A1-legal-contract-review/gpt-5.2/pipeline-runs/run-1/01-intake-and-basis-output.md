---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: pipeline
run: 1
stage: 01-intake-and-basis
---

document:
  title_or_id: "Common Paper Cloud Service Agreement — Standard Terms Version 2.1"
  source: file
  language: English
party_context:
  our_role: customer/buyer
  counterparty: "Provider (name not specified)"
deal_context:
  deadline: "2 weeks"
  deal_size_or_tier: "$150K/year; mid-market"
  strategic_importance: "Not strategic but important"
  focus_areas:
    - data protection
    - IP ownership
review_basis:
  basis: generic_standards
  playbook_files_used: []
  playbook_found: false
  missing_inputs:
    - "Any customer legal playbook / preferred positions (if available)"
    - "Executed Order Form / Cover Page / Key Terms for variables (term, pricing, SLA, governing law, notice addresses)"
    - "Counterparty legal name and jurisdiction"
    - "DPA and any security/privacy addenda (if applicable)"
assumptions:
  - "Review is from the Customer/buyer perspective per the provided scenario."
  - "Only the Standard Terms v2.1 text was provided; Order Form/Key Terms are not included."
  - "Priority focus areas are data protection and IP ownership."
