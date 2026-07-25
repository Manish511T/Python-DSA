
def printPattern(n):
    mid = n//2+1
    space = 0
    patternSize = n

    for i in range(1, n+1):
        for j in range(1, space+1):
            print("  ", end='')
        for j in range(1, patternSize+1):
            print("* ", end='')
        if i<mid:
            patternSize -=2
            space +=1
        else:
            patternSize +=2
            space -=1
        print()

n = int(input("Enter a number: "))
if n%2==0:
    print("Row must be odd number!")
else:
    printPattern(n)