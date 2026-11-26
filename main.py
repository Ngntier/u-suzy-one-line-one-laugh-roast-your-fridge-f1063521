#!/usr/bin/env python3
"""Write the one-line roast to entry.txt for the make.fun bounty."""

import os

ENTRY_LINE = (
    "The crisper drawer is just a morgue with better lighting — "
    "everything in there died with good intentions."
)


MAX_LINE_LENGTH = 200


def validate_entry(text):
    """Check the entry is a single non-empty line within the cap."""
    if not text:
        raise ValueError("entry line must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_LINE_LENGTH:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_LINE_LENGTH} cap"
        )
    return text


def output_path():
    """Resolve the output directory and entry file path."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main():
    checked = validate_entry(ENTRY_LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(checked)


if __name__ == "__main__":
    main()
