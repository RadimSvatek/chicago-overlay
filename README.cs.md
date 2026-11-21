# Chicago Overlay

**Lehký, plně přizpůsobitelný telemetrický a systémový HUD overlay pro Windows 10/11.**
Navržený pro simracing (přes SimHub) i sledování výkonu PC — bez zbytečného balastu, s minimálními nároky na RAM a vestavěným vizuálním editorem.

---

### Hlavní funkce

* **Univerzální telemetrie a systémová data:**
  * **SimRacing (SimHub Bridge):** Podpora více než 600 hodnot ze SimHubu (rychlost, otáčky, zařazený stupeň, živá delta, sektorové a traťové časy s automatickým fialovým/zeleným/žlutým stavovým barvením, rozestupy, teploty a tlaky pneumatik i brzd, palivo, vlajky, grafy pedálů). Obsahuje automatickou instalaci pluginu a hlídání kompatibility verzí.
  * **DirectX FPS a Frametime:** Měření FPS, frametime grafy a odezva CPU/GPU přes Intel PresentMon (funguje v okně bez okrajů i ve fullscreenu, nezávisle na značce grafické karty).
  * **Hardwarové senzory:** Teploty CPU/GPU, spotřeba ve Wattech, vytížení, RAM, teplotní čidla desky a otáčky ventilátorů přes LibreHardwareMonitor a podepsaný ovladač PawnIO.
  * **Plocha a multimédia:** Hodiny, datum a real-time audio spektrum (8 volitelných EQ motorů) se zobrazením právě přehrávané skladby.
* **Vestavěný vizuální editor (`Ctrl+Alt+E`):**
  * Přetahování myší, hromadný výběr prvků (jako v Průzkumníku), přichytávání k mřížce se zvýrazněnými hlavními linkami, zaměřovač přes obrazovku a ztmavení podkladu při úpravách.
  * Bohaté vizuální prvky: datové hodnoty, bary (plné, gradient, HSL spektrum, LED segmenty, svit, zrcadlový odraz), křivkové grafy, vlajky, sektory, časy kol a stavové boxy.
  * **Chytrá podmíněná pravidla:** Tříúrovňové barevné prahy, blikající výstrahy a podmínky zobrazení (`<`, `<=`, `=`, `!=`, `>=`, `>`) bez jediného řádku kódu.
* **Widgety na ploše — vrstva, co Windows nikdy neměly:**
  * Volně plovoucí nativní widgety (pilulky) kreslené vestavěným WPF enginem — **nula WebView2, minimum RAM**. Připneš je k libovolné hraně obrazovky, nebo přepneš na **volný režim** a zaparkuješ kamkoliv s přesnými X/Y.
  * **Chyť a táhni je přímo po ploše** v Edit módu (`Ctrl+Alt+E`) — pozice se sama uloží a po dokončení se vrací click-through.
  * Pro každý widget: vodorovná či svislá orientace, vlastní jméno (vidět v tray submenu), **témata ve stylu FanControlu** místo nekonečného ladění barev, celková průhlednost + zvlášť alfa podkladu a radius rohů (defaultně kapsle, `0` = hranaté).
  * Každý widget je řada (nebo sloupec) živých hodnot s vlastním skinem — FPS, frametimes, CPU, RAM, zátěž a teplota GPU… co zdroj vybereš. `start-widget` je v balení hned od první instalace, widgety se přepínají rovnou z tray menu a spravuje je samostatné okno Widgety.
* **Render motor na každý monitor zvlášť:**
  * `webview` nebo `native` per display — nativní engine kreslí `data` a `box` nody layoutu přímo ve WPF, **úplně bez WebView2 procesu** na dané obrazovce: míň RAM, okamžité kreslení a fixní číslicové sloty, takže hodnoty nikdy neposkakují.
* **RTSS OSD do hry:**
  * Živý text libovolného widgetu proudí do **RivaTuner Statistics Server** sdílené paměti — statistiky přímo ve hrách a exkluzivním fullscreenu, kam se běžný overlay nedostane (ověřeno naživo s RTSS 7.3.7).
* **Auto profily (HUD podle hry):**
  * Layout se přepne automaticky při spuštění hry nebo libovolného procesu — závodní HUD po startu, po vypnutí zpátky na čistou plochu. Detekce podle názvu procesu nebo hry ze SimHubu (částečná shoda).
  * Pro jednotlivé nebo všechny monitory, včetně pravidel „HUD vypnutý" — třeba závod na hlavním monitoru a postranní zhasnuté.
* **Řízení ventilátorů (bezpečné, na úrovni hw):**
  * Ovládání hlaviček ventilátorů desky (SuperIO čip přes PawnIO — jako FanControl), větráků GPU i USB řadičů — auto / manuální % / teplotní křivka.
  * Křivky s 2–6 body a hysterezí pro každou křivku; identifikace roztočí kanál na 100 %, aby bylo poznat, který větrák to fyzicky je.
  * Bezpečí vestavěné: spodní limit 20 %, okamžitý návrat na hardware-auto při kritické teplotě a hlídací guardian proces, který vrátí řízení i při pádu aplikace.
