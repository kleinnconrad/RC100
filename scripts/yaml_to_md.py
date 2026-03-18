import yaml
import os

def format_data(data, depth=1):
    md = ""
    # Sorgt für die korrekte Einrückung der Listenpunkte
    indent = "  " * (depth - 2) if depth >= 2 else ""
    
    if isinstance(data, dict):
        for key, value in data.items():
            formatted_key = str(key).replace('_', ' ').title()
            
            if isinstance(value, dict):
                if depth == 1:
                    md += f"\n### {formatted_key}\n\n"
                    md += format_data(value, depth + 1)
                elif depth == 2:
                    md += f"\n#### 🔹 {formatted_key}\n\n"
                    md += format_data(value, depth + 1)
                else:
                    md += f"{indent}* **{formatted_key}:**\n"
                    md += format_data(value, depth + 1)
            elif isinstance(value, list):
                if depth == 1:
                    md += f"\n### {formatted_key}\n\n"
                    md += format_data(value, depth + 1)
                elif depth == 2:
                    md += f"\n#### 🔹 {formatted_key}\n\n"
                    md += format_data(value, depth + 1)
                else:
                    md += f"{indent}* **{formatted_key}:**\n"
                    md += format_data(value, depth + 1)
            else:
                if isinstance(value, str) and '\n' in value:
                    md += f"{indent}* **{formatted_key}:**\n"
                    for line in value.split('\n'):
                        if line.strip():
                            md += f"{indent}  > {line.strip()}\n"
                else:
                    md += f"{indent}* **{formatted_key}:** {value}\n"
                    
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, dict):
                md += f"{indent}* 🔸 **Item {i+1}:**\n"
                md += format_data(item, depth + 1)
            else:
                md += f"{indent}* {item}\n"
    return md

def generate_markdown():
    input_file = 'full_spec.yaml'
    output_file = 'full_spec.md'

    if not os.path.exists(input_file):
        print(f"❌ {input_file} nicht gefunden.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    if not data or not isinstance(data, dict):
        return

    md_lines = []
    md_lines.append("# RC100 Gesamtspezifikation (Full Spec)\n")
    md_lines.append("> **Automatischer Build:** Diese Datei wird aus den modularen Spezifikationen generiert.\n")
    md_lines.append("---\n")

    # Hauptkategorien (die Dateinamen, z.B. Akku, Chassis)
    for section_key, section_data in sorted(data.items()):
        title = str(section_key).replace('_', ' ').upper()
        md_lines.append(f"## {title}\n")
        md_lines.append(format_data(section_data, depth=1))
        md_lines.append("\n---\n")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
        
    print("full_spec.md erfolgreich mit schönen Unterüberschriften generiert!")

if __name__ == '__main__':
    generate_markdown()
