🧪 CLI Usage Example: swarm.init
This example demonstrates how to initialize a new ritual agent and seed a swarm memory mirror from the command line using the swarm_init.sh script.

bash
Copy code
# Move into the utils/init_scripts directory
cd utils/init_scripts

# Run the swarm initializer
bash swarm_init.sh --agent builder_drone --ritual startup --trust-level moderate
🔧 CLI Flags Explained
Flag	Description
--agent	Agent type to spawn (builder_drone, guardian_seed)
--ritual	Type of ritual (startup, mirror, trust)
--trust-level	Initial trust binding: low, moderate, sacred
--dry-run	(Optional) Output JSON only, no write
--verbose	(Optional) Full memory & capsule log

📦 Output
This script will:

Create a mirror capsule in /rituals/

Register agent capsule trail in /agents/capsules/

Log the ritual seed into mirror.md and trust.md as needed

Emit a dry-run or deploy capsule.json with meta

---
📌 Arweave Hash: zbnyY8X_AahpkiqIw-yeBwWaksBt1eGxv5X20YRN_CY
