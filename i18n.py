"""UI texts for the WinMate site (English and German)."""

SCHEMA_CATEGORY = {
    "browsers": "BrowserApplication", "communication": "CommunicationApplication", "media": "MultimediaApplication",
    "av": "MultimediaApplication", "graphics": "DesignApplication", "gaming": "GameApplication",
    "office": "BusinessApplication", "notes": "BusinessApplication", "cloud": "UtilitiesApplication",
    "files": "UtilitiesApplication", "utilities": "UtilitiesApplication", "customization": "UtilitiesApplication",
    "hardware": "UtilitiesApplication", "security": "SecurityApplication", "vpn": "SecurityApplication",
    "remote": "UtilitiesApplication", "runtimes": "UtilitiesApplication", "ai": "UtilitiesApplication",
    "editors": "DeveloperApplication", "terminal": "DeveloperApplication", "devtools": "DeveloperApplication",
    "languages": "DeveloperApplication", "cli": "DeveloperApplication", "virtualization": "UtilitiesApplication",
    "selfhost": "UtilitiesApplication",
}

T = {
    "en": {
        "locale": "en_US",
        "lang_name": "English",
        "skip": "Skip to content",
        "home": "home",
        "nav_label": "Main",
        "nav_apps": "Apps",
        "nav_how": "How it works",
        "nav_bundles": "Bundles",
        "toggle_theme": "Toggle dark/light mode",
        "meta_title": "WinMate – install many Windows apps with one script (winget, Scoop, Chocolatey)",
        "meta_description": "Select from {n} Windows apps and generate one script that installs them with winget, Scoop or Chocolatey. Open source, no account, a single administrator prompt.",
        "hero_title": "Install many Windows apps with one script",
        "hero_lead": "Select from {n} checked apps or start from a bundle. WinMate generates one script for winget, Scoop or Chocolatey that runs with a single administrator prompt.",
        "hero_points_plain": "One administrator prompt, checked package IDs, winget/Scoop/Chocolatey, bundles, keyboard shortcuts, English and German, no account",
        "hud_apps": "Apps",
        "hud_selected": "Selected",
        "hud_bundles": "Bundles",
        "hud_pm": "Via",
        "bundle_groups": {"basics": "Basics", "play": "Play & Create", "tech": "Tech & Server"},
        "keys_title": "Keyboard",
        "keys_short": [("/", "Search"), ("↑↓←→", "Navigate"), ("Space", "Select"), ("S", "Get script"), ("?", "All shortcuts")],
        "keys_all": [
            ("/", "Focus search"), ("Esc", "Clear search / close dialog"), ("↑ ↓ ← →", "Move between apps"),
            ("Space / Enter", "Select or deselect the focused app"), ("A", "Select all visible apps"),
            ("C", "Clear the selection"), ("U", "Undo the last clear"), ("B", "Jump to the bundles"),
            ("P or 1 2 3", "Switch package manager"), ("S", "Open the install script"),
            ("Y", "Copy the script for PowerShell"), ("D", "Download WinMate-Install.cmd"), ("?", "Show this help"),
        ],
        "keys_dialog_title": "Keyboard shortcuts",
        "nav_about": "How it works",
        "nav_security": "Security",
        "toggle_fx": "Turn animations on/off",
        "sources_title": "Package sources",
        "sources_lead": "The script installs exactly these packages. Versions are the latest ones recorded by the automated catalog check on {date}; they are used when version pinning is enabled.",
        "col_manager": "Package manager",
        "col_package": "Package",
        "col_version": "Verified version",
        "col_manifest": "Source",
        "manifest_link": "Manifest",
        "bundle_core_title": "Core apps",
        "bundle_extra_title": "Extended selection",
        "bundle_extra_intro": "Optional additions. They start unticked in WinMate; tick the ones you need.",
        "opt_title": "Options",
        "opt_pin": "Pin the versions verified on {date} (winget, Chocolatey)",
        "dl_winget_json": "winget import file",
        "engine_info": "WinMate {version} · engine SHA-256 <code>{sha}</code> · <a href=\"{href}\">Verify a script</a>",
        "profile_title": "Profile",
        "profile_hint": "Save the current selection as a file and load it again later. winmate.ps1 reads the same file.",
        "profile_export": "Export",
        "profile_import": "Import",
        "security_title": "Security & trust",
        "security_meta": "What a WinMate script does with administrator rights, how packages are checked, the threat model, known limits, and how to verify a script.",
        "security_lead": "WinMate scripts run installers with administrator rights. This page describes what a script does, how packages are checked, where the limits are, and how to verify a script before running it.",
        "security_html": """<section id="what"><h2>What a WinMate script does</h2>
<ul>
<li>It runs <code>winget</code>, <code>scoop</code> or <code>choco</code> for the packages listed at the top of the script, and nothing else. That list is visible in the preview before the download.</li>
<li>It requests administrator rights <b>once</b>. Apps whose installers refuse elevation run under the normal user account through a temporary scheduled task that is removed afterwards.</li>
<li>It downloads nothing from WinMate. Installers come from the vendors, as recorded in the package manifests.</li>
<li>It writes a log and a run record to <code>%LOCALAPPDATA%\\WinMate</code>, plus an undo script that removes only the apps the run installed.</li>
<li>There is no telemetry. The selection is stored in the browser only (<a href="{privacy}">privacy</a>).</li>
</ul></section>
<section id="verify"><h2>Verifying a script</h2>
<dl class="ids"><dt>Current version</dt><dd>{version}</dd><dt>Engine SHA-256</dt><dd><code>{sha}</code></dd><dt>Built from commit</dt><dd><a href="{commit_url}" rel="noopener"><code>{commit}</code></a></dd></dl>
<p>Every generated script consists of a short configuration block with the selected apps and the engine, which is identical in all scripts. To confirm that the engine is unchanged:</p>
<ol>
<li>Download <code>winmate.ps1</code> from the <a href="{repo}/releases/latest" rel="noopener">latest GitHub release</a>. Releases are built by public GitHub Actions and carry a build provenance attestation: <code>gh attestation verify winmate.ps1 --repo Benett53/WinMate</code></li>
<li>Run <code>.\\winmate.ps1 -Verify .\\WinMate-Install.cmd</code>. It prints the apps the script installs and reports <b>OK</b> only if the engine matches the published hash.</li>
<li>Or compare the engine block manually against <a href="{repo}/blob/main/src/ps/engine.ps1" rel="noopener">src/ps/engine.ps1</a>. The site is built reproducibly from the repository, so the result can be rebuilt and compared; <code>build-info.json</code> lists the hashes.</li>
</ol></section>
<section id="packages"><h2>How packages are checked</h2>
<ul>
<li><b>winget</b>: manifests in <a href="https://github.com/microsoft/winget-pkgs" rel="noopener">microsoft/winget-pkgs</a> are validated and scanned by Microsoft before publication. winget compares the SHA-256 hash of every installer against its manifest and refuses to run a file that does not match. Store apps are delivered by the Microsoft Store.</li>
<li><b>Chocolatey</b>: community packages are moderated and virus-scanned; downloaded installers must carry checksums.</li>
<li><b>Scoop</b>: manifests contain hashes that Scoop checks after the download; buckets change through reviewed pull requests.</li>
<li><b>WinMate</b>: a scheduled job checks every package ID against the official indexes once a week (last check: {checked}) and records the current versions. Scripts use exact IDs (<code>--exact</code>) and a fixed source, and can pin the recorded versions.</li>
</ul></section>
<section id="threats"><h2>Threat model</h2>
<div class="table-wrap"><table class="compare"><thead><tr><th scope="col">Threat</th><th scope="col">Mitigation</th><th scope="col">Remaining risk</th></tr></thead><tbody>
<tr><th scope="row">The website or hosting is compromised and serves a modified script</th><td>Open source, reproducible build in public CI, script preview, engine hash checked by <code>-Verify</code> against an attested release, strict Content-Security-Policy</td><td>Scripts that are run without being read or verified</td></tr>
<tr><th scope="row">A package source or manifest is compromised</th><td>Review, scanning and hash checks by winget, Chocolatey and Scoop; optional version pinning</td><td>WinMate cannot detect a malicious package that the upstream repository accepted</td></tr>
<tr><th scope="row">A wrong or malicious package ID enters the catalog</th><td>Pull request review, CI validation against the official indexes, IDs visible on every app page and in the script</td><td>A reviewer overlooks a similar-looking ID</td></tr>
<tr><th scope="row">Typosquatting and ambiguous names</th><td>Exact package IDs (<code>--exact</code>) and a fixed source (<code>--source winget</code>) instead of name searches</td><td>Low</td></tr>
<tr><th scope="row">Abuse of the administrator session</th><td>One elevation, used only for the listed packages; no services, no persistent tasks; temporary files are deleted</td><td>Installers themselves run with full rights, which is inherent to installing software</td></tr>
<tr><th scope="row">A broken installation</th><td>Run record, undo script for newly installed apps, one retry, detailed logs</td><td>An undo cannot revert changes an installer makes outside its own uninstaller</td></tr>
</tbody></table></div></section>
<section id="limits"><h2>Known limits</h2>
<ul>
<li><b>No Authenticode signature.</b> Scripts are generated in the browser for one specific selection and therefore cannot be code-signed. Release files carry GitHub build provenance instead, and the engine hash is published.</li>
<li><b>No independent security audit.</b> The code is small and readable; reviews and reports are welcome.</li>
<li><b>Single maintainer.</b> Everything is public and can be checked.</li>
<li><b>Not a deployment or management tool.</b> WinMate generates install scripts. There is no central management, no offline mirror and no compliance reporting.</li>
</ul></section>
<section id="report"><h2>Reporting a vulnerability</h2>
<p>Please report security issues privately through <a href="{repo}/security/advisories/new" rel="noopener">GitHub security advisories</a> rather than in public issues. Details are in <a href="{repo}/blob/main/SECURITY.md" rel="noopener">SECURITY.md</a>. Wrong package IDs and other bugs belong in the <a href="{repo}/issues" rel="noopener">issue tracker</a>.</p></section>""",
        "about_title": "How WinMate works",
        "about_meta": "How WinMate installs Windows apps with one script and a single administrator prompt, which package manager to choose, and answers to common questions.",
        "about_lead": "WinMate turns a selection of apps into a single install script. This page explains how that works and answers common questions.",
        "credits_title": "Inspiration",
        "credits_html": "WinMate is inspired by <a href=\"https://tuxmate.com/\" rel=\"noopener\">TuxMate</a>, a bulk app installer for Linux by <a href=\"https://github.com/abusoww/tuxmate\" rel=\"noopener\">abusoww</a>. WinMate applies the same idea to Windows with winget, Scoop and Chocolatey.",
        "footer_inspired": "Inspired by <a href=\"https://tuxmate.com/\" rel=\"noopener\">TuxMate</a> for Linux.",
        "catalog_title": "Select apps",
        "catalog_lead": "Select apps, choose a package manager, then generate the install script. The selection is kept in this browser.",
        "filters": "Filters",
        "pm_title": "Package manager",
        "pm_hint_winget": "Recommended. Part of Windows 10 and 11; uses Microsoft's official repository, including Store apps.",
        "pm_hint_scoop": "Installs into the user folder without administrator rights. Well suited to developer tools.",
        "pm_hint_choco": "Large community repository. Installs system-wide and requires administrator rights.",
        "presets_title": "Bundles",
        "search_label": "Search apps",
        "search_placeholder": "Search {n} apps…",
        "only_selected": "Selected only",
        "no_results": "No apps match this search.",
        "noscript": "JavaScript is required to generate the install script. All apps can still be browsed, and every app page lists the install commands.",
        "category_page": "Category page →",
        "not_available_short": "Not available",
        "details": "Details",
        "selected": "apps selected",
        "clear": "Clear",
        "get_script": "Get install script",
        "close": "Close",
        "dlg_title": "Install script",
        "dl_cmd": "Download WinMate-Install.cmd",
        "copy_ps": "Copy for PowerShell",
        "dl_ps1": "Download .ps1",
        "copy_link": "Copy share link",
        "show_script": "Show the script",
        "run_steps": [
            "Run <code>WinMate-Install.cmd</code>. If SmartScreen appears, choose <b>More info → Run anyway</b>.",
            "Confirm the administrator prompt once. The installers then run silently.",
            "Read the summary at the end. Running the script again retries the apps that failed.",
        ],
        "how_title": "How it works",
        "how_lead": "From a fresh Windows installation to a configured PC in four steps.",
        "steps": [
            ("Select apps", "Browse by category, search, or start from a bundle such as <em>Essentials</em> or <em>Gaming PC</em>."),
            ("Choose a package manager", "winget is part of Windows and the default choice. Scoop and Chocolatey are installed by the script if selected."),
            ("Download and run", "Run <code>WinMate-Install.cmd</code> or paste the script into PowerShell. Every line can be read beforehand."),
            ("Check the summary", "The apps install one after another. The summary lists what was installed, what needs a restart and what failed."),
        ],
        "admin_title": "Why you only see one admin prompt",
        "admin_text": "Normally every installer requests administrator rights on its own. A WinMate script elevates itself <b>once</b> and runs all installers from that elevated window, so they inherit the permission. Apps whose installers refuse to run as administrator, such as Spotify, are installed afterwards under the normal user account.",
        "compare_title": "winget vs. Scoop vs. Chocolatey",
        "compare_lead": "All three are free command-line package managers for Windows. winget is the default choice.",
        "compare_rows": [
            ("Setup", "Built into Windows 10/11", "Installed automatically", "Installed automatically"),
            ("Admin rights", "Once (WinMate)", "Not needed", "Required"),
            ("Install location", "Normal installers (Program Files)", "Portable, in your user folder", "System-wide"),
            ("Repository", "Official Microsoft repo + Store", "Community buckets", "Community repository"),
            ("Best for", "Everyone", "Developers, portable tools", "IT admins, wide catalog"),
            ("Update all apps", "<code>winget upgrade --all</code>", "<code>scoop update *</code>", "<code>choco upgrade all -y</code>"),
        ],
        "bundles_title": "Ready-made bundles",
        "bundles_lead": "Every bundle has a small set of core apps and an extended list of optional additions.",
        "n_apps": "{n} apps",
        "faq_title": "Frequently asked questions",
        "footer_about": "WinMate generates install scripts for Windows, for setting up a new or reinstalled PC.",
        "footer_disclaimer": "WinMate is not affiliated with Microsoft or with any listed software vendor. All product names, logos and trademarks belong to their respective owners. Review a script before running it.",
        "footer_categories": "Categories",
        "footer_bundles": "Bundles",
        "footer_project": "Project",
        "footer_report": "Report a wrong package",
        "footer_made": "Open source under the MIT license.",
        "privacy": "Privacy",
        "privacy_meta": "WinMate uses no cookies, tracking or analytics. The app selection stays in the browser.",
        "privacy_html": """<p>WinMate is a static website. It has no user accounts, no cookies, no analytics and no advertising.</p>
<h2>What is stored</h2><p>The app selection, the chosen package manager and the theme setting are stored in the browser's <code>localStorage</code> so they are still available on the next visit. This data never leaves the device and can be removed at any time by clearing the site data in the browser.</p>
<h2>Generated scripts</h2><p>Install scripts are generated entirely in the browser. Nothing about the selection is sent to a server. A script contacts only the chosen package manager (winget, Scoop or Chocolatey) and the download servers of the software vendors.</p>
<h2>Hosting</h2><p>The site is hosted on Cloudflare. Like any web host, Cloudflare processes technical data such as IP addresses in order to deliver the site and protect it against abuse. See the <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Cloudflare privacy policy</a>.</p>
<h2>External links</h2><p>App pages link to the official websites of the software vendors. Their privacy policies apply on those sites.</p>""",
        "note_msstore": "This app is installed from the Microsoft Store through winget (<code>--source msstore</code>). Free apps do not require a Microsoft account.",
        "note_noadmin": "The installer of {name} refuses to run with administrator rights. The WinMate script installs it under the normal user account instead.",
        "note_nonportable": "The Scoop package comes from the <em>nonportable</em> bucket and may ask for administrator rights itself.",
        "app_title": "Install {name} on Windows – winget, Scoop & Chocolatey | WinMate",
        "app_meta": "{desc}. Install {name} on Windows 10 and 11 with winget, Scoop or Chocolatey, on its own or together with other apps in one script.",
        "app_h1": "Install {name} on Windows",
        "add_to_script": "Add to my install script",
        "official_site": "Official website",
        "install_commands": "Install commands",
        "install_commands_lead": "Open PowerShell or Windows Terminal and run one of these commands to install {name}.",
        "not_available_pm": "Not available in the {pm} repository.",
        "copy": "Copy",
        "package_ids": "Package details",
        "category": "Category",
        "bulk_title": "Install {name} together with other apps",
        "bulk_text": "Add this app to a WinMate selection to install it together with the rest in one script and with a single administrator prompt.",
        "related": "More {cat}",
        "schema_category": SCHEMA_CATEGORY,
        "categories": "Categories",
        "bundles": "Bundles",
        "cat_title": "{name} for Windows – install with winget, Scoop or Chocolatey | WinMate",
        "cat_h1": "{name} for Windows",
        "select_all_in_winmate": "Select all {n} apps in WinMate",
        "open_bundle_in_winmate": "Open this bundle in WinMate",
        "more_categories": "More categories",
        "more_bundles": "More bundles",
        "nf_title": "Page not found",
        "nf_text": "This page does not exist (anymore). The app you are looking for is probably still in the catalog.",
        "nf_home": "Back to the catalog",
        "js": {
            "selected": "apps selected", "selected_one": "app selected",
            "summary": "{n} apps · installed with {pm}",
            "warn_unavailable": "{n} selected app(s) are not available for {pm} and will be skipped: {names}",
            "warn_store": "Installed from the Microsoft Store via winget: {names}",
            "warn_noadmin": "Installed without admin rights (their installers require this): {names}",
            "warn_nonportable": "These Scoop packages may ask for admin rights themselves: {names}",
            "warn_scoop_admin": "Scoop installs into the user folder; no administrator prompt is needed.",
            "copied": "Script copied. Paste it into PowerShell and press Enter.",
            "link_copied": "Share link copied.",
            "downloaded": "Download started.",
            "preset_added": "{name}: {n} apps added",
            "result_count": "{shown} of {total} apps",
            "select_first": "Select at least one app first.",
            "nothing_for_pm": "None of the selected apps is available for {pm}.",
            "copy_done": "Copied!",
            "own": "{n} own", "via_bundles": "{n} from bundles",
            "bundle_apps": "{sel} of {total} apps selected",
            "bundle_hint": "Core apps are preselected; extended apps are optional.",
            "bundle_core": "Core", "bundle_extra": "Extended",
            "bundle_core_hint": "The minimum for this setup.", "bundle_extra_hint": "Optional additions.",
            "bundle_select": "Select bundle", "bundle_switch": "Switch to this bundle", "bundle_switch_hint": "Replaces {old}. Individually picked apps stay selected.",
            "bundle_add": "Add to my selection", "bundle_add_hint": "Keeps the current selection.",
            "bundle_only": "Only this bundle", "bundle_only_hint": "Deselects everything else.",
            "bundle_update": "Update bundle", "bundle_remove": "Remove bundle", "cancel": "Cancel",
            "tag_own": "your pick", "tag_na": "not on {pm}", "tag_other": "in {name}",
            "bundle_added": "{name} selected", "bundle_removed": "{name} removed",
            "cleared": "Selection cleared – press U to undo.", "undone": "Selection restored.",
            "all_selected": "{n} visible apps selected", "pm_now": "Package manager: {pm}", "remove_bundle": "Remove {name}",
            "summary_install": "{n} apps · install with {pm}",
            "dl_cmd_label": "Download {file}",
            "warn_pin_scoop": "Scoop cannot pin versions; the latest versions are used.",
            "warn_pin_missing": "No verified version for: {names} – the latest version is used.",
            "profile_exported": "Profile saved.", "profile_imported": "Profile loaded: {n} apps.", "profile_invalid": "This file is not a WinMate profile.",
        },
    },
    "de": {
        "locale": "de_DE",
        "lang_name": "Deutsch",
        "skip": "Zum Inhalt springen",
        "home": "Startseite",
        "nav_label": "Hauptmenü",
        "nav_apps": "Apps",
        "nav_how": "So funktioniert's",
        "nav_bundles": "Pakete",
        "toggle_theme": "Hell/Dunkel umschalten",
        "meta_title": "WinMate – viele Windows-Programme mit einem Skript installieren (winget, Scoop, Chocolatey)",
        "meta_description": "Aus {n} Windows-Programmen auswählen und ein Skript erhalten, das sie mit winget, Scoop oder Chocolatey installiert. Open Source, ohne Konto, mit nur einer Administrator-Abfrage.",
        "hero_title": "Viele Windows-Programme mit einem Skript installieren",
        "hero_lead": "Aus {n} geprüften Apps auswählen oder mit einem Bundle beginnen. WinMate erzeugt daraus ein Skript für winget, Scoop oder Chocolatey, das mit einer einzigen Administrator-Abfrage läuft.",
        "hero_points_plain": "Eine Administrator-Abfrage, geprüfte Paket-IDs, winget/Scoop/Chocolatey, Bundles, Tastenkürzel, Deutsch und Englisch, ohne Konto",
        "hud_apps": "Apps",
        "hud_selected": "Gewählt",
        "hud_bundles": "Bundles",
        "hud_pm": "Via",
        "bundle_groups": {"basics": "Basics", "play": "Spielen & Kreativ", "tech": "Technik & Server"},
        "keys_title": "Tastatur",
        "keys_short": [("/", "Suche"), ("↑↓←→", "Navigieren"), ("Leertaste", "Auswählen"), ("S", "Skript holen"), ("?", "Alle Kürzel")],
        "keys_all": [
            ("/", "Suche fokussieren"), ("Esc", "Suche leeren / Dialog schließen"), ("↑ ↓ ← →", "Zwischen Apps wechseln"),
            ("Leertaste / Enter", "Fokussierte App an- oder abwählen"), ("A", "Alle sichtbaren Apps auswählen"),
            ("C", "Auswahl leeren"), ("U", "Leeren rückgängig machen"), ("B", "Zu den Bundles springen"),
            ("P oder 1 2 3", "Paketmanager wechseln"), ("S", "Installationsskript öffnen"),
            ("Y", "Skript für PowerShell kopieren"), ("D", "WinMate-Install.cmd herunterladen"), ("?", "Diese Hilfe anzeigen"),
        ],
        "keys_dialog_title": "Tastenkürzel",
        "nav_about": "So funktioniert's",
        "nav_security": "Sicherheit",
        "toggle_fx": "Animationen an/aus",
        "sources_title": "Paketquellen",
        "sources_lead": "Das Skript installiert genau diese Pakete. Die Versionen sind die neuesten, die der automatische Katalog-Check am {date} erfasst hat; sie werden verwendet, wenn das Festschreiben von Versionen aktiviert ist.",
        "col_manager": "Paketmanager",
        "col_package": "Paket",
        "col_version": "Geprüfte Version",
        "col_manifest": "Quelle",
        "manifest_link": "Manifest",
        "bundle_core_title": "Kern-Apps",
        "bundle_extra_title": "Erweiterte Auswahl",
        "bundle_extra_intro": "Optionale Ergänzungen. In WinMate sind sie zunächst abgewählt und lassen sich einzeln anhaken.",
        "opt_title": "Optionen",
        "opt_pin": "Am {date} geprüfte Versionen festschreiben (winget, Chocolatey)",
        "dl_winget_json": "winget-Importdatei",
        "engine_info": "WinMate {version} · Engine-SHA-256 <code>{sha}</code> · <a href=\"{href}\">Skript verifizieren</a>",
        "profile_title": "Profil",
        "profile_hint": "Die aktuelle Auswahl als Datei speichern und später wieder laden. winmate.ps1 liest dieselbe Datei.",
        "profile_export": "Exportieren",
        "profile_import": "Importieren",
        "security_title": "Sicherheit & Vertrauen",
        "security_meta": "Was ein WinMate-Skript mit Administratorrechten tut, wie Pakete geprüft werden, das Bedrohungsmodell, bekannte Grenzen und die Verifikation eines Skripts.",
        "security_lead": "WinMate-Skripte führen Installer mit Administratorrechten aus. Diese Seite beschreibt, was ein Skript tut, wie Pakete geprüft werden, wo die Grenzen liegen und wie sich ein Skript vor dem Ausführen verifizieren lässt.",
        "security_html": """<section id="what"><h2>Was ein WinMate-Skript tut</h2>
<ul>
<li>Es ruft <code>winget</code>, <code>scoop</code> oder <code>choco</code> für die Pakete auf, die oben im Skript stehen, und sonst nichts. Diese Liste ist vor dem Download in der Vorschau sichtbar.</li>
<li>Es fordert <b>einmal</b> Administratorrechte an. Apps, deren Installer keine erhöhten Rechte akzeptieren, laufen über eine temporäre geplante Aufgabe mit dem normalen Benutzerkonto; die Aufgabe wird danach entfernt.</li>
<li>Es lädt nichts von WinMate herunter. Die Installer kommen von den Herstellern, wie in den Paket-Manifesten hinterlegt.</li>
<li>Es schreibt ein Protokoll und einen Lauf-Datensatz nach <code>%LOCALAPPDATA%\\WinMate</code> sowie ein Undo-Skript, das nur die in diesem Lauf installierten Apps entfernt.</li>
<li>Es gibt keine Telemetrie. Die Auswahl wird ausschließlich im Browser gespeichert (<a href="{privacy}">Datenschutz</a>).</li>
</ul></section>
<section id="verify"><h2>Ein Skript verifizieren</h2>
<dl class="ids"><dt>Aktuelle Version</dt><dd>{version}</dd><dt>Engine-SHA-256</dt><dd><code>{sha}</code></dd><dt>Gebaut aus Commit</dt><dd><a href="{commit_url}" rel="noopener"><code>{commit}</code></a></dd></dl>
<p>Jedes erzeugte Skript besteht aus einem kurzen Konfigurationsblock mit den gewählten Apps und der Engine, die in allen Skripten identisch ist. So lässt sich prüfen, dass die Engine unverändert ist:</p>
<ol>
<li><code>winmate.ps1</code> aus dem <a href="{repo}/releases/latest" rel="noopener">aktuellen GitHub-Release</a> herunterladen. Releases werden von öffentlichen GitHub Actions gebaut und tragen einen Herkunftsnachweis: <code>gh attestation verify winmate.ps1 --repo Benett53/WinMate</code></li>
<li><code>.\\winmate.ps1 -Verify .\\WinMate-Install.cmd</code> ausführen. Der Befehl listet die Apps auf, die das Skript installiert, und meldet nur dann <b>OK</b>, wenn die Engine dem veröffentlichten Hash entspricht.</li>
<li>Alternativ den Engine-Block von Hand mit <a href="{repo}/blob/main/src/ps/engine.ps1" rel="noopener">src/ps/engine.ps1</a> vergleichen. Die Seite wird reproduzierbar aus dem Repository gebaut, das Ergebnis lässt sich also nachbauen und vergleichen; die Hashes stehen in <code>build-info.json</code>.</li>
</ol></section>
<section id="packages"><h2>Wie Pakete geprüft werden</h2>
<ul>
<li><b>winget</b>: Manifeste in <a href="https://github.com/microsoft/winget-pkgs" rel="noopener">microsoft/winget-pkgs</a> werden vor der Veröffentlichung von Microsoft validiert und gescannt. winget vergleicht den SHA-256-Hash jedes Installers mit dem Manifest und führt eine abweichende Datei nicht aus. Store-Apps liefert der Microsoft Store aus.</li>
<li><b>Chocolatey</b>: Community-Pakete werden moderiert und auf Schadsoftware geprüft; heruntergeladene Installer müssen Prüfsummen mitbringen.</li>
<li><b>Scoop</b>: Manifeste enthalten Hashes, die Scoop nach dem Download prüft; Buckets ändern sich über geprüfte Pull Requests.</li>
<li><b>WinMate</b>: Ein geplanter Job prüft jede Paket-ID wöchentlich gegen die offiziellen Indizes (letzte Prüfung: {checked}) und erfasst die aktuellen Versionen. Skripte nutzen exakte IDs (<code>--exact</code>) und eine feste Quelle und können die erfassten Versionen festschreiben.</li>
</ul></section>
<section id="threats"><h2>Bedrohungsmodell</h2>
<div class="table-wrap"><table class="compare"><thead><tr><th scope="col">Bedrohung</th><th scope="col">Gegenmaßnahme</th><th scope="col">Restrisiko</th></tr></thead><tbody>
<tr><th scope="row">Website oder Hosting werden kompromittiert und liefern ein verändertes Skript aus</th><td>Open Source, reproduzierbarer Build in öffentlicher CI, Skriptvorschau, Engine-Hash über <code>-Verify</code> gegen ein attestiertes Release, strenge Content-Security-Policy</td><td>Skripte, die ungelesen und ungeprüft ausgeführt werden</td></tr>
<tr><th scope="row">Eine Paketquelle oder ein Manifest wird kompromittiert</th><td>Prüfung, Scans und Hash-Kontrollen durch winget, Chocolatey und Scoop; optionales Festschreiben von Versionen</td><td>WinMate erkennt kein bösartiges Paket, das die Upstream-Quelle akzeptiert hat</td></tr>
<tr><th scope="row">Eine falsche oder bösartige Paket-ID gelangt in den Katalog</th><td>Prüfung im Pull Request, CI-Validierung gegen die offiziellen Indizes, IDs auf jeder App-Seite und im Skript sichtbar</td><td>Eine ähnlich aussehende ID wird übersehen</td></tr>
<tr><th scope="row">Typosquatting und mehrdeutige Namen</th><td>Exakte Paket-IDs (<code>--exact</code>) und feste Quelle (<code>--source winget</code>) statt Namenssuche</td><td>Gering</td></tr>
<tr><th scope="row">Missbrauch der Administrator-Sitzung</th><td>Eine Rechteerhöhung, nur für die aufgeführten Pakete; keine Dienste, keine dauerhaften Aufgaben; temporäre Dateien werden gelöscht</td><td>Die Installer selbst laufen mit vollen Rechten, das liegt in der Natur einer Softwareinstallation</td></tr>
<tr><th scope="row">Eine Installation geht schief</th><td>Lauf-Datensatz, Undo-Skript für neu installierte Apps, eine Wiederholung, ausführliche Protokolle</td><td>Ein Undo kann Änderungen außerhalb des jeweiligen Deinstallers nicht zurücknehmen</td></tr>
</tbody></table></div></section>
<section id="limits"><h2>Bekannte Grenzen</h2>
<ul>
<li><b>Keine Authenticode-Signatur.</b> Skripte entstehen im Browser für eine bestimmte Auswahl und lassen sich deshalb nicht signieren. Release-Dateien tragen stattdessen einen GitHub-Herkunftsnachweis, und der Engine-Hash ist veröffentlicht.</li>
<li><b>Kein unabhängiges Sicherheitsaudit.</b> Der Code ist klein und lesbar; Reviews und Meldungen sind willkommen.</li>
<li><b>Ein Maintainer.</b> Alles ist öffentlich und damit nachprüfbar.</li>
<li><b>Kein Deployment- oder Verwaltungswerkzeug.</b> WinMate erzeugt Installationsskripte. Es gibt keine zentrale Verwaltung, keinen Offline-Spiegel und kein Compliance-Reporting.</li>
</ul></section>
<section id="report"><h2>Sicherheitslücken melden</h2>
<p>Sicherheitsprobleme bitte vertraulich über <a href="{repo}/security/advisories/new" rel="noopener">GitHub Security Advisories</a> melden, nicht in öffentlichen Issues. Details stehen in <a href="{repo}/blob/main/SECURITY.md" rel="noopener">SECURITY.md</a>. Falsche Paket-IDs und andere Fehler gehören in den <a href="{repo}/issues" rel="noopener">Issue-Tracker</a>.</p></section>""",
        "about_title": "So funktioniert WinMate",
        "about_meta": "Wie WinMate Windows-Programme mit einem Skript und einer einzigen Administrator-Abfrage installiert, welcher Paketmanager passt und Antworten auf häufige Fragen.",
        "about_lead": "WinMate macht aus einer App-Auswahl ein einzelnes Installationsskript. Diese Seite erklärt den Ablauf und beantwortet häufige Fragen.",
        "credits_title": "Inspiration",
        "credits_html": "WinMate ist inspiriert von <a href=\"https://tuxmate.com/\" rel=\"noopener\">TuxMate</a>, einem Bulk-Installer für Linux von <a href=\"https://github.com/abusoww/tuxmate\" rel=\"noopener\">abusoww</a>. WinMate überträgt dieselbe Idee mit winget, Scoop und Chocolatey auf Windows.",
        "footer_inspired": "Inspiriert von <a href=\"https://tuxmate.com/\" rel=\"noopener\">TuxMate</a> für Linux.",
        "catalog_title": "Apps auswählen",
        "catalog_lead": "Apps auswählen, Paketmanager festlegen und das Installationsskript erzeugen. Die Auswahl bleibt in diesem Browser gespeichert.",
        "filters": "Filter",
        "pm_title": "Paketmanager",
        "pm_hint_winget": "Empfohlen. In Windows 10 und 11 enthalten, nutzt das offizielle Microsoft-Repository einschließlich Store-Apps.",
        "pm_hint_scoop": "Installiert ohne Administratorrechte in den Benutzerordner. Gut geeignet für Entwicklerwerkzeuge.",
        "pm_hint_choco": "Großes Community-Repository. Installiert systemweit und benötigt Administratorrechte.",
        "presets_title": "Bundles",
        "search_label": "Apps durchsuchen",
        "search_placeholder": "{n} Apps durchsuchen…",
        "only_selected": "Nur ausgewählte",
        "no_results": "Keine App passt zur Suche.",
        "noscript": "Für das Erzeugen des Installationsskripts wird JavaScript benötigt. Alle Apps lassen sich trotzdem durchsuchen, und jede App-Seite enthält die Installationsbefehle.",
        "category_page": "Zur Kategorie →",
        "not_available_short": "Nicht verfügbar",
        "details": "Details",
        "selected": "Apps ausgewählt",
        "clear": "Leeren",
        "get_script": "Installationsskript holen",
        "close": "Schließen",
        "dlg_title": "Installationsskript",
        "dl_cmd": "WinMate-Install.cmd herunterladen",
        "copy_ps": "Für PowerShell kopieren",
        "dl_ps1": ".ps1 herunterladen",
        "copy_link": "Link zum Teilen kopieren",
        "show_script": "Skript anzeigen",
        "run_steps": [
            "<code>WinMate-Install.cmd</code> ausführen. Erscheint SmartScreen: <b>Weitere Informationen → Trotzdem ausführen</b>.",
            "Die Administrator-Abfrage einmal bestätigen. Danach laufen die Installationen automatisch.",
            "Am Ende die Zusammenfassung lesen. Ein erneuter Lauf wiederholt die fehlgeschlagenen Apps.",
        ],
        "how_title": "So funktioniert's",
        "how_lead": "In vier Schritten vom frisch installierten Windows zum eingerichteten PC.",
        "steps": [
            ("Apps auswählen", "Nach Kategorien stöbern, suchen oder mit einem Bundle wie <em>Grundausstattung</em> oder <em>Gaming-PC</em> beginnen."),
            ("Paketmanager wählen", "winget ist in Windows enthalten und die Standardwahl. Scoop und Chocolatey installiert das Skript bei Bedarf selbst."),
            ("Herunterladen und ausführen", "<code>WinMate-Install.cmd</code> ausführen oder das Skript in PowerShell einfügen. Jede Zeile lässt sich vorher lesen."),
            ("Zusammenfassung prüfen", "Die Apps werden nacheinander installiert. Die Zusammenfassung zeigt, was installiert wurde, was einen Neustart braucht und was fehlgeschlagen ist."),
        ],
        "admin_title": "Warum nur eine Admin-Abfrage erscheint",
        "admin_text": "Normalerweise fordert jeder Installer seine eigenen Administratorrechte an. Ein WinMate-Skript startet sich <b>einmal</b> mit Administratorrechten neu und führt alle Installationen aus diesem Fenster aus, sodass sie die Berechtigung erben. Apps, deren Installer keine Administratorrechte akzeptieren, etwa Spotify, werden anschließend mit dem normalen Benutzerkonto installiert.",
        "compare_title": "winget vs. Scoop vs. Chocolatey",
        "compare_lead": "Alle drei sind kostenlose Kommandozeilen-Paketmanager für Windows. winget ist die Standardwahl.",
        "compare_rows": [
            ("Einrichtung", "In Windows 10/11 integriert", "Wird automatisch installiert", "Wird automatisch installiert"),
            ("Adminrechte", "Einmal (WinMate)", "Nicht nötig", "Erforderlich"),
            ("Installationsort", "Normale Installer (Programme)", "Portabel im Benutzerordner", "Systemweit"),
            ("Repository", "Offizielles Microsoft-Repo + Store", "Community-Buckets", "Community-Repository"),
            ("Ideal für", "Alle", "Entwickler, portable Tools", "IT-Admins, große Auswahl"),
            ("Alles aktualisieren", "<code>winget upgrade --all</code>", "<code>scoop update *</code>", "<code>choco upgrade all -y</code>"),
        ],
        "bundles_title": "Fertige Pakete",
        "bundles_lead": "Jedes Bundle besteht aus wenigen Kern-Apps und einer erweiterten Liste mit optionalen Ergänzungen.",
        "n_apps": "{n} Apps",
        "faq_title": "Häufige Fragen",
        "footer_about": "WinMate erzeugt Installationsskripte für Windows, um einen neuen oder neu aufgesetzten PC einzurichten.",
        "footer_disclaimer": "WinMate steht in keiner Verbindung zu Microsoft oder den aufgeführten Softwareherstellern. Alle Produktnamen, Logos und Marken gehören den jeweiligen Eigentümern. Skripte vor dem Ausführen prüfen.",
        "footer_categories": "Kategorien",
        "footer_bundles": "Pakete",
        "footer_project": "Projekt",
        "footer_report": "Falsches Paket melden",
        "footer_made": "Open Source unter der MIT-Lizenz.",
        "privacy": "Datenschutz",
        "privacy_meta": "WinMate verwendet keine Cookies, kein Tracking und keine Analyse. Die App-Auswahl bleibt im Browser.",
        "privacy_html": """<p>WinMate ist eine statische Website. Es gibt keine Benutzerkonten, keine Cookies, keine Analyse und keine Werbung.</p>
<h2>Was gespeichert wird</h2><p>Die App-Auswahl, der gewählte Paketmanager und die Einstellung für hell oder dunkel liegen im <code>localStorage</code> des Browsers, damit sie beim nächsten Besuch noch vorhanden sind. Diese Daten verlassen das Gerät nicht und lassen sich jederzeit löschen, indem die Websitedaten im Browser entfernt werden.</p>
<h2>Erzeugte Skripte</h2><p>Installationsskripte entstehen vollständig im Browser. Zur Auswahl wird nichts an einen Server gesendet. Ein Skript kontaktiert nur den gewählten Paketmanager (winget, Scoop oder Chocolatey) und die Downloadserver der Softwarehersteller.</p>
<h2>Hosting</h2><p>Die Seite wird bei Cloudflare gehostet. Wie jeder Webhoster verarbeitet Cloudflare technische Daten wie IP-Adressen, um die Seite auszuliefern und vor Missbrauch zu schützen. Siehe die <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Datenschutzerklärung von Cloudflare</a>.</p>
<h2>Externe Links</h2><p>App-Seiten verlinken die offiziellen Websites der Softwarehersteller. Dort gelten deren Datenschutzerklärungen.</p>""",
        "note_msstore": "Diese App wird über winget aus dem Microsoft Store installiert (<code>--source msstore</code>). Für kostenlose Apps ist kein Microsoft-Konto nötig.",
        "note_noadmin": "Der Installer von {name} akzeptiert keine Administratorrechte. Das WinMate-Skript installiert die App deshalb mit dem normalen Benutzerkonto.",
        "note_nonportable": "Das Scoop-Paket stammt aus dem Bucket <em>nonportable</em> und kann selbst nach Administratorrechten fragen.",
        "app_title": "{name} unter Windows installieren – winget, Scoop & Chocolatey | WinMate",
        "app_meta": "{desc}. {name} unter Windows 10 und 11 mit winget, Scoop oder Chocolatey installieren – einzeln oder zusammen mit weiteren Apps in einem Skript.",
        "app_h1": "{name} unter Windows installieren",
        "add_to_script": "Zu meinem Installationsskript hinzufügen",
        "official_site": "Offizielle Website",
        "install_commands": "Installationsbefehle",
        "install_commands_lead": "Öffne PowerShell oder Windows Terminal und führe einen dieser Befehle aus, um {name} zu installieren.",
        "not_available_pm": "Im {pm}-Repository nicht verfügbar.",
        "copy": "Kopieren",
        "package_ids": "Paketdetails",
        "category": "Kategorie",
        "bulk_title": "{name} zusammen mit weiteren Apps installieren",
        "bulk_text": "Diese App zu einer WinMate-Auswahl hinzufügen und zusammen mit den übrigen Programmen in einem Skript und mit einer einzigen Administrator-Abfrage installieren.",
        "related": "Weitere Apps: {cat}",
        "schema_category": SCHEMA_CATEGORY,
        "categories": "Kategorien",
        "bundles": "Pakete",
        "cat_title": "{name} für Windows – mit winget, Scoop oder Chocolatey installieren | WinMate",
        "cat_h1": "{name} für Windows",
        "select_all_in_winmate": "Alle {n} Apps in WinMate auswählen",
        "open_bundle_in_winmate": "Dieses Bundle in WinMate öffnen",
        "more_categories": "Weitere Kategorien",
        "more_bundles": "Weitere Pakete",
        "nf_title": "Seite nicht gefunden",
        "nf_text": "Diese Seite gibt es nicht (mehr). Die gesuchte App ist wahrscheinlich trotzdem im Katalog.",
        "nf_home": "Zurück zum Katalog",
        "js": {
            "selected": "Apps ausgewählt", "selected_one": "App ausgewählt",
            "summary": "{n} Apps · Installation mit {pm}",
            "warn_unavailable": "{n} ausgewählte App(s) gibt es nicht für {pm}, sie werden übersprungen: {names}",
            "warn_store": "Wird über winget aus dem Microsoft Store installiert: {names}",
            "warn_noadmin": "Wird ohne Adminrechte installiert (der Installer verlangt das): {names}",
            "warn_nonportable": "Diese Scoop-Pakete fragen eventuell selbst nach Adminrechten: {names}",
            "warn_scoop_admin": "Scoop installiert in den Benutzerordner, eine Administrator-Abfrage ist nicht nötig.",
            "copied": "Skript kopiert. In PowerShell einfügen und Enter drücken.",
            "link_copied": "Link zum Teilen kopiert.",
            "downloaded": "Download gestartet.",
            "preset_added": "{name}: {n} Apps hinzugefügt",
            "result_count": "{shown} von {total} Apps",
            "select_first": "Wähle zuerst mindestens eine App aus.",
            "nothing_for_pm": "Keine der ausgewählten Apps ist für {pm} verfügbar.",
            "copy_done": "Kopiert!",
            "own": "{n} eigene", "via_bundles": "{n} aus Bundles",
            "bundle_apps": "{sel} von {total} Apps ausgewählt",
            "bundle_hint": "Die Kern-Apps sind vorausgewählt, die erweiterten sind optional.",
            "bundle_core": "Kern", "bundle_extra": "Erweitert",
            "bundle_core_hint": "Das Minimum für dieses Setup.", "bundle_extra_hint": "Optional dazuwählbar.",
            "bundle_select": "Bundle auswählen", "bundle_switch": "Zu diesem Bundle wechseln", "bundle_switch_hint": "Ersetzt {old}. Einzeln gewählte Apps bleiben erhalten.",
            "bundle_add": "Zur Auswahl hinzufügen", "bundle_add_hint": "Behält die bisherige Auswahl.",
            "bundle_only": "Nur dieses Bundle", "bundle_only_hint": "Alles andere wird abgewählt.",
            "bundle_update": "Bundle aktualisieren", "bundle_remove": "Bundle entfernen", "cancel": "Abbrechen",
            "tag_own": "selbst gewählt", "tag_na": "nicht bei {pm}", "tag_other": "in {name}",
            "bundle_added": "{name} ausgewählt", "bundle_removed": "{name} entfernt",
            "cleared": "Auswahl geleert – U drücken zum Rückgängigmachen.", "undone": "Auswahl wiederhergestellt.",
            "all_selected": "{n} sichtbare Apps ausgewählt", "pm_now": "Paketmanager: {pm}", "remove_bundle": "{name} entfernen",
            "summary_install": "{n} Apps · Installation mit {pm}",
            "dl_cmd_label": "{file} herunterladen",
            "warn_pin_scoop": "Scoop kann keine Versionen festschreiben; es werden die neuesten Versionen verwendet.",
            "warn_pin_missing": "Keine geprüfte Version für: {names} – es wird die neueste Version verwendet.",
            "profile_exported": "Profil gespeichert.", "profile_imported": "Profil geladen: {n} Apps.", "profile_invalid": "Diese Datei ist kein WinMate-Profil.",
        },
    },
}

