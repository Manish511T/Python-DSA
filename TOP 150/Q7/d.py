'''
d) Store first 100 prime numbers in a list/array.'''

def check_prime(n):
    if n<=1:
        return False
    
    for i in range(2, n):
        if n%i==0:
            return False

    return True

n=2
primes = []

while len(primes)<100:
    if check_prime(n):
        primes.append(n)
    n+=1

print(primes)