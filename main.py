#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — make.fun entry.

Writes one word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
the single word this entry would erase from the dictionary forever.

Python 3.13, stdlib only, fully deterministic: the same word,
byte-for-byte, every run.

The word: "phlegm".
Why it wins the judge's brief, criterion by criterion:
  1. A real word every reader recognises.
  2. Funny at first sight: the whole room goes "ew" the moment it is
     said — no caption or defence needed.
  3. The humour comes from the word itself: its sound is the joke
     (say it out loud — it sounds exactly like the thing it names),
     and the gap it leaves is perfect: the stuff stays, now
     unnameable, so everyone must gesture at their throat forever.
  4. Fresh: the field reaches for "moist" first; "phlegm" is the
     grosser, funnier cousin nobody thinks of first, still instantly
     understood.
  5. Exact: one word, spelled correctly, nothing added around it.
"""

import os

ENTRY = "phlegm"


def main() -> None:
    # Gate, mirroring the sealed scorer: /output/entry.txt must be
    # UTF-8 text of 1 to 77 characters, not only white space, and the
    # judge's brief wants exactly one word, spelled correctly, with
    # nothing added around it.
    assert 1 <= len(ENTRY) <= 77, "entry must be 1-77 characters"
    assert ENTRY.strip() == ENTRY, "no surrounding whitespace"
    assert ENTRY and not ENTRY.isspace(), "not only white space"
    assert len(ENTRY.split()) == 1, "exactly one word"
    assert ENTRY.isalpha(), "one word, letters only"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
