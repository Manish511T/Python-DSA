'''
Enter nth number to print series: 10
1 3 7 13 21 31 43 57 73 91 
'''
def print_series(n):
    num = 1
    diff = 2
    for i in range(0, n):
        print(num, end=' ')
        num = num + diff
        diff = diff +2


n = int(input("Enter nth number to print series: "))
print_series(n)