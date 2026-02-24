# Datei: yaml_to_md.py (muss ins Hauptverzeichnis!)
import yaml
import os

def format_data(data, depth=0):
    md = ""
    indent = "  " * depth
    if isinstance(data, dict):
        for key, value in data.items():
            formatted_key = str(key).replace('_', ' ').title()
            if isinstance(value, (dict, list)):
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
        for item in data:
            if isinstance(item, (dict, list)):
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
    if not data: return
    md_lines = ["# 🏎️ RC100 Gesamtspezifikation\n", "> Automatischer Build. Nicht manuell bearbeiten.\n", "---\n"]
    for section_key, section_data in data.items():
        md_lines.append(f"## ⚙️ {str(section_key).replace('_', ' ').upper()}\n")
        md_lines.append(format_data(section_data))
        md_lines.append("\n---\n")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
    print(f"🚀 {output_file} generiert.")

if __name__ == '__main__':
    generate_markdown()
