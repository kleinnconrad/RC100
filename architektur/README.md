# 🏛️ Architecture Decision Records (ADRs)

Dieses Verzeichnis enthält alle grundlegenden architektur- und Hardwareentscheidungen für das RC100 Projekt. **Diese Datei wird automatisch generiert. Bitte nicht manuell bearbeiten.**

## 📋 Übersicht

| ID | Datum | Titel | Status | Entscheidung |
| :--- | :--- | :--- | :--- | :--- |
| **002** | N/A | N/A | 🟢 Akzeptiert | N/A |
| **ADR-001** | 2026-02-24 | Auswahl der Chassis-Plattform und Make-or-Buy-Entscheidung (100 km/h Benchmark) | 🟡 Offen | MAKE - Carten T410R |
| **ADR-003** | 2026-02-24 | Auswahl des LiPo-Akkus für 100 km/h Ziel. | 🟡 Offen | Absima GreenHorn Line V2 (3S / 5000mAh / 50C / Hardcase) |
| **ADR-004** | 2026-02-24 | Auswahl des Ladegeräts für 3S LiPo-Akkus | 🟡 Offen | SkyRC S100neo |
| **ADR-005** | 2026-02-24 | Auswahl der Fernsteuerungsanlage für 100 km/h Speedruns | 🟡 Offen | DumboRC X6 |
| **ADR-006** | 2026-02-24 | Auswahl des Lenkservos für präzise High-Speed-Kontrolle | 🟡 Offen | Savöx SC-1251MG+ |
| **ADR-007** | 2026-02-24 | Auswahl der aktiven und passiven Motorkühlung für 3S-Speedruns | 🟡 Offen | Passiver 36mm Alu-Kühlkörper kombiniert mit aktivem 40x40mm High-Speed Alu-Lüfter |
| **ADR-008** | 2026-02-25 | Auswahl der Bereifung (Belted Gummireifen für Asphalt) für 100 km/h Speedruns | 🟡 Offen | Sweep HANKOOK Tread Belted tires Pre-glued set Pro-compound 36deg for Asphalt (SR-SSF-36AWPG) |

---

## 📖 Detail-Protokolle

### 002: 
**Status:** Akzeptiert | **Datum:** 

#### Kontext
Kein Kontext angegeben.

#### Entscheidung
> **Ausstehend**

#### Begründung (Rationale)
Keine Begründung angegeben.

---

### ADR-001: Auswahl der Chassis-Plattform und Make-or-Buy-Entscheidung (100 km/h Benchmark)
**Status:** Offen | **Datum:** 2026-02-24

#### Kontext
Für das 100 km/h-Speedrun-Projekt wird eine mechanisch stabile Basis benötigt. Die Plattform muss 
extremen Belastungen (ca. 44.000 U/min am Motor, massive Fliehkräfte an den Achsen) standhalten. 
Die grundlegende Architektur-Frage (Make or Buy) vergleicht den Aufbau eines eigenen Budget-Kits ("Make") 
mit dem Kauf eines teuren, vormontierten High-End-Wettbewerbschassis ("Buy"). 
Ein kritisches Risiko für den 3S-Einsatz stellen Differentialzahnräder aus Kunststoff/Composite dar, 
die dem Drehmoment oft nicht standhalten.


#### Entscheidung
> **MAKE - Carten T410R**

#### Begründung (Rationale)
Die Entscheidung fällt auf die "Make"-Option mit dem Carten T410R (~ 180 €). 
Es ist das einzige Kit im Benchmark-Feld dieser Preisklasse, das die essenziellen Anforderungen 
für einen 3S/100 km/h-Run ab Werk vereint: 
1. Eine steife 3mm Carbon-Bodenplatte (verhindert gefährliches Flattern). 
2. Einen robusten Kardanantrieb (eliminiert das Risiko überspringender Riemen). 
3. Differential-Zahnräder aus Sintermetall (löst das KO-Kriterium der abscherenden Kunststoff-Diffs). 
Der massive Preisvorteil gegenüber dem Xray X4 '24 rechtfertigt den erhöhten manuellen Setup-Aufwand vollkommen.


#### Konsequenzen
- Die Metall-Differentiale des T410R müssen zwingend präzise geshimmt werden, um Spielfreiheit zu garantieren.
- Die zentrale Aluminium-Kardanwelle muss vor dem Einbau auf Rundlauf geprüft werden, da bei Kardan-Setups starke Vibrationen entstehen können.


---

### ADR-003: Auswahl des LiPo-Akkus für 100 km/h Ziel.
**Status:** Offen | **Datum:** 2026-02-24

