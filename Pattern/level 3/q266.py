'''
Enter the number of Rows: 7
4       4       4       4       4       4       4 
4       3       3       3       3       3       4 
4       3       2       2       2       3       4 
4       3       2       1       2       3       4 
4       3       2       2       2       3       4 
4       3       3       3       3       3       4 
4       4       4       4       4       4       4 
'''
def print_pattern(n):
    if n % 2 == 0:
        print("Odd number only!")
        return

    mid = n // 2 + 1
    start = 1
    end = n

    for i in range(1, n + 1):
        num = mid

        for j in range(1, n + 1):

            if j < start:
                print(num, '\t', end='')
                num -= 1

            elif j >= end:
                print(num, '\t', end='')
                num += 1

            else:
                print(num, '\t', end='')   

        if i < mid:
            start += 1
            end -= 1
        else:
            start -= 1
            end += 1

        print()


n = int(input("Enter the number of Rows: "))
print_pattern(n)