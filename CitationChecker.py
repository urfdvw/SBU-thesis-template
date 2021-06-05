import os

# get the citations in the .tex files

# acquire the path of all files
tex_paths = []
for path, subdirs, files in os.walk('.'):
    for name in files:
        if name[-4:] == '.tex':
            tex_paths.append(os.path.join(path, name))
# acquire all mentioned ciation identifiers
cites = []
for path in tex_paths:
    file = open(path)
    text = file.read()
    pieces = text.split('\cite{')[1:] # ignore the first piece
    for p in pieces:
        cites += [s.strip() for s in p[:p.index('}')].split(',')]

        
# acquire all citations in .bib file
file = open('main.bib', encoding="utf-8")
text = file.read()
pieces = text.split('@')[1:] # ignore the first piece
papers = [p[p.index('{')+1 : p.index(',')].strip() for p in pieces]

# count
counts = dict()
for p in papers:
    counts[p] = 0
    
for c in cites:
    if c: # avoid empty strings
        counts[c] += 1
    
counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])} # sort by counts
# https://stackoverflow.com/a/613218/7037749

# output
out = open('CitationCounts.csv', 'w')
# count citations in tex, for double check
out.write('total' + ',' + str(sum([1 for k, v in counts.items() if v > 0])) + '/' + str(len(counts)) + '\n') 

for paper in counts:
    out.write(paper + ',' + str(counts[paper]) + '\n')
    