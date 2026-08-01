'''
Enter a number: 7
* * * * * * * * * * * * * 
* * * * * *   * * * * * * 
* * * * *       * * * * * 
* * * *           * * * * 
* * *               * * * 
* *                   * * 
*                       * 
'''
def print_pattern(n):
    mid = 2*n//2
    start = n
    end = n
    for i in range(1,n+1):
        for j in range(1, n*2):
            if j<=start or j>=end :
                print("* ", end='')
            else:
                print("  ", end='')
        print()
        if i<mid:
            start -=1
            end +=1

n = int(input("Enter a number: "))
if n%2==0:
    print("Enter odd number only!!!")
else:
    print_pattern(n)