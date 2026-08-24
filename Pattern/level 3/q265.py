def print_pascalRow(n):
    comb = 1
    print(comb, '\t\t', end='')

    for i in range(0, n):
        comb = comb*(n-i)//(i+1)
        print(comb, '\t\t', end='')


def pascalTriangle(n):
    space = n
    for i in range(0, n+1):
        for j in range(1, space+1):
            print('\t', end='')
        print_pascalRow(i)
        space -= 1
        print()


n=int(input("Enter the number of Rows: "))
pascalTriangle(n)