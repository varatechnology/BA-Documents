Thank you for your feedback. Let’s make Step 3 far more illustrative and visual, focusing on:  
- The actors and their actions  
- Exact flows for a deep field check, including document upload (if any)  
- The feedback/results mechanism  
- Privacy protections and candidate notifications

Here’s an enhanced, visually organized boxed diagram:

---

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
| Diagram Title: Step 3 – Specific Field-Level Verification Flow                         |
| Purpose: Visually demonstrates how verifiers select/check target fields,               |
| how issuer systems respond, and how results are securely returned and logged.          |
|                                                                                        |
| [Actors & Flow:]                                                                       |
|                                                                                        |
|   ┌────────┐   1. Sees full basic data (after Step 2 success)                          |
|   |Verifier|---------------------------------------------------------------------------┐
|   └────────┘                                                                            |
|        |                                                                               |
|        | 2. Selects field(s) to verify (e.g. "Marks", "Subject", "Exam Year")          |
|        |  [Optional: Uploads scan or photo of paper certificate for cross-check]        |
|        ▼                                                                               |
|   ┌────────────────┐    3. Sends secure field-verification request to Certcheck        |
|   | Certcheck UI   |-------------------------------------------------------------------|
|   └────────────────┘                                                                    |
|        |                                                                               |
|        ▼                                                                               |
| ┌────────────────────┐    4. Certcheck sends API call (field(s) only, not whole cert)  |
| |Issuer Client System|-----------------------------------------------------------------┐
| └────────────────────┘                                                                 |
|        |                                                                               |
|        |   5. Looks up original issuance records, compares each requested field        |
|        ▼                                                                               |
| ┌────────────────────┐                                                                 |
| |Issuer Client System|    6. Returns response per field: "Match"  "Mismatch"  Note     |
| └────────────────────┘                                                                 |
|        |                                                                               |
|        ▼                                                                               |
|   ┌────────────────┐    7. Certcheck presents field-level results:                     |
|   | Certcheck UI   |-------------------------------------------------------------------|
|   └────────────────┘        - Green "✔ Match" OR   Red "✗ Mismatch" per field          |
|        |                    - Visual side-by-side: scanned document vs. issuer value   |
|        ▼                                                                               |
|   ┌────────┐                                                                            |
|   |Verifier|    8. Verifier reviews, can download PDF report or take next action        |
|   └────────┘    (for audit, HR, embassy, etc.)                                         |
|                                                                                        |
| [Privacy & Logging:]                                                                   |
| - Every request is session-logged by Certcheck; includes verifier, fields, timestamps  |
| - Candidate is notified: "Your certificate was deep-verified by [Verifier]"            |
| - Only requested fields' values are exchanged; no extra or unrelated data is shown     |
|                                                                                        |
| Key Elements:                                                                         |
| - Field selection & optional document upload by verifier                               |
| - Per-field "Match"/"Mismatch" response only                                          |
| - All actions are auditable and transparent                                           |
| - Candidate always informed of what was accessed                                      |
|                                                                                        |
| Relationships:                                                                        |
| - Verifier asks, issuer confirms/denies, candidate kept in the loop at every step     |
|                                                                                        |
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

**This illustration provides:**  
- A clear vertical flow from verifier’s action → Certcheck → Issuer Client → back to verifier
- Explicit mention of field selection and document upload  
- Emphasis on feedback (“Match”/“Mismatch”)  
- Strong privacy and audit trail with candidate notifications for every deep check

**Would you like an end-to-end “full experience” diagram to tie all three steps into a single visual artifact, or more of an interactive wireframe/mockup for this step?**