'''
Enter a size of row: 5
                                A   
                        A       B       C   
                A       B       C       D       E   
        A       B       C       D       E       F       G   
A       B       C       D       E       F       G       H       I  
'''

def print_pattern(n):
    pattern_size = 1
    space = n-1
    
    for i in range(1, n+1):
        for j in range(1, space+1):
            print("\t", end='')
        for j in range(1, pattern_size+1):
            print(chr(64+j),'  \t', end='')
        
        space -=1
        pattern_size+=2
        print()


n = int(input("Enter a size of row: "))
print_pattern(n)