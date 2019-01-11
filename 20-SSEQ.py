def Sequence(source, sequence):
    x = y = 0
    pos = []

    while x < len(source) and y < len(sequence):
        if source[x] == sequence[y]:
            y += 1
            pos.append(x + 1)

        x += 1
    return pos


f = open("rosalind_sseq.txt", "r")

DnaSeqs = {}
cKey = ''
keys = []
for s in f:
    if '>' in s:
        key = s.rstrip().replace('>', '')
        cKey = key
        keys.append(key)
        DnaSeqs[cKey] = ''
    else:
        DnaSeqs[cKey] += s.rstrip()

indices = Sequence(DnaSeqs[keys[0]], DnaSeqs[keys[1]])
print (' '.join(map(str, indices)))
