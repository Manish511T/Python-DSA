'''
enter no. of rows: 5
E       E       E       E       E       E       E       E       E  
        D       D       D       D       D       D       D  
                C       C       C       C       C  
                        B       B       B  
                                A
'''

def print_pattern(n):
    pattern_size = 2*n-1
    space = 0
    num = n
    for i in range(1, n+1):
        for j in range(1, space+1):
            print(' ', '\t', end='')
        for j in range(1, pattern_size+1):
            print(chr(num+64), ' \t', end='')
        num -=1
        pattern_size -=2
        space +=1
        print()

n = int(input("enter no. of rows: "))
print_pattern(n)