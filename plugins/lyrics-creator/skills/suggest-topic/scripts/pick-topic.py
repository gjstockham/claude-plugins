#!/usr/bin/env python3
"""Pick a random topic from a topics text file (one topic per line)."""

import random
import sys


def pick_topic(filepath: str) -> str:
    with open(filepath, encoding="utf-8") as f:
        topics = [line.strip() for line in f if line.strip()]
    if not topics:
        print("ERROR: topics file is empty", file=sys.stderr)
        sys.exit(1)
    return random.choice(topics)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <topics-file>", file=sys.stderr)
        sys.exit(1)
    print(pick_topic(sys.argv[1]))
