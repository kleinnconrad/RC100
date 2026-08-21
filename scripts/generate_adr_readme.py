import yaml
import glob
import os

def generate_adr_readme():
    adr_folder = 'architecture'
    readme_path = os.path.join(adr_folder, 'README.md')
    search_pattern = os.path.join(adr_folder, 'adr_*.y*ml')
    
    files = sorted(glob.glob(search_pattern))
    
    if not files:
        print(f"No ADR files found in folder '{adr_folder}'.")
        return

    adrs = []
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            try:
                data = yaml.safe_load(f)
                if data:
                    if 'adr' in data:
                        adr_content = data['adr']
                    else:
                        root_key = list(data.keys())[0]
                        adr_content = data[root_key]
                    adrs.append(adr_content)
            except Exception as e:
                print(f"Error reading {file}: {e}")

    adrs = sorted(adrs, key=lambda x: x.get('id', ''))

    md_lines = []
    md_lines.append("# Architecture Decision Records (ADRs)\n")
    md_lines.append("This directory contains all fundamental architecture and hardware decisions for the RC100 project. **This file is generated automatically. Please do not edit manually.**\n")
    
    md_lines.append("## Overview\n")
    md_lines.append("| ID | Date | Title | Status | Decision |")
    md_lines.append("| :--- | :--- | :--- | :--- | :--- |")
    
    for adr in adrs:
        id_str = adr.get('id', 'N/A')
        date_str = adr.get('date', 'N/A')
        title_str = adr.get('title', 'N/A')
        status_str = adr.get('status', 'N/A')
        decision_str = adr.get('decision', 'N/A')
        
        if status_str.lower() in ['open', 'offen']:
            status_str = f"🟡 {status_str}"
        elif status_str.lower() in ['accepted', 'closed', 'decided', 'akzeptiert', 'geschlossen', 'entschieden']:
            status_str = f"🟢 {status_str}"
            
        md_lines.append(f"| **{id_str}** | {date_str} | {title_str} | {status_str} | {decision_str} |")
        
    md_lines.append("\n---\n")
    
    md_lines.append("## Detailed Logs\n")
    
    for adr in adrs:
        md_lines.append(f"### {adr.get('id', '')}: {adr.get('title', '')}")
        md_lines.append(f"**Status:** {adr.get('status', '')} | **Date:** {adr.get('date', '')}\n")
        
        md_lines.append("#### Context")
        md_lines.append(f"{adr.get('context', 'No context provided.')}\n")
        
        md_lines.append("#### Decision")
        md_lines.append(f"> **{adr.get('decision', 'Pending')}**\n")
        
        md_lines.append("#### Rationale")
        md_lines.append(f"{adr.get('rationale', 'No rationale provided.')}\n")
        
        if 'consequences' in adr:
            md_lines.append("#### Consequences")
            for cons in adr['consequences']:
                md_lines.append(f"- {cons}")
            md_lines.append("\n")
            
        md_lines.append("---\n")

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
        
    print(f"SUCCESS: README.md successfully generated in folder {adr_folder}!")

if __name__ == '__main__':
    generate_adr_readme()
