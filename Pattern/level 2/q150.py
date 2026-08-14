'''
Enter no. of row: 7
                        16 
                15              14 
        13              12              11 
10              9               8               7 
        6               5               4 
                3               2 
                        1 
'''

def print_pattern(n):
    if n%2 ==0 :
        print("Odd number only! ")
        return
    pattern_size = 1
    mid = n//2+1
    space = mid-1
    num = mid**2
    for i in range(1, n+1):
        for j in range(1,space+1):
            print('\t', end='')
        for j in range(1, pattern_size+1):
            print(num,'\t\t', end='')
            num -=1
        if i<mid:
            space -=1
            pattern_size +=1
        else :
            space +=1
            pattern_size -=1
        print()

n = int(input("Enter no. of row: "))
print_pattern(n)