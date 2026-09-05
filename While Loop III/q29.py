n = int(input("Enter a number: "))

if n <= 0:
    print(False)
else:
    while n % 4 == 0:
        n //= 4

    if n == 1:
        print(True)
    else:
        print(False)

