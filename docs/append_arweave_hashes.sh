#!/bin/bash

# === CONFIGURATION ===
ANCHORS_FILE="anchors.md"
ROOT_DIR="/c/Users/Canajun/Documents/GitHub/alvearium"

# === FUNCTIONALITY ===
echo "🔍 Scanning $ANCHORS_FILE and applying hashes in $ROOT_DIR..."

# Ensure anchors.md exists
if [[ ! -f "$ANCHORS_FILE" ]]; then
  echo "❌ anchors.md not found!"
  exit 1
fi

# Parse anchors.md and process each row
grep -E '^\| ' "$ANCHORS_FILE" | while IFS='|' read -r _ relpath txid _; do
  # Clean up inputs
  relpath=$(echo "$relpath" | xargs)
  txid=$(echo "$txid" | tr -d '`' | xargs)

  # Skip empty
  [[ -z "$relpath" || -z "$txid" ]] && continue

  # Translate path from anchors.md to absolute file location
  clean_path="${relpath#*/}" # strip leading folder
  full_path="$ROOT_DIR/$clean_path"

  # Normalize slashes
  full_path="${full_path//\\//}"

  if [[ -f "$full_path" ]]; then
    echo -e "\n---\n📌 Arweave Hash: $txid" >> "$full_path"
    echo "✅ Appended to: $full_path"
  else
    echo "⚠️ File not found: $full_path"
  fi
done

echo "🎉 All matching files processed."

