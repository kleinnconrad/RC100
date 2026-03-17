# 🧪 Testprotokoll - Leerlaufdrehzahl & Top-Speed Kalkulation

**Datum:** 17.03.2026
**Status:** Erfolgreich abgeschlossen

## 📝 Versuchsaufbau & Methodik

* **Messmethode:** Optische Drehzahlerfassung (RPM) mittels Lasertachometer.
* **Testumgebung:** Unloaded Test (Fahrzeug aufgebockt, Antriebsstrang läuft ohne Bodenkontakt/Lastwiderstand).
* **Durchführung:** Ein Reflexionsstreifen wurde zur sauberen Signalgebung auf die Außenflanke des rechten Hinterrades geklebt. Die Messung erfolgte bei 100 % Gashebelstellung über die Carson-Fernsteuerung.
* **Ergebnis:** Das System lief stabil und ohne Aussetzer. Es wurde eine maximale Raddrehzahl von **11.200 RPM** erfasst.

## 🧮 Berechnung der theoretischen Höchstgeschwindigkeit

Die theoretische Radgeschwindigkeit ohne Last (Wheel Speed) wird aus dem Raddurchmesser (d = 64 mm) und der ermittelten Drehzahl abgeleitet.

Formel: v = (d * π * rpm * 60) / 1.000.000

v = (64 * 3.14159 * 11200 * 60) / 1.000.000
**v ≈ 135,11 km/h**

> **Aerodynamischer Reality Check:** Die errechneten ~135 km/h repräsentieren die mechanische Maximalgeschwindigkeit im luftleeren Raum ohne Fahrwiderstände. Unter realen Bedingungen auf dem Asphalt (Luftwiderstand der Karosserie, Rollwiderstand, Spannungsabfall des LiPos unter Last) muss mit einem Verlust von ca. 20 bis 25 % gerechnet werden. Mit diesem Setup befindet sich das Fahrzeug rechnerisch exakt im Sweet Spot, um die anvisierten echten 100 km/h auf der Straße (GPS-gemessen) sicher und wiederholbar zu knacken.
