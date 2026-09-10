'''
Enter no. of rows: 7
            * 
          * * 
        * * * 
      * * * * 
    * * * * * 
  * * * * * * 
* * * * * * *
'''
def  print_pattern(n):
    space = n-1
    pattern_size = 1 
    for i in range(1, n+1):
        for j in range(1, space+1):
            print('  ', end='')
        for j in range(1, pattern_size+1):
            print('* ', end='')
        print()
        space -=1
        pattern_size +=1


n = int(input("Enter no. of rows: "))
print_pattern(n)