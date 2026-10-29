# Alvearium repository guide

This guide points to the current repository layout and distinguishes runnable code from specifications and historical material.

## Start here

| Goal | Start with |
| --- | --- |
| Run the local prototype | [Spawn guide](docs/spawn.md), then [spawn code guide](code/spawn/README.md) |
| Review implementation | `code/spawn/spawn.py`, `code/spawn/pins.json`, and tests where present |
| Study architecture | `docs/`, `pages/`, and linked component repositories |
| Review historical provenance | `docs/anchors.md`, noting that it describes an earlier snapshot |
| Reuse code or assets | Read `LICENSE` and confirm applicable terms before copying |

## Current status

The local spawn runner is a prototype. Other identity, governance, value, memory and chain capabilities may be described in documents or component repositories, but should not be assumed to be integrated into this runnable slice.

## Repository map

- `code/spawn/` contains the local spawn prototype and related configuration examples.
- `docs/` contains design and implementation notes.
- `pages/` contains manifesto and whitepaper material.
- Asset and schematic files provide visual material.
- `LICENSE` contains custom terms combined with CC0 material. Do not assume this is equivalent to an unmodified standard open-source license.

## Historical documents

Older documents may refer to paths and scripts that are not present at those locations in the current tree. Treat such references as historical until checked against the current repository. An old anchor list is not proof that the current working tree matches an earlier snapshot.
