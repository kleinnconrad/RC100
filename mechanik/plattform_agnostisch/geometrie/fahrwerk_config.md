## Fahrwerksgeometrie: Spur & Sturz (Das 100 km/h Setup)

Die Fahrwerksgeometrie entscheidet bei extremen Geschwindigkeiten darüber, ob das Auto stabil geradeaus fährt oder unkontrollierbar ausbricht. Hier sind die wichtigsten physikalischen Parameter und unser spezifisches Speedrun-Setup.

### 1. Spur (Toe)
Die Spur beschreibt den Winkel der Räder im Verhältnis zur Längsachse des Autos, **wenn man von oben herabschaut**.



* **Vorspur (Toe-in):** Die Räder zeigen an der Front leicht nach **innen** (`/ \`).
  * *Effekt:* Das Auto will stur geradeaus fahren und stabilisiert sich selbst. Es lenkt in Kurven träger ein.
* **Nachspur (Toe-out):** Die Räder zeigen an der Front leicht nach **außen** (`\ /`).
  * *Effekt:* Das Auto lenkt extrem aggressiv in Kurven ein, wird aber auf der Geraden extrem nervös und beginnt zu "schwimmen".

### 2. Sturz (Camber)
Der Sturz beschreibt den Winkel der Räder, **wenn man von vorne oder hinten auf das Auto schaut**.



* **Negativer Sturz:** Die Räder kippen an der Oberseite in Richtung Chassis-Mitte (`/ \`).
  * *Effekt:* Beim Wanken in der Kurve drückt sich das äußere Rad flach auf den Asphalt und generiert maximalen Grip.
* **Positiver Sturz:** Die Räder kippen oben nach außen (`\ /`).
  * *Effekt:* Fährt sich instabil und hat im Onroad-RC-Bereich keinen Nutzen.
* **Neutraler Sturz (0°):** Das Rad steht exakt senkrecht (`| |`).
  * *Effekt:* Maximale Auflagefläche auf der Geraden (solange sich der Reifen nicht durch Fliehkraft verformt).

---

### Setup-Plan (Carten T410R)

Für einen kompromisslosen Speedrun (exakt geradeaus, maximale Stabilität) gilt folgendes Basis-Setup:

| Achse / Parameter | Einstellung | Physikalischer Grund für 100 km/h |
| :--- | :--- | :--- |
| **Vorderachse: Spur** | **0° (Neutral)** | Kein Bremswiderstand durch "schräg" stehende Räder. Das Lenkservo hält das Auto auf Kurs. |
| **Hinterachse: Spur** | **2.5° bis 3° Vorspur** | **Extrem wichtig!** Der aerodynamische "Anker". Zwingt das Heck, immer hinter der Front zu bleiben. Ohne Vorspur dreht sich das Auto bei 80 km/h sofort um die eigene Achse. *(Beim Carten T410R oft durch die hinteren Querlenkerhalter / Toe-Blocks vorgegeben).* |
| **Sturz (Vorne & Hinten)**| **-0.5° bis -1.0° (Leicht Negativ)**| Nicht komplett 0°, da sich der Gummi-Reifen bei 10.000 U/min durch die Fliehkraft in der Mitte minimal aufbläht (Ballooning). Der winzige negative Sturz kompensiert das, sodass die Lauffläche bei Top-Speed plan auf dem Asphalt bleibt. |

### Einstellung am Chassis
Beim Carten T410R wird die Geometrie über die **Spurstangen** (Turnbuckles – Metallstäbe mit Rechts-/Linksgewinde) eingestellt:
* **Spur (Vorne):** Änderung der Länge an den Stangen des *Lenkgestänges*.
* **Sturz:** Änderung der Länge an den *oberen Querlenkern*.
