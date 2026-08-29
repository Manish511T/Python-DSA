'''
WAJP to print sum of cubes of numbers from 1
to 100 by using recursion.
'''

def getSumOfCube(n):
    if n==1:
        return 1

    return n**3 + getSumOfCube(n-1)

print(getSumOfCube(100))