'''
Enter no. of row: 5
Q                               P 
O       N               M       L 
K       J       I       H       G 
F       E               D       C 
B                               A
'''
def print_pattern(n):
    if n%2==0:
        print("Odd number only!")
        return

    start = 1
    end = n
    mid = n//2+1
    num = n*(n+1)//2+mid-1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j<=start or j>=end:
                print(chr(64+num), '\t', end='')
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
