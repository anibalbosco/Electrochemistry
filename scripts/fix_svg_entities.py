#!/usr/bin/env python3
"""Rewrite SVG figure text using XML entities so chemistry symbols render reliably."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIGURES = ROOT / "assets" / "figures"

# Common corrupted patterns -> XML entities (ASCII-safe in SVG text nodes)
REPLACEMENTS: list[tuple[str, str]] = [
    ("Cu\u00b2\u207a", "Cu&#xb2;&#x207a;"),
    ("Cu2+", "Cu&#xb2;&#x207a;"),
    ("Cu\u00b2+", "Cu&#xb2;&#x207a;"),
    ("Cu{z", "Cu&#xb2;&#x207a;"),
    ("Cuz", "Cu&#xb2;&#x207a;"),
    ("Cu\uFFFDz", "Cu&#xb2;&#x207a;"),
    ("Zn\u00b2\u207a", "Zn&#xb2;&#x207a;"),
    ("Zn{z", "Zn&#xb2;&#x207a;"),
    ("Znz", "Zn&#xb2;&#x207a;"),
    ("Ag\u207a", "Ag&#x207a;"),
    ("Agz", "Ag&#x207a;"),
    ("Ag{z", "Ag&#x207a;"),
    ("2e\u207b", "2e&#x207b;"),
    ("2e-", "2e&#x207b;"),
    ("2e{", "2e&#x207b;"),
    ("e\u207b", "e&#x207b;"),
    ("e{", "e&#x207b;"),
    ("H\u2082", "H&#x2082;"),
    ("H2", "H&#x2082;"),
    ("Hz", "H&#x2082;"),
    ("H\uFFFD", "H&#x2082;"),
    ("O\u2082", "O&#x2082;"),
    ("O2", "O&#x2082;"),
    ("O\uFFFD", "O&#x2082;"),
    ("H\u2082O", "H&#x2082;O"),
    ("H\uFFFDO", "H&#x2082;O"),
    ("AgNO\u2083", "AgNO&#x2083;"),
    ("AgNO\uFFFD", "AgNO&#x2083;"),
    ("\u2192", "&#x2192;"),
    ("\uFFFD", "&#x2192;"),  # lone replacement char often was arrow
    ("\u2212", "&#x2212;"),
    ("\u0012", "&#x2212;"),  # corrupted minus (DC2)
    ("(-)", "(&#x2212;)"),
    ("(−)", "(&#x2212;)"),
    ("Cu\u2013Zn", "Cu&#x2013;Zn"),
    ("Cu\uFFFDZn", "Cu&#x2013;Zn"),
    ("\u00d7", "&#x00d7;"),
    ("\u03c1", "&#x03c1;"),
    ("\u03c0", "&#x03c0;"),
    ("2\u00d7", "2&#x00d7;"),
    ("V(H\u2082)", "V(H&#x2082;)"),
    ("V(H\uFFFD)", "V(H&#x2082;)"),
    ("V(O\u2082)", "V(O&#x2082;)"),
    ("H\u2082/", "H&#x2082;/"),
    (" / O\u2082", " / O&#x2082;"),
    (" \u2248 ", " &#x2248; "),
    ("H 2 : 1", "&#x2248; 2 : 1"),
]

# Fix double-replacements from order issues
POST_REPLACEMENTS = [
    ("H&#x2082;&#x2082;", "H&#x2082;"),
    ("O&#x2082;&#x2082;", "O&#x2082;"),
    ("&#x2192;&#x2192;", "&#x2192;"),
    ("&#x2212;&#x2212;", "&#x2212;"),
]


def fix_text_content(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    for old, new in POST_REPLACEMENTS:
        text = text.replace(old, new)
    # Em dash / corrupted separator in titles -> ASCII hyphen
    text = re.sub(r"Session (\d)\s+\S\s+", r"Session \1 - ", text)
    text = re.sub(r"\s+\S\s+(Mode |produces |copper |Reversible)", r" - \1", text)
    return text


def fix_svg(path: Path) -> bool:
    original = path.read_text(encoding="utf-8", errors="replace")
    fixed = fix_text_content(original)
    if fixed != original:
        path.write_text(fixed, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> None:
    changed = 0
    for svg in sorted(FIGURES.glob("*.svg")):
        if fix_svg(svg):
            print(f"  fixed {svg.name}")
            changed += 1
    print(f"Done. {changed} file(s) updated.")


if __name__ == "__main__":
    main()
