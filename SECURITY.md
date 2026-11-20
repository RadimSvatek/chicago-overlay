# Security Policy

## Supported Versions

Only the **latest release** is supported with fixes, including security fixes. Check [Releases](https://github.com/RadimSvatek/chicago-overlay/releases) before reporting — the in-app updater tracks `releases/latest` automatically.

## What runs elevated, and why

Chicago runs with administrator rights because it talks to hardware:

- **PawnIO driver + LibreHardwareMonitor** (open source) — CPU/GPU/board sensors and optional fan control. Fan control **writes to hardware registers**; a panic failsafe, minimum-PWM floor and a `--guardian` watchdog restore hardware-auto control if the app dies.
- **Cleaner "force" mode (T800, opt-in)** — uses the Windows Restart Manager to terminate processes that lock files you chose to delete. It never touches Chicago's own process tree or processes marked `RmCritical`, but it *is* intentionally aggressive — report it if you find a path where it kills something it must not.
- **Update check** — reads GitHub Releases over HTTPS only; it never downloads or executes code by itself.

What it does **not** do: no accounts, no telemetry, no tracking, no ads. Network access is limited to the update check and an optional latency ping (`1.1.1.1`) if you enable the network widget.

## Verify your download

- Download only from [GitHub Releases](https://github.com/RadimSvatek/chicago-overlay/releases) — the project has no other distribution channel.
- Each release notes page lists **SHA-256** hashes for both the zip and the installer inside it. Compare before running.
- The installer is unsigned (no commercial code-signing certificate) — a SmartScreen warning on first run is expected, not a sign of tampering. A mismatched hash is.

## Reporting a vulnerability

Use **GitHub Security Advisories** → *Report a vulnerability* in the [Security tab](https://github.com/RadimSvatek/chicago-overlay/security). Especially welcome:

- escalation paths through the elevated process, data folder, or settings/layout files,
- misuse of fan-control writes or the guardian process,
- the cleaner terminating processes it should protect,
- anything in the installer/update flow.

Please don't disclose exploit details in public issues until a fix is out.
