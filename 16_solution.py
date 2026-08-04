'''
Solution for question 16 of Rosalind Bioinformatics stronghold
Title: Finding a Protein Motif
Given: UniProt Protein Database access IDs.
'''


All_IDs="""Q6A9W5
P98119_URT1_DESRO
P01044_KNH1_BOVIN
P01042_KNH_HUMAN
A5F5B4
Q8CE94
P00744_PRTZ_BOVIN
O82484
Q90X23
P07725_CD8A_RAT
Q83I57
"""
IDs=All_IDs.splitlines()

import urllib.request


#FASTA PARSING

data_dict={}
data=""

for x in IDs:
  clean_ID=x.split("_")[0]
  #url=f"http://www.uniprot.org/uniprot/{clean_ID}.fasta" is causing isssues
  url = f"https://rest.uniprot.org/uniprotkb/{clean_ID}.fasta"
  response=urllib.request.urlopen(url)
  whole_fasta=response.read().decode("utf-8")


  for line in whole_fasta.splitlines():
    if line.startswith(">"):
      ind_1=line.find("|")
      ind_2=line.find("|",ind_1+1)
      data=line[ind_1+1:ind_2]
      data_dict[data]=""
    else:
      data_dict[data]+=line

'''
Expected Output:
For each protein possessing the N-glycosylation motif, output its given access
ID followed by a list of locations in the protein string where the motif can be found.
'''

#N{P}[ST]{P} means N, anything except P, either S or T, anything except P

import re

N_g_motif=r"(?=(N[^P][ST][^P]))" #(?= ) to find overlapping motifs


for seq_name,seq in data_dict.items():
  motif_ind=re.finditer(N_g_motif,seq)

  locations=[]

  for match in motif_ind:
    locations.append(str(match.start()+1))

  if locations:
    for x in IDs:
      if seq_name in x:
        print(x)
        print(" ".join(locations))

'''
Output:
Q6A9W5
8 220 394
P98119_URT1_DESRO
153 398
P01044_KNH1_BOVIN
47 87 168 169 197 204
P01042_KNH_HUMAN
48 169 205 294
A5F5B4
68
Q8CE94
369
P00744_PRTZ_BOVIN
59 191 289
O82484
104 108 546 742 765
P07725_CD8A_RAT
63
'''

