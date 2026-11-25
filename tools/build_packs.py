#!/usr/bin/env python3
"""build_packs.py - packs-src/<id>/ -> packs/<id>.cpk +
regeneruje packs/index.json. Spousti CI po merge do main;
lze pustit i lokalne.

.cpk = zip: meta.json + data-relativni cesty (layouts/,
tiles/, ...). index.json nese sha256+size+files - aplikace
proti nim pri instalaci verifikuje.

Pouziti: python tools\build_packs.py
"""
import io, json, hashlib, sys
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "packs-src"
OUT = ROOT / "packs"


def build(d):
    meta = json.loads(
        (d / "meta.json").read_text(encoding="utf-8"))
    buf = io.BytesIO()
    files = []
    with ZipFile(buf, "w", ZIP_DEFLATED) as z:
        # embedded meta staci id/type/ver/name - aplikace
        # z nej cte jen identitu; index nese zbytek
        z.writestr("meta.json", json.dumps(
            {k: meta[k] for k in ("id", "type", "ver", "name")},
            ensure_ascii=False, separators=(",", ":")))
        for f in sorted(d.rglob("*")):
            if f.is_file() and f.name != "meta.json":
                rel = f.relative_to(d).as_posix()
                z.write(f, rel)
                files.append(rel)
    data = buf.getvalue()
    (OUT / f"{meta['id']}.cpk").write_bytes(data)
    return {
        "id": meta["id"], "name": meta["name"],
        "ver": meta["ver"], "type": meta["type"],
        "min_app": meta["min_app"],
        "desc_cs": meta["desc_cs"], "desc_en": meta["desc_en"],
        "zip": f"{meta['id']}.cpk",
        "sha256": hashlib.sha256(data).hexdigest(),
        "size": len(data), "files": files}


def main():
    OUT.mkdir(exist_ok=True)
    ids = set()
    packs = []
    for d in sorted(SRC.iterdir()):
        if d.is_dir() and (d / "meta.json").exists():
            p = build(d)
            packs.append(p)
            ids.add(p["id"] + ".cpk")
            print(f"{p['id']}.cpk  {p['size']} B  "
                  f"{len(p['files'])} souboru")
    # smaz cpk bez src slozky (pack se odebirá smazanim src)
    for old in OUT.glob("*.cpk"):
        if old.name not in ids:
            old.unlink()
            print("smazan osirely", old.name)
    (OUT / "index.json").write_text(
        json.dumps({"packs": packs}, ensure_ascii=False,
                   indent=2) + "\n", encoding="utf-8")
    print(f"index.json: {len(packs)} packu")


if __name__ == "__main__":
    sys.exit(main())
