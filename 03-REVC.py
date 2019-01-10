DNA = open('rosalind_revc.txt', 'r')
output = open('rosalind_revc_answer.txt', 'w')
line = DNA.readline().rstrip()
OppStrand = ''
Nuc = list(line)
for n in Nuc:
    if n == 'A':
        OppStrand += 'T'
    if n == 'T':
        OppStrand += 'A'
    if n == 'G':
        OppStrand += 'C'
    if n == 'C':
        OppStrand += 'G'

reversed_OppStrand = OppStrand[::-1]
print(reversed_OppStrand)
