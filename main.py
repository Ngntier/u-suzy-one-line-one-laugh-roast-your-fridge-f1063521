import os

LINE = "The crisper drawer is just a morgue with better lighting — everything in there died with good intentions."

def main():
    # Gate check: entry must be 1-200 characters of UTF-8 text.
    encoded = LINE.encode("utf-8")
    if not 1 <= len(LINE) <= 200 or len(encoded) > 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 characters")
    if any(ord(c) < 32 and c not in "\t" for c in LINE):
        raise ValueError("entry line must not contain control characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    print(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
