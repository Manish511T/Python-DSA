'''
Enter a number: 7
1  
0  0  
1  1  1  
0  0  0  0  
1  1  1  1  1  
0  0  0  0  0  0  
1  1  1  1  1  1  1 
'''


# def print_pattern(n):
#     num = 1
#     for i in range(1, n+1):
#         for j in range(num):
#             print(num%2,' ', end='')
#         num +=1
#         print()

def print_pattern(n):
    pattern_size = 1
    num = 1
    for i in range(1, n+1):
        for j in range(1, pattern_size+1):
            print(num%2, ' ', end='')
        num +=1
        pattern_size+=1
        print()

n = int(input("Enter a number: "))
print_pattern(n)