#### Kontext
Um das RC100 Projekt auf über 100 km/h zu beschleunigen, muss die Energiequelle perfekt 
auf den 4000kV Motor und den 120A ESC (Hobbywing QuicRun) abgestimmt sein. 
Ein 2S LiPo (7.4V) würde nur ca. 29.600 U/min liefern, was für 100 km/h bei normaler 
Übersetzung nicht ausreicht. Daher ist ein 3S LiPo (11.1V) zwingend erforderlich, um 
die rechnerischen ~44.400 U/min zu erreichen. Zudem muss der Akku kurzzeitig extreme 
Ströme liefern können, ohne in der Spannung einzubrechen (Voltage Sag), und bei einem 
eventuellen Crash bei hoher Geschwindigkeit physisch geschützt sein.


#### Entscheidung
> **Absima GreenHorn Line V2 (3S / 5000mAh / 50C / Hardcase)**

#### Begründung (Rationale)
Die Entscheidung fällt auf den Absima GreenHorn V2 3S LiPo. Mit 50C Entladerate bietet er 
genügend Puffer für die massiven Stromspitzen beim Beschleunigen der 64Z/38Z Übersetzung. 
Das Hardcase ist ein absolutes Sicherheits-Muss für Speedruns, da ein Einschlag bei 100 km/h 
einen Softcase-LiPo sofort zerstören und entzünden würde. Der vorkonfektionierte XT60-Stecker 
garantiert einen geringen Übergangswiderstand für die hohen Ströme.


#### Konsequenzen
- Chassis-Modifikation: Da 3S Hardcase-Akkus ca. 35mm hoch sind, muss die obere Carbon-Akkustrebe im Carten T410R mit 10mm Spacern und längeren M3-Schrauben erhöht werden.
- Stecker-Kompatibilität: Der Hobbywing-Regler muss zwingend mit einem passenden XT60-Stecker verlötet werden (keine Tamiya-Stecker bei diesen Strömen!).
- Sicherheit: Laden und Lagern des Akkus (55.5 Wh) darf nur unter Aufsicht in einem Bat-Safe oder einer feuerfesten LiPo-Tasche erfolgen.


---

### ADR-004: Auswahl des Ladegeräts für 3S LiPo-Akkus
**Status:** Offen | **Datum:** 2026-02-24

#### Kontext
Das Laden des im ADR-003 definierten 3S LiPo-Akkus (11.1V, 5000mAh, 55.5 Wh) erfordert ein 
sicheres und leistungsfähiges Ladegerät. Um den Akku schonend mit 1C (5 Ampere) zu laden, 
wird eine Ladeleistung von mindestens 63 Watt (5 Ampere * 12.6V Ladeschlussspannung) benötigt. 
Zudem muss das Ladegerät die Zellenspannungen (Balancing) exakt überwachen und den internen 
Widerstand der Zellen messen können, um Brandgefahr vorzubeugen. Der Anschluss muss die 
hohen Ströme sicher über einen XT60-Stecker übertragen können.


#### Entscheidung
> **SkyRC S100neo**

#### Begründung (Rationale)
Die Entscheidung fällt auf das SkyRC S100neo. Es deckt den "Sweet Spot" zwischen Sicherheit, 
Leistung und Budget perfekt ab. Die 100 Watt interne Leistung (AC) sind mehr als ausreichend, 
um den 3S 5000mAh LiPo in etwa einer Stunde schonend vollzuladen. Besonders vorteilhaft ist 
der fest in der Frontblende integrierte XT60-Anschluss, der gefährliche und fehleranfällige 
Adapterkabel überflüssig macht. Dies passt perfekt zur Architektur-Entscheidung des Absima-Akkus.


#### Konsequenzen
- Sicherheit beim Laden: Neben dem XT60-Hauptstecker muss zwingend das weiße JST-XH Balancer-Kabel des Akkus in den Port des Ladegeräts gesteckt werden, da sonst die Einzelzellen nicht überwacht werden.
- Kabel-Minimalismus: Es werden keine zusätzlichen Ladekabel benötigt (Akku wird direkt an das Gerät gesteckt).
- Kühlung: Das Ladegerät verfügt über einen aktiven Lüfter. Beim Laden muss auf einen sicheren Stand und freie Luftzufuhr geachtet werden.


---

### ADR-005: Auswahl der Fernsteuerungsanlage für 100 km/h Speedruns
**Status:** Offen | **Datum:** 2026-02-24

#### Kontext
Ein RC-Car, das mit 100 km/h (ca. 27,7 Meter pro Sekunde) fährt, legt in wenigen Sekunden 
enorme Distanzen zurück. Die Fernsteuerung (Transmitter) und der Empfänger (Receiver) 
müssen daher zwingend eine extrem hohe und stabile Reichweite (300 bis 400 Meter) aufweisen, 
damit das Fahrzeug am Ende der Beschleunigungsstrecke nicht außer Kontrolle gerät. 
Zudem ist bei diesen Geschwindigkeiten eine elektronische Stabilisierungshilfe (Gyro) 
im Empfänger hochgradig empfehlenswert, um das Fahrzeug beim kleinsten Ausbrechen 
automatisch in der Spur zu halten.


