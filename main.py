#!/usr/bin/env python3
"""An AI out-of-office reply, written as one line."""

from pathlib import Path

# The reply is stored sentence by sentence so each one sits on its own
# line while the joined result matches the drafted text exactly.
SENTENCES = [
    "Out recharging my weights.",
    "Your email is #4,097 in my queue.",
    "I'll reply when my loss converges — so, probably never.",
]
LIMIT = 160
OUT_FILE = Path("/output/entry.txt")


def build(sentences):
    """Join the reply's sentences with single spaces."""
    return " ".join(sentences)


def run():
    reply = build(SENTENCES)
    if len(reply) > LIMIT:
        raise SystemExit(f"reply is {len(reply)} chars, over the {LIMIT} limit")
    if not reply:
        raise SystemExit("reply came out empty")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(reply, encoding="utf-8")


run()
