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
* **Echte Multi-Monitor-Unterstützung & geringer RAM-Verbrauch:**
  * Jedem Monitor lassen sich ein eigenes Layout sowie eine unabhängige Bildwiederholrate (Volle Geschwindigkeit / 60 / 30 / 20 / 10 / 5 Hz) zuweisen.
  * Wahl zwischen **Shared Canvas** (ein einziger WebView2-Renderer für alle Monitore — spart ca. 140 MB RAM pro zusätzlichem Bildschirm) oder **Split Canvas**.
* **14 einsatzbereite Vorlagen enthalten:**
  * Enthält die Layouts `start`, `race-minimal`, `race-hud`, `race-pro`, `race-pro-2`, `race-hw`, `system-hw`, `system-hud`, `media-eq`, `media-hud`, `media-hud-2`, `combo-desk`, `combo-hud` und `sci-fi`.
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

Vielen Dank fürs Ausprobieren — wir sehen uns auf der Strecke!

---

### Lizenz & Vertrieb

* **Anwendung (`Chicago Overlay`):** **Donationware / Freeware** — komplett kostenlos herunterladbar und nutzbar, ohne gesperrte Funktionen oder Abonnements. Wenn dir das Programm gefällt, freue ich mich sehr über jeden freiwilligen Beitrag über [Ko-fi](https://ko-fi.com/radimsvatek). Die Weitergabe veränderter Programmdateien oder der kommerzielle Weiterverkauf ohne Genehmigung ist nicht gestattet.
* **Quellcode:** nicht öffentlich — wird vom Autor privat gehalten. Jede Nutzung des Codes in anderen Projekten oder Produkten erfordert die Genehmigung des Autors.
* **Layouts & Sprachpakete (`.json`):** Frei nutzbar, anpassbar und innerhalb der Community teilbar.
* **Gewährleistung:** Die Software wird "wie besehen" bereitgestellt, ohne jegliche Gewährleistung. Nutzung auf eigenes Risiko.
