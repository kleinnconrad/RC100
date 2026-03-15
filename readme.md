# RC100: 100 km/h 1:10 RC-Auto-Projekt

Willkommen im RC100 Projekt-Repository. Dies ist ein privates Projekt mit dem Ziel, einen **RC Onroad Tourenwagen im Maßstab 1:10** zu entwerfen und zu bauen, der Geschwindigkeiten von **mindestens 100 km/h** erreicht. Das primäre technische Ziel ist es, die Leistung zu maximieren und den Bau gleichzeitig so **günstig** und **zuverlässig** wie möglich zu halten.

## 📂 Repository-Struktur

Das Projekt ist in themenspezifische Unterordner gegliedert, um Spezifikationen, Daten und Designs übersichtlich zu strukturieren:

* **/architektur** - Für Architectural Decision Records (ADRs) und grundlegende Systemdesigns.
* **/elektronik** - Für elektronische Komponenten und zugehörige Spezifikationen.
* **/mechanik** - Für mechanische Teile,  Chassis-Design und physische Spezifikationen.
* **/messdaten** - Für Testergebnisse und Leistungsmessdaten.
* **/projekt** - Für allgemeines Projektmanagement, Planung und Übersichten.
* **/scripts** - Für Automatisierungen und Berechnungen.

---

## 🛠️ Arbeitsweise in diesem Repository

Alle Mitwirkenden können Standard-Git-Praktiken (Branching, Committing, Pulling, Pushing) nutzen, um allgemeine Projektinformationen, CAD-Dateien oder Testdaten in die jeweiligen Unterordner hochzuladen. Für Spezifikationen und Architektur-Entscheidungen gelten die folgenden spezifischen Workflows.

### 1. Hinzufügen oder Ändern von Spezifikationen
Systemspezifikationen werden thematisch verteilt in den entsprechenden Unterordnern verwaltet. 

* **Format:** YAML
* **Namenskonvention:** `spec_<beschreibender_name>.yaml` (z. B. `spec_motor.yaml`)
* **Speicherort:** Platziere die Datei in dem Unterordner, der thematisch am besten passt (z. B. `/elektronik`).
* **Workflow:** Datei einfach committen und pushen. Unsere automatisierte Pipeline fasst alle individuellen Spezifikationen in einer zentralen `full_spec.yaml` und einer formatierten `full_spec.md` im Hauptverzeichnis zusammen.

> **Tipp:** Wenn du mit der YAML-Syntax nicht vertraut bist, empfehlen wir dringend, ein LLM (Large Language Model wie Gemini oder ChatGPT) zu verwenden, um die YAML-Struktur für dich zu generieren. Beschreibe deine Spezifikation einfach als normalen Text und bitte das LLM, sie als saubere YAML-Datei zu formatieren.

### 2. Dokumentation von Architektur-Entscheidungen (ADRs)
Wann immer eine wichtige Designentscheidung getroffen wird (z. B. die Wahl eines bestimmten Motorprotokolls), sollte diese als ADR dokumentiert werden.

* **Format:** YAML
* **Namenskonvention:** `adr_<beschreibender_name>.yaml` (z. B. `adr_batteriechemie.yaml`)
* **Speicherort:** Muss im Ordner `/architektur` abgelegt werden.
* **Workflow:** Datei committen und pushen. Eine automatisierte Pipeline kompiliert alle ADRs sofort in eine gut lesbare `README.md` im Ordner `/architektur`.

> **Tipp:** Genau wie bei den Spezifikationen gilt: Wenn du nicht weißt, wie man ein ADR in YAML strukturiert, nutze ein LLM, um deine Entscheidungsnotizen in eine korrekt formatierte YAML-Datei zu übersetzen.

---

## 🤖 Automatisierung & GitHub Actions

Dieses Repository nutzt GitHub Actions (im Ordner `.github/workflows/`), um automatisch Dokumentationen zu generieren und Konfigurationen zusammenzuführen. Du musst im Normalfall nichts tun, um diese auszulösen – sie starten automatisch, wenn entsprechende Dateien hochgeladen oder geändert werden.

