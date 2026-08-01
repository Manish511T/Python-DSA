'''
Enter a number: 7
1  
2  2  
3  3  3  
4  4  4  4  
5  5  5  5  5  
6  6  6  6  6  6  
7  7  7  7  7  7  7 
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

