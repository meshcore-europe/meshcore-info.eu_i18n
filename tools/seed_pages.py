#!/usr/bin/env python3
"""Seed content/<lang>/ pages from content/en/ with a local LLM (spec 6.3).

A page is (re)translated when it is missing, or when it is machine
translated (status ai) and its English source changed since (stale
source_hash); --reseed-ai also redoes current machine pages. A page with
status human is never touched, even when stale: a reviewer updates it.

The translation block records a hash of each English section and of each
translated front matter field. A stale machine page keeps every section and
field whose English hash is unchanged, so a fix made there by hand stays,
and only the changed ones are translated again, each on its own with the
page so far as context. A page without that record, or --reseed-ai,
is translated whole.

A claude-* model translates the whole page, front matter fields and body,
in one call, written as a native writer would (tools/llm.py WHOLE_SYSTEM).
A front matter field or section of that answer that fails its check is
translated again on its own. A local model translates the body section by
section (a section starts at a heading); each section gets the sections
translated before it as context, so a term keeps one translation on the
whole page.
Each translated section must pass the parity check against its English
section (tools/parity.py) and keep protected terms and radio values
(tools/protected.py); after a failed retry the English section is kept, so
bad output never reaches the page. Front matter: title, lead,
description and eyebrow are translated; every other key is copied; the
translation
block records status ai, the English source_hash and today's date.

Usage:
  seed_pages.py [--langs nl,de] [--pages about.md,map.md] [--reseed-ai] [--dry-run]
  (endpoint and model: see tools/llm.py)
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable
from datetime import date
from pathlib import Path

import yaml

import parity
import protected
from common import ROOT, Language, content_pages, languages, split_front_matter
from source_hash import source_hash, string_hash
from validate_pages import TRANSLATED

# (text, language, context) -> translation; context is the page translated so far.
Translate = Callable[..., str]
# (English page, language) -> translated page, in one call.
TranslatePage = Callable[[str, Language], str]
ATTEMPTS = 2
# Above the translation block of a machine page: a reader who fixes one word
# on GitHub should know the next seeding run replaces it unless status is human.
NUDGE = "# Fixed the wording? Set status to human, or a change to the English there can replace your fix.\n"


def sections(body: str) -> list[str]:
    """Split a Markdown body before each heading outside code blocks."""
    parts, current, fence = [], [], None
    for line in body.splitlines(keepends=True):
        m = parity.FENCE.match(line)
        if fence is None and m:
            fence = m.group(1)
        elif fence is not None and m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
            fence = None
        elif fence is None and parity.HEADING.match(line) and current:
            parts.append("".join(current))
            current = []
        current.append(line)
    if current:
        parts.append("".join(current))
    return parts


def faithful(en: str, text: str, terms: list[str]) -> bool:
    return bool(text.strip()) and not parity.compare(en, text) and not protected.problems(en, text, terms)


def translate_section(section: str, lang: Language, translate: Translate, terms: list[str],
                      context: str = "") -> tuple[str, bool]:
    """(translated section, True) or (the English section, False)."""
    core = section.strip("\n")
    if not core.strip():
        return section, True
    lead = section[: len(section) - len(section.lstrip("\n"))]
    trail = section[len(section.rstrip("\n")):]
    for _ in range(ATTEMPTS):
        try:
            text = (translate(core, lang, context) if context else translate(core, lang)).strip("\n")
        except Exception:
            continue
        if faithful(core, text, terms):
            return lead + text + trail, True
    return section, False


def needs_seeding(path: Path, en_hash: str, reseed_ai: bool) -> bool:
    if not path.is_file():
        return True
    meta, _ = split_front_matter(path.read_text(encoding="utf-8"))
    block = meta.get("translation") if isinstance(meta.get("translation"), dict) else {}
    if block.get("status") == "human":
        return False
    return reseed_ai or block.get("source_hash") != en_hash


def fingerprint(en_meta: dict, en_body: str) -> tuple[dict, list[str]]:
    """Hashes of the English translated fields and of each English section."""
    fields = {k: string_hash(v) for k, v in en_meta.items() if k in TRANSLATED and isinstance(v, str) and v.strip()}
    return fields, [string_hash(part) for part in sections(en_body)]


def translation_block(en_path: Path, en_meta: dict, en_body: str, today: str) -> dict:
    fields, parts = fingerprint(en_meta, en_body)
    return {"status": "ai", "source_hash": source_hash(en_path), "seeded": today, "fields": fields, "sections": parts}


def render(meta: dict, body: str) -> str:
    """The page file: front matter, the translation block last, then the body."""
    rest = {k: v for k, v in meta.items() if k != "translation"}
    front = yaml.safe_dump(rest, sort_keys=False, allow_unicode=True, width=1000) if rest else ""
    block = meta.get("translation")
    if isinstance(block, dict):
        # Written by hand, so every hash is quoted: a YAML 1.2 reader takes 1e234567 for a number.
        # The hashes take one line each, so a reader editing the page on GitHub sees the text first.
        lines = [f"status: {block['status']}", f"source_hash: '{block['source_hash']}'", f"seeded: '{block['seeded']}'"]
        if "fields" in block:
            lines.append("fields: {" + ", ".join(f"{k}: '{v}'" for k, v in block["fields"].items()) + "}")
        if "sections" in block:
            lines.append("sections: [" + ", ".join(f"'{v}'" for v in block["sections"]) + "]")
        front += NUDGE + "translation:\n" + "".join(f"  {line}\n" for line in lines)
    return f"---\n{front}---\n{body}"


def seed_page(root: Path, lang: Language, page: str, translate_text: Translate,
              translate_string: Translate, today: str | None = None) -> list[str]:
    """Write content/<lang>/<page>; returns messages about sections kept in English."""
    today = today or date.today().isoformat()
    terms = protected.load_terms(root)
    en_path = root / "content" / "en" / page
    en_meta, en_body = split_front_matter(en_path.read_text(encoding="utf-8"))
    kept = []
    meta = {}
    for key, value in en_meta.items():
        if key in TRANSLATED and isinstance(value, str) and value.strip():
            text, ok = translate_section(value, lang, translate_string, terms)
            meta[key] = text.strip() if ok else value
            if not ok:
                kept.append(f"front matter {key!r} kept in English")
        else:
            meta[key] = value
    parts, translated = [], [str(meta.get("title", ""))]
    for number, section in enumerate(sections(en_body), 1):
        text, ok = translate_section(section, lang, translate_text, terms, "\n".join(translated).strip())
        parts.append(text)
        if ok:
            translated.append(text)
        if not ok:
            kept.append(f"section {number} kept in English")
    body = "".join(parts)
    meta["translation"] = translation_block(en_path, en_meta, en_body, today)
    target = root / "content" / lang.key / page
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(render(meta, body).encode("utf-8"))
    return kept


def seed_page_whole(root: Path, lang: Language, page: str, translate_page: TranslatePage,
                    translate_text: Translate, translate_string: Translate, today: str | None = None) -> list[str]:
    """Write content/<lang>/<page> from one call for the whole page.

    A front matter field or section that fails its check is translated again on
    its own, as seed_page does; returns messages about what was redone or kept in English."""
    today = today or date.today().isoformat()
    terms = protected.load_terms(root)
    en_path = root / "content" / "en" / page
    en_meta, en_body = split_front_matter(en_path.read_text(encoding="utf-8"))
    fields = {k: v for k, v in en_meta.items() if k in TRANSLATED and isinstance(v, str) and v.strip()}
    meta_out, body_out = {}, ""
    try:
        meta_out, body_out = split_front_matter(translate_page(render(fields, en_body), lang).strip() + "\n")
    except Exception:
        pass
    kept, meta = [], {}
    for key, value in en_meta.items():
        if key not in fields:
            meta[key] = value
            continue
        text = meta_out.get(key)
        if isinstance(text, str) and faithful(value, text, terms):
            meta[key] = text.strip()
            continue
        text, ok = translate_section(value, lang, translate_string, terms)
        meta[key] = text.strip() if ok else value
        if not ok:
            kept.append(f"front matter {key!r} kept in English")
    en_parts, out_parts = sections(en_body), sections(body_out.lstrip("\n"))
    if len(out_parts) != len(en_parts):
        out_parts = [""] * len(en_parts)
    parts = []
    for number, (en, text) in enumerate(zip(en_parts, out_parts), 1):
        lead = en[: len(en) - len(en.lstrip("\n"))]
        trail = en[len(en.rstrip("\n")):]
        if faithful(en.strip("\n"), text.strip("\n"), terms) or not en.strip():
            parts.append(lead + text.strip("\n") + trail if en.strip() else en)
            continue
        text, ok = translate_section(en, lang, translate_text, terms, "".join(parts).strip())
        parts.append(text)
        kept.append(f"section {number} " + ("translated again on its own" if ok else "kept in English"))
    meta["translation"] = translation_block(en_path, en_meta, en_body, today)
    target = root / "content" / lang.key / page
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(render(meta, "".join(parts)).encode("utf-8"))
    return kept


def seed_page_changed(root: Path, lang: Language, page: str, translate_text: Translate,
                      translate_string: Translate, today: str | None = None) -> list[str] | None:
    """Update a stale machine page in place: translate only what changed in English.

    Returns messages about the sections and fields translated again, or None when
    the page has no usable record of its English (then translate it whole)."""
    target = root / "content" / lang.key / page
    if not target.is_file():
        return None
    meta, body = split_front_matter(target.read_text(encoding="utf-8"))
    block = meta.get("translation") if isinstance(meta.get("translation"), dict) else {}
    old_fields, old_parts = block.get("fields"), block.get("sections")
    if block.get("status") != "ai" or not isinstance(old_fields, dict) or not isinstance(old_parts, list):
        return None
    done_parts = sections(body)
    if len(done_parts) != len(old_parts):
        return None
    today = today or date.today().isoformat()
    terms = protected.load_terms(root)
    en_path = root / "content" / "en" / page
    en_meta, en_body = split_front_matter(en_path.read_text(encoding="utf-8"))
    new_fields, new_parts = fingerprint(en_meta, en_body)
    done: dict[str, list[str]] = {}
    for h, text in zip(old_parts, done_parts):
        done.setdefault(h, []).append(text)
    notes, out = [], {}
    for key, value in en_meta.items():
        if key not in new_fields:
            out[key] = value
        elif old_fields.get(key) == new_fields[key] and isinstance(meta.get(key), str):
            out[key] = meta[key]
        else:
            text, ok = translate_section(value, lang, translate_string, terms)
            out[key] = text.strip() if ok else value
            notes.append(f"front matter {key!r} " + ("translated again" if ok else "kept in English"))
    parts = []
    for number, (en, h) in enumerate(zip(sections(en_body), new_parts), 1):
        if done.get(h):
            parts.append(done[h].pop(0))
            continue
        text, ok = translate_section(en, lang, translate_text, terms, "".join(parts).strip())
        parts.append(text)
        notes.append(f"section {number} " + ("translated again" if ok else "kept in English"))
    out["translation"] = translation_block(en_path, en_meta, en_body, today)
    target.write_bytes(render(out, "".join(parts)).encode("utf-8"))
    return notes


def plan(root: Path, lang: Language, reseed_ai: bool, only: set[str] | None = None) -> list[str]:
    """English pages this language should (re)translate."""
    todo = []
    for page, path in content_pages(root, "en").items():
        if only and page not in only:
            continue
        if needs_seeding(root / "content" / lang.key / page, source_hash(path), reseed_ai):
            todo.append(page)
    return todo


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--langs", help="comma-separated language keys (default: all)")
    parser.add_argument("--pages", help="comma-separated pages, as in content/en/ (default: all)")
    parser.add_argument("--reseed-ai", action="store_true", help="also redo current machine pages")
    parser.add_argument("--dry-run", action="store_true", help="list pages to seed, call nothing")
    args = parser.parse_args(argv)
    wanted = set(args.langs.split(",")) if args.langs else None
    only = set(args.pages.split(",")) if args.pages else None
    targets = [l for l in languages(ROOT) if l.key != "en" and (wanted is None or l.key in wanted)]
    if args.dry_run:
        for lang in targets:
            print(f"{lang.key}: {', '.join(plan(ROOT, lang, args.reseed_ai, only)) or 'nothing to do'}")
        return 0
    import llm
    config = llm.Config.from_env()
    translate_text, translate_string = llm.translator(config, "page"), llm.translator(config, "string")
    whole = llm.page_translator(config) if config.model.startswith("claude-") else None
    for lang in targets:
        for page in plan(ROOT, lang, args.reseed_ai, only):
            kept = None if args.reseed_ai else seed_page_changed(ROOT, lang, page, translate_text, translate_string)
            if kept is None and whole:
                kept = seed_page_whole(ROOT, lang, page, whole, translate_text, translate_string)
            elif kept is None:
                kept = seed_page(ROOT, lang, page, translate_text, translate_string)
            print(f"{lang.key}/{page}: written" + (f", {len(kept)} note(s)" if kept else ""), flush=True)
            for message in kept:
                print(f"  {message}")
    if config.model.startswith("claude-"):
        print(f"spent: {llm.spent()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
