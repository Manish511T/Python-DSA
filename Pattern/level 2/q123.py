'''
Enter a size of row: 5
E               E               E               E               E 
        D               D               D               D 
                C               C               C 
                        B               B 
                                A 
'''

def print_pattern(n):
    pattern_size = n
    space = 0
    num = n
    for i in range(1, n+1):
        for j in range(1, space+1):
            print('\t', end='')
        for j in range(1, pattern_size+1):
            print(chr(64+num), '\t\t', end='')
        num -=1
        pattern_size -=1
        space +=1
        print()


n = int(input("Enter a size of row: "))
print_pattern(n)