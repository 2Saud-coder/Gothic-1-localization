#!/usr/bin/env python3
"""Prepare Arabic targets for Gothic's left-to-right, non-shaping text renderer.

The source CSVs remain normal Unicode Arabic. Only a disposable build copy is
reshaped into presentation forms and reordered for visual left-to-right output.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import arabic_reshaper
from bidi.algorithm import get_display


ARABIC_RE = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]")
BOUNDARY_RE = re.compile(r"(\||\\n|[\r\n])")
MARKUP_RE = re.compile(
    r"(<[^<>]*>|\[[^\[\]]*\]|\{[A-Za-z0-9_]+\}|%[A-Za-z0-9]*|\\[A-Za-z])"
)


def shape_segment(text: str) -> str:
    """Shape one text run while leaving inline control tokens untouched."""
    if not ARABIC_RE.search(text):
        return text

    parts = MARKUP_RE.split(text)
    shaped_parts = []
    for part in parts:
        if not part or MARKUP_RE.fullmatch(part):
            shaped_parts.append(part)
            continue
        shaped = arabic_reshaper.reshape(part)
        shaped_parts.append(get_display(shaped, base_dir="R"))
    return "".join(shaped_parts)


def shape_target(text: str) -> str:
    """Keep option separators and explicit line breaks in their original slots."""
    return "".join(
        part if BOUNDARY_RE.fullmatch(part) else shape_segment(part)
        for part in BOUNDARY_RE.split(text)
    )


def transform_csv(path: Path) -> int:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.reader(handle))

    if not rows or "target" not in rows[0]:
        return 0

    target_index = rows[0].index("target")
    changed = 0
    for row in rows[1:]:
        if len(row) <= target_index:
            continue
        target = row[target_index]
        shaped = shape_target(target)
        if shaped != target:
            row[target_index] = shaped
            changed += 1

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(
            handle,
            quoting=csv.QUOTE_ALL,
            lineterminator="\n",
        )
        writer.writerows(rows)
    return changed


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: shape_arabic.py <Arabic translation directory>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"Arabic translation directory not found: {root}", file=sys.stderr)
        return 2

    changed = 0
    for path in sorted(root.rglob("*.csv")):
        changed += transform_csv(path)

    print(f"Prepared Arabic display order in {changed} translation entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
