# WAP to print and count all the numbers
# from 1 to 100 which are divisible by 7 or
# ends with 7.

count = 0
i = 1
while i<=100:
    if i%7==0 or i%10==7:
        print(i)
        count +=1
    i+=1

print('Count: ',count)