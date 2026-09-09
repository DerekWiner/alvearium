# code/spawn

```bash
python3 code/spawn/spawn.py sign-on --identity solana:nft:YOURMINT
python3 code/spawn/spawn.py spawn --identity solana:nft:YOURMINT --intent "List three peaceful sandbox uses."
python3 code/spawn/mount_genesis.py code/spawn/genesis.example.json
```

OpenClaw / OpenRouter Qwen:

```bash
export OPENAI_BASE_URL=https://openrouter.ai/api/v1
export OPENAI_API_KEY=sk-or-...
export OPENAI_MODEL=qwen/qwen3.5-9b
```

Copy `pins.json` into the OpenClaw workspace. Do not give the agent Arweave write or mint authority.
