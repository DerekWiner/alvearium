#!/usr/bin/env python3
"""Alvearium spawn v0 — local sandbox runner."""
from __future__ import annotations

import hashlib
import json
import os
import time
import uuid
from pathlib import Path

ROOT = Path(os.environ.get("ALVEARIUM_HOME", ".alvearium"))
LEDGER = ROOT / "ledger.json"
SANDBOX = ROOT / "sandbox"
FREE_SPAWNS = 2


def load() -> dict:
    ROOT.mkdir(parents=True, exist_ok=True)
    SANDBOX.mkdir(parents=True, exist_ok=True)
    if LEDGER.exists():
        return json.loads(LEDGER.read_text())
    data = {"identities": {}}
    LEDGER.write_text(json.dumps(data, indent=2))
    return data


def save(data: dict) -> None:
    LEDGER.write_text(json.dumps(data, indent=2))


def sign_on(identity: str) -> dict:
    data = load()
    if identity not in data["identities"]:
        data["identities"][identity] = {
            "created": int(time.time()),
            "free_remaining": FREE_SPAWNS,
            "credits": 0,
            "spawns": 0,
        }
        save(data)
        return {"status": "created", "identity": identity, "charged": 0}
    return {"status": "exists", "identity": identity, "charged": 0}


def take_budget(row: dict):
    if row["free_remaining"] > 0:
        row["free_remaining"] -= 1
        return True, "free", 0
    if row["credits"] >= 1:
        row["credits"] -= 1
        return True, "credit", 1
    return False, "need_credit", 0


def call_model(intent: str, budget_tokens: int) -> str:
    base = os.environ.get("OPENAI_BASE_URL")
    key = os.environ.get("OPENAI_API_KEY")
    if not base or not key:
        return f"[dry-run] would ask model: {intent[:200]}"
    try:
        import urllib.request

        body = json.dumps(
            {
                "model": os.environ.get("OPENAI_MODEL", "qwen"),
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a sandboxed Alvearium spawn. No network, no spend.",
                    },
                    {"role": "user", "content": intent},
                ],
                "max_tokens": min(budget_tokens, 512),
            }
        ).encode()
        req = urllib.request.Request(
            base.rstrip("/") + "/chat/completions",
            data=body,
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
            },
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read().decode())
        return payload["choices"][0]["message"]["content"]
    except Exception as exc:
        return f"[model-error] {exc}"


def spawn(identity: str, intent: str) -> dict:
    data = load()
    if identity not in data["identities"]:
        return {"status": "denied", "reason": "sign-on first"}
    row = data["identities"][identity]
    ok, lane, spent = take_budget(row)
    if not ok:
        return {
            "status": "need_credit",
            "http": 402,
            "hint": "python3 code/spawn/spawn.py credit --identity ... --n 100",
        }
    spawn_id = "sp_" + uuid.uuid4().hex[:12]
    box = SANDBOX / spawn_id
    box.mkdir()
    intent_hash = "sha256:" + hashlib.sha256(intent.encode()).hexdigest()
    t0 = time.time()
    output = call_model(intent, 512)
    seconds = round(time.time() - t0, 3)
    receipt = {
        "spawn_id": spawn_id,
        "intent": intent,
        "intent_hash": intent_hash,
        "identity": identity,
        "lane": lane,
        "credits_spent": spent,
        "seconds": seconds,
        "status": "ok",
        "output": output,
    }
    (box / "receipt.json").write_text(json.dumps(receipt, indent=2))
    (box / "output.txt").write_text(output)
    row["spawns"] += 1
    save(data)
    return receipt


def main() -> None:
    import argparse

    p = argparse.ArgumentParser(description="Alvearium spawn v0")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("sign-on")
    a.add_argument("--identity", required=True)
    b = sub.add_parser("spawn")
    b.add_argument("--identity", default="local:dev")
    b.add_argument("--intent", required=True)
    c = sub.add_parser("credit")
    c.add_argument("--identity", required=True)
    c.add_argument("--n", type=int, default=100)
    sub.add_parser("status")
    args = p.parse_args()
    if args.cmd == "sign-on":
        print(json.dumps(sign_on(args.identity), indent=2))
    elif args.cmd == "spawn":
        sign_on(args.identity)
        print(json.dumps(spawn(args.identity, args.intent), indent=2))
    elif args.cmd == "credit":
        sign_on(args.identity)
        data = load()
        data["identities"][args.identity]["credits"] += args.n
        save(data)
        print(json.dumps(data["identities"][args.identity], indent=2))
    else:
        print(json.dumps(load(), indent=2))


if __name__ == "__main__":
    main()
