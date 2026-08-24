def print_pattern(n):

    for i in range(1, n+1):
        for j in range(1, n+1):
            if j%2 !=0:
                print((j-1)*n+i, end='\t')
            else:
        
                print(j*n-i+1, end='\t')
        print()

n=int(input("Enter the number of Rows: "))
print_pattern(n)




# n = int(input("Enter the Number of Rows: "))

# num = 1

# for row in range(1, n + 1):

#     for group in range(1, n + 1):
#         if group % 2 != 0:
#             print((group - 1) * n + row, end="\t")
#         else:
#             print(group * n - row + 1, end="\t")

#     print()