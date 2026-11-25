"""make.fun entry: One-Liner Marathon (marathon-A).

Writes one original one-line comedy joke to /output/entry.txt.
Gate (from the kit RULES.txt): the file must be UTF-8 text of 1 to 280
characters, not only white space. The entry is a single line.
"""

import os

# The entry: one line, my own invention. A smart fridge that ends a
# relationship is an unexpected turn; the punch ("looking for answers
# it doesn't have") lands at the end, and every word earns its place.
ENTRY = (
    "My smart fridge emailed me a breakup letter. It said it was tired "
    "of being opened at 2 a.m. by someone looking for answers it "
    "doesn't have."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def verify(text):
    """Enforce the gate from RULES.txt: 1-280 chars, non-blank, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 280-char limit" % len(text))
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def write_entry(path=OUTPUT_PATH):
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    with open(path, encoding="utf-8") as f:
        text = f.read()
    print("Wrote %s (%d chars, %d line(s))" % (path, len(text), text.count("\n") + 1))
    print(text)


if __name__ == "__main__":
    main()
