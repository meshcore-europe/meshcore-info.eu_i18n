#!/usr/bin/env python3
"""The judge for translations, where a search rule cannot decide (issue #55).

Asks a model whether a translation keeps the meaning of its English source
and reads as if written in its language (docs/design/ui-copy.md section 7),
and scores both from 1 to 5. tools/grade_copy.py covers every rule a search
can decide; this judge covers the rest: a fact dropped or changed, a term
no longer explained on first use, a limit that became vague, a companion
that pairs over Bluetooth only.

The judge runs through tools/llm.py. By default it is Claude Opus
(claude-opus-5-5), not the Claude Fable that translates, so the
translator does not grade its own work.

  JUDGE_MODEL   model id (default claude-opus-5-5)
  JUDGE_EFFORT  effort (default medium)

Usage:
  judge.py --langs nl,de [--pages about.md] [--strings N] [--ai] [--json FILE]

--strings N judges N strings per language, the same N in every language
(a fixed spread over en.json), in batches of 40.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

import llm
from common import ROOT, languages
from grade_copy import Unit, units

BATCH = 40

SYSTEM = (
    "You review translations for meshcore-info.eu, a non-commercial community website about "
    "MeshCore, a LoRa radio mesh messaging system. English is the source. You compare a "
    "translation with its English source and score two things from 1 to 5.\n"
    "meaning: does the translation say what the English says?\n"
    "  5 every fact, number, limit, condition and actor kept, nothing added\n"
    "  4 one nuance weakened, no fact wrong\n"
    "  3 one fact dropped, added or changed\n"
    "  2 several facts dropped, added or changed\n"
    "  1 a different message\n"
    "Check in particular: a number the English gives exactly stays exact (no 'about'); where the "
    "English explains companion, repeater, room server or observer, the translation explains it "
    "there too; a companion pairs with a phone or a laptop, over Bluetooth or USB, wherever the "
    "English says so.\n"
    "natural: does it read as if it was written in the target language?\n"
    "  5 a native writer would write it like this: informal address to one person, short "
    "sentences, the usual words for the domain\n"
    "  4 correct, one phrase reads translated\n"
    "  3 several phrases read translated, or the address is formal\n"
    "  2 hard to read, word-for-word\n"
    "  1 wrong language or broken\n"
    "Markdown, link targets, code and shortcodes are checked elsewhere: ignore them. Do not "
    "score style rules the English itself breaks. Radio values keep the English notation on "
    "purpose (869.618 MHz, not 869,618 MHz), and the glossary translations are agreed: do not "
    "flag either.\n"
    "Answer with JSON only, no prose around it."
)

PAGE_FORMAT = ('{"meaning": n, "natural": n, "issues": [{"quote": "<translated words>", '
               '"problem": "<what is wrong, in English>"}]}')
STRING_FORMAT = ('{"scores": {"<key>": [meaning, natural], ...}, "issues": [{"key": "<key>", '
                 '"problem": "<what is wrong, in English>"}]}')


@dataclass
class Verdict:
    lang: str
    unit: str
    meaning: float
    natural: float
    issues: list[dict] = field(default_factory=list)


def config() -> llm.Config:
    return llm.Config("", os.environ.get("JUDGE_MODEL", "claude-opus-5-5"), 0.0,
                      float(os.environ.get("LLM_TIMEOUT", "600")), os.environ.get("JUDGE_EFFORT", "medium"))


def parse(answer: str) -> dict:
    """The JSON object in the judge's answer, even inside a code fence."""
    match = re.search(r"\{.*\}", answer, re.S)
    if not match:
        raise ValueError(f"no JSON in the judge's answer: {answer[:200]!r}")
    return json.loads(match.group(0))


def page_request(unit: Unit, lang_name: str) -> str:
    return (f"Target language: {lang_name}\nFormat: {PAGE_FORMAT}\n\n"
            f"English page:\n{unit.source}\n\nTranslated page:\n{unit.text}\n")


