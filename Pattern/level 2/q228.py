'''
Enter nth number to print series: 10
3 5 9 17 33 65 129 257 513 1025 
'''
def print_series(n):
    num = 3
    for i in range(1, n+1):
        print(num, end=' ')
        num = num*2-1

n = int(input("Enter nth number to print series: "))
print_series(n)