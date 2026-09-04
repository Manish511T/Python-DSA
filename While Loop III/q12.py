n = int(input("Enter number: "))
count = 0
while n>0:
    digit = n%10
    if digit <=5 :
        count +=1
    n //=10

print(count)

