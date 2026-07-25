'''
Enter a number: 13
* * * * * * * * * * * * * 
  * * * * * * * * * * * 
    * * * * * * * * * 
      * * * * * * * 
        * * * * * 
          * * * 
            * 
'''



def printPattern(n):
    space = 0
    patternSize = n

    for i in range(1, n+1):
        for j in range(1,space+1):
            print("  ", end='')
        for j in range(1, patternSize+1):
            print('* ', end='')
        space += 1
        patternSize -=2
        print()
        

n = int(input("Enter a number: "))
if n%2==0:
    print("Row must be an odd number!")
else:
    printPattern(n)
