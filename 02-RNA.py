with open('rosalind_rna.txt') as Data_RNA:
	dna = Data_RNA.read().strip()

with open('rosalind_rna.txt', 'w') as RNA:
	RNA.write(dna.replace('T', 'U'))
	print (dna.replace('T', 'U'))
