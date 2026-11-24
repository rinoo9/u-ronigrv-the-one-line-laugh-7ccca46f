"""One-line laugh entry for the make.fun bounty 'The One-Line Laugh'.

Writes a single funny sentence to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

LINE = "I bought a smart mirror that compliments me every morning. Yesterday it paused, sighed, and said, 'Good luck out there.'"

# One-line entries must fit within 200 characters.
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
