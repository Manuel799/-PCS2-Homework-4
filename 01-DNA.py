with open('rosalind_dna.txt') as Data_DNA:
	dna = Data_DNA.read()

c_nucleotides = []
for nuc in ['A', 'C', 'G', 'T']:
	c_nucleotides.append(str(dna.count(nuc)))

print (' '.join(c_nucleotides))

