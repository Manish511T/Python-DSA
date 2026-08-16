'''
Enter no. of row: 7
31                                              30 
29      28                              27      26 
25      24      23              22      21      20 
19      18      17      16      15      14      13 
12      11      10              9       8       7 
6       5                               4       3 
2                                               1 
'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only!")
        return

    start = 1
    end = n
    mid = n//2+1
    num = n*(n+1)//2 + mid -1
    for i in range(1, n+1):
        
        for j in range(1, n+1):
            if j<=start or j>=end:
                print(num, '\t', end='')
                num -=1
            else:
                print(' ', '\t', end='')

        if i<mid:
            start +=1
            end -=1
        else:
            start -=1
            end +=1
        print()

n = int(input("Enter no. of row: "))
print_pattern(n)
