import os, re, glob

exact_titles = set()
for d in ['wiki/sources', 'wiki/entities', 'wiki/concepts', 'wiki/synthesis']:
    for f in glob.glob(d + '/*.md'):
        with open(f, encoding='utf-8') as file:
            for line in file:
                if line.startswith('# '):
                    title = line[2:].strip()
                    exact_titles.add(title)
                    break

broken = []
for f in glob.glob('wiki/**/*.md', recursive=True):
    content = open(f, encoding='utf-8').read()
    links = set(re.findall(r'\[\[(.*?)\]\]', content))
    for link in links:
        if link not in exact_titles:
            broken.append(f"File: {f} | Broken Link: [[{link}]]")

print("Broken links:")
for b in broken:
    print(b)
