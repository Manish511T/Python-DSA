'''
Enter a size of row: 7
                  1  
               2  2  
            3  3  3  
         4  4  4  4  
      5  5  5  5  5  
   6  6  6  6  6  6  
7  7  7  7  7  7  7 
'''
def print_pattern(n):
    pattern_size = 1
    space = n-1

    for i in range(1, n+1):
        for j in range(1, space+1):
            print(' ',' ', end='')
        for j in range(1, pattern_size+1):
            print(i,' ', end='')
        space -=1
        pattern_size+=1
        print()
        

n = int(input("Enter a size of row: "))
print_pattern(n)