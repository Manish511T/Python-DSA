n = int(input("Enter number: "))
count = 0
temp = n
while temp>0:
    digit = temp%10
    if n%digit ==0:
        count+=1
    temp //=10

print(count)

