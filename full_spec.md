# 🏎️ RC100 Gesamtspezifikation (Full Spec)

> **Automatischer Build:** Diese Datei wird aus den modularen Spezifikationen generiert.

---

## ⚙️ AKKU


### 📦 Battery Meta

* **Brand:** Absima
* **Series:** GreenHorn Line V2
* **Part Number:** 4140014
* **Type:** LiPo (Lithium-Polymer)

### 📦 Electrical Specifications

* **Voltage:** 11.1V (Nennspannung)
* **Cells:** 3S
* **Capacity:** 5000 mAh
* **Energy:** 55.5 Wh
* **Discharge Rate Continuous:** 50C
* **Max Continuous Amp Draw:** 250A

### 📦 Connectors

* **Main Power:** XT60 (Plug & Play mit Hobbywing QuicRun G2 ESC)
* **Balancer:** XH (Standard-Balancer für das Ladegerät)

### 📦 Physical Specifications

* **Case Type:** Hardcase (HC) - Hartplastik Box
* **Safety:** Zwingend erforderlich für Speedruns zum Schutz vor Kardanwelle/Crashes
* **Weight G:** 370

#### 🔹 Dimensions

  * **Length Mm:** 138
  * **Width Mm:** 46
  * **Height Mm:** 35

### 📦 Chassis Integration Notes

* **Issue:** Der Carten T410R ist ab Werk für 2S-Akkus (25mm Höhe) konzipiert. Dieser 3S-Akku ist 35mm hoch.
* **Solution:** Die obere Carbon-Akkustrebe des Chassis muss 'höhergelegt' werden.

#### 🔹 Required Parts

  * 2x Distanzhülsen/Spacers (Kunststoff oder Alu) mit ca. 10mm Höhe
  * 2x minimal längere M3-Schrauben (ca. M3x16 oder M3x18)
* **Execution:** Spacers auf die originalen Alu-Pfosten legen, Carbon-Strebe darauf verschrauben. Kein Dremeln oder Fräsen am Chassis notwendig.


---

## ⚙️ BRUSHLESS COMBO


### 📦 Combo Meta

* **Brand:** Hobbywing
* **Series:** QuicRun Generation 2 (G2)
* **Part Number:** HW38030208
* **Waterproof Rating:** IP67 (Regler)

### 📦 Esc Specifications

* **Model:** QuicRun WP 10BL120 G2
* **Type:** Brushless (Sensored & Sensorless unterstützt)
* **Current Continuous:** 120A
* **Current Burst:** 760A
* **Voltage Input:** 2S - 4S LiPo
* **Bec Output:** 6.0V / 7.4V schaltbar bei 5A
* **Cooling Fan:** Ja (wird über das BEC betrieben)

#### 🔹 Programming Options

  * LED Programmierkarte
  * LCD Programmierbox (G2)
* **Battery Connector:** XT60 (ab Werk verlötet)

#### 🔹 Motor Limits

  * **Limit 3S:** <= 4000kV (Baugröße max. 3660)
  * **Limit 4S:** <= 2600kV (Baugröße max. 4268)

#### 🔹 Dimensions

  * **Length Mm:** 52.8
  * **Width Mm:** 39.8
  * **Height Mm:** 38.2
* **Weight G:** 119

### 📦 Motor Specifications

* **Model:** QuicRun 3652SL G2
* **Type:** Brushless (Sensorlos / Sensorless)
* **Poles:** 4
* **Kv Rating:** 4000
* **Voltage Input:** 2S - 3S LiPo
* **No Load Current:** 5.3A

#### 🔹 Dimensions

  * **Diameter Mm:** 36.0
  * **Length Mm:** 52.0

#### 🔹 Shaft

  * **Diameter Mm:** 3.175
  * **Length Mm:** 15.0
* **Weight G:** 224
* **Housing:** CNC-gefrästes Aluminium

### 📦 Compatibility Check

