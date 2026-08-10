'''
Enter a size of row: 5
            A  
         A  B  
      A  B  C  
   A  B  C  D  
A  B  C  D  E  
'''

def print_pattern(n):
    pattern_size = 1
    space = n-1
    for i in range(1, n+1):
        for j in range(1, space+1):
            print(' ', ' ', end='')
        for j in range(1, pattern_size+1):
            print(chr(64+j),' ', end='')
        pattern_size +=1
        space -=1
        print()

n = int(input("Enter a size of row: "))
print_pattern(n)