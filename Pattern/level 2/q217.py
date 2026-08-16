'''
Enter no. of row: 7
1                                               1 
1       2                               2       1 
1       2       3               3       2       1 
1       2       3       4       3       2       1 
1       2       3               3       2       1 
1       2                               2       1 
1                                               1
'''
def print_pattern(n):
    if n % 2 == 0:
        print("Odd number only!")
        return

    start = 1
    end = n
    mid = n // 2 + 1

    for i in range(1, n + 1):
        num = 1

        for j in range(1, n + 1):

            if j == start and j == end:
                print(num, '\t', end='')

            elif j <= start:
                print(num, '\t', end='')
                num += 1

            elif j >= end:
                print(num - 1, '\t', end='')
                num -= 1

            else:
                print(' ', '\t', end='')

        if i < mid:
            start += 1
            end -= 1
        else:
            start -= 1
            end += 1

        print()


n = int(input("Enter no. of row: "))
print_pattern(n)