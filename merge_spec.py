import yaml
import glob
import os

def build_full_spec(output_file='full_spec.yaml', input_pattern='spec_*.yaml'):
    merged_data = {}
    
    # Alle passenden Dateien im Verzeichnis finden
    files = sorted(glob.glob(input_pattern))
    
    if not files:
        print("Keine Spezifikations-Dateien gefunden.")
        return

    for file in files:
        # Verhindern, dass sich das Skript selbst einliest, falls Muster abweicht
        if file == output_file:
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            try:
                # safe_load verhindert das Ausführen von schadhaftem Code im YAML
                data = yaml.safe_load(f)
                if data:
                    merged_data.update(data)
            except yaml.YAMLError as exc:
                print(f"Fehler beim Parsen von {file}: {exc}")

    # Das fertige Dictionary in die Master-Datei schreiben
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(
            merged_data, 
            f, 
            default_flow_style=False, 
            sort_keys=False, 
            allow_unicode=True # Wichtig für deutsche Umlaute!
        )
        
    print(f"Erfolgreich {len(files)} Dateien zu '{output_file}' gemergt.")

if __name__ == '__main__':
    build_full_spec()