'''
Enter nth number to print series: 10
1 3 7 15 31 63 127 255 511 1023 
'''
def print_series(n):
    num = 1
    for i in range(1, n+1):
        print(num, end=' ')
        num = 2*num +1

n = int(input("Enter nth number to print series: "))
print_series(n)