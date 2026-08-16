'''
Enter no. of rows: 7
                        A 
                B               B 
        C                               C 
D                                               D 
        C                               C 
                B               B 
                        A 
'''
def print_pattern(n):
    if n%2==0:
        print("Enter only odd number!")
        return
    mid = n//2+1
    start = mid
    end = mid
    num = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j==start or j==end:
                print(chr(num+64), '\t', end='')
            else:
                print('\t', end='')

        if i<mid:
            num +=1
            start -=1
            end +=1
        else:
            num -=1
            start +=1
            end -=1
        print()

n = int(input("Enter no. of rows: "))
print_pattern(n)