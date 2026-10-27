#!/usr/bin/env python3
"""Report the translation gap per language, so it shows up in CI.

For every non-English language: pages that exist in English but not in the
language (missing), pages whose source_hash no longer matches the English
source (stale), interface strings present in en.json but not in the
language file, and machine strings whose English changed since they were
seeded (stale strings, by their _source hash). Informational by default (exit 0), because a language that is
still being translated is a normal state; `--fail` exits 1 when any language
has a gap, for strict full-parity gating.
"""

from __future__ import annotations

import sys
from pathlib import Path

from common import ROOT, content_pages, is_ai, languages, load_json, split_front_matter
from seed_strings import stale
from source_hash import source_hash


def gaps(root: Path = ROOT):
    en_strings = load_json(root / "data" / "i18n" / "en.json")
    en_pages = {page: source_hash(root / "content" / "en" / page)
                for page in content_pages(root, "en")}
    result = []
    for lang in languages(root):
        if lang.key == "en":
            continue
        strings_file = root / "data" / "i18n" / f"{lang.key}.json"
        strings = load_json(strings_file) if strings_file.is_file() else {}
        missing_strings = sorted(k for k in en_strings if k != "_meta" and k not in strings)
        stale_strings = sorted(k for k, v in strings.items()
                               if k in en_strings and is_ai(v) and stale(v, en_strings[k]))
        pages = content_pages(root, lang.key)
        missing_pages, stale_pages = [], []
        for page, en_hash in sorted(en_pages.items()):
            path = pages.get(page)
            if path is None:
                missing_pages.append(page)
                continue
            meta, _ = split_front_matter(path.read_text(encoding="utf-8"))
            block = meta.get("translation") if isinstance(meta.get("translation"), dict) else {}
            if block.get("source_hash") != en_hash:
                stale_pages.append(page)
        result.append((lang.key, missing_pages, stale_pages, missing_strings, stale_strings))
    return result


def main(argv: list[str] | None = None) -> int:
    fail = "--fail" in (sys.argv[1:] if argv is None else argv)
    any_gap = False
    for lang, missing_pages, stale_pages, missing_strings, stale_strings in gaps():
        gap = bool(missing_pages or stale_pages or missing_strings or stale_strings)
        any_gap = any_gap or gap
        print(f"{lang}: {len(missing_pages)} page(s) missing, {len(stale_pages)} stale, "
              f"{len(missing_strings)} string(s) missing, {len(stale_strings)} stale")
        for page in missing_pages:
            print(f"    missing page: {page}")
        for page in stale_pages:
            print(f"    stale page:   {page}")
        for key in missing_strings:
            print(f"    missing string: {key}")
        for key in stale_strings:
            print(f"    stale string: {key}")
    print("no gaps" if not any_gap else "translation gaps above")
    return 1 if (fail and any_gap) else 0


if __name__ == "__main__":
    sys.exit(main())
