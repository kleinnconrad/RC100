import os
import shutil
import re
from pathlib import Path

def find_latest_setup_sheet(setup_dir: Path) -> Path | None:
    """Finds the setup sheet with the highest number in its filename."""
    highest_num = -1
    latest_file = None

    if not setup_dir.exists():
        print(f"Directory {setup_dir} does not exist.")
        return None

    # Pattern to match filenames like "1_setup_sheet.yaml"
    pattern = re.compile(r"^(\d+)_setup_sheet\.ya?ml$")

    for file_path in setup_dir.iterdir():
        if file_path.is_file():
            match = pattern.match(file_path.name)
            if match:
                num = int(match.group(1))
                if num > highest_num:
                    highest_num = num
                    latest_file = file_path

    return latest_file

import yaml
import json

def main():
    root_dir = Path(__file__).parent.parent
    setup_dir = root_dir / "setup_sheets"
    docs_dir = root_dir / "docs"

    latest_file = find_latest_setup_sheet(setup_dir)

    if latest_file:
        print(f"Found latest setup sheet: {latest_file.name}")
        
        # Ensure docs directory exists
        docs_dir.mkdir(parents=True, exist_ok=True)
        
        target_path = docs_dir / "latest_setup.json"
        
        # Parse YAML and convert to JSON
        with open(latest_file, 'r') as f:
            data = yaml.safe_load(f)
            
        with open(target_path, 'w') as f:
            json.dump(data, f)
            
        print(f"Converted to {target_path}")
    else:
        print("No setup sheets found.")
        exit(1)

if __name__ == "__main__":
    main()
