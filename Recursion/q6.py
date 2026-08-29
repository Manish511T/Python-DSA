'''
WAJP to print sum of squares of numbers from
1 to 100 by using recursion.
'''
def getSumOfSquare(n):
    if n==1:
        return 1

    return n**2 + getSumOfSquare(n-1)

print(getSumOfSquare(100))