DNA = open("rosalind_lcsq.txt", "r")
lcsq = []
seq = DNA.read()
seq = seq.replace("Rosalind_", "")
seq = seq.replace("\n", "")
seq = ''.join([i for i in seq if not i.isdigit()])
lcsq = seq.split(">")
lcsq.remove("")
x,y = lcsq
st = [''] * (len(y) + 1)
for a in x:
    yx = st
    st = ['']
    for j, k in enumerate(y):
        if(a == k):
            st.append(yx[j] + a)
        else:
            st.append(max(yx[j+1], st[-1], key=len))
print (st[-1])
