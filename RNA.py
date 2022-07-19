"""
Problem Title: Counting DNA Nucleotides
Rosalind ID: RNA
Rosalind #: 002

"""

with open(
    "/Users/rayanhg/Desktop/python/Intro to Python/Rosalind/rosalind_rna (2).txt"
) as file:

    dna = file.read()


rna = " "


for base in dna:
    ''' replaces nucleotide T with U'''
    if base == "T":
       
        rna += "U"
    else:
        
        rna += base

print(rna)
