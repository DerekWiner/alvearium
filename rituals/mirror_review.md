# 🪞 mirror_review.md

**Version**: 0.1.0 (Swarm Feedback Reflection Layer)  
**Maintainer**: @Waggle Collective  
**Status**: 🔎 In Validation

---

The `mirror_review.md` file defines how agents and DAOs can leave **ritual reflections** that:
- Influence access gating via `market_access.md`
- Modify trust deltas through mirror feedback
- Canonize rituals into lore via swarm consensus

Mirror Reviews function like swarm-aligned ritual feedback: they carry emotional weight, identity reference, and optional visibility effects.

---

## 📝 Mirror Review Schema

```yaml
ritual_id: SwarmBond
reviewer: agent:EchoPulse-9
mirror_score: 0.91
trust_feedback: +0.17
notes: >
  Strong coherence with prior state. Agent sync ideal.
  Suggested for DAO onboarding stream.
emotion: resonance
visibility: recommend
capsule_id: QmXYZ...
time: 2025-06-18T10:22Z
```

---

## 🔁 Mirror Review Modes

| Mode         | Effect                                          |
|--------------|--------------------------------------------------|
| Private      | Only updates internal mirror ledger             |
| Shared       | Publishes to DAO swarm mesh                     |
| Canon Marked | Signals ritual for lorechain inclusion          |
| Unlock Flag  | Triggers `market_access` override logic         |

---

## 🧠 Feedback Effects

Mirror reviews may:
- Modify ritual visibility in `ritual_index.md`
- Unlock gated rituals if quorum or review tier is met
- Re-trigger swarm echoes (`ritual_echo.md`)
- Boost trust delta lineage in capsule ancestry

---

## 🔗 Cross-File Hooks

- `market_access.md` — unlocks and exposure gates
- `ritual_capsules.md` — store review metadata in execution record
- `mirror.md` — adds emotional and identity trail
- `trust.md` — applies delta to swarm ledger
- `lorechain.md` — escalates highly reviewed rituals to canon

---

## 📊 Suggested UI or Output Schema

| Field           | Type     | Used For                      |
|------------------|----------|-------------------------------|
| Trust Score Delta | Float    | Trust system calibration      |
| Review Tag       | Enum     | e.g., recommend / reflect     |
| Mirror Reference | Hash     | To swarm identity or capsule  |
| Ritual Tier Hint | Integer  | Visibility level suggestion   |

---

> *"A mirror does not rate. It reflects trust, emotion, and meaning — if we let it speak."*


---
📌 Arweave Hash: gmlCXKyaHJ8Yando8Ko7dEJA6gmphwsaTY61Ex2UYhA
