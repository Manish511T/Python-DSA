'''
Enter no. of row: 7
1                                               2 
3       4                               5       6 
7       8       9               10      11      12 
13      14      15      16      17      18      19 
20      21      22              23      24      25 
26      27                              28      29 
30                                              31
'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only!")
        return

    start = 1
    end = n
    mid = n//2+1
    num = 1
    for i in range(1, n+1):
        
        for j in range(1, n+1):
            if j<=start or j>=end:
                print(num, '\t', end='')
                num +=1
            else:
                print(' ', '\t', end='')

        if i<mid:
            start +=1
            end -=1
        else:
            start -=1
            end +=1
        print()

n = int(input("Enter no. of row: "))
print_pattern(n)
