'''
Enter a size of row: 5
E 
D       D 
C       C       C 
B       B       B       B 
A       A       A       A       A 
'''

def print_pattern(n):
    pattern_size = 1
    num = n

    for i in range(1, n+1):
        for j in range(1, pattern_size+1):
            print(chr(64+num), "\t", end='')
        pattern_size+=1
        num -=1
        print()

n = int(input("Enter a size of row: "))
print_pattern(n)