input_file = 'rosalind_subs.txt'

with open(input_file) as file:
    dna1 = file.readline().strip()
    dna2 = file.readline().strip()
i = dna1.find(dna2)
while i != -1:
    print (i + 1)
    i = dna1.find(dna2, i + 1)
