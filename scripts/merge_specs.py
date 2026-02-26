import yaml
import glob
import os

def merge_specs():
    # Das Zauberwort heißt "recursive=True" und "**/"
    # So sucht das Skript im Hauptverzeichnis UND in allen Unterordnern!
    files = glob.glob('**/spec_*.yaml', recursive=True)
    merged_data = {}
    
    if not files:
        print("⚠️ Warnung: Keine Dateien mit dem Muster 'spec_*.yaml' gefunden!")
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            try:
                data = yaml.safe_load(f)
                if data:
                    # Macht aus 'ordner/spec_brushless_combo.yaml' -> 'Brushless Combo'
                    clean_name = os.path.basename(file).replace('spec_', '').replace('.yaml', '').replace('_', ' ').title()
                    
                    merged_data[clean_name] = data
                    print(f"✅ {file} erfolgreich zu '{clean_name}' hinzugefügt.")
            except Exception as e:
                print(f"❌ Fehler beim Lesen von {file}: {e}")
                
    with open('full_spec.yaml', 'w', encoding='utf-8') as f:
        # sort_keys=False behält die saubere Reihenfolge der Blöcke bei
        yaml.dump(merged_data, f, allow_unicode=True, sort_keys=False)
        
    print(f"🚀 full_spec.yaml erfolgreich generiert! ({len(files)} Module zusammengeführt)")

if __name__ == '__main__':
    merge_specs()
