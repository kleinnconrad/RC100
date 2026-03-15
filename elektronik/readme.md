# 🛠️ Build Log - Carten T410R Speedrun Projekt

**Meilenstein:** Tag 3 - Elektronik-Integration & Antriebsstrang
**Datum:** 15.03.2026
**Status:** In Progress

## 📝 Fortschritt & Technische Erkenntnisse

* **Motor-Packaging (3660 vs. 3650):** Der Hobbywing 3660er Motor passt in das Chassis, bewegt sich jedoch an den Grenzen der physischen Toleranz. 
  > **Architektonische Note:** Laut Hersteller ist das Chassis primär für kürzere 3650er Motoren ausgelegt. Ein 3650er würde sich minimal in den 5 cm langen Bodenausschnitt des Chassis versenken. Der 3660er sitzt stramm, kollidiert aber nicht mit kritischen Antriebskomponenten.

* **Kalibrierung des Antriebsstrangs:** Das Zahnflankenspiel (Gear Mesh) zwischen dem Hartstahl-Ritzel und dem Hauptzahnrad wurde nach bewährter Best-Practice mit einem normalen Streifen Papier kalibriert. Dies stellt einen leichtgängigen Lauf sicher und verhindert bei hohen Drehzahlen sowohl übermäßige Reibungshitze als auch das "Strippen" der Zähne.

* **Energie-Packaging (LiPo):** Entgegen der Spezifikationen in der Carten-Bauanleitung lässt sich der 3 cm hohe Absima 3S-LiPo physisch einwandfrei im Batteriefach verbauen. Das ist ein kritischer Gewinn für die Energiebereitstellung des 120A Setups.

* **Thermisches Management (Custom Lüfter-Mod):** Der zuvor beschaffte Kühlkörper (für glatte 36er Motoren) erwies sich als inkompatibel mit dem geriffelten Gehäuse des Quicrun G2 Motors. Eine Montage hätte aufgrund der minimalen Kontaktfläche ohnehin zu keiner Kühlleistung geführt. 
  > **Lösung:** Der Lüfter wurde vom fehlerhaften Aluminium-Träger demontiert und direkt auf dem Motor fixiert. Der Airflow wird nun direkt in die werkseitigen Kühlrippen des Motorgehäuses geleitet.

* **ESC-Montage:** Der Fahrtenregler (ESC) wurde schwingungsgedämpft mittels doppelseitigem Klebeband sicher auf dem Chassis fixiert. 

* **Telemetrie-Infrastruktur:** Der Ruddog GPS Analyzer findet seinen festen Platz auf der Karbon-Mittelstrebe (Upper Deck). Diese Position schützt das Modul mechanisch bei Überschlägen und gewährt gleichzeitig eine ungestörte Sichtachse zum Himmel für einen schnellen Satelliten-Fix.

## 📸 Visuelle Dokumentation

![Elektronik Detail 1](https://github.com/kleinnconrad/RC100/blob/main/elektronik/fotos/PXL_20260315_082845293.MP.jpg?raw=true)
![Elektronik Detail 2](https://github.com/kleinnconrad/RC100/blob/main/elektronik/fotos/PXL_20260315_082910089.jpg?raw=true)
![Elektronik Detail 3](https://github.com/kleinnconrad/RC100/blob/main/elektronik/fotos/PXL_20260315_091731103.jpg?raw=true)
![Elektronik Detail 4](https://github.com/kleinnconrad/RC100/blob/main/elektronik/fotos/PXL_20260315_110323844.jpg?raw=true)
