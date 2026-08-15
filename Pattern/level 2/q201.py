'''
Enter no. of row: 7
3       2       1       0       1       2       3 
        2       1       0       1       2 
                1       0       1 
                        0 
                1       0       1 
        2       1       0       1       2 
3       2       1       0       1       2       3 
'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only")
    pattern_size = n
    mid = n//2+1
    space = 0
    num = mid - 1
    for i in range(1, n+1):
        for j in range(1, space+1):
            print('\t', end='')
        colmid = pattern_size//2+1
        for j in range(1, pattern_size+1):
            if j<colmid:
                print(num, '\t', end='')
                num -=1
            else:
                print(num, '\t', end='')
                num +=1

        if i<mid:
            num -= 2
            pattern_size -=2
            space +=1
        else:
            pattern_size +=2
            space -=1
        print()


        
n = int(input("Enter no. of row: "))
print_pattern(n)