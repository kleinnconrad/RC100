import yaml
import glob
import os

def build_full_spec(output_file='full_spec.yaml'):
    merged_data = {}
    
    # Wir suchen explizit nach .yaml und .yml Dateien in allen Unterordnern
    # Das Muster '**/spec_*.y*ml' deckt spec_akku.yaml ab, egal wo sie liegt
    search_pattern = os.path.join('**', 'spec_*.y*ml')
    
    # recursive=True sucht in Unterordnern
    # we_ignore_case=True hilft, falls Dateiendungen groß geschrieben sind
    files = sorted(glob.glob(search_pattern, recursive=True))
    
    print(f"DEBUG: Suche gestartet im Verzeichnis: {os.getcwd()}")
    print(f"DEBUG: Suchmuster: {search_pattern}")
    print(f"DEBUG: Gefundene Dateien: {files}")

    if not files:
        print("❌ Keine Spezifikations-Dateien gefunden. Prüfe die Ordnerstruktur!")
        # Wir listen zur Sicherheit alle Dateien auf, um zu sehen, was der Bot sieht
        all_files = [f for f in glob.glob('**/*', recursive=True)]
        print(f"DEBUG: Sichtbare Dateien im Repo: {all_files}")
        return

    for file in files:
        # Verhindern, dass die Output-Datei selbst eingelesen wird
        if os.path.basename(file) == output_file:
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            try:
                data = yaml.safe_load(f)
                if data:
                    merged_data.update(data)
                    print(f"✅ {file} wurde hinzugefügt.")
            except Exception as e:
                print(f"⚠️ Fehler beim Lesen von {file}: {e}")

    # Die Datei wird im aktuellen Hauptverzeichnis erstellt
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(
            merged_data, 
            f, 
            default_flow_style=False, 
            sort_keys=False, 
            allow_unicode=True
        )
        
    print(f"🚀 Erfolg! '{output_file}' mit {len(merged_data)} Hauptsektionen erstellt.")

if __name__ == '__main__':
    build_full_spec()