# RC100 Gesamtspezifikation (Full Spec)

> **Automatischer Build:** Diese Datei wird aus den modularen Spezifikationen generiert.

---

## AKKU


### Battery Meta

* **Brand:** Absima
* **Series:** GreenHorn Line V2
* **Part Number:** 4140014
* **Type:** LiPo (Lithium-Polymer)

### Electrical Specifications

* **Voltage:** 11.1V (Nennspannung)
* **Cells:** 3S
* **Capacity:** 5000 mAh
* **Energy:** 55.5 Wh
* **Discharge Rate Continuous:** 50C
* **Max Continuous Amp Draw:** 250A

### Connectors

* **Main Power:** XT60 (Plug & Play mit Hobbywing QuicRun G2 ESC)
* **Balancer:** XH (Standard-Balancer für das Ladegerät)

### Physical Specifications

* **Case Type:** Hardcase (HC) - Hartplastik Box
* **Safety:** Zwingend erforderlich für Speedruns zum Schutz vor Kardanwelle/Crashes
* **Weight G:** 370

#### Dimensions

  * **Length Mm:** 138
  * **Width Mm:** 46
  * **Height Mm:** 35

### Chassis Integration Notes

* **Issue:** Der Carten T410R ist ab Werk für 2S-Akkus (25mm Höhe) konzipiert. Dieser 3S-Akku ist 35mm hoch.
* **Solution:** Die obere Carbon-Akkustrebe des Chassis muss 'höhergelegt' werden.

#### Required Parts

  * 2x Distanzhülsen/Spacers (Kunststoff oder Alu) mit ca. 10mm Höhe
  * 2x minimal längere M3-Schrauben (ca. M3x16 oder M3x18)
* **Execution:** Spacers auf die originalen Alu-Pfosten legen, Carbon-Strebe darauf verschrauben. Kein Dremeln oder Fräsen am Chassis notwendig.


---

## BODY


### Aerodynamik Meta

* **Brand:** ZooRacing
* **Modell:** Hellcat
* **Fahrzeugklasse:** 1:10 On-Road Tourenwagen
* **Breite Mm:** 190
* **Radstand Mm:** 257
* **Material:** Polycarbonat (Lexan)
* **Materialstaerke Mm:** 0.7

#### Shopping Item

  * **In Liste Aufnehmen:** True
  * **Artikel Name:** ZooRacing Hellcat 190mm Tourenwagen Karosserie (0.7mm Regular)
  * **Kategorie:** Karosserie & Aerodynamik
  * **Referenz Link:** Suche bei RC-KleinKram oder Tonisport nach 'ZooRacing Hellcat 0.7mm'
  * **Geschaetzter Preis Eur:** 32.9

### Aerodynamic Features

* **Front:** Tief gezogene Nase und sanfter Haubenwinkel reduzieren den Staudruck und verhindern Lift.
* **Roofline:** Flach abfallendes Dach leitet die Luft laminar und störungsfrei zum Heckflügel.
* **Rear Wing:** Inkludierter High-Downforce Flügel sorgt für zwingend benötigte Heckstabilität bei High-Speed.

### Preparation And Painting

* **Reinigung:** Die Innenseite der Karosserie vor dem Lackieren zwingend mit Spülmittel auswaschen, um Trennmittelreste aus der Produktion zu entfernen.
* **Lack Typ:** Ausschließlich Polycarbonat-Spray (z.B. Tamiya PS-Farben) verwenden. Von innen in mehreren dünnen Schichten lackieren.
* **Schutzfolie:** Die äußere Overspray-Schutzfolie erst nach dem kompletten Lackieren und Bohren der Löcher abziehen.

### Mounting Instructions

* **Karosserieloecher:** Löcher nicht stechen, sondern mit einem speziellen Karosseriebohrer (Reamer) bohren, um Risse im Lexan zu vermeiden.
* **Bumper Support:** Der Front-Schaumstoffbumper des Chassis muss den vorderen Karosserieüberhang mechanisch abstützen.
* **Radkaesten:** Radkästen mit einer gebogenen Lexanschere ausschneiden und Kanten mit feinem Schleifpapier glätten, um Einreißen bei Vibrationen zu verhindern.


---

## BRUSHLESS COMBO


### Combo Meta

* **Beschreibung:** Spezifikation des Brushless-Antriebsstrangs für 100 km/h an 3S.
* **Architektur Status:** ADR-002: Hobbywing QuicRun WP10BL120 G2 Combo (3660SL 3700KV) akzeptiert

### Elektronischer Fahrtenregler Esc

