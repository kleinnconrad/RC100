# 🏛️ Architecture Decision Records (ADRs)

Dieses Verzeichnis enthält alle grundlegenden Architektur- und Hardwareentscheidungen für das RC100 Projekt. **Diese Datei wird automatisch generiert. Bitte nicht manuell bearbeiten.**

## 📋 Übersicht

| ID | Datum | Titel | Status | Entscheidung |
| :--- | :--- | :--- | :--- | :--- |
| **ADR-001** | 2026-02-24 | Auswahl der Chassis-Plattform und Make-or-Buy-Entscheidung (100 km/h Benchmark) | 🟡 Offen | MAKE - Carten T410R |
| **ADR-002** | 2026-02-24 | Auswahl der Brushless-Antriebseinheit (ESC & Motor) für 100 km/h Speedruns | 🟡 Offen | Hobbywing QuicRun WP 10BL120 G2 Combo |

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
