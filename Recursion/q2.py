'''
WAJP to generate numbers from 10 to 1 by
using recursion.
'''

def printNumber(n):
    if n>10:
        return 
    
    printNumber(n+1)
    print(n)

printNumber(1)