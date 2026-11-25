#!/usr/bin/env python3
"""validate_packs.py - kontrola packs-src/ slozek pred PR
(lokalne) a v CI. Zrcadli pravidla co aplikace vynucuje pri
instalaci .cpk (Packs.PathOk) + bezpecnostni whitelist
pripon - pack nese jen deklarativni obsah (json/obrazky/
zvuky/fonty), zadny executable.

Pouziti: python tools\validate_packs.py
Exit 0 = OK, 1 = chyby (vytiskne je).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "packs-src"

# ---- zrcadli src\Chicago.App\Data\Packs.cs _roots/_protected
ROOTS = ("dash.", "tiles/", "layouts/", "img/", "lang/",
         "skins/", "macros/", "calc/", "props/", "presets/",
         "sounds/", "icons/", "widgets/", "map-img/")
PROTECTED = {"settings.json", "components.json",
             "packs.json", "packs-catalog.json",
             "ai-status.json", "log.txt", "map.json",
             "dash.json"}

# CI vrstva nad PathOk - pack je jen obsah, ne kod
EXTS = {".json", ".png", ".jpg", ".jpeg", ".svg", ".webp",
        ".gif", ".wav", ".mp3", ".ogg", ".ttf", ".otf",
        ".md", ".txt"}
MAX_FILE = 2 * 1024 * 1024        # 2 MB na soubor
MAX_FILES = 200                   # pojistka proti spamu
TYPES = {"layout", "dash", "tiles", "skin", "lang",
         "mixed"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,62}$")
VER_RE = re.compile(r"^\d+\.\d+(\.\d+)?$")
REQ_META = ("id", "type", "ver", "name", "min_app",
            "desc_cs", "desc_en")


def path_ok(rel):
    low = rel.lower()
    if (not rel or rel.startswith("/") or rel.startswith("\\")
            or ":" in rel or ".." in rel):
        return "nepovolena cesta"
    if low in PROTECTED:
        return "protected soubor"
    if not low.startswith(ROOTS):
        return "mimo whitelist rootu"
    return None


def check_pack(d, errs):
    meta_p = d / "meta.json"
    if not meta_p.exists():
        errs.append(f"{d.name}: chybi meta.json")
        return
    try:
        meta = json.loads(meta_p.read_text(encoding="utf-8"))
    except Exception as e:
        errs.append(f"{d.name}: meta.json invalid - {e}")
        return
    for k in REQ_META:
        if k not in meta:
            errs.append(f"{d.name}: meta.json chybi '{k}'")
    pid = meta.get("id", "")
    if not ID_RE.match(str(pid)):
        errs.append(f"{d.name}: spatne id '{pid}' "
                    "(a-z0-9-, 2-63 znaku)")
    if pid != d.name:
        errs.append(f"{d.name}: meta id '{pid}' != nazev "
                    "slozky")
    if meta.get("type") not in TYPES:
        errs.append(f"{d.name}: type musi byt z "
                    f"{sorted(TYPES)}")
    if not VER_RE.match(str(meta.get("ver", ""))):
        errs.append(f"{d.name}: ver musi byt N.N[.N]")
    if not VER_RE.match(str(meta.get("min_app", ""))):
        errs.append(f"{d.name}: min_app musi byt N.N[.N]")

    files = [f for f in sorted(d.rglob("*"))
             if f.is_file() and f.name != "meta.json"]
    if not files:
        errs.append(f"{d.name}: prazdny pack (jen meta.json)")
    if len(files) > MAX_FILES:
        errs.append(f"{d.name}: {len(files)} souboru "
                    f"> max {MAX_FILES}")
    for f in files:
        rel = f.relative_to(d).as_posix()
        if err := path_ok(rel):
            errs.append(f"{d.name}: {rel} - {err}")
        if f.suffix.lower() not in EXTS:
            errs.append(f"{d.name}: {rel} - pripona "
                        f"'{f.suffix}' mimo whitelist")
        if f.stat().st_size > MAX_FILE:
            errs.append(f"{d.name}: {rel} - {f.stat().st_size} B"
                        " > 2 MB limitu")
        if f.suffix.lower() == ".json":
            try:
                json.loads(f.read_text(encoding="utf-8"))
            except Exception as e:
                errs.append(f"{d.name}: {rel} - invalid JSON "
                            f"({e})")


def main():
    errs = []
    if not SRC.exists():
        print("packs-src\\ neexistuje", file=sys.stderr)
        sys.exit(1)
    for d in sorted(SRC.iterdir()):
        if d.is_dir():
            check_pack(d, errs)
    if errs:
        print("VALIDACE SELHALA:")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    print(f"validace OK - {sum(1 for d in SRC.iterdir() if d.is_dir())} packu")


if __name__ == "__main__":
    main()
