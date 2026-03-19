# Testbericht - Erste unstrukturierte Testfahrt

**Datum:** 17.03.2026  
**Status:** ❌ Gescheitert (Testabbruch)

## Schadensbericht

<img src="https://github.com/kleinnconrad/RC100/blob/main/messdaten/fotos/PXL_20260317_162312395.jpg" alt="Schadensbild Antriebsstrang 1" width="30%">
*Abbildung 1: Zustand des Antriebsstrangs nach dem Testabbruch.*

<img src="https://github.com/kleinnconrad/RC100/blob/main/messdaten/fotos/PXL_20260317_162327676.MP.jpg" alt="Schadensbild Antriebsstrang 2" width="30%">
*Abbildung 2: Detailaufnahme der Schäden an Hauptzahnrad und Ritzel.*
  
* **Kritischer Montagefehler (Antriebsstrang):** Die Madenschraube des Motorritzels war unzureichend fixiert (bzw. nicht korrekt auf der flachen Stelle der Motorwelle positioniert). Durch die hohen Fliehkräfte und Vibrationen ist das Hartstahl-Ritzel auf der Welle nach vorne gerutscht.
* **Totalschaden Getriebe:** Das Verrutschen führte zu einem asymmetrischen Eingriff der Zahnräder. Das Hauptzahnrad (Spur Gear) aus Kunststoff wurde dadurch komplett abrasiert/zerstört. Gleichzeitig hat sich die Bohrung des Motorritzels durch die extreme Hebelwirkung und das Durchdrehen auf der Welle irreparabel verformt.

## Punch zu hoch eingestellt für die lange Übersetzung 
Der Motor konnte bei der Übersetzung von 43 zu 72 Zähnen und einem Punch von 5 nicht oder kaum andrehen. **Zwingend erforderlich ist es den Punch auf 1 einzustellen und das Fahrzeug etwas anzuschieben**. Bei der Testfahrt ist der ESC beim anfahren öfter in die Notabschaltung gegangen.

## Motor falsch gepolt
Die gewählte Polung (technischer Vorwärtsgang) entsprach nicht dem physikalischen Vorwärtsgang. Unter der Vermutung die Drehrichtungen seien kommutativ, wurde bei der Testfahrt die Throttle Einstellung an der Fernsteuerung auf "REV" gesetzt. Dadurch wurde das Auto im technischen Rückwärtsgang nach vorne gefahren. Dies erklärt neben dem Punch und der langen Übersetzung das schwierige anfahren.

## Korrekturen
1. Beschaffung eines neuen 48DP Motorritzels aus gehärtetem Stahl (5mm Bohrung).
2. Beschaffung eines Upgrade-Hauptzahnrads (z.B. Kimbrough 72T 48DP) kompatibel mit dem Carten T410R Mitnehmer.
3. Sichere Montage des neuen Ritzels mit mittelfester Schraubensicherung (Loctite).
4. Neukalibrierung des Hobbywing ESC an die Carson-Fernsteuerung (mechanische Endpunkte anlernen). 
5. Punch unbedingt auf 1 setzen.
6. Fahrzeug beim anfahren leicht anschieben, um Notabschaltungen des ESC zu verhindern.
7. Motor umpolen.
