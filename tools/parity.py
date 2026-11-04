"""Structural parity of a translated Markdown body with its English source
(spec section 8.4). The seeder (plan 4) runs the same check on each
section it translates, so a bad translation never reaches a file.

A translation must keep, compared with the English body:
- the heading levels and explicit heading ids ({#legal}), in order: links
  to #legal must keep working when the heading text is translated;
- the shortcode tags with their parameters, in order (inner text may change);
- the fenced code blocks, unchanged and in order;
- the inline code spans and the link targets, bare URLs included (any order);
- the number of blocks (paragraph, list, table, code block), so a line the
  English does not have cannot slip onto the page.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field

FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
HEADING = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]|$)")
HEADING_ID = re.compile(r"\{[^}]*#([\w-]+)[^}]*\}\s*$")
# A code span ends with its paragraph: it never crosses a blank line.
INLINE_CODE = re.compile(r"(`+)((?:(?!\n[ \t]*\n).)+?)\1", re.S)
SHORTCODE = re.compile(r"\{\{[<%].*?[%>]\}\}", re.S)
LINK_TARGETS = [
    re.compile(r"\]\(\s*<?([^)\s>]+)>?(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"),  # [text](url "title")
    re.compile(r"^ {0,3}\[[^\]]+\]:\s*<?(\S+?)>?(?:\s|$)", re.M),                      # [ref]: url
    re.compile(r"<((?:https?|mailto):[^>\s]+)>"),                                       # <https://...>
    re.compile(r"\b(?:href|src)\s*=\s*[\"']([^\"']+)[\"']"),                            # raw HTML
]
# Bare URLs, which Hugo's Goldmark linkify turns into links. Searched after the
# forms above are blanked out, so no URL counts twice.
BARE_URL = re.compile(r"(?<![\w/.@-])(?:https?://|www\.)[^\s<>\"'()\[\]]+")
TRAILING = ".,;:!?*_~"
# The name of a shortcode tag; group 1 is "/" for a closing tag.
SHORTCODE_NAME = re.compile(r"\{\{[<%]\s*(/?)\s*([\w-]+)")


@dataclass
class Structure:
    headings: list[int] = field(default_factory=list)
    heading_ids: list[str] = field(default_factory=list)
    code_blocks: list[str] = field(default_factory=list)
    inline_code: list[str] = field(default_factory=list)
    shortcodes: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)


def structure(body: str) -> Structure:
    s = Structure()
    prose: list[str] = []
    fence, block = None, []
    for line in body.replace("\r\n", "\n").split("\n"):
        m = FENCE.match(line)
        if fence is None and m:
            fence, block = m.group(1), [line.strip()]
        elif fence is not None:
            block.append(line)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not line.strip()[len(m.group(1)):]:
                s.code_blocks.append("\n".join(block))
                fence = None
        else:
            prose.append(line)
            h = HEADING.match(line)
            if h:
                s.headings.append(len(h.group(1)))
                s.heading_ids += HEADING_ID.findall(line)
    if fence is not None:
        s.code_blocks.append("\n".join(block))
    text = "\n".join(prose)
    s.inline_code = [m.group(2).strip() for m in INLINE_CODE.finditer(text)]
    text = INLINE_CODE.sub(" ", text)
    s.shortcodes = [" ".join(m.group(0).split()) for m in SHORTCODE.finditer(text)]
    text = SHORTCODE.sub(" ", text)
    s.links = [m.group(1) for pattern in LINK_TARGETS for m in pattern.finditer(text)]
    for pattern in LINK_TARGETS:
        text = pattern.sub(" ", text)
    s.links += [m.group(0).rstrip(TRAILING) for m in BARE_URL.finditer(text)]
    return s


def sections(body: str) -> list[str]:
    """Split a Markdown body before each heading outside code blocks."""
    parts, current, fence = [], [], None
    for line in body.splitlines(keepends=True):
        m = FENCE.match(line)
        if fence is None and m:
            fence = m.group(1)
        elif fence is not None and m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
            fence = None
        elif fence is None and HEADING.match(line) and current:
            parts.append("".join(current))
            current = []
        current.append(line)
    if current:
        parts.append("".join(current))
    return parts


def blocks(body: str) -> list[str]:
    """Split each section into its blocks (paragraph, list, table, code block), after a blank line.

    Never inside a code block or between a shortcode's opening and closing tag, so
    each block can be translated on its own; joined, the blocks give the body back."""
    parts = []
    for section in sections(body):
        closing = {m.group(2) for m in map(SHORTCODE_NAME.match, SHORTCODE.findall(section))
                   if m and m.group(1)}
        current, fence, depth = [], None, 0
        for line in section.splitlines(keepends=True):
            after_blank = current and not current[-1].strip() and any(l.strip() for l in current)
            if line.strip() and after_blank and fence is None and depth == 0:
                parts.append("".join(current))
                current = []
            current.append(line)
            m = FENCE.match(line)
            if fence is None and m:
                fence = m.group(1)
            elif fence is not None and m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            elif fence is None:
                for tag in SHORTCODE.finditer(line):
                    name = SHORTCODE_NAME.match(tag.group(0))
                    if name and name.group(2) in closing:
                        depth += -1 if name.group(1) else 1
        if current:
            parts.append("".join(current))
    return parts


def _diff(kind: str, en: list[str], tr: list[str]) -> list[str]:
    missing = sorted((Counter(en) - Counter(tr)).elements())
    extra = sorted((Counter(tr) - Counter(en)).elements())
    found = [f"{kind}: missing {missing}"] if missing else []
    return found + ([f"{kind}: not in the English source {extra}"] if extra else [])


def compare(en_body: str, translated_body: str) -> list[str]:
    """Problems with the translation's structure; empty when it matches."""
    en, tr = structure(en_body), structure(translated_body)
    found = []
    if en.headings != tr.headings:
        found.append(f"heading levels {tr.headings} differ from the English source {en.headings}")
    if en.heading_ids != tr.heading_ids:
        found.append(f"heading ids {tr.heading_ids} differ from the English source {en.heading_ids}")
    if en.code_blocks != tr.code_blocks:
        found.append(f"code blocks differ from the English source ({len(en.code_blocks)} in English, "
                     f"{len(tr.code_blocks)} here; code is never translated)")
    if en.shortcodes != tr.shortcodes:
        found.append(f"shortcodes {tr.shortcodes} differ from the English source {en.shortcodes}")
    en_blocks, tr_blocks = len(blocks(en_body)), len(blocks(translated_body))
    if en_blocks != tr_blocks:
        found.append(f"{tr_blocks} blocks (paragraphs, lists, tables, code) where the English source has {en_blocks}")
    found += _diff("inline code", en.inline_code, tr.inline_code)
    found += _diff("link targets", en.links, tr.links)
    return found
