Here’s a more detailed **Sequence Workflow Diagram** illustrating the step-by-step interactions among Verifier, Certcheck Platform, Issuer Client, Blockchain, and DigiLocker during certificate verification. This will clarify the timing and flow of data and proof collection:

```
┌────────────────────────────────────────────────────────────────────────────┐
| Diagram Title: Certificate Verification Sequence Workflow via Certcheck     |
| Purpose: Visualizes the chronological steps taken by Certcheck to retrieve  |
| and validate certificate data from issuing institutes, blockchain, and      |
| DigiLocker, producing trusted multi-proof verification output.              |
|                                                                            |
| Key Entities:                                                              |
| - Verifier: Initiates verification request.                              |
| - Certcheck: Orchestrator of data fetch and proof aggregation.          |
| - Issuer Client: Provides authoritative certificate data on demand.     |
| - Blockchain: Immutable ledger for existence and integrity proofs.      |
| - DigiLocker: Proof of certificate ownership repository.                 |
|                                                                            |
|                                                                               |
| Step 1: Verifier → Certcheck                   : Requests verification          |
| Step 2: Certcheck → Issuer Client               : Fetch certificate data         |
| Step 3: Issuer Client → Certcheck               : Sends live certificate data    |
| Step 4: Certcheck → Blockchain                   : Validates certificate hash     |
| Step 5: Blockchain → Certcheck                   : Confirms data integrity & existence |
| Step 6: Certcheck → DigiLocker                   : Checks user proof-of-ownership |
| Step 7: DigiLocker → Certcheck                   : Returns ownership status        |
| Step 8: Certcheck → Verifier                      : Returns combined proof results  |
|                                                                            |
┌────────────┐        ┌──────────────┐       ┌─────────────┐       ┌────────────┐
│ Verifier   │        │ Certcheck    │       │ Issuer      │       │ Blockchain │
│            │        │ Platform     │       │ Client      │       │            │
│            │        │              │       │             │       │            │
│  1:Request ├───────►│              │       │             │       │            │
│            │        │ 2: Fetch data├──────►│             │       │            │
│            │        │              │       │  3: Data    │       │            │
│            │        │              │◄──────┤             │       │            │
│            │        │ 4: Verify hash│──────►│             │       │            │
│            │        │              │       │             │       │  5: Confirm│
│            │        │              │◄──────┤             │       │ integrity  │
└────────────┘        │              │       │             │       │            │
                      │ 6: Check own.│──────►│             │       │            │
                      │              │       │             │       │            │
                      │              │◄──────┤             │       │            │
                      │ 8: Return    │       │             │       │            │
                      │ results      │──────►│             │       │            │
                      └──────────────┘       └─────────────┘       └────────────┘
                          ▲
                          │
                      ┌──────────┐
                      │ DigiLocker│
                      │ 7: Return │
                      │ ownership │
                      │ status    │
                      └──────────┘
└────────────────────────────────────────────────────────────────────────────┘
```

---

### Explanation of Workflow Steps:

1. **Verifier** submits a certificate verification request to Certcheck.  
2. **Certcheck** calls the Issuer Client API hosted by the issuing institute to fetch live certificate data.  
3. **Issuer Client** responds with the authoritative certificate data without Certcheck storing it.  
4. Certcheck queries the **Blockchain** to validate the certificate’s hash, confirming data integrity.  
5. **Blockchain** returns confirmation of certificate existence and immutability status.  
6. Certcheck queries **DigiLocker** to verify the claimant’s proof of ownership of the certificate.  
7. DigiLocker responds with the ownership verification result.  
8. Certcheck aggregates all inputs and returns a consolidated verification report to the Verifier.

---

Please let me know if you want me to create additional diagrams such as a stakeholder map or focus next on security, scalability, or user experience considerations.