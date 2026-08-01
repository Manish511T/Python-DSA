'''
Enter a number: 7
*           * 
* *       * * 
* * *   * * * 
* * * * * * * 
* * *   * * * 
* *       * * 
*           * '''


def print_pattern(n):
    start = 1
    end = n
    mid = n//2+1

    for i in range(1, n+1):
        for j in range(1, n+1):
            if j<=start or j>=end:
                print('* ', end='')
            else:
                print('  ', end='')
        print()
        if i<mid:
            start +=1
            end -=1
        else:
            start -=1
            end +=1


n = int(input("Enter a number: "))
print_pattern(n)