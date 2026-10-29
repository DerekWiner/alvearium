# Alvearium Spawn prototype

**Status, local prototype. Not a token launch or production agent sandbox.**

A spawn is currently a local record of a requested model task. The prototype accepts an identity string and an intent, tracks a simple local allowance, optionally calls a chat-completions endpoint, and writes a receipt.

## What is implemented

The current Python entry point is `code/spawn/spawn.py`.

- A JSON ledger is stored under `.alvearium/ledger.json` by default.
- The local ledger tracks identities, remaining free spawns, credits and spawn counts.
- The runner accepts an intent string.
- Without both `OPENAI_BASE_URL` and `OPENAI_API_KEY`, the model call returns a dry-run message.
- When configured, it sends a chat-completions request to the supplied endpoint.
- A receipt and output file are written under `.alvearium/sandbox/<spawn-id>/`.

Set `ALVEARIUM_HOME` to use a different data directory.

## What this script does not implement

The script does not itself provide authentication of a GitHub account, wallet or NFT; cryptographic proof that an identity string belongs to a person; secure operating-system sandboxing; a technical prohibition on network access; hosted account management; payment processing; on-chain receipt verification; or production concurrency control.

The model prompt is not a security boundary. Do not run untrusted generated code or expose credentials to a process that has not been isolated and reviewed.

## Local use

From the repository root:

```bash
python3 code/spawn/spawn.py sign-on --identity local:dev
python3 code/spawn/spawn.py spawn --identity local:dev --intent "Summarise the supplied task."
python3 code/spawn/spawn.py status
```

The prototype stores state locally. The `credit` command manually increments the local counter. This script does not integrate Stripe, Solana Pay or a hosted billing backend.

## Model endpoint configuration

Set `OPENAI_BASE_URL`, `OPENAI_API_KEY` and `OPENAI_MODEL` in the environment when using a compatible endpoint. Never commit real API keys. Use a Git-ignored local environment file or a suitable secret manager.

## Receipts

Receipts record the intent, a hash of the intent, identity string, lane, credit count, elapsed time, status and output. A receipt is useful for local inspection, but it is not a signed attestation and does not independently prove that a claimed action occurred.

## Related files

- `code/spawn/spawn.py`
- `code/spawn/README.md`
- `code/spawn/pins.json`
- `code/spawn/genesis.example.json`
