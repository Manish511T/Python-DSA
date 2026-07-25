'''
n=7
* * * * 
* * * 
* * 
* 
* * 
* * * 
* * * * 
'''


def printPattern(n):
    mid = n//2 +1
    patternSize = mid

    for i in range(1, n+1):
        for j in range(1, patternSize+1):
            print('*', end=' ')
        if i<mid:
            patternSize -=1
        else:
            patternSize +=1

        print()


n = int(input("Enter a number: "))
if n%2==0:
    print("Row must be an odd number!")
else:
    printPattern(n)

