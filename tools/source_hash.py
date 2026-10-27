#!/usr/bin/env python3
"""Translation staleness hash (spec section 6.2), identical to Hugo.

themes/fieldmap/layouts/_partials/source-hash.html computes
`substr (sha256 (strings.TrimSpace .RawContent)) 0 8` for a page. This
module computes the same value from the Markdown file, so the seeder,
the coverage report and CI agree with what the site shows:

- the file is read as bytes and decoded as UTF-8, so CRLF line endings
  hash exactly as Hugo sees them (they differ from LF on purpose);
- a leading byte-order mark is ignored, as Hugo ignores it;
- YAML (---) and TOML (+++) front matter are removed; other front
  matter formats are rejected rather than guessed;
- surrounding whitespace is trimmed with Go's unicode.IsSpace set, which
  differs from Python's str.strip() (Python also strips U+001C-U+001F).

Usage: source_hash.py FILE...   prints "<hash>  <file>" per file.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

# Go unicode.IsSpace: Latin-1 spaces plus the Unicode White_Space property.
GO_SPACE = "\t\n\v\f\r \x85\xa0                　"

FRONT_MATTER = {
    "---": re.compile(r"\A---[ \t]*\r?\n.*?^---[ \t]*(?:\r?\n|\Z)", re.S | re.M),
    "+++": re.compile(r"\A\+\+\+[ \t]*\r?\n.*?^\+\+\+[ \t]*(?:\r?\n|\Z)", re.S | re.M),
}


def body(text: str) -> str:
    """The page body Hugo exposes as .RawContent (front matter removed)."""
    text = text.removeprefix("﻿")
    for delimiter, pattern in FRONT_MATTER.items():
        if text.startswith(delimiter):
            match = pattern.match(text)
            if not match:
                raise ValueError(f"unterminated {delimiter} front matter")
            return text[match.end():]
    if text.lstrip(GO_SPACE).startswith("{"):
        raise ValueError("JSON front matter is not supported; use YAML (---)")
    return text


def source_hash_text(text: str) -> str:
    return hashlib.sha256(body(text).strip(GO_SPACE).encode("utf-8")).hexdigest()[:8]


def string_hash(text: str) -> str:
    """The same hash for one English string of data/i18n/en.json, stored as _source."""
    return hashlib.sha256(text.strip(GO_SPACE).encode("utf-8")).hexdigest()[:8]


def source_hash(path: Path | str) -> str:
    return source_hash_text(Path(path).read_bytes().decode("utf-8"))


def main(argv: list[str]) -> int:
    for name in argv:
        print(f"{source_hash(name)}  {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
