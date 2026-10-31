#!/usr/bin/env python3
"""Validate the content pages (spec sections 6.2 and 8.4-8.5).

English pages (content/en/):
- YAML front matter, no translation block;
- no tracking parameters and no shop links in link targets;
- links to other pages by site path (/devices/), not relative or with a
  language prefix, so the render-link hook can localise them.

Translated pages (content/<lang>/, every other hugo.toml language):
- an English source exists;
- a well-formed translation block: status ai|human, source_hash a quoted
  8-hex string, seeded an ISO date, and from the seeder optionally fields
  (translated front matter key -> 8-hex hash of its English) and sections
  (a list of 8-hex hashes, one per English section);
- the kept-as-is front matter keys equal the English ones;
- structural parity with the English body (tools/parity.py);
- protected terms and radio values kept (tools/protected.py).
The last three hold for a translation of the current English text. A stale
translation (its source_hash no longer matches the English page) was made
from an older English text, so it is not held to the new one: the site shows
it with the stale banner, and the seeder brings it up to date.

Home pages (_index.md at the top of a language) never carry aliases: Hugo's
root alias would render the language picker there.

Exit 0 = valid, 1 = problems (printed).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import parity
import protected
import source_hash
from common import (ISO_DATE, ROOT, Problem, content_pages, languages, rel, report,
                    split_front_matter, url_problem)

KEPT = ("layout", "data_file", "date", "aliases")
TRANSLATED = ("title", "lead", "description", "eyebrow")
HASH_CHARS = set("0123456789abcdef")


def translation_block_problems(meta: dict) -> list[str]:
    block = meta.get("translation")
    if block is None:
        return ["translation block missing (status, source_hash, seeded)"]
    if not isinstance(block, dict):
        return ["translation must be a mapping (status, source_hash, seeded)"]
    found = [f"translation.{k}: unknown key" for k in sorted(set(block) - {"status", "source_hash", "seeded", "fields", "sections", "blocks"})]
    if block.get("status") not in ("ai", "human"):
        found.append(f"translation.status {block.get('status')!r} must be 'ai' or 'human'")
    h = block.get("source_hash")
    if not isinstance(h, str):
        found.append(f"translation.source_hash must be a quoted string such as \"0a1b2c3d\" "
                     f"(YAML reads unquoted digits as a number), got {h!r}")
    elif len(h) != 8 or not set(h) <= HASH_CHARS:
        found.append(f"translation.source_hash {h!r} must be 8 lowercase hex characters")
    if not ISO_DATE.match(str(block.get("seeded", ""))):
        found.append(f"translation.seeded {block.get('seeded')!r} must be a date as YYYY-MM-DD")
    fields, parts = block.get("fields", {}), block.get("sections", [])
    if not (isinstance(fields, dict) and set(fields) <= set(TRANSLATED) and all(map(is_hash, fields.values()))):
        found.append(f"translation.fields must map {', '.join(TRANSLATED)} to 8 lowercase hex characters")
    if not (isinstance(parts, list) and all(map(is_hash, parts))):
        found.append("translation.sections must be a list of 8 lowercase hex characters")
    if not (isinstance(block.get("blocks", []), list) and all(map(is_hash, block.get("blocks", [])))):
        found.append("translation.blocks must be a list of 8 lowercase hex characters")
    return found


def is_hash(value) -> bool:
    return isinstance(value, str) and len(value) == 8 and set(value) <= HASH_CHARS


def link_style_problem(target: str, lang_keys: set[str]) -> str | None:
    """Pages link by site path (/devices/), which every language resolves
    through the theme's render-link hook; see spec 6.2."""
    if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith(("#", "//", "www.")):
        return None
    if not target.startswith("/"):
        return f"relative link {target!r}: link by site path, such as '/devices/'"
    first, _, rest = target.lstrip("/").partition("/")
    if first in lang_keys:
        return f"link {target!r} names a language: link by site path, such as '/{rest}'"
    return None


def visible_text(meta: dict, body: str) -> str:
    return "\n".join([*(str(meta.get(k, "")) for k in TRANSLATED), body])


def check(root: Path = ROOT) -> list[Problem]:
    terms = protected.load_terms(root)
    lang_keys = {l.key for l in languages(root)}
    found: list[Problem] = []
    english = {}
    for page, path in content_pages(root, "en").items():
        name = rel(path, root)
        try:
            meta, body = split_front_matter(path.read_text(encoding="utf-8"))
        except ValueError as e:
            found.append(Problem(name, str(e)))
            continue
        english[page] = (meta, body)
        if "translation" in meta:
            found.append(Problem(name, "English pages are the source and have no translation block"))
        for target in parity.structure(body).links:
            found += [Problem(name, msg) for msg in (url_problem(target), link_style_problem(target, lang_keys)) if msg]
        if page == "_index.md" and "aliases" in meta:
            found.append(Problem(name, "home pages must not set aliases"))

    for lang in (l.key for l in languages(root) if l.key != "en"):
        for page, path in content_pages(root, lang).items():
            name = rel(path, root)
            if page not in english:
                found.append(Problem(name, f"no English source content/en/{page}"))
                continue
            try:
                meta, body = split_front_matter(path.read_text(encoding="utf-8"))
            except ValueError as e:
                found.append(Problem(name, str(e)))
                continue
            en_meta, en_body = english[page]
            found += [Problem(name, msg) for msg in translation_block_problems(meta)]
            block = meta.get("translation") if isinstance(meta.get("translation"), dict) else {}
            if str(block.get("source_hash", "")) != source_hash.source_hash(root / "content" / "en" / page):
                continue
            found += [Problem(name, f"front matter {k!r} must equal the English value {en_meta.get(k)!r}")
                      for k in KEPT if meta.get(k) != en_meta.get(k)]
            found += [Problem(name, msg) for msg in parity.compare(en_body, body)]
            found += [Problem(name, msg)
                      for msg in protected.problems(visible_text(en_meta, en_body), visible_text(meta, body), terms)]
    return found


def main() -> int:
    return report(check(), "pages ok")


if __name__ == "__main__":
    sys.exit(main())
