# WAP to print a number is a prime number
# or not.

n = int(input("Enter a number: "))

if n<=1:
    print(n,' is not a prime number')
else:
    isprime = True
    i=2
    while i<n:
        if n%i==0:
            isprime = False
            break
        i+=1
    if isprime :
        print(n, ' is a prime number')
    else:
        print(n, ' is not a prime number')