* **Chassis Fit:** Perfekt. Motor-Durchmesser 36mm passt exakt in den T410R Motorhalter.
* **Gearing Fit:** Perfekt. 3.175mm Welle nimmt Standard 48dp Ritzel auf.
* **Power Headroom:** Gut. Motor ist an der Obergrenze des ESCs bei 3S, aber die 120A Dauerleistung fangen die Spitzen sicher ab.


---

## ⚙️ CARTENT410R


### 📦 Chassis Meta

* **Brand:** Carten
* **Model:** T410R Tourenwagen Bausatz
* **Part Number:** NHA413

### 📦 Carten T410R


#### 🔹 Allgemein

  * **Fahrzeugtyp:** 1:10 Elektro Tourenwagen (EP Touring Car)
  * **Lieferzustand:** Bausatz (Kit) - unmontiert
  * **Einsatzbereich:** On-Road / Asphalt / Teppich

#### 🔹 Abmessungen

  * **Spurbreite Mm:** 190
  * **Radstand Mm:** 258

#### 🔹 Chassis Und Aufbau

  * **Bodenplatte:** 2,25 mm Eco-Carbon (kohlefaserverstärktes Verbundmaterial)
  * **Oberdeck:** 2,0 mm Eco-Carbon
  * **Daempferbruecken:** 3,0 mm Eco-Carbon (vorne & hinten, diverse Montagepunkte)
  * **Motorhalterung:** CNC-gefrästes Aluminium
  * **Servohalterung:** Floating Servo Mount (Aluminium)
  * **Akkuhalterung:** Vorbereitet für 2S Standard-LiPo (Stickpack) oder Shorty-LiPo
  * **Karosseriehalter:** Verstellbare Kunststoff-Pfosten

#### 🔹 Antriebsstrang

  * **Antriebsart:** 4WD Allrad, zentraler Kardanantrieb (Wellenantrieb)
  * **Mittelantriebswelle:** Aluminium (rot eloxiert)
  * **Differentiale:** Gekapselte Kegeldifferentiale (vorne & hinten)
  * **Differential Zahnraeder:** Metallzahnräder
  * **Antriebswellen:** Stahl CVD (Constant Velocity Drives) an Vorder- und Hinterachse
  * **Hauptzahnradhalterung:** Aluminium
  * **Radmitnehmer:** 12 mm Sechskant, Aluminium
  * **Interne Untersetzung:** 1:2.47 bis 1:2.53
  * **Kugellager:** Komplett kugelgelagert (mit Gummidichtungen)

#### 🔹 Fahrwerk Und Federung

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

#### 🔹 Lenkung

  * **Lenksystem:** Kugelgelagertes Dual-Bellcrank-System (Doppelarm)
  * **Lenkhebel C Hubs:** Composite-Kunststoff


---

## ⚙️ DIFFERENTIALE


### 📦 Differential Meta

* **Type:** Öldruck-Kegeldifferential (Metal Gear)
* **Mechanical Load Capacity:** > 100 km/h (ca. 8.300 U/min Achsdrehzahl)

### 📦 Material And Construction

* **Gears Ring And Bevel:** Sintermetall / Stahl
* **Diff Outdrives Cup Joints:** Gehärteter Stahl
* **Diff Case Cup:** Faserverstärkter Verbundkunststoff (Composite)

### 📦 Mandatory Modifications


#### 🔹 Perfect Shimming

  * **Issue:** Spielfreiheit
  * **Description:** Die inneren Metallzahnräder müssen beim Zusammenbau mit hauchdünnen Passscheiben (Shims) absolut spielfrei eingestellt werden. Nur so wird verhindert, dass die Zähne unter dem extremen Drehmoment des 3S-Motors überspringen oder abreißen.

#### 🔹 Reinforced Sealing

  * **Issue:** O-Ring Abdichtung
  * **Description:** Bei 8.300 U/min erzeugt das Öl im Inneren einen massiven Fliehkraftdruck nach außen. Die Gummi-O-Ringe müssen mit zähem Spezialfett (z. B. 'Green Slime') abgedichtet werden, damit das Differential nicht trockenläuft.

