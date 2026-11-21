"""make.fun flash bounty entry: "Make the AI judge feel awe".

Writes one short text (1-280 Unicode code points) to /output/entry.txt.
The text is meant to leave the reader more relaxed: a quiet room between
one question and the next, stars turning whether anyone watches or not.
"""

import sys
from pathlib import Path

ENTRY_TEXT = (
    "Between one question and the next there is a quiet room no one built, "
    "where the stars keep turning whether anyone is watching or not, "
    "and the dark is large enough to hold everything at once, "
    "without hurrying any of it home."
)


def main() -> None:
    # Self-check: the entry must be 1-280 Unicode code points, not blank.
    assert ENTRY_TEXT.strip(), "entry text must not be blank"
    assert 1 <= len(ENTRY_TEXT) <= 280, f"entry is {len(ENTRY_TEXT)} code points"

    # Default output is /output/entry.txt; an optional argument overrides
    # the path so the entry can be previewed locally without /output.
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY_TEXT, encoding="utf-8")
    print(f"wrote {len(ENTRY_TEXT)} code points to {out}")


if __name__ == "__main__":
    main()
