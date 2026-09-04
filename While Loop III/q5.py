n = int(input("Enter number: "))
digit = 0
biggest = 0
while n>0:
    digit = n%10
    if digit>=biggest:
        biggest = digit
    n //=10

print(biggest)


