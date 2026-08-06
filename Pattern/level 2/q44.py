'''
Enter a number: 5
15  
14  13  
12  11  10  
9  8  7  6  
5  4  3  2  1  
'''

def print_pattern(n):
    pattern_size = 1
    num = n*3
    for i in range(1, n+1):
        for j in range(1, pattern_size+1):
            print(num, ' ', end='')
            num -=1
        pattern_size+=1
        print()

n = int(input("Enter a number: "))
print_pattern(n)