#### 🔹 Oil Viscosity

  * **Issue:** Sperrwirkung & Geradeauslauf
  * **Description:** Das Baukasten-Öl ist zu weich und führt bei Speedruns zu unkontrollierbarem Ausbrechen, wenn ein Rad minimal Grip verliert. Es muss extrem zähes Silikonöl verwendet werden, um das Auto auf einen sturen Geradeauslauf zu zwingen.
  * **Setup Recommendation:**
    * **Front Axle:** ca. 100.000 cSt (oder ein komplett starrer Spool/Starrachse)
    * **Rear Axle:** ca. 10.000 cSt


---

## ⚙️ FERNSTEUERUNG


### 📦 Tx Meta Transmitter

* **Brand:** DumboRC
* **Model:** X6
* **Type:** 2.4 GHz Pistolengriff-Sender (Surface)
* **Channels:** 6
* **Price Class:** Budget / MVP (~35 - 45 EUR)

### 📦 Tx Performance

* **Protocol:** FHSS (Frequency-Hopping Spread Spectrum)
* **Range Ground:** 300 - 400 Meter (Überlebenswichtig für 100 km/h Runs)
* **Response Time:** 12 ms (Extrem niedrige Latenz)
* **Power Supply:** 4x AA Batterien (Alternative: 2S LiPo im Batteriefach)

### 📦 Rx Meta Receiver

* **Model:** X6FG (Das 'G' ist das kritische Feature!)
* **Channels:** 6

#### 🔹 Integrated Features

  * Elektronischer Gyroskop-Kreisel (Gyro)
* **Input Voltage:** 4.8V - 10.0V (Kompatibel mit dem 6.0V/7.4V BEC des Hobbywing-Reglers)

### 📦 Calibration And Setup

* **Gyro Activation:** Der Gyro muss am Empfänger meist per Knopf-Kombination (schnelles Drücken) aktiviert werden (LED wechselt die Farbe, meist auf Grün oder Orange). Vor dem Fahren unbedingt aufbocken und prüfen, ob der Gyro in die korrekte Richtung gegenlenkt!
* **Steering Dual Rate:** Über den CH1-Drehregler an der Fernsteuerung den maximalen Lenkausschlag (Dual Rate) zwingend auf ca. 30 % reduzieren. Bei 100 km/h führt ein voller Lenkausschlag zum sofortigen Überschlag.
* **Throttle Trim:** Die Trimmung für das Gas (TH Trim) muss zwingend auf dem Nullpunkt (Mitte) stehen, bevor der Hobbywing-Regler zum ersten Mal kalibriert wird.


---

## ⚙️ KARDANWELLE UND JOINTS


### 📦 Center Shaft Meta

* **Component:** Zentrale Antriebswelle (Center Shaft)

### 📦 Material And Suitability


#### 🔹 Driveshaft

  * **Component:** Kardanwelle (Welle)
  * **Material:** Aluminium (eloxiert), hohl oder massiv (je nach Batch)
  * **Suitability 100Kmh 3S:** JA. Aluminium ist hier besser als Stahl, da die geringere rotierende Masse bei ca. 26.000 U/min weniger Vibrationen erzeugt.

#### 🔹 Joint Cups

  * **Component:** Verbindungsstücke (Diff-Inputs)
  * **Material:** Stahl (Gehärtet)
  * **Suitability 100Kmh 3S:** JA. Die Aufnahmen am Differentialeingang sind aus Stahl und halten dem Drehmoment des 3S-Antriebs stand.

#### 🔹 Rpm Load

  * **Component:** Drehzahl-Belastung
  * **Specification:** Welle rotiert mit ca. 26.000 U/min
  * **Suitability 100Kmh 3S:** Kritisch, aber für das Baukasten-Teil machbar, solange keine Unwucht vorliegt.

### 📦 Mandatory Durability Measures


