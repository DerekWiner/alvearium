#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

PINS = Path(__file__).with_name("pins.json")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def deny(reason: str) -> int:
    print(json.dumps({"status": "denied", "reason": reason}, indent=2))
    return 2


def main() -> int:
    pins = json.loads(PINS.read_text())
    allowed = {e["name"]: e for e in pins.get("allowed", [])}
    if len(sys.argv) < 2:
        print("usage: mount_genesis.py <local-genesis.json>")
        return 1
    path = Path(sys.argv[1])
    if not path.is_file():
        return deny("missing_file")
    raw = path.read_bytes()
    digest = sha256_bytes(raw)
    expected = pins.get("genesis_sha256")
    if expected and expected != digest:
        return deny("genesis_hash_mismatch")
    try:
        gen = json.loads(raw.decode())
    except json.JSONDecodeError:
        return deny("genesis_not_json")
    for pack in gen.get("packs", []):
        name = pack.get("name")
        if name not in allowed:
            return deny(f"unpinned_pack:{name}")
        if pack.get("exec") is True:
            return deny(f"exec_forbidden:{name}")
    print(json.dumps({"status": "mounted", "genesis_sha256": digest, "execute": False}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
