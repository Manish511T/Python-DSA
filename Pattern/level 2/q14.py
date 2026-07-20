def printPattern(n):
    patternSize = n
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j>=patternSize:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        patternSize -=1
        print()

n = int(input("Enter a number: "))
printPattern(n)

