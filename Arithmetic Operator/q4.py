# For the given three numbers. 
# Swap 1st into 2nd ,2nd into 3rd and 3rd into 1st number.
# a. With using fourth variable
# b. Without using fourth variable

a = 10
b = 20
c = 30

# a. With using fourth variable
print("question - a")

print("a",a)
print("b",b)
print("c",c)
temp = 0
temp = a
a = c
c = b
b = temp
print("after swap")
print("a",a)
print("b",b)
print("c",c)


# b. Without using fourth variable
print("question - b")

print("a",a)
print("b",b)
print("c",c)
a = a+b+c
b = a - (b+c)
c = a - (b+c)
a = a - (b+c)
print("after swap")
print("a",a)
print("b",b)
print("c",c)