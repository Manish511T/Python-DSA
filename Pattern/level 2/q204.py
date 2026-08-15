'''
Enter no. of row: 7
3       3       3       3       3       3       3 
        2       2       2       2       2 
                1       1       1 
                        0 
                1       1       1 
        2       2       2       2       2 
3       3       3       3       3       3       3 
'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only")
    pattern_size = n
    mid = n//2+1
    space = 0
    num = mid-1
    for i in range(1, n+1):
        for j in range(1, space+1):
            print('\t', end='')
        for j in range(1, pattern_size+1):
            print(num, '\t', end='')
        
        if i<mid:
            num -=1
            pattern_size -=2
            space +=1
        else:
            num +=1
            pattern_size +=2
            space -=1
        print()


        
n = int(input("Enter no. of row: "))
print_pattern(n)