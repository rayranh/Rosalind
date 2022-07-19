'''
Problem Title:Conditions and Loops
Rosalind ID:INI4
Rosalind #:004
URL: https://rosalind.info/problems/ini4/
'''
a = 4545
b = 9171
result = 0  
for i in range(a,b+1): 
    if i%2 == 1:
           result += i
        
print (result)
