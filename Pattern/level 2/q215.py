'''
Enter no. of row: 7
1                                               1 
1       0                               0       1 
1       0       1               1       0       1 
1       0       1       0       1       0       1 
1       0       1               1       0       1 
1       0                               0       1 
1                                               1 
'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only!")
        return

    start = 1
    end = n
    mid = n//2+1

    for i in range(1, n+1):
        num = 1
        for j in range(1, n+1):
            if j<=start or j>=end:
                print(num%2, '\t', end='')
            else:
                print(' ', '\t', end='')
            num +=1

        if i<mid:
            start +=1
            end -=1
        else:
            start -=1
            end +=1
        print()

n = int(input("Enter no. of row: "))
print_pattern(n)
