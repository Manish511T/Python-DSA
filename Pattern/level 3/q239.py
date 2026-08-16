'''
Enter no. of rows: 5
1       2       3       4       5 
6       7       8       9       10 
11      12      13      14      15 
16      17      18      19      20 
21      22      23      24      25 
'''
def print_pattern(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(num, '\t', end='')
            num +=1
        print()

n = int(input("Enter no. of rows: "))
print_pattern(n)