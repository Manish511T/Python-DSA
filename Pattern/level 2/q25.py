
def printPattern(n):
    mid = n//2+1
    space = mid-1
    patternSize = 1

    for i in range(1, n):
        for j in range(1,space+1):
            print("  ", end='')
        for j in range(1, patternSize+1):
            print('* ', end='')
        if i<mid:
            space -= 1
            patternSize +=2
        else:
            space += 1
            patternSize -=2
        print()
        


n = int(input("Enter a number: "))
printPattern(n)
