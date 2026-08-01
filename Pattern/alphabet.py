def print_pattern(n):
    pattern_size = 1
    space = n-1
    for i in range(1, n+1):
        for j in range(1, space+1):
            print('   ', end='')
        for j in range(1, pattern_size+1):
            print(chr(j+64),' ', end='')
        print()
        space-=1
        pattern_size +=2
        print()

n = int(input("Enter a number: "))
print_pattern(n)