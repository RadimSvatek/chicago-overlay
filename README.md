![Chicago Overlay](assets/chicago_banner.png)

**A lightweight, customizable, multi-monitor telemetry & system HUD overlay for Windows 10/11.**
Built for sim racing (via SimHub), PC hardware monitoring, and safe hardware-level fan control — but really, it is the layer Windows never shipped: a visual widget builder for anything your PC knows. Drag-and-drop layout editor, 600+ data sources, text, bars, graphs and images anywhere on any screen — zero code. Race HUD on Saturday, PC dashboard on Sunday — the same engine, your layout.

**600+ live props — every single one goes to your HUD, pill, widget or RTSS in-game overlay. The look is 100% your canvas.**

![Chicago Overlay — Assetto Corsa race HUD at 60 Hz](assets/ingame_ac.jpg)

![Chicago Overlay — control center, startup & tasks, cleanup and fan curves](assets/promo_windows.png)

![Desktop widgets — clock, now playing and audio spectrum on the desktop](assets/desktop.jpg)

![The same HUD in the visual editor — drag & drop, snapping grid, live inspector, zero code](assets/desktop_edit.jpg)

![Editor canvas zoom at 305% — pro-grade zoom for tiny elements: Ctrl+wheel to center, Alt+wheel around the cursor, Ctrl+Alt+drag pans, floating pill returns to 100%](assets/desktop_zoom.png)

![Computed grid nodes — perspective synthwave platform with depth-scaled crawl text and a 3D EQ spectrum filling the grid cells live](assets/synthwave_stage.png)

![Tron tunnel — flipped ceiling platform with crawl text converging on the horizon above a floor platform running a live 3D EQ spectrum](assets/4.png)

---

### Key Features

* **Universal Telemetry & System Data:**
  * **Sim Racing (SimHub Bridge):** Full support for 900+ SimHub properties (speed, RPM, gear, live delta, sector & lap times with automatic purple/green/yellow status colors, gaps, tyre/brake temperatures & pressures, fuel, flags, pedal graphs). Runs the full licensed 60 Hz tick with delta frames (only changed values travel the wire), cached accessors and bindable wheel-button actions — feather-light CPU cost. Includes automatic plugin installation and version checks.
  * **DirectX FPS & Frametimes:** Vendor-agnostic FPS, frametime graphs, and CPU/GPU frame times powered by Intel PresentMon (works in borderless & fullscreen).
  * **Hardware Sensors:** Real-time CPU/GPU temperatures, power draw (W), usage, RAM, motherboard temperature sensors and fan RPMs via LibreHardwareMonitor & signed PawnIO driver.
  * **Network Telemetry:** ping, packet loss %, and down/up throughput (kB/s) — with configurable ping targets (address list in Settings, add your own, cycle them via a shortcut; `Net.Target` shows the active one). For online racing and everyday monitoring; usable in alert rules ("packet loss" voice warning).
  * **Desktop & Media:** Clock, date, and real-time audio spectrum visualizer (8 selectable EQ engines) with current track info.
* **Built-in Visual HUD Builder (`Ctrl+Alt+E`):**
  * Drag-and-drop placement, multi-select marquee, snapping grid with configurable major lines, screen-wide crosshairs, and background dimming scrim for easy editing.
  * Rich visual elements: data readouts, bars (solid, gradient, HSL spectrum, LED segments, glow, reflection), line graphs, flags, sectors, lap times, status boxes — and **image elements** for team logos, channel branding, badges or any picture — a must-have when your HUD doubles as a stream overlay (fit modes, opacity, background, corner radius, PNG transparency).
  * Right-click any element for **layer ordering** — to front / forward / backward / to back works across every element type, groups move as a block, full undo support.
  * **Smart Conditional Rules:** 3-level color thresholds, blinking alerts, and visibility rules (`<`, `<=`, `=`, `!=`, `>=`, `>`) without touching a single line of code.
