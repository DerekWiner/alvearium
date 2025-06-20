#!/bin/bash

# === CONFIGURATION ===
ANCHORS_FILE="./anchors.md"
ROOT_DIR="./alvearium-0.1-alpha"
TMP_FILE=".tmp_replacements"

# === STEP 1: BUILD LOOKUP TABLE FROM anchors.md ===
declare -A FILE_HASH_MAP

while IFS='|' read -r file hash link; do
    file=$(echo "$file" | xargs)
    hash=$(echo "$hash" | tr -d '`' | xargs)
    if [[ "$file" != "" && "$hash" =~ ^[a-zA-Z0-9_-]{43,}$ ]]; then
        FILE_HASH_MAP["$file"]="$hash"
    fi
done < <(grep -E '^|' "$ANCHORS_FILE")

# === STEP 2: FIND + REPLACE PLACEHOLDERS ===
echo "🛠 Updating IPFS mirror references..."

for rel_path in "${!FILE_HASH_MAP[@]}"; do
    file_path="$ROOT_DIR/${rel_path#*/}" # remove "alvearium-0.1-alpha/" prefix if repeated
    hash="${FILE_HASH_MAP[$rel_path]}"
    arweave_link="https://arweave.net/$hash"

    if [[ -f "$file_path" ]]; then
        # Replace common IPFS phrases and update inline
        sed -i.bak \
            -e "s|IPFS mirror: pending|Arweave mirror: [$hash]($arweave_link)|g" \
            -e "s|ipfs://[a-zA-Z0-9]*|$arweave_link|g" \
            "$file_path"

        echo "✅ Updated: $file_path"
    else
        echo "⚠️ File not found: $file_path"
    fi
done

echo "🎉 Done. IPFS references have been replaced with Arweave links."