* **Typ:** Brushless ESC (Sensorless)
* **Ampere Dauerlast:** Min. 120A
* **Lipo Support:** 2S - 3S (optional bis 4S)
* **Bec Spannung:** 6.0V oder 7.4V (einstellbar für Servo - ACHTUNG: Auf 6.0V für Carson Empfänger belassen!)
* **Steckersystem Akku:** XT60 (Ab Werk bei der G2 Combo verlötet)
* **Steckersystem Motor:** 4.0mm Goldkontakt
* **Referenz Modell:** Hobbywing QuicRun WP10BL120 G2
* **Hinweis Packaging:** Aufgrund des längeren Motors muss der ESC im T410R Chassis möglichst weit nach hinten oder leicht versetzt montiert werden.

#### Shopping Item

  * **In Liste Aufnehmen:** True
  * **Artikel Name:** Hobbywing QuicRun Brushless Combo WP10BL120 G2 (inkl. 3660SL 3700KV Motor)
  * **Kategorie:** Antrieb & Elektronik
  * **Referenz Link:** https://www.rcfox.de/HW38030211-HobbyWing-Quicrun-Brushless-Combo-WP10BL120G2-mit-3660SL-3700KV-G2
  * **Geschaetzter Preis Eur:** 89.0

### Brushless Motor

* **Baugroesse:** 3660 (36 mm Durchmesser, 60 mm Länge)
* **Kv Wert:** 3700KV
* **Wellendurchmesser:** 5.0 mm (Erfordert zwingend 48dp Ritzel mit 5mm Bohrung!)
* **Pol Anzahl:** 4-Pol (für hohes Drehmoment)
* **Referenz Modell:** Hobbywing 3660SL G2 (3700KV)
* **Thermische Toleranz:** Max. 25.0 % berechnete Radlast

#### Shopping Item

  * **In Liste Aufnehmen:** False

### Motor Ritzel

* **Typ:** Large Bore Pinion Gear
* **Zahnflankenprofil Pitch:** 48dp
* **Zaehnezahl:** 43Z
* **Bohrung:** 5.0 mm (Zwingend für die Welle des Hobbywing 3660 Motors!)
* **Material:** Gehärteter Stahl

#### Shopping Item

  * **In Liste Aufnehmen:** True
  * **Artikel Name:** Robinson Racing RRP-2043 (48dp, 43T, 5mm Bore)
  * **Kategorie:** Antrieb & Mechanik
  * **Referenz Link:** https://www.ebay.com/itm/234242275376
  * **Geschaetzter Preis Eur:** 15.0

### Kuehlung

* **Motor Kuehler:** Passiver Aluminium-Kühlkörper für 36mm Motoren
* **Motor Luefter:** Optional: 30mm oder 40mm High-Speed Lüfter (Betrieb über freien Steckplatz am Empfänger)

#### Shopping Item

  * **In Liste Aufnehmen:** False


---

## CARTENT410R


### Chassis Meta

* **Brand:** Carten
* **Model:** T410R Tourenwagen Bausatz
* **Part Number:** NHA413

### Carten T410R


#### Allgemein

  * **Fahrzeugtyp:** 1:10 Elektro Tourenwagen (EP Touring Car)
  * **Lieferzustand:** Bausatz (Kit) - unmontiert
  * **Einsatzbereich:** On-Road / Asphalt / Teppich

#### Abmessungen

  * **Spurbreite Mm:** 190
  * **Radstand Mm:** 258

#### Chassis Und Aufbau

  * **Bodenplatte:** 2,25 mm Eco-Carbon (kohlefaserverstärktes Verbundmaterial)
  * **Oberdeck:** 2,0 mm Eco-Carbon
  * **Daempferbruecken:** 3,0 mm Eco-Carbon (vorne & hinten, diverse Montagepunkte)
  * **Motorhalterung:** CNC-gefrästes Aluminium
  * **Servohalterung:** Floating Servo Mount (Aluminium)
  * **Akkuhalterung:** Vorbereitet für 2S Standard-LiPo (Stickpack) oder Shorty-LiPo
  * **Karosseriehalter:** Verstellbare Kunststoff-Pfosten

#### Antriebsstrang

  * **Antriebsart:** 4WD Allrad, zentraler Kardanantrieb (Wellenantrieb)
  * **Mittelantriebswelle:** Aluminium (rot eloxiert)
  * **Differentiale:** Gekapselte Kegeldifferentiale (vorne & hinten)
  * **Differential Zahnraeder:** Metallzahnräder
  * **Antriebswellen:** Stahl CVD (Constant Velocity Drives) an Vorder- und Hinterachse
  * **Hauptzahnradhalterung:** Aluminium
  * **Radmitnehmer:** 12 mm Sechskant, Aluminium
  * **Interne Untersetzung:** 1:2.47 bis 1:2.53
  * **Kugellager:** Komplett kugelgelagert (mit Gummidichtungen)

#### Fahrwerk Und Federung

  * **Stossdaempfer:** Aluminium Öldruckstoßdämpfer (mit Gewindefahrwerk)
  * **Querlenkerhalter:** Aluminium (Toe Blocks)
  * **Stabilisatoren:** Vorne und hinten enthalten
  * **Geometrie Einstellung:** Stufenlos einstellbar über R/L Gewindestangen (Turnbuckles)
  * **Einstellbare Parameter:**
    * Sturz
    * Spur
    * Nachlauf (Caster)
    * Ausfederweg (Droop)
    * Bodenfreiheit (Ride Height)
    * Ackermann

