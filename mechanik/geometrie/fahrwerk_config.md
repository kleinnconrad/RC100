## Fahrwerksgeometrie: Spur & Sturz (Das 100 km/h Setup)


## Inhaltsverzeichnis
* [Fahrwerksgeometrie: Spur & Sturz (Das 100 km/h Setup)](#fahrwerksgeometrie-spur--sturz-das-100-kmh-setup)
  * [1. Spur (Toe)](#1-spur-toe)
  * [2. Sturz (Camber)](#2-sturz-camber)
  * [Setup-Plan (Carten T410R)](#setup-plan-carten-t410r)
  * [Einstellung am Chassis](#einstellung-am-chassis)


Die Fahrwerksgeometrie entscheidet bei hohen Geschwindigkeiten darüber, ob das Auto stabil geradeaus fährt oder unkontrollierbar ausbricht. Hier sind die wichtigsten physikalischen Parameter und unser spezifisches Speedrun-Setup.

### 1. Spur (Toe)
Die Spur beschreibt den Winkel der Räder im Verhältnis zur Längsachse des Autos, **wenn man von oben herabschaut**.



* **Vorspur (Toe-in):** Die Räder zeigen an der Front leicht nach **innen** (`/ \`).
  * *Effekt:* Das Auto will stur geradeaus fahren und stabilisiert sich selbst. Es lenkt in Kurven träger ein.
* **Nachspur (Toe-out):** Die Räder zeigen an der Front leicht nach **außen** (`\ /`).
  * *Effekt:* Das Auto lenkt stark aggressiv in Kurven ein, wird aber auf der Geraden stark nervös und beginnt zu "schwimmen".

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
| **Vorderachse: Spur** | **0° (Neutral)** | Minimierung des Rollwiderstands bei Geradeausfahrt. |
| **Hinterachse: Spur** | **2,5° Vorspur** | Erhöhung der Fahrstabilität. Verhindert das Ausbrechen der Hinterachse bei hohen Geschwindigkeiten. (Beim Carten T410R durch die hinteren Querlenkerhalter vorgegeben). |
| **Sturz (Vorne & Hinten)**| **0° (Neutral)** | Maximale Auflagefläche des Reifens bei Geradeausfahrt für optimale Traktion. |

### Einstellung am Chassis
Beim Carten T410R wird die Geometrie über die **Spurstangen** (Turnbuckles – Metallstäbe mit Rechts-/Linksgewinde) eingestellt:
* **Spur (Vorne):** Änderung der Länge an den Stangen des *Lenkgestänges*.
* **Sturz:** Änderung der Länge an den *oberen Querlenkern*.