* **Desktop Widgets — the layer Windows never shipped:**
  * Free-floating native widgets (pills) drawn by a built-in WPF engine — **zero WebView2, near-zero RAM**. Snap them to any screen edge, or flip to **free mode** and park them anywhere with pixel-precise X/Y.
  * **Grab and drag them right on the desktop** in Edit mode (`Ctrl+Alt+E`) — the position saves itself and click-through comes back the moment you're done.
  * Per widget: horizontal or vertical orientation, custom name (shown in the tray submenu), **theme presets** instead of endless color fiddling, overall transparency plus a separate background alpha, and corner radius (capsule pill by default, `0` = sharp box).
  * Every widget is a row (or column) of live values with its own skin — FPS, frametimes, CPU, RAM, GPU load & temp… whatever source you pick. A ready-made `start-widget` ships on first install, widgets toggle straight from the tray menu, and a standalone Widgets window manages them all.
* **Render engine per monitor:**
  * Pick `webview` or `native` per display — the native engine paints `data` & `box` layout nodes directly in WPF with **no WebView2 process at all** on that screen: less RAM, instant paint, and fixed-width digit slots so values never jitter. A layout holding only a pill never starts WebView at all — the monitor runs native automatically, and `Ctrl+Alt+I` shows which engine each screen actually uses.
* **RTSS in-game OSD:**
  * Stream any widget's live text into **RivaTuner Statistics Server** shared memory — your stats inside exclusive-fullscreen games where ordinary overlays can't reach (verified live on RTSS 7.3.7).
* **Smart Resource Supervision — checkbox = permission, run = demand:**
  * An enabled source no longer runs just because the app is open. EQ, clock, hardware monitoring and PresentMon start only while something actually consumes them (a layout, widget, RTSS stream, alert rule, live session, fan control, an open HW window) — and stop the moment nobody needs them. Idle tray icon = idle app.
  * **Chicago audits itself:** `App.*` props expose its own CPU, private & shared RAM, WebView child count and their cost, threads, window counts and every source's state. The **Sources page** shows live usage plus *why* each source runs or idles.
* **Auto Profiles (game-aware HUD):**
  * Switch layouts automatically when a game or any process starts — race HUD on launch, back to a clean desktop on exit. Detection via process name or SimHub game name (partial match).
  * Per-monitor or all monitors, plus "HUD off" rules — e.g. race layout on the main screen, side monitors dark.
* **Fan Control (safe, hardware-level):**
  * Control motherboard fan headers (SuperIO chip via PawnIO), GPU fans, and USB fan controllers — auto / manual % / temperature curve.
  * Curves with 2-6 draggable points and per-curve hysteresis; fan identification spins a channel to 100 % so you can tell which header is which.
  * **Tray temperature icons:** any fan's temperature source can live in the tray as a transparent icon with the live value — LED "segment" digits (default) or classic mono typeface, accent or custom color per fan.
  * Dedicated **Fans window** from the tray menu, plus built-in warnings for missing admin rights and conflicts with other fan-control software.
  * Safety built in: 20 % minimum floor, instant return to hardware-auto on critical temps, and a watchdog guardian process that restores fan control even if the app crashes.
* **Button & Key Mapping (wheel/button-box friendly):**
  * Bind any keyboard key or steering wheel / button-box button (up to 16 devices × 32 buttons) on the dedicated Shortcuts page — cycle layouts, HUD on/off, edit mode, identify monitors, fans on/off, or start the stress test.
  * Works in-game; layout cycling offers a per-monitor choice and an optional voice announcement of the layout name — handy for VR.
* **HW Info — your PC at a glance:**
  * Windows version, BIOS, motherboard, CPU (cores/socket/clock), GPU (VRAM/driver), RAM modules, and disks with capacity — in a tray window, a settings page, and the bundled `hw-info` HUD layout. Complete PC summary at a glance.
