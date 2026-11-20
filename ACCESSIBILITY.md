# Accessibility

**Chicago Overlay** is built to stay usable across different setups, vision preferences and input devices — racing in a VR headset included.

## Audio & Voice Feedback

- **Text-to-speech (Windows SAPI):** the app can *announce layout switches* out loud — enable the voice option and you'll hear the layout name, hands-free, no eyes off the track.
- **Alert rules with voice or tone:** telemetry rules can fire a `say` announcement (custom text, e.g. *"fuel low"*) or a distinctive two-tone beep (1046→1319 Hz), each with its own cooldown so it won't spam.
- All audio uses built-in Windows facilities — no extra runtime, no downloads.

## Visual Clarity

- **Full Light and Dark themes** — each theme keeps its own accent pair (dark: `#18D4C2`, light: `#008080` + `#1F4E52` title), or pick your own high-contrast colors in Settings.
- **UI scaling** — in Settings or on launch via `/scale:<percent>`, useful on 4K and small secondary screens.
- **Gentle alerting, not strobing** — the `blink` alert is a smooth 1.1 s ease-in-out "breathing" fade (configurable speed), never a hard flash.
- **Everything is restylable** — every HUD element's font, size, color and position is freely editable in the layout editor; nothing is locked at a fixed size.

## Input & Navigation

- **Global hotkeys:** `Ctrl+Alt+E` edit mode, `Ctrl+Alt+H` toggle HUD, `Ctrl+Alt+I` identify screens, `Ctrl+Alt+C` copy layout — all work from anywhere in Windows.
- **Steering wheels & button boxes:** up to **16 devices × 32 buttons** (DirectInput — wheels, pedals, button boxes, gamepads) can bind app actions.
- **Full command-line interface** — `/help` lists every switch (`/layout`, `/fans`, `/cleaner`, `/source`, …) for direct window access and automation without touching menus.

## Feedback

Hit a barrier we missed? Open an issue at [GitHub Issues](https://github.com/RadimSvatek/chicago-overlay/issues) — describe what you were trying to do and what got in the way.
