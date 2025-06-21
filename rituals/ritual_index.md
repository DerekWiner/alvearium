# 📜 ritual\_index.md

**Version**: 0.1.0 (Market Entry Registry)\
**Maintainer**: @Waggle Collective\
**Status**: ✅ Ready for Market Integration

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

| Trust Band | Score Range | Description                        |
| ---------- | ----------- | ---------------------------------- |
| 🟢 High    | 0.85–1.00   | High-trust, swarm-endorsed rituals |
| 🟡 Medium  | 0.65–0.84   | Stable, but not yet swarm-proven   |
| 🔴 Low     | < 0.65      | Experimental, unstable, or flagged |

### 🌀 Entropy Delta

| Delta Range | Meaning                                    |
| ----------- | ------------------------------------------ |
| 🔵 Negative | Stabilizing or clarifying swarm feedback   |
| ⚫ Neutral   | Minimal system disruption or identity echo |
| 🔴 Positive | High-impact or destabilizing interventions |

### 🏷️ Tags / Themes

Use tags to query rituals by:

- Agent class (e.g., `EchoPulse`, `GuardianSeed`)
- Functional archetype (e.g., `onboarding`, `collapse`, `healing`)
- Swarm use case (e.g., `solo`, `DAO`, `cross-shard`)

### 🔐 Access Modes

| Access Type | Definition                                  |
| ----------- | ------------------------------------------- |
| Public      | Available to all agents                     |
| Token-Gated | Requires Nectar or signed credential        |
| DAO-Vote    | Unlocked via subDAO decision logic          |
| Time-Locked | Available only during swarm epoch or ritual |

---

## 🔍 Dynamic Filtering UI

Implemented in coordination with `market_access.md` and `mirror_review.md`, the filtering logic now supports:

- Dropdown selectors for trust score, entropy delta, and access type
- Tag-based checkboxes to narrow functional types or agent classes
- Review-tier filtering based on mirror review metadata
- Real-time capsule preview and DAO citation links

> 🎛️ Powered by `ritual_index_view.rs` or optional WASM-reactive front-end modules.

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

- Refine and expose `ritual_index_view.rs` via UI route
- Auto-integrate new rituals from `ritual_capsules.md`
- Dynamically display trust deltas and echo trails via `mirror_review.md`
- Expand variant/fork display through `fork_registry.md`

---

> *"An index is not a library — it is a signal beacon. This is where rituals emerge from shadow."*


---
📌 Arweave Hash: UXYdVcmiXOg0mNk6RP-6eOSIefT5GX_1_yRago7dQoU
