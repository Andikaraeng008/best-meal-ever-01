"""Best Meal entry: write one sentence about the best meal ever had.

The sentence is a single concrete memory: a bowl of soup left at the
door after a father's funeral, still warm, with a note that turns grief
into care in its final phrase. It is written verbatim to
/output/entry.txt, exactly one sentence of 158 characters.
"""

import os

ENTRY = (
    # One sentence, 158 characters: concrete dish, place, moment, and a
    # closing twist ("eat first, grieve later") that reframes the meal.
    "The best meal I ever had was a bowl of soup my neighbour left at "
    "my door after my father's funeral, still warm, with a note that "
    "said eat first, grieve later."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
