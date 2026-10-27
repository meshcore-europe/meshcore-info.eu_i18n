#!/usr/bin/env python3
"""Reviewed translations stay reviewed (spec section 6.3, enforced in CI).

Compares the working tree with the point where it branched off a base git
ref (the merge base with the PR's target branch, so reviews merged into the
target later do not count) and fails when a change would undo a native
speaker's review:
- a plain-string (human) value in data/i18n/<lang>.json became an _ai
  object, null, or disappeared while en.json still has the key;
- a content/<lang>/ page with translation.status human lost that status,
  or was deleted while its English source still exists.

Editing reviewed text by hand is fine: it stays a plain string or a
status: human page. The seeders never do any of the above; this is the
backstop that keeps a regression from merging.

Usage: check_human_protection.py --base origin/main
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from common import ROOT, Problem, content_pages, is_ai, languages, load_json, report, split_front_matter


def git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, encoding="utf-8")


def at_base(root: Path, base: str, path: str) -> str | None:
    result = git(root, "show", f"{base}:{path}")
    return result.stdout if result.returncode == 0 else None


def is_human_page(text: str | None) -> bool:
    if text is None:
        return False
    try:
        meta, _ = split_front_matter(text)
    except ValueError:
        return False
    block = meta.get("translation")
    return isinstance(block, dict) and block.get("status") == "human"


def string_problems(root: Path, base: str, lang: str, en: dict, base_files: set[str]) -> list[Problem]:
    path = f"data/i18n/{lang}.json"
    if path not in base_files:
        return []
    before = json.loads(at_base(root, base, path) or "{}")
    now = load_json(root / path) if (root / path).is_file() else {}
    found = []
    for key, value in before.items():
        if key == "_meta" or not isinstance(value, str) or key not in en:
            continue
        entry = now.get(key)
        if isinstance(entry, str):
            continue
        what = "machine text" if is_ai(entry) else "nothing"
        found.append(Problem(path, f"{key}: reviewed string was replaced by {what}"))
    return found


def page_problems(root: Path, base: str, lang: str, en_pages: set[str], base_files: set[str]) -> list[Problem]:
    now = content_pages(root, lang)
    found = []
    for path in sorted(f for f in base_files if f.startswith(f"content/{lang}/") and f.endswith(".md")):
        page = path.removeprefix(f"content/{lang}/")
        if page not in en_pages or not is_human_page(at_base(root, base, path)):
            continue
        if page not in now:
            found.append(Problem(path, "reviewed translation was deleted"))
        elif not is_human_page(now[page].read_text(encoding="utf-8")):
            found.append(Problem(path, "reviewed translation lost translation.status human"))
    return found


def check(root: Path = ROOT, base: str = "origin/main") -> list[Problem]:
    if git(root, "rev-parse", "--verify", "--quiet", f"{base}^{{commit}}").returncode != 0:
        raise SystemExit(f"base ref {base!r} not found; fetch it first")
    fork = git(root, "merge-base", base, "HEAD").stdout.strip()
    base = fork or base
    en = load_json(root / "data" / "i18n" / "en.json")
    en_pages = set(content_pages(root, "en"))
    base_files = set(git(root, "ls-tree", "-r", "--name-only", base, "--", "data/i18n", "content").stdout.splitlines())
    found = []
    for lang in (l.key for l in languages(root) if l.key != "en"):
        found += string_problems(root, base, lang, en, base_files)
        found += page_problems(root, base, lang, en_pages, base_files)
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base", required=True, help="git ref to compare with, such as origin/main")
    args = parser.parse_args(argv)
    return report(check(base=args.base), "reviewed translations intact")


if __name__ == "__main__":
    sys.exit(main())
