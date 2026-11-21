# Chicago Overlay

**Ein leichtgewichtiges, frei anpassbares Multi-Monitor-Telemetrie- und System-HUD-Overlay für Windows 10/11.**
Entwickelt für Sim-Racing (über SimHub) und PC-Hardware-Monitoring — ohne unnötigen Ballast, mit minimalem RAM-Verbrauch und integriertem visuellem Layout-Editor.

---

### Hauptfunktionen

* **Universelle Telemetrie- & Systemdaten:**
  * **Sim-Racing (SimHub Bridge):** Volle Unterstützung für über 600 SimHub-Werte (Geschwindigkeit, Drehzahl, Gang, Live-Delta, Sektor- und Rundenzeiten mit automatischer violetter/grüner/gelber Statusfärbung, Abstände, Reifen- und Bremstemperaturen sowie -drücke, Kraftstoff, Flaggen, Pedal-Graphen). Inklusive automatischer Plugin-Installation und Versionsprüfung.
  * **DirectX-FPS & Frametimes:** Herstellerunabhängige FPS-Anzeige, Frametime-Graphen sowie CPU-/GPU-Framezeiten über Intel PresentMon (funktioniert im Vollbild- sowie im rahmenlosen Fenstermodus).
  * **Hardware-Sensoren:** Echtzeit-Temperaturen für CPU/GPU, Leistungsaufnahme (W), Auslastung, RAM sowie Mainboard-Lüfterdrehzahlen über LibreHardwareMonitor und den signierten PawnIO-Treiber.
  * **Desktop & Multimedia:** Uhrzeit, Datum und ein Echtzeit-Audio-Spektrum-Visualizer (8 wählbare EQ-Engines) inklusive Anzeige des aktuell abgespielten Titels.
* **Integrierter visueller HUD-Editor (`Strg+Alt+E`):**
  * Drag-and-Drop-Platzierung, Mehrfachauswahl (Auswahlrahmen), einrastendes Raster mit konfigurierbaren Hauptlinien, bildschirmweites Fadenkreuz und Hintergrundabdunklung für entspanntes Bearbeiten.
  * Vielfältige visuelle Elemente: Datenfelder, Balken (einfarbig, Farbverlauf, HSL-Spektrum, LED-Segmente, Leuchteffekt, Spiegelung), Liniendiagramme, Flaggen, Sektoren, Rundenzeiten und Status-Boxen.
  * **Intelligente bedingte Regeln:** 3-stufige Farbschwellenwerte, blinkende Warnungen und Sichtbarkeitsregeln (`<`, `<=`, `=`, `!=`, `>=`, `>`) ganz ohne Programmierkenntnisse.
* **Desktop-Widgets — die Ebene, die Windows nie hatte:**
  * Frei schwebende native Widgets (Pills), gezeichnet von der eingebauten WPF-Engine — **null WebView2, minimaler RAM-Verbrauch**. An jede Bildschirmkante andocken oder in den **Frei-Modus** schalten und mit pixelgenauem X/Y parken.
  * **Direkt auf dem Desktop greifen und ziehen** im Edit-Modus (`Strg+Alt+E`) — die Position speichert sich von selbst, Click-Through kehrt danach zurück.
  * Pro Widget: horizontale oder vertikale Ausrichtung, eigener Name (im Tray-Untermenü sichtbar), **Theme-Presets im FanControl-Stil** statt endloser Farbspielerei, Gesamt-Transparenz plus separates Hintergrund-Alpha und Eckenradius (standardmäßig Kapsel, `0` = eckig).
  * Jedes Widget ist eine Zeile (oder Spalte) Live-Werte mit eigenem Skin — FPS, Frametimes, CPU, RAM, GPU-Last & -Temperatur… je nach gewählter Quelle. Ein fertiges `start-widget` liegt ab der Erstinstallation bei, Widgets schalten sich direkt im Tray-Menü um, und ein eigenes Widget-Fenster verwaltet sie alle.
