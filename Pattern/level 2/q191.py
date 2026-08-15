'''
Enter no. of row: 7
                        D 
                C       C       C 
        B       B       B       B       B 
A       A       A       A       A       A       A 
        B       B       B       B       B 
                C       C       C 
                        D 
'''

def print_pattern(n):
    if n%2==0:
        print("Odd number only")
    pattern_size = 1
    mid = n//2+1
    space = mid-1
    num = mid
    for i in range(1, n+1):
        for j in range(1,space+1):
            print('\t', end='')
        
        for j in range(1, pattern_size+1):
            print(chr(64+num), '\t', end='')
        
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