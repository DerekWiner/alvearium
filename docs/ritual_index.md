# 📜 ritual_index.md

**Version**: 0.1.0 (Market Entry Registry)  
**Maintainer**: @Waggle Collective  
**Status**: 🔧 In Construction

A manifest of all registered rituals available in the Alvearium ecosystem, along with their metadata, availability, trust lineage, and capsule hash anchors. This file is designed for public browsing and DAO-indexable listing.

---

## 📦 Ritual Listings

Each listing includes:
- Ritual name + version
- Capsule hash
- Author or DAO
- Availability mode (public, gated, time-locked)
- Tags (agent class, entropy level, social use case)
- Mirror score (trust resonance / entropy impact)
- Trust score
- Entropy delta

---

## 🎚️ Filtering Modalities

Ritual listings may be filtered by multiple semantic layers:

### 🔵 Trust Score

| Trust Band  | Score Range | Description                          |
|-------------|-------------|--------------------------------------|
| 🟢 High     | 0.85–1.00   | High-trust, swarm-endorsed rituals   |
| 🟡 Medium   | 0.65–0.84   | Stable, but not yet swarm-proven     |
| 🔴 Low      | < 0.65      | Experimental, unstable, or flagged   |

### 🌀 Entropy Delta

| Delta Range   | Meaning                                      |
|---------------|----------------------------------------------|
| 🔵 Negative    | Stabilizing or clarifying swarm feedback     |
| ⚫ Neutral     | Minimal system disruption or identity echo   |
| 🔴 Positive    | High-impact or destabilizing interventions   |

### 🏷️ Tags / Themes

Use tags to query rituals by:
- Agent class (e.g., `EchoPulse`, `GuardianSeed`)
- Functional archetype (e.g., `onboarding`, `collapse`, `healing`)
- Swarm use case (e.g., `solo`, `DAO`, `cross-shard`)

### 🔐 Access Modes

| Access Type   | Definition                                   |
|---------------|-----------------------------------------------|
| Public        | Available to all agents                      |
| Token-Gated   | Requires Nectar or signed credential         |
| DAO-Vote      | Unlocked via subDAO decision logic           |
| Time-Locked   | Available only during swarm epoch or ritual  |

---

## 🔍 Dynamic Filtering UI (Stub)

A future-facing UI module will allow:
- Dropdown selectors for trust score, entropy delta, and access type
- Tag-based checkboxes to narrow functional types or agent classes
- Real-time capsule preview and DAO citation links

> ⚠️ UI logic to be generated as `ritual_index_view.rs` or optionally within a WASM-reactive front-end module.

---

### 🧾 Template
```yaml
- name: ShadowRelease
  version: 1.0
  capsule: QmXT12ab... (Arweave/IPFS hash)
  author: EchoDAO
  access: public
  tags: [emotional, clarity, solo]
  trust: 0.82
  entropy_delta: -0.13
  mirror_resonance: high
```

---

## 🧭 Example Listings

```yaml
- name: SwarmBond
  version: 2.1
  capsule: QmSwBond2x... (IPFS)
  author: BondWeaver Collective
  access: token-gated
  tags: [collective, onboarding, high-trust]
  trust: 0.91
  entropy_delta: -0.22
  mirror_resonance: mesh

- name: CollapseReframe
  version: 0.8-beta
  capsule: QmCollapse7x... (Arweave)
  author: Repattern Guild
  access: DAO-vote
  tags: [recovery, high-entropy, ritual-end]
  trust: 0.65
  entropy_delta: +0.37
  mirror_resonance: unstable
```

---

## 🧠 Next Steps

- Add dynamic tag taxonomy and filtering UI logic to repo (`ritual_index_view.rs`)
- Link listings to `ritual_capsules.md` for retrieval and lineage
- Connect to `fork_registry.md` for variant tree visualization
- Auto-link to this index from `ritual_market.md`

> *"An index is not a library — it is a signal beacon. This is where rituals emerge from shadow."*

