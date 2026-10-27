#!/usr/bin/env python3
"""Validate data/i18n/<lang>.json (spec sections 6.1 and 8.3).

- one file per hugo.toml language, and none for other languages;
- every file matches data/schema/i18n.json (kiekr format);
- _meta.language is the file's language key and _meta.name its hugo.toml
  label, so _meta cannot drift;
- en.json holds only plain strings (no _ai, no null);
- translations hold only keys that en.json has, keep the {placeholders}
  of the English string, and keep protected terms and radio values.

Exit 0 = valid, 1 = problems (printed).
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

import protected
from common import ROOT, Problem, languages, load_json, rel, report, schema_problems, string_value

PLACEHOLDER = re.compile(r"\{[a-z_]+\}")


def placeholders(text: str) -> list[str]:
    return sorted(PLACEHOLDER.findall(text))


def check(root: Path = ROOT) -> list[Problem]:
    i18n = root / "data" / "i18n"
    langs = {l.key: l for l in languages(root)}
    terms = protected.load_terms(root)
    found: list[Problem] = []
    files = {}
    for lang in langs:
        path = i18n / f"{lang}.json"
        name = rel(path, root)
        if not path.is_file():
            found.append(Problem(name, "missing (every language in hugo.toml needs a strings file)"))
            continue
        try:
            files[lang] = load_json(path)
        except json.JSONDecodeError as e:
            found.append(Problem(name, f"invalid JSON: {e}"))
    for path in sorted(i18n.glob("*.json")):
        if path.stem not in langs:
            found.append(Problem(rel(path, root), f"language {path.stem!r} is not in hugo.toml"))

    en = files.get("en")
    for lang, data in files.items():
        name = f"data/i18n/{lang}.json"
        schema_found = schema_problems(data, "i18n", name, root)
        found += schema_found
        if schema_found:
            continue
        m = data["_meta"]
        if m["language"] != lang:
            found.append(Problem(name, f"_meta.language {m['language']!r} must be {lang!r}"))
        if m["name"] != langs[lang].label:
            found.append(Problem(name, f"_meta.name {m['name']!r} must be {langs[lang].label!r} (the label in hugo.toml)"))
        if lang == "en":
            found += [Problem(name, f"{key}: English strings must be plain text")
                      for key, v in data.items() if key != "_meta" and not isinstance(v, str)]
            continue
        if en is None:
            continue
        for key, entry in data.items():
            if key == "_meta":
                continue
            if key not in en:
                found.append(Problem(name, f"key {key!r} is not in en.json"))
                continue
            source, text = string_value(en[key]), string_value(entry)
            if source is None or text is None:
                continue
            if Counter(placeholders(text)) != Counter(placeholders(source)):
                found.append(Problem(name, f"{key}: placeholders {placeholders(text)} differ from English {placeholders(source)}"))
            found += [Problem(name, f"{key}: {msg}") for msg in protected.problems(source, text, terms)]
    return found


def main() -> int:
    return report(check(), "i18n ok")


if __name__ == "__main__":
    sys.exit(main())
