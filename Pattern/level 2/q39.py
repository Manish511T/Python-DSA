'''
Enter a number: 7
1  
1  2  
1  2  3  
1  2  3  4  
1  2  3  4  5  
1  2  3  4  5  6  
1  2  3  4  5  6  7  
'''


# def print_pattern(n):
#     num = 1
#     for i in range(1, n+1):
#         for j in range(num):
#             print(num,' ', end='')
#         num +=1
#         print()

def print_pattern(n):
    pattern_size = 1
    for i in range(1, n+1):
        num = 1
        for j in range(1, pattern_size+1):
            print(num,' ',end='')   
            num +=1 
        pattern_size +=1
        
        print()


n = int(input("Enter a number: "))
print_pattern(n)