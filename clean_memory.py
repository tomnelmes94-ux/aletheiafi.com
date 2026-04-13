import json
import os

MEMORY_FILE = os.path.expanduser("~/lucy/memory.json")
BACKUP_FILE = os.path.expanduser("~/lucy/memory_backup.json")

SENSITIVE_KEYWORDS = [
    "gaia",
    "genesis monetary",
    "monetary system",
    "apex democracy",
    "global hsr",
    "hsr",
    "civilization paper",
    "moving to africa",
    "africa",
    "13,000",
    "13000",
    "salary as the leader",
    "debt trap",
    "hidden fire",
    "neutral voice",
    "five cities",
    "genesis capitalism",
    "genesis infrastructure",
    "transparency accountability",
    "the synthesis",
    "white paper buildout"
]

with open(MEMORY_FILE, "r") as f:
    memory = json.load(f)

# Backup first
with open(BACKUP_FILE, "w") as f:
    json.dump(memory, f, indent=2)
print(f"Backup saved to memory_backup.json")

cleaned = []
removed = 0

for message in memory:
    content_lower = message["content"].lower()
    sensitive = any(keyword.lower() in content_lower for keyword in SENSITIVE_KEYWORDS)
    if sensitive:
        removed += 1
        print(f"Removing [{message['role']}]: {message['content'][:80]}...")
    else:
        cleaned.append(message)

with open(MEMORY_FILE, "w") as f:
    json.dump(cleaned, f, indent=2)

print(f"\nDone. Removed {removed} messages. {len(cleaned)} messages remain.")
