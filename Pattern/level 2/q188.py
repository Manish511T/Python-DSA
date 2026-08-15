'''
Enter no. of row: 7
                        A 
                B       C       D 
        E       F       G       H       I 
J       K       L       M       N       O       P 
        Q       R       S       T       U 
                V       W       X 
                        Y 
'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only")
    pattern_size = 1
    mid = n//2+1
    space = mid-1
    
    num = 1
    for i in range(1, n+1):
        for j in range(1,space+1):
            print('\t', end='')
        colmid = pattern_size//2+1
        for j in range(1, pattern_size+1):
            print(chr(64+num), '\t', end='')
            num +=1
        
        if i<mid:
            pattern_size +=2
            space -=1
        else:
            pattern_size -=2
            space +=1
        print()


n = int(input("Enter no. of row: "))
print_pattern(n)