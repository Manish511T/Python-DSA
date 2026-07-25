'''
Enter a number: 7
* * * * * * * 
  * * * * * * 
    * * * * * 
      * * * * 
        * * * 
          * * 
            * 
'''

def printPattern(n):
    space = 0
    patternSize = n

    for i in range(1, n+1):
        for j in range(1,space+1):
            print(" ", end=' ')
        for j in range(1, patternSize+1):
            print('*', end=' ')
        space += 1
        patternSize -=1
        print()
        


n = int(input("Enter a number: "))
printPattern(n)