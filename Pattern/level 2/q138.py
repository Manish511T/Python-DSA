'''
enter no. of rows: 5
A       B       C       D       E       F       G       H       I  
        A       B       C       D       E       F       G  
                A       B       C       D       E  
                        A       B       C  
                                A  
'''

def print_pattern(n):
    pattern_size = 2*n-1
    space = 0

    for i in range(1, n+1):
        for j in range(1, space+1):
            print(' ', '\t', end='')
        for j in range(1, pattern_size+1):
            print(chr(j+64), ' \t', end='')
        pattern_size -=2
        space +=1
        print()

n = int(input("enter no. of rows: "))
print_pattern(n)