"""Shared helpers for the repository tools (spec section 8).

Every tool takes the repository root as a parameter (default ROOT), so the
tests can run it against a small temporary copy. Languages always come from
hugo.toml, never from a hard-coded list (spec section 3).
"""

from __future__ import annotations

import json
import os
import re
import tomllib
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@dataclass(frozen=True)
class Language:
    key: str      # URL prefix, content directory and strings file name
    label: str    # display name, also _meta.name of its strings file
    locale: str   # lang/hreflang value; the key unless hugo.toml sets one


@dataclass(frozen=True)
class Problem:
    file: str     # path relative to the repository root, with forward slashes
    message: str

    def __str__(self) -> str:
        return f"{self.file}: {self.message}"


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def languages(root: Path = ROOT) -> list[Language]:
    """The site languages in hugo.toml weight order; English first."""
    config = tomllib.loads((root / "hugo.toml").read_text(encoding="utf-8"))
    entries = sorted(config["languages"].items(), key=lambda kv: kv[1].get("weight", 0))
    return [Language(key, conf["label"], conf.get("locale", key)) for key, conf in entries]


class _StringDateLoader(yaml.SafeLoader):
    """SafeLoader that keeps dates as the strings written in the file.

    JSON Schema validates strings, and the tools compare dates as text.
    """


_StringDateLoader.yaml_implicit_resolvers = {
    first: [(tag, regexp) for tag, regexp in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for first, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def load_yaml_text(text: str):
    return yaml.load(text, Loader=_StringDateLoader)


def load_yaml(path: Path):
    return load_yaml_text(path.read_text(encoding="utf-8"))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


FRONT_MATTER = re.compile(r"\A---[ \t]*\r?\n(.*?)^---[ \t]*(?:\r?\n|\Z)", re.S | re.M)


def split_front_matter(text: str) -> tuple[dict, str]:
    """(front matter, body) of a content page. Content pages use YAML (---)."""
    text = text.removeprefix("﻿")
    match = FRONT_MATTER.match(text)
    if not match:
        raise ValueError("no YAML front matter (--- ... ---)")
    meta = load_yaml_text(match.group(1)) or {}
    if not isinstance(meta, dict):
        raise ValueError("front matter is not a mapping")
    return meta, text[match.end():]


def string_value(entry) -> str | None:
    """The visible text of a kiekr string entry: plain string or {value}."""
    if isinstance(entry, str):
        return entry
    if isinstance(entry, dict) and isinstance(entry.get("value"), str):
        return entry["value"]
    return None


def is_ai(entry) -> bool:
    return isinstance(entry, dict) and entry.get("_ai") is True


def content_pages(root: Path, lang: str) -> dict[str, Path]:
    """Markdown pages of one language, keyed by path inside content/<lang>/."""
    base = root / "content" / lang
    if not base.is_dir():
        return {}
    return {rel(p, base): p for p in sorted(base.rglob("*.md"))}



def english_page_exists(root: Path, path: str) -> bool:
    """Whether a site path such as /about or /blog has an English page."""
    base = root / "content" / "en" / path.strip("/")
    candidates = [base / "_index.md", base / "index.md"]
    if path.strip("/"):
        candidates.append(base.with_suffix(".md"))
    return any(c.is_file() for c in candidates)


# Content rules: no tracking parameters and no shop links.
TRACKING_PARAMS = {"ref", "referral", "referrer", "aff", "affid", "aff_id", "affiliate", "tag",
                   "fbclid", "gclid", "msclkid", "mc_cid", "mc_eid", "igshid", "si"}
SHOP_HOSTS = re.compile(r"(?:^|\.)(?:amazon\.[a-z.]+|amzn\.[a-z]+|a\.co|aliexpress\.[a-z.]+|ebay\.[a-z.]+"
                        r"|temu\.com|banggood\.com|tindie\.com|etsy\.com)$")


def url_problem(url: str) -> str | None:
    """Why a URL may not appear on the site, or None."""
    from urllib.parse import parse_qsl, urlsplit

    parts = urlsplit("https://" + url if url.startswith("www.") else url)
    if SHOP_HOSTS.search(parts.hostname or ""):
        return f"shop link {url!r} (devices are specs only)"
    for key, _ in parse_qsl(parts.query, keep_blank_values=True):
        if key.lower().startswith("utm_") or key.lower() in TRACKING_PARAMS:
            return f"tracking or referral parameter {key!r} in {url!r}"
    return None


def schema_problems(instance, schema_name: str, file: str, root: Path = ROOT) -> list[Problem]:
    """Validate instance against data/schema/<schema_name>.json."""
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import best_match

    schema = load_json(root / "data" / "schema" / f"{schema_name}.json")
    validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
    found = []
    for error in sorted(validator.iter_errors(instance), key=lambda e: list(map(str, e.absolute_path))):
        detail = best_match(error.context) if error.context else error
        where = "/".join(map(str, error.absolute_path)) or "(top level)"
        found.append(Problem(file, f"{where}: {detail.message}"))
    return found


def report(problems: list[Problem], ok: str) -> int:
    """Print problems (as GitHub annotations inside Actions); exit code."""
    in_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    for p in problems:
        print(f"::error file={p.file}::{p.message}" if in_actions else str(p))
    if problems:
        print(f"{len(problems)} problem(s)")
        return 1
    print(ok)
    return 0
