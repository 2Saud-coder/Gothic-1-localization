#!/usr/bin/env python3
"""Validate the Arabic localization CSV structure and fallback markers."""

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_DIR = ROOT / ".translations" / "en"
AR_DIR = ROOT / ".translations" / "ar"
EXPECTED_HEADER = [
    "location",
    "source",
    "target",
    "id",
    "fuzzy",
    "context",
    "translator_comments",
    "developer_comments",
]
ARABIC_RE = re.compile(r"[\u0600-\u06FF]")
errors = []
translated = 0
fallback = 0

english_files = sorted(EN_DIR.glob("*.csv"))
if not english_files:
    errors.append("No English reference CSV files were found.")

for english_path in english_files:
    arabic_path = AR_DIR / english_path.name
    if not arabic_path.is_file():
        errors.append(f"Missing Arabic file: {arabic_path.relative_to(ROOT)}")
        continue

    try:
        with english_path.open("r", encoding="utf-8-sig", newline="") as handle:
            english_rows = list(csv.reader(handle))
        with arabic_path.open("r", encoding="utf-8-sig", newline="") as handle:
            arabic_rows = list(csv.reader(handle))
    except (UnicodeError, csv.Error) as exc:
        errors.append(f"Could not parse {arabic_path.name}: {exc}")
        continue

    if not arabic_rows or arabic_rows[0] != EXPECTED_HEADER:
        errors.append(f"{arabic_path.name}: unexpected or missing CSV header.")
        continue
    if not english_rows or english_rows[0] != EXPECTED_HEADER:
        errors.append(f"{english_path.name}: English reference header changed.")
        continue
    if len(arabic_rows) != len(english_rows):
        errors.append(
            f"{arabic_path.name}: {len(arabic_rows) - 1} rows; "
            f"expected {len(english_rows) - 1}."
        )
        continue

    for line_number, row in enumerate(arabic_rows[1:], start=2):
        if len(row) != len(EXPECTED_HEADER):
            errors.append(f"{arabic_path.name}:{line_number}: expected 8 columns.")
            continue
        target = row[2].strip()
        fuzzy = row[4].strip().lower()
        if not target:
            continue
        if ARABIC_RE.search(target):
            translated += 1
        else:
            fallback += 1
            if fuzzy not in {"1", "true", "yes"}:
                errors.append(
                    f"{arabic_path.name}:{line_number}: non-Arabic fallback "
                    "must be marked fuzzy=1."
                )

if errors:
    print("Arabic localization validation failed:")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print(
    f"Validated {len(english_files)} Arabic CSV files; "
    f"{translated} entries contain Arabic text and "
    f"{fallback} non-Arabic fallback entries are marked for review."
)
