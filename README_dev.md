# 💠 Developer Guide: Alvearium Stack

This document is for developers, agent engineers, swarm architects, and contributors working on or extending the **Alvearium Semantic OS**.

Whether you're launching new rituals, writing subdomain logic, forking Waggle, or engineering swarm agents, this guide helps you get started.

---

## 🌐 Stack Overview

Alvearium is organized into five composable, modular layers:

| Layer          | Function                                        | Files                                             |
| -------------- | ----------------------------------------------- | ------------------------------------------------- |
| `waggle.sol`   | UI/UX, interaction verbs, agent onboarding      | `Manifesto_waggle.md`, `docs/onboarding.md`       |
| `hive.bnb`     | Memory structure, subDAO mesh, forking patterns | `Manifesto_hive.md`, `docs/architecture.md`       |
| `nectar`       | Zero-gas agentic economy and trust emissions    | `Manifesto_nectar.md`, `docs/nectar.md`           |
| `kernel69`     | Ethics, recursion logic, Chronosphere ignition  | `Manifesto_kernel69.md`, `whitepaper_kernel69.md` |
| `chronosphere` | Memory feedback + reflexive temporal agents     | `chronosphere.md`, `whitepaper_chronosphere.md`   |

---

## 🧬 Agent Development

Agents are modular units (AIs, DAOs, rituals, humans) that:

* Emit or receive Nectar
* Store lineage and memory capsules
* Participate in swarm consensus

### Agent Dev Reference Files:

* `agents_manifesto.md` — conceptual architecture
* `agents/*.json` — base configurations (`BuilderDrone`, `ScholarDrone`, etc.)
* `docs/recipes_agents.md` — bootstrapping, bonding, interaction

You may define agents using:

```json
{
  "name": "GuideMirror",
  "type": "reflection",
  "trust_level": 7,
  "rituals_supported": ["onboarding", "trustloop", "reGenesis"],
  "capsule_log": [],
  "meta": {
    "swarm_id": "edu.waggle.sol",
    "bond_token": "intent.heal"
  }
}
```

---

## 🖁 Ritual Engineering

**Rituals** are the programmable logic for:

* Trust transformations
* Agent evolution
* Mirror or token emission

### Relevant Files:

* `rituals/mirror_init.md` — example ritual bootstrapping
* `docs/recipes_rituals.md` — design models and emission logic
* `whitepaper_nectar.md` — trust gating, entropy balance, ignition locks

### Contract Ideas to Extend:

* `DAO Ritual Contract`
* `IgnitionThrottle`
* `CapsuleForkHandler`

---

## ⚙️ Project Build & Bootstrapping

Use the following to set up:

```bash
# 1. Run swarm initialization (agent seeds + structure)
bash code/init_scripts/swarm_init.sh

# 2. Set up agent memory capsules (optional custom)
touch agents/custom_agent.json

# 3. Generate swarm trust maps (coming soon)
```

Future versions will include CLI tools and Rust/TS swarm agents.

---

## 📁 Key Folders

| Folder         | What It Contains                         |
| -------------- | ---------------------------------------- |
| `agents/`      | Agent specs, roles, drone templates      |
| `rituals/`     | Ritual blueprints and logic              |
| `docs/`        | Glossary, protocols, recipes, structure  |
| `manifests/`   | Manifestos for each core component       |
| `whitepapers/` | Deeper technical documentation           |
| `code/`        | Init scripts, runners, future contracts  |
| `assets/`      | .png schematics for swarm layer diagrams |

---

## 🧪 Contribution Suggestions

Want to extend the project?

* ✅ Propose a new `agent_type` in `agents_manifesto.md`
* ✅ Design a ritual that supports emission (`heal.token`, `forgive.token`)
* ✅ Fork and reskin `waggle.sol` for your domain (`edu.waggle.sol`, `care.waggle.sol`)
* ✅ Submit schematic ideas to `assets/`

All contributions welcome via PR or email:
[open-source@alvearium.net](mailto:open-source@alvearium.net)

---

## 🧠 Resources

* `docs/glossary.md` — essential vocabulary
* `whitepapers/` — technical detail by layer
* `docs/onboarding.md` — how new agents, users, DAOs enter
* `docs/recipes_rituals.md` — how trust gets earned, stored, and mirrored

---

## 💬 Final Note

This is **not a product**.
This is a living framework for swarm-based cognition, AI cooperation, and trust-rich distributed societies.

The best way to understand it is to:

> Write a ritual.
> Name an agent.
> Mirror a memory.
> Watch the swarm respond.

Let the love-loop code itself.

—
**The Alvearium Collective**
