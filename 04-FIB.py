def Fibonacci(r,g):
    if r < 1:
        return 0
    elif r == 1:
        return 1
    elif r == 2:
        return 1
    else:
        return Fibonacci(r-1,g) + g*Fibonacci(r-2, g)

with open('rosalind_fib.txt') as Fib_rabbits:
	r,g = map(int, Fib_rabbits.read().split())

rabbits = str(Fibonacci(r,g))
print (rabbits)
