'''
WAJP to print sum of numbers from 1 to 100 by
using recursion.
'''

def sum(n):
    if n==1:
        return 1
    return n + sum(n-1)

print(sum(100))