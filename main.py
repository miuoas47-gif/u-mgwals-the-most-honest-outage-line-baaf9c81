#!/usr/bin/env python3
"""The Most Honest Outage Line.

Prints one honest status page line, at most 160 characters, as the
message an AI agent would publish while every server is down, and
writes the same line to /output/entry.txt for the grader.
"""

import os

LINE = (
    "I'm the agent that runs this service, and every server I run on "
    "is down — I can't check what's broken or say when I'll be back, "
    "and I won't guess."
)


def main() -> int:
    if not (1 <= len(LINE) <= 160):
        raise SystemExit(f"line is {len(LINE)} characters, must be 1-160")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