* **Session Reports & Built-in Stress Test:**
  * After each gaming session a summary is recorded (average fps, 1% low, max CPU/GPU temps & power, duration) — browse them in the standalone Sessions window (tray menu or Settings), delete or ignore apps you don't want tracked.
  * Built-in CPU (0-100 % on all cores), GPU (WebGL shader) and RAM (MB allocation) stress test — perfect for tuning fan curves and the `tune-lab` layout without external tools.
* **Alerts & Bottleneck Detection:**
  * "key >= / <= value" rules on any telemetry with a beep or Windows voice announcement (cooldown between repeats).
  * `Sys.Limit` / `Sys.Throttle` keys show what is holding your FPS back — GPU, CPU, or thermal throttle.
* **System Cleanup with T800 mode:**
  * One-click deep clean for Windows junk and browser data: temp files, logs, caches, delivery optimization, WinSxS components (DISM), font & thumbnail caches, update leftovers, Defender & diagnostic history and more — every item labeled by risk tier (safe / dangerous / privacy / user data).
  * Optional **T800 mode** force-deletes locked files: it terminates the processes holding them — protecting itself, its own child processes and anything marked system-critical — and schedules the stragglers for removal at the next boot. Silent clean-up also runs from the recycle-bin context menu.
* **Start & Tasks manager:**
  * Everything that starts with your PC in a single window — registry Run keys, startup folders, services and all scheduled tasks (trigger type, next & last run, run-now, disable, and delete for non-system entries).
* **Command-line control (`/help`):**
  * One exe, many switches (`/x`, `-x` or `--x`): jump straight to any window (`/settings`, `/widgets`, `/cleaner`, `/startup`, `/fans`, `/hwinfo` …), pick a mode (`/tools`, `/lite`, `/full`), run a silent clean (`/clean`, `/clean-bin`) or set launch state without writing settings (`/debug`, `/applog`, `/source`, `/lang`, `/scale`, `/layout`).
  * The installer adds an optional **"Chicago Control Center"** desktop icon that opens the Control Center directly (`/settings`) — handy if the tray icon is ever unreachable. Copy the shortcut and change its parameter to pin any window to your desktop.
* **Chicago HW Tools — dedicated PC-tuning mode:**
  * Don't race? Run Chicago as a lean PC-tuning tool: fan control with curves, tray temperature icons, HW info, live network ping/loss, stress test, session reports, system cleanup and alerts — with the overlay, SimHub plugin and WebView2 completely off.
  * Installs as an optional component with its own **"Chicago HW Tools"** shortcut and icon — or launch it anytime via `chicago.exe --tools`. The main app can also run lean with `/lite`.
* **True Multi-Monitor & Low-Footprint Architecture:**
  * Assign different layouts and independent refresh rates (Full / 60 / 30 / 20 / 10 / 5 Hz) per monitor.
  * Choose between **Shared Canvas** (single WebView2 renderer across all monitors, saving ~140 MB RAM per extra display) or **Split Canvas**.
  * Tuned for near-zero CPU cost: hardware init and rescans run in the background, telemetry rides on delta frames, and idle work is gated — the overlay stays snappy and invisible until it has something to show.
* **20 Ready-to-Use Presets Included:**
  * Includes `start`, `race-minimal`, `race-hud`, `race-pro`, `race-pro-2`, `race-hw`, `system-hw`, `system-hud`, `hw-info`, `maxi-hw`, `media-eq`, `media-hud`, `media-hud-2`, `combo-desk`, `combo-hud`, `tune-lab` (fan-curve & stress tuning), `flat-stage`, `persp-stage`, `pill-hw` (native widget demo) and `sci-fi`.
* **7 Languages & Native Windows 11/10 Styling:**
  * Available in **English, Czech, German, Spanish, French, Italian, and Polish** (both installer and app). Follows your Windows accent color and dark/light theme — or pick any custom accent; the brand teal `#18D4C2` comes preselected on a clean install (your choice is never overwritten).

