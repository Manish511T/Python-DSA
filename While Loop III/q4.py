n = int(input("Enter number: "))
digit = 0
while n>0:
    digit = n%10
    if digit>=5:
        print(digit)
    n //=10


