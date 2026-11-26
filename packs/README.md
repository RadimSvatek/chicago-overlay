# Chicago Overlay - community packy

Tenhle katalog žije v aplikaci v **Správce komponent → Packy**.
Katalog čte `packs/index.json` - ten (ani `.cpk`) **needituj
ručně**, generuje je CI.

## Jak přispět packem

1. Forkni repo, vytvoř složku `packs-src/<moje-id>/`
   (`<moje-id>` = `a-z0-9-`, 2-63 znaků).
2. Do ní `meta.json` + soubory packu v data-relativních
   cestách (viz níže).
3. Lokálně ověř: `python tools\validate_packs.py`
4. Pošli PR - CI validuje, maintainer reviewne a mergne.
   Po merge workflow sám zbuildí `<id>.cpk` a přepíše
   `index.json` - do PR **nepřidávej `.cpk` ani `index.json`**.

Update packu = stejná složka, vyšší `ver` v `meta.json` -
aplikace uživatelům ukáže badge "update".

## meta.json

```json
{
  "id": "moje-id",
  "type": "layout",
  "ver": "1.0",
  "name": "Muj pack",
  "min_app": "1.6.736",
  "desc_cs": "Co pack obsahuje (cz)",
  "desc_en": "What the pack contains (en)"
}
```

`type`: `layout` | `dash` | `tiles` | `skin` | `lang` |
`mixed`.

## Povolené cesty a soubory

Soubory padají do `data\` uživatele - whitelist rootů:

| Prefix        | Obsah                          |
| ------------- | ------------------------------ |
| `layouts/`    | HUD layouty `.json`            |
| `dash.`       | dashboard `dash.<id>.json`     |
| `tiles/`      | šablony dlaždic `.json`        |
| `macros/`     | makra `.json`                  |
| `calc/` `props/` `presets/` | výpočty a konstanty  |
| `img/` `map-img/` `icons/` | obrázky              |
| `sounds/`     | zvuky                          |
| `lang/`       | překlady `.json`               |
| `skins/` `widgets/` | skiny a widgety            |

Pravidla (vynucuje validátor i aplikace při instalaci):

- jen deklarativní obsah - přípony `.json`, `.png/.jpg/
  .jpeg/.svg/.webp/.gif`, `.wav/.mp3/.ogg`, `.ttf/.otf`,
  `.md`, `.txt` (žádný executable kód)
- max 2 MB / soubor, max 200 souborů / pack
- žádné `..`, `:`, absolutní cesty
- app-owned soubory (`settings.json`, `packs.json`,
  `map.json`...) jsou protected - pack je nemůže přepsat
- `.json` soubory musí být validní JSON
- kolize s uživatelovým souborem = instalace se odmítne,
  jeho práce se nepřepíše

## Moderace

PR review = čitelné JSON diffs (proto src složky, ne
binárky). Maintainer merge = vydání. Sporný obsah:
layouty propů - validátor strukturu, review smysl.

## Vlastní JSONy - ne jen packy

Všechny soubory v `data\` jsou **čistý JSON** - spořiče,
layouty, makra, výpočty, kanály. Uživatel si je může
doplnit/upravit podle sebe:

- **v aplikaci** - inspektor/layout editor (drag&drop,
  živý náhled ~400 ms hot-reload),
- **externím editoru** - libovolný textový editor,
  `ai-status.json` hlásí chyby formátu okamžitě,
- **nechat udělat AI** - `data\AGENTS.md` nese kompletní
  specifikaci formátu a bezpečnostní pravidla; katalog
  propů je `exports\props-export.json` (regenerace
  `/obj.aictx`) - AI klient ví, co smí vázat.

Známý formát = snadné sdílení: zabal vlastní soubory jako
pack (postup výše) a pošli PR - komunita si je nainstaluje
jedním kliknutím ze Správce komponent → Packy.
