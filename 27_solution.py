
'''
Solution for question 27 of Rosalind Bioinformatics stronghold
Title: Partial Permutations
Given:  Positive integers n and k
in range 100≥n>0 and 10≥k>0

'''

'''
Expected Output:
The total number of partial permutations (n,k) modulo 1,000,000
'''

#MAIN LOGIC

n=96

k=8


import math

t_perm=math.perm(n,k) %1000000

print(t_perm)


#Output: 828800

