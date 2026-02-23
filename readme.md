# 🏎️ Projekt: Carten T410R - The 100 km/h Build

## 📌 Mission Briefing
Dieses Repository dient als "Single Source of Truth" für unser 1:10 RC-Speedrun-Projekt. 
Das Ziel ist es, ein Carten T410R Tourenwagen-Chassis mechanisch und elektronisch so abzustimmen, dass es reproduzierbar und stabil die **100 km/h (62 mph) Marke** knackt, ohne dabei strukturell zu versagen.

## 🛠️ Hardware Stack (Basis)
* **Chassis:** Carten T410R (1:10, 4WD Kardan, 3mm Carbon)
* **Antriebsstrang:** Sintermetall-Differentiale & Aluminium-Kardanwelle
* **Elektronik:** 120A ESC mit 4000kV Brushless Motor
* **Energie:** 3S LiPo (11.1V)
* **Target FDR (Getriebe):** ~ 4.26 (64Z Hauptzahnrad / 38Z Ritzel)

*Die exakten und aktuellen technischen Parameter liegen in der `full_spec.yaml`.*

---

## 🔄 Unser Git-Workflow (Der digitale Boxenstopp)
Da wir am Auto kontinuierlich Parameter (Öl-Viskosität, Ritzel, Fahrwerk) verändern werden, nutzen wir Git, um kein funktionierendes Setup versehentlich zu überschreiben.

### Die goldenen Regeln:
1. **Der Main-Branch (`main`):** Hier liegt *ausschließlich* das aktuell stabile und fahrbare Setup.
2. **Neues Setup testen (Branching):** * Bevor etwas am Auto umgebaut wird, erstellen wir einen neuen Branch (z.B. `setup/diff-oil-100k`).
   * Die Änderungen werden dort im YAML dokumentiert und committet.
3. **Der Track-Test:** Das Auto wird mit dem neuen Setup gefahren.
4. **Auswertung (Pull Request):** * **Erfolg:** Das Auto lag stabil bei Top-Speed -> Wir öffnen einen PR und mergen das neue Setup in `main`.
   * **Fehlschlag:** Das Auto war unfahrbar -> Wir verwerfen den Branch und bauen das Auto mechanisch wieder auf den Stand von `main` zurück.

---

## ⚠️ Safety First & Pre-Flight Checks
> Bei Rad-Drehzahlen jenseits der 8.000 U/min herrschen extreme Fliehkräfte. 
> **Vor jedem Speedrun zwingend prüfen:**
> * Ist das Zahnflankenspiel (Gear Mesh) korrekt?
> * Sitzt die Kardanwelle spielfrei (Floating Check)?
> * Sind die Belted-Reifen intakt und fest verschraubt?

Benchmarks:
- Schumacher Mi9 Chassis 649€
- Awesomatix A800RR 780€
- Xray X4 702€
