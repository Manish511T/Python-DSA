# WAP to print and count all the numbers
# from 1 to 1000 which are divisible by 7
# and also ends with 7.

count = 0
i = 1
while i<=1000:
    if i%7==0 and i%10==7:
        print(i)
        count +=1
    i+=1

print('Count: ',count)