* **Render-Engine pro Monitor:**
  * `webview` oder `native` pro Anzeige wählbar — die native Engine zeichnet `data`- & `box`-Layoutknoten direkt in WPF, **ganz ohne WebView2-Prozess** auf diesem Bildschirm: weniger RAM, sofortiges Zeichnen und feste Ziffernslots, sodass Werte nie zittern.
* **RTSS-Ingame-OSD:**
  * Live-Text jedes Widgets in den **RivaTuner Statistics Server** Shared Memory streamen — Statistiken in exklusivem Vollbild, wo normale Overlays nicht hinkommen (live verifiziert mit RTSS 7.3.7).
* **Auto-Profile (spielabhängiges HUD):**
  * Wechselt Layouts automatisch, wenn ein Spiel oder ein beliebiger Prozess startet — Renn-HUD beim Start, nach dem Beenden zurück zum aufgeräumten Desktop. Erkennung über Prozessname oder SimHub-Spielname (Teilübereinstimmung).
  * Pro Monitor oder für alle, plus „HUD aus"-Regeln — z. B. Rennlayout auf dem Hauptbildschirm, Seitenmonitore dunkel.
* **Lüftersteuerung (sicher, auf Hardware-Ebene):**
  * Steuerung der Mainboard-Lüfter-Header (SuperIO-Chip über PawnIO — wie FanControl), GPU-Lüfter und USB-Lüftercontroller — Auto / manuell % / Temperaturkurve.
  * Kurven mit 2–6 Ankern und Hysterese pro Kurve; Lüfter-Identifikation dreht einen Kanal auf 100 %, damit du erkennst, welcher Header welcher ist.
  * Sicherheit eingebaut: 20%-Minimum, sofortige Rückkehr zu Hardware-Auto bei kritischen Temperaturen und ein Guardian-Watchdog-Prozess, der die Steuerung selbst bei einem App-Absturz zurücksetzt.
* **HW-Info — dein PC auf einen Blick:**
  * Windows-Version, BIOS, Mainboard, CPU (Kerne/Sockel/Takt), GPU (VRAM/Treiber), RAM-Module und Festplatten mit Kapazität — im Tray-Fenster, auf einer Einstellungsseite und im mitgelieferten `hw-info`-Layout. Ersetzt die HWiNFO-Übersicht.
* **Warnungen & Bottleneck-Erkennung:**
  * Regeln „Schlüssel >= / <= Wert" über beliebiger Telemetrie mit Piep oder Windows-Sprachansage (mit Pause zwischen Wiederholungen).
  * `Sys.Limit` / `Sys.Throttle` zeigen, was deine FPS bremst — GPU, CPU oder Thermo-Throttle.
* **Echte Multi-Monitor-Unterstützung & geringer RAM-Verbrauch:**
  * Jedem Monitor lassen sich ein eigenes Layout sowie eine unabhängige Bildwiederholrate (Volle Geschwindigkeit / 60 / 30 / 20 / 10 / 5 Hz) zuweisen.
  * Wahl zwischen **Shared Canvas** (ein einziger WebView2-Renderer für alle Monitore — spart ca. 140 MB RAM pro zusätzlichem Bildschirm) oder **Split Canvas**.
* **15 einsatzbereite Vorlagen enthalten:**
  * Enthält die Layouts `start`, `race-minimal`, `race-hud`, `race-pro`, `race-pro-2`, `race-hw`, `system-hw`, `system-hud`, `hw-info`, `media-eq`, `media-hud`, `media-hud-2`, `combo-desk`, `combo-hud` und `sci-fi`.
* **7 Sprachen & natives Windows-11/10-Design:**
  * Verfügbar auf **Deutsch, Englisch, Tschechisch, Spanisch, Französisch, Italienisch und Polnisch** (sowohl Installer als auch App). Übernimmt automatisch die Windows-Akzentfarbe sowie den Dunkel-/Hellmodus.

---

### Schnellstart

