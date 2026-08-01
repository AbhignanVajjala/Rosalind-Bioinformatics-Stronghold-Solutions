
'''
Solution for question 13 of Rosalind Bioinformatics stronghold
Title: Calculating Expected Offspring
Given:
Six non-negative integers. The integers correspond to the number of couples
in a population possessing each genotype pairing for a given factor.
In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
'''

'''
From a Punnett square, the probability of dominant offspring of each pair

1. 1
2. 1
3. 1
4. 0.75
5. 0.5
6. 0
'''

'''
Expected Output:
The expected number of offspring displaying the dominant phenotype in the next
generation, under the assumption that every couple has exactly two offsprings.
'''

'''
Probabilty of dominant offspring from each pair under
the assumption that every couple has exactly two offsprings:

1. 2
2. 2
3. 2
4. 1.5
5. 1
6. 0
'''

#The actual solution


from re import split

population=list(map(int,input().split()))

p1=population[0]*2
p2=population[1]*2
p3=population[2]*2
p4=population[3]*1.5
p5=population[4]*1
p6=population[5]*0

num=sum([p1,p2,p3,p4,p5,p6])

print(num)

#Input: 17551 16813 19121 16860 17995 18935

#Output: 150255.0

