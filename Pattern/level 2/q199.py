'''
Enter no. of row: 7
31      30      29      28      27      26      25 
        24      23      22      21      20 
                19      18      17 
                        16 
                15      14      13 
        12      11      10      9       8 
7       6       5       4       3       2       1 
'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only")
    pattern_size = n
    mid = n//2+1
    space = 0
    num = n*(n+1)//2 + mid-1

    for i in range(1, n+1):
        for j in range(1, space+1):
            print('\t', end='')
        for j in range(1, pattern_size+1):
            print(num, '\t', end='')
            num-=1

        if i<mid:
            pattern_size -=2
            space +=1
        else:
            pattern_size +=2
            space -=1
        print()


        
n = int(input("Enter no. of row: "))
print_pattern(n)