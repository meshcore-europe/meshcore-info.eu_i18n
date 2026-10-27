"""Protected terms and radio values (spec sections 6.5 and 8.5).

A term from glossary/protected.txt that appears in the English source must
appear unchanged in the translation. Numbers with radio units are protected
too: the translation must carry exactly the values of the English source
(869.525 MHz stays 869.525 MHz, not 869,525 MHz), including signs (-148 dBm)
and both ends of a range (869.4-869.65 MHz). Only the separator between
number and unit may differ: a space, a no-break space, none, or a hyphen as
in the German compound "868-MHz-Band".
"""

from __future__ import annotations

import re
from pathlib import Path

from common import ROOT

NUMBER = r"[-−+]?\d+(?:[.,]\d+)?"
UNIT = r"(GHz|MHz|kHz|dBm|dBi|dB|mW|mAh|W)\b"
MEASUREMENT = re.compile(
    rf"(?<![\w.,\-−+])(?:({NUMBER})(\s?[-–]\s?|\s+to\s+))?({NUMBER})(?:\s+|-)?{UNIT}"
    r"|\b(SF\d{1,2})\b"
)


def load_terms(root: Path = ROOT) -> list[str]:
    lines = (root / "glossary" / "protected.txt").read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.lstrip().startswith("#")]


def measurements(text: str, optional: set[str] | None = None) -> set[str]:
    """Radio values in text, normalised to '<number> <unit>'; a range gives both ends.

    The low end of a range written with "to" ("3 to 5 W") goes into optional
    when given: a translation may write it as "3-5 W" or as "3 a 5 W"."""
    found = set()
    for m in MEASUREMENT.finditer(text):
        if m.group(5):
            found.add(m.group(5))
            continue
        found.add(f"{m.group(3)} {m.group(4)}")
        if m.group(1):
            low = f"{m.group(1)} {m.group(4)}"
            if "to" in m.group(2) and optional is not None:
                optional.add(low)
            else:
                found.add(low)
    return found


def problems(en: str, translated: str, terms: list[str]) -> list[str]:
    found = [f"protected term {t!r} is missing" for t in terms if t in en and t not in translated]
    optional: set[str] = set()
    en_values, tr_values = measurements(en, optional), measurements(translated)
    found += [f"value {v!r} from the English source is missing" for v in sorted(en_values - tr_values)]
    found += [f"value {v!r} is not in the English source" for v in sorted(tr_values - en_values - optional)]
    return found
