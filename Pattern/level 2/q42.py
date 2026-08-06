'''
Enter a number: 7
1  
2  1  
3  2  1  
4  3  2  1  
5  4  3  2  1  
6  5  4  3  2  1  
7  6  5  4  3  2  1 
'''


def print_pattern(n):
    pattern_size = 1
    for i in range(1, n+1):
        num = pattern_size
        for j in range(1, pattern_size+1):
            print(num,' ', end='')
            num -=1
        pattern_size+=1
        print()


n = int(input("Enter a number: "))
print_pattern(n)