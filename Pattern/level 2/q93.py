'''
Enter a size of row: 5
                                1   
                        2       3       4   
                5       6       7       8       9   
        10      11      12      13      14      15      16   
17      18      19      20      21      22      23      24      25 
'''

def print_pattern(n):
    pattern_size = 1
    space = n-1
    num = 1
    for i in range(1, n+1):
        for j in range(1, space+1):
            print('\t', end='')
        for j in range(1, pattern_size+1):
            print(num,'  \t',end='')
            num +=1
        space -=1
        pattern_size +=2
        print()

n = int(input("Enter a size of row: "))
print_pattern(n)