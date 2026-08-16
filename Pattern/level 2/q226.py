'''
Enter nth number to print series: 10
2 6 12 20 30 42 56 72 90 110
'''
def print_series(n):
    for i in range(1, n+1):
        res = i*(i+1)
        print(res, end=' ')

n = int(input("Enter nth number to print series: "))
print_series(n)