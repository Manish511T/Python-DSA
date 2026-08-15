'''
Enter no. of row: 7
1       2       3       4       5       6       7 
        8       9       10      11      12 
                13      14      15 
                        16 
                17      18      19 
        20      21      22      23      24 
25      26      27      28      29      30      31 
'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only")
    pattern_size = n
    mid = n//2+1
    space = 0

    num = 1
    for i in range(1, n+1):
        for j in range(1, space+1):
            print('\t', end='')
        for j in range(1, pattern_size+1):
            print(num, '\t', end='')
            num+=1

        if i<mid:
            pattern_size -=2
            space +=1
        else:
            pattern_size +=2
            space -=1
        print()


        
n = int(input("Enter no. of row: "))
print_pattern(n)