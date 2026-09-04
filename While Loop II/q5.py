'''
Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.
'''
n = int(input("Enter a number: "))
sum = 0
i = 1
while i<=n:
    if i%3 == 0 or i%5==0 or i%7==0 :
        sum +=i
    i+=1

print(sum)