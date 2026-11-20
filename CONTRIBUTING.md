# Contributing & Feedback

Thanks for using **Chicago Overlay**! The application source is kept private — but the project lives on community feedback: bug reports, layouts, translations and ideas are all welcome.

## Reporting Bugs

1. Check the issue still occurs in the [latest release](https://github.com/RadimSvatek/chicago-overlay/releases).
2. Relaunch the app with logging:
   ```cmd
   chicago.exe /debug /applog
   ```
   Reproduce the problem, then grab `data\log.txt` from the install folder (usually `C:\Program Files\Chicago Overlay\data\log.txt`).
3. Open an issue at [GitHub Issues](https://github.com/RadimSvatek/chicago-overlay/issues) and include:
   - Windows version (`winver` → e.g. *Windows 11 23H2, build 22631*),
   - how you run the app (default overlay, `--lite`, or `--tools` HW-Tools mode),
   - steps to reproduce + what you expected,
   - the log file (or the relevant lines).

## Sharing Layouts

Layouts are portable JSON — no tools needed:

- `Ctrl+Alt+C` copies the layout under your cursor straight to the clipboard,
- or hold `Ctrl+Alt+I` and click the ⧉ chip on the screen card,
- or use the **copy** button in the Inspector.

Paste the JSON into an issue (title it e.g. `[layout] my GPU dashboard`) — anyone can save it to `data\layouts\` and pick it in the tray menu. Screenshots of the result are gold.

## Translations

- Run `chicago.exe --export-lang` — it dumps the built-in `cs.json` / `en.json` into a `lang\` folder next to the exe.
- Copy `en.json`, rename it to your language code (e.g. `sk.json`), and translate the **values** — never the keys.
- Drop the file into `data\lang\` and switch language in Settings to test it live.
- Then attach it to an issue (`[lang] Slovak`) — we'll ship it bundled in the next release.

Bundled languages: `cs`, `en` (built in) + `de`, `es`, `fr`, `it`, `pl`. Corrections to existing files work the same way.

## Ideas

Feature requests go to Issues too — describe the use-case rather than the implementation ("I want to see X when Y happens" beats a spec). The best contributions so far came from people describing what Windows doesn't show them.
