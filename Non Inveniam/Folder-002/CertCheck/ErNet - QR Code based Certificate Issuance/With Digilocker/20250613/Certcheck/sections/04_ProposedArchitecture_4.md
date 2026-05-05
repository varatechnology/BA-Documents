Thank you for confirming. Below is a **granular, step-by-step diagram** focused on the verification process initiated by a verifier (for example, scanning a QR code on a certificate). This sequence shows how Certcheck orchestrates live data retrieval, blockchain proof validation, DigiLocker ownership verification, and the return of a multi-proof result—all without storing raw credential data.

---

```
┌─────────────────────────────────────────────────────────────────────────────┐
| Diagram Title: Step-by-Step Verification Sequence via Certcheck              |
| Purpose: Illustrates how a verifier checks a certificate using QR code/API,  |
| and how Certcheck fetches data, validates proofs, aggregates responses, and  |
| returns results—without storing raw data.                                   |
|                                                                             |
|  [1]           [2]               [3]               [4]        [5]           |
| Verifier    Certcheck       Issuer Client       Blockchain  DigiLocker      |
|─────────────────────────────────────────────────────────────────────────────|
|1. Verifier scans      │                                                │   │
|   QR code or submits  │                                                │   │
|   verification req    │                                                │   │
|         │            ─┼─► 2. Certcheck receives request                │   │
|         │             │    (QR/API)                                    │   │
|         │             │                                                │   │
|         │            ─┼─► 3. Fetches live credential data   ───────────►   │
|         │             │   from Issuer Client (REST API)                │   │
|         │             │   (Issuer Client never sends data               │   │
|         │             │    outside this flow)                           │   │
|         │             │                                                │   │
|         │             │◄── 4. Receives credential artifact/metadata     │   │
|         │             │    (PDF/JSON/signatures)                        │   │
|         │             │                                                │   │
|         │            ─┼─► 5. Hashes credential and queries   ──────────►   │
|         │             │    Blockchain for matching proof                │   │
|         │             │                                                │   │
|         │             │◄── 6. Blockchain returns                        │   │
|         │             │    existence/integrity status                   │   │
|         │             │                                                │   │
|         │            ─┼─► 7. Queries DigiLocker for                     │   │
|         │             │   proof of user ownership                       │   │
|         │             │                                                │   │
|         │             │◄── 8. Ownership confirmation/status             │   │
|         │             │                                                │   │
|         │            ─┼─► 9. Aggregates all three proofs                │   │
|         │             │    (existence, integrity, ownership)            │   │
|         │             │                                                │   │
|         │◄────────────┼─10. Returns final verification result           │   │
|         │             │    (multilayered, tamper-proof, instant)        │   │
|                                                                             |
|Key Elements:                                                                |
|- Verifier: Employer, government, third party.                               |
|- Certcheck: Stateless orchestrator and proof engine.                        |
|- Issuer Client: Authoritative API at the issuing organization.              |
|- Blockchain: Decentralized store for existence/integrity proof.             |
|- DigiLocker: Government system for user ownership verification.              |
|                                                                             |
|Relationships/Flows:                                                         |
|- Certcheck never retains raw data—each request fetches, verifies, and       |
|  discards sensitive information outside of on-chain cryptographic proofs.   |
|- Each proof source (Issuer Client, Blockchain, DigiLocker) contributes      |
|  independently, providing confidence and auditability.                      |
|- Result to verifier includes structured proof and (optionally) links         |
|  to raw artifacts stored at source and/or references to immutable records.   |
└─────────────────────────────────────────────────────────────────────────────┘
```

---

**Explanation of Steps:**

1. **Verifier** initiates a verification (via QR scan, web/API).
2. **Certcheck** receives the request.
3. It **fetches credential data live** from the Issuer Client (never stores this).
4. Issuer Client responds with the signed artifacts/metadata.
5. Certcheck hashes these and **queries Blockchain** for an on-chain match (existence/integrity).
6. Blockchain responds with match/no match.
7. Certcheck **queries DigiLocker** for proof of candidate ownership.
8. DigiLocker confirms or denies ownership proof.
9. Certcheck **aggregates all proofs** into a single structured result.
10. **Verifier receives the multilayered verification result** with audit trail and complete trust evidence.

---

**This diagram clarifies the real-time, stateless, and multi-proof workflow with clear separation of duties for each system.**

Would you like the same “step-by-step” treatment for the issuance process, or do you want to move to more technical aspects (e.g., security architecture, scalability, or error handling in verification)?