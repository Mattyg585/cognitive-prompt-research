---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: pipeline
run: 2
stage: 01-intake-and-basis
---

document:
  title_or_id: "Common Paper Cloud Service Agreement — Standard Terms v2.1"
  source: file
  language: "en"
party_context:
  our_role: customer/buyer
  counterparty: "Provider (unnamed in provided text)"
deal_context:
  deadline: "2 weeks"
  deal_size_or_tier: "mid-market (~$150K/year)"
  strategic_importance: "New vendor; important but not strategic"
  focus_areas:
    - data_protection
    - ip_ownership
review_basis:
  basis: generic_standards
  playbook_files_used: []
  playbook_found: false
  missing_inputs:
    - "Any organization-specific legal/procurement playbook or fallback positions to apply"
    - "Cover Page / Key Terms / Order Form values (fees, term, use limitations, liability caps, notice dates, etc.)"
    - "Counterparty legal entity name and any special regulatory constraints (if applicable)"
assumptions:
  - "Review is from the Customer/buyer perspective per provided test scenario."
  - "No organizational playbook files were found in the repository using lightweight pattern search."
  - "Only the Standard Terms text was provided; Cover Page / Order Form terms are not included."