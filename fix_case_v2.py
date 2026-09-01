import os
import glob
import re

known_names = {
    'Carten', 'Bauhaus', 'Metro', 'Hornbach', 'Loctite', 
    'Creative', 'Commons', 'Mit', 'Gyros', 'Gyro', 'Macpherson'
}

def process_text(text):
    result = ""
    i = 0
    while i < len(text):
        if text[i:i+3] == '```':
            pass
        if text[i] == '`':
            # Skip inline code
            end = text.find('`', i+1)
            if end == -1: end = len(text)
            else: end += 1
            result += text[i:end]
            i = end
            continue
        if text[i] == ']' and i+1 < len(text) and text[i+1] == '(':
            # Skip link url
            end = text.find(')', i+1)
            if end == -1: end = len(text)
            else: end += 1
            result += text[i:end]
            i = end
            continue
            
        # Match a title case word with word boundaries
        m = re.match(r'([A-Z][a-z]+)\b', text[i:])
        if m:
            # Check if there is a word boundary before it. 
            # If not, it means we are inside a word like GitHub, skip it.
            if i > 0 and text[i-1].isalpha():
                result += text[i]
                i += 1
                continue
                
            word = m.group(1)
            if word in known_names:
                result += word
                i += len(word)
                continue
                
            prefix = result
            # Replace [L] and [M] with a period so they act as sentence boundaries
            prefix_mod = re.sub(r'\[[LM]\]', '.', prefix)
            # Also replace <br> with a period
            prefix_mod = re.sub(r'<br>', '.', prefix_mod, flags=re.IGNORECASE)
            
            # Check if prefix_mod ends with a sentence boundary (ignoring trailing spaces and markdown symbols)
            # Boundary characters: . ! ? :
            is_boundary = False
            
            # Remove trailing space and markdown syntax
            trailing_symbols_pattern = r'[\*\#\-\|\>\"\'\(\[\s\]]*$'
            clean_prefix = re.sub(trailing_symbols_pattern, '', prefix_mod)
            
            if len(clean_prefix) == 0:
                is_boundary = True
            elif clean_prefix.endswith('.') or clean_prefix.endswith('!') or clean_prefix.endswith('?') or clean_prefix.endswith(':'):
                is_boundary = True
            elif clean_prefix.lower().endswith('<br>'):
                is_boundary = True
                
            if is_boundary:
                result += word
            else:
                result += word.lower()
                
            i += len(word)
            continue
            
        result += text[i]
        i += 1
        
    return result

def process_file(filepath):
    if '.agents' in filepath: return
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    in_code_block = False
    in_frontmatter = False
    for i, line in enumerate(lines):
        if line.strip() == '---' and i == 0:
            in_frontmatter = True
            new_lines.append(line)
            continue
        if in_frontmatter and line.strip() == '---':
            in_frontmatter = False
            new_lines.append(line)
            continue
        if in_frontmatter:
            new_lines.append(line)
            continue
            
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
            
        if in_code_block:
            new_lines.append(line)
            continue
            
        new_line = process_text(line)
        new_lines.append(new_line)
        
    if lines != new_lines:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated {filepath}")

files = glob.glob('**/*.md', recursive=True)
for f in files:
    process_file(f)
