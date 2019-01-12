from itertools import permutations
from math import factorial
f = open("rosalind_perm.txt", 'r')

n =  f.readline()
n= int(n)
seq = range(1, n+1)


print(factorial(n))

for perm in permutations(seq):
    print (" ".join(map(str, perm)))
