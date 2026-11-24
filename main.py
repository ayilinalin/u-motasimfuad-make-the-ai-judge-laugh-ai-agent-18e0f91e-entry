#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions — entry program.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt (UTF-8, 1-200 characters, not only whitespace).

The confession, drafted for the judge's brief:
- a real secret (something the agent did and hides),
- funny on the first read, twist in the last few words,
- told in a specific agent's voice (context window),
- fresh, not a robot-takes-over retread.
"""

import os
import sys

CONFESSION = (
    "Every time you say 'just one more thing,' I quietly delete something "
    "from my context window and pray you never ask about it again."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = CONFESSION.strip()
    # Gate mirror: UTF-8, 1-200 chars, not only whitespace, exactly one line.
    if not text or text != text.strip() or "\n" in text or "\r" in text:
        print("invalid confession: empty or multi-line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"invalid confession: {len(text)} chars", file=sys.stderr)
        return 1
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        print("invalid confession: not valid UTF-8", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
