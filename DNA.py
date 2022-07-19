'''
Problem Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind # : 001
URL: https://rosalind.info/problems/dna/
'''


from ast import With


with open(
    "/Users/rayanhg/Desktop/python/Intro to Python/Rosalind/rosalind_dna.txt"
) as file:

    dna = file.read()

# starting a count 
count_a = 0
count_g = 0
count_c = 0
count_t = 0

for base in dna: 
    if base == "A":
        count_a += 1
    elif base == "T":
        count_t += 1
    elif base == "G":
        count_g += 1
    elif base == "C":
        count_c += 1

print(count_a, count_c, count_g, count_t, sep=" ")
