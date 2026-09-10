n = int(input("Enter a binary number: "))

power = 0
decimal = 0
while n>0:
    digit = n%10
    decimal += digit*(2**power)
    power +=1
    n //=10


print(decimal)
