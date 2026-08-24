'''
Enter the number of Rows: 7
                                                        1 
                                                1               1 
                                        1               2               1 
                                1               3               3               1 
                        1               4               6               4               1 
                1               5               10              10              5               1 
        1               6               15              20              15              6               1 
1               7               21              35              35              21              7               1 
'''

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