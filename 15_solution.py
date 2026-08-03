
'''
Solution for question 15 of Rosalind Bioinformatics stronghold
Title: Independent Alleles
Given: Two positive integers k and N
'''

from re import split

k,N=list(map(int,input().split()))

'''
Tom, in the 0th generation has genotype Aa Bb. Tom has two children
in the 1st generation, each of whom has two children, and so on.

#Each organism always mates with an organism having genotype Aa Bb.

'''

'''
Expected Output:

The probability that at least N Aa Bb organisms will
belong to the k-th generation of Tom's family tree

# Don't count the Aa Bb mates at each level
'''

#From Punnett Square of AaBb x AaBb, the probablity of getting AaBb is 1/4

import math

total_org=2**k
AaBb_prob=0

for x in range(N,total_org+1):
  combin=math.comb(total_org,x)
  with_AaBb=math.pow(0.25,x)
  non_AaBb=math.pow(0.75,(total_org-x))

  prob=combin*with_AaBb*non_AaBb
  AaBb_prob +=prob

print(AaBb_prob)

#Input:5 7
#Output: 0.7221283346177969