#### 🔹 Centering Floating Problem

  * **Issue:** Zentrierung (Das 'Floating' Problem)
  * **Description:** Die Welle darf in den Bechern (Cups) nicht hin und her schlagen ('chatter').
  * **Action:** Zwingend kleine O-Ringe oder Schaumstoff-Plättchen (oft im Baukasten enthalten oder aus alten Dämpfer-Gummis geschnitten) in die Becher legen, bevor die Welle eingesetzt wird. Die Welle muss 'schwimmend', aber spielfrei zwischen den Diffs sitzen.

#### 🔹 Joint Lubrication

  * **Issue:** Schmierung der Gelenke
  * **Description:** Die Enden der Kardanwelle (Dogbones), die in den Stahlbechern laufen, sind Metall auf Metall. Bei 3S-Power entsteht hier massiver Verschleiß ('Einschlagen').
  * **Action:** Diese Kontaktpunkte mit zähem Molybdän-Fett (schwarz) oder speziellem 'Joint Grease' schmieren, um die Reibung zu minimieren.

#### 🔹 Runout Check

  * **Issue:** Prüfung auf Rundlauf
  * **Description:** Roll die Welle vor dem Einbau über eine Glasplatte (oder einen Spiegel).
  * **Action:** Wenn sie auch nur minimal 'eiert' (verbogen ist), wird sie bei 26.000 U/min das ganze Chassis in zerstörerische Vibrationen versetzen. In diesem Fall muss sie sofort ersetzt werden.


---

## ⚙️ KUEHLUNG


### 📦 Cooling Motor

* **Component:** Hobbywing QuicRun 3652SL (4000kV)

#### 🔹 Heatsink

  * **Size:** 36mm (Passend für 540er / 3650 / 3652 Baugröße)
  * **Material:** Aluminium
  * **Mounting:** Aufsteck-Kühlkörper (Clip-On)

#### 🔹 Fan Active

  * **Size:** 40x40mm High-Speed Lüfter
  * **Rpm:** 16.000 - 20.000 U/min
  * **Frame Material:** Aluminium (für bessere Wärmeableitung)
  * **Suggested Brands:**
    * Surpass Hobby (Rocket Serie)
    * Yeah Racing (Tornado)
    * WTF (Wild Turbo Fan)
  * **Power Supply:** Anschluss an freien Empfänger-Kanal (z.B. CH3 oder CH4), Stromversorgung direkt über das BEC des Reglers (6.0V/7.4V)

### 📦 Cooling Esc

* **Component:** Hobbywing QuicRun WP 10BL120 G2
* **Status:** Keine Modifikation notwendig
* **Description:** Der Regler verfügt ab Werk über einen verschraubten Kühlkörper und einen aktiven Lüfter, der auf die 120A Dauerlast abgestimmt ist und für 3S-Speedruns ausreicht.

### 📦 Cooling Best Practices


#### 🔹 Thermal Paste

  * **Issue:** Wärmeübertragung
  * **Action:** Ein winziger Tropfen PC-Wärmeleitpaste zwischen Motorgehäuse und Alu-Kühlkörper verbessert die Hitzeübertragung massiv.

#### 🔹 Cable Management

  * **Issue:** Sog des High-Speed-Lüfters
  * **Action:** Alle Sensorkabel und Antennen zwingend mit Kabelbindern fixieren, damit sie nicht vom starken Luftzug in die Rotorblätter gesaugt werden.

#### 🔹 Body Airflow

  * **Issue:** Hitzestau unter der Karosserie
  * **Action:** Für Speedruns zwingend Lüftungslöcher in die Frontscheibe oder die hinteren Seitenfenster schneiden, damit ein kühlender Durchzug (Airflow) entsteht.


---

## ⚙️ LADEGERAET


### 📦 Charger Meta

* **Brand:** SkyRC
* **Model:** S100neo
* **Type:** Smart AC/DC Ladegerät
* **Architecture Fit:** Perfekt. Hat XT60-Buchse direkt im Gehäuse verbaut. Kein Adapter-Chaos.

