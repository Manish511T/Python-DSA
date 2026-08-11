'''
A               A               A               A               A 
        B               B               B               B 
                C               C               C 
                        D               D 
                                E 
'''

def print_pattern(n):
    pattern_size = n
    space = 0

    for i in range(1, n+1):
        for j in range(1, space+1):
            print('\t', end='')
        for j in range(1, pattern_size+1):
            print(chr(64+i), '\t\t', end='')
        pattern_size -=1
        space +=1
        print()


n = int(input("Enter a size of row: "))
print_pattern(n)