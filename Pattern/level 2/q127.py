'''
Enter a size of row: 5
1    2    3    4    5    6    7    8    9    
     1    2    3    4    5    6    7    
          1    2    3    4    5    
               1    2    3    
                    1
'''

def print_pattern(n):
    pattern_size = 2*n-1
    space = 0
    
    for i in range(1, n+1):
        num = 1
        for j in range(1, space+1):
            print(' ','   ', end='')
        for j in range(1, pattern_size+1):
            print(num, '   ', end='')
            num +=1
        pattern_size -=2
        space +=1
        print()


n = int(input("Enter a size of row: "))
print_pattern(n)