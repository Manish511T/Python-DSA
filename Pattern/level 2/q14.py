def printPattern(n):
    pattern_size = 1
    mid = n//2+1

    for i in range(1, n+1):
        for j in range(1, pattern_size):
            print('*', end=' ')
        if i<mid:
            pattern_size +=1
        else:
            pattern_size -=1
        print()


n = int(input("Enter a number: "))
printPattern(n)
