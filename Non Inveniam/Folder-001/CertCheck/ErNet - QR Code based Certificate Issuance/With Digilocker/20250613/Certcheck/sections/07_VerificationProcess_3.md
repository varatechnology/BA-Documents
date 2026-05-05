Thank you for your feedback. Let’s make the Step 1 diagram much more concrete and visually intuitive, closely mapping the journey – from scanning the QR code to what the verifier sees, with clear actions and outcomes. I will emphasize the actual actors, key checks, what is shown on screen, and what triggers the next step.

---

```
┌─────────────────────────────────────────────────────────────────────────────┐
| Diagram Title: Step 1 – QR Code Based Initial Verification                  |
| Purpose: Clearly illustrates how a verifier uses the QR code to confirm     |
| certificate existence, what information is immediately visible, and how     |
| candidate consent is requested for further verification.                    |
|                                                                            |
| [Diagram Visualization:]                                                    |
|                                                                            |
| [1] Verifier                                                    ┌────────┐ |
|     │                                                           │Candidate│ |
|     ▼                                                           └────────┘ |
| Scans QR code on                                                 ▲         |
| certificate PDF/print                                            │         |
|     │                                                            │         |
|     ▼                                                            │         |
| ┌───────────────┐                                                │         |
| |Certcheck      |                                                │         |
| |Platform       |------------- Checks QR code validity -----------┘         |
| └───────────────┘               (digital signature, expiry)                |
|     │                                                                  |
|     ├── Checks Blockchain: Does Certificate ID exist & is not revoked?  |
|     │                                                                  |
|     ▼                                                                  |
| ┌────────────────────────────────────────────────────────────────────┐  |
| | Certcheck returns to Verifier UI:                                  |  |
| | - "QR Code Valid / Certificate Found"                              |  |
| | - Obfuscated details:                                              |  |
| |     • Masked candidate name (e.g. "A*** S***")                     |  |
| |     • Issuer name (e.g. "ABC University")                          |  |
| |     • Partial Certificate ID, Blockchain TxID, and Timestamp       |  |
| | “Sensitive details hidden. To view, request candidate consent.”    |  |
| | [Button: Request Candidate Consent]                                |  |
| └────────────────────────────────────────────────────────────────────┘  |
|    │                                                                   |
|    └─► If verifier clicks consent button, system prompts candidate     |
|         via DigiLocker or notification (starts Step 2).                |
|                                                                         |
| Key Elements:                                                          |
| - QR Code Scan: Launches quick, anonymous certificate check.           |
| - Certcheck: Only shows non-sensitive proof-of-existence.              |
| - Blockchain: Proof anchor, not raw data.                              |
| - Consent Button: No detailed info without candidate’s digital consent.|
|                                                                         |
| Relationships:                                                         |
| - Verifier cannot see private fields before candidate agrees.           |
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Improvements:

- **Step-by-step visual breakdown:** The diagram walks through every user/system action.
- **Clear screen outcomes explained:** Explicitly notes what the verifier sees and what is withheld.
- **Obvious next steps:** Consent workflow is visually distinct; nothing moves forward without candidate’s say-so.
- **Privacy highlighted:** No detailed data leaks; candidate controls the rest of the process.

---

If this approach is clearer, I’ll proceed in the same way for Step 2: Full Data Verification. If you want any further refinements (such as an actual box-process flow, or more of a wireframe-style UX sketch), please let me know!