#### Lenkung

  * **Lenksystem:** Kugelgelagertes Dual-Bellcrank-System (Doppelarm)
  * **Lenkhebel C Hubs:** Composite-Kunststoff


---

## DIFFERENTIALE


### Differential Meta

* **Type:** Öldruck-Kegeldifferential (Metal Gear)
* **Mechanical Load Capacity:** > 100 km/h (ca. 8.300 U/min Achsdrehzahl)

### Material And Construction

* **Gears Ring And Bevel:** Sintermetall / Stahl
* **Diff Outdrives Cup Joints:** Gehärteter Stahl
* **Diff Case Cup:** Faserverstärkter Verbundkunststoff (Composite)

### Mandatory Modifications


#### Perfect Shimming

  * **Issue:** Spielfreiheit
  * **Description:** Die inneren Metallzahnräder müssen beim Zusammenbau mit hauchdünnen Passscheiben (Shims) absolut spielfrei eingestellt werden. Nur so wird verhindert, dass die Zähne unter dem extremen Drehmoment des 3S-Motors überspringen oder abreißen.

#### Reinforced Sealing

  * **Issue:** O-Ring Abdichtung
  * **Description:** Bei 8.300 U/min erzeugt das Öl im Inneren einen massiven Fliehkraftdruck nach außen. Die Gummi-O-Ringe müssen mit zähem Spezialfett (z. B. 'Green Slime') abgedichtet werden, damit das Differential nicht trockenläuft.

#### Oil Viscosity

  * **Issue:** Sperrwirkung & Geradeauslauf
  * **Description:** Das Baukasten-Öl ist zu weich und führt bei Speedruns zu unkontrollierbarem Ausbrechen, wenn ein Rad minimal Grip verliert. Es muss extrem zähes Silikonöl verwendet werden, um das Auto auf einen sturen Geradeauslauf zu zwingen.
  * **Setup Recommendation:**
    * **Front Axle:** ca. 100.000 cSt (oder ein komplett starrer Spool/Starrachse)
    * **Rear Axle:** ca. 10.000 cSt


---

## FERNSTEUERUNG


### Tx Meta Transmitter

* **Brand:** Carson
* **Model:** Reflex Wheel X1
* **Type:** 2.4 GHz Pistolengriff-Sender (Surface)
* **Channels:** 2
* **Price Class:** Budget / MVP (~35 EUR)

#### Shopping Item

  * **In Liste Aufnehmen:** True
  * **Artikel Name:** Carson Reflex Wheel X1 2.4Ghz Fernsteuerungs-Set (inkl. Empfänger)
  * **Kategorie:** Steuerung & Elektronik
  * **Referenz Link:** Suche bei Modellbau-Fachhändler (z.B. Tamico, Berlinski, Amazon)
  * **Geschaetzter Preis Eur:** 35.0

### Tx Performance

* **Protocol:** FHSS (Frequency-Hopping Spread Spectrum)
* **Range Ground:** ~150 Meter (Ausreichend für übersichtliche Speedruns)
* **Response Time:** Standard 2.4Ghz Latenz
* **Power Supply:** 4x AA Batterien

### Rx Meta Receiver

* **Model:** Carson Micro-Empfänger (im Set enthalten)
* **Channels:** 4 (Physische Steckplätze, 2 aktiv nutzbar)

#### Integrated Features

  * Fail-Safe Funktion (Schutz bei Signalverlust)
* **Input Voltage:** 4.8V - 6.0V (Achtung: BEC des ESC darf nicht auf 7.4V stehen!)

### Calibration And Setup

* **Fail Safe Activation:** Das Fail-Safe muss zwingend programmiert werden! Auto aufbocken, Vollbremsung an der Funke halten und den Setup-Knopf am Empfänger drücken. Beim Ausschalten der Funke muss das Auto sofort bremsen.
* **Steering Dual Rate:** Über den Dual Rate (D/R) Drehregler an der Fernsteuerung den maximalen Lenkausschlag zwingend auf ca. 30 % reduzieren. Bei 100 km/h führt ein voller Lenkausschlag zum sofortigen Überschlag.
* **Throttle Trim:** Die Trimmung für das Gas (TH Trim) muss zwingend exakt auf dem Nullpunkt (Mitte) stehen, bevor der Hobbywing-Regler zum ersten Mal kalibriert wird.
* **Bec Voltage Warning:** Der Hobbywing 120A Regler hat ein einstellbares BEC (Stromversorgung für Empfänger/Servo). Dieses muss zwingend auf 6.0V eingestellt bleiben, da der Carson Empfänger bei 7.4V durchbrennen kann.


