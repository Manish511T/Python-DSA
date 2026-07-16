# WAJP to swap two numbers.
# a. With using a third variable
# b. Without using third variable


a = 10
b = 20

# a. With using a third variable
print("question - a")

print("a",a)
print("b",b)
temp = 0
temp=a
a=b
b=temp
print("after swap")
print("a",a)
print("b",b)

# b. Without using third variable
print("question - b")
print("a",a)
print("b",b)
a = a+b
b = a-b
a = a-b
print("after swap")
print("a",a)
print("b",b)