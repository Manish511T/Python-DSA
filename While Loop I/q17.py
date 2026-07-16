# WAP to count the factors of a number.

# i/p: 28
# o/p: Total Factors are: 6

count=0
n = 28
i=1
while i<=28:
    if n%i==0:
        count+=1
    i+=1
print('Count: ', count)