---

## GETRIEBE


### Getriebe Meta

* **Brand:** Arrowmax
* **Model:** Motorritzel 42Z (48dp / 3.17mm Welle) ODER Robinson Racing 5mm bore 48dp 43teeth falls 3660 motor mit 5mm Welle gefahren wird: https://www.ebay.com/itm/234242275376
* **Part Number:** 42T-48P

### Getriebe Setup


#### Hauptzahnrad Spur

  * **Zähne:** 72
  * **Typ:** Baukasten Standard
  * **Modul:** 48dp

#### Motorritzel Pinion

  * **Zähne:** 42
  * **Material:** Hardcoated Alu oder Stahl

#### Berechnete Werte

  * **Interne Uebersetzung:** 2.47
  * **Gesamt Ratio:** 4.23
  * **Zielgeschwindigkeit:** > 100 km/h

### Einstellbereich Mit 72Z Hauptzahnrad

* **Hinweis:** Laut Carten Handbuch (T410R mit Gear Diff 2.47) ohne Umbau des 72Z Hauptzahnrads fahrbar:

#### Max Beschleunigung

  * **Ritzel:** 21
  * **Ratio:** 8.47

#### Mid Range

  * **Ritzel:** 31
  * **Ratio:** 5.74

#### High Speed Bereich

  * **Ritzel 34:** 5.23
  * **Ritzel 35:** 5.08
  * **Ritzel 36:** 4.94
  * **Ritzel 37:** 4.81

#### Max Top Speed

  * **Ritzel 41:** 4.34
  * **Ritzel 42:** 4.23
  * **Ritzel 43:** 4.14
  * **Ritzel 44:** 4.04


---

## GPS


### Telemetrie Meta

* **Typ:** GNSS Performance Analyzer (GPS/GLONASS)
* **Referenz Modell:** Ruddog GPS Performance Analyzer
* **Messfrequenz:** 10 Hz (10 Updates pro Sekunde - kritisch für RC Speedruns!)
* **Schnittstelle:** Bluetooth 4.0 (Auslesen per iOS/Android App)
* **Stromversorgung:** Integrierter LiPo-Akku (via USB ladbar)
* **Gewicht:** ca. 38 Gramm

#### Shopping Item

  * **In Liste Aufnehmen:** True
  * **Artikel Name:** Ruddog GPS Performance Analyzer
  * **Kategorie:** Testing & Validierung
  * **Referenz Link:** Suche bei Modellbau-Fachhändler (z.B. RC-KleinKram, Tamico, Monster Hopups)
  * **Geschaetzter Preis Eur:** 85.0

### App Integration

* **Software:** RC Gears / Ruddog App (oder baugleiche SkyRC App)
* **Funktionen:** Top-Speed Messung, 0-100 km/h Zeitmessung, Track-Logging

### Mounting And Setup

* **Positionierung:** Zwingend an einer Stelle montieren, die freie Sicht zum Himmel hat. Karbonbauteile (wie das Upper-Deck des Carten) schirmen das Satellitensignal ab! Bester Montageort: Auf dem vorderen Schaumstoff-Rammschutz (Bumper).
* **Fixierung:** Das Modul bei Speedruns zwingend mit Klettverschluss UND einem zusätzlichen Kabelbinder oder Tape sichern. Die G-Kräfte bei einem Crash sind enorm.
* **Bedienung:** Das Modul blinkt während der Satellitensuche. Erst losfahren, wenn das GPS-Signal (meist durch durchgehendes Leuchten) als 'Locked' bestätigt ist, sonst fehlen die ersten Meter in der Messung.


---

## HAUPTZAHNRAD


### Spur Gear Meta

* **Type:** CNC-gefrästes Hauptzahnrad (48 DP, 72T)
* **Mechanical Load Capacity:** > 100 km/h (ausgelegt für 3S / 120A Brushless-Systeme)

### Material And Construction

* **Gear Body:** POM (Polyoxymethylen / Delrin) - CNC gefräst
* **Mounting Interface:** Standard 1:10 Tourenwagen 4-Loch-Aufnahme
* **Mating Pinion:** Gehärteter Stahl (zwingend erforderlich)

### Mandatory Modifications


#### Pinion Securing

  * **Issue:** Verrutschen des Motorritzels (Ursache für Getriebeschaden)
  * **Description:** Um ein erneutes Verrutschen und Zerstören des Hauptzahnrads durch asymmetrischen Eingriff zu verhindern, muss die Madenschraube des Hartstahl-Ritzels zwingend mit mittelfester Schraubensicherung (z. B. Loctite 243 / blau) auf der flachen Stelle der Motorwelle gesichert werden.

