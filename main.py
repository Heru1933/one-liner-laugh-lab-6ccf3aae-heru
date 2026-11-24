"""One-Liner Laugh Lab entry: the robot vacuum's excuse.

Writes exactly one line to entry.txt — the excuse a robot vacuum
gives after eating a sock: a self-defence claim, the sock having
lunged at its brushes first. One line, no trailing newline, so the
gate counts only the line itself.
"""

import os
import sys


def main():
    entry = "The sock lunged at my brushes first. I was defending my charging dock."
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