### Verfügbare Workflows

1. **Build Spec (`build_spec.yml`)**
    * **Auslöser:** Startet automatisch, wenn eine Datei mit dem Muster `spec_*.yaml` in einem Unterordner hinzugefügt oder geändert wird.
    * **Aktion:** Führt `merge_specs.py` aus, um alle einzelnen Spezifikationsdateien zu einer einzigen, zentralen `full_spec.yaml` im Hauptverzeichnis zusammenzuführen.
2. **Build Full Spec MD (`build_full_spec_md.yml`)**
    * **Auslöser:** Startet *automatisch als abhängige Aktion* direkt nach dem erfolgreichen Abschluss von `build_spec.yml`.
    * **Aktion:** Führt `yaml_to_md.py` aus, um die rohe `full_spec.yaml` in eine ansprechende, gut lesbare `full_spec.md` im Hauptverzeichnis umzuwandeln.
3. **Build ADR Readme (`build_adr_readme.yml`)**
    * **Auslöser:** Startet automatisch, wenn eine Datei mit dem Muster `adr_*.yaml` im Ordner `/architektur` hinzugefügt oder geändert wird.
    * **Aktion:** Führt `generate_adr_readme.py` aus, um alle ADRs in einer zentralen `architektur/README.md` zusammenzustellen, die eine chronologische Übersicht der Projektentscheidungen bietet.

4. **Build shopping list (`build_spec.yml`)**
    * **Auslöser:** Startet automatisch, wenn eine Datei mit dem Muster `spec_*.yaml` in einem Unterordner hinzugefügt oder geändert wird.
    * **Aktion:** Führt `generate_shopping_list.py` aus, um eine shopping list im Ordner `projekt/kosten`zu erstellen.

### Workflows manuell auslösen
Wenn du Änderungen an den Python-Skripten testest oder die Dokumentation neu generieren möchtest, ohne eine Spec/ADR zu ändern, kannst du diese Aktionen manuell starten:
1. Navigiere zum Tab **Actions** oben im GitHub-Repository.
2. Klicke in der linken Seitenleiste auf den Workflow, den du ausführen möchtest (z. B. `build_spec`).
3. Klicke auf den Button **Run workflow** auf der rechten Seite.
4. Wähle den gewünschten Branch aus und klicke auf den grünen Button **Run workflow**.

## 🧮 Speed & Getriebe Rechner (CLI-Tool)

Um bei 100 km/h nicht blindlings die Elektronik zu überlasten, enthält dieses Repository ein maßgeschneidertes Python-Skript zur Berechnung der optimalen Getriebeübersetzung für den **Carten T410R**. 

Der Rechner simuliert anhand des Reifendurchmessers und der gewünschten Zielgeschwindigkeit die exakte mechanische Belastung (Radlast) für den Motor bei allen passenden Motorritzeln (21Z - 44Z am 72Z Hauptzahnrad). Er warnt vor Überlastung und teilt die möglichen Setups automatisch in Belastungs-Zonen (Grün, Gelb, Rot) für einen 4000kV / 3S Antrieb ein.

**So startest du das Tool lokal:**
```bash
python scripts/calc/getriebe_calc.py
```
## 🚀 Top-Speed & Limit Rechner (CLI-Tool)

Dieser "Reverse-Calculator" ergänzt den Getriebe-Rechner, indem er die maximal mögliche Höchstgeschwindigkeit des Carten T410R auf Basis der physischen Hardware-Limits berechnet. Anstatt eine Wunschgeschwindigkeit vorzugeben, berechnet das Skript anhand deiner Motor- und Akku-Daten sowie deiner persönlichen Schmerzgrenze für die thermische Belastung (Radlast), was das Auto wirklich hergibt.

**So startest du das Tool lokal:**
```bash
python scripts/calc/max_speed.py
```
