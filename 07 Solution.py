'''
Solution for question 7 of Rosalind Bioinformatics stronghold
Title: Mendel's First Law
Given Information:
Three positive integers k,m,and n,representing a population containing (k+m+n)organisms:
k-individuals are homozygous dominant for a factor,
m-idnuviduals are heterozygous factor,
n-induviduals are homozygous recessive.

Expected Output:
The probability that two randomly selected mating organisms will produce
an individual possessing a dominant allele (and thus displaying the dominant phenotype).

Mating pool:
|k x k , k x m , k x n |
|m x k , m x m , m x n |
|n x k , n x m , n x n |

#In the mating pool taking the matches which get recessive genes:
m x m , m x n , n x m , n x n
#In these matches the probability to get recessive genes:
1/4 , 1/2 , 1/2 , 1
'''
#Given values
k=26
m=28
n=24
T=k+m+n
#Calculation
re_prob=((1/4)*((m/T)*((m-1)/(T-1)))+(1/2)*((m/T)*((n)/(T-1)))+(1/2)*((n/T)*((m)/(T-1)))+(1)*((n/T)*((n-1)/(T-1))))
#To get the expected dominant allele manifestation probability
dom_prob=1-(re_prob)
print(dom_prob)
#Output: 0.7647352647352648