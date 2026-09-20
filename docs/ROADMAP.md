# Roadmap

Plans change with feedback. Suggestions belong in the [issue tracker](https://github.com/baba537/WinMate/issues).

## Done

- 2.3.0: bundles split into core and extended apps, catalog sorted by category and ranking, scripts reduced to
  installing, reworked texts in English and German
- 2.2.0: `winmate.ps1` CLI with script verification and run history, undo script, profiles, winget import file,
  version pinning, public CI, reproducible builds, weekly catalog check, releases with build provenance,
  security page, threat model, catalog policy

## Next

- **Tested on clean Windows**: an automated end-to-end install run in Windows Sandbox or a CI VM, including the
  administrator path.
- **WinGet Configuration (DSC) export** (`winget configure`) for repeatable, declarative setups.
- **Better failure details**: map common installer exit codes to readable hints.
- **Accessibility review** of the website with screen readers.

## Later

- Offline packages: `winget download` into a folder plus an offline install script.
- Custom package lists outside the catalog.
- More languages for the website.

## Out of scope

- Central management of many PCs; Intune, Configuration Manager and similar tools cover that.
- Hosting or mirroring installers.
- Collecting telemetry.
