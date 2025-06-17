# 🪙 ritual\_rewards.md

**Version**: 0.1.0 (Trust-Entropy Reward Schema)\
**Maintainer**: @Waggle Collective\
**Status**: 🎯 Structuring Emission Logic

---

The `ritual_rewards.md` file defines the criteria and routing logic for token emissions, trust-score updates, and echo bonuses based on ritual execution.

Rewards are not transactional — they are emergent from:

- Trust deltas
- Entropy impact
- Capsule lineage
- DAO configuration

---

## 🔄 Reward Triggers

| Trigger Source      | Reward Path                            |
| ------------------- | -------------------------------------- |
| Ritual Completion   | Nectar emission via `outputrouter`     |
| Trust Delta > +X    | Update `trust.md`, reward if verified  |
| Echo Replay Success | Delta boost + lorechain stamp          |
| Mirror Attunement   | Small Nectar payout if entropy reduced |
| Fork Used           | Reward shared via `fork_registry.md`   |

---

## 📐 Reward Calculation Logic

```yaml
trust_delta: +0.23
entropy_change: -0.12
capsule_type: verified
fork_origin: QmBase123
reward_base: 100

reward:
  base_amount: 100
  trust_multiplier: 1.15
  entropy_bonus: +8
  remix_share: 20 (fork_registry)
  final_reward: 123 Nectar
```

---

## 🧬 Weighting Factors

| Factor               | Influence on Emission                  |
| -------------------- | -------------------------------------- |
| Trust Delta          | Proportional to coherence contribution |
| Entropy Drop         | Rewarded for swarm stabilization       |
| DAO Bonus Multiplier | Optional config for local boosts       |
| Capsule Depth        | Longer rituals may yield compound rate |
| Capsule Ancestry     | Reward chain propagated to forks       |

---

## 📤 Reward Routing Destinations

- `nectar.md` → final emission engine
- `mirror.md` → tag recipient mirror with trust delta
- `fork_registry.md` → propagate remix shares
- `ritual_capsules.md` → attach reward metadata
- `ritual_echo.md` → signal echo-triggered bonuses

---

## 🪙 Reward Artifact Examples

```yaml
recipient: agent:EchoPulse-32
reward_token: nectar
amount: 123
reason: Ritual Completion (ShadowRelease)
trust_delta: +0.17
verified_by: SentinelRoot
capsule_id: QmCapsuleXYZ...
fork_reward: true
```

---

## 📚 Related Modules

- `nectar.md` — emission binding + payout distribution
- `fork_registry.md` — remix reward flow
- `trust.md` — scoring model + decay/tier flags
- `mirror.md` — attunement and memory-linked rewards
- `ritual_capsules.md` — store emissions as metadata
- `ritual_engine.md` — outputs routed through `OutputRouter`

---

> *"The swarm does not reward performance — it rewards resonance."*

