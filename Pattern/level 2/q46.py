'''
Enter a number: 5
15 
13      14 
10      11      12 
6       7       8       9 
1       2       3       4       5 
'''
def print_pattern(n):
    pattern_size = 1
    num = n*(n+1)//2
    for i in range(1, n+1):
        for j in range(1, pattern_size+1):
            print(num, '\t', end='')
            num +=1
        num = num - (2*i+1)
        pattern_size +=1
        print()

n = int(input("Enter a number: "))
print_pattern(n)