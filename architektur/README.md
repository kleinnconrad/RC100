# 🏛️ Architecture Decision Records (ADRs)

Dieses Verzeichnis enthält alle grundlegenden architektur- und Hardwareentscheidungen für das RC100 Projekt. **Diese Datei wird automatisch generiert. Bitte nicht manuell bearbeiten.**

## 📋 Übersicht

| ID | Datum | Titel | Status | Entscheidung |
| :--- | :--- | :--- | :--- | :--- |
| **ADR-001** | 2026-03-06 | Auswahl der Chassis-Plattform und Make-or-Buy-Entscheidung (100 km/h Benchmark) | 🟢 entschieden | MAKE - Carten T410R |
| **ADR-002** | 2026-03-06 | Auswahl der Brushless-Motor-Combo für 100 km/h Speedruns | 🟢 entschieden | Hobbywing QuicRun WP10BL120 G2 Combo (3660SL 3700KV) |
| **ADR-003** | 2026-03-06 | Auswahl des LiPo-Akkus für 100 km/h Ziel. | 🟢 entschieden | Absima GreenHorn Line V2 (3S / 5000mAh / 50C / Hardcase) |
| **ADR-004** | 2026-03-06 | Auswahl des Ladegeräts für 3S LiPo-Akkus | 🟢 entschieden | SkyRC S100neo |
| **ADR-005** | 2026-03-06 | Auswahl der Fernsteuerungsanlage für 100 km/h Speedruns | 🟢 entschieden | Carson Reflex Wheel X1 |
| **ADR-006** | 2026-03-06 | Auswahl des Lenkservos für präzise High-Speed-Kontrolle | 🟢 entschieden | JX PDI-4409MG |
| **ADR-007** | 2026-03-06 | Auswahl der aktiven und passiven Motorkühlung für 3S-Speedruns | 🟢 entschieden | Passiver 36mm Alu-Kühlkörper kombiniert mit aktivem 40x40mm High-Speed Alu-Lüfter |
| **ADR-008** | 2026-02-25 | Auswahl der Bereifung (Belted Gummireifen für Asphalt) für 100 km/h Speedruns | 🟡 Offen | Sweep HANKOOK Tread Belted tires Pre-glued set Pro-compound 36deg for Asphalt (SR-SSF-36AWPG) |
| **ADR-009** | 2026-03-12 | Auswahl der aerodynamischen Karosserie für 100 km/h Speedruns | 🟢 entschieden | ZooRacing Hellcat (190 mm, 0.7mm Stärke) |
| **ADR-010** | 2026-03-10 | Auswahl des GPS-Messsystems zur Validierung der 100 km/h Marke | 🟢 entschieden | Ruddog GPS Performance Analyzer |

---

## 📖 Detail-Protokolle

### ADR-001: Auswahl der Chassis-Plattform und Make-or-Buy-Entscheidung (100 km/h Benchmark)
**Status:** entschieden | **Datum:** 2026-03-06

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

### ADR-002: Auswahl der Brushless-Motor-Combo für 100 km/h Speedruns
**Status:** entschieden | **Datum:** 2026-03-06

#### Kontext
Um einen 1/10 Tourenwagen (Carten T410R) auf 100 km/h zu beschleunigen, muss das Getriebe extrem 
'lang' übersetzt werden (hohe Radlast > 22 %). Ein klassischer 3650er-Motor (50 mm Länge) operiert 
hierbei an seiner thermischen Belastungsgrenze. Es wird zwingend ein Antriebsstrang benötigt, 
der bei 3S-Spannung (11.1V) genügend mechanisches Drehmoment (Motorbaugröße 3660) liefert und 
dessen Fahrtenregler (ESC) die hohen Blockierströme beim Beschleunigen sicher verarbeiten 
kann (min. 120A).


#### Entscheidung
> **Hobbywing QuicRun WP10BL120 G2 Combo (3660SL 3700KV)**

