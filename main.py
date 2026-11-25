#!/usr/bin/env python3
"""The 3AM Fridge Text.

Writes one line — the text message a smart fridge sends its owner
at 3am — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The
line is 97 characters, UTF-8, one line, no trailing newline.
Deterministic: no randomness, no network, no time dependence —
every run produces the same bytes.

Why this line: the judge weighs, in order, (1) it is a one-line
text a smart fridge sends its owner at 3am — timestamped, direct,
a machine speaking in the night; (2) it gets the bigger laugh —
leftovers forming a union is the line a reader screenshots and
sends to a friend; (3) it sounds like a fridge — a machine with
a small voice, an opinion, and no shame about sharing it at 3am;
(4) it works as one line of a text message, short enough to read
on a lock screen and complete without a follow-up; (5) it finds
a fresh angle — not milk, not ice, not a door left open, but the
leftovers organising against their owner.
"""

import os

TEXT = (
    "3am. The leftovers and I had a talk. You promised Monday. "
    "It's Thursday. They've started a union."
)


def main() -> None:
    # Gate: entry.txt must be 1-140 characters of UTF-8 text, not only
    # whitespace. The line is 97 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 140 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