FAQ = {
    "en": [
        ("Is WinMate free and safe to use?",
         "WinMate is free and open source under the MIT license. The script is generated in the browser and contains only commands for the official package managers winget, Scoop and Chocolatey, which download the installers from the software vendors. The script can be read in full before it is run."),
        ("Why does the script ask for administrator rights only once?",
         "Most installers need administrator rights and would each show their own UAC prompt. A WinMate script elevates itself once and runs all installers from that session. Apps that must not be installed as administrator, such as Spotify, are installed afterwards under the normal user account."),
        ("Which package manager should I choose?",
         "Use <b>winget</b> if in doubt: it is part of Windows 10 and 11, uses Microsoft's official repository and can install Microsoft Store apps. <b>Scoop</b> installs portable apps into the user folder without administrator rights, which suits developer tools. <b>Chocolatey</b> has a large community catalog and installs system-wide."),
        ("Does this work on a brand-new Windows installation?",
         "Yes, that is the main use case. winget ships with Windows 11 and current Windows 10 builds. If it is not registered yet, the script registers it or opens the App Installer page in the Microsoft Store. Scoop and Chocolatey are installed by the script when selected."),
        ("Windows says \"Windows protected your PC\". What now?",
         "SmartScreen shows this warning for unsigned files downloaded from the internet. Choose <b>More info</b> and then <b>Run anyway</b>. As an alternative, use <b>Copy for PowerShell</b> and paste the script into a PowerShell window, which needs no file at all."),
        ("What happens to apps that are already installed?",
         "The package manager checks every app. An app that is already present is updated if a newer version exists, otherwise it is skipped. The summary marks these apps accordingly."),
        ("Which runtimes are needed on a fresh Windows?",
         "Many games and programs require the <b>Visual C++ Redistributables</b> and the <b>.NET Desktop Runtime</b>. Older games may also need <b>DirectX</b>, <b>XNA</b> or <b>OpenAL</b>. They are listed in the category <i>Runtimes &amp; Dependencies</i> and in the <i>Runtimes</i> bundle."),
        ("What is the difference between core and extended apps in a bundle?",
         "The core apps are the minimum that makes a setup work, and they are preselected. The extended list holds optional additions and alternatives; they stay unticked until they are selected."),
        ("An app failed to install. What can I do?",
         "Run the script again: apps that are already installed are skipped. Some failures are temporary, for example while a vendor is publishing a new version. The full log is written to <code>%LOCALAPPDATA%\\WinMate\\logs</code>. If a package ID is wrong, please open an issue on GitHub."),
        ("How do I update all apps later?",
         "Run <code>winget upgrade --all</code>, <code>scoop update *</code> or <code>choco upgrade all -y</code> in PowerShell, depending on the package manager that was used."),
        ("Can the installed apps be removed again?",
         "After an installation, WinMate writes an undo script to <code>%LOCALAPPDATA%\\WinMate\\runs</code>. It removes exactly the apps that this run installed and leaves everything that was already present untouched."),
        ("How can I check that a script was not tampered with?",
         "Every script contains the same engine, whose SHA-256 hash is published on the <a href=\"../security/#verify\">security page</a> and in every GitHub release. <code>winmate.ps1 -Verify WinMate-Install.cmd</code> compares the hash and lists the apps the script installs."),
        ("Does WinMate collect any data?",
         "No. There are no cookies, no analytics and no accounts. The selection is stored in the browser only and can be shared through a link that contains the app names."),
    ],
    "de": [
        ("Ist WinMate kostenlos und sicher?",
         "WinMate ist kostenlos und Open Source unter der MIT-Lizenz. Das Skript entsteht im Browser und enthält nur Befehle für die offiziellen Paketmanager winget, Scoop und Chocolatey, die die Installer bei den Herstellern laden. Das Skript lässt sich vor dem Ausführen vollständig lesen."),
        ("Warum fragt das Skript nur einmal nach Administratorrechten?",
         "Die meisten Installer brauchen Administratorrechte und würden jeweils eine eigene UAC-Abfrage zeigen. Ein WinMate-Skript startet sich einmal mit erhöhten Rechten neu und führt von dort alle Installationen aus. Apps, die nicht als Administrator installiert werden dürfen, etwa Spotify, werden anschließend mit dem normalen Benutzerkonto installiert."),
        ("Welcher Paketmanager ist der richtige?",
         "Im Zweifel <b>winget</b>: Es ist in Windows 10 und 11 enthalten, nutzt das offizielle Microsoft-Repository und kann Microsoft-Store-Apps installieren. <b>Scoop</b> installiert portable Apps ohne Administratorrechte in den Benutzerordner, was zu Entwicklerwerkzeugen passt. <b>Chocolatey</b> hat einen großen Community-Katalog und installiert systemweit."),
        ("Funktioniert das auf einem frisch installierten Windows?",
         "Ja, das ist der Hauptanwendungsfall. winget ist bei Windows 11 und aktuellem Windows 10 dabei. Ist es noch nicht registriert, übernimmt das Skript die Registrierung oder öffnet die App-Installer-Seite im Microsoft Store. Scoop und Chocolatey installiert das Skript bei Bedarf selbst."),
        ("Windows meldet \"Der Computer wurde durch Windows geschützt\". Was tun?",
         "SmartScreen zeigt diese Meldung bei unsignierten Dateien aus dem Internet. Auf <b>Weitere Informationen</b> und dann auf <b>Trotzdem ausführen</b> klicken. Alternativ das Skript über <b>Für PowerShell kopieren</b> in ein PowerShell-Fenster einfügen, dann wird keine Datei benötigt."),
        ("Was passiert mit Apps, die schon installiert sind?",
         "Der Paketmanager prüft jede App. Eine bereits vorhandene App wird aktualisiert, falls es eine neuere Version gibt, sonst übersprungen. In der Zusammenfassung sind diese Apps entsprechend markiert."),
        ("Welche Laufzeiten braucht ein frisches Windows?",
         "Viele Spiele und Programme setzen die <b>Visual C++ Redistributables</b> und die <b>.NET Desktop Runtime</b> voraus. Ältere Spiele brauchen teilweise zusätzlich <b>DirectX</b>, <b>XNA</b> oder <b>OpenAL</b>. Sie stehen in der Kategorie <i>Laufzeiten &amp; Abhängigkeiten</i> und im Bundle <i>Laufzeiten</i>."),
        ("Was unterscheidet Kern-Apps und erweiterte Apps in einem Bundle?",
         "Die Kern-Apps sind das Minimum, mit dem ein Setup funktioniert; sie sind vorausgewählt. Die erweiterte Liste enthält optionale Ergänzungen und Alternativen und bleibt abgewählt, bis sie angehakt wird."),
        ("Eine App ließ sich nicht installieren. Was tun?",
         "Das Skript erneut ausführen: Bereits installierte Apps werden übersprungen. Manche Fehler sind vorübergehend, etwa während ein Hersteller eine neue Version veröffentlicht. Das vollständige Protokoll liegt unter <code>%LOCALAPPDATA%\\WinMate\\logs</code>. Ist eine Paket-ID falsch, bitte ein Issue auf GitHub eröffnen."),
        ("Wie lassen sich später alle Apps aktualisieren?",
         "Je nach verwendetem Paketmanager in PowerShell <code>winget upgrade --all</code>, <code>scoop update *</code> oder <code>choco upgrade all -y</code> ausführen."),
        ("Lassen sich die installierten Apps wieder entfernen?",
         "Nach einer Installation schreibt WinMate ein Undo-Skript nach <code>%LOCALAPPDATA%\\WinMate\\runs</code>. Es entfernt genau die Apps, die dieser Lauf installiert hat, und lässt alles Vorhandene unangetastet."),
        ("Wie lässt sich prüfen, dass ein Skript nicht manipuliert wurde?",
         "Jedes Skript enthält dieselbe Engine, deren SHA-256-Hash auf der <a href=\"../security/#verify\">Sicherheitsseite</a> und in jedem GitHub-Release steht. <code>winmate.ps1 -Verify WinMate-Install.cmd</code> vergleicht den Hash und listet die Apps auf, die das Skript installiert."),
        ("Sammelt WinMate Daten?",
         "Nein. Es gibt keine Cookies, keine Analyse-Tools und keine Konten. Die Auswahl liegt nur im Browser und lässt sich über einen Link teilen, der die App-Namen enthält."),
    ],
}