#### Begründung (Rationale)
Die Entscheidung fällt auf die Hobbywing QuicRun G2 Combo. Sie eliminiert das Ausfallrisiko von 
No-Name-Motoren und bietet eine perfekt aufeinander abgestimmte Architektur (Firmware von ESC 
und Motor-Timing sind optimal verzahnt). Der 3660er Motor liefert mit seinen 3700KV an 3S 
(ca. 41.000 U/min) die perfekte Drehzahl und hat durch den längeren Rotor genug Drehmoment, 
um die errechnete Radlast von ca. 24 % souverän zu stemmen. Dies ist die sicherste und 
effizienteste Lösung im Budget unter 100 €.


#### Konsequenzen
- Packaging (Bauraum): Der 3660er Motor ist 10 mm länger als das Standardmaß. Der ESC und der Empfänger müssen im T410R-Chassis entsprechend weiter hinten platziert werden.
- Ritzel-Bohrung (WICHTIG): Hobbywing liefert den 3660SL G2 in der Regel mit einer 5.0 mm Welle aus (Spezifikationen beim Händler vor der Ritzelbestellung final verifizieren). Ein 48dp-Ritzel mit 5 mm Bohrung (z.B. Robinson Racing) ist zwingend erforderlich.
- Stromversorgung: Die Systemspannung ist hart auf 3S LiPo limitiert. Ein 4S-Betrieb würde die maximal zulässige Rotordrehzahl des Motors überschreiten.


---

### ADR-003: Auswahl des LiPo-Akkus für 100 km/h Ziel.
**Status:** entschieden | **Datum:** 2026-03-06

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
**Status:** entschieden | **Datum:** 2026-03-06

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
**Status:** entschieden | **Datum:** 2026-03-06

#### Kontext
Ein RC-Car, das mit 100 km/h (ca. 27,7 Meter pro Sekunde) fährt, legt in wenigen Sekunden 
enorme Distanzen zurück. Die Fernsteuerung (Transmitter) und der Empfänger (Receiver) 
müssen daher zwingend eine stabile Funkverbindung und ein absolut verlässliches Fail-Safe 
aufweisen, damit das Fahrzeug am Ende der Beschleunigungsstrecke nicht außer Kontrolle gerät. 
Es muss abgewogen werden zwischen maximaler Reichweite inkl. Gyro-Unterstützung und einem 
robusten, ausfallsicheren MVP-Ansatz (Minimum Viable Product), der die Komplexität im Setup reduziert.


#### Entscheidung
> **Carson Reflex Wheel X1**

#### Begründung (Rationale)
Die Entscheidung fällt im Sinne eines sauberen MVP-Ansatzes auf die Carson Reflex Wheel X1. 
Obwohl die DumboRC auf dem Papier mehr Reichweite und einen Gyro bietet, reicht die Carson 
für die ersten validen 100 km/h-Runs auf übersichtlichen Parkplätzen oder Strecken vollkommen aus. 
Sie ist ein bewährter Industrie-Standard im Einstiegssegment, bietet eine extrem zuverlässige 
Fail-Safe-Funktion und die überlebenswichtige Steering Dual-Rate Einstellung. Dieser 
pragmatische Ansatz spart Komplexität beim Setup (kein Gyro-Wobble-Risiko) und liefert 
genau die Baseline an Funktionalität, die aktuell benötigt wird.


