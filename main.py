#!/usr/bin/env python3
"""elevawkward - Invent a Word We Need (make.fun).

Writes the entry text to /output/entry.txt, the one text the
competition's judge compares. Standard library only, no network,
deterministic: every run writes the same bytes.

The entry must be between 1 and 140 characters, so main() checks
the length before writing anything; a bad length fails loudly
instead of producing an invalid submission. The output path is
/output/entry.txt when that directory exists (the competition
sandbox), and falls back to output/ next to this file for local
runs, so the same bytes land in the same file either way.
"""

import os
from pathlib import Path

# "elevawkward" blends elevator + awkward: the word itself is the
# joke, naming the stiff silence of a shared lift in one breath.
ENTRY = (
    "elevawkward (n.) \u2014 the stiff, eyes-on-the-floor silence "
    "of sharing a lift with a stranger."
)


def main() -> None:
    # The gate only accepts 1 to 140 characters, so refuse to write
    # anything outside that range instead of submitting an invalid entry.
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-140")
    out_dir = Path("/output") if Path("/output").is_dir() else Path(__file__).resolve().parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
