'''
Enter no. of row: 7
A                                               A 
A       B                               B       A 
A       B       C               C       B       A 
A       B       C       D       C       B       A 
A       B       C               C       B       A 
A       B                               B       A 
A                                               A 
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
            if j==start and j==end:
                print(chr(64+num), '\t', end='')
            elif j<=start :
                print(chr(64+num), '\t', end='')
                num+=1
            elif j>=end:
                print(chr(64+num-1), '\t', end='')
                num-=1
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
