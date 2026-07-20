n = int(input("Enter a number: "))
mid = (n//2)+1
if n%2==0:
    print("Enter odd number")
else:
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==mid or j==mid:
                print('*', end=' ')
            else:
                print(" ", end=' ')
        print()