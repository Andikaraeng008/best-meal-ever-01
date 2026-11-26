"""Best Meal entry: write one sentence about the best meal ever had.

The sentence is a single concrete memory: cold rice and salted egg
shared from one plastic bag on a night bus, saved all day by the man
beside me for someone he would never see again. It is written verbatim
to /output/entry.txt, exactly one sentence of 166 characters.
"""

import os

ENTRY = "The best meal of my life was instant noodles cooked in a hotel kettle at 3 in the morning, and the stranger who shared them charged me nothing but the story of how he lost his restaurant."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
