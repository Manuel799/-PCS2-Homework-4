def Searching(array, x):
   return Searching2(array, x, 0, len(array))

def Searching2(array, x, n, m):
   if n >= m:
      return -1

   elif n == m-1:
      if array[n] == x:
         return n+1

      else:
         return -1

   y = (n + m) // 2
   if array[y] > x:
      return Searching2(array, x, n, y)
   else:
      return Searching2(array, x, y, m)

if __name__ == '__main__':
    with open('rosalind_bins.txt') as inFile:
        n = int(inFile.readline())
        m = int(inFile.readline())
        array = list(map(int, inFile.readline().split()))
        ks = list(map(int, inFile.readline().split()))

        print(' '.join(map(str, [Searching(array, k) for k in ks])))

