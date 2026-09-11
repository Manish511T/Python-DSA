n = int(input("Enter a number: "))
max_product = 0
l = []
while n>0:
    digit = n%10
    l.append(digit)
    n //=10
        
for i in range(len(l)):
    for j in range(i+1, len(l)):
        res = l[i]*l[j]
        if res>max_product:
            max_product = res
            
print(max_product)