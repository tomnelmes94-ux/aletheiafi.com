import os
import fitz

INTAKE_DIR = os.path.expanduser("~/lucy/pdf_intake")
DOCS_DIR = os.path.expanduser("~/lucy/docs")

os.makedirs(DOCS_DIR, exist_ok=True)

converted = 0
for filename in os.listdir(INTAKE_DIR):
    if filename.endswith(".pdf"):
        input_path = os.path.join(INTAKE_DIR, filename)
        output_name = filename.replace(".pdf", ".txt")
        output_path = os.path.join(DOCS_DIR, output_name)
        try:
            doc = fitz.open(input_path)
            text = ""
            for page in doc:
                text += page.get_text()
            if text.strip():
                with open(output_path, "w") as f:
                    f.write(text)
                print(f"Converted — {output_name} ({len(text)} chars)")
                converted += 1
            else:
                print(f"Empty — {output_name}")
        except Exception as e:
            print(f"Failed — {filename}: {e}")

print(f"\n{converted} documents converted.")