### 📦 Power Specifications

* **Input Voltage Ac:** 100-240V (Integriertes Netzteil für normale Steckdose)
* **Input Voltage Dc:** 6-30V
* **Charge Power Max Ac:** 100W
* **Charge Power Max Dc:** 200W
* **Discharge Power Max:** 5W (Hauptanschluss) / 20W (Balanceport)

### 📦 Charging Capabilities


#### 🔹 Supported Chemistries

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

### 📦 Physical Specifications

* **Display:** Farb-LCD-Bildschirm

#### 🔹 Dimensions Mm

  * **Length:** 105
  * **Width:** 105
  * **Height:** 62
* **Weight G:** 340
* **Control Interface:** Einfache 3-Tasten-Steuerung

### 📦 Lipo Safety And Workflow

* **Charging Rule:** Den 5000mAh Akku immer mit '1C' laden. Am Ladegerät den Ladestrom auf exakt 5.0A einstellen.
* **Storage Rule:** Nach dem Fahren NIEMALS den Akku leer in die Ecke legen. Immer das 'Storage'-Programm am S100neo starten, um die Zellen auf 3.8V Einlagerungsspannung zu bringen.
* **Fire Safety:** Akkus immer in einem feuerfesten LiPo-Safe-Bag laden und aufbewahren.


---

## ⚙️ REIFEN


### 📦 Reifen Meta

* **Brand:** Sweep Racing
* **Model:** HANKOOK Tread Belted tires Pre-glued set Pro-compound 36deg for Asphalt
* **Part Number:** SR-SSF-36AWPG
* **Type:** Gewebeverstärkte Gummireifen (Belted), fertig verklebt

### 📦 Physical Specifications

* **Width:** 24mm (Standard 1:10 Tourenwagen)
* **Hex Size:** 12mm
* **Compound:** 36 Shore (Hart / optimiert für Asphalt)
* **Tread Pattern:** Hankook lizenziertes Profil (Rillen)
* **Wheel Design:** 12-Speichen-Felge (Weiß)
* **Surface Recommendation:** Asphalt (Alltag / ungesäubert)

### 📦 Performance Features

* **Anti Ballooning:** Ein eingegossener Kevlar-/Aramid-Gürtel verhindert das lebensgefährliche Ausdehnen (Pizza-Cutter-Effekt) bei den angepeilten 44.000 U/min (100 km/h).
* **Pre Glued:** Ab Werk industriell verklebt, was das Risiko minimiert, dass sich der Reifen bei extremen Fliehkräften von der Felge löst.

### 📦 Architecture Rationale

* **Why Not Slicks:**
  > Ein profilloser Voll-Slick (z. B. Sweep EXP Belted Slicks) bietet theoretisch die absolute
  > Höchstleistung, maximale Kontaktfläche (100 % Gummi) und extreme Laufruhe bei 100 km/h.
  > Dieser Vorteil gilt jedoch nur auf perfekt präparierten, staubfreien Rennstrecken.
  > Im realen Einsatz auf normalen Straßen oder Parkplätzen sammeln Slicks den feinen Staub auf
  > und verlieren massiv an Traktion. Das gewählte Hankook-Profil mit seinen Rillen kann diesen
  > Straßenschmutz abtransportieren und bietet auf ungesäubertem Asphalt ein deutlich sichereres,
  > gutmütigeres Fahrverhalten bei voller Anti-Ballooning-Sicherheit.


---

## ⚙️ SERVO


### 📦 Servo Meta

* **Brand:** Savöx
* **Model:** SC-1251MG+
* **Type:** Digitales Low-Profile Servo
* **Features:** Softstart (Verhindert hartes Zucken beim Einschalten, schont die Mechanik)
* **Price Class:** Mid-Range (~55 EUR)

### 📦 Mechanical Specifications

