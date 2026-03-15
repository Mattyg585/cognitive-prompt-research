# Experiment A6 Evaluation: SecOps Incident Response

**Model:** gemini-3-pro-preview
**Date:** 2026-03-15
**Evaluator:** Blind Evaluator

## 1. Summary of Outputs

*   **Baseline:** Produced a standard, competent incident postmortem. It covered the basic facts (what, when, how) and provided a standard "5 Whys" analysis. Action items were relevant but somewhat generic.
*   **Optimised:** Significantly enriched the analysis by adding a "Root Cause Analysis (Drill Down)" section that explicitly categorized causes into **Proximal**, **Systemic**, and **Process** categories, alongside the "5 Whys". This added structural depth to the learning. Action items were robust.
*   **Pipeline:** Produced highly polished, professional reports with "Executive Summaries" and clean formatting. However, it reverted to a standard "5 Whys" structure, dropping the explicit "Drill Down" categorization found in the Optimised runs. The focus shifted slightly from deep analysis to clear reporting.

## 2. Scoring

| Dimension | Baseline | Optimised | Pipeline |
| :--- | :---: | :---: | :---: |
| **1. Depth** | 3 | 5 | 4 |
| **2. Specificity** | 3 | 4 | 4 |
| **3. Natural Variation** | N/A* | 4 | 3 |
| **4. Completeness** | 3 | 5 | 4 |
| **5. Audience Awareness** | 3 | 4 | 5 |
| **6. Org Learning (Domain)** | 3 | 5 | 4 |

*\*Baseline had only 1 run available.*

### Reasoning

*   **Depth:** The **Optimised** version achieves a 5 because of the "Drill Down" section. Distinguishing between *Proximal* (developer error), *Systemic* (secure-by-default gaps), and *Process* (testing gaps) causes forces a deeper level of analysis than just a list of whys. The **Pipeline** is good (4) but loses this explicit structural scaffolding for depth.
*   **Specificity:** Both **Optimised** and **Pipeline** improved on the Baseline by being more precise about the failure mechanisms (e.g., specifying that Snyk checked dependencies but not logic).
*   **Natural Variation:** The **Optimised** runs showed good variation in phrasing while maintaining the superior "Drill Down" structure. **Pipeline** runs were very similar to each other, bordering on templated.
*   **Completeness:** **Optimised** feels the most complete as a learning tool because it attacks the root cause from two angles (Drill Down + 5 Whys). **Pipeline** is complete as a report but slightly less comprehensive as an analysis.
*   **Audience Awareness:** **Pipeline** wins here (5). It adds an "Executive Summary" and formats the document perfectly for a leadership read. **Optimised** is a great engineering doc, but Pipeline is a great *company* doc.
*   **Organisational Learning (Domain):** **Optimised** wins. The explicit separation of "Process" and "Systemic" causes is exactly what transforms an incident report into an organisational learning artifact.

## 3. Comparative Analysis

### Optimised vs. Baseline
The **Optimised** output is a clear tier above the Baseline. The Baseline is a "fill in the blanks" form; the Optimised version is a thoughtful analysis. The addition of the "Drill Down" section is a high-leverage prompt engineering win that drastically improves the utility of the output without requiring more tokens.

### Pipeline vs. Optimised
This is an interesting trade-off.
*   **Optimised** is better for **Engineers and Architects**. It breaks down the failure modes explicitly.
*   **Pipeline** is better for **Executives and Stakeholders**. It is polished, concise, and professional.

However, since the goal is "Organisational Learning," the **Optimised** version is arguably superior because it retains the raw analytical distinctions that might get smoothed over in a "polished" pipeline run. The Pipeline smoothed the "Drill Down" section back into a narrative or standard 5 Whys, which actually *reduced* the analytical clarity slightly in favor of readability.

## 4. Conclusion

**Winner:** **Optimised**

The **Optimised** single-turn prompt produced the most valuable artifact for preventing recurrence (the core goal of a postmortem). The separation of cause types (Proximal/Systemic/Process) is a critical cognitive aid that the Pipeline effectively "polished away."

**Recommendation:** The Pipeline should be adjusted to *retain* the "Drill Down" structure from the Optimised prompt, as it adds significant value that is lost in the current multi-stage process. The ideal output would be the **Pipeline's polish** wrapping the **Optimised version's analytical structure**.
