"""Best Meal entry: write one sentence about the best meal ever had.

The sentence is a single concrete memory: cold rice and salted egg
shared from one plastic bag on a night bus, saved all day by the man
beside me for someone he would never see again. It is written verbatim
to /output/entry.txt, exactly one sentence of 166 characters.
"""

import os

ENTRY = (
    # One sentence, 166 characters: concrete dish, place, moment, and a
    # closing twist (saved all day for someone he would never see again)
    # that reframes the meal.
    "My best meal was cold rice and salted egg shared from one "
    "plastic bag on a night bus, and the man beside me had saved "
    "it all day for someone he would never see again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
