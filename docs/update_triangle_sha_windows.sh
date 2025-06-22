#!/bin/bash

# Set correct path for Windows Git Bash
ANCHOR_DIR="/c/Users/Canajun/Documents/GitHub/alvearium/docs"

ANCHORS_FILE="$ANCHOR_DIR/anchors.md"
METADATA_FILE="$ANCHOR_DIR/anchors_metadata.md"
MANIFEST_FILE="$ANCHOR_DIR/anchors_manifest_hash.md"

# Compute current SHA256 hashes
HASH_ANCHORS=$(shasum -a 256 "$ANCHORS_FILE" | cut -d ' ' -f 1)
HASH_METADATA=$(shasum -a 256 "$METADATA_FILE" | cut -d ' ' -f 1)
HASH_MANIFEST=$(shasum -a 256 "$MANIFEST_FILE" | cut -d ' ' -f 1)

# Overwrite triangle section in each file
for FILE in "$ANCHORS_FILE" "$METADATA_FILE" "$MANIFEST_FILE"; do
  # Remove previous triangle reference block
  sed -i '/🔗 Triangle SHA-256 References:/,/^$/d' "$FILE"
done

# Append updated triangle block
echo -e "\n---\n🔗 Triangle SHA-256 References:\n- anchors_metadata.md: \`$HASH_METADATA\`\n- anchors_manifest_hash.md: \`$HASH_MANIFEST\`" >> "$ANCHORS_FILE"
echo -e "\n---\n🔗 Triangle SHA-256 References:\n- anchors.md: \`$HASH_ANCHORS\`\n- anchors_manifest_hash.md: \`$HASH_MANIFEST\`" >> "$METADATA_FILE"
echo -e "\n---\n🔗 Triangle SHA-256 References:\n- anchors.md: \`$HASH_ANCHORS\`\n- anchors_metadata.md: \`$HASH_METADATA\`" >> "$MANIFEST_FILE"

echo "✅ Triangle SHA-256 hashes updated in all three files."
