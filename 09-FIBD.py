with open('rosalind_fibd.txt') as input_data:
    n,m = map(int, input_data.read().split())
Rabbits = [1]+[0]*(m-1)
for year in range(1, n):
    Bunnies = 0
    for j in range(1,m):
        Bunnies += Rabbits[(year-j-1)%m]
    Rabbits[(year)%m] = Bunnies
Total_Rabbits = sum(Rabbits)
print (Total_Rabbits)
