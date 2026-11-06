# Arabic Test Build - Gothic 1

This is a development test package, not a finished public release.

## Download

1. Open the [Arabic localization build on GitHub Actions](https://github.com/2Saud-coder/Gothic-1-localization/actions/runs/42296748250).
2. Under **Artifacts**, download `gothic-1-localization-build`.
3. Extract the downloaded artifact ZIP.
4. Inside it, extract `Gothic_1_Localized.zip`.

## Install

1. In Steam, open Gothic 1 Classic's **Manage > Browse local files**.
2. Back up the game's existing `Data` and `System` folders.
3. Copy the `Data` and `System` folders from the extracted package into the game directory and allow the files to merge.
4. Install Union first if it is not already installed. The upstream localization project requires Union for UTF-8 languages.
5. Run `GothicStarter.exe` and select **Gothic Localized (ar)**.

## What to test

- Do Arabic letters appear as connected, readable words?
- Does text flow from right to left?
- Are menu labels, dialogue, item names, and journal text positioned correctly?
- Do Arabic and Latin strings (names, numbers, key names) display in the right order?
- Does the game start without script or font errors?

## Known limitations

- The build compiles successfully and creates `G1_ar.mod` using UTF-8.
- 1,728 entries currently contain Arabic text.
- 9,339 non-Arabic fallback entries remain marked for translation/review.
- Arabic font coverage and right-to-left shaping have not yet been verified in the running game.

If the letters appear disconnected, reversed, or as squares, stop and report exactly what appears. Do not merge this branch or treat the package as a complete release until these tests pass.
