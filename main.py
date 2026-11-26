"""Best Meal entry: write one sentence about the best meal ever had.

The sentence is a single concrete memory: my own wedding cake eaten
alone in a parking lot at two in the morning, the groom was me, the
bride had left, and the cake was still perfect. It is written verbatim
to /output/entry.txt, exactly one sentence of 174 characters.
"""

import os

ENTRY = "The best meal of my life was my own wedding cake eaten alone in a parking lot at two in the morning, and the groom was me, the bride had left, and the cake was still perfect."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
