'''
Enter a number: 5
A  
B  C  
D  E  F  
G  H  I  J  
K  L  M  N  O  
'''

def print_pattern(n):
    pattern_size = 1
    num = 1
    for i in range(1,n+1):
        for j in range(1, pattern_size+1):
            print(chr(num+64),' ', end='')
            num +=1
        pattern_size+=1
        print()

n = int(input("Enter a number: "))
print_pattern(n)