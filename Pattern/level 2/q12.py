def printPattern(n):
    patterSize = 1
    for i in range(1, n+1):
        for j in range(patterSize):
            print('*', end=' ')
        patterSize +=1
        print()


n = int(input("Enter a number: "))
printPattern(n)
