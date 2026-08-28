def print_pattern(n):
    if n%2==0:
        print("odd number only!")
        return
    
    mid = n//2+1
    startspace = mid-1
    startpattern_size = 1
    endpattern_size = 5*n//2+1
    for i in range(1, n+1):
        # pattern 1
        for j in range(1, startspace+1):
            print('  ', end='')
        for j in range(1, startpattern_size+1):
            print('* ', end='')

        # Pattern 2

        for j in range(mid+1, n+2):
            if (i==1 or j==n+1) and i<=mid :
                print('@ ', end='') 
            else:
                print('  ', end='')

        # Pattern 3
        for j in range(n+2, 2*n):
            if i>mid:
                print('* ', end='')
            else:
                print('  ', end='')

        #Pattern 4
        for j in range(2*n, 2*n+mid):
            if (j==2*n or i==1) and i<=mid:
                print('@ ', end='')
            else:
                print('  ', end='')   

        #Pattern 5
        for j in range(5*n//2+1, endpattern_size+1):
            print('* ', end='')

        print()
        if i<mid:
            startpattern_size +=1
            startspace -=1
            endpattern_size +=1
        else:
            startpattern_size -=1
            startspace +=1
            endpattern_size -=1


n = int(input("Enter the number of Rows: "))
print_pattern(n)