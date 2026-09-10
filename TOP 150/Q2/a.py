def triangles(nums):
    a,b,c = nums

    if a+b<=c or b+c<=a or c+a<=b:
        print('none')
    elif a==b==c:
        print('equilateral')
    elif a==b or b==c or c==a:
        print('isosceles')
    else:
        print('scalene')

nums = eval(input("Enter 3 number in list: "))
triangles(nums)