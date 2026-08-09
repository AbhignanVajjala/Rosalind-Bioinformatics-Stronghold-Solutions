
'''
Solution for question 18 of Rosalind Bioinformatics stronghold
Title: Open Reading Frames
Given: A DNA string s in FASTA format.
'''

'''
Expected Output:
Every distinct candidate protein string that can be translated from ORFs of s
'''

#MAIN LOGIC

fasta=""">Rosalind_6383
GATTGTTACCCTACGATCTTCGAACCATAACCGTATGGAAAATATTAAGGTCAAGCTAAT
GATACTTGGTGAATCGTTGCATAGAAACGGCGCAATGATTCATCCGGCTGTGCCATGAAA
ACCATAAAATCGTGTCGTGCCTTGCCTTACTTCATACAAGGCAGACCCTTTTGGCCCGCA
TGACCATTTCACATGACTAGGTTCGGGACGCCAGTACATTTTCAATCGTATGAAGGGCAG
TTCTTAAATACCAAGCCATATGTAGCCCACACTTGTCCGGGCCGCAAATACTGATCCCAT
GAATACCCCCCCGATCGGGCAATGGTTTGTACGGCCTTGCAATTCTTTTACCTTTTCGTG
GAATATAGTGCCTCATTGCACGGGACCGACGTATTGACCCGCCCGCGGCCTTGGCATATA
GCGGATTTACGGCGTAAAAGTAATGTGTAGTTAGAGAGACTGATTGTAGCTACAATCAGT
CTCTCTAACTACACATCATAGACCTTACGGATCAGTTGTAATTCTAACTGCGATAAAGCC
GGGTCGCTACCTTAACAGCTGGGTTAGCCGTTAGATACGATACAATAACGACCCTCCAAC
GGCGGCCCCTGTTCTGCCAGAGGCTCTACAGAAGGCGGTCACCCTCTCGGGGTGGAGACG
GACAGCGTCAGTGCGGGGCTTATGAAGGGCGCAACAACCCTTTGCGAACCAACACCAAAG
CCGTAATTGGACCCGGTAATATCGCCTGGTGTTCAGCCATTACAGTTGGCCTGAGCTACA
CTTTTGCTCGTGGATTGATATGGAGAAGAACGCGACGACCCTCATCCGCTGCGCTTGGTG
GTTTACCGAGGTGGACAAACTCAACCTTGGACCAGCCGTCTGCTCCACCGGTTCTGTAGT
TGGAAAGCGTATATTCCTAGAACGTCTGCAGCAAAGTT
"""

#Assigning dna str from the fasta
dna_str=""
for line in fasta.splitlines():
  if line.startswith(">"):
    continue
  else:
    dna_str +=line

#Making the reverse complimentary dna

dna="ATCG"
comp="TAGC"
comp=str.maketrans(dna,comp)
rev_comp=dna_str.translate(comp)[::-1]

#Finding instances of ATG in the given DNA string

start="ATG"
start_ind=0
locations=[]


while True:

  location=dna_str.find(start,start_ind)
  if location== -1:
    break
  locations.append(location)
  start_ind=location+1

#Finding instances of ATG in the reverse compliment string of the given DNA string

start_1="ATG"
start_ind_1=0
locations_1=[]

while True:

  location=rev_comp.find(start_1,start_ind_1)
  if location== -1:
    break
  locations_1.append(location)
  start_ind_1=location+1

#A dictionary with codons and their respective proteins

dna_codon_table = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': 'Stop', 'TAG': 'Stop',
    'TGT': 'C', 'TGC': 'C', 'TGA': 'Stop', 'TGG': 'W',

    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',

    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',

    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

#FOR MAIN STRAND

final_proteins=set() #To avoid duplicates

for x in locations:
  protein=""

  for i in range(x,len(dna_str),3):
    codon=dna_str[i:i+3]

    if len(codon)<3:
      break

    symbol=dna_codon_table[codon]

    if symbol=="Stop":
      final_proteins.add(protein)
      break

    protein +=symbol






#FOR REVERSE COMPLIMENTARY STRAND


for x in locations_1:
  protein=""

  for i in range(x,len(rev_comp),3):
    codon=rev_comp[i:i+3]

    if len(codon)<3:
      break

    symbol=dna_codon_table[codon]

    if symbol=="Stop":
      final_proteins.add(protein)
      break

    protein +=symbol


for x in final_proteins:
  print(x)

'''
Output:
MQRFTKYH
MILGESLHRNGAMIHPAVP
MRVVAFFSISIHEQKCSSGQL
M
MVRRS
MNHCAVSMQRFTKYH
MAQPDESLRRFYATIHQVSLA
MK
MAWYLRTALHTIENVLASRT
MVMRAKRVCLV
MKGATTLCEPTPKP
MVFMAQPDESLRRFYATIHQVSLA
MKTIKSCRALPYFIQGRPFWPA
MAEHQAILPGPITALVLVRKGLLRPS
MCS
MYWRPEPSHVKWSCGPKGSALYEVRQGTTRFYGFHGTAG
MTISHD
MNTPPIGQWFVRPCNSFTFSWNIVPHCTGPTY
MENIKVKLMILGESLHRNGAMIHPAVP
MMCS
MVCTALQFFYLFVEYSASLHGTDVLTRPRPWHIADLRRKSNV
MIHPAVP
MGSVFAARTSVGYIWLGI
MPRPRAGQYVGPVQ
MRHYIPRKGKRIARPYKPLPDRGGIHGISICGPDKCGLHMAWYLRTALHTIENVLASRT
MKGSS
MRAKRVCLV
MTRFGTPVHFQSYEGQFLNTKPYVAHTCPGRKY
'''

