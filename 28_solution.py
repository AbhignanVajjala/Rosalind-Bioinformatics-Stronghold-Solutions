
'''
Solution for question 28 of Rosalind Bioinformatics stronghold
Title: Modeling Random Genomes
Given: A DNA string s and an array A containing at most 20 numbers between 0 and 1.

'''
s="ATGTTTAGGGTGTCCGCAGCGCTTGGAATCAACTCCGTATGGCTTAAACCCACAGGAACACACCACACCTATGTGATTCCCCCGG"

#A=0.080 0.153 0.197 0.239 0.328 0.351 0.439 0.447 0.545 0.604 0.660 0.711 0.728 0.811 0.872 0.933

A=list(map(float,input().split()))


'''
Expected Output:
An array B having the same length as A in which B[k] represents the common logarithm
of the probability that a random string constructed with the GC-content found in A[k]
will match s exactly.
'''

#MAIN LOGIC

import math

B=[] #A list to store results

for x in A:
  G_prob=x/2

  C_prob=G_prob

  A_prob=(1-x)/2

  T_prob=A_prob




  total_log=0

  for y in s:
    if y=="A" or y=="T":
      l=math.log10(A_prob)
    elif y=="G" or y=="C":
      l=math.log10(G_prob)

    total_log+=l

  B.append(total_log)

print(*(round(b,3)for b in B))

'''
Output:
-76.397 -65.161 -61.148 -58.304 -54.278 -53.559 -51.718 -51.615 -51.129 -51.533 -52.449 -53.818 -54.409 -58.623 -63.976 -73.9
'''

