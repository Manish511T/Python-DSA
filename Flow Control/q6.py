# WAP to take three sides of a triangle and
# print it is equilateral, isosceles or scalene
# triangle or not using if else statement.

s1 = int(input('Enter 1st side of a triangle: '))
s2 = int(input('Enter 2nd side of a triangle: '))
s3 = int(input('Enter 3rd side of a triangle: '))

if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    if s1==s2==s3:
        print("Equilateral")
    elif s1==s2 or s2==s3 or s1==s3:
        print('isosceles')
    else:
        print('scalene')
else:
    print("Triangle is not valid")