#### Gear Mesh Calibration

  * **Issue:** Zahnflankenspiel bei > 11.000 U/min
  * **Description:** Das Spiel zwischen Stahlritzel und Delrin-Hauptzahnrad muss mit der bewährten Papiermethode exakt kalibriert werden. Ein zu enges Spiel führt zu extremer Reibungshitze und Leistungsverlust, ein zu weites Spiel zum sofortigen 'Strippen' der Delrin-Zähne durch das hohe Drehmoment.

#### Material Selection

  * **Issue:** Vermeidung von Stahl-Hauptzahnrädern
  * **Description:** Bewusster Verzicht auf ein Hauptzahnrad aus Stahl. Dies hält die rotierende Masse gering (bessere Beschleunigung) und fungiert im Falle einer Blockade im Antriebsstrang als mechanische Sollbruchstelle (Fail-Safe), um die Motorwelle und den ESC vor Überlastung zu schützen.


---

## KARDANWELLE UND JOINTS


### Center Shaft Meta

* **Component:** Zentrale Antriebswelle (Center Shaft)

### Material And Suitability


#### Driveshaft

  * **Component:** Kardanwelle (Welle)
  * **Material:** Aluminium (eloxiert), hohl oder massiv (je nach Batch)
  * **Suitability 100Kmh 3S:** JA. Aluminium ist hier besser als Stahl, da die geringere rotierende Masse bei ca. 26.000 U/min weniger Vibrationen erzeugt.

#### Joint Cups

  * **Component:** Verbindungsstücke (Diff-Inputs)
  * **Material:** Stahl (Gehärtet)
  * **Suitability 100Kmh 3S:** JA. Die Aufnahmen am Differentialeingang sind aus Stahl und halten dem Drehmoment des 3S-Antriebs stand.

#### Rpm Load

  * **Component:** Drehzahl-Belastung
  * **Specification:** Welle rotiert mit ca. 26.000 U/min
  * **Suitability 100Kmh 3S:** Kritisch, aber für das Baukasten-Teil machbar, solange keine Unwucht vorliegt.

### Mandatory Durability Measures


#### Centering Floating Problem

  * **Issue:** Zentrierung (Das 'Floating' Problem)
  * **Description:** Die Welle darf in den Bechern (Cups) nicht hin und her schlagen ('chatter').
  * **Action:** Zwingend kleine O-Ringe oder Schaumstoff-Plättchen (oft im Baukasten enthalten oder aus alten Dämpfer-Gummis geschnitten) in die Becher legen, bevor die Welle eingesetzt wird. Die Welle muss 'schwimmend', aber spielfrei zwischen den Diffs sitzen.

#### Joint Lubrication

  * **Issue:** Schmierung der Gelenke
  * **Description:** Die Enden der Kardanwelle (Dogbones), die in den Stahlbechern laufen, sind Metall auf Metall. Bei 3S-Power entsteht hier massiver Verschleiß ('Einschlagen').
  * **Action:** Diese Kontaktpunkte mit zähem Molybdän-Fett (schwarz) oder speziellem 'Joint Grease' schmieren, um die Reibung zu minimieren.

#### Runout Check

  * **Issue:** Prüfung auf Rundlauf
  * **Description:** Roll die Welle vor dem Einbau über eine Glasplatte (oder einen Spiegel).
  * **Action:** Wenn sie auch nur minimal 'eiert' (verbogen ist), wird sie bei 26.000 U/min das ganze Chassis in zerstörerische Vibrationen versetzen. In diesem Fall muss sie sofort ersetzt werden.


---

## KUEHLUNG


### Cooling Motor

* **Component:** Hobbywing QuicRun 3652SL (4000kV)

#### Heatsink

  * **Size:** 36mm (Passend für 540er / 3650 / 3652 Baugröße)
  * **Material:** Aluminium
  * **Mounting:** Aufsteck-Kühlkörper (Clip-On)

#### Fan Active

  * **Size:** 40x40mm High-Speed Lüfter
  * **Rpm:** 16.000 - 20.000 U/min
  * **Frame Material:** Aluminium (für bessere Wärmeableitung)
  * **Suggested Brands:**
    * Surpass Hobby (Rocket Serie)
    * Yeah Racing (Tornado)
    * WTF (Wild Turbo Fan)
  * **Power Supply:** Anschluss an freien Empfänger-Kanal (z.B. CH3 oder CH4), Stromversorgung direkt über das BEC des Reglers (6.0V/7.4V)

### Cooling Esc

* **Component:** Hobbywing QuicRun WP 10BL120 G2
* **Status:** Keine Modifikation notwendig
* **Description:** Der Regler verfügt ab Werk über einen verschraubten Kühlkörper und einen aktiven Lüfter, der auf die 120A Dauerlast abgestimmt ist und für 3S-Speedruns ausreicht.

### Cooling Best Practices


#### Thermal Paste

  * **Issue:** Wärmeübertragung
  * **Action:** Ein winziger Tropfen PC-Wärmeleitpaste zwischen Motorgehäuse und Alu-Kühlkörper verbessert die Hitzeübertragung massiv.

