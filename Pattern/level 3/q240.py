'''
Enter no. of rows: 5
25      24      23      22      21 
20      19      18      17      16 
15      14      13      12      11 
10      9       8       7       6 
5       4       3       2       1 
'''
def print_pattern(n):
    num = n*n
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(num, '\t', end='')
            num -=1
        print()

n = int(input("Enter no. of rows: "))
print_pattern(n)