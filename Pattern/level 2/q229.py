'''
Enter nth number to print series: 5
1 2 5 26 677 
'''
def print_series(n):
    num = 1
    for i in range(1, n+1):
        print(num, end=' ')
        num = num*num +1

n = int(input("Enter nth number to print series: "))
print_series(n)