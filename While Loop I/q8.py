# WAP to print all the numbers from 1 to
# 100 which are perfect cube.

i=1
while i<=100: 
    cube_root = round(i**(1/3))
    if cube_root**3 == i:
        print(i)
    i+=1