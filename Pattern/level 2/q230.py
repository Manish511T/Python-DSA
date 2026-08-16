'''
Enter nth number to print series: 7
1 2 6 7 21 22 66 
'''
def print_series(n):
    num = 1
    for i in range(0, n):
        print(num, end=' ')
        if i%2==0:
            num = num + 1
        else:
            num = num*3

n = int(input("Enter nth number to print series: "))
print_series(n)