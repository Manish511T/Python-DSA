def pattern_print(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i,end='\t')
        print()

n=int(input('Enter a Number: '))
pattern_print(n)