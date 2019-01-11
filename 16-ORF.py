import re
DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def find_orf(sequence):
    start_position = 1
    start_indexs = []
    stop_indexs = []
    for i in range(1, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    for i in range(1, len(sequence), 3):
        stops = ["TAA", "TAA", "TGA"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    for i in range(0, len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                mark = stop_indexs[j] + 3
                break

    return orf

f = open('rosalind_orf.txt','r')
file = f.read()
seqcount = file.count('>')
print("Number of sequence = " + str(seqcount))

f = open('rosalind_orf.txt','r')
file = f.readlines()

sequences = []
seq = ""
for f in file:
    if not f.startswith('>'):
        f = f.replace(" ","")
        f = f.replace("\n","")
        seq = seq + f
    else:
        sequences.append(seq)
        seq = ""

sequences.append(seq)
sequences = sequences[1:]

lengths = [len(s) for s in sequences]
print("\nMax sequence length = " + str(max(lengths)))
print("Min sequence length = " + str(min(lengths)))

print("\nSequence Length Report:")
for j in range(seqcount):
    print("Length of sequence" + str(j) + " is " + str(lengths[j]))

n = 1
lengths = []
for s in sequences:
    orfs = find_orf(s)
    print("ORF")
    for j in orfs:
        print(j)
        print("==============")
        lengths.append(len(j))

print("\nLongest ORF is:" + str(max(lengths)))

