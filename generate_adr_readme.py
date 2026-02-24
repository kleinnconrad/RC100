import yaml
import glob
import os

def generate_adr_readme():
    # Pfad auf kleingeschriebenes 'architektur' angepasst
    adr_folder = 'Architektur'
    readme_path = os.path.join(adr_folder, 'README.md')
    search_pattern = os.path.join(adr_folder, 'adr_*.y*ml')
    
    files = sorted(glob.glob(search_pattern))
    
    if not files:
        print(f"Keine ADR-Dateien im Ordner '{adr_folder}' gefunden.")
        return

    adrs = []
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            try:
                data = yaml.safe_load(f)
                if data:
                    root_key = list(data.keys())[0]
                    adr_content = data[root_key]
                    adrs.append(adr_content)
            except Exception as e:
                print(f"Fehler beim Lesen von {file}: {e}")

    adrs = sorted(adrs, key=lambda x: x.get('id', ''))

    md_lines = []
    md_lines.append("# 🏛️ Architecture Decision Records (ADRs)\n")
    md_lines.append("Dieses Verzeichnis enthält alle grundlegenden Architektur- und Hardwareentscheidungen für das RC100 Projekt. **Diese Datei wird automatisch generiert. Bitte nicht manuell bearbeiten.**\n")
    
    md_lines.append("## 📋 Übersicht\n")
    md_lines.append("| ID | Datum | Titel | Status | Entscheidung |")
    md_lines.append("| :--- | :--- | :--- | :--- | :--- |")
    
    for adr in adrs:
        id_str = adr.get('id', 'N/A')
        date_str = adr.get('date', 'N/A')
        title_str = adr.get('title', 'N/A')
        status_str = adr.get('status', 'N/A')
        decision_str = adr.get('decision', 'N/A')
        
        if status_str.lower() == 'offen':
            status_str = f"🟡 {status_str}"
        elif status_str.lower() in ['akzeptiert', 'geschlossen', 'entschieden']:
            status_str = f"🟢 {status_str}"
            
        md_lines.append(f"| **{id_str}** | {date_str} | {title_str} | {status_str} | {decision_str} |")
        
    md_lines.append("\n---\n")
    
    md_lines.append("## 📖 Detail-Protokolle\n")
    
    for adr in adrs:
        md_lines.append(f"### {adr.get('id', '')}: {adr.get('title', '')}")
        md_lines.append(f"**Status:** {adr.get('status', '')} | **Datum:** {adr.get('date', '')}\n")
        
        md_lines.append("#### Kontext")
        md_lines.append(f"{adr.get('context', 'Kein Kontext angegeben.')}\n")
        
        md_lines.append("#### Entscheidung")
        md_lines.append(f"> **{adr.get('decision', 'Ausstehend')}**\n")
        
        md_lines.append("#### Begründung (Rationale)")
        md_lines.append(f"{adr.get('rationale', 'Keine Begründung angegeben.')}\n")
        
        if 'consequences' in adr:
            md_lines.append("#### Konsequenzen")
            for cons in adr['consequences']:
                md_lines.append(f"- {cons}")
            md_lines.append("\n")
            
        md_lines.append("---\n")

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
        
    print(f"🚀 README.md erfolgreich im Ordner {adr_folder} generiert!")

if __name__ == '__main__':
    generate_adr_readme()
