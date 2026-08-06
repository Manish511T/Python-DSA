'''
Enter a number: 5
1 
3       2 
6       5       4 
10      9       8       7 
15      14      13      12      11 
'''
def print_pattern(n):
    pattern_size = 1
    num = 1
    for i in range(1, n+1):
        num += pattern_size - 1
        for j in range(1, pattern_size+1):
            print(num, '\t', end='')
            num -=1
        pattern_size+=1
        num +=pattern_size
        print()

n = int(input("Enter a number: "))
print_pattern(n)