'''
Problem Title: Working with Files
Rosalind ID:INI5
Rosalind #:005
URL:https://rosalind.info/problems/ini5/
'''

i = 1
# Opening the file
f = open("Data/rosalind_ini5.txt","r")

for line in f.readlines():
    if i % 2 == 0:
        print(line)
        i += 1

        f.close()
