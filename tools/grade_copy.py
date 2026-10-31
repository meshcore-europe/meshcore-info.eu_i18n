#!/usr/bin/env python3
"""Search-rule graders for visitor text, per language (issue #55 step 1).

Holds every string in data/i18n/<lang>.json and every page in
content/<lang>/ to the rules of docs/design/ui-copy.md that a search can
decide. The word lists per language are in tools/copy_rules.py; whether a
translation keeps the meaning of its source is for tools/judge.py.

A translation is compared with its English source: a rule counts only what
the translation adds over the English (a long sentence that is long in
English too is the source's, not the translator's). English itself is
graded on its own counts.

Rules, hard (a translation must have none) and soft (count, compare with
the baseline):

  hard  em-dash        the character U+2014
  hard  broken-word    a word split over 2 lines with a hyphen ("MIT-" and
                       "licentie"), which renders as "MIT- licentie"
  hard  address        formal or plural address (section 2)
  hard  placeholders   {placeholders} of a string, structure of a page
                       (tools/parity.py)
  hard  protected      glossary/protected.txt terms and radio values
                       (tools/protected.py)
  hard  numbers        every number of the English source, none added
  hard  approx         "about" before a number the English gives exactly
  hard  abbreviations  LoRa, MQTT, USB, ... kept as written
  hard  never          Meshcore, ISM band, internal terms (sections 3, 8, 9)
  hard  exclamation    no exclamation marks (section 2)
  soft  sentence       a sentence over 25 words (section 1: 10 to 15)
  soft  paragraph      a paragraph over 100 words or 10 sentences
  soft  glossary       a glossary term of the English missing (section 8)
  soft  count-list     a count sentence or heading before a list (section 6)
  soft  negation       doubled negation (section 9)
  soft  filler         filler, sales and generated-text words (section 3)
  soft  polite         politeness filler and apologies (section 3)
  soft  do-not-use     the "Do not use" column of section 8

The table also counts the stale pages: translated before their English
changed, so their numbers, links and structure lag behind the source.

Usage:
  grade_copy.py [--langs nl,de] [--pages about.md] [--keys 'hero_*'] [--kind strings|pages]
                [--ai] [--since REF] [--details] [--json FILE] [--check]

--ai grades only machine translations (_ai strings, status ai pages).
--since REF grades only what changed since REF (its merge base with HEAD):
the changed pages and the strings whose entry changed. The CI of the
translations repository runs it on every pull request.
--check exits 1 when a hard rule fails.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path

import copy_rules as R
import parity
import protected
import sync_glossary
from source_hash import source_hash
from common import (ROOT, content_pages, is_ai, languages, load_json, split_front_matter,
                    string_value)
from validate_i18n import placeholders
from validate_pages import TRANSLATED

HARD = ["em-dash", "broken-word", "address", "placeholders", "protected", "numbers", "approx", "abbreviations", "never",
        "exclamation"]
SOFT = ["sentence", "paragraph", "glossary", "count-list", "negation", "filler", "polite", "do-not-use"]
LONG_SENTENCE = 25
LONG_PARAGRAPH_WORDS = 100
LONG_PARAGRAPH_SENTENCES = 10

WORD = re.compile(r"\w(?:[\w'’.,\-]*\w)?")
NUMBER = re.compile(r"\d+(?:[.,]\d+)*")
SENTENCE_END = re.compile(r"(?<=[.!?…])[\"”»’)]*\s+")
# Abbreviations that end in a full stop without ending the sentence.
ABBREVIATION = re.compile(r"(?:\b\w\.){2,}$|\b(?:ca|cca|kb|ok|bzw|vs|etc|nr|no|approx|incl|max|min|z|n|vgl|zB)\.$",
                          re.I)
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
TABLE_ROW = re.compile(r"^\s*\|")
HEADING = re.compile(r"^\s*#{1,6}\s+")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


@dataclass
class Unit:
    lang: str
    kind: str          # "string" or "page"
    id: str            # data/i18n/nl.json:key or content/nl/about.md
    source: str        # the English, raw (string value or whole page file)
    text: str          # the translation, raw; for English the English again
    stale: bool = False  # a page whose English changed after it was translated


@dataclass
class Finding:
    unit: str
    rule: str
    message: str


@dataclass
class Grade:
    lang: str
    units: int = 0
    words: int = 0
    sentences: int = 0
    stale: int = 0
    counts: Counter = field(default_factory=Counter)
    findings: list[Finding] = field(default_factory=list)

    @property
    def hard(self) -> int:
        return sum(self.counts[r] for r in HARD)

    @property
    def soft(self) -> int:
        return sum(self.counts[r] for r in SOFT)


# --- prose --------------------------------------------------------------

@dataclass
class Block:
    kind: str          # "paragraph", "heading", "item", "row"
    text: str
    list_id: int = -1  # items of one list share an id


def page_prose(raw: str) -> tuple[str, str]:
    """(visible text, Markdown body) of a page file; front matter fields first."""
    meta, body = split_front_matter(raw)
    head = "\n\n".join(str(meta[k]) for k in TRANSLATED if isinstance(meta.get(k), str))
    return head + "\n\n" + body, body


def strip_markup(text: str) -> str:
    """Markdown and HTML reduced to the words a visitor reads."""
    lines, fence = [], None
    for line in text.split("\n"):
        m = parity.FENCE.match(line)
        if fence is None and m:
            fence = m.group(1)
            continue
        if fence is not None:
            if m and m.group(1)[0] == fence[0]:
                fence = None
            continue
        lines.append(line)
    text = "\n".join(lines)
    text = parity.SHORTCODE.sub(" ", text)
    text = parity.INLINE_CODE.sub("code", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\{#[\w-]+\}", "", text)
    text = re.sub(r"<[^>\n]+>", " ", text)
    text = re.sub(r"(?<![\w])(?:https?://|www\.)\S+", " ", text)
    text = re.sub(r"[*_]{1,3}(?=\S)|(?<=\S)[*_]{1,3}", "", text)
    return text


def blocks(text: str) -> list[Block]:
    """Paragraphs, headings, list items and table rows of visible text."""
    out: list[Block] = []
    para: list[str] = []
    list_id, in_list = 0, False

    def flush():
        if para:
            out.append(Block("paragraph", " ".join(para)))
            para.clear()

    for line in strip_markup(text).split("\n"):
        if not line.strip():
            flush()
            continue
        if HEADING.match(line):
            flush()
            in_list = False
            out.append(Block("heading", HEADING.sub("", line).strip()))
        elif LIST_ITEM.match(line):
            flush()
            if not in_list:
                list_id += 1
                in_list = True
            out.append(Block("item", LIST_ITEM.sub("", line).strip(), list_id))
        elif TABLE_ROW.match(line):
            flush()
            in_list = False
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                out += [Block("row", c) for c in cells if c]
        elif out and out[-1].kind == "item" and not para and line.startswith((" ", "\t")):
            out[-1].text += " " + line.strip()
        else:
            if para == [] and in_list and out and out[-1].kind == "item":
                in_list = False
            para.append(line.strip())
    flush()
    return out


def sentences(text: str) -> list[str]:
    found, current = [], ""
    for part in SENTENCE_END.split(text.strip()):
        current = f"{current} {part}".strip() if current else part
        if not ABBREVIATION.search(current):
            found.append(current)
            current = ""
    if current:
        found.append(current)
    return [s for s in found if WORD.search(s)]


def words(text: str) -> list[str]:
    return WORD.findall(text)


# --- rules ----------------------------------------------------------------

def compiled(patterns: list[str], flags=re.I) -> list[re.Pattern]:
    return [re.compile(p, flags) for p in patterns]


def count_patterns(text: str, patterns: list[re.Pattern]) -> list[str]:
    return [m.group(0) for p in patterns for m in p.finditer(text)]


def mid_sentence(text: str, start: int) -> bool:
    before = text[:start].rstrip(" \t*_\"'„“«(-")
    return bool(before) and before[-1] not in ".!?:\n#|"


def address_hits(text: str, lang: str) -> list[str]:
    hits = []
    for pattern in R.ADDRESS.get(lang, ("", []))[1]:
        if pattern.startswith("MID:"):
            hits += [m.group(0) for m in re.finditer(pattern[4:], text) if mid_sentence(text, m.start())]
        else:
            hits += [m.group(0) for m in re.finditer(pattern, text, re.I)]
    return hits


def approx_hits(text: str, lang: str) -> list[str]:
    near = [rf"(?:{p})(?:\W+\w+){{0,2}}?\W+[-−+]?\d" for p in R.APPROX.get(lang, [])]
    return count_patterns(text, compiled(near))


def number_set(text: str) -> Counter:
    return Counter(re.sub(r"\D", "", n) for n in NUMBER.findall(text))


def glossary_rows(lang: str, root: Path) -> dict[str, str]:
    rows = dict(R.GUIDE_GLOSSARY.get(lang, {}))
    rows.update({en.lower(): tr for en, tr in sync_glossary.rows(lang, root)})
    return rows


def stem(term: str) -> str:
    """Enough of a glossary word to find it inflected (Knotens, repeaterit)."""
    return term.lower() if len(term) <= 5 else term.lower()[:-2]


def negation_hits(sents: list[str], lang: str) -> list[str]:
    """Sentences that deny twice: two negations a few words apart ("not
    without"), or a denial right after a denial (the section 9 example)."""
    patterns = compiled(R.NEGATION.get(lang, []))
    hits, previous = [], False
    for s in sents:
        spots = sorted({(m.start(), m.group(0).lower()) for p in patterns for m in p.finditer(s)})
        close = any(wa != wb and len(words(s[a:b])) <= 3 and not re.search(r"[,:;]", s[a:b])
                    for (a, wa), (b, wb) in zip(spots, spots[1:]))
        if close or (spots and previous):
            hits.append(s)
        previous = bool(spots)
    return hits


def count_list_hits(bs: list[Block], lang: str) -> list[str]:
    numbers = {w: i + 2 for i, w in enumerate(R.NUMBER_WORDS.get(lang, "").split())}
    sizes = Counter(b.list_id for b in bs if b.kind == "item")
    hits = []
    for i, b in enumerate(bs):
        if b.kind != "item" or (i and bs[i - 1].kind == "item" and bs[i - 1].list_id == b.list_id):
            continue
        if i == 0 or bs[i - 1].kind not in ("paragraph", "heading"):
            continue
        before = bs[i - 1].text.lower()
        if len(words(before)) > 12 and not before.rstrip().endswith(":"):
            continue
        said = {int(n) for n in re.findall(r"(?<![\d.,])\d+(?![\d.,]\d)", before)}
        said |= {v for w, v in numbers.items() if re.search(rf"\b{re.escape(w)}\b", before)}
        if sizes[b.list_id] in said:
            hits.append(bs[i - 1].text)
    return hits


@dataclass
class Measure:
    """Everything the rules count in one text, so source and translation compare."""
    hits: dict[str, list[str]]
    words: int
    sentences: int


def measure(raw: str, kind: str, lang: str) -> Measure:
    visible = page_prose(raw)[0] if kind == "page" else raw
    bs = blocks(visible) if kind == "page" else [Block("paragraph", strip_markup(visible))]
    prose = "\n".join(b.text for b in bs)
    all_sents = [s for b in bs for s in sentences(b.text)]
    hits: dict[str, list[str]] = {}
    hits["em-dash"] = ["\u2014"] * prose.count("\u2014")
    hits["broken-word"] = re.findall(r"\w+-\n[ \t]*\w+", strip_markup(visible)) if kind == "page" else []
    hits["address"] = address_hits(prose, lang)
    hits["approx"] = approx_hits(prose, lang)
    hits["never"] = [m.group(0) for p, _ in R.NEVER for m in re.finditer(p, prose)]
    hits["exclamation"] = re.findall(r"[!¡]", prose) + EMOJI.findall(prose)
    hits["sentence"] = [s for s in all_sents if len(words(s)) > LONG_SENTENCE]
    hits["paragraph"] = [b.text[:60] for b in bs if b.kind == "paragraph"
                         and (len(words(b.text)) > LONG_PARAGRAPH_WORDS
                              or len(sentences(b.text)) > LONG_PARAGRAPH_SENTENCES)]
    hits["count-list"] = count_list_hits(bs, lang)
    hits["negation"] = [s for b in bs for s in negation_hits(sentences(b.text), lang)]
    hits["filler"] = count_patterns(prose, compiled(R.FILLER.get(lang, [])))
    hits["polite"] = count_patterns(prose, compiled(R.POLITE.get(lang, [])))
    hits["do-not-use"] = count_patterns(prose, compiled(R.DO_NOT_USE.get(lang, [])))
    return Measure(hits, len(words(prose)), len(all_sents))


def pair_findings(unit: Unit, terms: list[str], gloss: dict[str, str]) -> list[Finding]:
    """Rules that hold a translation against its English source."""
    found = []
    if unit.kind == "page":
        en_visible, en_body = page_prose(unit.source)
        tr_visible, tr_body = page_prose(unit.text)
        found += [Finding(unit.id, "placeholders", m) for m in parity.compare(en_body, tr_body)]
    else:
        en_visible, tr_visible = unit.source, unit.text
        if Counter(placeholders(en_visible)) != Counter(placeholders(tr_visible)):
            found.append(Finding(unit.id, "placeholders",
                                 f"placeholders {placeholders(tr_visible)} differ from {placeholders(en_visible)}"))
    en_prose, tr_prose = strip_markup(en_visible), strip_markup(tr_visible)
    found += [Finding(unit.id, "protected", m) for m in protected.problems(en_prose, tr_prose, terms)]
    en_n, tr_n = number_set(en_prose), number_set(tr_prose)
    found += [Finding(unit.id, "numbers", f"number {n} of the English is missing") for n in sorted(en_n - tr_n)]
    found += [Finding(unit.id, "numbers", f"number {n} is not in the English") for n in sorted(tr_n - en_n)]
    for abbr in R.ABBREVIATIONS:
        if re.search(rf"\b{abbr}\b", en_prose) and not re.search(rf"\b{abbr}", tr_prose):
            found.append(Finding(unit.id, "abbreviations", f"{abbr} of the English is missing"))
    lower = tr_prose.lower()
    for term, translation in gloss.items():
        if re.search(rf"\b{re.escape(term)}s?\b", en_prose, re.I) and stem(translation) not in lower:
            found.append(Finding(unit.id, "glossary", f"{term!r} should be {translation!r}"))
    return found


def grade_unit(unit: Unit, terms: list[str], gloss: dict[str, str]) -> tuple[Measure, list[Finding]]:
    tr = measure(unit.text, unit.kind, unit.lang)
    if unit.lang == "en":
        return tr, [Finding(unit.id, rule, h) for rule, hs in tr.hits.items() for h in hs]
    en = measure(unit.source, unit.kind, "en")
    found = []
    for rule, hs in tr.hits.items():
        excess = len(hs) - len(en.hits[rule])
        if excess > 0:
            found += [Finding(unit.id, rule, h) for h in hs[-excess:]]
    return tr, found + pair_findings(unit, terms, gloss)


# --- units ----------------------------------------------------------------

def changed_since(root: Path, ref: str, lang: str) -> tuple[set[str], set[str]]:
    """(pages, string keys) of one language that changed since the merge base of ref and HEAD."""
    from check_human_protection import at_base, git
    if git(root, "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}").returncode != 0:
        raise SystemExit(f"ref {ref!r} not found; fetch it first")
    base = git(root, "merge-base", ref, "HEAD").stdout.strip() or ref
    names = git(root, "diff", "--name-only", base, "--", f"content/{lang}").stdout.splitlines()
    names += git(root, "ls-files", "--others", "--exclude-standard", f"content/{lang}").stdout.splitlines()
    pages = {n.split("/", 2)[2] for n in names if n.endswith(".md")}
    path = f"data/i18n/{lang}.json"
    before = json.loads(at_base(root, base, path) or "{}")
    now = load_json(root / path) if (root / path).is_file() else {}
    return pages, {k for k, v in now.items() if k != "_meta" and before.get(k) != v}


def units(root: Path, lang: str, kind: str | None = None, only_ai: bool = False,
          pages: set[str] | None = None, keys: list[str] | None = None) -> list[Unit]:
    """Strings and pages of one language; pages and keys (shell globs) limit them."""
    out = []
    if kind in (None, "strings"):
        en = load_json(root / "data" / "i18n" / "en.json")
        data = en if lang == "en" else load_json(root / "data" / "i18n" / f"{lang}.json")
        for key, source in en.items():
            entry = data.get(key)
            text = string_value(entry)
            if key == "_meta" or not isinstance(source, str) or text is None:
                continue
            if keys and not any(fnmatch.fnmatchcase(key, p) for p in keys):
                continue
            if only_ai and lang != "en" and not is_ai(entry):
                continue
            out.append(Unit(lang, "string", f"data/i18n/{lang}.json:{key}", source, text))
    if kind in (None, "pages"):
        english = content_pages(root, "en")
        for page, path in content_pages(root, lang).items():
            if page not in english or (pages and page not in pages):
                continue
            raw = path.read_text(encoding="utf-8")
            meta, _ = split_front_matter(raw)
            block = meta.get("translation") if isinstance(meta.get("translation"), dict) else {}
            if only_ai and lang != "en" and block.get("status") != "ai":
                continue
            stale = lang != "en" and block.get("source_hash") != source_hash(english[page])
            out.append(Unit(lang, "page", f"content/{lang}/{page}", english[page].read_text(encoding="utf-8"), raw,
                            stale))
    return out


def grade(root: Path, lang: str, kind: str | None = None, only_ai: bool = False,
          pages: set[str] | None = None, keys: list[str] | None = None) -> Grade:
    terms = protected.load_terms(root)
    gloss = glossary_rows(lang, root)
    g = Grade(lang)
    for unit in units(root, lang, kind, only_ai, pages, keys):
        m, found = grade_unit(unit, terms, gloss)
        g.units += 1
        g.stale += unit.stale
        g.words += m.words
        g.sentences += m.sentences
        g.findings += found
        g.counts.update(f.rule for f in found)
    return g


def table(grades: list[Grade]) -> str:
    head = ["lang", "units", "stale", "words", "w/sent"] + HARD + SOFT + ["hard", "soft", "soft/1k"]
    rows = [head, ["---"] * len(head)]
    for g in grades:
        per_k = 1000 * g.soft / g.words if g.words else 0
        rows.append([g.lang, str(g.units), str(g.stale), str(g.words), f"{g.words / max(g.sentences, 1):.1f}"]
                    + [str(g.counts[r]) for r in HARD + SOFT] + [str(g.hard), str(g.soft), f"{per_k:.1f}"])
    return "\n".join("| " + " | ".join(r) + " |" for r in rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--langs", help="comma-separated language keys (default: every translation)")
    parser.add_argument("--pages", help="comma-separated pages, as in content/en/")
    parser.add_argument("--keys", help="comma-separated string key patterns such as 'hero_*,device.*'")
    parser.add_argument("--kind", choices=["strings", "pages"], help="only strings or only pages")
    parser.add_argument("--ai", action="store_true", help="only machine translations")
    parser.add_argument("--since", help="only what changed since this git ref, such as origin/main")
    parser.add_argument("--details", action="store_true", help="print every finding")
    parser.add_argument("--json", type=Path, help="write the grades and findings to this file")
    parser.add_argument("--check", action="store_true", help="exit 1 when a hard rule fails")
    args = parser.parse_args(argv)
    keys = args.langs.split(",") if args.langs else [l.key for l in languages(ROOT) if l.key != "en"]
    only = set(args.pages.split(",")) if args.pages else None
    patterns = args.keys.split(",") if args.keys else None
    grades = []
    for lang in keys:
        if args.since:
            pages, changed = changed_since(ROOT, args.since, lang)
            g = grade(ROOT, lang, "pages", args.ai, pages) if pages else Grade(lang)
            if changed:
                s = grade(ROOT, lang, "strings", args.ai, None, sorted(changed))
                g.units, g.words, g.sentences = g.units + s.units, g.words + s.words, g.sentences + s.sentences
                g.counts.update(s.counts)
                g.findings += s.findings
            grades.append(g)
        else:
            grades.append(grade(ROOT, lang, args.kind, args.ai, only, patterns))
    print(table(grades))
    for g in grades:
        for f in g.findings:
            if args.details or (args.check and f.rule in HARD):
                print(f"{f.unit}: {f.rule}: {f.message}")
    if args.json:
        args.json.write_text(json.dumps([{**asdict(g), "counts": dict(g.counts), "hard": g.hard, "soft": g.soft}
                                         for g in grades], ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 1 if args.check and any(g.hard for g in grades) else 0


if __name__ == "__main__":
    sys.exit(main())
