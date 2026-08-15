'''
Enter no. of row: 7
                        A 
                A       B       A 
        A       B       C       B       A 
A       B       C       D       C       B       A 
        A       B       C       B       A 
                A       B       A 
                        A 
'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only")
    pattern_size = 1
    mid = n//2+1
    space = mid-1
    
    for i in range(1, n+1):
        num = 1
        for j in range(1,space+1):
            print('\t', end='')
        colmid = pattern_size//2+1
        for j in range(1, pattern_size+1):
            if j<colmid:
                print(chr(64+num), '\t', end='')
                num +=1
            else:
                print(chr(64+num), '\t', end='')
                num -=1

        if i<mid:
            num -=1
            pattern_size +=2
            space -=1
        else:
            num +=1
            pattern_size -=2
            space +=1
        print()


n = int(input("Enter no. of row: "))
print_pattern(n)