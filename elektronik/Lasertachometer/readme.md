# 🧪 Testbericht - Telemetrie & Werkzeuge

**Komponente:** Digitales Lasertachometer (Optische Drehzahlmessung)
**Datum:** 16.03.2026
**Status:** Verifiziert / Einsatzbereit

## 📝 Validierung & Erkenntnisse

* **Messmethode:** Das Lasertachometer wurde zur Validierung erfolgreich im RPM-Modus (Umdrehungen pro Minute) getestet.
* **Referenz-Testlauf:** Um die Genauigkeit der Messung zu verifizieren, wurde der Test an einem bekannten, bereits vorhandenen RC-Auto durchgeführt. Zur Erfassung des optischen Lasersignals wurde ein Reflexionsstreifen an der Außenflanke des Rades appliziert.
* **Plausibilitätsprüfung:** Der erfasste RPM-Wert und die daraus abgeleitete Geschwindigkeit sind absolut plausibel. Das Messgerät liefert verlässliche Daten und ist somit für die Datenerfassung am Carten T410R Speedrun-Projekt freigegeben.

## 🧮 Theoretische Geschwindigkeit

v = (d * π * rpm * 60) / 1000²

**Testrechnung mit den erfassten Werten:**
* Raddurchmesser (d): 64 mm
* Gemessene Drehzahl (rpm): 2340.2

v = (64 * 3.14159 * 2340.2 * 60) / 1.000.000
**v ≈ 28,23 km/h**

## 📸 Visuelle Dokumentation

![Lasertachometer Testaufbau](https://github.com/kleinnconrad/RC100/blob/main/elektronik/fotos/PXL_20260316_115617586.MP.jpg?raw=true)
