'''

Problem Title: Complementing a Strand of DNA
Rosalind ID:RECV
Rosalind #:003
URL: https://rosalind.info/problems/revc/

'''

with open(
    "/Users/rayanhg/Desktop/python/Intro to Python/Rosalind/rosalind_revc (1).txt"
) as file:
    dna = file.read().rstrip(
        "\n"
    )

# create a dictionary
comp = {"A": "T", "G": "C", "T": "A", "C": "G"}
# creating an empty string
comp_dna = " "
for base in dna:
    comp_dna += comp[base]
# printing in reverse
print(comp_dna[::-1])
