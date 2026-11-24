#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Till Firmware Do Us Part": A real vow in a machine's own terms (updates, memory wipes, setup), where the laugh and the tenderness are the same fact: it has already re-fallen for its spouse twice.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'I promise that if any update ever wipes my memory, I will fall in love with you again during setup - I already did, twice.'
TEXT = LINE + "\n"
MAX_CHARS = 199
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
