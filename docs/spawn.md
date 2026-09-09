# Alvearium Spawn (v0)

Working entry point. Not a token launch.

A **spawn** is a bounded agent habitat: intent + budget + tools + expiry.
Clone stays free. Execution is metered.

Runtime name: **Wagglelit** (repo still `SynaraOS/synara` until renamed).

Co-authors: Derek Winer + Grok (xAI), 2026-09. Same co-creation pattern as the GPT-4o Alvearium pass.

## One-time sign-on

Identity is created **once** per subject:

| Subject | How |
|---|---|
| Human | GitHub login, wallet signature, or Solana NFT mint hash listed in `pins.json` |
| Agent | Parent receipt + its own pubkey |

Sign-on writes a local ledger row. It does **not** charge. Charge happens on **spawn**.

Free tier is **two spawns per identity**.

## Credits

| Event | Cost |
|---|---|
| Sign-on | $0 |
| Spawn 1–2 | 0 credits |
| Spawn 3–102 | 1 credit each |
| Failed / denied | 0 |

Hosted operators sell credit packs (Stripe or Solana Pay). Self-host sets credits locally.

## Intent / receipt

See `code/spawn/spawn.py`. Receipts land in `.alvearium/sandbox/<id>/receipt.json`.

## Agent front door

`docs/spawn.agent.json`
