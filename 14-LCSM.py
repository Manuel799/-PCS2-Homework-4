Sequences=open("rosalind_lcsm.txt","r")
seqs=Sequences.readlines()
seq=("".join([i.rstrip("\n") for i in seqs])).split(">")[1:]
start=11
seq=[i[start:] for i in seq]
TFlist=[False]*len(seq)
motiflist=[]
n=len(seq[0])
def motifs(seq):
      for k in range(1,n)[::-1]:
            for i in range(n-k):
                  TFlist=[True for j in seq[1:] if seq[0][i:i+k+1] in j]
                  if sum(TFlist)==len(seq)-1:
                        return seq[0][i:i+k+1]
print (motifs(seq))
