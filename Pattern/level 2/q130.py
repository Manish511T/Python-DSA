'''
Enter a size of row: 5
25      24      23      22      21      20      19      18      17    
        16      15      14      13      12      11      10    
                9       8       7       6       5    
                        4       3       2    
                                1  
'''

def print_pattern(n):
    pattern_size = 2*n-1
    space = 0
    
    num = n*n
    for i in range(1, n+1):
        for j in range(1, space+1):
            print(' ','\t', end='')
        for j in range(1, pattern_size+1):
            print(num, '   \t', end='')
            num -=1
        pattern_size -=2
        space +=1
        print()


n = int(input("Enter a size of row: "))
print_pattern(n)