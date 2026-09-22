'''
Write an optimized program to check
whether the given number is a prime
number or NOT.
'''

def check_prime(n):
    if n<=1:
        return False
    
    for i in range(2, n):
        if n%i==0:
            return False

    return True

n = int(input("Enter a number: "))
isPrime = check_prime(n)
if isPrime:
    print(n," is a prime number")
else:
    print(n," is not a prime number")
