'''
Enter a size of row: 5
                                1  
                        1       1       2   
                3       4       1       5       6   
        7       8       9       1       10      11      12   
13      14      15      16      1       17      18      19      20  
'''

def print_pattern(n):
    pattern_size = 1
    space = n-1
    num = 1
    for i in range(1, n+1):
        for j in range(1, space+1):
            print('\t', end='')

        colmid = pattern_size//2+1
        for j in range(1, pattern_size+1):
            if j==colmid:
                print(1,' \t', end='')
            else:
                print(num,'  \t',end='')
                num +=1
        space -=1
        pattern_size +=2
        print()

n = int(input("Enter a size of row: "))
print_pattern(n)