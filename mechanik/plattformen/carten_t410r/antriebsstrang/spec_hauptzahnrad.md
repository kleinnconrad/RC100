# ⚙️ Komponentenspezifikation - Upgrade Hauptzahnrad (Spur Gear)

**Komponente:** CNC-gefrästes Hauptzahnrad (z. B. Arrowmax, RW Racing, Revolution Design)
**Einsatzbereich:** Antriebsstrang (Iteration 2.0)
**Status:** Beschaffung ausstehend

## 📊 Technische Parameter

* **Zähnezahl (Teeth):** 72T
* **Zahnflankenprofil (Pitch):** 48 DP (Diametral Pitch) - *Muss exakt mit dem Motorritzel übereinstimmen!*
* **Material:** POM (Polyoxymethylen / Markenname: Delrin)
* **Fertigungsverfahren:** CNC-gefräst (Machined) aus dem Vollen, *nicht* im Spritzgussverfahren (Molded) hergestellt.
* **Befestigung:** Standard 1:10 Tourenwagen 4-Loch-Aufnahme (direkt kompatibel mit dem Carten T410R Aluminium-Mitnehmer).

## 🏗️ Architektonische Begründung (Materialwahl)

Der Wechsel von Baukasten-Kunststoff auf gefrästes CNC-Delrin (und bewusst nicht auf Stahl) basiert auf folgenden Engineering-Prinzipien für Hochgeschwindigkeits-Setups:

* **Maximale Rundlaufgenauigkeit:** Spritzguss-Zahnräder aus dem Baukasten können beim Abkühlen minimal schrumpfen und eiern. Ein CNC-gefrästes Delrin-Rad ist absolut zentrisch. Dies eliminiert Vibrationen und Resonanzen im Antriebsstrang bei Drehzahlen von über 11.000 RPM.
* **Reibung & Thermik:** POM/Delrin ist ein thermoplastischer Hochleistungskunststoff mit exzellenten, selbstschmierenden Gleiteigenschaften. In Kombination mit einem gehärteten Stahl-Motorritzel sorgt dies für minimale Reibungsverluste und maximale Kraftübertragung ohne externe Schmierung.
* **Geringe rotierende Masse:** Im Gegensatz zu einem massiven Stahl-Zahnrad hält Delrin das Gewicht des Antriebsstrangs extrem niedrig. Der Motor muss keine schwere Schwungmasse beschleunigen, was das Ansprechverhalten und die Beschleunigung massiv verbessert.
* **Mechanischer Fail-Safe:** Sollte der Antriebsstrang blockieren, fungiert das Delrin-Rad weiterhin als Sollbruchstelle. Es schützt somit teurere Komponenten wie die Motorwelle vor dem Verbiegen oder den ESC vor dem Durchbrennen.

## 🛠️ Montage-Voraussetzungen & Corrective Actions

> **Kritischer Montage-Standard:** Das neue Hauptzahnrad wird in Kombination mit einem neuen Hartstahl-Motorritzel (48 DP, 5 mm Bohrung) verbaut. Um den Fehler der ersten Testfahrt zu eliminieren, wird die Madenschraube des Ritzels zwingend mit mittelfester Schraubensicherung (z. B. Loctite 243 / blau) auf der Abflachung der Motorwelle gesichert. Das Zahnflankenspiel wird erneut mit der Papiermethode kalibriert.
> 