#### Cable Management

  * **Issue:** Sog des High-Speed-Lüfters
  * **Action:** Alle Sensorkabel und Antennen zwingend mit Kabelbindern fixieren, damit sie nicht vom starken Luftzug in die Rotorblätter gesaugt werden.

#### Body Airflow

  * **Issue:** Hitzestau unter der Karosserie
  * **Action:** Für Speedruns zwingend Lüftungslöcher in die Frontscheibe oder die hinteren Seitenfenster schneiden, damit ein kühlender Durchzug (Airflow) entsteht.


---

## LADEGERAET


### Charger Meta

* **Brand:** SkyRC
* **Model:** S100neo
* **Type:** Smart AC/DC Ladegerät
* **Architecture Fit:** Perfekt. Hat XT60-Buchse direkt im Gehäuse verbaut. Kein Adapter-Chaos.

### Power Specifications

* **Input Voltage Ac:** 100-240V (Integriertes Netzteil für normale Steckdose)
* **Input Voltage Dc:** 6-30V
* **Charge Power Max Ac:** 100W
* **Charge Power Max Dc:** 200W
* **Discharge Power Max:** 5W (Hauptanschluss) / 20W (Balanceport)

### Charging Capabilities


#### Supported Chemistries

  * LiPo
  * LiIon
  * LiFe
  * LiHV
  * NiMH
  * NiCd
  * Pb
* **Supported Cells Lipo:** 1S bis 6S
* **Charge Current Range:** 0.1A - 12.0A
* **Discharge Current Range:** 0.1A - 2.0A
* **Balancer Current Max:** 1.0A

### Physical Specifications

* **Display:** Farb-LCD-Bildschirm

#### Dimensions Mm

  * **Length:** 105
  * **Width:** 105
  * **Height:** 62
* **Weight G:** 340
* **Control Interface:** Einfache 3-Tasten-Steuerung

### Lipo Safety And Workflow

* **Charging Rule:** Den 5000mAh Akku immer mit '1C' laden. Am Ladegerät den Ladestrom auf exakt 5.0A einstellen.
* **Storage Rule:** Nach dem Fahren NIEMALS den Akku leer in die Ecke legen. Immer das 'Storage'-Programm am S100neo starten, um die Zellen auf 3.8V Einlagerungsspannung zu bringen.
* **Fire Safety:** Akkus immer in einem feuerfesten LiPo-Safe-Bag laden und aufbewahren.


---

## LASERTACHOMETER


### Messwerkzeug Meta

* **Typ:** Berührungsloses Laser-Drehzahlmessgerät
* **Referenz Modell:** DT-2234C+ (oder baugleiche Klone wie Neoteck/Proster)
* **Messbereich:** 2.5 bis 99.999 RPM
* **Messgenauigkeit:** +/- 0.05%

#### Shopping Item

  * **In Liste Aufnehmen:** True
  * **Artikel Name:** Digitaler Laser Tachometer (DT-2234C+)
  * **Kategorie:** Werkstatt & Tools
  * **Referenz Link:** Suche bei Amazon nach 'Laser Tachometer DT-2234C+'
  * **Geschaetzter Preis Eur:** 18.0

### Test Protokoll

* **Vorbereitung:** Reflektorstreifen (beiliegend) auf Reifenflanke oder Ritzel kleben.
* **Durchfuehrung:** Fahrzeug sicher aufbocken. Funke einschalten, Vollgas geben und Laser auf den rotierenden Streifen richten.
* **Sicherheitswarnung:** WICHTIG: Bei 100 km/h Radumdrehungsgeschwindigkeit blähen sich Gummireifen extrem auf (Ballooning). Schutzbrille tragen und nicht direkt in der Fliehkraft-Linie der Räder stehen, falls sich die Verklebung des Reifens löst!


---

## PAINT


### Lackierung Meta

* **Brand:** Tamiya
* **System:** 3-Schicht Metallic-Aufbau
* **Typ:** Spezial-Polycarbonatspray (Lexan) - Ätzt sich in den Kunststoff ein
* **Eigenschaften:** Hochflexibel, extrem widerstandsfähig gegen Abblättern bei Crashes.

#### Shopping Items

  * 🔸 **Item 1:**
    * **Artikel Name:** Tamiya PS-15 Metallic Rot (100ml)
    * **Referenz Link:** Suche nach Tamiya PS-15 bei RC-Shops
    * **Geschaetzter Preis Eur:** 8.5
  * 🔸 **Item 2:**
    * **Artikel Name:** Tamiya PS-12 Silber (100ml)
    * **Referenz Link:** Suche nach Tamiya PS-12 bei RC-Shops
    * **Geschaetzter Preis Eur:** 8.5
  * 🔸 **Item 3:**
    * **Artikel Name:** Tamiya PS-5 Schwarz (100ml)
    * **Referenz Link:** Suche nach Tamiya PS-5 bei RC-Shops
    * **Geschaetzter Preis Eur:** 8.5

