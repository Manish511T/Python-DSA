'''
Enter a size of row: 5
9       8       7       6       5       4       3       2       1  
        7       6       5       4       3       2       1  
                5       4       3       2       1  
                        3       2       1  
                                1  
'''

def print_pattern(n):
    pattern_size = 2*n-1
    space = 0
    for i in range(1, n+1):
        num = pattern_size
        for j in range(1, space+1):
            print(' ','\t', end='')
        for j in range(1, pattern_size+1):
            print(num, ' \t', end='')
            num -=1
        pattern_size -=2
        space +=1
        print()

n = int(input("Enter a size of row: "))
print_pattern(n)