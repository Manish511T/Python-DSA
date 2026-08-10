'''
Enter a size of row: 5
            A  
         C  B  
      F  E  D  
   J  I  H  G  
O  N  M  L  K 
'''

def print_pattern(n):
    pattern_size = 1
    space = n-1
    num = 1
    for i in range(1, n+1):
        for j in range(1, space+1):
            print(' ', ' ', end='')
        for j in range(1, pattern_size+1):
            print(chr(64+num),' ', end='')
            num -=1
        num +=2*i+1
        pattern_size +=1
        space -=1
        print()

n = int(input("Enter a size of row: "))
print_pattern(n)