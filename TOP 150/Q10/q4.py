'''
Enter no. of rows: 9
* * * * * 
* * * * 
* * * 
* * 
* 
* * 
* * * 
* * * * 
* * * * * 
'''
def  print_pattern(n):
    mid = n//2+1
    pattern_size = mid 
    for i in range(1, n+1):
        for j in range(1, pattern_size+1):
            print('* ', end='')
        print()

        if i<mid:
            pattern_size -=1
        else:
            pattern_size +=1


n = int(input("Enter no. of rows: "))
print_pattern(n)