'''
Solution for question 11 of Rosalind Bioinformatics stronghold
Title: Mortal Fibonacci Rabbits
Given: Positive integers n<=100 and m<=20
'''
#Each pair of rabbits reaches maturity in one month and produces a single pair of offspring
#Rabbits live for the given 'm' months

n=94 #number of months
m=18 #months of rabbit lifespan

'''
1. Starts with 1 baby pair in the first month
2. They become adults
3. They reproduce
4. They die at after 'm' months

The main logic from this is:

" F[n]=F[n-1]+F[n-2]-F[n-(m+1)] "

Expected Output:
The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months
'''

F =[0]*(n+1)
F[1]=1
F[2]=1

for i in range(3,n+1):
  if i<=m:
    F[i]=F[i-1]+F[i-2] #Before any rabbits die
  elif i==m+1:
    F[i]=F[i-1]+F[i-2]-1 #The exact month the 'original' rabbit pair dies
  else:
    F[i]=F[i-1]+F[i-2]-F[i-(m+1)] #The after months
print(F[n])

#Output: 19621631195557366770

