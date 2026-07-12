'''
Solution for question 4 of Rosalind Bioinformatics stronghold
Title: Rabbits and Recurrence Relations
'''
n=32 #number of months
k=3 #pairs of rabbits produced in one generation
F =[0]*(n+1)
F[1]=1
F[2]=1
'''
MONTH 1: Starts from 1 pair of children
MONTH 2: The pair become adults and reproduce 3 baby pairs.... and so on
#The main logic is F(n)=F(n-1)+(k*(F(n-2)))
'''
#Expected output:The total number of rabbit pairs that will be present
for i in range(3,n+1):
  F[i]=F[i-1]+(k*(F[i-2]))
print(F[n])
#Output: 108412748857