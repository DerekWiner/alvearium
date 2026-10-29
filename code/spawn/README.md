# Spawn prototype

This directory contains a local Python prototype for recording and running a bounded model request.

## Local dry run

```bash
python3 code/spawn/spawn.py sign-on --identity local:dev
python3 code/spawn/spawn.py spawn --identity local:dev --intent "List three peaceful sandbox uses."
python3 code/spawn/spawn.py status
```

Without both `OPENAI_BASE_URL` and `OPENAI_API_KEY`, the runner returns a dry-run response instead of calling a model.

## Optional endpoint configuration

Set these environment variables in your shell or a local, Git-ignored environment file.

```bash
export OPENAI_BASE_URL="https://openrouter.ai/api/v1"
export OPENAI_API_KEY="YOUR_API_KEY"
export OPENAI_MODEL="qwen/qwen3.5-9b"
```

These are example values. Confirm that the provider supports the configured API format and model name. Never commit a real API key.

## Local data

By default, ledger and receipt files are written under `.alvearium/`. Set `ALVEARIUM_HOME` to choose another directory.

## Security notes

- Treat intent strings and model outputs as untrusted.
- Do not provide wallet signing, minting or Arweave write authority to this prototype.
- A model prompt saying “no network” does not prevent network access at the operating-system level.
- Do not execute generated code without a separately configured sandbox.
- `pins.json` contains configuration placeholders. Replace them only with verified values and document their source.

For implementation limits and the receipt format, see [the spawn guide](../../docs/spawn.md).