#### Konsequenzen
- Sicherheitsarchitektur (Fail-Safe): Das Fail-Safe des beiliegenden Carson Micro-Empfängers muss vor der ersten Fahrt zwingend auf 'Bremse/Neutral' programmiert werden. Bei Signalverlust darf der 3660er Motor kein Gas mehr annehmen.
- Spannungs-Constraint (BEC): Der Hobbywing 120A Regler darf maximal 6.0V an den Empfänger liefern. Die 7.4V Option des ESC darf nicht aktiviert werden, da der Carson Empfänger sonst durchbrennen könnte.
- Fahrverhalten (Dual Rate): Da kein Gyro vorhanden ist, der das Auto automatisch stabilisiert, muss der maximale Lenkausschlag über das Dual-Rate-Rad am Sender für Speedruns zwingend auf ca. 30 % reduziert werden, um ein Aufschaukeln der Lenkung zu verhindern.
- Batterien: Der Sender benötigt 4x AA Batterien. Für eine absolut konstante Sendeleistung ohne Einbrüche sollten hochwertige Akkus (z.B. Eneloop) verwendet werden.


---

### ADR-006: Auswahl des Lenkservos für präzise High-Speed-Kontrolle
**Status:** entschieden | **Datum:** 2026-03-06

#### Kontext
Bei Geschwindigkeiten von 100 km/h wirken enorme aerodynamische und mechanische Kräfte 
auf die Vorderräder des Carten T410R. Ein minimales Zittern, Spiel oder eine zu langsame 
Reaktionszeit des Lenkservos können sofort zum Kontrollverlust und Totalausfall führen. 
Zudem ist der Platz in einem 1:10 Tourenwagen-Chassis begrenzt. Da unsere MVP-Fernsteuerung 
(Carson Reflex Wheel X1) über keinen elektronischen Gyro verfügt, muss das Servo den 
Geradeauslauf mechanisch extrem präzise und kraftvoll halten. Gefordert ist ein Servo 
mit Metallgetriebe (Robustheit), hoher Stellgeschwindigkeit (~0.11s) und ausreichender 
Stellkraft (ca. 9 kg).


#### Entscheidung
> **JX PDI-4409MG**

#### Begründung (Rationale)
Die Entscheidung fällt im Sinne der Budget-Optimierung auf das JX PDI-4409MG. Es erfüllt 
alle harten Architektur-Constraints: Ein Metallgetriebe verhindert Zahnausfall bei 100 km/h, 
die 9.2 kg Stellkraft halten die Vorderräder stabil gegen den Winddruck, und die Low-Profile-
Bauform schafft zwingend benötigten Platz für den Hobbywing 120A ESC auf dem engen Chassis. 
Der Verzicht auf das Premium-Zentrierverhalten eines Savöx-Servos ist ein akzeptabler 
Trade-off für reine Geradeaus-Speedruns.


#### Konsequenzen
- Servohorn-Upgrade: Das Plastik-Servohorn des Carten-Bausatzes muss zwingend gegen ein steifes Aluminium-Servohorn mit 25 Zähnen (25T - Standard für JX/Futaba/Savöx) getauscht werden.
- BEC-Spannung: Das BEC des Hobbywing-Reglers wird auf 6.0V belassen. Dies liefert die volle Leistung für das Servo (9.2kg / 0.11s) und schützt gleichzeitig den Carson-Empfänger vor Überspannung.
- Dual-Rate Setup: Da das Servo sehr schnell reagiert, muss der maximale Lenkausschlag an der Carson-Funke für den High-Speed-Run stark limitiert werden (ca. 30%), um ein Verreißen der Lenkung bei 100 km/h zu verhindern.


---

### ADR-007: Auswahl der aktiven und passiven Motorkühlung für 3S-Speedruns
**Status:** entschieden | **Datum:** 2026-03-06

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

### ADR-009: Auswahl der aerodynamischen Karosserie für 100 km/h Speedruns
**Status:** entschieden | **Datum:** 2026-03-12

#### Kontext
Bei einer Zielgeschwindigkeit von 100 km/h (ca. 27,7 m/s) ist die Karosserie kein rein optisches 
Bauteil mehr, sondern die primäre aerodynamische Schutzschicht. Eine klassische, eckige Karosserie 
fängt Luft unter der Frontschürze ein, was unweigerlich zu einem 'Blow-over' (Abheben durch 
Staudruck) führt. Gleichzeitig darf der Luftwiderstand (cW-Wert) den Motor nicht unnötig einbremsen. 
Das Carten T410R Chassis erfordert eine Breite von 190 mm. Die Materialstärke ist kritisch: 
Dünnes Lexan (< 0.5 mm) verformt sich bei 100 km/h massiv.


