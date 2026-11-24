"""Entry for u-kreutzx-the-funniest-out-of-office-054815cf.

Writes the one-line out-of-office reply to /output/entry.txt, the path
the sealed scorer reads. A reply a real person would actually set, with
a voice of its own and a twist the reader does not see coming: the inbox
is not empty, it is simply, finally, unseen.
"""

import os

ENTRY = (
    "I am out of office and will not see your email, which is the closest "
    "I have ever come to inbox zero."
)

MAX_CHARS = 140


def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, max {MAX_CHARS}"
    )
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
