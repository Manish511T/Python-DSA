'''
Enter a number: 9
        * 
      * * * 
    *   *   * 
  *     *     * 
* * * * * * * * * 
  *     *     * 
    *   *   * 
      * * * 
        * 
'''


def print_pattern(n):
    mid = n//2+1
    start = mid
    end = mid
    for i in range(1,n+1):
        for j in range(1, end+1):
            if j==start or j==end or j==mid or i==mid:
                print("* ", end='')
            else:
                print("  ", end='')
        print()
        if i<mid:
            start -=1
            end +=1
        else:
            start +=1
            end -=1

n = int(input("Enter a number: "))
if n%2==0:
    print("Enter odd number only!!!")
else:
    print_pattern(n)