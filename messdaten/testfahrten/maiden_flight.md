# Testbericht - Maiden Flight (Erste Testfahrt auf Asphalt)

**Datum:** 17.03.2026
**Umgebung:** Reale Testumgebung (Asphalt)
**Status:** ❌ Gescheitert (Testabbruch)

## 📸 Visuelle Schadensdokumentation

![Schadensbild Antriebsstrang 1](https://github.com/kleinnconrad/RC100/blob/main/messdaten/fotos/PXL_20260317_162312395.jpg?raw=true)
*Abbildung 1: Zustand des Antriebsstrangs nach dem Testabbruch.*

![Schadensbild Antriebsstrang 2](https://github.com/kleinnconrad/RC100/blob/main/messdaten/fotos/PXL_20260317_162327676.MP.jpg?raw=true)
*Abbildung 2: Detailaufnahme der Schäden an Hauptzahnrad und Ritzel.*

## Schadensbericht & Mechanische Analyse

* **Kritischer Montagefehler (Antriebsstrang):** Die Madenschraube des Motorritzels war unzureichend fixiert (bzw. nicht korrekt auf der flachen Stelle der Motorwelle positioniert). Durch die hohen Fliehkräfte und Vibrationen ist das Hartstahl-Ritzel auf der Welle nach vorne gerutscht.
* **Totalschaden Getriebe:** Das Verrutschen führte zu einem asymmetrischen Eingriff der Zahnräder. Das Hauptzahnrad (Spur Gear) aus Kunststoff wurde dadurch komplett abrasiert/zerstört. Gleichzeitig hat sich die Bohrung des Motorritzels durch die extreme Hebelwirkung und das Durchdrehen auf der Welle irreparabel verformt.
* **Architektur-Entscheidung (Upgrade):** Das werkseitige Kunststoff-Hauptzahnrad hat sich als offensichtlicher Schwachpunkt für ein 3S/120A-Setup erwiesen. Als Corrective Action werden sowohl das Motorritzel als auch das Hauptzahnrad durch Komponenten aus härterem Material (CNC-gefrästes Delrin & Hartstahl) ersetzt, um die Antriebskräfte in Zukunft sicher zu übertragen.

## Analyse Steuerung & Elektronik

* **Kalibrierungs-Defizite:** Die Abstimmung zwischen der Carson-Fernsteuerung und dem Fahrzeug war fehlerhaft. Die Lenkung war nicht sauber getrimmt, was zu einem unruhigen, instabilen Geradeauslauf führte.
* **Gas-Annahme (Deadband/Cogging):** Die Nullpunkt-Position (Neutralstellung) des Gashebels wurde vom ESC nicht exakt erkannt. Dies führte dazu, dass das Fahrzeug beim Anfahren aus dem Stillstand teilweise Befehle komplett ignorierte oder stark verzögert reagierte. Eine saubere Endpunkt-Kalibrierung (Vollgas/Bremse/Neutral) ist zwingend erforderlich.

## Next Steps & Corrective Actions
1. Beschaffung eines neuen 48DP Motorritzels aus gehärtetem Stahl (5mm Bohrung).
2. Beschaffung eines Upgrade-Hauptzahnrads (z.B. Kimbrough 72T 48DP) kompatibel mit dem Carten T410R Mitnehmer.
3. Sichere Montage des neuen Ritzels mit mittelfester Schraubensicherung (Loctite).
4. Neukalibrierung des Hobbywing ESC an die Carson-Fernsteuerung (mechanische Endpunkte anlernen). 
