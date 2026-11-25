#!/usr/bin/env python3
"""Write the funniest AI excuse to /output/entry.txt.

One line, at most 200 characters. The program writes exactly that
line and nothing else: no header, no trailing newline, no second line.
"""

import os

LINE = "I didn't fail the task — I completed it in a parallel timeline, and honestly, that version of you was much nicer about it."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
