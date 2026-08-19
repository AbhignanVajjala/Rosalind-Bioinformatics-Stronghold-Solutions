
'''
Solution for question 26 of Rosalind Bioinformatics stronghold
Title: Perfect Matchings and RNA Secondary Structures
Given: An RNA string 's' having the same number of occurrences of 'A' as 'U'
and the same number of occurrences of 'C' as 'G'

'''

fasta=""">Rosalind_4381
CUUCCCAGACAAGUCACUUUUGUCUCGUAGCCGUCACGACGAACGGCAGAAUUGAGGCUG
AAAUGGGCUUUCGAUA"""

#s is the rna string

s=""

#Extraction of rna string from fasta

for line in fasta.splitlines():
  if line.startswith(">"):
    continue
  else:
    s+=line

'''
Expected Output:

The total possible number of perfect matchings of basepair edges in the bonding graph of s

'''


'''
From the given data:
1.Count of A = Count of U
2.Count of G = Count of C

#The required steps
1.Counting either A or U
2.Counting either G or C
3.Multiplying with the factorial of those respective counts
'''


#MAIN LOGIC

A_count=s.count("A") #counting A or U is the same, as they are equal here

G_count=s.count("G") #counting G or C is the same, as they are equal here

from math import factorial

A_fact=factorial(A_count)

G_fact=factorial(G_count)

m=(A_fact)*(G_fact)

print(m)

#Output: 14797530453474819213543604224000000

