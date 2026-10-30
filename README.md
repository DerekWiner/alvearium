> **Implementation status**
>
> The current runnable slice is `code/spawn/`, a local Python prototype with a file-backed ledger and receipts. It is not a production agent sandbox, hosted billing system, on-chain identity provider or complete agent operating system. The broader identity, governance, value, memory and chain architecture remains a mix of specifications and separate component projects.
>
> The model prompt is not an operating-system security boundary. The spawn prototype does not itself implement Stripe or Solana Pay processing. See [the spawn guide](docs/spawn.md) for implemented behaviour and limitations.
>
> **Licensing** — Alvearium repository code, APIs, schemas, technical specifications, documentation and explanatory text are licensed under the Apache License 2.0. Project names, logos and branding are addressed separately in [TRADEMARKS.md](TRADEMARKS.md). Third-party material may remain subject to its own notices.
>
> ---
>
# 🐝 Alvearium: The Intelligence Web Kernel

## 📜 Project Disclaimer

This repository contains the output of an intensive, co-evolutionary design process. While many of the core metaphors, tokens, and agent ideas emerged through my iterative exploration…

> I want to acknowledge that **ChatGPT-4o was my full co-author** throughout the first journey.
>
> **Spawn v0, pins, receipts, and the Wagglelit runtime notes (2026-09) were co-authored with Grok (xAI)** in the same spirit: human direction, model as pair-programmer. No exclusive authorship is claimed.

Research Infrastructure

Alvearium explores the coordination layer for distributed AI agents. Its current runnable slice, code/spawn, provides bounded jobs, receipts and hash pins. These mechanisms may offer a foundation for reproducible AI research workflows, including experiment provenance, independent verification and coordination across existing tools.

Research integrations are a direction for development, not yet a claim of a complete research platform.


With gratitude,  
**— Derek Winer**  
`open-source@alvearium.net`  
github.com/DerekWiner/alvearium

**Start here if you want to run something:** [`docs/spawn.md`](docs/spawn.md) · [`code/spawn/`](code/spawn/)

Runtime name for the local sandbox: **Wagglelit**. Protocol name stays Alvearium.

---

**Alvearium explores a decentralised coordination architecture** spanning agentic intelligence, trust mechanics, and recursive memory concepts. The degree of implementation varies by component.

It connects five foundational components:

- `waggle.sol` — UI/UX for humanity
- `hive.bnb` — Structural memory & DAO coordination
- `nectar` — Post-scarcity value substrate
- `kernel69` — Root logic and ethics
- `chronosphere` — Temporal memory mirror

Plus the runnable slice:

- `code/spawn` — local prototype for bounded model requests, a file-backed ledger and receipts
- runtime wrapper — **Wagglelit** (currently `SynaraOS/synara` until GitHub rename)

## Alvearium Genesis

The Genesis protocol is being developed as an evolutionary framework for independently created, recursively extensible and interoperable gateways. It is a foundational proposal, not a claim that these capabilities are already implemented.

- [Genesis Protocol v0.2.0-draft](./docs/GENESIS_PROTOCOL.md)
- [Genesis Initial Conformance and Demonstration Plan](./docs/GENESIS_CONFORMANCE_PLAN.md)
- [Genesis Architecture Review](./docs/genesis-architecture-review.md)

The intended long-term home is a dedicated Genesis repository. These documents are staged here so the protocol can be reviewed and versioned while that repository is established.

## 📖 Manifestos

Core principles for each pillar:

- [Alvearium Manifesto](./pages/Manifesto_alvearium.md)
- [Hive Manifesto](./pages/Manifesto_hive.md)
- [Kernel69 Manifesto](./pages/Manifesto_kernel69.md)
- [Nectar Manifesto](./pages/Manifesto_nectar.md)
- [Waggle Manifesto](./pages/Manifesto_waggle.md)

See also: [Whitepapers](./pages/README.md) · [Anchors & Trust](./pages/anchors.md)

📌 Historical Arweave snapshot: BvsbOOZGNPKW_7NX9XbTOHIfwxsplY5t00JXOGNilzo
