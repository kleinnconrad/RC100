import yaml
import os
import urllib.parse

def find_part_info(data):
    """Sucht rekursiv nach Marke, Modell und Artikelnummer in den YAML-Daten."""
    info = {'brand': '', 'model': '', 'part_number': ''}
    
    def search_dict(d):
        for k, v in d.items():
            if isinstance(v, dict):
                search_dict(v)
            elif isinstance(v, str):
                k_lower = str(k).lower()
                if k_lower in ['brand', 'hersteller', 'marke']:
                    info['brand'] = v
                elif k_lower in ['model', 'modell', 'name']:
                    info['model'] = v
                elif k_lower in ['part_number', 'artikelnummer', 'part number']:
                    info['part_number'] = v

    if isinstance(data, dict):
        search_dict(data)
    return info

def generate_shopping_list():
    input_file = 'full_spec.yaml'
    
    # NEU: Der neue Zielpfad
    output_file = 'projekt/kosten/shopping_list.md'

    if not os.path.exists(input_file):
        print(f"❌ {input_file} nicht gefunden. Bitte zuerst specs mergen.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
        except Exception as e:
            print(f"⚠️ Fehler beim Parsen der YAML: {e}")
            return

    if not data or not isinstance(data, dict):
        return

    md_lines = []
    md_lines.append("# 🛒 RC100 Einkaufsliste (Shopping List)\n")
    md_lines.append("> **Automatischer Build:** Diese Liste wird live aus deiner Architektur generiert. Klicke auf die Shop-Links, um den aktuell besten Preis zu finden.\n")
    md_lines.append("| Kategorie | Bauteil | Artikelnummer | Status | Preis-Check |")
    md_lines.append("| :--- | :--- | :--- | :--- | :--- |")

    for category, content in data.items():
        info = find_part_info(content)
        
        if not info['brand'] and not info['model']:
            continue 
            
        bauteil_name = f"{info['brand']} {info['model']}".strip()
        part_number = info['part_number'] if info['part_number'] else "-"
        
        search_term = f"{bauteil_name} {part_number}".replace("-", "").strip()
        query_encoded = urllib.parse.quote_plus(search_term)
        
        google_link = f"[🔍 Google Shopping](https://www.google.com/search?tbm=shop&q={query_encoded})"
        berlinski_link = f"[🛒 Berlinski](https://www.modellbau-berlinski.de/katalog/artikelinfo/x/x/x?q={query_encoded})"
        ruddog_link = f"[🛒 Ruddog](https://www.ruddog.eu/Search?ke={query_encoded})"
        
        links = f"{google_link}<br>{berlinski_link}<br>{ruddog_link}"
        
        md_lines.append(f"| **{category}** | {bauteil_name} | `{part_number}` | [ ] Offen | {links} |")

    # NEU: Erstellt den Ordner 'projekt/kosten', falls er nicht existiert
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
        
    print(f"🚀 Erfolg! '{output_file}' wurde generiert.")

if __name__ == '__main__':
    generate_shopping_list()