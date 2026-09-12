n = int(input("Enter a number: "))

if n<10:
    print(n)
else:
    while n>=10:
        total = 0
        while n>0:
            digit = n%10
            total += digit
            n //=10
        n = total
    print(total)

