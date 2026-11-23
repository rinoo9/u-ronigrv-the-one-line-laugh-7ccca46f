"""One-line laugh entry for the make.fun bounty 'The One-Line Laugh'.

Writes a single funny sentence to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

LINE = "I downloaded a budgeting app to stop wasting money, and it immediately charged me $5 a month to tell me I'm wasting money."


def main() -> None:
    assert 1 <= len(LINE) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
