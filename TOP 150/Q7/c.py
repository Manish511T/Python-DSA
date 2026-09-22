'''
c) Print nth prime number.
'''
def check_prime(n):
    if n<=1:
        return False
    
    for i in range(2, n):
        if n%i==0:
            return False

    return True


n = int(input("Enter a number: "))

for i in range(1, n):
    if check_prime(i):
        print(i)

