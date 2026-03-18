# Hobbywing QuicRun 120A ESC

## 1. Kalibrierung des Gaswegs (Throttle Range Calibration)

### 1.1 Vorbereitung der Fernsteueranlage (Transmitter)
* Gastrimmung (Throttle Trim) auf den Wert 0 (Neutral) setzen.
* Endpunkte (EPA - End Point Adjustment) für Gas und Bremse auf 100% einstellen.
* ABS-Bremsfunktionen zwingend deaktivieren.
* Gaskanal-Invertierung prüfen (bei Futaba-Systemen i.d.R. "REV", bei anderen Herstellern "NOR").
* Fernsteuerung einschalten.

### 1.2 Durchführung der Kalibrierung
1. Fahrakku an den ausgeschalteten Regler (ESC) anschließen.
2. Die SET-Taste am Regler drücken und gedrückt halten.
3. Den Regler über den Hauptschalter einschalten.
4. Sobald die rote Status-LED zu blinken beginnt, die SET-Taste unverzüglich loslassen.
5. **Neutralpunkt:** Gashebel in Neutralstellung belassen. SET-Taste einmal drücken. Die grüne LED blinkt einmal zur Bestätigung.
6. **Vollgas-Endpunkt:** Gashebel auf maximale Vorwärts-Position (Vollgas) ziehen und am mechanischen Anschlag halten. SET-Taste einmal drücken. Die grüne LED blinkt zweimal.
7. **Vollbrems-Endpunkt:** Gashebel auf maximale Rückwärts-Position (Vollbremse) drücken und am mechanischen Anschlag halten. SET-Taste einmal drücken. Die grüne LED blinkt dreimal.
8. Gashebel in Neutralstellung zurückführen. Der Regler schließt den Initialisierungsprozess nach ca. drei Sekunden ab und ist betriebsbereit.

---

## 2. Parametrierung des "Punch" (Start Mode) via LED-Programmierkarte

### 2.1 Anschluss der Programmierkarte
1. Sicherstellen, dass der Regler ausgeschaltet ist.
2. Das Verbindungskabel der Programmierkarte in den dedizierten PRG-Anschluss (3-polig) des Reglers einstecken.
3. Polarität zwingend beachten: Das Massekabel (schwarz/braun) muss an den Minuspol (-), das Signalkabel (weiß/orange) an den Signalpol (S/P).
4. Das gegenüberliegende Ende des Kabels mit der Programmierkarte verbinden.

### 2.2 Einstellung des Parameters
1. Fahrakku anschließen und den Regler einschalten. Die numerische Segmentanzeige der Programmierkarte wird aktiviert.
2. Taste **ITEM** iterativ betätigen, bis der Parameter für "Start Mode / Punch" (i.d.R. Menüpunkt 4) auf dem linken Displayfeld angezeigt wird.
3. Taste **VALUE** betätigen, um den numerischen Wert zu spezifizieren.
   * *Hinweis für die vorliegende Hochlast-Übersetzung (43/72):* Wert zwingend auf **1 (Soft)** setzen, um kritische Einschaltströme (Blockierströme) zu minimieren und eine Auslösung der Überstromschutzschaltung zu verhindern.
4. Taste **OK** drücken, um den geänderten Wert in den nichtflüchtigen Speicher des Reglers zu schreiben. (Motor gibt i.d.R. ein akustisches Bestätigungssignal ab).
5. Regler ausschalten und die physische Verbindung zur Programmierkarte trennen.
