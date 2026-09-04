n = int(input("Enter number: "))
digit = 0
biggest = 0
smallest = n%10
diff = 0
while n>0:
    digit = n%10
    if digit>=biggest:
        biggest = digit
    elif digit<=smallest:
        smallest = digit
    diff = biggest-smallest
    n //=10

print(diff)


