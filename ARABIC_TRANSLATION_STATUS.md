# Arabic Localization Status

This branch is the working branch for the Arabic localization of Gothic 1.

## Current state

- All 30 translation CSV files from `.translations/en` have matching files under `.translations/ar`.
- The Arabic locale is explicitly configured as UTF-8 in `.scripts/release.sh`.
- Initial Arabic translation work has been added:
  - `Menu.csv`: 174 Arabic entries; the remaining date/time placeholders are intentionally retained.
  - `MOBSI.csv`: 20 Arabic entries.
  - `Monsters.csv`: 34 Arabic creature names.
  - `Text_Constants.csv`: 136 Arabic entries covering world objects, factions, spells, skills, and inventory categories.
  - `Items.csv`: 150 Arabic item names/descriptions covering amulets, rings, runes, scrolls, potions, maps, and documents.
  - `Log_Constants.csv`: 96 Arabic quest-log entries, trader hints, and trainer information.
  - `Cutscenes.csv`: 54 Arabic lines across the opening, introductory dialogue, final prayer, and ending.
- A validation script checks all 30 files for UTF-8 readability, matching CSV headers/row counts, and fuzzy markers on non-Arabic fallback entries.
- A separate GitHub Actions workflow validates the CSVs and then attempts a full localization build on this branch.
- Untranslated English fallback entries in the other files are marked `fuzzy=1` for review. They are not presented as completed Arabic translations.

## Important technical validation still required

1. Run the upstream `dacode subs` and `dacode compile` pipeline for the `ar` locale.
2. Confirm the UTF-8 font pack contains the required Arabic glyphs.
3. Test Arabic glyph shaping, right-to-left ordering, punctuation, and mixed Arabic/Latin strings in-game.
4. Replace English fallback strings with reviewed Arabic translations and clear their fuzzy flags only after review.

## Release status

This is a development branch, not a finished release. A successful UTF-8 compile alone does not prove that Gothic 1 renders Arabic correctly. Do not merge or publish as a complete Arabic localization until the in-game font and RTL tests pass.
