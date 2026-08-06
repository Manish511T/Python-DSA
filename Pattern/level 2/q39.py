'''

'''


def print_pattern(n):
    num = 1
    for i in range(1, n+1):
        for j in range(num):
            print(num,' ', end='')
        num +=1
        print()


n = int(input("Enter a number: "))
print_pattern(n)