'''
Enter no. of row: 7
      1   
    1   0   
  1   0   1   
1   0   1   0   
  1   0   1   
    1   0   
      1   
'''

def print_pattern(n):
    if n%2 ==0 :
        print("Odd number only! ")
        return
    pattern_size = 1
    mid = n//2+1
    space = mid-1

    for i in range(1, n+1):
        num = 1
        for j in range(1,space+1):
            print('  ', end='')
        for j in range(1, pattern_size+1):
            print(num%2,'  ', end='')
            num +=1
        if i<mid:
            space -=1
            pattern_size +=1
        else :
            space +=1
            pattern_size -=1
        print()

n = int(input("Enter no. of row: "))
print_pattern(n)