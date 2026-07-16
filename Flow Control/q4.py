# WAP to take three angles of a triangle
# from user and print triangle is valid or not
# using if else statement.

a1 = int(input('Enter 1st angle of a triangle: '))
a2 = int(input('Enter 2nd angle of a triangle: '))
a3 = int(input('Enter 3rd angle of a triangle: '))

if a1 > 0 and a2 > 0 and a3 > 0 and a1+a2+a3 == 180:
    print("Triangle is valid")
else:
    print("Triangle is not valid")