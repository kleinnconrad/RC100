## 🧪 Meilenstein 1: No-Load RPM Test (Antriebsstrang "Unit-Test")

Dieses Protokoll dient der Validierung des isolierten Antriebsstrangs auf dem Prüfstand (ohne Räder, ohne Last). Ziel ist es, die mechanische Integrität und die Ziel-Drehzahlen bei 3S-Spannung zu verifizieren, bevor Störfaktoren wie Aerodynamik oder Reibung (Track-Test) hinzukommen.

### 📝 Test-Metadaten
* **Datum:** [TT.MM.YYYY]
* **Git-Branch:** `main` (oder spezifischer Test-Branch)
* **Akku-Spannung (Start):** [z.B. 12.5V - Vollgeladen]
* **Regler-Settings (ESC):** Timing [0°], Punch [Level 3]

### 🛠️ Messmethode: Optischer Laser-Tachometer
Um die extremen Drehzahlen sicher und berührungsfrei zu erfassen, nutzen wir einen digitalen Laser-Drehzahlmesser (Photo Tachometer).
**Durchführung der Messung:**
1. **Präparieren:** Schneide ein winziges Quadrat (ca. 5x5 mm) des dem Messgerät beiliegenden Reflexionsklebebands ab.
2. **Markieren:** Klebe es exakt auf das zu messende rotierende Bauteil (siehe Tabelle unten).
3. **Messen:** Richte den Laser des Tachometers aus sicherer Entfernung auf das rotierende Teil.
4. **Auslesen:** Der Sensor erfasst bei jeder Umdrehung den Lichtblitz des Klebebands und berechnet daraus die exakten RPM (Revolutions per Minute).

### ⚙️ Test-Szenarien & RPM-Messung
> **⚠️ SICHERHEITSHINWEIS:** Gashebel extrem langsam hochziehen! Schutzbrille zwingend tragen! Maximal 10 Sekunden Vollgas am Stück, um eine Überhitzung durch fehlende Kühlluft zu vermeiden.

| Test-ID | Messpunkt (Reflexionsband) | Erwartete Drehzahl (RPM) | Gemessene Drehzahl (RPM) | Pass / Fail |
| :--- | :--- | :--- | :--- | :--- |
| `TC-01` | Motorritzel (Flache Seite) | ~ 44.000 | [ 00.000 ] | [ ] |
| `TC-02` | Hauptwelle (Alu-Mittelwelle) | ~ 26.000 | [ 00.000 ] | [ ] |
| `TC-03` | Radachse / Sechskant-Mitnehmer | ~ 10.400 | [ 00.000 ] | [ ] |

### 🔍 Post-Test Inspektion (Mechanischer Health-Check)
Nach den Vollgas-Zyklen sind folgende Parameter zwingend zu prüfen, um strukturelle Probleme frühzeitig zu erkennen:

* [ ] **Temperatur-Check:** Motor und ESC sind unter 60°C geblieben? *(Messwert: [ ] °C)*
* [ ] **Zahnflankenspiel (Gear Mesh):** Hat sich der Motorhalter durch die extremen Vibrationen verschoben? (Den "Papier-Test" zur Sicherheit wiederholen).
* [ ] **Schwingungsanalyse:** Gab es extreme Unwuchten oder unnatürliches "Schlagen" der Kardan-Gelenke (Dogbones) im Leerlauf?
* [ ] **Sichtprüfung Verschleiß:** Sind Kunststoffsplitter, Staub oder Abrieb unter dem Hauptzahnrad zu finden?

**Notizen / Auffälligkeiten zur Fehlerbehebung:**
> *[Hier dokumentieren, falls z.B. das Timing am ESC reduziert werden muss, weil der Motor im Leerlauf zu heiß wird, oder ob das Gear Mesh korrigiert wurde.]*
