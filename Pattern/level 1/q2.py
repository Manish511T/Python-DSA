def pattern_print(n):
    for i in range(1, n+1):
        for j in range(1,n+1):
            # print(i%2, end=' ') 
            '''
            1 1 1 1 1 
            0 0 0 0 0 
            1 1 1 1 1 
            0 0 0 0 0 
            1 1 1 1 1 
            '''

            # and
            print((i+1)%2,end=' ')
            '''
            0 0 0 0 0 
            1 1 1 1 1 
            0 0 0 0 0 
            1 1 1 1 1 
            0 0 0 0 0 
            '''

        print()

n=int(input("Enter a number: "))
pattern_print(n)