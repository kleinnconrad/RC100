# 🏛️ Architecture Decision Records (ADRs)

Dieses Verzeichnis enthält alle grundlegenden Architektur- und Hardwareentscheidungen für das RC100 Projekt. **Diese Datei wird automatisch generiert. Bitte nicht manuell bearbeiten.**

## 📋 Übersicht

| ID | Datum | Titel | Status | Entscheidung |
| :--- | :--- | :--- | :--- | :--- |
| **ADR-001** | 2026-02-24 | Auswahl der Chassis-Plattform und Make-or-Buy-Entscheidung (100 km/h Benchmark) | 🟡 Offen | MAKE - Carten T410R |
| **ADR-002** | 2026-02-24 | Auswahl der Brushless-Antriebseinheit (ESC & Motor) für 100 km/h Speedruns | 🟡 Offen | Hobbywing QuicRun WP 10BL120 G2 Combo |
| **ADR-003** | 2026-02-24 | Auswahl des LiPo-Akkus für 100 km/h Ziel | 🟡 Offen | Absima GreenHorn Line V2 (3S / 5000mAh / 50C / Hardcase) |
| **ADR-004** | 2026-02-24 | Auswahl des Ladegeräts für 3S LiPo-Akkus | 🟡 Offen | SkyRC S100neo |
| **ADR-005** | 2026-02-24 | Auswahl der Fernsteuerungsanlage für 100 km/h Speedruns | 🟡 Offen | DumboRC X6 |

---

## 📖 Detail-Protokolle

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

### ADR-002: Auswahl der Brushless-Antriebseinheit (ESC & Motor) für 100 km/h Speedruns
**Status:** Offen | **Datum:** 2026-02-24

#### Kontext
Für das Carten T410R Chassis wird ein Antriebssystem benötigt, das in der Lage ist, 
das Fahrzeug auf über 100 km/h zu beschleunigen. Dies erfordert den Betrieb an einem 
3S LiPo-Akku (11.1V Nennspannung) und eine extreme Übersetzung (64Z/38Z). 
Durch die lange Übersetzung entstehen beim Beschleunigen massive Stromspitzen (Ampere). 
Ein Standard-Regler (60A bis 80A) würde hier sofort in die thermische Abschaltung gehen 
oder durchbrennen. Benötigt wird eine Kombination aus hoher Spannungsfestigkeit, 
ausreichendem Ampere-Puffer (Headroom) und einer Motordrehzahl von ca. 4000kV.


#### Entscheidung
> **Hobbywing QuicRun WP 10BL120 G2 Combo**

#### Begründung (Rationale)
Die Entscheidung fällt auf die Hobbywing QuicRun 120A Combo. Sie bietet das beste 
Kosten-Nutzen-Verhältnis für diese spezifische Architektur. 120 Ampere Dauerlast 
bieten das zwingend notwendige thermische und elektrische Sicherheitsnetz für die 
extreme 64Z/38Z Übersetzung. Da bei Speedruns hauptsächlich im oberen Drehzahlbereich 
gefahren wird, kann auf ein teures Sensorkabel-Setup (Option 2 & 3) verzichtet werden. 
Im Gegensatz zu Option 1 (Surpass) garantiert Hobbywing hier reproduzierbare Qualität 
und ein stabiles BEC, was bei über 100 km/h einen Ausfall der Lenkung verhindert.


#### Konsequenzen
- System ist sensorlos (Sensorless): Beim langsamen Anfahren kann leichtes 'Cogging' (Stottern) auftreten. Dies ist für das Speedrun-Ziel irrelevant.
- Zusätzliche Kühlung erforderlich: Der 3652SL Motor muss bei 3S zwingend mit einem passiven Alu-Kühlkörper und einem aktiven 40mm High-Speed-Lüfter nachgerüstet werden (siehe spec_cooling.yaml).
- Kein integriertes Data-Logging: Topspeed und Temperaturen müssen extern gemessen werden (z. B. GPS-Logger und Infrarot-Thermometer).


---

### ADR-003: Auswahl des LiPo-Akkus für 100 km/h Ziel
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
