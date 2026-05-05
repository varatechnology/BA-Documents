Thank you for the additional details about the Issuer Client and Certcheck platform architecture. To proceed, I’ll outline a clear summary incorporating these points and then propose a detailed architecture and workflow explanation to clarify the roles and data flows.

---

### Summary of Certcheck Platform Components & Roles:

- **Issuer Client**  
  - Web-based REST API hosted on the issuing institute’s side.  
  - Acts as the authoritative access point for certificate data during verification requests.  
  - Ensures data privacy since no raw data is stored on Certcheck.

- **Certcheck Platform**  
  - Serves as an orchestrator and facilitator without storing any certificate data.  
  - Performs live fetching of certificate information from Issuer Clients on demand.  
  - Leverages both Blockchain and DigiLocker ecosystems to provide layered proofs during verification.

- **Proofs Generated during Verification:**  
  1. **Proof of Existence:** Confirms the certificate exists in the issuing institute’s system and is recorded on blockchain.  
  2. **Proof of Data Integrity:** Validates that the certificate’s data has not been altered since issuance by comparing with blockchain hash.  
  3. **Proof of Ownership:** Confirms the claimant’s possession of the document, supported by DigiLocker’s ownership verification.

---

### Proposed Architecture & Workflow Explanation:

1. **Issuing Institute** runs the **Issuer Client** which exposes REST APIs for certificate verification requests.  
2. A verifier initiates a document verification via **Certcheck**, which:  
   - Calls the Issuer Client API to fetch data dynamically for requested credentials.  
   - Queries blockchain for corresponding certificate hashes to validate integrity and existence.  
   - Interfaces with DigiLocker to confirm the user’s proof of ownership for the credential.  
3. Certcheck combines these inputs to deliver a **trusted verification response** containing the three key proofs without storing sensitive data internally.  
4. This orchestration ensures minimal data exposure while maximizing trust via multi-source confirmation.

---

Would you like me to create a detailed integration architecture diagram illustrating these components, data flows, and proof verifications? This would help visualize how Certcheck interacts with issuing institutes, blockchain, and DigiLocker to produce trusted verification outcomes.