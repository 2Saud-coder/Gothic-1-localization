# Arabic Localization Status

This branch is the working branch for the Arabic localization of Gothic 1.

## Current state

- All 30 translation CSV files from `.translations/en` have matching files under `.translations/ar`.
- Arabic is explicitly configured as UTF-8 in `.scripts/release.sh`.
- The current working set contains approximately 1,728 Arabic entries across the following files:
  - `Menu.csv`: 174 Arabic entries; only the day/time display placeholders remain in English.
  - `MOBSI.csv`: all 20 interaction descriptions translated.
  - `Monsters.csv`: all 65 creature names translated.
  - `Text_Constants.csv`: 359 entries translated, covering world objects, factions, spells, skills, inventory, stats, armor, messages, and chapter titles.
  - `Items.csv`: 150 item descriptions translated, covering amulets, rings, runes, scrolls, potions, maps, and documents.
  - `Log_Constants.csv`: 96 quest-log entries, trader hints, and trainer information translated.
  - `Cutscenes.csv`: all non-empty opening, introductory dialogue, final prayer, and ending lines translated.
  - `Dia_OTHER.csv`: all 45 entries translated.
  - `Dia_XARDASDEMON.csv`: all 34 entries translated.
  - `Dia_EBR.csv`: all 144 entries translated.
  - `Dia_NPC.csv`: all 197 NPC names and labels localized.
  - `Dia_ORC.csv`: all 229 Tarrok, Ur-Shak, and orc-priest dialogue entries translated.
  - `Dia_BAU.csv`: all 161 rice-farm, Horatio, and dam quest dialogue entries translated.
  - `Dia_GRD.csv`: first 115 of 875 guard dialogue entries translated, covering Bullit and Scorpio introductions, crossbow training, arena admission, betting, and fighter training. The remaining 760 entries are English fallback and marked for review.
- Non-Arabic fallback entries in the remaining files are marked `fuzzy=1` for review; they are not represented as completed translations.
- `.scripts/validate_arabic.py` checks all 30 CSV files for UTF-8 readability, matching headers and row counts, and fuzzy markers on non-Arabic fallback entries.
- `.github/workflows/validate_arabic.yml` runs the validator and then compiles localization packages on pushes to this branch.

## Build verification

A GitHub Actions build completed successfully on this branch and produced `G1_ar.mod` using UTF-8. The build log confirms that the Arabic locale was compiled and packed into the localization archive.

## Important in-game validation still required

1. Install the generated package and select the Arabic locale in GothicStarter.
2. Confirm that the UTF-8 font pack contains the required Arabic glyphs.
3. Test Arabic letter shaping, right-to-left ordering, punctuation, and mixed Arabic/Latin strings in-game.
4. Continue replacing fuzzy English fallback strings with reviewed Arabic translations.

## Release status

This is a development branch, not a finished public release. A successful UTF-8 compile does not prove that Gothic 1 renders Arabic correctly. Do not merge or publish as a complete Arabic localization until the in-game font and RTL tests pass.
