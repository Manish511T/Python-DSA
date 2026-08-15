'''
Enter no. of row: 7
                        1 
                1       1       2 
        3       4       1       5       6 
1       1       1       1       1       1       1 
        7       8       1       9       10 
                11      1       12 
                        1 
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
            if i==mid or j==colmid:
                print(1, '\t', end='')
            else:
                print(num, '\t', end='')
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