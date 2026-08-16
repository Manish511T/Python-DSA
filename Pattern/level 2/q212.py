'''
Enter no. of row: 7
1                                               1 
2       2                               2       2 
3       3       3               3       3       3 
4       4       4       4       4       4       4 
5       5       5               5       5       5 
6       6                               6       6 
7                                               7 
'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only")
    start = 1
    end = n
    mid = n//2+1

    for i in range(1, n+1):
        for j in range(1, n+1):
            if j<=start or j>=end:
                print(i,'\t', end='')
            else:
                print('  ','\t', end='')
        print()
        if i<mid:
            start +=1
            end -=1
        else:
            start -=1
            end +=1

n = int(input("Enter no. of row: "))
print_pattern(n)

