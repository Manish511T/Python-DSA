'''
Enter no. of rows: 7
*
**
***
****
***
**
*
'''
def  print_pattern(n):
    pattern_size = 1
    mid = n//2+1
    for i in range(1, n+2):
        for j in range(1, pattern_size+1):
            print('*', end='')
        print()

        if i<mid:
            pattern_size +=1
        else:
            pattern_size -=1


n = int(input("Enter no. of rows: "))
print_pattern(n)