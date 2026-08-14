'''
Enter a size of row: 5
1       2       3       4       5       4       3       2       1  
        2       3       4       5       4       3       2  
                3       4       5       4       3  
                        4       5       4  
                                5  
'''

def print_pattern(n):
    pattern_size = 2*n-1
    space = 0
    num = 1
    for i in range(1, n+1):
        for j in range(1, space+1):
            print(' ','\t', end='')
        colmid = pattern_size//2+1
        for j in range(1, pattern_size+1):
            if j<colmid:
                print(num, ' \t', end='')
                num +=1
            else:
                print(num, ' \t', end='')
                num -=1
        num = i+1
        pattern_size -=2
        space +=1
        print()

n = int(input("Enter a size of row: "))
print_pattern(n)