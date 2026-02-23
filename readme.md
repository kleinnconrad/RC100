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

---

## 🏆 High-End Benchmarks (Zum Vergleich)
Um das Preis-Leistungs-Verhältnis und den ingenieurstechnischen Ansatz unseres 100 km/h-Projekts richtig einzuordnen, betrachten wir hier die aktuellen Referenz-Chassis aus dem professionellen Tourenwagen-Wettbewerb. 

Diese Modelle repräsentieren das absolute obere Ende des Marktes in Sachen Toleranzen, extrem tiefem Schwerpunkt und Materialgüte:

| Hersteller & Modell | Antriebsart | Technisches Highlight | Ca. Preis (Bausatz) |
| :--- | :--- | :--- | :--- |
| **Schumacher Mi9** | Riemen | Britisches Top-Engineering, extrem tiefer Schwerpunkt | ~ 649 € |
| **Xray X4** | Riemen | Ultra-Low-Profile Dämpfer, Referenzklasse bei Qualität | ~ 702 € |
| **Awesomatix A800RR** | Riemen | Revolutionäres Rotationsdämpfer-System (ohne Federn) | ~ 780 € |

> **Unser Fazit:** Mit dem Carten T410R (~180 €) setzen wir bewusst auf eine mechanisch extrem robuste und wartungsarme **Kardan-Plattform**. Wir zahlen nur einen Bruchteil der Wettbewerbs-Boliden, treffen für reine Geradeaus-Speedruns aber den absoluten Sweet Spot aus Steifigkeit, Stabilität und Budget.

---
