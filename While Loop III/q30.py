n = int(input("Enter a number: "))

if n == 0:
    print("0")
else:
    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2

    print(binary)