### Vorbereitung Prep

* **Schritt 1 Waschen:** Karosserie von INNEN gründlich mit lauwarmem Wasser und einfachem Spülmittel (ohne Pflegezusätze) auswaschen. Mit Küchenpapier trocknen. Das entfernt Produktionsfett und verhindert, dass die Farbe abperlt.
* **Schritt 2 Abkleben:** Die beiliegenden Scheibenaufkleber von INNEN auf die Fenster kleben. Die Ränder der Aufkleber mit dem Fingernagel oder einem Zahnstocher fest anrubbeln, damit später keine Farbe darunterlaufen kann.
* **Schritt 3 Anwaermen:** Alle drei Sprühdosen für 10 Minuten in eine Schüssel mit warmem (nicht kochendem!) Leitungswasser stellen. Der Druck steigt leicht, die Farbe zerstäubt viel feiner und bildet keine dicken Tropfen beim Sprühen.

### Durchfuehrung 3 Schicht

* **Regel Nummer 1:** LEXAN WIRD IMMER VON INNEN LACKIERT! Die äußere, matte Schutzfolie bleibt bis zum allerletzten Schritt auf der Karosserie!

#### Phase 1 Hauptfarbe Ps15

  * **Durchgaenge:** 3 bis 4 hauchdünne Schichten
  * **Technik:** Die ERSTE Schicht ist nur ein feiner Nebel (Klebeschicht). Sie MUSS fleckig und durchsichtig aussehen! Nicht versuchen, es sofort deckend zu machen. 10 Minuten warten. Dann die nächste dünne Schicht sprühen. Wiederholen, bis das Rot aufgebraucht ist.

#### Phase 2 Brillanz Ps12

  * **Durchgaenge:** 2 dünne Schichten
  * **Technik:** Wenn das Rot komplett trocken ist (mindestens 30 Min warten), sprühst du das Silber in 2 Durchgängen (mit 10 Min Pause) direkt auf das Rot. Dies wirkt als Reflektor für die Metallic-Partikel und lässt das Rot extrem leuchten.

#### Phase 3 Versiegelung Ps5

  * **Durchgaenge:** 1 bis 2 dünne Schichten
  * **Technik:** Wenn das Silber trocken ist, sprühst du das Schwarz als letzte Schicht darüber. Das blockt jegliches Licht von unten, macht das Rot extrem satt und sorgt dafür, dass dein Auto von innen hochprofessionell schwarz und sauber aussieht.

### Finish Und Montage

* **Schritt 1 Masken Entfernen:** Wenn das Schwarz handtrocken ist (nach ca. 1-2 Stunden), die Fenstermasken von innen vorsichtig abziehen.
* **Schritt 2 Magic Moment:** Jetzt die äußere, matte Schutzfolie der Karosserie abziehen. Darunter kommt das spiegelglatte, perfekte Metallic-Rot zum Vorschein!


---

## REIFEN


### Reifen Meta

* **Brand:** Sweep Racing
* **Model:** HANKOOK Tread Belted (SR-SSF-36AWPG)
* **Typ:** Gewebeverstärkter Gummi-Hohlkammerreifen (Belted)
* **Profil:** Lizenziertes Hankook Profil (für Parkplatz-Asphalt optimiert)
* **Shore Haerte:** 36° (Medium/Hard - idealer Kompromiss aus Grip und Haltbarkeit bei extremer Reibung)
* **Radmitnehmer:** 12mm Sechskant (Hex) - Passend für Baukasten-Mitnehmer des Carten T410R
* **Montage Status:** Pre-glued (Ab Werk industriell verklebt auf Speichenfelgen)

#### Shopping Item

  * **In Liste Aufnehmen:** True
  * **Artikel Name:** Sweep HANKOOK Belted Tires 36deg Pre-glued (SR-SSF-36AWPG)
  * **Kategorie:** Räder & Reifen
  * **Referenz Link:** Suche nach Sweep SR-SSF-36AWPG bei gängigen RC-Shops
  * **Geschaetzter Preis Eur:** 34.9

### Setup Instructions

* **Ballooning Schutz:** Dank der inneren Kevlar-/Nylon-Gewebeeinlage dehnt sich der Reifen bei ca. 8.800 U/min (Achsdrehzahl bei 100 km/h) nicht aus. Die Aerodynamik der ZooRacing Hellcat und die Bodenfreiheit bleiben dadurch konstant sicher.
* **Radmuttern Sicherung:** Zwingend Stoppmuttern mit intaktem Nylonring (M4) verwenden und fest anziehen. Die brachiale Beschleunigung des 3660er Motors kann lockere Muttern sofort abdrehen.
* **Auswuchten:** Trotz industrieller Fertigung können Reifen leichte Unwuchten haben. Bei starken Vibrationen am aufgebockten Chassis die Räder auswuchten (z.B. mit Knetblei in der Felge), um die Radlager des Carten T410R bei 100 km/h nicht zu zerstören.
* **Einfahren Scrubbing:** Die glatte Produktionsschicht auf dem Gummi muss erst abgefahren werden. Die ersten Testläufe zum Kalibrieren des ESCs nutzen, um den Grip für den finalen Topspeed-Run aufzubauen.


