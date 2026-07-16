# WAP to print and count all the factors of a
# number.

# i/p: 28
# o/p: 1 2 4 7 14 28
# Total Factors are: 6

count=0
n = 28
i=1
while i<=28:
    if n%i==0:
        print(i, end=' ')
        count+=1
    i+=1
print(end='\n')
print('Total factors are: ', count)