'''
Enter a size of row: 5
                                1 
                        3       2 
                6       5       4 
        10      9       8       7 
15      14      13      12      11 
'''

def print_pattern(n):
    pattern_size = 1
    space = n-1
    num = 1
    for i in range(1, n+1):
        num += pattern_size-1
        for j in range(1, space+1):
            print(' ','\t', end='')
        for j in range(1, pattern_size+1):
            print(num,'\t', end='')
            num-=1
        num += pattern_size+1
        space -=1
        pattern_size+=1
        print()

n = int(input("Enter a size of row: "))
print_pattern(n)