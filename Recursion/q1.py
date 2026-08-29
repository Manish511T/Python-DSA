'''
WAJP to generate numbers from 1 to 10 by using recursion.
'''

def printNumber(n):
    if n>10:
        return 

    print(n)
    return printNumber(n+1)

printNumber(1)