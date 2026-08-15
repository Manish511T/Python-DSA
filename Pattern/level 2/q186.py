'''
Enter no. of row: 7
                        A 
                B       B       B 
        C       C       C       C       C 
D       D       D       D       D       D       D 
        E       E       E       E       E 
                F       F       F 
                        G 
`'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only")
    pattern_size = 1
    mid = n//2+1
    space = mid-1

    for i in range(1, n+1):
        for j in range(1,space+1):
            print('\t', end='')
        
        for j in range(1, pattern_size+1):
            print(chr(64+i), '\t', end='')
        
        if i<mid:
            pattern_size +=2
            space -=1
        else:
            pattern_size -=2
            space +=1
        print()


n = int(input("Enter no. of row: "))
print_pattern(n)