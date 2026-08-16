'''
Enter no. of rows: 7
                        1 
                2               2 
        3                               3 
4                                               4 
        5                               5 
                6               6 
                        7 
'''
def print_pattern(n):
    if n%2==0:
        print("Enter only odd number!")
        return
    mid = n//2+1
    start = mid
    end = mid

    for i in range(1, n+1):
        for j in range(1, n+1):
            if j==start or j==end:
                print(i, '\t', end='')
            else:
                print('\t', end='')

        if i<mid:
            start -=1
            end +=1
        else:
            start +=1
            end -=1
        print()

n = int(input("Enter no. of rows: "))
print_pattern(n)