1. **Installation:** Starte `chicago overlay setup <ver>.exe` (~70 MB, enthält .NET 8 & WebView2 Voraussetzungen). Der Installer erkennt `.NET 8` / `WebView2` automatisch und installiert das Plugin `Chicago.Bridge.dll` direkt in deinen SimHub-Ordner.
2. **In SimHub aktivieren:** Öffne SimHub und aktiviere das Plugin **Chicago Overlay**, sobald die Abfrage erscheint (oder nutze die Ein-Klick-Installation/-Aktualisierung im Tray-Menü der App bzw. unter *Einstellungen → Quellen*).
3. **Anpassen:** Drücke jederzeit **`Strg+Alt+E`**, um den **Edit-Modus** und den Inspektor zu öffnen. Mit **`Strg+Alt+H`** blendest du das HUD ein/aus und mit **`Strg+Alt+I`** identifizierst du deine Monitore.

---

### Hinter dem Projekt (Ein Wort vom Autor)

Chicago Overlay entstand nicht in einem modernen Großraumbüro — das gesamte Projekt wurde in einem **Wohnwagenwerk-Wohnwagen aus dem Jahr 1984** programmiert und getestet, der mein Zuhause ist. Auf gewisse Weise passt das perfekt zum Motorsport: 1984 war die goldene Ära der Formel 1, als Fahrer und Ingenieure noch direkt in ihren Wohnwagen im Fahrerlager lebten und arbeiteten.

Da ich in einer Region lebe, in der es für mich auf dem lokalen Arbeitsmarkt keine Einsatzmöglichkeiten gibt, wurde die Entwicklung dieses Tools zu meinem Weg, jahrzehntelange Erfahrung der alten PC-Schule sinnvoll einzusetzen — mit Fokus auf saubere Handwerkskunst, keinerlei stille Fehler und höchsten Respekt vor jedem Megabyte Arbeitsspeicher und jedem einzelnen Frame pro Sekunde.

**Euer Feedback bestimmt die Zukunft:**
Jede Idee, jeder Fehlerbericht, jedes geteilte Layout und jeder Vorschlag aus der Community ist herzlich willkommen. Wenn das Projekt auf Interesse stößt, entwickle ich es gerne weiter und biete auch individuelle Unterstützung für einzelne Fahrer sowie Sim-Racing-Teams an.

Wenn dir Chicago Overlay Freude bereitet und du die Weiterentwicklung unterstützen möchtest (oder mir einfach in einer nicht ganz einfachen Lebenssituation helfen willst), hat jeder freiwillige Beitrag für mich einen enormen Wert — sowohl als Anerkennung der Arbeit als auch als echte, praktische Hilfe:

**[Auf Ko-fi unterstützen (Karte / Apple Pay / Google Pay / PayPal)](https://ko-fi.com/radimsvatek)**

*P.S. Das Projekt steht immer noch bei 0 Sternen — wenn Chicago deinen PC etwas schöner macht, kostet ein ⭐ nichts und hilft wirklich, es überhaupt zu finden.*

Vielen Dank fürs Ausprobieren — wir sehen uns auf der Strecke!

---

### Lizenz & Vertrieb

* **Anwendung (`Chicago Overlay`):** **Donationware / Freeware** — komplett kostenlos herunterladbar und nutzbar, ohne gesperrte Funktionen oder Abonnements. Wenn dir das Programm gefällt, freue ich mich sehr über jeden freiwilligen Beitrag über [Ko-fi](https://ko-fi.com/radimsvatek). Die Weitergabe veränderter Programmdateien oder der kommerzielle Weiterverkauf ohne Genehmigung ist nicht gestattet.
* **Quellcode:** nicht öffentlich — wird vom Autor privat gehalten. Jede Nutzung des Codes in anderen Projekten oder Produkten erfordert die Genehmigung des Autors.
* **Layouts & Sprachpakete (`.json`):** Frei nutzbar, anpassbar und innerhalb der Community teilbar.
* **Gewährleistung:** Die Software wird "wie besehen" bereitgestellt, ohne jegliche Gewährleistung. Nutzung auf eigenes Risiko.