def strings_request(batch: list[Unit], lang_name: str) -> str:
    pairs = {u.id.split(":", 1)[1]: {"en": u.source, "translation": u.text} for u in batch}
    return (f"Target language: {lang_name}\nFormat: {STRING_FORMAT}\n"
            "Score every key. The strings are interface text: labels, buttons and short descriptions.\n\n"
            + json.dumps(pairs, ensure_ascii=False, indent=1))


def judge_page(cfg: llm.Config, unit: Unit, ask=llm.chat) -> Verdict:
    answer = parse(ask(cfg, SYSTEM, page_request(unit, llm.LANG_NAMES[unit.lang])))
    return Verdict(unit.lang, unit.id, float(answer["meaning"]), float(answer["natural"]), answer.get("issues", []))


def judge_strings(cfg: llm.Config, batch: list[Unit], ask=llm.chat) -> list[Verdict]:
    lang = batch[0].lang
    answer = parse(ask(cfg, SYSTEM, strings_request(batch, llm.LANG_NAMES[lang])))
    issues: dict[str, list[dict]] = {}
    for issue in answer.get("issues", []):
        issues.setdefault(str(issue.get("key")), []).append(issue)
    verdicts = []
    for u in batch:
        key = u.id.split(":", 1)[1]
        meaning, natural = answer["scores"].get(key, [None, None])
        if meaning is not None:
            verdicts.append(Verdict(lang, u.id, float(meaning), float(natural), issues.get(key, [])))
    return verdicts


def spread(strings: list[Unit], n: int) -> list[Unit]:
    """n strings chosen by a hash of their key, so every language gets the same keys."""
    key = lambda u: hashlib.sha256(u.id.split(":", 1)[1].encode()).hexdigest()
    return sorted(strings, key=key)[:n]


def summary(verdicts: list[Verdict]) -> str:
    rows = ["| lang | units | meaning | natural | issues |", "| --- | --- | --- | --- | --- |"]
    for lang in dict.fromkeys(v.lang for v in verdicts):
        vs = [v for v in verdicts if v.lang == lang]
        rows.append(f"| {lang} | {len(vs)} | {sum(v.meaning for v in vs) / len(vs):.2f} | "
                    f"{sum(v.natural for v in vs) / len(vs):.2f} | {sum(len(v.issues) for v in vs)} |")
    return "\n".join(rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--langs", help="comma-separated language keys (default: every translation)")
    parser.add_argument("--pages", default="", help="comma-separated pages, as in content/en/")
    parser.add_argument("--strings", type=int, default=0, help="judge N strings per language")
    parser.add_argument("--ai", action="store_true", help="only machine translations")
    parser.add_argument("--json", type=Path, help="write every verdict to this file")
    args = parser.parse_args(argv)
    keys = args.langs.split(",") if args.langs else [l.key for l in languages(ROOT) if l.key != "en"]
    pages = set(filter(None, args.pages.split(",")))
    cfg = config()
    verdicts: list[Verdict] = []
    for lang in keys:
        if pages:
            for unit in units(ROOT, lang, "pages", args.ai, pages):
                verdicts.append(judge_page(cfg, unit))
                print(f"{unit.id}: meaning {verdicts[-1].meaning}, natural {verdicts[-1].natural}", flush=True)
        chosen = spread(units(ROOT, lang, "strings", args.ai), args.strings) if args.strings else []
        for i in range(0, len(chosen), BATCH):
            verdicts += judge_strings(cfg, chosen[i:i + BATCH])
        if chosen:
            print(f"{lang}: {len(chosen)} strings judged", flush=True)
    print(summary(verdicts))
    print(f"spent: ${llm.spent_usd:.2f}")
    if args.json:
        args.json.write_text(json.dumps([asdict(v) for v in verdicts], ensure_ascii=False, indent=1) + "\n",
                             encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
