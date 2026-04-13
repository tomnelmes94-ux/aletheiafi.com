import json
import os
from datetime import datetime

MEMORY_FILE = os.path.expanduser("~/lucy/memory.json")
ARCHIVE_DIR = os.path.expanduser("~/lucy/memory_archive")
ACTIVE_MESSAGES = 20  # 10 exchanges = 20 messages (user + assistant pairs)

os.makedirs(ARCHIVE_DIR, exist_ok=True)

with open(MEMORY_FILE, "r") as f:
    memory = json.load(f)

if len(memory) <= ACTIVE_MESSAGES:
    print(f"Memory at {len(memory)} messages — no trim needed.")
else:
    archive = memory[:-ACTIVE_MESSAGES]
    active = memory[-ACTIVE_MESSAGES:]
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_path = os.path.join(ARCHIVE_DIR, f"archive_{timestamp}.json")
    
    with open(archive_path, "w") as f:
        json.dump(archive, f, indent=2)
    
    with open(MEMORY_FILE, "w") as f:
        json.dump(active, f, indent=2)
    
    print(f"Trimmed. {len(archive)} messages archived. {len(active)} active.")
    print(f"Archive saved: archive_{timestamp}.json")
