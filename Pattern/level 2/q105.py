'''
Enter a size of row: 5
                                Y   
                        X       W       V   
                U       T       S       R       Q   
        P       O       N       M       L       K       J   
I       H       G       F       E       D       C       B       A   
'''

def print_pattern(n):
    pattern_size = 1
    space = n-1
    num = n*n
    for i in range(1, n+1):
        for j in range(1, space+1):
            print("\t", end='')
        for j in range(1, pattern_size+1):
            print(chr(64+num),'  \t', end='')
            num-=1
        
        space -=1
        pattern_size+=2
        print()


n = int(input("Enter a size of row: "))
print_pattern(n)