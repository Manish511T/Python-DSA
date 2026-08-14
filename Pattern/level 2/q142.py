'''
enter no. of rows: 5
I       H       G       F       E       D       C       B       A  
        G       F       E       D       C       B       A  
                E       D       C       B       A  
                        C       B       A  
                                A  
'''
def print_pattern(n):
    pattern_size = 2*n-1
    space = 0
    for i in range(1, n+1):
        num = pattern_size
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