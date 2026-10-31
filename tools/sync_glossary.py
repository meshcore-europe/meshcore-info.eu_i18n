#!/usr/bin/env python3
"""Sync glossary/<lang>.tsv from kiekr-i18n, and validate glossaries (spec 6.5).

kiekr-i18n (github.com/marcelverdult/kiekr-i18n) keeps one TSV per
language: two tab-separated columns (English term, translation), no
header. For each non-English language in hugo.toml this tool looks for
an upstream file named after the language's locale, then its key
(pt-PT.tsv, then pt.tsv), and copies it verbatim to glossary/<key>.tsv.
Languages kiekr lacks keep their local file; new terms for them are
offered upstream by pull request, so a later sync replaces the local copy.

glossary/site/<lang>.tsv holds the terms only this site uses (antenna and
clock words, for example), in the same format, so kiekr-i18n can take a
file over as it is. A site term must not repeat a term of glossary/<lang>.tsv:
then the two files join into one without a conflict. rows() gives both.

Usage:
  sync_glossary.py           write upstream glossaries into glossary/
  sync_glossary.py --check   exit 1 if a synced file differs from upstream
  sync_glossary.py --validate  check the local files' format only (no network)
"""

from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from collections.abc import Callable
from pathlib import Path

from common import ROOT, Language, Problem, languages, rel, report

UPSTREAM = "https://raw.githubusercontent.com/marcelverdult/kiekr-i18n/main/glossary/{name}.tsv"
TIMEOUT_S = 30


def fetch(url: str) -> str | None:
    """The file at url, or None when it does not exist (HTTP 404)."""
    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT_S) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def parse(text: str) -> list[tuple[str, str]]:
    """Rows of a glossary TSV; ValueError names the first bad line."""
    rows, seen = [], set()
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        cells = line.split("\t")
        if len(cells) != 2 or not cells[0].strip() or not cells[1].strip():
            raise ValueError(f"line {number}: expected 'English term<TAB>translation'")
        term = cells[0].strip().lower()
        if term in seen:
            raise ValueError(f"line {number}: term {cells[0]!r} appears twice")
        seen.add(term)
        rows.append((cells[0], cells[1]))
    return rows


def rows(lang: str, root: Path = ROOT) -> list[tuple[str, str]]:
    """The glossary of a language: the shared terms, then the site's own."""
    found = []
    for path in (root / "glossary" / f"{lang}.tsv", root / "glossary" / "site" / f"{lang}.tsv"):
        if path.is_file():
            found += parse(path.read_text(encoding="utf-8"))
    return found


def upstream_names(lang: Language) -> list[str]:
    return list(dict.fromkeys([lang.locale, lang.key]))


def validate(root: Path = ROOT) -> list[Problem]:
    keys = {l.key for l in languages(root) if l.key != "en"}
    found = []
    for path in sorted((root / "glossary").glob("*.tsv")) + sorted((root / "glossary" / "site").glob("*.tsv")):
        name = rel(path, root)
        if path.stem not in keys:
            found.append(Problem(name, f"{path.stem!r} is not a translated language in hugo.toml"))
            continue
        try:
            terms = parse(path.read_text(encoding="utf-8"))
        except ValueError as e:
            found.append(Problem(name, str(e)))
            continue
        shared = root / "glossary" / f"{path.stem}.tsv"
        if path.parent.name == "site" and shared.is_file():
            try:
                both = {en.lower() for en, _ in parse(shared.read_text(encoding="utf-8"))} & {en.lower() for en, _ in terms}
            except ValueError:
                both = set()
            found += [Problem(name, f"term {t!r} is in {rel(shared, root)} too; keep it in one file") for t in sorted(both)]
    return found


def sync(root: Path = ROOT, check: bool = False,
         get: Callable[[str], str | None] = fetch) -> list[Problem]:
    found = []
    for lang in languages(root):
        if lang.key == "en":
            continue
        target = root / "glossary" / f"{lang.key}.tsv"
        name = rel(target, root)
        for upstream in upstream_names(lang):
            text = get(UPSTREAM.format(name=upstream))
            if text is not None:
                break
        else:
            print(f"{name}: local (kiekr-i18n has no {lang.locale} glossary)")
            continue
        try:
            parse(text)
        except ValueError as e:
            found.append(Problem(name, f"upstream {upstream}.tsv is invalid: {e}"))
            continue
        current = target.read_bytes().decode("utf-8") if target.is_file() else None
        if current == text:
            print(f"{name}: up to date with kiekr-i18n {upstream}.tsv")
        elif check:
            found.append(Problem(name, f"differs from kiekr-i18n {upstream}.tsv; run tools/sync_glossary.py"))
        else:
            target.parent.mkdir(exist_ok=True)
            target.write_bytes(text.encode("utf-8"))
            print(f"{name}: updated from kiekr-i18n {upstream}.tsv")
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="report drift instead of writing")
    parser.add_argument("--validate", action="store_true", help="only check the local files' format, offline")
    args = parser.parse_args(argv)
    if args.validate:
        return report(validate(), "glossaries ok")
    return report(sync(check=args.check), "glossaries in sync" if args.check else "glossaries synced")


if __name__ == "__main__":
    sys.exit(main())
