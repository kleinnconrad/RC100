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

## 🚀 Architektur-Dokumentation & Automatisierung

Dieses Repository nutzt einen **"Docs-as-Code"** Ansatz. Die Fahrzeugspezifikationen sind modular in einzelnen YAML-Dateien abgelegt und werden automatisch zu einer Gesamtspezifikation zusammengeführt.

## 📂 Ordnerstruktur

```text
.
├── .github/workflows/
│   └── build_spec.yml      # GitHub Action (Pipeline-Logik)
├── specs/                  # Fachmodule (Einzel-Spezifikationen)
│   ├── spec_motor.yaml
│   ├── spec_akku.yaml
│   └── ...
├── merge_specs.py          # Python-Merge-Skript (SSOT-Logik)
└── full_spec.yaml          # Generierte Gesamtspezifikation (Build-Artefakt)
```

## ⚙️ Der Automatisierungs-Workflow
Um Konsistenz zu gewährleisten, wird die Datei full_spec.yaml niemals manuell bearbeitet. Der Prozess ist vollständig automatisiert:
Änderung: Eine Spezifikation im Ordner specs/ wird angepasst (z. B. Zellenzahl im Akku-Modul).
Push: Die Änderung wird auf den main-Branch gepusht.
CI-Pipeline: GitHub Actions erkennt die Änderung und startet einen virtuellen Runner.
Merge: Das Skript merge_specs.py sucht rekursiv nach allen spec_*.yaml Dateien und führt sie zusammen.
Sync: Der GitHub-Bot committet die aktualisierte full_spec.yaml automatisch zurück in das Repository.

## 🛠 Manuelle Synchronisation
Sollte die Pipeline lokal getestet werden müssen, kann das Skript manuell ausgeführt werden (erfordert PyYAML):

```text
pip install pyyaml
python merge_specs.py
```

## ⚠️ Wichtige Hinweise für Mitwirkende
Präfix-Regel: Alle Quelldateien müssen mit spec_ beginnen und auf .yaml enden.
Schreibrechte: Die GitHub Action benötigt Read and write permissions (einstellbar unter Settings > Actions > General), um die generierte Datei speichern zu können.
Single Source of Truth: Fachliche Details immer nur in den Modul-Dateien ändern, da die full_spec.yaml bei jedem Push überschrieben wird.

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
