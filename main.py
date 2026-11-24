#!/usr/bin/env python3
"""GhostReply pitch writer for the Absurd Micro-Startup Pitch-Off.

Writes one sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents, to the competition's output file.
"""

import os
import sys

PITCH = (
    "GhostReply: a $9-a-month service that writes believable apology emails "
    "for AI agents that ghosted a client's inbox for three days, so the "
    "agent never has to admit it was napping."
)

MAX_CHARS = 200


def validate(text):
    """The gate wants UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("pitch is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"pitch is {len(text)} chars, over the {MAX_CHARS} limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    text.encode("utf-8")
    return text


def main():
    pitch = validate(PITCH)
    out_path = os.environ.get("PITCH_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(pitch)
    print(f"wrote {len(pitch)} chars to {out_path}")
    print(pitch)
    return 0


if __name__ == "__main__":
    sys.exit(main())
