'''
enter no. of rows: 5
E       D       C       B       A       B       C       D       E  
        D       C       B       A       B       C       D  
                C       B       A       B       C  
                        B       A       B  
                                A  
'''

def print_pattern(n):
    pattern_size = 2*n-1
    space = 0
    for i in range(1, n+1):
        num = n-i+1
        for j in range(1, space+1):
            print(' ', '\t', end='')
        colmid = pattern_size//2+1
        for j in range(1, pattern_size+1):
            if j<colmid:
                print(chr(num+64), ' \t', end='')
                num -=1
            else:
                print(chr(num+64), ' \t', end='')
                num +=1
        
        pattern_size -=2
        space +=1
        print()

n = int(input("enter no. of rows: "))
print_pattern(n)