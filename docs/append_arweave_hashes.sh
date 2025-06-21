#!/bin/bash

ANCHORS_FILE="anchors.md"
ROOT_DIR="./alvearium"

# Validate
if [[ ! -f "$ANCHORS_FILE" ]]; then
  echo "❌ anchors.md not found!"
  exit 1
fi

echo "🔍 Scanning anchors.md and applying hashes..."

# Read each row from anchors.md
grep -E '^\| ' "$ANCHORS_FILE" | while IFS='|' read -r _ relpath txid link; do
  # Clean inputs
  relpath=$(echo "$relpath" | xargs)
  txid=$(echo "$txid" | tr -d '`' | xargs)

  # Build full path
  filepath="$ROOT_DIR/${relpath#*/}"

  # Skip if file doesn't exist
  if [[ ! -f "$filepath" ]]; then
    echo "⚠️ Skipping missing: $filepath"
    continue
  fi

  # Append Arweave hash footer
  echo -e "\n---\n📌 Arweave Hash: $txid" >> "$filepath"
  echo "✅ Appended hash to $filepath"
done

echo "🎉 Done. All Arweave hashes appended to file footers."
