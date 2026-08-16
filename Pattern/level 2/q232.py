'''
Enter number to print Finonacci series: 10
0 0 1 1 2 4 7 13 24 44 
'''
def print_series(n):
    first = 0
    second = 0
    third = 1
    for i in range(0, n):
        print(first, end=' ')
        first, second, third = second,third ,first+second+third

n = int(input("Enter number to print Finonacci series: "))
print_series(n)