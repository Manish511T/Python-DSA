# WAP to print all the factors of a number.
# i/p: 28
# o/p: 1 2 4 7 14 28

n = 28
i=1
while i<=28:
    if n%i==0:
        print(i, end=' ')
    i+=1