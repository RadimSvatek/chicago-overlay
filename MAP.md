# 🗺️ The Map — Spatial Control & Idea Cheat Sheet

> **Town Square vs. Open Sandbox:** The main menu acts as your *Town Square* for instant access, while **The Map** (`chicago.exe /map`) is your personal open canvas—designed around **spatial memory**, **playfulness**, and **granular security**.

---

## 💡 Concept & Theme Ideas (Build Your Own World)

Instead of digging through nested settings menus, place modules where your brain naturally expects them. Replace any module tile with a custom PNG image, set a background (including retro Win95-style tiling), and build your own environment:

| Theme Concept | How to Build It | Best Modules to Combine |
| :--- | :--- | :--- |
| **🛰️ Orbital Station (ISS)** | Use a deep-space backdrop and snap modules together with visible joints like pressurized station hulls. | `Bridge` (Command), `Fans` & `HW` (Life Support), `Channels` (Comms) |
| **🏠 Smart Home / Base Blueprint** | Set your apartment/house floorplan as the background and place modules directly into the rooms they control. | `Home Assistant`, `Routers`, `Printers` (3D print room), `Remote` (NAS/Server) |
| **🌳 RPG Talent Tree** | Arrange modules as interconnected skill nodes—core system at the root, advanced telemetry and automation branching outward. | `Props` -> `Calc` -> `Aura RGB` / `LED Matrix` / `Macros` |
| **🎛️ Retro Winamp Rack** | Use magnetic edge-snapping to dock compact modules into a single unified hardware deck that moves as one piece. | `Bartender`, `OBS`, `Media`, `Pomodoro` |

---

## 🛡️ Purposeful Design: Per-Module Permissions

The Map isn't just visual—it acts as a **smart security boundary** (better than running an entire app as Admin):

* **Engine Room (Elevated / UAC):** Check *"Run as administrator"* in module properties **only** for modules that talk directly to low-level hardware (`Fans`, `Fan Options`, `HW Info`, `HW Maxi`).
* **Standard Deck (Safe User Token):** Keep `WebView` overlays, `OBS`, `Home Assistant`, `Routers`, and `Bartender` running with standard user privileges.
* **One-Click Elevation:** Chicago elevates only when an admin module is opened, and lets you drop back via *"Restart without admin"* anytime.

---

## ⌨️ Controls & Shortcuts Cheat Sheet

| Action | Control / Shortcut |
| :--- | :--- |
| **Open The Map** | `chicago.exe /map` · Tray Menu · Control Center · Desktop Icon |
| **Move Docked Assembly** | Drag any snapped module (moves the entire linked cluster Winamp-style) |
| **Undock Single Module** | `Shift + Drag` or `Ctrl + Alt + Drag` (or Right-click → *Undock*) |
| **Pixel-Perfect Alignment** | Select module + `Arrow Keys` (`1 px`) · `Shift + Arrow Keys` (`8 px`) |
| **Module Customization** | `Right-Click` on module → Size, Custom Image, Font, Admin Rights |
| **Canvas & Grid Settings** | Click **Map Settings** → Grid, Magnetize, Default Size, Retro Tile BG, Reset |
| **Fullscreen Command Mode** | `F11` (toggle) · `Esc` (exit) |

---

## 🚀 Quick Start Tips for New Users

1. **Start with 3 core islands:** Group **Hardware/Cooling** on one side, **Network/Smart Home** on the other, and **Bridge/Bartender** in the center.
2. **Use transparent PNGs:** Drop custom icons or blueprints into `data\map-img\` and assign them via module properties to turn tiles into real instruments.
3. **Backup your layout:** Your entire station layout is cleanly stored in `data\map.json`—easy to back up, version, or share.
