with open('rosalind_hamm.txt', 'r') as DnaStrands:
  Hamm_Distance = 0
  Strands = DnaStrands.read().split()
  FirstStrand = Strands[0]
  SecondStrand = Strands[1]
  for i in range(len(FirstStrand)):
    if FirstStrand[i] != SecondStrand[i]:
      Hamm_Distance += 1

  print (Hamm_Distance)
