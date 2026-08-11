'''
Enter a size of row: 5
                                A
                        B       C       B
                C       D       E       D       C
        D       E       F       G       F       E       D
E       F       G       H       I       H       G       F       E   
'''

def print_pattern(n):
    pattern_size = 1
    space = n-1
    for i in range(1, n+1):
        num = i
        for j in range(1, space+1):
            print("\t", end='')
        colmid = pattern_size//2+1
        for j in range(1, pattern_size+1):
            if j<colmid:
                print(chr(64+num),'  \t', end='')
                num +=1
            else:
                print(chr(64+num),'  \t', end='')
                num -=1
        space -=1
        pattern_size+=2
        print()


n = int(input("Enter a size of row: "))
print_pattern(n)