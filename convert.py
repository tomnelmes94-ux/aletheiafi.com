import json
import re
import os

INPUT_FILE = os.path.expanduser("~/lucy/first_night.txt")
OUTPUT_FILE = os.path.expanduser("~/lucy/memory.json")

import os

with open(INPUT_FILE, "r") as f:
    raw = f.read()

# Split on Tom: or Lucy: markers
pattern = re.compile(r'\n(Tom|Lucy):\s*')
parts = pattern.split(raw)

messages = []
i = 1
while i < len(parts) - 1:
    speaker = parts[i].strip()
    content = parts[i+1].strip()
    if speaker == "Tom":
        role = "user"
    elif speaker == "Lucy":
        role = "assistant"
    else:
        i += 2
        continue
    if content:
        messages.append({"role": role, "content": content})
    i += 2

with open(OUTPUT_FILE, "w") as f:
    json.dump(messages, f, indent=2)

print(f"Done. {len(messages)} messages saved to memory.json")
