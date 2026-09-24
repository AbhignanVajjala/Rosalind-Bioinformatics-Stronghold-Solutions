
'''
Solution for question 33 of Rosalind Bioinformatics stronghold
Title: Catalan Numbers and RNA Secondary Structures
Given: An RNA string s having the same number of occurrences of 'A' as 'U'
and the same number of occurrences of 'C' as 'G'.
'''


fasta=""">Rosalind_4340
ACCGGUCGACUUGGCGGCCGUACAUAUGCCAGCAGAUUGAUCCUUAAUACGCGGAGUAGA
UAUACUAGGCUGCCCUUCCCAUAUAUCGACGCGUUACGGCGGAGCUUAGAUAGCUAAUCU
ACAUAUGCGGGCCCAUGGUAGCUCGUUAAUCGACCGGUCGAGCGCAUGUACCGGAAUUGC
CAUUAUGCAGCGGUACUACCGACGCUUCGAUAAGGGCCCGGAUAUCAUCGCGCGCCGGGA
UCCCAGGCCGCUAGCUAUGCAUGGUAGCGGCCAUUAUGCGUAUACUAA
"""

rna_str=""

for line in fasta.splitlines():
  if line.startswith(">"):
    continue
  else:
    rna_str+=line

'''
Expected Output:
The total number of noncrossing perfect matchings of basepair edges
in the bonding graph of s, modulo 1000000
'''

#MAIN CODE

import sys

sys.setrecursionlimit(2000)

#So that the code will not crash

useful_strand={"":1}

def nc_mathchings(rna):
  if rna in useful_strand:
    return useful_strand[rna]

  if len(rna)%2 !=0:
    return 0  #Because if the specific rna has odd length, one is not paired

  pairs={"A":"U","U":"A","C":"G","G":"C"}

  total_comb=0

  first=rna[0]

  for m in range(1,len(rna),2):
    if rna[m]==pairs[first]:
      primary_piece=rna[1:m]
      secondary_piece=rna[m+1:]

      inside_comb=nc_mathchings(primary_piece)
      outside_comb=nc_mathchings(secondary_piece)
      total_comb+=((inside_comb)*(outside_comb))

  total_comb=total_comb % 1000000

  useful_strand[rna]=total_comb

  return total_comb


#To get the final answer

print(nc_mathchings(rna_str))

#Output:916160

