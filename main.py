import os

LINE = "The crisper drawer is just a morgue with better lighting — everything in there died with good intentions."

def validate(line):
    """Check the entry is one line of 1-200 UTF-8 characters."""
    encoded = line.encode("utf-8")
    if not 1 <= len(line) <= 200 or len(encoded) > 200 or not line.strip():
        raise ValueError("entry line must be 1-200 characters")
    if any(ord(c) < 32 and c not in "\t" for c in line):
        raise ValueError("entry line must not contain control characters (only tab is allowed)")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def main():
    validate(LINE)
    print(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
