'''
Enter a size of row: 7
1   2   3   4   5   6   7   
  1   2   3   4   5   6   
    1   2   3   4   5   
      1   2   3   4   
        1   2   3   
          1   2   
            1  
'''

def print_pattern(n):
    pattern_size = n
    space = 0
    for i in range(1, n+1):
        for j in range(1, space+1):
            print("  ", end='')
        for j in range(1, pattern_size+1):
            print(j, '  ', end='')
        pattern_size -=1
        space +=1
        print()


n = int(input("Enter a size of row: "))
print_pattern(n)
