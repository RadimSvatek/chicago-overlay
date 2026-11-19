![Chicago Overlay](assets/chicago_banner.png)

**A lightweight, customizable, multi-monitor telemetry & system HUD overlay for Windows 10/11.**
Built for sim racing (via SimHub), PC hardware monitoring, and safe hardware-level fan control — with zero bloat, low memory footprint, a built-in visual layout editor, and an at-a-glance HW info panel.

---

### Key Features

* **Universal Telemetry & System Data:**
  * **Sim Racing (SimHub Bridge):** Full support for 600+ SimHub properties (speed, RPM, gear, live delta, sector & lap times with automatic purple/green/yellow status colors, gaps, tyre/brake temperatures & pressures, fuel, flags, pedal graphs). Includes automatic plugin installation and version checks.
  * **DirectX FPS & Frametimes:** Vendor-agnostic FPS, frametime graphs, and CPU/GPU frame times powered by Intel PresentMon (works in borderless & fullscreen).
  * **Hardware Sensors:** Real-time CPU/GPU temperatures, power draw (W), usage, RAM, motherboard temperature sensors and fan RPMs via LibreHardwareMonitor & signed PawnIO driver.
  * **Network Telemetry:** ping, packet loss %, and down/up throughput (kB/s) — with configurable ping targets (address list in Settings, add your own, cycle them via a shortcut; `Net.Target` shows the active one). For online racing and everyday monitoring; usable in alert rules ("packet loss" voice warning).
  * **Desktop & Media:** Clock, date, and real-time audio spectrum visualizer (8 selectable EQ engines) with current track info.
* **Built-in Visual HUD Builder (`Ctrl+Alt+E`):**
  * Drag-and-drop placement, multi-select marquee, snapping grid with configurable major lines, screen-wide crosshairs, and background dimming scrim for easy editing.
  * Rich visual elements: data readouts, bars (solid, gradient, HSL spectrum, LED segments, glow, reflection), line graphs, flags, sectors, lap times, status boxes — and **image elements** for team logos, channel branding, badges or any picture — a must-have when your HUD doubles as a stream overlay (fit modes, opacity, background, corner radius, PNG transparency).
  * Right-click any element for **layer ordering** — to front / forward / backward / to back works across every element type, groups move as a block, full undo support.
  * **Smart Conditional Rules:** 3-level color thresholds, blinking alerts, and visibility rules (`<`, `<=`, `=`, `!=`, `>=`, `>`) without touching a single line of code.
* **Auto Profiles (game-aware HUD):**
  * Switch layouts automatically when a game or any process starts — race HUD on launch, back to a clean desktop on exit. Detection via process name or SimHub game name (partial match).
  * Per-monitor or all monitors, plus "HUD off" rules — e.g. race layout on the main screen, side monitors dark.
* **Fan Control (safe, hardware-level):**
  * Control motherboard fan headers (SuperIO chip via PawnIO — like FanControl), GPU fans, and USB fan controllers — auto / manual % / temperature curve.
  * Curves with 2-6 draggable points and per-curve hysteresis; fan identification spins a channel to 100 % so you can tell which header is which.
  * **Tray temperature icons:** any fan's temperature source can live in the tray as a transparent icon with the live value — LED "segment" digits (default) or classic mono typeface, accent or custom color per fan.
  * Dedicated **Fans window** from the tray menu, plus built-in warnings for missing admin rights and conflicts with other fan-control software.
  * Safety built in: 20 % minimum floor, instant return to hardware-auto on critical temps, and a watchdog guardian process that restores fan control even if the app crashes.
* **Button & Key Mapping (wheel/button-box friendly):**
  * Bind any keyboard key or steering wheel / button-box button (up to 16 devices × 32 buttons) on the dedicated Shortcuts page — cycle layouts, HUD on/off, edit mode, identify monitors, fans on/off, or start the stress test.
  * Works in-game; layout cycling offers a per-monitor choice and an optional voice announcement of the layout name — handy for VR.
