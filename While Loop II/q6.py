'''
You are given positive integers n and m.

Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.
'''

n=10
m = 3
num1 = 0
num2 = 0
i = 1
while i<=n:
    if i%m !=0:
        num1 +=i
    elif i%m ==0:
        num2 +=i
    i+=1

print(num1-num2)