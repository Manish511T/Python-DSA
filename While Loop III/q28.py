n = int(input("Enter a number: "))

if n <= 0:
    print(False)
else:
    while n % 3 == 0:
        n //= 3

    if n == 1:
        print(True)
    else:
        print(False)