* **HW info — PC na jeden pohled:**
  * Verze Windows, BIOS, deska, CPU (jádra/socket/takt), GPU (VRAM/ovladač), moduly RAM a disky s kapacitou — v okně z tray, na stránce v nastavení i v přiloženém layoutu `hw-info`. Náhrada výpisu HWiNFO.
* **Upozornění a detekce bottlenecku:**
  * Pravidla „klíč >= / <= hodnota" nad libovolnou telemetrií s pípnutím nebo hlasovou hláškou Windows (s pauzou mezi opakováním).
  * Klíče `Sys.Limit` / `Sys.Throttle` ukážou, co brzdí FPS — GPU, CPU nebo teplotní throttle.
* **Skutečná podpora více monitorů a úspora RAM:**
  * Každý monitor může mít vlastní layout i nezávislou obnovovací frekvenci (Plná / 60 / 30 / 20 / 10 / 5 Hz).
  * Volba mezi **sdíleným plátnem** (jeden WebView2 renderer pro všechny monitory — úspora ~140 MB RAM na každý další monitor) nebo **oddělenými okny**.
* **15 vyladěných šablon v balíčku:**
  * Obsahuje layouty `start`, `race-minimal`, `race-hud`, `race-pro`, `race-pro-2`, `race-hw`, `system-hw`, `system-hud`, `hw-info`, `media-eq`, `media-hud`, `media-hud-2`, `combo-desk`, `combo-hud` a `sci-fi`.
* **7 jazyků a nativní vzhled Windows 11/10:**
  * Kompletně v **češtině, angličtině, němčině, španělštině, francouzštině, italštině a polštině**. Automaticky přebírá akcentovou barvu a tmavý/světlý motiv Windows.

---

### Rychlý start

1. **Instalace:** Spusť `chicago overlay setup <ver>.exe` (~70 MB, obsahuje prerekvizity .NET 8 a WebView2). Instalátor sám ověří `.NET 8` / `WebView2` a nasadí plugin `Chicago.Bridge.dll` přímo do složky SimHubu.
2. **Povolení v SimHubu:** Spusť SimHub a potvrď povolení pluginu **Chicago Overlay** (případně kdykoliv aktualizuj na jedno kliknutí z menu v tray nebo v *Nastavení → Zdroje*).
3. **Úpravy:** Stiskni **`Ctrl+Alt+E`** pro zapnutí **Edit módu** a otevření Inspektoru. Klávesou **`Ctrl+Alt+H`** skryješ/zobrazíš HUD a **`Ctrl+Alt+I`** identifikuješ monitory.

---

### Příběh projektu (Slovo autora)

Chicago Overlay nevznikl v moderní kanceláři — celý projekt byl napsán a odladěn v **obytném karavanu Wohnwagenwerk z roku 1984**, který je mým domovem. Svým způsobem to k motorsportu krásně sedí: rok 1984 byl zlatou érou Formule 1, kdy závodníci i konstruktéři bydleli a pracovali přímo ve svých karavanech v padoku.

Protože bydlím v místě, kde pro mě na trhu práce není uplatnění, stal se vývoj tohoto nástroje cestou, jak zúročit zkušenosti staré počítačové školy — s důrazem na poctivé řemeslo, žádná tichá selhání a maximální ohled na každý megabajt paměti i každé FPS.

**Vaše zpětná vazba určuje další směr:**
Každý nápad, názor, hlášení chyby nebo vlastní layout od komunity je upřímně vítán. Pokud bude o nástroj zájem, rád ho budu rozvíjet dál a mohu nabídnout i individuální přístup při ladění pro jednotlivce nebo e-sportové týmy.

Pokud vám Chicago Overlay dělá radost a chcete podpořit jeho další vývoj (nebo mi jen pomoct v nelehké životní situaci), jakýkoliv dobrovolný příspěvek pro mě bude mít obrovskou hodnotu — nejen jako uznání odvedené práce, ale i jako skutečná pomoc:

**[Podpořit přes Ko-fi (Karta / Apple Pay / Google Pay / PayPal)](https://ko-fi.com/radimsvatek)**

*P.S. Projekt má pořád 0 hvězdiček — když ti Chicago udělá radost, kliknutí na ⭐ nic nestojí a hrozně pomůže, aby ho vůbec někdo našel.*

Díky za vyzkoušení — vidíme se na trati!

---

### Licence a distribuce

* **Aplikace (`Chicago Overlay`):** **Donationware / Freeware** — zcela zdarma ke stažení a používání, bez uzamčených funkcí nebo předplatného. Pokud se vám líbí, budu moc rád za jakýkoliv dobrovolný příspěvek přes [Ko-fi](https://ko-fi.com/radimsvatek). Šíření upravených binárních souborů nebo komerční prodej bez povolení není dovolen.
* **Zdrojový kód:** není veřejný — drží jej autor v privátním režimu. Jakékoliv použití kódu v jiných projektech nebo produktech vyžaduje svolení autora.
* **Layouty a jazykové balíčky (`.json`):** volné k použití, úpravám a sdílení v rámci komunity.
* **Záruka:** software je poskytován "tak jak je", bez jakékoliv záruky. Použití na vlastní riziko.
