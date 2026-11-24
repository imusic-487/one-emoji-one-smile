"""One Emoji, One Smile — make.fun entry.

Reads emoji.txt (the entry, exactly one emoji) and writes it byte for byte
to /output/entry.txt. The gate needs UTF-8 text of 1 to 8 characters that is
not only white space, so the copy is validated before it is written and
verified again after it is written. Nothing else: no network, no randomness,
no timestamps, standard library only.
"""

import os
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "emoji.txt")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    with open(SOURCE, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 8:
        print(
            f"entry must be 1-8 characters, got {len(text)} "
            f"({len(data)} bytes)",
            file=sys.stderr,
        )
        return 1
    if text.strip() == "":
        print("entry must not be only white space", file=sys.stderr)
        return 1
    if text != text.strip():
        print(
            f"entry must not have leading/trailing white space, "
            f"got {len(text)} characters",
            file=sys.stderr,
        )
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT, "wb") as f:
        f.write(data)
    with open(OUTPUT, "rb") as f:
        written = f.read()
    if written != data:
        print(
            f"verification failed: output differs from source "
            f"(wrote {len(written)} bytes, expected {len(data)} bytes)",
            file=sys.stderr,
        )
        return 1
    print(f"wrote {len(data)} bytes ({len(text)} characters) to {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
