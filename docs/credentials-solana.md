# Solana NFT as credential (v0)

Not a collectible drop. The mint address (or metadata URI hash) is an **allowlisted identity**.

1. You mint (or already hold) one NFT.
2. Put `solana:nft:<MINT>` in `code/spawn/pins.json` under `credentials`.
3. OpenClaw / spawn.py `--identity solana:nft:<MINT>`.
4. Changing the mint means a git pin change — same as any other identity.

The chain does not run the sandbox. It only names who may start one.
Do not give agents the mint authority or update-authority.
