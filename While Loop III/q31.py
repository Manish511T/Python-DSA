n = int(input("Enter a number: "))

if n <= 0:
    print("Positive natural number only!!")
else:
    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2

    print(binary)