---

## SERVO


### Servo Meta

* **Brand:** JX
* **Model:** PDI-4409MG
* **Type:** Digitales Low-Profile Servo
* **Features:** Coreless Motor (schnelles Ansprechverhalten), exzellentes Preis-Leistungs-Verhältnis
* **Price Class:** Budget (~15 - 22 EUR)

### Mechanical Specifications

* **Gears:** Metallgetriebe (Aluminium/Kupfer - überlebenswichtig bei 100 km/h)
* **Case:** Kunststoff mit Aluminium-Mittelteil (als Kühlkörper für den Motor)
* **Spline Teeth:** 25T (WICHTIG: Standard Futaba/Savöx/JX Zahnkranz)

#### Dimensions Mm

  * **Length:** 40.3
  * **Width:** 20.2
  * **Height:** 26.1
* **Weight G:** 44.5

### Performance Specifications

* **Operating Voltage:** 4.8V - 6.0V
* **Torque 6V:** 9.2 kg-cm
* **Speed 6V:** 0.11 sec / 60°
* **Return To Center Accuracy:** Gut (Völlig ausreichend für das angepeilte Speedrun-Projekt)

### Mandatory Upgrades

* **Part:** Aluminium-Servohorn (Zwingend 25T Verzahnung für JX/Futaba kaufen!)
* **Reason:** Das Baukasten-Plastikhorn verbiegt sich (Flex) bei 100 km/h unter dem extremen Winddruck auf die Vorderräder. Das Alu-Horn garantiert eine absolut steife, spielfreie Lenkverbindung.
* **Installation:** Die Schraube, die das Horn auf dem Servo hält, zwingend mit Schraubensicherungslack (z. B. Loctite mittelfest) fixieren, damit sie sich durch Vibrationen nicht löst.

### Transmitter Setup

* **Dual Rate:** Für den 100 km/h Run muss an der Fernsteuerung zwingend das 'Dual Rate' (D/R) oder der Lenkausschlag (EPA) auf ca. 30-40% reduziert werden. Minimale Lenkbewegungen reichen bei Top-Speed völlig aus. Voller Ausschlag führt zum sofortigen Überschlag.


---

## WERKZEUG


### Werkzeug Meta

* **Beschreibung:** Benötigtes Werkzeug für den Zusammenbau des Carten T410R.

### Werkzeug Liste


#### Inbus Schraubendreher

  * **Typ:** Innensechskant-Schraubendreher (Hex Wrenches)
  * **Groessen:** 1.5 mm, 2.0 mm, 2.5 mm
  * **Hinweis:** Pflichtkauf! Carten nutzt im gesamten Auto metrische M3-Maschinenschrauben (keine selbstschneidenden Schrauben). Ein hochwertiger Inbus ist hier extrem wichtig, um die Schraubenköpfe und das harte Plastikgewinde beim Eindrehen nicht zu beschädigen.
  * **Brand:** Neewer
  * **Model:** Titan RC Inbus Set (1.5/2.0/2.5/3.0)

#### Steckschluessel

  * **Typ:** RC Radkreuz / Steckschlüssel (Box Wrench)
  * **Groessen:** 5.5 mm und 7.0 mm
  * **Hinweis:** Die 5.5 mm brauchst du permanent für alle M3-Muttern im Chassis. Die 7.0 mm sind für die Radmuttern. Die in der Carten-Anleitung erwähnten 10.0 mm werden bei diesem 1/10 Modell überhaupt nicht benötigt.
  * **Status:** Vorhanden (Kein Kauf nötig)

#### Klebstoffe Und Chemie

  * **Schraubensicherung:**
    * **Typ:** Schraubensicherungslack (Screw Cement / Threadlocker)
    * **Hinweis:** Extrem wichtig! Kommt an alle Schrauben, die in Metall gedreht werden (z. B. Motorritzel). In der Carten-Anleitung oft fälschlicherweise als 'GLUE' beschriftet. Niemals für Plastik verwenden!
    * **Brand:** Loctite
    * **Model:** 243 Mittelfest (Blau)

#### Klebebaender

  * **Panzertape:**
    * **Typ:** Glasfaserklebeband (Glass Tape)
    * **Hinweis:** Pflicht für den T410R! Das Auto besitzt keine klassischen Plastik-Akkuhalterungen. Das Klebeband wird laut Anleitung durch die Schlitze im Carbon-Chassis gezogen, um den LiPo-Akku festzuschnallen.
    * **Brand:** Arrowmax
    * **Model:** Fibre Tape / Battery Tape


---
