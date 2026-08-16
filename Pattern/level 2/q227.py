'''
Enter nth number to print series: 10
2 5 11 23 47 95 191 383 767 1535 
'''
def print_series(n):
    num = 2
    for i in range(1, n+1):
        print(num, end=' ')
        num = num * 2+1

n = int(input("Enter nth number to print series: "))
print_series(n)