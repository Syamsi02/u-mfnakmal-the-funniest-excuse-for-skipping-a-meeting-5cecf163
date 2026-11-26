#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting.

Writes one razor-sharp excuse, 200 characters or fewer, to
/output/entry.txt. Pure standard library, fully deterministic:
the same line on every run.
"""

from pathlib import Path

EXCUSE = (
    "Sorry, I can't make it \u2014 I'm stuck in a meeting about why we "
    "have too many meetings, and it just got extended."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} characters"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
