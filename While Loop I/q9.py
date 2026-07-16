# WAP to print and count all the numbers
# from 1 to 100 which are perfect cube.
count = 0
i = 1
while i<=100:
    cube_root = round(i**(1/3))
    if cube_root**3 == i:
        print(i)
        count +=1
    i +=1
    
print('count: ',count)