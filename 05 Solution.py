''' 
Solution for question 5 of Rosalind Bioinformatics stronghold
Title: Computing GC Content
Given data:

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

'''
data={"Rosalind_6404":"CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG",
"Rosalind_5959": "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC",
"Rosalind_0808":"CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"}
'''
Expected Output:
The ID of the string having the highest GC-content,
followed by the GC-content of that string. #In a new line
#Rosalind allows for a default error of 0.001
'''
x=data.get("Rosalind_6404")
y=data.get("Rosalind_5959")
z=data.get("Rosalind_0808")

g1=x.count("G")
c1=x.count("C")
gc1=g1+c1
gc1_p=(gc1/len(x)*100)

g2=y.count("G")
c2=y.count("C")
gc2=g2+c2
gc2_p=(gc2/len(y)*100)

g3=z.count("G")
c3=z.count("C")
gc3=g3+c3
gc3_p=(gc3/len(z)*100)

#Highest GC content percentage
highest_gcp=max(gc1_p,gc2_p,gc3_p)
if highest_gcp==gc1_p:
  print("Rosalind_6404")
  print(gc1_p)
elif highest_gcp==gc2_p:
  print("Rosalind_5959")
  print(gc2_p)
elif highest_gcp==gc3_p:
  print("Rosalind_0808")
  print(gc3_p)
#Output:
'''
Rosalind_0808
60.91954022988506
'''