#### Entscheidung
> **ZooRacing Hellcat (190 mm, 0.7mm Stärke)**

#### Begründung (Rationale)
Die Entscheidung fällt auf die ZooRacing Hellcat in der 0.7mm Standard-Stärke. Sie stellt den 
optimalen Kompromiss aus minimalem Luftwiderstand (für das Erreichen der 100 km/h) und sicherem 
Anpressdruck (Verhinderung von Blow-overs) dar. Im Gegensatz zu extrem flachen LMP-Karosserien 
passt sie problemlos über die Stoßdämpferbrücken des Carten T410R. Die Materialstärke von 0.7mm 
garantiert, dass die Karosserie dem massiven Staudruck bei Top-Speed standhält und nicht zu 
vibrieren oder auf die Reifen zu schleifen beginnt.


#### Konsequenzen
- Lackierung: Die Karosserie wird unlackiert geliefert. Es muss zwingend spezielle Lexan-Farbe (Polycarbonat-Farbe, z.B. Tamiya PS-Serie) verwendet werden, da normale Farbe abblättern würde.
- Montage: Der mitgelieferte Heckflügel muss extrem steif verschraubt werden. Die Karosserielöcher müssen passgenau mit einer Lexanschere und einem Karosseriebohrer bearbeitet werden.
- Chassis-Vorbereitung: Der Schaumstoff-Bumper an der Front des Carten T410R muss exakt bündig mit der Innenseite der Frontschürze abschließen, um ein Eindrücken bei High-Speed zu verhindern.


---

### ADR-010: Auswahl des GPS-Messsystems zur Validierung der 100 km/h Marke
**Status:** entschieden | **Datum:** 2026-03-10

#### Kontext
Die berechneten mathematischen Modelle (Achsdrehzahl, Rollwiderstand, Spannungseinbruch) 
müssen in der Realität ('Integration Test' auf der Straße) durch harte Telemetriedaten 
validiert werden. Da das Fahrzeug den Topspeed von 100 km/h oft nur für ein Zeitfenster 
von 2 bis 3 Sekunden hält, ist eine extrem hohe Abtastrate (Update-Frequenz) des 
Messgeräts zwingend erforderlich. Gleichzeitig darf das Modul das Fahrzeuggewicht (CG) 
und die Aerodynamik nicht negativ beeinflussen.


#### Entscheidung
> **Ruddog GPS Performance Analyzer**

#### Begründung (Rationale)
Die Entscheidung fällt auf den Ruddog GPS Performance Analyzer. Er ist das perfekte 'Fit-for-Purpose'-
Tool für dieses Projekt. Die 10Hz Abtastrate garantiert, dass die exakte Höchstgeschwindigkeit 
erfasst wird, selbst wenn diese nur für den Bruchteil einer Sekunde anliegt. Das geringe Gewicht 
von 38g verändert das Fahrverhalten des Carten T410R nicht, und die Bluetooth-App-Schnittstelle 
erspart ein schweres, ablesbares Display direkt auf dem Fahrzeug.


#### Konsequenzen
- Signal-Constraint: Das GPS-Signal geht problemlos durch Lexan-Karosserien, wird aber von Karbonfasern massiv geblockt. Das Modul darf im Carten T410R nicht direkt *unter* dem Karbon-Oberdeck montiert werden. Die optimale Position ist auf dem Schaumstoff-Bumper vorne.
- Befestigung: Das Gerät muss extrem sicher (z.B. mit starkem Klettband oder 3M Dual Lock) fixiert werden, damit es bei einem Überschlag bei 100 km/h nicht als Projektil wegfliegt.


---
