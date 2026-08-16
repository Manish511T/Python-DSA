'''
Enter number to print Finonacci series: 10
0 1 1 2 3 5 8 13 21 34 
'''
def print_series(n):
    first = 0
    second = 1

    for i in range(0, n):
        print(first, end=' ')
        first, second = second, first+second

n = int(input("Enter number to print Finonacci series: "))
print_series(n)