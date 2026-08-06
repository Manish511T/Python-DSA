'''
a) WAJP to swap two numbers using a third
variable.
b) WAJP to swap two numbers without using a
third variable.
'''

# a) WAJP to swap two numbers using a third
# variable.

a = 2
b = 3
print("Before Swape")
print(a)
print(b)
temp = a
a = b
b = temp
print("After Swape")
print(a)
print(b)


# b) WAJP to swap two numbers without using a
# third variable.

print("Before Swape")
print(a)
print(b)

a = a+b
b = a-b
a = a-b
print("After Swape")
print(a)
print(b)
