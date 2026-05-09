import os, re, glob

# Map of title to slug
pages = {}
for d in ['wiki/sources', 'wiki/entities', 'wiki/concepts', 'wiki/synthesis']:
    for f in glob.glob(d + '/*.md'):
        slug = os.path.basename(f)[:-3]
        with open(f, encoding='utf-8') as file:
            for line in file:
                if line.startswith('# '):
                    title = line[2:].strip()
                    pages[title] = slug
                    pages[title.lower()] = slug
                    break

def fix_links(match):
    original_text = match.group(1)
    # If it's already aliased, ignore
    if '|' in original_text:
        return match.group(0)
    
    slug = pages.get(original_text) or pages.get(original_text.lower())
    if slug:
        if slug == original_text:
            return f"[[{slug}]]"
        else:
            return f"[[{slug}|{original_text}]]"
    
    # Try to slugify if not found
    computed_slug = re.sub(r'[^a-z0-9а-яё]+', '-', original_text.lower()).strip('-')
    if computed_slug != original_text:
        return f"[[{computed_slug}|{original_text}]]"
    return f"[[{computed_slug}]]"

files_changed = 0
for f in glob.glob('wiki/**/*.md', recursive=True):
    with open(f, encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(r'\[\[(.*?)\]\]', fix_links, content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        files_changed += 1
        print(f"Fixed links in {f}")

print(f"Total files updated: {files_changed}")
