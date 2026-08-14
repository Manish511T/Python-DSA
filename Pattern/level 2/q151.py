'''
Enter no. of row: 7
                        1 
                2               2 
        3               3               3 
4               4               4               4 
        3               3               3 
                2               2 
                        1 
'''
def print_pattern(n):
    if n%2 ==0 :
        print("Odd number only! ")
        return
    pattern_size = 1
    mid = n//2+1
    space = mid-1
    num = 1
    for i in range(1, n+1):
        for j in range(1,space+1):
            print('\t', end='')
        for j in range(1, pattern_size+1):
            print(num,'\t\t', end='')
        if i<mid:
            num +=1
            space -=1
            pattern_size +=1
        else :
            num -=1
            space +=1
            pattern_size -=1
        print()

n = int(input("Enter no. of row: "))
print_pattern(n)