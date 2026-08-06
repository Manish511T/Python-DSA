'''
Enter a number: 5
O  
N  M  
L  K  J  
I  H  G  F  
E  D  C  B  A 
'''


def print_pattern(n):
    pattern_size = 1
    num = n*(n+1)//2

    for i in range(1, n+1):
        for j in range(1, pattern_size+1):
            print(chr(num+64), ' ',end='')
            num -=1
        pattern_size+=1
        print()

n = int(input("Enter a number: "))
print_pattern(n)