# WAP to print all are equal if all have same
# value or print biggest value of three
# numbers using if else statement.


n1 = 20
n2 = 20
n3 = 100
if n1==n2==n3:
    print("All are equal")
elif n1>n2 and n1>n3:
    print(n1," is biggest number")
elif n2>n1 and n2>n3:
    print(n2," is biggest number")
else:
    print(n3," is biggest number")