* **HW Info — your PC at a glance:**
  * Windows version, BIOS, motherboard, CPU (cores/socket/clock), GPU (VRAM/driver), RAM modules, and disks with capacity — in a tray window, a settings page, and the bundled `hw-info` HUD layout. No separate HWiNFO summary needed.
* **Session Reports & Built-in Stress Test:**
  * After each gaming session a summary is recorded (average fps, 1% low, max CPU/GPU temps & power, duration) — browse them in the standalone Sessions window (tray menu or Settings), delete or ignore apps you don't want tracked.
  * Built-in CPU (0-100 % on all cores), GPU (WebGL shader) and RAM (MB allocation) stress test — perfect for tuning fan curves and the `tune-lab` layout without external tools.
* **Alerts & Bottleneck Detection:**
  * "key >= / <= value" rules on any telemetry with a beep or Windows voice announcement (cooldown between repeats).
  * `Sys.Limit` / `Sys.Throttle` keys show what is holding your FPS back — GPU, CPU, or thermal throttle.
* **Lite Mode — fans & HW monitor only:**
  * Don't race? Run Chicago as a lean PC-tuning tool: fan control with curves, tray temperature icons, HW info, live network ping/loss, stress test, session reports and alerts — with the overlay, SimHub plugin and WebView2 completely off.
  * Enable it in the installer options, in Settings, or just launch the always-installed **"Chicago Overlay lite"** shortcut (both full and lite shortcuts optionally on the desktop).
* **True Multi-Monitor & Low RAM Architecture:**
  * Assign different layouts and independent refresh rates (Full / 60 / 30 / 20 / 10 / 5 Hz) per monitor.
  * Choose between **Shared Canvas** (single WebView2 renderer across all monitors, saving ~140 MB RAM per extra display) or **Split Canvas**.
* **16 Ready-to-Use Presets Included:**
  * Includes `start`, `race-minimal`, `race-hud`, `race-pro`, `race-pro-2`, `race-hw`, `system-hw`, `system-hud`, `hw-info`, `media-eq`, `media-hud`, `media-hud-2`, `combo-desk`, `combo-hud`, `tune-lab` (fan-curve & stress tuning), and `sci-fi`.
* **7 Languages & Native Windows 11/10 Styling:**
  * Available in **English, Czech, German, Spanish, French, Italian, and Polish** (both installer and app). Follows your Windows accent color and dark/light theme — or pick any custom accent; the brand teal `#18D4C2` comes preselected on a clean install (your choice is never overwritten).

---

### Full or Lite — your choice at install

One installer, two editions. You pick right after the info page — and you can always launch the other edition later, both live side by side.

| | **Full** | **Lite** |
|---|:---:|:---:|
| HUD overlay, layouts & visual editor | ✓ | — |
| SimHub racing telemetry | ✓ | — |
| Media info & audio spectrum | ✓ | — |
| FPS & frametimes (PresentMon) | ✓ | ✓ |
| Fan control, curves & guardian watchdog | ✓ | ✓ |
| HW info, sensors & network monitoring | ✓ | ✓ |
| Stress test, session reports & alerts | ✓ | ✓ |
| Settings, updates, autostart, 7 languages | ✓ | ✓ |
| WebView2 runtime loaded | ✓ | never |

*Both editions get their own Start-menu shortcut (desktop optional). Lite is a lean resident tool for PC tuning — no overlay, no SimHub, minimal RAM.*

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

Thank you for taking it for a spin — see you on track!

---

### License & Distribution

* **Application (`Chicago Overlay`):** **Donationware / Freeware** — completely free to download and use with no locked features or subscriptions. If you find it useful, any voluntary contribution via [Ko-fi](https://ko-fi.com/radimsvatek) is greatly appreciated. Redistribution of modified binaries or commercial resale without permission is not allowed.
* **Source code:** not public — kept private by the author. Any use of the code in other projects or products requires the author's permission.
* **Layouts & Language Packs (`.json`):** free to use, modify, and share within the community.
* **Warranty:** the software is provided "as is", without warranty of any kind. Use at your own risk.
