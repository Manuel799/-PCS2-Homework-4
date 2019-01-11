from Bio import SeqIO
Strands = []
DNA = open('rosalind_tran.txt', 'r')
for record in SeqIO.parse(DNA, 'fasta'):
    Strands.append(str(record.seq))
DNA.close()
s1 = Strands[0]
s2 = Strands[1]

transition = 0
transversion = 0
AG = ['A', 'G']
CT = ['C', 'T']
for x, y in zip(s1, s2):
    if x != y:
        if x in AG and y in AG:
            transition += 1
        elif x in CT and y in CT:
            transition += 1
        else:
            transversion += 1
print('%0.11f' % (transition / transversion))
