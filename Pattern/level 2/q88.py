'''
Enter a size of row: 5
                1   
            0   0   0   
        1   1   1   1   1   
    0   0   0   0   0   0   0   
1   1   1   1   1   1   1   1   1  
'''

def print_pattern(n):
    pattern_size = 1
    space = n-1
    for i in range(1, n+1):
        
        for j in range(1, space+1):
            print("    ", end='')
        for j in range(1, pattern_size+1):
            print(i%2,'  ',end='')
        space -=1
        pattern_size +=2
        print()

n = int(input("Enter a size of row: "))
print_pattern(n)