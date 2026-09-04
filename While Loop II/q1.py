'''
WAJP to print sum of all natural numbers from 1 to 100.
'''

n = int(input("Enter a number: "))
i = 1
sum = 0
while i<=n:
    sum +=i
    i +=1

print(sum)