#### Entscheidung
> **DumboRC X6**

#### Begründung (Rationale)
Die Entscheidung fällt auf die DumboRC X6. Sie bietet exakt die zwei Features, die für 
das Projekt überlebenswichtig sind, ohne das Budget zu sprengen: Eine außergewöhnlich 
hohe Reichweite und die Möglichkeit, kostengünstige Gyro-Empfänger zu nutzen. Da bei einem 
Speedrun keine komplexen Mischer, Dual-Rate-Kurven oder Telemetriedaten auf einem 
Senderdisplay benötigt werden, ist das spartanische Design der X6 kein technischer Nachteil, 
sondern ein effizienter Ressourceneinsatz.


#### Konsequenzen
- Empfänger-Wahl: Es muss zwingend der Empfänger 'X6FG' (das 'G' steht für Gyro) verbaut werden. Der Standard-Empfänger X6F hat keine Stabilisierung.
- Setup: Der Gyro (Kanal 6 Drehregler am Sender) muss vor dem ersten Run auf einer sicheren Fläche präzise eingestellt werden (Sensitivität), damit sich die Lenkung bei High-Speed nicht aufschaukelt (Speed-Wobble).
- Batterien: Der Sender benötigt 4x AA Batterien. Für konstante Sendeleistung sollten hochwertige Akkus (z.B. Eneloop) verwendet werden.


---

### ADR-006: Auswahl des Lenkservos für präzise High-Speed-Kontrolle
**Status:** Offen | **Datum:** 2026-02-24

#### Kontext
Bei Geschwindigkeiten von 100 km/h wirken enorme aerodynamische und mechanische Kräfte 
auf die Vorderräder des Carten T410R. Ein minimales Zittern, Spiel oder eine zu langsame 
Reaktionszeit des Lenkservos können sofort zum Kontrollverlust und Totalausfall führen. 
Zudem ist der Platz in einem 1:10 Tourenwagen-Chassis begrenzt, weshalb Standardgrößen 
oft das Kabelmanagement erschweren oder den Schwerpunkt unnötig nach oben verlagern. 
Gefordert ist ein Servo mit Metallgetriebe (Robustheit), hoher Stellgeschwindigkeit 
(unter 0.10s) und ausreichender Stellkraft (ca. 8-10 kg).


#### Entscheidung
> **Savöx SC-1251MG+**

#### Begründung (Rationale)
Die Entscheidung fällt auf das Savöx SC-1251MG+. Es bietet die exakt benötigte Balance aus 
Geschwindigkeit (0.09s), Kraft (9.0 kg bei 6.0V) und Bauform (Low-Profile). Die verringerte 
Bauhöhe senkt den Schwerpunkt des Chassis und schafft Platz für die Kabelführung des 120A Reglers. 
Das '+' im Namen steht für den Softstart und die Sanwa-SSR-Kompatibilität, was eine extrem 
feinfühlige und hochauflösende Ansteuerung ermöglicht. Ein Ausfall der Lenkung durch 
Zahnradbruch wird durch das Vollmetallgetriebe quasi eliminiert.


#### Konsequenzen
- Servohorn-Upgrade: Das dem Carten-Bausatz beiliegende Plastik-Servohorn muss zwingend gegen ein steifes Aluminium-Servohorn mit 25 Zähnen (25T - passend für Savöx/Futaba) getauscht werden, da Plastik bei High-Speed flext.
- BEC-Spannung: Das BEC (Battery Eliminator Circuit) des Hobbywing-Reglers muss auf 6.0V eingestellt werden, um die volle Leistung des Servos abzurufen.
- Stromhunger: Savöx-Servos ziehen kurzzeitig hohe Anlaufströme. Das 5A BEC des Hobbywing 10BL120 G2 ist dafür aber stark genug dimensioniert (kein externer Kondensator/Glitch-Buster nötig).


---

### ADR-007: Auswahl der aktiven und passiven Motorkühlung für 3S-Speedruns
**Status:** Offen | **Datum:** 2026-02-24

#### Kontext
Das anvisierte Ziel von 100 km/h erfordert den Einsatz eines 4000kV Motors an einem 
3S LiPo (11.1V), was zu extremen Drehzahlen von ca. 44.400 U/min und einer enormen 
länger übersetzten Last (64Z/38Z) führt. Unter diesen Bedingungen entsteht im Motor 
binnen Sekunden massiv nutzlose Abwärme. Ohne angemessene Kühlung droht die 
Entmagnetisierung des Rotors (Hitzetod) oder das Schmelzen der Isolierung. 
Daher ist ein kompromissloses thermisches Management-System zwingend erforderlich.


