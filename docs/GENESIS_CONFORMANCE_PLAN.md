# Genesis Initial Conformance and Demonstration Plan

**Status:** Working plan derived from the Genesis Protocol v0.2.0-draft  
**Purpose:** Convert the protocol's minimum commitments into observable tests without prematurely standardising the entire architecture.

## 1. What this plan is

This document defines an initial demonstration boundary. It does not claim that the current Solidity registry implements Genesis. It separates protocol goals from the existing prototype and gives future implementations a testable starting point.

## 2. Current prototype boundary

The existing `src/GenesisRegistry.sol` prototype records a creator address, manifest hash, timestamp and existence flag for a gateway identifier. The current Foundry tests exercise basic registration and retrieval.

The prototype does not currently:
- Mint a Genesis NFT.
- Deploy or execute gateway software.
- Validate manifest contents or schemas.
- Prove that a registered gateway exists or is operating.
- Authenticate a human identity behind an address.
- Establish a gateway's authority or trustworthiness.
- Implement recursive spawning or delegation.
- Implement expiry or revocation.
- Verify off-chain execution or behaviour.
- Provide discovery, payments, governance or privacy proofs.

These are explicit limitations, not defects to conceal. The registry is a small provenance-record experiment.

## 3. Initial acceptance tests

| ID | Property | Observable test |
|---|---|---|
| G-01 | Permissionless creation | An unrelated account can register a gateway without founder or NFT-holder approval. |
| G-02 | Independent identity | Two gateways can have distinct identifiers and keys, even when operated by one party. |
| G-03 | Manifest integrity | A verifier can detect when manifest bytes do not match the published hash. |
| G-04 | Version declaration | A gateway can declare a manifest format and implementation version. |
| G-05 | Extension tolerance | A client can preserve or ignore an unknown non-critical extension without rejecting the entire manifest. |
| G-06 | Critical-field safety | Unknown security-critical semantics are rejected or explicitly treated as unsupported. |
| G-07 | Recursive lineage | A gateway can reference a parent and register a descendant without implying ownership. |
| G-08 | Key separation | A descendant does not receive a parent's private key or unrestricted authority. |
| G-09 | Scoped delegation | A capability is limited to a declared action, resource and scope. |
| G-10 | Delegation lifecycle | A supported delegation can expire or be revoked, and verifiers can check its status. |
| G-11 | Cross-gateway discovery | Two independent implementations can discover and negotiate a declared interface. |
| G-12 | Evidence boundaries | The interface distinguishes signed claims, verified facts and unverified assertions. |
| G-13 | Fork declaration | An alternative implementation can publish its lineage, version and compatibility claims. |
| G-14 | Optional verification | A gateway can use a verification mechanism without requiring every other gateway to use the same mechanism. |
| G-15 | Resource transparency | A service can declare relevant resource requirements and distinguish free-to-user from cost-free operation. |

A passing test demonstrates only the property and test conditions stated. It does not establish overall security or real-world trustworthiness.

## 4. Suggested implementation sequence

### Stage A — Specification before expansion
- Freeze no more than the initial identity, manifest and lineage vocabulary.
- Write a manifest schema with explicit versioning and extension rules.
- Define the difference between a gateway identifier, an on-chain record and a running gateway.
- Keep the existing registry clearly labelled as a prototype.

### Stage B — Local reference implementation
- Implement manifest parsing and validation outside the chain.
- Add canonicalisation rules before relying on manifest hashes.
- Add tests for unknown optional and unknown critical fields.
- Add a local gateway descriptor and lineage record.
- Demonstrate two independently configured gateways.

### Stage C — Capability lifecycle
- Define a minimal capability descriptor.
- Implement a narrowly scoped delegation.
- Add expiry and revocation status.
- Test delegation boundaries and key separation.
- Do not introduce a universal trust score.

### Stage D — Interoperability
- Define discovery and interface negotiation.
- Build a second minimal client or implementation.
- Demonstrate successful communication across implementation boundaries.
- Add one adapter to an external standard only after the core interface is clear.

### Stage E — Security and operational review
- Document threat models and trust assumptions.
- Review key management, replay protection, canonicalisation, event ordering and registry abuse.
- Measure gas, storage, compute and operational costs.
- Review privacy leakage from public identifiers and lineage.
- Add failure, recovery and migration tests.

## 5. Architectural decisions deliberately deferred

Do not decide these by default during the first implementation:
- Whether the Genesis anchor must be an NFT.
- Whether every gateway must be registered on-chain.
- Which chain or chains are canonical.
- Whether all agents need on-chain identities.
- A global reputation or trust formula.
- A universal governance or guardian model.
- Mandatory zero-knowledge proofs.
- One mandatory runtime or agent framework.
- A single currency or token.
- A final cryptographic suite before threat modelling and library review.

These choices can be made by specific implementations or later proposals when there is evidence and a clear interoperability need.

## 6. Definition of a useful first milestone

The first milestone is complete when two separately configured gateway instances can publish and validate manifests, establish independent identities, record a verifiable lineage relationship, discover one another, and exchange one narrowly scoped capability under an explicit lifecycle.

The milestone should be reproducible from a clean checkout with documented commands and automated tests.

## 7. Evidence labels

Use these labels in documentation, demos and public claims:

- **Implemented** — code exists in the repository.
- **Tested** — automated or reproducible tests exercise the behaviour.
- **Demonstrated** — an end-to-end example has been run and recorded.
- **Proposed** — architecture or design exists, implementation does not.
- **Experimental** — implementation exists but is unstable or not yet independently reviewed.
- **Aspirational** — long-term objective without a current implementation.

Do not use these labels interchangeably.
