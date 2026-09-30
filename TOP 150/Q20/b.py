'''
WAP to print max and min element of array
'''

arr = eval(input("Enter an array: "))
max = arr[0]
min = arr[0]

for i in range(len(arr)):
    if arr[i]>max:
        max = arr[i]
    elif arr[i]<min:
        min = arr[i]

print(min)
print(max)