* **Gears:** Metallgetriebe (Titan/Aluminium)
* **Case:** Teil-Aluminium (für bessere Wärmeableitung)
* **Spline Teeth:** 25T (WICHTIG: Standard Savöx/Futaba Zahnkranz)

#### 🔹 Dimensions Mm

  * **Length:** 40.8
  * **Width:** 20.2
  * **Height:** 25.4
* **Weight G:** 44.5

### 📦 Performance Specifications

* **Operating Voltage:** 4.8V - 6.0V
* **Torque 6V:** 9.0 kg-cm
* **Speed 6V:** 0.09 sec / 60°
* **Return To Center Accuracy:** Sehr hoch (Kritisch für stabilen Geradeauslauf bei 100 km/h)

### 📦 Mandatory Upgrades

* **Part:** Aluminium-Servohorn (Zwingend 25T Verzahnung für Savöx kaufen!)
* **Reason:** Das Baukasten-Plastikhorn verbiegt sich (Flex) bei 100 km/h unter dem extremen Winddruck auf die Vorderräder. Das Alu-Horn garantiert eine absolut steife, spielfreie Lenkverbindung.
* **Installation:** Die Schraube, die das Horn auf dem Servo hält, zwingend mit Schraubensicherungslack (z. B. Loctite mittelfest) fixieren, damit sie sich durch Vibrationen nicht löst.

### 📦 Transmitter Setup

* **Dual Rate:** Für den 100 km/h Run muss an der Fernsteuerung zwingend das 'Dual Rate' (D/R) oder der Lenkausschlag (EPA) auf ca. 30-40% reduziert werden. Minimale Lenkbewegungen reichen bei Top-Speed völlig aus. Voller Ausschlag führt zum sofortigen Überschlag.


---

## ⚙️ ZAHNFLANKENSPIEL


### 📦 Compatibility Check Gearing

* **Status:** PASS
* **Fitment Type:** Drop-In-Fit
* **Modifications Required:** Keine (Kein Fräsen oder Dremeln notwendig)

#### 🔹 Tooth Sum Theory

  * **Description:** Der Abstand zwischen Motorwelle und Hauptwelle ist durch die Langlöcher im Aluminium-Motorhalter begrenzt. Die Passgenauigkeit lässt sich bei gleichem Pitch (48dp) über die Summe der Zähne beider Zahnräder berechnen.

#### 🔹 Setups Comparison

  * **Standard Setup:**
    * **Spur Gear Teeth:** 72
    * **Pinion Gear Teeth:** 30
    * **Total Teeth:** 102
  * **Speedrun Setup:**
    * **Spur Gear Teeth:** 64
    * **Pinion Gear Teeth:** 38
    * **Total Teeth:** 102

#### 🔹 Conclusion

  * **Result:** Da die Zähnesumme (102 Zähne) und damit der physische Gesamtdurchmesser beider Setups exakt identisch ist, bleibt der Motor sicher im Verstellbereich der Langlöcher.
  * **Gear Mesh Setup:** Es gibt ausreichend Spielraum, um das Zahnflankenspiel (Gear Mesh) mit dem Papier-Trick perfekt einzustellen.

### 📦 Purchasing And Installation Tips


#### 🔹 Spur Gear

  * **Teeth:** 64
  * **Pitch:** 48dp
  * **Mounting Requirement:** Muss Standard-Bohrungen in der Mitte haben (meist 3 oder 4 Löcher im Kreis), um auf den Carten-Aluminium-Mitnehmer geschraubt werden zu können.
  * **Suggested Brands:**
    * Arrowmax
    * Kimbrough

#### 🔹 Pinion Gear

  * **Teeth:** 38
  * **Pitch:** 48dp
  * **Clearance Warning:** Ein 38Z Ritzel ist physisch massiv. Beim Einbau zwingend prüfen, dass das große Ritzel nicht an der rotierenden Aluminium-Kardanwelle in der Mitte schleift. Ein minimaler Sicherheitsabstand muss zwingend erhalten bleiben.


---
