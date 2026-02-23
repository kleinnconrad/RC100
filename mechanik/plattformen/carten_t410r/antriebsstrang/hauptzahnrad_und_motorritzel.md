# Spezifikation: Carten T410R Speed-Getriebe (100 km/h an 3S)

## 1. Setup & Übersetzung

| Bauteil / Eigenschaft | Spezifikation / Wert |
| :--- | :--- |
| **Hauptzahnrad (Spur Gear)** | 64 Zähne (Pitch: 48dp), z. B. von Kimbrough |
| **Motorritzel (Pinion Gear)** | 38 Zähne (Pitch: 48dp), zwingend aus Stahl (z. B. Arrowmax) |
| **Interne Getriebeuntersetzung** | 2,53 (Festwert des Carten T410R) |
| **Gesamtuntersetzung (FDR)** | 4,26 |

## 2. Physikalische Passgenauigkeit & Wichtige Hinweise

* **Passt das physikalisch in das Chassis?** Ja. Der Carten T410R nutzt ab Werk ein 72Z Hauptzahnrad. Wenn du dort ein riesiges 38Z Ritzel anbauen willst, blockiert der Motor am Chassis oder der Mittelwelle. Durch den Wechsel auf das kleinere 64Z Hauptzahnrad schrumpft der Durchmesser des Rades. Der Motor wandert dadurch näher an die Mittelachse, und das große 38Z Ritzel hat exakt den nötigen Platz im Verstellbereich des Aluminium-Motorhalters, ohne an das Oberdeck zu stoßen.
* **Die Berechnung:** Die Gesamtuntersetzung (Final Drive Ratio) berechnet sich wie folgt: (Hauptzahnrad ÷ Motorritzel) × Interne Untersetzung. Also: (64 ÷ 38) × 2,53 = 4,26. Dieser Wert ist der perfekte Kompromiss, damit der 4000kV Motor das Auto auf 100 km/h schiebt, ohne in den ersten 10 Sekunden durchzubrennen.
* **Zwingendes Ritzel-Material:** Da das Hauptzahnrad aus Kunststoff besteht (was wichtig ist, damit das Getriebe leise läuft und bei Schlägen nicht sofort bricht), muss das Motorritzel aus gehärtetem Stahl sein. Ein Aluminium-Ritzel würde sich bei dieser Leistung sofort abnutzen und das Hauptzahnrad mit zerstören.