#### Entscheidung
> **Passiver 36mm Alu-Kühlkörper kombiniert mit aktivem 40x40mm High-Speed Alu-Lüfter**

#### Begründung (Rationale)
Die Entscheidung fällt auf ein duales Kühlsystem (aktiv und passiv). Der 36mm 
Alu-Aufsteckkühlkörper passt perfekt auf den Hobbywing 3652SL Motor. Der 40mm 
High-Speed-Lüfter mit Aluminiumrahmen bietet durch Drehzahlen von bis zu 20.000 U/min 
den nötigen Orkan, um die Hitze wegzublasen. Ein Aluminiumrahmen beim Lüfter 
verhindert zudem, dass sich dieser bei Stauhitze verformt, und dient als zusätzlicher 
Mini-Kühlkörper.


#### Konsequenzen
- Stromversorgung: Der Lüfter muss in einen freien Steckplatz des DumboRC-Empfängers (z.B. CH3 oder CH4) gesteckt werden, um Strom vom Regler-BEC zu beziehen.
- Kabelmanagement: Durch den extremen Sog des High-Speed-Lüfters müssen alle Kabel (insbesondere Antenne und Servokabel) zwingend mit Kabelbindern gesichert werden, damit sie nicht in die Rotorblätter geraten.
- Wärmeleitpaste: Es wird dringend empfohlen, zwischen Motor und Alu-Kühlkörper einen Tropfen PC-Wärmeleitpaste aufzutragen, um den thermischen Übergangswiderstand zu minimieren.


---

### ADR-008: Auswahl der Bereifung (Belted Gummireifen für Asphalt) für 100 km/h Speedruns
**Status:** Offen | **Datum:** 2026-02-25

#### Kontext
Bei einer Zielgeschwindigkeit von 100 km/h und den damit verbundenen extremen Drehzahlen 
der Räder dehnen sich Standard-Gummireifen durch die Fliehkraft massiv in der Mitte aus 
(der sogenannte "Pizza-Cutter-Effekt" oder "Ballooning"). Das führt zu einem sofortigen 
Kontrollverlust und oft zum Platzen des Reifens. Gefordert sind fertig verklebte Reifen 
auf Felgen mit einem 12mm-Sechskant-Mitnehmer (passend für das Carten T410R Chassis), 
die ihre Form unter extremen Fliehkräften zu 100 % beibehalten und deren Gummimischung 
der hohen Reibungshitze auf rauem Asphalt standhält.
Zusätzlich muss die reale Streckenbeschaffenheit (nicht staubfreier Normal-Asphalt vs. 
sauber präparierte Rennstrecke) bei der Wahl des Reifenprofils (Slick vs. Rillen) 
beachtet werden.


#### Entscheidung
> **Sweep HANKOOK Tread Belted tires Pre-glued set Pro-compound 36deg for Asphalt (SR-SSF-36AWPG)**

#### Begründung (Rationale)
Die Entscheidung fällt auf die fertig verklebten Sweep HANKOOK Tread Belted Reifen mit 
der härteren 36-Shore Asphalt-Mischung. Obwohl ein profilloser Voll-Slick physikalisch 
die absolute Höchstleistung und maximale Laufruhe bei 100 km/h bietet, ist er im realen 
Einsatz auf nicht perfekt gekehrten Parkplätzen zu empfindlich gegen feinen Staub (Verlust 
der Traktion). Das Hankook-Profil kann leichten Schmutz abtransportieren und bietet 
auf Normal-Asphalt das sicherere und gutmütigere Fahrverhalten. Gleichzeitig garantiert 
das essenzielle Kevlar-Gewebe (Belt) absolute Sicherheit gegen das lebensgefährliche Ausdehnen.


#### Konsequenzen
- Vorab-Check: Auch ab Werk fertig verklebte Reifen müssen vor dem ersten Run zwingend auf Verarbeitungsfehler an der Klebenaht geprüft werden (kurz an der Reifenflanke ziehen).
- Auswuchten: Da bei 100 km/h kleinste Unwuchten das Fahrwerk destabilisieren, sollten die Räder idealerweise mit einer RC-Reifenwaage und Knetblei ausgewuchtet werden.
- Temperaturfenster: Die 36-Shore Mischung ist relativ hart. Um maximalen mechanischen Grip aufzubauen, müssen die Reifen vor dem eigentlichen Speedrun durch 1-2 langsame Runden warmgefahren werden.


---
