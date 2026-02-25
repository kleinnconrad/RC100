import yaml
import glob
import os

def merge_specs():
    # Sucht alle spec_*.yaml Dateien
    files = glob.glob('spec_*.yaml')
    merged_data = {}
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            try:
                data = yaml.safe_load(f)
                if data:
                    # Macht aus 'spec_brushless_combo.yaml' -> 'Brushless Combo'
                    clean_name = os.path.basename(file).replace('spec_', '').replace('.yaml', '').replace('_', ' ').title()
                    
                    # Packt den gesamten Inhalt der Datei unter diesen Namen
                    merged_data[clean_name] = data
            except Exception as e:
                print(f"Fehler beim Lesen von {file}: {e}")
                
    with open('full_spec.yaml', 'w', encoding='utf-8') as f:
        # sort_keys=False verhindert, dass das YAML-Modul die Reihenfolge im Block zerstört
        yaml.dump(merged_data, f, allow_unicode=True, sort_keys=False)
        
    print("🚀 full_spec.yaml erfolgreich generiert und sauber nach Komponenten gruppiert!")

if __name__ == '__main__':
    merge_specs()
