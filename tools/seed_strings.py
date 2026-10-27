#!/usr/bin/env python3
"""Seed data/i18n/<lang>.json from en.json with a local LLM (spec section 6.3).

Fills strings that are missing or null, and machine strings whose English
changed since they were seeded (their _source no longer matches the English
string); with --reseed-ai also replaces every other machine string
({"value", "_ai": true}). Never touches a plain string: that is a human
translation. A claude-* model gets the strings in
batches of 200 per request (measured on 200 nl strings, 26 October 2026:
5,700 input tokens against 13,700 in batches of 40, the same grader
findings; one request per string costs about 10 times more); a local model gets one string per request. A translation that changes the
{placeholders}, drops a protected term or alters a radio value is skipped
and stays untranslated, so bad output never reaches the file. Written
entries are {"value": ..., "_ai": true, "_seeded": today, "_source": hash}.

Usage:
  seed_strings.py [--langs nl,de] [--keys 'hero_*,device.*'] [--reseed-ai] [--limit N] [--dry-run]
  (endpoint and model: see tools/llm.py)
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import sys
from collections import Counter
from collections.abc import Callable
from datetime import date
from pathlib import Path

import protected
from common import ROOT, Language, is_ai, languages, load_json
from source_hash import string_hash
from validate_i18n import placeholders

Translate = Callable[[str, Language], str]
TranslateBatch = Callable[[dict[str, str], Language], dict[str, str]]
BATCH = 200


def matches(key: str, patterns: list[str] | None) -> bool:
    return not patterns or any(fnmatch.fnmatchcase(key, p) for p in patterns)


def pending(en: dict, data: dict, reseed_ai: bool, patterns: list[str] | None = None) -> list[str]:
    """Keys of en.json this language should (re)translate; patterns limit them (shell globs)."""
    keys = []
    for key, source in en.items():
        if key == "_meta" or not isinstance(source, str) or not matches(key, patterns):
            continue
        entry = data.get(key)
        if entry is None or (is_ai(entry) and (reseed_ai or stale(entry, source))):
            keys.append(key)
    return keys


def stale(entry: dict, source: str) -> bool:
    """A machine string seeded from older English; one without _source predates the hash and counts as current."""
    return "_source" in entry and entry["_source"] != string_hash(source)


def check(source: str, text: str, terms: list[str]) -> list[str]:
    found = []
    if not text.strip():
        found.append("empty")
    if Counter(placeholders(text)) != Counter(placeholders(source)):
        found.append("placeholders changed")
    return found + protected.problems(source, text, terms)


def batched(translate_batch: TranslateBatch, size: int = BATCH):
    """Turn a batch translator into the per-key results seed_language needs."""
    def results(texts: dict[str, str], lang: Language) -> dict[str, str | Exception]:
        out: dict[str, str | Exception] = {}
        keys = list(texts)
        for i in range(0, len(keys), size):
            chunk = {k: texts[k] for k in keys[i:i + size]}
            try:
                answer = translate_batch(chunk, lang)
            except Exception as e:  # endpoint trouble: leave the chunk for the next run
                out.update({k: e for k in chunk})
                continue
            out.update({k: answer.get(k, ValueError("missing from the answer")) for k in chunk})
        return out
    return results


def one_by_one(translate: Translate):
    def results(texts: dict[str, str], lang: Language) -> dict[str, str | Exception]:
        out: dict[str, str | Exception] = {}
        for key, text in texts.items():
            try:
                out[key] = translate(text, lang)
            except Exception as e:  # endpoint trouble: leave it for the next run
                out[key] = e
        return out
    return results


def seed_language(root: Path, lang: Language, translate: Translate, reseed_ai: bool = False,
                  limit: int | None = None, today: str | None = None,
                  translate_batch: TranslateBatch | None = None,
                  patterns: list[str] | None = None) -> tuple[int, list[str]]:
    """Translate one language's pending strings; returns (written, skipped messages).

    With translate_batch, the strings go in batches of BATCH per request."""
    today = today or date.today().isoformat()
    en = load_json(root / "data" / "i18n" / "en.json")
    path = root / "data" / "i18n" / f"{lang.key}.json"
    data = load_json(path)
    terms = protected.load_terms(root)
    keys = pending(en, data, reseed_ai, patterns)[:limit]
    written, skipped = 0, []
    results = (batched(translate_batch) if translate_batch else one_by_one(translate))({k: en[k] for k in keys}, lang)
    for key in keys:
        text = results[key]
        if isinstance(text, Exception):
            skipped.append(f"{key}: endpoint error {text}")
            continue
        problems = check(en[key], text, terms)
        if problems:
            skipped.append(f"{key}: {'; '.join(problems)}")
            continue
        data[key] = {"value": text, "_ai": True, "_seeded": today, "_source": string_hash(en[key])}
        written += 1
    if written:
        data["_meta"]["updated"] = today
        ordered = {"_meta": data["_meta"]}
        ordered.update({k: data[k] for k in en if k in data and k != "_meta"})
        ordered.update({k: v for k, v in data.items() if k not in ordered})
        path.write_bytes((json.dumps(ordered, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    return written, skipped


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--langs", help="comma-separated language keys (default: all)")
    parser.add_argument("--keys", help="comma-separated key patterns such as 'hero_*,device.*' (default: all)")
    parser.add_argument("--reseed-ai", action="store_true", help="also replace current machine strings")
    parser.add_argument("--limit", type=int, help="at most N strings per language")
    parser.add_argument("--dry-run", action="store_true", help="count pending strings, call nothing")
    args = parser.parse_args(argv)
    wanted = set(args.langs.split(",")) if args.langs else None
    patterns = args.keys.split(",") if args.keys else None
    targets = [l for l in languages(ROOT) if l.key != "en" and (wanted is None or l.key in wanted)]
    en = load_json(ROOT / "data" / "i18n" / "en.json")
    if args.dry_run:
        for lang in targets:
            data = load_json(ROOT / "data" / "i18n" / f"{lang.key}.json")
            print(f"{lang.key}: {len(pending(en, data, args.reseed_ai, patterns)[:args.limit])} pending")
        return 0
    import llm
    config = llm.Config.from_env()
    translate = llm.translator(config, "string")
    translate_batch = llm.batch_translator(config) if config.model.startswith("claude-") else None
    for lang in targets:
        written, skipped = seed_language(ROOT, lang, translate, args.reseed_ai, args.limit,
                                         translate_batch=translate_batch, patterns=patterns)
        print(f"{lang.key}: wrote {written}, skipped {len(skipped)}", flush=True)
        for message in skipped:
            print(f"  skipped {message}")
    if config.model.startswith("claude-"):
        print(f"spent: {llm.spent()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
