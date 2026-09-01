import os
import glob
import re

known_names = {'Carten', 'T410R', 'Bauhaus', 'Metro', 'Hornbach', 'Loctite', 'GitHub', 'Creative', 'Commons', 'Mit'}

def preserve_special(match):
    word = match.group(1)
    if word in known_names:
        return word
    return word.lower()

def process_text(text):
    # Split text into parts to avoid touching URLs or inline code
    # We will just parse out [...] and normal text, ignoring (...) if it follows ]
    # Actually, a simpler way is to find words to lowercase:
    # A word to lowercase is a Title Case word ([A-Z][a-z]+) that is NOT:
    # - At the start of a sentence
    # - In known_names
    
    # We can do this by splitting the line by sentence boundaries or just iterating over all Title Case words
    # and checking their preceding characters.
    
    # First, let's identify parts we should NOT modify:
    # - inline code: `...`
    # - link urls: ](...)
    # - html tags: <...>
    
    result = ""
    i = 0
    while i < len(text):
        if text[i:i+3] == '```':
            # This shouldn't happen inside a line, but just in case
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
            
        # Match a title case word
        m = re.match(r'([A-Z][a-z]+)', text[i:])
        if m:
            word = m.group(1)
            # Check if it's a known name
            if word in known_names:
                result += word
                i += len(word)
                continue
                
            # Check if it's the first word in a sentence.
            # Look backwards in 'result' to see if it's preceded only by non-alphanumeric (like #, *, -, |)
            # OR preceded by a sentence terminator (. : ! ?) and spaces.
            
            # Find the last non-space character before this word
            last_char = ''
            for c in reversed(result):
                if not c.isspace() and c not in ['*', '#', '-', '|', '>', '[', ']']:
                    last_char = c
                    break
                    
            if last_char in ['', '.', ':', '!', '?']:
                # It is the start of a sentence/heading, keep it capitalized
                result += word
            else:
                # Lowercase it
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
            
        # Process regular line
        new_line = process_text(line)
        new_lines.append(new_line)
        
    if lines != new_lines:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated {filepath}")

files = glob.glob('**/*.md', recursive=True)
for f in files:
    process_file(f)