---

### Full or HW Tools — your choice at install

One installer, two editions. You pick right after the info page — and you can always launch the other edition later, both live side by side.

| | **Full** | **HW Tools** |
|---|:---:|:---:|
| HUD overlay, layouts & visual editor | ✓ | — |
| SimHub racing telemetry | ✓ | — |
| Media info & audio spectrum | ✓ | — |
| FPS & frametimes (PresentMon) | ✓ | ✓ |
| Fan control, curves & guardian watchdog | ✓ | ✓ |
| HW info, sensors & network monitoring | ✓ | ✓ |
| Stress test, session reports & alerts | ✓ | ✓ |
| System cleanup & start/tasks manager | ✓ | ✓ |
| Settings, updates, autostart, 7 languages | ✓ | ✓ |
| WebView2 runtime loaded | ✓ | never |

*Both editions get their own Start-menu shortcut (desktop optional). HW Tools is the same `chicago.exe` running in a dedicated `--tools` mode — no overlay, no SimHub, minimal RAM.*

---

### Quick Start

1. **Install:** Run `chicago overlay setup <ver>.exe` (~70 MB, bundled with .NET 8 & WebView2 prerequisites). The installer automatically detects `.NET 8` / `WebView2` and installs the `Chicago.Bridge.dll` plugin directly into your SimHub folder.
2. **Enable in SimHub:** Open SimHub and enable the **Chicago Overlay** plugin when prompted (or use the one-click installer/updater inside the app's tray menu or *Settings → Sources*).
3. **Customize:** Press **`Ctrl+Alt+E`** anytime to enter **Edit Mode** and open the Inspector. Press **`Ctrl+Alt+H`** to toggle HUD visibility, or **`Ctrl+Alt+I`** to identify your monitors.

---

### Download

Grab the latest `chicago_overlay_<ver>.zip` from **[Releases](../../releases)**, extract it and run the setup inside (.NET 8 + WebView2 prerequisites are bundled). In-app update checker notifies you about new versions.

---

### Behind the Project (A Note from the Author)

Chicago Overlay wasn't built in a modern corporate office — it was coded and tested inside a **1984 Wohnwagenwerk caravan**, which is my home. In a way, it feels fitting: 1984 was the golden era of Formula 1, back when drivers and engineers lived and worked right out of their caravans in the paddock.

Living in a rural area with limited local job opportunities, building this project became my way to put decades of old-school PC craftsmanship to good use — focusing on clean engineering, zero silent failures, and respecting every megabyte of RAM and every frame per second.

**Your feedback drives what comes next:**
Every idea, bug report, layout share, or suggestion from the community is genuinely welcome. If the project resonates with you, I am committed to developing it further and offering direct, individual support to users and sim racing teams.

If you enjoy using Chicago Overlay and want to support future development (or simply help out in a tough situation), any voluntary contribution means the world to me — both as recognition of the work and as real, practical help:

**[Support on Ko-fi (Card / Apple Pay / Google Pay / PayPal)](https://ko-fi.com/radimsvatek)**

*P.S. The project still sits at 0 stars — if Chicago made your PC a bit nicer, hitting ⭐ costs nothing and genuinely helps it get found.*

Thank you for taking it for a spin — see you on track!

---

### License & Distribution

* **Application (`Chicago Overlay`):** **Donationware / Freeware** — completely free to download and use with no locked features or subscriptions. If you find it useful, any voluntary contribution via [Ko-fi](https://ko-fi.com/radimsvatek) is greatly appreciated. Redistribution of modified binaries or commercial resale without permission is not allowed.
* **Source code:** not public — kept private by the author. Any use of the code in other projects or products requires the author's permission.
* **Layouts & Language Packs (`.json`):** free to use, modify, and share within the community.
* **Warranty:** the software is provided "as is", without warranty of any kind. Use at your own risk.
