'''
Problem Title:Rabbits and Recurrence Relations
Rosalind ID:FIB
Rosalind #:004
URL:https://rosalind.info/problems/fib/
'''
gen = 29
fib = [0, 1]
litter = 4
for i in range(gen - 1):
   
    fib.append((fib[-2]) * litter + fib[-1])

print(fib)


