# WAP to print and count all the numbers
# from 1 to 100 which are perfect square.

count = 1
i = 1

while i*i<=100:
    print(i*i)
    count = i
    i+=1

print('total ',count)