with open("rosalind_cons.txt","r") as f:
    Rosalind={}
    Sequences=f.readline().strip()
    while Sequences!='':
        name="".join(list(Sequences)[1:len(Sequences)])
        Sequences=f.readline().strip()
        while Sequences!='' and Sequences[0]!=">":
            if name not in Rosalind:
                Rosalind[name]=Sequences
            else:
                Rosalind[name]+=Sequences
            Sequences=f.readline().strip()

length=len(list(Rosalind.values())[0])
profile=[[0]*(length+1) for i in range(4)]

profile[0][0]="A:"
profile[1][0]="C:"
profile[2][0]="G:"
profile[3][0]="T:"

for x in Rosalind:
    for i in range(len(Rosalind[x])):
        if Rosalind[x][i]=="A":
            profile[0][i+1]+=1
        else:
            if Rosalind[x][i]=="C":
                profile[1][i+1]+=1
            else:
                if Rosalind[x][i]=="G":
                    profile[2][i+1]+=1
                else:
                    profile[3][i+1]+=1

consString=''
for i in range(length):
    a=[profile[j][i+1] for j in range(4)]
    m=max(a)
    maxs=[j for j, k in enumerate(a) if k==m]
    if maxs[0]==0:
        consString+="A"
    else:
        if maxs[0]==1:
            consString+="C"
        else:
            if maxs[0]==2:
                consString+="G"
            else:
                consString+="T"

print(consString)

for i in range(4):
    print(' '.join(map(str, profile[i])))
