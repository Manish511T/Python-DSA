'''
Enter a size of row: 7
                                                7 
                                        6       6 
                                5       5       5 
                        4       4       4       4 
                3       3       3       3       3 
        2       2       2       2       2       2 
1       1       1       1       1       1       1 
'''

def print_pattern(n):
    pattern_size = 1
    space = n-1
    num = n
    for i in range(1, n+1):
        for j in range(1, space+1):
            print(' ','\t', end='')
        for j in range(1, pattern_size+1):
            print(num,'\t', end='')
        num-=1
        space -=1
        pattern_size+=1
        print()
        

n = int(input("Enter a size of row: "))
print_pattern(n)