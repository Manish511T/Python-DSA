'''
Enter a size of row: 5
A 
B       B 
C       C       C 
D       D       D       D 
E       E       E       E       E 
'''

def print_pattern(n):
    pattern_size = 1

    for i in range(1, n+1):
        for j in range(1, pattern_size+1):
            print(chr(64+i),'\t', end='')
        pattern_size +=1
        print()

n = int(input("Enter a size of row: "))
print_pattern(n)