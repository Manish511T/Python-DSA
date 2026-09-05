n = int(input("Enter number: "))
rev = 0
while n>0:
    digit = n%10
    rev = rev*10 +digit
    n //=10


while rev>0:
    digit = rev%10
    print(digit)
    rev //=10
